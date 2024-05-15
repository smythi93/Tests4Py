"""
This module provides functions to cache projects and virtual environments.
"""

import shutil
from pathlib import Path

from tests4py.constants import GLOBAL_PROJECTS, GLOBAL_GIT, VENV
from tests4py.projects import Project


def check_cache_exists(project: Project) -> bool:
    """
    Check if the project is cached.
    :param Project project: The project to check.
    :return bool: True if the project is cached, False otherwise.
    """
    return (GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT).exists()


def copy_cached(project: Project, dst: Path):
    """
    Copy the cached project to the destination.
    :param Project project: The project.
    :param Path dst: The destination to copy the project sources to.
    :return: The return of the shutil.copytree function.
    """
    shutil.rmtree(dst, ignore_errors=True)
    return shutil.copytree(
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT,
        dst,
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )


def cache(project: Project, src: Path):
    """
    Cache the project.
    :param Project project: The project.
    :param Path src: The source of the project to cache from.
    :return: The return of the shutil.copytree function.
    """
    shutil.rmtree(
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT, ignore_errors=True
    )
    return shutil.copytree(
        src,
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT,
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )


def check_cache_exists_env(project: Project) -> bool:
    """
    Check if the virtual environment is cached.
    :param Project project: The project to check.
    :return bool: True if the virtual environment is cached, False otherwise.
    """
    return (GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}").exists()


def copy_cached_env(project: Project, dst: Path):
    """
    Copy the cached virtual environment to the destination.
    :param Project project: The project.
    :param Path dst: The destination to copy the virtual environment to.
    :return: The return of the shutil.copytree function.
    """
    shutil.rmtree(dst / VENV, ignore_errors=True)
    return shutil.copytree(
        GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}",
        dst / VENV,
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )


def cache_venv(project: Project, src: Path):
    """
    Cache the virtual environment for a project.
    :param Project project: The project.
    :param Path src: The source of the virtual environment to cache from.
    :return: The return of the shutil.copytree function.
    """
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


def clear_project(project: Project):
    """
    Clear a project from the cache.
    :param Project project: The project to clear.
    :return None:
    """
    shutil.rmtree(
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT,
        ignore_errors=True,
    )


def clear_venv(project: Project):
    """
    Clear a virtual environment from the cache.
    :param Project project: The project to clear the virtual environment.
    :return None:
    """
    shutil.rmtree(
        GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}",
        ignore_errors=True,
    )
