import os
from pathlib import Path
from typing import Optional, Tuple, List
from xml.etree import ElementTree

from tests4py import projects
from tests4py.constants import (
    INFO_FILE,
    REQUIREMENTS_FILE,
    PYTEST_PATTERN,
    NEWLINE_TOKEN,
)
from tests4py.logger import LOGGER
from tests4py.projects import (
    Project,
    ansible,
    black,
    cookiecutter,
    fastapi,
    httpie,
    keras,
    luigi,
    matplotlib,
    pandas,
    pysnooper,
    sanic,
    scrapy,
    spacy,
    thefuck,
    tornado,
    tqdm,
    youtubedl,
    TestingFramework,
    middle,
    markup,
    calculator,
    expression,
)
from tests4py.tests.utils import TestResult


def setup():
    LOGGER.info("Loading projects")
    ansible.register()
    black.register()
    calculator.register()
    cookiecutter.register()
    expression.register()
    fastapi.register()
    httpie.register()
    keras.register()
    luigi.register()
    markup.register()
    matplotlib.register()
    middle.register()
    pandas.register()
    pysnooper.register()
    sanic.register()
    scrapy.register()
    spacy.register()
    thefuck.register()
    tornado.register()
    tqdm.register()
    youtubedl.register()


def load_project(work_dir: Path) -> Tuple[Project, Path, Path]:
    LOGGER.info(f"Checking whether Tests4Py project")
    tests4py_info = work_dir / INFO_FILE
    tests4py_requirements = work_dir / REQUIREMENTS_FILE
    if not tests4py_info.exists():
        raise ValueError(f"No Tests4Py project found in {work_dir}, no tests4py_info")
    elif not tests4py_requirements.exists():
        raise ValueError(
            f"No Tests4Py project found in {work_dir}, no tests4py_requirements"
        )

    setup()
    return projects.load_bug_info(tests4py_info), tests4py_info, tests4py_requirements


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
