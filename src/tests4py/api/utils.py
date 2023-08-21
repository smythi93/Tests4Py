from pathlib import Path
from typing import Optional, Union

from tests4py.api.config import load_config, GlobalConfig
from tests4py.constants import DEFAULT_WORK_DIR, INFO_FILE
from tests4py.projects import Project


def get_work_dir(work_dir_or_project: Optional[Union[Path, Project]] = None):
    if work_dir_or_project is None:
        config = load_config()
        return get_correct_dir(config)
    elif isinstance(work_dir_or_project, Project):
        return DEFAULT_WORK_DIR / work_dir_or_project.get_identifier()
    else:
        return work_dir_or_project


def get_correct_dir(config: GlobalConfig):
    current_dir = Path.cwd()
    tests4py_info = current_dir / INFO_FILE
    if tests4py_info.exists():
        return current_dir
    elif config.last_workdir is not None:
        return config.last_workdir
    raise OSError("Cannot identify Tests4Py project in cwd or cached directory")
