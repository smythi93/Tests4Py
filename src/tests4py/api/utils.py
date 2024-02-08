import os
from pathlib import Path
from typing import Optional, Union, Tuple

from tests4py import projects
from tests4py.api.config import load_config, GlobalConfig
from tests4py.constants import DEFAULT_WORK_DIR, INFO_FILE, REQUIREMENTS_FILE
from tests4py.logger import LOGGER
from tests4py.projects import (
    Project,
    ansible,
    black,
    calculator,
    cookiecutter,
    expression,
    fastapi,
    httpie,
    keras,
    luigi,
    markup,
    matplotlib,
    middle,
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


def get_work_dir(work_dir_or_project: Optional[Union[os.PathLike, Project]] = None):
    if work_dir_or_project is None:
        config = load_config()
        return get_correct_dir(config)
    elif isinstance(work_dir_or_project, Project):
        return DEFAULT_WORK_DIR / work_dir_or_project.get_identifier()
    else:
        return Path(work_dir_or_project)


def get_correct_dir(config: GlobalConfig):
    current_dir = Path.cwd()
    tests4py_info = current_dir / INFO_FILE
    if tests4py_info.exists():
        return current_dir
    elif config.last_workdir is not None:
        return config.last_workdir
    raise OSError("Cannot identify Tests4Py project in cwd or cached directory")


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


def load_project(
    work_dir: Path, only_project: bool = False
) -> Project | Tuple[Project, Path, Path]:
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
    if only_project:
        return projects.load_bug_info(tests4py_info)
    return projects.load_bug_info(tests4py_info), tests4py_info, tests4py_requirements
