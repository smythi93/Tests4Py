import enum
from configparser import ConfigParser
from pathlib import Path
from typing import List, Optional

from fuzzingbook.Grammars import Grammar

from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API

bugs = dict()


class Status(enum.Enum):
    OK = True
    NOT_OK = False


class TestStatus(enum.Enum):
    PASSING = 0  # Indicates passing tests
    FAILING = 1  # Indicates failing tests
    ERROR = 2  # Indicates tests that cannot run because of an error
    WRONG = 3  # Indicates tests that are wrong, i.e., the tests contain the bug, not the program


class TestingFramework(enum.Enum):
    PYTEST = "pytest"
    UNITTEST = "unittest"


class Project:
    def __init__(
        self,
        bug_id: int,
        project_name: str,
        github_url: str,
        status: Status,
        cause: str,
        python_version: str,
        python_path: str,
        buggy_commit_id: str,
        fixed_commit_id: str,
        testing_framework: TestingFramework,
        test_file: List[Path],
        test_cases: List[str],
        darwin_python_version: Optional[str] = None,
        python_fallback_version: Optional[str] = None,
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
        grammar: Optional[Grammar] = None,
    ):
        if project_name not in bugs:
            bugs[project_name] = dict()
        bugs[project_name][bug_id] = self
        self.project_name = project_name
        self.bug_id = bug_id
        self.github_url = github_url
        self.status = status
        self.cause = cause
        self.python_version = python_version
        self.python_path = python_path
        self.buggy_commit_id = buggy_commit_id
        self.fixed_commit_id = fixed_commit_id
        self.testing_framework = testing_framework
        self.test_file = test_file
        self.test_cases = test_cases
        self.darwin_python_version = (
            darwin_python_version
            if darwin_python_version is not None
            else python_version
        )
        self.python_fallback_version = (
            python_fallback_version
            if python_fallback_version is not None
            else (
                darwin_python_version
                if darwin_python_version is not None
                else python_version
            )
        )
        self.test_status_fixed = test_status_fixed
        self.test_status_buggy = test_status_buggy
        self.buggy = False
        self.compiled = False
        self.systemtests = systemtests
        self.unittests = unittests
        self.api = api
        self.grammar = grammar

    def write_bug_info(self, path: Path):
        config = ConfigParser()
        config["info"] = {
            "name": self.project_name,
            "bug_id": self.bug_id,
            "buggy": self.buggy,
            "compiled": self.compiled,
        }
        with open(path, "w") as fp:
            config.write(fp)

    def get_identifier(self):
        return f"{self.project_name}_{self.bug_id}"

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.project_name}_{self.bug_id}_{'buggy' if self.buggy else 'fixed'}"


def get_project(project_name: str, bug_id: int) -> Project:
    global bugs
    try:
        bug = bugs[project_name.lower()]
    except KeyError:
        raise ValueError(f"Project {project_name} not found")
    try:
        project: Project = bug[bug_id]
    except KeyError:
        raise ValueError(f"BugID {bug_id} not found for project {project_name}")
    return project


def get_matching_projects(
    project_name: str = None, bug_id: int = None
) -> List[Project]:
    global bugs
    result = list()
    for current_project_name in bugs:
        for current_bug_id in bugs[current_project_name]:
            if (project_name is None or project_name == current_project_name) and (
                bug_id is None or bug_id == current_bug_id
            ):
                result.append(bugs[current_project_name][current_bug_id])
    return result


def get_number_of_bugs(project_name: str) -> int:
    global bugs
    try:
        bug = bugs[project_name]
    except KeyError:
        raise ValueError(f"Project {project_name} not found")
    return len(bug)


def get_project_names() -> List[str]:
    global bugs
    return list(bugs.keys())


def load_bug_info(path: Path) -> Project:
    config = ConfigParser()
    config.read(path.absolute())
    project = get_project(config["info"]["name"], int(config["info"]["bug_id"]))
    project.buggy = config["info"]["buggy"] == "True"
    project.compiled = config["info"]["compiled"] == "True"
    return project


__all__ = [
    "Status",
    "TestStatus",
    "TestingFramework",
    "Project",
    "get_number_of_bugs",
    "get_project_names",
    "get_matching_projects",
    "load_bug_info",
    "ansible",
    "black",
    "cookiecutter",
    "fastapi",
    "httpie",
    "keras",
    "luigi",
    "matplotlib",
    "pandas",
    "pysnooper",
    "sanic",
    "scrapy",
    "spacy",
    "thefuck",
    "tornado",
    "tqdm",
    "youtubedl",
]
