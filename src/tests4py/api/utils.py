"""
Utilities for Tests4Py API
"""

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


def get_work_dir(
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None
) -> Path:
    """
    Get the workdir of a project.

    This function returns the working directory for a given project. If no argument is provided,
    it will load the global configuration and return the directory specified there. If a Project
    instance is provided, it will return the default working directory joined with the project's
    identifier. If a path is provided, it will simply return that path.

    :param Optional[Union[os.PathLike, Project]] work_dir_or_project: The working directory or project. If None, the
    function will load the global configuration and return the directory specified there.
    :return Path: The working directory of the project.
    """
    if work_dir_or_project is None:
        config = load_config()
        return get_correct_dir(config)
    elif isinstance(work_dir_or_project, Project):
        return DEFAULT_WORK_DIR / work_dir_or_project.get_identifier()
    else:
        return Path(work_dir_or_project)


def get_correct_dir(config: GlobalConfig):
    """
    Get the correct directory for the Tests4Py project.

    This function will return the current working directory if the Tests4Py project is found there.
    If the project is not found, it will return the last working directory specified in the global
    configuration. If no last working directory is specified, it will raise an OSError.

    :param GlobalConfig config: The global configuration.
    :return Path: The correct directory for the Tests4Py project.
    """
    current_dir = Path.cwd()
    tests4py_info = current_dir / INFO_FILE
    if tests4py_info.exists():
        return current_dir
    elif config.last_workdir is not None:
        return config.last_workdir
    raise OSError("Cannot identify Tests4Py project in cwd or cached directory")


def setup():
    """
    Set up the Tests4Py API.

    This function will load all the projects and register them in the global namespace.
    :return: None
    """
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
    """
    Load a Tests4Py project from a given working directory.

    This function checks whether a Tests4Py project exists in the provided working directory by looking for the
    tests4py_info and tests4py_requirements files. If these files are not found, it raises a ValueError. If the files
    are found, it sets up the Tests4Py API and loads the project information from the tests4py_info file.

    :param Path work_dir: The working directory where the Tests4Py project is located.
    :param bool only_project: If True, the function will return only the Project object. If False, it will return a
    tuple containing the Project object, the path to the tests4py_info file, and the path to the tests4py_requirements
    file.
    :return Project | Tuple[Project, Path, Path]: The loaded Project object, or a tuple containing the Project object
    and the paths to the tests4py_info and tests4py_requirements files.
    """
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
