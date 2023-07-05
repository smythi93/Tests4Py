import importlib.resources
import os
import shutil
import subprocess
from pathlib import Path
from typing import List, Union

from tabulate import tabulate

from tests4py import projects
from tests4py.constants import (
    DEFAULT_WORK_DIR,
    FIX_FILES,
    INFO_FILE,
    REQUIREMENTS_FILE,
    SETUP_FILE,
    HARNESS_FILE,
    PATCH_FILE,
    EXPLANATION_FILE,
    DEFAULT_UNITTESTS_DIVERSITY_PATH,
    DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
    UNITTEST_TOTAL_PATTERN,
    UNITTEST_FAILED_PATTERN,
    GLOBAL_PROJECTS,
)
from tests4py.framework.environment import (
    __env_on__,
    __create_venv__,
    __activate_venv__,
    __update_env__,
)
from tests4py.framework.logger import LOGGER
from tests4py.framework.utils import (
    CheckoutReport,
    __get_project__,
    CompileReport,
    TestReport,
    __get_pytest_result__,
    InfoReport,
    load_config,
    check_cache_exists_project,
    copy_cached_project,
    cache_project,
    check_cache_exists_env,
    copy_cached_env,
    cache_venv,
    __get_test_results__,
)
from tests4py.projects import (
    resources,
    TestingFramework,
    get_number_of_bugs,
    get_project_names,
    TestStatus,
    Project,
)


