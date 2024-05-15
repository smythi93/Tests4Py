"""
This module provides the API for the global configuration of the Tests4Py package.
"""

import json
import os
from pathlib import Path
from typing import Optional

from tests4py.api.report import ConfigReport
from tests4py.constants import GLOBAL_CONFIG_FILE, GLOBAL_CONFIGS, GLOBAL_PROJECTS


class GlobalConfig:
    """
    The global configuration of the Tests4Py package.
    """

    def __init__(
        self, cache: Optional[bool] = None, last_workdir: Optional[os.PathLike] = None
    ):
        """
        Initialize the global configuration.
        :param Optional[bool] cache: The cache flag, which enables the caching of virtual environments and project
        sources.
        :param Optional[os.PathLike] last_workdir: The last working directory used by the package.
        """
        self.cache: bool = bool(cache)
        self.last_workdir: Optional[Path] = (
            None if last_workdir is None else Path(last_workdir)
        )

    @staticmethod
    def load() -> "GlobalConfig":
        """
        Load the global configuration from the global configuration file.
        :return GlobalConfig: The global configuration.
        """
        with open(GLOBAL_CONFIG_FILE, "r") as fp:
            json_dict = json.loads(fp.read() or "{}")
        return GlobalConfig(**json_dict)

    def write(self):
        """
        Write the global configuration to the global configuration file.
        :return None:
        """
        with open(GLOBAL_CONFIG_FILE, "w") as fp:
            json.dump(self.__dict__, fp, default=str)


def load_config() -> GlobalConfig:
    """
    Load the global configuration.
    :return GlobalConfig: The global configuration.
    """
    os.makedirs(GLOBAL_CONFIGS, exist_ok=True)
    if os.path.exists(GLOBAL_CONFIG_FILE):
        config = GlobalConfig.load()
    else:
        config = GlobalConfig()
        config.write()
    os.makedirs(GLOBAL_PROJECTS, exist_ok=True)
    return config


def config_set(
    name: str, value: bool, report: Optional[ConfigReport] = None
) -> ConfigReport:
    """
    Set a configuration flag.
    :param str name: The name of the configuration flag.
    :param bool value: The value of the configuration flag.
    :param Optional[ConfigReport] report: The report for the Tests4Py pipeline.
    :return ConfigReport: The report for the Tests4Py pipeline.
    """
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
