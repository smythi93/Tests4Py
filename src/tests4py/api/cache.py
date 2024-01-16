import shutil
from pathlib import Path

from tests4py.constants import GLOBAL_PROJECTS, GLOBAL_GIT, VENV
from tests4py.projects import Project


def check_cache_exists(project: Project):
    return (GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT).exists()


def copy_cached(project: Project, dst: Path):
    shutil.rmtree(dst, ignore_errors=True)
    return shutil.copytree(
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT,
        dst,
        dirs_exist_ok=True,
        copy_function=shutil.copy,
    )


def cache(project: Project, src: Path):
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


def clear_project(project: Project):
    shutil.rmtree(
        GLOBAL_PROJECTS / project.project_name / GLOBAL_GIT,
        ignore_errors=True,
    )


def clear_venv(project: Project):
    shutil.rmtree(
        GLOBAL_PROJECTS / project.project_name / f"venv_{project.bug_id}",
        ignore_errors=True,
    )
