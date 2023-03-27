import os
from pathlib import Path
from typing import Optional, Tuple

from tests4py import projects
from tests4py.framework.constants import (
    INFO_FILE,
    REQUIREMENTS_FILE,
    SETUP_FILE,
    CHECKOUT,
    COMPILE,
    TEST,
    PYTEST_PATTERN,
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
)


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
        raise ValueError(f"No Tests4Py project found int {work_dir}, no tests4py_info")
    elif not tests4py_requirements.exists():
        raise ValueError(
            f"No Tests4Py project found int {work_dir}, no tests4py_requirements"
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