def checkout_project(
    project: Project,
    work_dir: Path = DEFAULT_WORK_DIR,
    update: bool = False,
    force: bool = False,
    report: CheckoutReport = None,
    verbose: bool = False,
) -> CheckoutReport:
    if report is None:
        report = CheckoutReport()
    config = load_config()
    try:
        report.project = project

        check_further = project.status is projects.Status.OK

        work_location = work_dir / project.get_identifier()
        if update and work_location.exists():
            project_verify, _, _, _ = __get_project__(work_location)
            version_verify = 1 - int(project_verify.buggy)
            compiled_verify = project_verify.compiled
        else:
            version_verify = int(project.buggy)
            compiled_verify = False

        if version_verify != 1 - int(project.buggy):
            tmp_location = (work_dir / f"tmp_{project.project_name}").absolute()

            if check_further:
                if force or not config.cache or not check_cache_exists_project(project):
                    LOGGER.info(
                        f"Cloning {project.github_url} into {work_location}... "
                    )
                    subprocess.run(
                        ["git", "clone", project.github_url, work_location],
                        stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                    )
                    if config.cache and not check_cache_exists_project(project):
                        cache_project(project, work_location)
                else:
                    LOGGER.info(
                        f"Copying {project.github_url} from {GLOBAL_PROJECTS / project.project_name} "
                        f"into {work_location}... "
                    )
                    copy_cached_project(project, work_location)
            else:
                raise AttributeError("Not status=OK")

            current_dir = Path.cwd()
            try:
                LOGGER.info(f"Entering dir {work_location}")
                os.chdir(work_location)

                LOGGER.info(
                    f"Resetting git at {work_location} to {project.fixed_commit_id}"
                )
                subprocess.run(
                    ["git", "reset", "--hard", project.fixed_commit_id],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                )

                LOGGER.info(f"Creating tmp location at {tmp_location}")
                os.makedirs(tmp_location, exist_ok=True)

                LOGGER.info(f"Copying required files to {tmp_location}")
                result = subprocess.run(
                    ["git", "show", "--name-only"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
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

                for test_file in project.test_file:
                    if test_file.is_dir():
                        shutil.copytree(
                            test_file,
                            tmp_location / str(test_file).replace(os.path.sep, "_"),
                            dirs_exist_ok=True,
                        )
                    else:
                        shutil.copy(
                            test_file,
                            tmp_location / str(test_file).replace(os.path.sep, "_"),
                        )

                LOGGER.info(f"Checkout buggy commit id {project.buggy_commit_id}")
                subprocess.run(
                    ["git", "reset", "--hard", project.buggy_commit_id],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                )
                subprocess.run(
                    ["git", "clean", "-f", "-d"],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                )

                LOGGER.info(f"Copying required files from {tmp_location}")

                for test_file in project.test_file:
                    dest = tmp_location / str(test_file).replace(os.path.sep, "_")
                    if dest.is_dir():
                        shutil.copytree(dest, test_file, dirs_exist_ok=True)
                    else:
                        shutil.copy(dest, test_file)

                patch_fix_all = list()
                # Copy other change file from fixed to buggy if version is fixed commit
                for change_file in change_file_all:
                    change_file_path = tmp_location / change_file.replace(
                        os.path.sep, "_"
                    )
                    if change_file_path.exists():
                        patch_fix_all.append(change_file)
                        if not project.buggy:
                            shutil.move(change_file_path, change_file)
            finally:
                shutil.rmtree(tmp_location, ignore_errors=True)
                os.chdir(current_dir)

            LOGGER.info(f"Create info file")
            with open(work_location / FIX_FILES, "w") as fp:
                fp.write(";".join(patch_fix_all))

        else:
            project.compiled = compiled_verify

        # Move information about bug to clone project folder
        project.write_bug_info(work_location / INFO_FILE)

        LOGGER.info(f"Copying resources for {project.get_identifier()}")
        with importlib.resources.path(
            getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}"),
            "requirements.txt",
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / REQUIREMENTS_FILE)
        with importlib.resources.path(
            getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}"),
            "setup.sh",
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / SETUP_FILE)
        with importlib.resources.path(
            getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}"),
            "harness.py",
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / HARNESS_FILE)
            else:
                with importlib.resources.path(
                    getattr(resources, project.project_name), "harness.py"
                ) as default_resource:
                    if default_resource.exists():
                        shutil.copy(default_resource, work_location / HARNESS_FILE)

        with importlib.resources.path(
            getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}"),
            "fix.patch",
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / PATCH_FILE)
        with importlib.resources.path(
            getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}"),
            "explanation.md",
        ) as resource:
            if resource.exists():
                shutil.copy(resource, work_location / EXPLANATION_FILE)

        if project.unittests:
            with importlib.resources.path(
                getattr(
                    getattr(resources, project.project_name), f"bug_{project.bug_id}"
                ),
                "unittests.py",
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

        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def compile_project(
    work_dir_or_project: Union[Path, Project] = None,
    recompile: bool = False,
    force: bool = False,
    report: CompileReport = None,
    verbose: bool = False,
) -> CompileReport:
    if report is None:
        report = CompileReport()
    config = load_config()
    current_dir = Path.cwd()
    if work_dir_or_project is None:
        work_dir = current_dir
    elif isinstance(work_dir_or_project, Project):
        work_dir = DEFAULT_WORK_DIR / work_dir_or_project.get_identifier()
    else:
        work_dir = work_dir_or_project
    try:
        project, t4p_info, t4p_requirements, t4p_setup = __get_project__(work_dir)
        report.project = project
        if project.compiled and not recompile:
            LOGGER.info(f"{project} already compiled")
            report.successful = True
            return report
        environ = __env_on__(project)
        if force or not config.cache or not check_cache_exists_env(project):
            __create_venv__(work_dir, environ)
            env_exists = False
        else:
            copy_cached_env(project, work_dir)
            env_exists = True

        environ = __activate_venv__(work_dir, environ)

        if not env_exists:
            LOGGER.info("Installing utilities")
            __update_env__(environ)

            LOGGER.info("Installing requirements")
            subprocess.check_call(
                ["python", "-m", "pip", "install", "-r", t4p_requirements],
                stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                env=environ,
            )

            LOGGER.info("Checking and installing test requirements")
            test_requirements = Path("test_requirements.txt")
            if test_requirements.exists():
                subprocess.check_call(
                    ["python", "-m", "pip", "install", "-r", test_requirements],
                    stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                    env=environ,
                )

        LOGGER.info("Run setup")
        if t4p_setup.exists():
            with open(t4p_setup, "r") as setup_file:
                for line in setup_file:
                    if line:
                        subprocess.check_call(
                            line,
                            shell=True,
                            env=environ,
                            stdout=subprocess.STDOUT if verbose else subprocess.DEVNULL,
                        )

        if config.cache:
            cache_venv(project, work_dir)

        LOGGER.info("Set compiled flag")
        project.compiled = True
        project.write_bug_info(t4p_info)

        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    finally:
        os.chdir(current_dir)
    return report


def info_project(
    project_name: str = None, bug_id: int = None, report: InfoReport = None
):
    if report is None:
        report = InfoReport()
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
            project = projects.get_project(project_name, 1)
            report.example = True
            report.project = project
            description = project.project_name
        else:
            project = projects.get_project(project_name, bug_id)
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
                ("Test Files", "\n".join(map(str, project.test_file))),
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


def test_project(
    work_dir_or_project: Union[Path, Project] = None,
    single_test: Union[List[str], str] = None,
    all_tests: bool = False,
    xml_output: Path = None,
    coverage: bool = False,
    report: TestReport = None,
) -> TestReport:
    if report is None:
        report = TestReport()
    current_dir = Path.cwd()
    if work_dir_or_project is None:
        work_dir = current_dir
    elif isinstance(work_dir_or_project, Project):
        work_dir = DEFAULT_WORK_DIR / work_dir_or_project.get_identifier()
    else:
        work_dir = work_dir_or_project
    try:
        project, _, _, _ = __get_project__(work_dir)
        report.project = project
        if not project.compiled:
            raise ValueError(
                f"Project {project.project_name} at {work_dir} was not compiled"
            )

        if project.buggy and project.test_status_buggy == projects.TestStatus.PASSING:
            LOGGER.warning(
                f"The tests will pass on this buggy version {project.get_identifier()}"
            )
        elif (
            not project.buggy
            and project.test_status_fixed == projects.TestStatus.FAILING
        ):
            LOGGER.warning(
                f"The tests will fail on this fixed version {project.get_identifier()}"
            )

        environ = __env_on__(project)
        environ = __activate_venv__(work_dir, environ)

        command = ["python", "-m"]

        if coverage:
            subprocess.run(
                ["python", "-m", "pip", "install", "coverage"],
                env=environ,
            )
            command += ["coverage", "run", "-m"]

        if project.testing_framework == TestingFramework.PYTEST:
            command.append(TestingFramework.PYTEST.value)
            if xml_output:
                command.append(f"--junit-xml={xml_output.absolute()}")
        elif project.testing_framework == TestingFramework.UNITTEST:
            if xml_output:
                subprocess.run(
                    ["python", "-m", "pip", "install", "unittest-xml-reporting"],
                    env=environ,
                )
                command += ["xmlrunner", "--output-file", xml_output.absolute()]
            else:
                command.append(TestingFramework.UNITTEST.value)
        else:
            raise NotImplementedError(
                f"No command found for {project.testing_framework.value}"
            )
        if not all_tests and not single_test:
            LOGGER.info(f"Run relevant tests {project.test_cases}")
            command += project.test_cases
        elif single_test:
            if isinstance(single_test, str):
                command.append(single_test)
            else:
                command += single_test

        LOGGER.info(f"Run tests with command {command}")
        output = subprocess.run(command, stdout=subprocess.PIPE, env=environ).stdout
        LOGGER.info(output.decode("utf-8"))

        successful = False
        if project.testing_framework == TestingFramework.PYTEST:
            (
                successful,
                report.total,
                report.failing,
                report.passing,
            ) = __get_pytest_result__(output)
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
            report.results = __get_test_results__(project, work_dir, xml_output)
        LOGGER.info(f"Ran {report.total} tests")
        LOGGER.info(f"{report.passing} passed --- {report.failing} failed")
        report.successful = successful
    except BaseException as e:
        report.raised = e
        report.successful = False
    finally:
        os.chdir(current_dir)
    return report
