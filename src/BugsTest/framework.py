import importlib.resources
import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

from BugsTest import projects
from BugsTest.projects import ansible, pysnooper, resources, Project, TestingFramework

CHECKOUT = 'checkout'
COMPILE = 'compile'
COVERAGE = 'coverage'
FUZZ = 'fuzz'
INFO = 'info'
MUTATION = 'mutation'
TEST = 'test'
UNITTEST = 'unittest'
SYSTEMTEST = 'systemtest'
GENERATE = 'generate'

DEFAULT_WORK_DIR = Path(Path.cwd(), 'tmp').absolute()

LOGGER = logging.getLogger('BugsTest')
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s :: %(levelname)-8s :: %(message)s',
)

VERSION_PATTERN = re.compile(r'Installed Python-(?P<v>\d+.\d+.\d+)')


class Report:

    def __init__(self, command: str, subcommand: str = None):
        self.command: str = command
        self.subcommand: Optional[str] = subcommand
        self.successful: Optional[bool] = None
        self.raised: Optional[BaseException] = None


class ProjectReport(Report):

    def __init__(self, command: str, subcommand: str = None):
        self.project: Optional[Project] = None
        super().__init__(command, subcommand=subcommand)


class CheckoutReport(ProjectReport):

    def __init__(self):
        super().__init__(CHECKOUT)


class CompileReport(ProjectReport):

    def __init__(self):
        super().__init__(COMPILE)


class TestingReport(ProjectReport):

    def __init__(self, command: str, subcommand: str = None):
        self.total: Optional[int] = None
        self.passing: Optional[int] = None
        self.failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)


class TestReport(TestingReport):

    def __init__(self):
        super().__init__(TEST)


def _setup():
    # TODO setup all projects
    LOGGER.info('Loading projects')
    ansible.register()
    pysnooper.register()


def _env_on(project: Project, verbose=True):
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    LOGGER.info(f'Checking for platform {sys.platform}')
    if sys.platform == "darwin":
        v = project.darwin_python_version
    else:
        v = project.python_version
    current_versions = subprocess.check_output(['pyenv', 'versions', '--bare']).decode('utf-8').splitlines()
    if v not in current_versions:
        try:
            LOGGER.info(f'Try to install pyenv python {v}')
            subprocess.check_call(['pyenv', 'install', v])
        except subprocess.CalledProcessError:
            LOGGER.info(f'Failed. Check for best alternative to pyenv python {v}')
            v = '.'.join(project.python_version.split('.')[:-1])
            p, r, s = project.python_version.split('.')[:3]
            s = int(s)
            best_sub_version = None
            for candidate in current_versions:
                cp, cr, cs = candidate.split('.')[:3]
                if cp == p and cr == r:
                    cs = int(cs)
                    if cs >= s and best_sub_version is None or cs < best_sub_version:
                        best_sub_version = cs
            if best_sub_version is not None:
                v = f'{v}.{best_sub_version}'
                LOGGER.info(f'Found alternative to pyenv python {v}')
            else:
                LOGGER.info(f'Failed. Try to install fallback pyenv python {v}')
                output = subprocess.check_output(['pyenv', 'install', v]).decode('utf-8')
                match = VERSION_PATTERN.search(output)
                if match:
                    v = match.group('v')
                    LOGGER.info(f'Found pyenv python {v}')
                else:
                    LOGGER.info(f'Failed. Using current python version instead.')

    os.environ['PATH'] = f'{Path(os.environ["PYENV_ROOT"], "versions", v, "bin")}:' \
                         f'{os.environ["PATH"]}'
    LOGGER.info(f'Check for activated python version')
    output = subprocess.check_output(['python', '--version']).decode('utf-8').replace('\n', '')
    if not output.endswith(v):
        raise OSError(f'Python version {v} not set, because current version is {output}')
    LOGGER.info(f'Using pyenv python {v}')
    subprocess.run(['pip', 'install', '--upgrade', 'pip'])


def _source(script):
    output = subprocess.check_output(f'. {script}; env', shell=True).decode('utf-8')
    env = dict()
    for line in output.splitlines():
        key, value = line.split('=', 1)
        env[key] = value
    os.environ.update(env)


def _activating_venv(env_dir: Path, verbose=True):
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    LOGGER.info('Activating virtual env')

    if (env_dir / 'Scripts').exists():
        _source(env_dir / 'Scripts' / 'activate')
    else:
        try:
            subprocess.check_call(['dos2unix', '--version'])
        except OSError:
            raise ValueError(f'Please install dos2unix (sudo apt-get dos2unix)')
        _source(env_dir / 'bin' / 'activate')


def _deactivating_venv(verbose=True):
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    LOGGER.info('Deactivating virtual env')
    _source('deactivate')


