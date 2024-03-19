import importlib.resources
import os
import shutil
import subprocess
from pathlib import Path
from typing import List, Union, Optional

from tabulate import tabulate

from tests4py.api.cache import (
    check_cache_exists,
    copy_cached,
    cache,
    check_cache_exists_env,
    copy_cached_env,
    cache_venv,
)
from tests4py.api.config import load_config
from tests4py.api.report import CheckoutReport, CompileReport, InfoReport, TestReport
from tests4py.api.test import get_pytest_result, get_test_results
from tests4py.api.utils import get_work_dir, load_project
from tests4py.constants import (
    DEFAULT_WORK_DIR,
    FIX_FILES,
    INFO_FILE,
    REQUIREMENTS_FILE,
    HARNESS_FILE,
    PATCH_FILE,
    EXPLANATION_FILE,
    DEFAULT_UNITTESTS_DIVERSITY_PATH,
    DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
    UNITTEST_TOTAL_PATTERN,
    UNITTEST_FAILED_PATTERN,
    GLOBAL_PROJECTS,
    PYENV_EXISTS,
    PYTHON,
)
from tests4py.environment import (
    env_on,
    create_venv,
    activate_venv,
    update_env,
    sflkit_env,
    install_pyenv,
)
from tests4py.logger import LOGGER
from tests4py.projects import (
    resources,
    TestingFramework,
    get_number_of_bugs,
    get_project_names,
    TestStatus,
    Project,
    Status,
    get_project,
    get_matching_projects,
)


