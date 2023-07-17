from tests4py.framework.utils import load_config, ConfigReport


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