def bugstest_checkout(project_name: str, bug_id: int, version_id: int = 1, work_dir: Path = DEFAULT_WORK_DIR,
                      verbose=True) -> CheckoutReport:
    report = CheckoutReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    try:
        if not project_name:
            raise AttributeError('Please input project name')
        if bug_id is None:
            raise AttributeError('Please input bug id')
        if version_id is None or version_id not in (0, 1):
            version_id = 1
        if not work_dir:
            work_dir = DEFAULT_WORK_DIR
        project_name = project_name.lower()
        LOGGER.info(f'PROJECT_NAME: {project_name}')
        LOGGER.info(f'BUG_ID: {bug_id}')
        LOGGER.info(f'VERSION_ID: {version_id}')
        LOGGER.info(f'WORK_DIR: {work_dir}')

        _setup()

        project = projects.get_project(project_name, bug_id)
        if version_id != 1:
            project.buggy = True
        report.project = project

        check_further = project.status is projects.Status.OK

        work_location = work_dir / f'{project.project_name}_{project.bug_id}'
        tmp_location = (work_dir / 'tmp' / project_name).absolute()

        if check_further:
            LOGGER.info(f'Cloning {project.github_url} into {work_location}... ')
            subprocess.run(['git', 'clone', project.github_url, work_location])
        else:
            raise AttributeError('Not status=OK')

        current_dir = Path.cwd()
        try:
            LOGGER.info(f'Entering dir {work_location}')
            os.chdir(work_location)

            LOGGER.info(f'Resetting git at {work_location} to {project.fixed_commit_id}')
            subprocess.run(['git', 'reset', '--hard', project.fixed_commit_id])

            LOGGER.info(f'Creating tmp location at {tmp_location}')
            os.makedirs(tmp_location, exist_ok=True)

            LOGGER.info(f'Copying required files to {tmp_location}')
            result = subprocess.run(['git', 'show', '--name-only'], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT).stdout.decode('utf-8')
            change_file_all = list()

            for line in result.split('\n'):
                if line:
                    line_path = work_location / line
                    if line_path.exists() and line_path.is_file():
                        change_file_all.append(f'{line}')
                        if version_id == 1:
                            shutil.copy(line_path,
                                        tmp_location / line.replace(os.path.sep, '_'))

            for test_file in project.test_file:
                shutil.copy(test_file,
                            tmp_location / str(test_file).replace(os.path.sep, '_'))

            LOGGER.info(f'Checkout buggy commit id {project.buggy_commit_id}')
            subprocess.run(['git', 'reset', '--hard', project.buggy_commit_id])
            subprocess.run(['git', 'clean', '-f', '-d'])

            LOGGER.info(f'Copying required files from {tmp_location}')

            for test_file in project.test_file:
                shutil.copy(tmp_location / str(test_file).replace(os.path.sep, '_'),
                            test_file)

            patch_fix_all = list()
            # Copy other change file from fixed to buggy if version is fixed commit
            for change_file in change_file_all:
                change_file_path = tmp_location / change_file.replace(os.path.sep, '_')
                if change_file_path.exists():
                    patch_fix_all.append(change_file)
                    if version_id == 1:
                        shutil.move(change_file_path, change_file)
        finally:
            os.chdir(current_dir)

        LOGGER.info(f'Create info file')
        with open(work_location / 'bugstest_patchfile.info', 'w') as fp:
            fp.write(';'.join(patch_fix_all))

        # Move information about bug to clone project folder
        project.write_bug_info(work_location / 'bugstest_info.ini')

        LOGGER.info(f'Copying resources for {project.project_name}_{project.bug_id}')
        with importlib.resources.path(getattr(getattr(resources, project.project_name), f'bug_{project.bug_id}'),
                                      'requirements.txt') as resource:
            shutil.copy(resource, work_location / 'bugstest_requirements.txt')
        with importlib.resources.path(getattr(getattr(resources, project.project_name), f'bug_{project.bug_id}'),
                                      'setup.sh') as resource:
            shutil.copy(resource, work_location / 'bugstest_setup.sh')

        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def bugstest_compile(work_dir: Path = None, verbose: bool = True) -> CompileReport:
    report = CompileReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    try:
        if work_dir is None:
            work_dir = Path.cwd()

        if not work_dir.exists():
            raise IOError(f'{work_dir} does not exist')

        current_dir = Path.cwd()
        try:
            LOGGER.info(f'Entering dir {work_dir}')
            os.chdir(work_dir)

            LOGGER.info(f'Checking whether BugsTest project')
            bugstest_info = work_dir / 'bugstest_info.ini'
            bugstest_requirements = work_dir / 'bugstest_requirements.txt'
            bugstest_setup = work_dir / 'bugstest_setup.sh'
            if not bugstest_info.exists():
                raise ValueError(f'No BugsTest project found int {work_dir}, no bugstest_info')
            elif not bugstest_requirements.exists():
                raise ValueError(f'No BugsTest project found int {work_dir}, no bugstest_requirements')
            elif not bugstest_setup.exists():
                raise ValueError(f'No BugsTest project found int {work_dir}, no bugstest_setup')

            _setup()
            project = projects.load_bug_info(bugstest_info)
            report.project = project
            _env_on(project, verbose=verbose)
            env_dir = Path('env')
            shutil.rmtree(env_dir, ignore_errors=True)

            LOGGER.info('Creating virtual env')
            subprocess.run(['python', '-m', 'venv', env_dir])

            _activating_venv(env_dir)
            if sys.platform not in ('win32', 'cygwin'):
                subprocess.run(['dos2unix', bugstest_requirements])

            LOGGER.info('Installing utilities')
            subprocess.check_call(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])
            subprocess.check_call(['python', '-m', 'pip', 'install', '--upgrade', 'setuptools'])
            subprocess.check_call(['python', '-m', 'pip', 'install', 'wheel==0.37.1'])
            subprocess.check_call(['python', '-m', 'pip', 'install', 'pytest==7.0.1'])

            LOGGER.info('Installing requirements')
            subprocess.check_call(['python', '-m', 'pip', 'install', '-r', bugstest_requirements])

            LOGGER.info('Checking and installing test requirements')
            test_requirements = Path('test_requirements.txt')
            if test_requirements.exists():
                subprocess.check_call(['python', '-m', 'pip', 'install', '-r', test_requirements])

            LOGGER.info('Run setup')
            with open(bugstest_setup, 'r') as setup_file:
                for line in setup_file:
                    if line:
                        subprocess.check_call(line, shell=True)

            LOGGER.info('Set compiled flag')
            project.compiled = True
            project.write_bug_info(bugstest_info)

            report.successful = True
        finally:
            _deactivating_venv()
            os.chdir(current_dir)
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def coverage(work_dir: str, single_test: str = None, all_tests: bool = False, relevant_tests: bool = True):
    pass