def checkout(
    project: Project | str,
    work_dir: Path = DEFAULT_WORK_DIR,
    update: bool = False,
    force: bool = False,
    report: Optional[CheckoutReport] = None,
    verbose: bool = False,
) -> CheckoutReport:
    """
    Performs the checkout operation for the given project.

    Args:
        project (Project | str): The project to be checked out.
        work_dir (Path): The working directory for the checkout operation. Defaults to DEFAULT_WORK_DIR.
        update (bool): Indicates whether to update the project. Defaults to False.
        force (bool): Indicates whether to force the checkout. Defaults to False.
        report (Optional[CheckoutReport]): The checkout report. Defaults to None.
        verbose (bool): Indicates whether to display verbose output. Defaults to False.

    Returns:
        CheckoutReport: The report of the checkout operation.
    """
    if report is None:
        report = CheckoutReport()
    config = load_config()
    try:
        if isinstance(project, str):
            matching_projects = get_matching_projects(project)
            if matching_projects:
                project = matching_projects[0]
            else:
                raise ValueError(f"Project {project} not found")
        report.project = project

        check_further = project.status is Status.OK

        work_location = work_dir / project.get_identifier()
        report.location = work_location
        if update and work_location.exists():
            project_verify = load_project(work_location, only_project=True)
            project.compiled = project_verify.compiled
        else:
            tmp_location = (work_dir / f"tmp_{project.project_name}").absolute()

            if check_further:
                if force or not config.cache or not check_cache_exists(project):
                    LOGGER.info(
                        f"Cloning {project.github_url} into {work_location}... "
                    )
                    if work_location.exists():
                        shutil.rmtree(work_location, ignore_errors=True)
                    subprocess.run(
                        ["git", "clone", project.github_url, work_location],
                        stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                    )
                    if config.cache:
                        cache(project, work_location)
                else:
                    LOGGER.info(
                        f"Copying {project.github_url} from {GLOBAL_PROJECTS / project.project_name} "
                        f"into {work_location}... "
                    )
                    copy_cached(project, work_location)
            else:
                raise AttributeError("Not status=OK")

            try:
                LOGGER.info(
                    f"Resetting git at {work_location} to {project.fixed_commit_id}"
                )
                subprocess.run(
                    ["git", "reset", "--hard", project.fixed_commit_id],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                    cwd=work_location,
                )

                LOGGER.info(f"Creating tmp location at {tmp_location}")
                os.makedirs(tmp_location, exist_ok=True)

                LOGGER.info(f"Copying required files to {tmp_location}")
                result = subprocess.run(
                    ["git", "show", "--name-only"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=work_location,
                ).stdout.decode("utf-8")
                change_file_all = list()

                for line in result.split("\n"):
                    if line:
                        line_path = work_location / line
                        if line_path.exists() and line_path.is_file():
                            change_file_all.append(f"{line}")
                            if not project.buggy:
                                shutil.copy(
                                    line_path,
                                    tmp_location / line.replace(os.path.sep, "_"),
                                )

                for test_file in project.test_files:
                    if (work_location / test_file).is_dir():
                        shutil.copytree(
                            work_location / test_file,
                            tmp_location / str(test_file).replace(os.path.sep, "_"),
                            dirs_exist_ok=True,
                        )
                    else:
                        shutil.copy(
                            work_location / test_file,
                            tmp_location / str(test_file).replace(os.path.sep, "_"),
                        )

                LOGGER.info(f"Checkout buggy commit id {project.buggy_commit_id}")
                subprocess.run(
                    ["git", "reset", "--hard", project.buggy_commit_id],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                    cwd=work_location,
                )
                subprocess.run(
                    ["git", "clean", "-f", "-d"],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                    cwd=work_location,
                )

                LOGGER.info(f"Copying required files from {tmp_location}")

                for test_file in project.test_files:
                    dest = tmp_location / str(test_file).replace(os.path.sep, "_")
                    if dest.is_dir():
                        shutil.copytree(
                            dest, work_location / test_file, dirs_exist_ok=True
                        )
                    else:
                        shutil.copy(dest, work_location / test_file)

                patch_fix_all = list()
                # Copy other change file from fixed to buggy if version is fixed commit
                for change_file in change_file_all:
                    change_file_path = tmp_location / change_file.replace(
                        os.path.sep, "_"
                    )
                    if change_file_path.exists():
                        patch_fix_all.append(change_file)
                        if not project.buggy:
                            shutil.move(change_file_path, work_location / change_file)

                project.patch(work_location)
            finally:
                shutil.rmtree(tmp_location, ignore_errors=True)

            LOGGER.info(f"Create info file")
            with open(work_location / FIX_FILES, "w") as fp:
                fp.write(";".join(patch_fix_all))

        # Move information about bug to clone project folder
        project.write_bug_info(work_location / INFO_FILE)

        LOGGER.info(f"Copying resources for {project.get_identifier()}")
        project_resources = importlib.resources.files(
            getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}")
        )
        with importlib.resources.as_file(
            project_resources.joinpath(
                "requirements.txt",
            )
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / REQUIREMENTS_FILE)
            else:
                with importlib.resources.as_file(
                    importlib.resources.files(
                        getattr(resources, project.project_name)
                    ).joinpath("requirements.txt")
                ) as default_resource:
                    if default_resource.exists():
                        shutil.copy(default_resource, work_location / REQUIREMENTS_FILE)
        with importlib.resources.as_file(
            project_resources.joinpath("harness.py"),
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / HARNESS_FILE)
            else:
                with importlib.resources.as_file(
                    importlib.resources.files(
                        getattr(resources, project.project_name)
                    ).joinpath("harness.py")
                ) as default_resource:
                    if default_resource.exists():
                        shutil.copy(default_resource, work_location / HARNESS_FILE)

        with importlib.resources.as_file(
            project_resources.joinpath(
                "fix.patch",
            )
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / PATCH_FILE)
        with importlib.resources.as_file(
            project_resources.joinpath(
                "explanation.md",
            )
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / EXPLANATION_FILE)

        if project.unittests:
            with importlib.resources.as_file(
                project_resources.joinpath(
                    "unittests.py",
                )
            ) as resource:
                if resource.exists():
                    shutil.copy(
                        resource, work_location / DEFAULT_UNITTESTS_DIVERSITY_PATH
                    )

        if project.systemtests:
            module = getattr(
                getattr(
                    getattr(resources, project.project_name), f"bug_{project.bug_id}"
                ),
                "systemtests",
            )
            module.TestsPassing().write(
                work_location / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
                grammar=project.grammar,
            )
            module.TestsFailing().write(
                work_location / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
                grammar=project.grammar,
            )
        config.last_workdir = work_location.absolute()
        config.write()
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def build(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    rebuild: bool = False,
    force: bool = False,
    report: Optional[CompileReport] = None,
    sfl: bool = False,
    verbose: bool = False,
) -> CompileReport:
    if not PYENV_EXISTS:
        install_pyenv()
    report = report or CompileReport()
    config = load_config()
    work_dir = get_work_dir(work_dir_or_project)
    report.location = work_dir
    try:
        project, t4p_info, t4p_requirements = load_project(work_dir)
        report.project = project
        if project.compiled and not rebuild:
            LOGGER.info(f"{project} already compiled")
            report.successful = True
            return report
        environ = env_on(project)
        if force or not config.cache or not check_cache_exists_env(project):
            create_venv(work_dir, environ)
            env_exists = False
        else:
            copy_cached_env(project, work_dir)
            env_exists = True

        environ = activate_venv(work_dir, environ)
        report.env = environ

        if not env_exists:
            LOGGER.info("Installing utilities")
            update_env(environ)

            LOGGER.info("Installing requirements")
            subprocess.check_call(
                [PYTHON, "-m", "pip", "install", "-r", t4p_requirements],
                stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                env=environ,
            )

            LOGGER.info("Checking and installing test requirements")
            test_requirements = work_dir / "test_requirements.txt"
            if test_requirements.exists():
                subprocess.check_call(
                    [PYTHON, "-m", "pip", "install", "-r", test_requirements],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                    env=environ,
                )

        if config.cache:
            cache_venv(project, work_dir)

        if sfl:
            sflkit_env(environ)

        LOGGER.info("Run setup")
        for command in project.setup:
            subprocess.check_call(
                command,
                env=environ,
                stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                cwd=work_dir,
            )

        LOGGER.info("Set compiled flag")
        project.compiled = True
        project.write_bug_info(t4p_info)

        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def info(
    project_name: Optional[str] = None,
    bug_id: Optional[int] = None,
    report: Optional[InfoReport] = None,
):
    report = report or InfoReport()
    try:
        if not project_name:
            print("The existing subjects in Tests4Py:")
            print()
            print(
                tabulate(
                    map(lambda p: [p, get_number_of_bugs(p)], get_project_names()),
                    headers=["project", "# bugs"],
                    tablefmt="fancy_grid",
                )
            )
            print()
            print("Set a project to get further information.")
            report.successful = True
            return report
        project_name = project_name.lower()
        if bug_id is None:
            project = get_project(project_name, 1)
            report.example = True
            report.project = project
            description = project.project_name
        else:
            project = get_project(project_name, bug_id)
            report.project = project
            description = f"{project.project_name} with bug id {project.bug_id}"

        data = [
            ("Name", project.project_name),
            ("URL", project.github_url),
            ("Status", project.status),
        ]
        if bug_id is None:
            data.append(("Bugs", get_number_of_bugs(project.project_name)))
        else:
            data += [
                ("ID", project.bug_id),
                ("Python Version", project.python_version),
                ("Python Path", project.python_path),
                ("Buggy Commit", project.buggy_commit_id),
                ("Fixed Commit", project.fixed_commit_id),
                ("Test Files", "\n".join(map(str, project.test_files))),
                ("Test Cases", "\n".join(project.test_cases)),
                ("Unit Tests", project.unittests is not None),
                ("System Tests", project.systemtests is not None),
            ]

        print(f"Information for project {description}:")
        print()
        print(
            tabulate(
                data,
                tablefmt="fancy_grid",
            )
        )
        print()

        if bug_id is not None:
            if project.test_status_buggy == TestStatus.PASSING:
                print("WARNING: The tests do not fail on the buggy commit.")
                print("Hence, this subject is not useful.")
                print()
            if project.test_status_fixed == TestStatus.FAILING:
                print("WARNING: The tests do fail on the fixed commit.")
                print(
                    "The subject could still be used and generated tests and the oracle reveal to correct fault."
                )
                print()

        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def test(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    single_test: Optional[Union[List[str], str]] = None,
    relevant_tests: bool = False,
    all_tests: bool = False,
    xml_output: Optional[Path] = None,
    coverage: bool = False,
    report: Optional[TestReport] = None,
) -> TestReport:
    if report is None:
        report = TestReport()
    work_dir = get_work_dir(work_dir_or_project)
    report.location = work_dir
    try:
        project = load_project(work_dir, only_project=True)
        report.project = project
        if not project.compiled:
            raise ValueError(
                f"Project {project.project_name} at {work_dir} was not compiled"
            )

        if project.buggy and project.test_status_buggy == TestStatus.PASSING:
            LOGGER.warning(
                f"The tests will pass on this buggy version {project.get_identifier()}"
            )
        elif not project.buggy and project.test_status_fixed == TestStatus.FAILING:
            LOGGER.warning(
                f"The tests will fail on this fixed version {project.get_identifier()}"
            )

        environ = env_on(project)
        environ = activate_venv(work_dir, environ)

        command = [PYTHON, "-m"]

        if coverage:
            subprocess.run(
                [PYTHON, "-m", "pip", "install", "coverage"], env=environ, cwd=work_dir
            )
            command += ["coverage", "run", "-m"]

        if project.testing_framework == TestingFramework.PYTEST:
            command.append(TestingFramework.PYTEST.value)
            command.append(f"--rootdir={work_dir}")
            if xml_output:
                command.append(f"--junit-xml={xml_output.absolute()}")
        elif project.testing_framework == TestingFramework.UNITTEST:
            if xml_output:
                subprocess.run(
                    [PYTHON, "-m", "pip", "install", "unittest-xml-reporting"],
                    env=environ,
                    cwd=work_dir,
                )
                command += ["xmlrunner", "--output-file", xml_output.absolute()]
            else:
                command.append(TestingFramework.UNITTEST.value)
        else:
            raise NotImplementedError(
                f"No command found for {project.testing_framework.value}"
            )
        if not relevant_tests and not all_tests and not single_test:
            LOGGER.info(f"Run relevant tests {project.test_cases}")
            command += project.test_cases
        elif all_tests:
            if project.test_base:
                command.append(project.test_base)
        elif relevant_tests:
            command += project.relevant_test_files
        elif single_test:
            if isinstance(single_test, str):
                command.append(single_test)
            else:
                command += single_test

        LOGGER.info(f"Run tests with command {command}")
        output = subprocess.run(
            command, stdout=subprocess.PIPE, env=environ, cwd=work_dir
        ).stdout
        LOGGER.info(output.decode("utf-8"))

        successful = False
        if project.testing_framework == TestingFramework.PYTEST:
            (
                successful,
                report.total,
                report.failing,
                report.passing,
            ) = get_pytest_result(output)
        elif project.testing_framework == TestingFramework.UNITTEST:
            number_match = UNITTEST_TOTAL_PATTERN.search(output)
            failed_match = UNITTEST_FAILED_PATTERN.search(output)
            if number_match:
                report.total = int(number_match.group("n"))
            if failed_match:
                report.failing = int(number_match.group("f"))
            if number_match and failed_match:
                report.passing = report.total - report.failing
                successful = True
        else:
            raise NotImplementedError(
                f"No command found for {project.testing_framework.value}"
            )

        if xml_output:
            report.results = get_test_results(project, work_dir, xml_output)
        LOGGER.info(f"Ran {report.total} tests")
        LOGGER.info(f"{report.passing} passed --- {report.failing} failed")
        report.successful = successful
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
