import json
import os
from pathlib import Path
from typing import Optional

from tests4py.api.report import ConfigReport
from tests4py.constants import GLOBAL_CONFIG_FILE, GLOBAL_CONFIGS, GLOBAL_PROJECTS


class GlobalConfig:
    def __init__(
        self,
        cache: Optional[bool] = None,
        last_workdir: Optional[os.PathLike] = None,
        mode: Optional[str] = None,
    ):
        self.cache: bool = bool(cache)
        self.last_workdir: Optional[Path] = (
            None if last_workdir is None else Path(last_workdir)
        )
        # Execution backend. "pyenv" (default) builds/runs subjects directly on the
        # host via pyenv virtualenvs. "docker" is the optional containerised backend
        # (see tests4py.api.docker / `t4p docker`). Unknown values fall back to pyenv.
        self.mode: str = mode if mode in ("pyenv", "docker") else "pyenv"

    @staticmethod
    def load():
        with open(GLOBAL_CONFIG_FILE, "r") as fp:
            json_dict = json.loads(fp.read() or "{}")
        return GlobalConfig(**json_dict)

    def write(self):
        with open(GLOBAL_CONFIG_FILE, "w") as fp:
            json.dump(self.__dict__, fp, default=str)


def load_config() -> GlobalConfig:
    os.makedirs(GLOBAL_CONFIGS, exist_ok=True)
    if os.path.exists(GLOBAL_CONFIG_FILE):
        config = GlobalConfig.load()
    else:
        config = GlobalConfig()
        config.write()
    os.makedirs(GLOBAL_PROJECTS, exist_ok=True)
    return config


def config_set(name: str, value: bool, report: Optional[ConfigReport] = None):
    if report is None:
        report = ConfigReport()
    try:
        config = load_config()
        if hasattr(config, name):
            setattr(config, name, value)
        else:
            raise AttributeError(f"Config has no attribute {name}")
        config.write()
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
