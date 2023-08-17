from tests4py.api.config import load_config
from tests4py.api.report import ConfigReport


def tests4py_config_set(name: str, value: bool):
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
