from tests4py.api.config import config_set
from tests4py.api.report import ConfigReport


def tests4py_config_set(name: str, value: bool):
    report = ConfigReport()
    return config_set(name, value, report)
