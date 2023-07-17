import json
import logging
import os
import shutil
from pathlib import Path
from typing import Optional, Tuple, List
from xml.etree import ElementTree

from tests4py import projects
from tests4py.constants import (
    INFO_FILE,
    REQUIREMENTS_FILE,
    SETUP_FILE,
    CHECKOUT,
    COMPILE,
    TEST,
    PYTEST_PATTERN,
    INFO,
    GLOBAL_CONFIG_FILE,
    GLOBAL_CONFIGS,
    GLOBAL_PROJECTS,
    CACHE,
    CONFIG,
    GLOBAL_GIT,
    VENV,
    GRAMMAR,
    NEWLINE_TOKEN,
)
from tests4py.framework.logger import LOGGER
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
)
from tests4py.tests.utils import TestResult


class Report:
    def __init__(self, command: str, subcommand: str = None):
        self.command: str = command
        self.subcommand: Optional[str] = subcommand
        self.successful: Optional[bool] = None
        self.raised: Optional[BaseException] = None

    def to_dict(self):
        dictionary = {
            "command": self.command,
        }
        if self.subcommand:
            dictionary["subcommand"] = self.subcommand
        dictionary["successful"] = self.successful
        if not self.successful and self.raised:
            dictionary["raised"] = getattr(self.raised, "message", repr(self.raised))
        return dictionary

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return self.__repr__()


class ProjectReport(Report):
    def __init__(self, command: str, subcommand: str = None):
        self.project: Optional[Project] = None
        super().__init__(command, subcommand=subcommand)

    def to_dict(self):
        dictionary = super().to_dict()
        if self.project:
            dictionary["project"] = f"{self.project.project_name}_{self.project.bug_id}"
        return dictionary


class CheckoutReport(ProjectReport):
    def __init__(self):
        super().__init__(CHECKOUT)


class CompileReport(ProjectReport):
    def __init__(self):
        super().__init__(COMPILE)


class InfoReport(ProjectReport):
    def __init__(self):
        super().__init__(INFO)
        self.example = False

    def to_dict(self):
        dictionary = super().to_dict()
        if self.example:
            dictionary["project"] = self.project.project_name
        return dictionary


class TestingReport(ProjectReport):
    def __init__(self, command: str, subcommand: str = None):
        self.total: Optional[int] = None
        self.passing: Optional[int] = None
        self.failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)


class TestReport(TestingReport):
    def __init__(self):
        super().__init__(TEST)
        self.results: Optional[List[Tuple[str, TestResult]]] = None


class CacheReport(Report):
    def __init__(self):
        super().__init__(CACHE)
        self.checkout_reports = dict()
        self.compile_reports = dict()


class ConfigReport(Report):
    def __init__(self):
        super().__init__(CONFIG)


class GrammarReport(ProjectReport):
    def __init__(self):
        super().__init__(GRAMMAR)


class GenerateReport(TestingReport):
    def __init__(self, command: str, subcommand: str = None):
        self.verify_passing: Optional[int] = None
        self.verify_failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)


def __setup__():
    LOGGER.info("Loading projects")
    ansible.register()
    black.register()
    cookiecutter.register()
    fastapi.register()
    httpie.register()
    keras.register()
    luigi.register()
    matplotlib.register()
    pandas.register()
    pysnooper.register()
    sanic.register()
    scrapy.register()
    spacy.register()
    thefuck.register()
    tornado.register()
    tqdm.register()
    youtubedl.register()


def __get_project__(work_dir: Path) -> Tuple[Project, Path, Path, Path]:
    LOGGER.info(f"Entering dir {work_dir}")
    os.chdir(work_dir)

    LOGGER.info(f"Checking whether Tests4Py project")
    tests4py_info = work_dir / INFO_FILE
    tests4py_requirements = work_dir / REQUIREMENTS_FILE
    tests4py_setup = work_dir / SETUP_FILE
    if not tests4py_info.exists():
        raise ValueError(f"No Tests4Py project found in {work_dir}, no tests4py_info")
    elif not tests4py_requirements.exists():
        raise ValueError(
            f"No Tests4Py project found in {work_dir}, no tests4py_requirements"
        )

    __setup__()
    return (
        projects.load_bug_info(tests4py_info),
        tests4py_info,
        tests4py_requirements,
        tests4py_setup,
    )


def __get_pytest_result__(
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


def __replace_important_in_test_report__(s: str):
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


def __get_test_results__(
    project: Project, working_directory: os.PathLike, report_file: os.PathLike
) -> List[Tuple[str, TestResult]]:
    test_results = list()
    is_unittest_ = project.testing_framework == TestingFramework.UNITTEST
    try:
        with open(report_file, "r") as fp:
            s = fp.read()
        tree = ElementTree.fromstring(__replace_important_in_test_report__(s))
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


def __init_logger__(verbose=True):
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)


class GlobalConfig:
    def __init__(self, cache: bool = None):
        self.cache: bool = bool(cache)

    @staticmethod
    def load():
        with open(GLOBAL_CONFIG_FILE, "r") as fp:
            json_dict = json.loads(fp.read() or "{}")
        return GlobalConfig(**json_dict)

    def write(self):
        with open(GLOBAL_CONFIG_FILE, "w") as fp:
            json.dump(self.__dict__, fp)


def load_config() -> GlobalConfig:
    os.makedirs(GLOBAL_CONFIGS, exist_ok=True)
    if os.path.exists(GLOBAL_CONFIG_FILE):
        config = GlobalConfig.load()
    else:
        config = GlobalConfig()
        config.write()
    os.makedirs(GLOBAL_PROJECTS, exist_ok=True)
    return config


def check_cache_exists_project(project: Project):
    return (GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT).exists()


def copy_cached_project(project: Project, dst: Path):
    shutil.rmtree(dst, ignore_errors=True)
    return shutil.copytree(
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT,
        dst,
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )


def cache_project(project: Project, src: Path):
    shutil.rmtree(
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT, ignore_errors=True
    )
    return shutil.copytree(
        src,
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT,
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )


def check_cache_exists_env(project: Project):
    return (GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}").exists()


def copy_cached_env(project: Project, dst: Path):
    shutil.rmtree(dst / VENV, ignore_errors=True)
    return shutil.copytree(
        GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}",
        dst / VENV,
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )


def cache_venv(project: Project, src: Path):
    shutil.rmtree(
        GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}",
        ignore_errors=True,
    )
    return shutil.copytree(
        src / VENV,
        GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}",
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )
