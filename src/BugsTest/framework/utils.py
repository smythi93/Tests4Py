import logging
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple

from BugsTest import projects
from BugsTest.projects import Project, ansible, pysnooper

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
DEFAULT_UNITTESTS_DIVERSITY_PATH = 'bugstest_unittests_diversity.py'
DEFAULT_SYSTEMTESTS_DIVERSITY_PATH = 'bugstest_systemtest_diversity'

LOGGER = logging.getLogger('BugsTest')
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s :: %(levelname)-8s :: %(message)s',
)

VERSION_PATTERN = re.compile(r'Installed Python-(?P<v>\d+.\d+.\d+)')
PYTEST_PATTERN = re.compile(rb'= ((((?P<f>\d+) failed)|((?P<p>\d+) passed)|(\d+ warnings?))(, )?)+ in ')
UNITTEST_TOTAL_PATTERN = re.compile(rb'Ran (?P<t>\d+) tests? in')
UNITTEST_FAILED_PATTERN = re.compile(rb'FAILED (failures=(?P<f>\d+))')

SYSTEMTESTS_FAILING_CLASS = 'TestsFailing'
SYSTEMTESTS_PASSING_CLASS = 'TestsPassing'


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


class GenerateReport(TestingReport):

    def __init__(self, command: str, subcommand: str = None):
        self.varify_passing: Optional[int] = None
        self.varify_failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)


def __setup__():
    # TODO setup all projects
    LOGGER.info('Loading projects')
    ansible.register()
    pysnooper.register()


def __env_on__(project: Project, verbose=True):
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


def __source__(script):
    output = subprocess.check_output(f'. {script}; env', shell=True).decode('utf-8')
    env = dict()
    for line in output.splitlines():
        key, value = line.split('=', 1)
        env[key] = value
    os.environ.update(env)


def __activating_venv__(env_dir: Path, verbose=True):
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    LOGGER.info('Activating virtual env')

    if (env_dir / 'Scripts').exists():
        __source__(env_dir / 'Scripts' / 'activate')
    else:
        try:
            subprocess.check_call(['dos2unix', '--version'])
        except OSError:
            raise ValueError(f'Please install dos2unix (sudo apt-get dos2unix)')
        __source__(env_dir / 'bin' / 'activate')


def __deactivating_venv__(verbose=True):
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    LOGGER.info('Deactivating virtual env')
    __source__('deactivate')


def __get_project__(work_dir: Path) -> Tuple[Project, Path, Path, Path]:
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

    __setup__()
    return projects.load_bug_info(bugstest_info), bugstest_info, bugstest_requirements, bugstest_setup


def __get_pytest_result__(output: bytes) -> tuple[bool, int, int, int] | tuple[bool, None, None, None]:
    match = PYTEST_PATTERN.search(output)
    if match:
        if match.group('f'):
            failing = int(match.group('f'))
        else:
            failing = 0
        if match.group('p'):
            passing = int(match.group('p'))
        else:
            passing = 0
        return True, failing + passing, failing, passing
    return False, None, None, None
