import json
import os
import subprocess
from pathlib import Path
from typing import Optional, Union, Dict, Tuple, Sequence, List
from xml.etree import ElementTree

from tests4py.api.report import (
    SystemtestGenerateReport,
    SystemtestTestReport,
    UnittestGenerateReport,
    UnittestTestReport,
    RunReport,
    GetTestReport,
)
from tests4py.api.utils import get_work_dir, load_project
from tests4py.constants import (
    DEFAULT_SUB_PATH_SYSTEMTESTS,
    DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
    DEFAULT_SUB_PATH_UNITTESTS,
    PYTHON,
    DEFAULT_UNITTESTS_DIVERSITY_PATH,
    PYTEST_PATTERN,
    NEWLINE_TOKEN,
)
from tests4py.environment import env_on, activate_venv
from tests4py.logger import LOGGER
from tests4py.projects import Project, TestingFramework, resources
from tests4py.tests.utils import TestResult


def run(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    args_or_path: Sequence[str] | Path = None,
    invoke_oracle: bool = False,
    report: Optional[RunReport] = None,
):
    report = report or RunReport()
    try:
        work_dir = get_work_dir(work_dir_or_project)
        project = load_project(work_dir, only_project=True)
        report.project = project

        if project.api is None:
            raise NotImplementedError(
                f"Systemtest execution is not enabled for {project.project_name}_{project.bug_id}"
            )
        if args_or_path is None:
            raise ValueError(
                f"Required input path or str to run {project.project_name}_{project.bug_id}"
            )
        report.input = str(args_or_path)
        environ = env_on(project)
        environ = activate_venv(work_dir, environ)
        if not isinstance(args_or_path, Path):
            args_or_path = [args.replace("\\-", "-") for args in args_or_path]
        result, feedback, stdout, stderr = project.api.run(
            args_or_path, environ, work_dir=work_dir, invoke_oracle=invoke_oracle
        )
        if invoke_oracle:
            LOGGER.info(f"Input was identified as {result}")
        LOGGER.info(f"Output: \n{stdout}")
        LOGGER.info(f"Error: \n{stderr}")
        report.test_result = result
        report.feedback = feedback
        report.stdout = stdout
        report.stderr = stderr
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def get_tests(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    report: Optional[GetTestReport] = None,
    as_strings: bool = False,
):
    report = report or GetTestReport()
    try:
        if work_dir_or_project is not None and isinstance(work_dir_or_project, Project):
            project = work_dir_or_project
        else:
            work_dir = get_work_dir(work_dir_or_project)
            project = load_project(work_dir, only_project=True)
        report.project = project

        if project.systemtests is None or project.api is None:
            raise NotImplementedError(
                f"Systemtests are not enabled for {project.project_name}_{project.bug_id}"
            )
        module = getattr(
            getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}"),
            "systemtests",
        )
        report.passing_tests = (
            list(module.TestsPassing().tests)
            if as_strings
            else list(
                map(
                    project.api.get_test_arguments_from_string,
                    module.TestsPassing().tests,
                )
            )
        )
        report.failing_tests = (
            list(module.TestsFailing().tests)
            if as_strings
            else list(
                map(
                    project.api.get_test_arguments_from_string,
                    module.TestsFailing().tests,
                )
            )
        )
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def _get_systemtest_runs(
    project: Project,
    path: os.PathLike | List[os.PathLike],
    environ: Dict[str, str],
    work_dir: Optional[Path] = None,
) -> Tuple[int, int, int, Dict[str, Tuple[TestResult, str]]]:
    total, passing, failing = 0, 0, 0
    results: Dict[str, Tuple[TestResult, str]] = dict()
    if not isinstance(path, list):
        path = [path]
    for p in path:
        for test, result, feedback in project.api.tests(p, environ, work_dir=work_dir):
            results[str(test)] = (result, feedback)
            if TestResult.PASSING == result:
                passing += 1
            elif TestResult.FAILING == result:
                failing += 1
            total += 1
    return total, passing, failing, results


