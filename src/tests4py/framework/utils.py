import json
import logging
import os
import shutil
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
    INFO,
    GLOBAL_CONFIG_FILE,
    GLOBAL_CONFIGS,
    GLOBAL_PROJECTS,
    CACHE,
    CONFIG,
    GLOBAL_GIT,
    VENV,
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


class InfoReport(ProjectReport):
    def __init__(self):
        super().__init__(INFO)
        self.example = False


class TestingReport(ProjectReport):
    def __init__(self, command: str, subcommand: str = None):
        self.total: Optional[int] = None
        self.passing: Optional[int] = None
        self.failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)


class TestReport(TestingReport):
    def __init__(self):
        super().__init__(TEST)


class CacheReport(Report):
    def __init__(self):
        super().__init__(CACHE)
        self.checkout_reports = dict()
        self.compile_reports = dict()


class ConfigReport(Report):
    def __init__(self):
        super().__init__(CONFIG)


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
