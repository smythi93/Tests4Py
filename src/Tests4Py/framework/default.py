import importlib.resources
import logging
import os
import shutil
import subprocess
from pathlib import Path

from Tests4Py import projects
from Tests4Py.framework.constants import (
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
)
from Tests4Py.framework.environment import (
    __env_on__,
    __create_venv__,
    __activate_venv__,
    __update_env__,
)
from Tests4Py.framework.logger import LOGGER
from Tests4Py.framework.utils import (
    CheckoutReport,
    __setup__,
    __get_project__,
    CompileReport,
    TestReport,
    __get_pytest_result__,
)
from Tests4Py.projects import resources, TestingFramework


def tests4py_checkout(
    project_name: str,
    bug_id: int,
    version_id: int = 1,
    work_dir: Path = DEFAULT_WORK_DIR,
    update: bool = False,
    verbose=True,
) -> CheckoutReport:
    report = CheckoutReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    try:
        if not project_name:
            raise AttributeError("Please input project name")
        if bug_id is None:
            raise AttributeError("Please input bug id")
        if version_id is None or version_id not in (0, 1):
            version_id = 1
        if not work_dir:
            work_dir = DEFAULT_WORK_DIR
        project_name = project_name.lower()
        LOGGER.info(f"PROJECT_NAME: {project_name}")
        LOGGER.info(f"BUG_ID: {bug_id}")
        LOGGER.info(f"VERSION_ID: {version_id}")
        LOGGER.info(f"WORK_DIR: {work_dir}")

        __setup__()

        project = projects.get_project(project_name, bug_id)
        if version_id != 1:
            project.buggy = True
        report.project = project

        check_further = project.status is projects.Status.OK

        work_location = work_dir / f"{project.project_name}_{project.bug_id}"
        if update and work_location.exists():
            project_verify, _, _, _ = __get_project__(work_location)
            version_verify = 1 - int(project_verify.buggy)
            compiled_verify = project_verify.compiled
        else:
            version_verify = 1 - version_id
            compiled_verify = False

        if version_verify != version_id:
            tmp_location = (work_dir / f"tmp_{project_name}").absolute()

            if check_further:
                LOGGER.info(f"Cloning {project.github_url} into {work_location}... ")
                subprocess.run(["git", "clone", project.github_url, work_location])
            else:
                raise AttributeError("Not status=OK")

            current_dir = Path.cwd()
            try:
                LOGGER.info(f"Entering dir {work_location}")
                os.chdir(work_location)

                LOGGER.info(
                    f"Resetting git at {work_location} to {project.fixed_commit_id}"
                )
                subprocess.run(["git", "reset", "--hard", project.fixed_commit_id])

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
                            if version_id == 1:
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
                subprocess.run(["git", "reset", "--hard", project.buggy_commit_id])
                subprocess.run(["git", "clean", "-f", "-d"])

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
                        if version_id == 1:
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

        LOGGER.info(f"Copying resources for {project.project_name}_{project.bug_id}")
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


def tests4py_compile(
    work_dir: Path = None, recompile: bool = False, verbose: bool = True
) -> CompileReport:
    report = CompileReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    if work_dir is None:
        work_dir = Path.cwd()

    current_dir = Path.cwd()
    try:

        if not work_dir.exists():
            raise IOError(f"{work_dir} does not exist")
        project, t4p_info, t4p_requirements, t4p_setup = __get_project__(work_dir)
        report.project = project
        if project.compiled and not recompile:
            LOGGER.info(f"{project} already compiled")
            report.successful = True
            return report
        environ = __env_on__(project, verbose=verbose)
        __create_venv__(work_dir, environ)

        environ = __activate_venv__(work_dir, environ, verbose=verbose)

        LOGGER.info("Installing utilities")
        __update_env__(environ)

        LOGGER.info("Installing requirements")
        subprocess.check_call(
            ["python", "-m", "pip", "install", "-r", t4p_requirements], env=environ
        )

        LOGGER.info("Checking and installing test requirements")
        test_requirements = Path("test_requirements.txt")
        if test_requirements.exists():
            subprocess.check_call(
                ["python", "-m", "pip", "install", "-r", test_requirements], env=environ
            )

        LOGGER.info("Run setup")
        if t4p_setup.exists():
            with open(t4p_setup, "r") as setup_file:
                for line in setup_file:
                    if line:
                        subprocess.check_call(line, shell=True, env=environ)

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


def tests4py_coverage(
    work_dir: str,
    single_test: str = None,
    all_tests: bool = False,
    relevant_tests: bool = True,
):
    pass


def tests4py_fuzz(project_name: str, bug_id: int, work_dir: str):
    if not project_name:
        raise AttributeError("Please input project name")
    if bug_id is None:
        raise AttributeError("Please input bug id")
    pass


def tests4py_info(project_name: str, bug_id: int):
    if not project_name:
        raise AttributeError("Please input project name")
    if bug_id is None:
        raise AttributeError("Please input bug id")
    pass


def tests4py_mutation(
    work_dir: str,
    target: str = None,
    unit_test: str = None,
    relevant_tests: bool = True,
):
    pass


def tests4py_test(
    work_dir: Path = None,
    single_test: str = None,
    all_tests: bool = False,
    output: Path = None,
    verbose=True,
) -> TestReport:
    report = TestReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    if work_dir is None:
        work_dir = Path.cwd()

    current_dir = Path.cwd()
    try:
        project, _, _, _ = __get_project__(work_dir)
        report.project = project
        if not project.compiled:
            raise ValueError(
                f"Project {project.project_name} at {work_dir} was not compiled"
            )

        if project.buggy and project.test_status_buggy == projects.TestStatus.PASSING:
            LOGGER.warning(
                f"The tests will pass on this buggy version {project.project_name}_{project.bug_id}"
            )
        elif (
            not project.buggy
            and project.test_status_fixed == projects.TestStatus.FAILING
        ):
            LOGGER.warning(
                f"The tests will fail on this fixed version {project.project_name}_{project.bug_id}"
            )

        environ = __env_on__(project, verbose=verbose)
        environ = __activate_venv__(work_dir, environ)

        command = ["python", "-m"]

        if project.testing_framework == TestingFramework.PYTEST:
            command.append(TestingFramework.PYTEST.value)
            if output:
                command.append(f"--junit-xml={output.absolute()}")
        elif project.testing_framework == TestingFramework.UNITTEST:
            if output:
                subprocess.run(
                    ["python", "-m", "pip", "install", "unittest-xml-reporting"],
                    env=environ,
                )
                command += ["xmlrunner", "--output-file", output.absolute()]
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
            command.append(single_test)

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
        LOGGER.info(f"Ran {report.total} tests")
        LOGGER.info(f"{report.passing} passed --- {report.failing} failed")
        report.successful = successful
    except BaseException as e:
        report.raised = e
        report.successful = False
    finally:
        os.chdir(current_dir)
    return report