def systemtest_generate(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    path: Path = None,
    n: int = 1,
    p: Union[int, float] = 1,
    is_only_passing: bool = False,
    is_only_failing: bool = False,
    append: bool = False,
    verify: bool = False,
    report: Optional[SystemtestGenerateReport] = None,
) -> SystemtestGenerateReport:
    report = report or SystemtestGenerateReport()

    work_dir = get_work_dir(work_dir_or_project)

    try:
        project = load_project(work_dir, only_project=True)
        report.project = project

        if project.systemtests is None:
            raise NotImplementedError(
                f"System test generation is not enabled for {project.project_name}_{project.bug_id}"
            )

        if is_only_passing and is_only_failing:
            raise ValueError(
                f"Generate of only passing and failing tests at the same time not possible"
            )

        if path is None:
            path = work_dir / DEFAULT_SUB_PATH_SYSTEMTESTS
        if path.exists() and not path.is_dir():
            raise ValueError(
                f"Generation of system tests is not possible because {path} is a directory"
            )

        if p < 1:
            project.systemtests.failing_probability = p
        else:
            project.systemtests.failing_probability = p / n

        if is_only_passing:
            LOGGER.info(
                f"Generate {n} only passing tests for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.systemtests.generate_only_passing_tests(
                n=n, path=path, append=append
            )
        elif is_only_failing:
            LOGGER.info(
                f"Generate {n} only failing tests for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.systemtests.generate_only_failing_tests(
                n=n, path=path, append=append
            )
        else:
            LOGGER.info(
                f"Generate {n} passing and failing tests with failing probability "
                f"{project.systemtests.failing_probability} for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.systemtests.generate_tests(n=n, path=path, append=append)

        if project.api is not None and result.tests:
            passing_tests = [
                test for test, r in result.tests if r == TestResult.PASSING
            ]
            failing_tests = [
                test for test, r in result.tests if r == TestResult.FAILING
            ]
            report.passing_tests = list(
                map(project.api.get_test_arguments_from_string, passing_tests)
            )
            report.failing_tests = list(
                map(project.api.get_test_arguments_from_string, failing_tests)
            )

        report.passing = result.passing
        report.failing = result.failing
        report.total = n
        if verify:
            environ = env_on(project)
            environ = activate_venv(work_dir, environ)

            (
                _,
                report.verify_passing,
                report.verify_failing,
                report.verify_results,
            ) = _get_systemtest_runs(project, path, environ, work_dir=work_dir)
            LOGGER.info(
                f"Verify: {report.verify_passing} passed --- {report.verify_failing} failed"
            )
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def clean_results(
    results: Dict[str, Tuple[TestResult, str]]
) -> Dict[str, Tuple[str, str]]:
    cleaned_results = dict()
    for test in results:
        result, feedback = results[test]
        cleaned_results[test] = (result.name, feedback)
    return cleaned_results


def systemtest_test(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    path_or_str: os.PathLike | List[os.PathLike] = None,
    diversity: bool = False,
    output: Path = None,
    report: Optional[SystemtestTestReport] = None,
) -> SystemtestTestReport:
    if report is None:
        report = SystemtestTestReport()

    work_dir = get_work_dir(work_dir_or_project)

    try:
        project = load_project(work_dir, only_project=True)
        report.project = project

        if project.api is None:
            raise NotImplementedError(
                f"Systemtest execution is not enabled for {project.project_name}_{project.bug_id}"
            )

        if path_or_str is None and not diversity:
            path_or_str = work_dir / DEFAULT_SUB_PATH_SYSTEMTESTS
        if path_or_str and isinstance(path_or_str, Path) and not path_or_str.exists():
            raise ValueError(
                f"Running of system tests is not possible because {path_or_str} does not exist"
            )

        environ = env_on(project)
        environ = activate_venv(work_dir, environ)

        report.total, report.passing, report.failing = 0, 0, 0
        report.results = dict()

        if path_or_str:
            (
                report.total,
                report.passing,
                report.failing,
                r,
            ) = _get_systemtest_runs(project, path_or_str, environ, work_dir=work_dir)
            report.results.update(r)
        if diversity and (work_dir / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH).exists():
            t, p, f, r = _get_systemtest_runs(
                project,
                work_dir / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
                environ,
                work_dir=work_dir,
            )
            report.total += t
            report.passing += p
            report.failing += f
            report.results.update(r)
        if output:
            with open(output, "w") as output_file:
                json.dump(clean_results(report.results), output_file)
        LOGGER.info(f"Ran {report.total} tests")
        LOGGER.info(f"{report.passing} passed --- {report.failing} failed")
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def unittest_generate(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    path: Path = None,
    n: int = 1,
    p: Union[int, float] = 0.5,
    is_only_passing: bool = False,
    is_only_failing: bool = False,
    append: bool = False,
    verify: bool = False,
    report: Optional[UnittestGenerateReport] = None,
) -> UnittestGenerateReport:
    if report is None:
        report = UnittestTestReport()

    work_dir = get_work_dir(work_dir_or_project)

    try:
        project = load_project(work_dir, only_project=True)
        report.project = project

        if project.unittests is None:
            raise NotImplementedError(
                f"Unittest generation is not enabled for {project.project_name}_{project.bug_id}"
            )

        if is_only_passing and is_only_failing:
            raise ValueError(
                f"Generate of only passing and failing tests at the same time not possible"
            )

        if path is None:
            path = work_dir / DEFAULT_SUB_PATH_UNITTESTS
        if path.exists() and path.is_dir():
            raise ValueError(
                f"Generation of unittest is not possible because {path} is a directory"
            )

        if p < 1:
            project.unittests.failing_probability = p
        else:
            project.unittests.failing_probability = p / n

        if is_only_passing:
            LOGGER.info(
                f"Generate {n} only passing tests for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.unittests.generate_only_passing_tests(
                n=n, path=path, append=append
            )
        elif is_only_failing:
            LOGGER.info(
                f"Generate {n} only failing tests for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.unittests.generate_only_failing_tests(
                n=n, path=path, append=append
            )
        else:
            if n < p:
                raise ValueError(
                    f"Cannot generate {n} tests with a failing probability "
                    f"{project.unittests.failing_probability}>1"
                )
            LOGGER.info(
                f"Generate {n} passing and failing tests with failing probability "
                f"{project.unittests.failing_probability} for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.unittests.generate_tests(n=n, path=path, append=append)

        report.passing = result.passing
        report.failing = result.failing
        report.total = n
        if verify:
            environ = env_on(project)
            environ = activate_venv(work_dir, environ)

            command = [
                PYTHON,
                "-m",
                TestingFramework.PYTEST.value,
                f"--rootdir={work_dir}",
                path,
            ]
            output = subprocess.run(
                command, stdout=subprocess.PIPE, env=environ, cwd=work_dir
            ).stdout
            (
                report.successful,
                _,
                report.verify_failing,
                report.verify_passing,
            ) = get_pytest_result(output)
            LOGGER.info(
                f"Verify: {report.verify_passing} passed --- {report.verify_failing} failed"
            )
        else:
            report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def unittest_test(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    path: Path = None,
    diversity: bool = True,
    output: Path = None,
    report: Optional[UnittestTestReport] = None,
) -> UnittestTestReport:
    if report is None:
        report = UnittestTestReport()
    work_dir = get_work_dir(work_dir_or_project)

    try:
        project = load_project(work_dir, only_project=True)
        report.project = project

        if project.unittests is None:
            raise NotImplementedError(
                f"Unit testing is not enabled for {project.project_name}_{project.bug_id}"
            )

        if path is None and not diversity:
            path = work_dir / DEFAULT_SUB_PATH_UNITTESTS
        if path and path.exists() and path.is_dir():
            raise ValueError(
                f"Running of unittest is not possible because {path} is a directory"
            )

        environ = env_on(project)
        environ = activate_venv(work_dir, environ)

        command = [
            PYTHON,
            "-m",
            TestingFramework.PYTEST.value,
            f"--rootdir={work_dir}",
        ]
        if output:
            command.append(f"--junit-xml={output.absolute()}")
        if diversity and (work_dir / DEFAULT_UNITTESTS_DIVERSITY_PATH).exists():
            command.append(work_dir / DEFAULT_UNITTESTS_DIVERSITY_PATH)
        if path:
            command.append(path)
        output = subprocess.run(
            command, stdout=subprocess.PIPE, env=environ, cwd=work_dir
        ).stdout
        (
            report.successful,
            report.total,
            report.failing,
            report.passing,
        ) = get_pytest_result(output)
        LOGGER.info(f"Ran {report.total} tests")
        LOGGER.info(f"{report.passing} passed --- {report.failing} failed")
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def get_pytest_result(
    output: bytes,
) -> tuple[bool, Optional[int], Optional[int], Optional[int]]:
    match = PYTEST_PATTERN.search(output)
    if match:
        if match.group("f"):
            failing = int(match.group("f"))
        else:
            failing = 0
        if match.group("p"):
            passing = int(match.group("p"))
        else:
            passing = 0
        return True, failing + passing, failing, passing
    return False, None, None, None


def replace_important_in_test_report(s: str):
    important = False
    result = ""
    escaped = False
    while s:
        if not important:
            if s.startswith('name="'):
                result += 'name="'
                s = s[6:]
                important = True
            elif s.startswith('classname="'):
                result += 'classname="'
                s = s[11:]
                important = True
            else:
                result += s[0]
                s = s[1:]
        else:
            if s[0] == "\n":
                result += NEWLINE_TOKEN
                s = s[1:]
            elif s[0] == '"' and not escaped:
                result += '"'
                s = s[1:]
                important = False
            elif s[0] == "\\" and not escaped:
                result += "\\"
                s = s[1:]
                escaped = True
            else:
                result += s[0]
                s = s[1:]
                escaped = False
    return result


def get_test_results(
    project: Project, working_directory: os.PathLike, report_file: os.PathLike
) -> List[Tuple[str, TestResult]]:
    test_results = list()
    is_unittest_ = project.testing_framework == TestingFramework.UNITTEST
    try:
        with open(report_file, "r") as fp:
            s = fp.read()
        tree = ElementTree.fromstring(replace_important_in_test_report(s))
    except FileNotFoundError:
        print("pytest did not generate file")
        return test_results
    except ElementTree.ParseError:
        print("pytest produced empty file")
        return test_results
    for testcase in tree.findall(".//testcase"):
        if is_unittest_:
            test = (
                testcase.get("classname").replace(NEWLINE_TOKEN, "\n")
                + "."
                + testcase.get("name").replace(NEWLINE_TOKEN, "\n")
            )
        else:
            path = testcase.get("classname").replace(NEWLINE_TOKEN, "\n").split(".")
            file = ""
            classes = "::"
            for i in range(1, len(path) + 1):
                file = os.path.join(*path[:i]) + ".py"
                if os.path.exists(os.path.join(working_directory, file)):
                    if len(path[i:]) > 0:
                        classes = "::" + "::".join(path[i:]) + "::"
                    break
            test = file + classes + testcase.get("name").replace(NEWLINE_TOKEN, "\n")
        if testcase.find("failure") is not None or testcase.find("error") is not None:
            test_results.append((test, TestResult.FAILING))
        elif len(list(testcase)) == 0 or (
            (
                len(list(testcase)) == 1
                and (
                    testcase.find("system-out") is not None
                    or testcase.find("system-err") is not None
                )
            )
            or (
                len(list(testcase)) == 2
                and (
                    testcase.find("system-out") is not None
                    and testcase.find("system-err") is not None
                )
            )
        ):
            test_results.append((test, TestResult.PASSING))
        else:
            test_results.append((test, TestResult.UNDEFINED))
    return test_results