def fuzz(project_name: str, bug_id: int, work_dir: str):
    if not project_name:
        raise AttributeError('Please input project name')
    if bug_id is None:
        raise AttributeError('Please input bug id')
    pass


def info(project_name: str, bug_id: int):
    if not project_name:
        raise AttributeError('Please input project name')
    if bug_id is None:
        raise AttributeError('Please input bug id')
    pass


def mutation(work_dir: str, target: str = None, unit_test: str = None, relevant_tests: bool = True):
    pass


def bugstest_test(work_dir: Path = None, single_test: str = None, all_tests: bool = False, output: Path = None,
                  verbose=True) -> TestReport:
    report = TestReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    try:
        if work_dir is None:
            work_dir = Path.cwd()

        current_dir = Path.cwd()
        try:
            LOGGER.info(f'Entering dir {work_dir}')
            os.chdir(work_dir)

            LOGGER.info(f'Checking whether BugsTest project')
            bugstest_info = work_dir / 'bugstest_info.ini'
            bugstest_requirements = work_dir / 'bugstest_requirements.txt'
            bugstest_setup = work_dir / 'bugstest_setup.sh'
            if not bugstest_info.exists():
                raise ValueError(f'No BugsTest project found int {work_dir}, no bugstest_info')
            elif not bugstest_requirements.exists():
                raise ValueError(f'No BugsTest project found int {work_dir}, no bugstest_requirements')
            elif not bugstest_setup.exists():
                raise ValueError(f'No BugsTest project found int {work_dir}, no bugstest_setup')

            _setup()
            project = projects.load_bug_info(bugstest_info)
            report.project = project
            if not project.compiled:
                raise ValueError(f'Project {project.project_name} at {work_dir} was not compiled')

            if project.buggy and project.test_status_buggy == projects.TestStatus.PASSING:
                LOGGER.warning(f'The tests will pass on this buggy version {project.project_name}_{project.bug_id}')
            elif not project.buggy and project.test_status_fixed == projects.TestStatus.FAILING:
                LOGGER.warning(f'The tests will fail on this fixed version {project.project_name}_{project.bug_id}')

            _env_on(project, verbose=verbose)
            _activating_venv(Path('env'))

            command = ['python', '-m']

            if project.testing_framework == TestingFramework.PYTEST:
                command.append(TestingFramework.PYTEST.value)
                if output:
                    command.append(f'--junit-xml={output.absolute()}')
            elif project.testing_framework == TestingFramework.UNITTEST:
                if output:
                    subprocess.run(['python', '-m', 'pip', 'install', 'unittest-xml-reporting'])
                    command += ['xmlrunner', '--output-file', output.absolute()]
                else:
                    command.append(TestingFramework.UNITTEST.value)
            else:
                raise NotImplementedError(f'No command found for {project.testing_framework.value}')
            if not all_tests and not single_test:
                LOGGER.info(f'Run relevant tests {project.test_cases}')
                command += project.test_cases
            elif single_test:
                command.append(single_test)

            LOGGER.info(f'Run tests with command {command}')
            # TODO Get number of tests + failing + passing
            subprocess.run(command)

            report.successful = True
        finally:
            _deactivating_venv()
            os.chdir(current_dir)
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report

