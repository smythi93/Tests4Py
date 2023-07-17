from pathlib import Path

from tests4py import projects, api
from tests4py.constants import (
    DEFAULT_WORK_DIR,
)
from tests4py.framework.logger import LOGGER
from tests4py.framework.utils import (
    CheckoutReport,
    __setup__,
    CompileReport,
    TestReport,
    __init_logger__,
    InfoReport,
)


def tests4py_checkout(
    project_name: str,
    bug_id: int,
    fixed: bool = False,
    work_dir: Path = DEFAULT_WORK_DIR,
    update: bool = False,
    force: bool = False,
    verbose=True,
) -> CheckoutReport:
    report = CheckoutReport()
    __init_logger__(verbose=verbose)

    try:
        if not project_name:
            raise AttributeError("Please input project name")
        if bug_id is None:
            raise AttributeError("Please input bug id")
        if fixed is None or fixed not in (True, False):
            fixed = False
        if not work_dir:
            work_dir = DEFAULT_WORK_DIR
        project_name = project_name.lower()
        LOGGER.info(f"PROJECT_NAME: {project_name}")
        LOGGER.info(f"BUG_ID: {bug_id}")
        LOGGER.info(f"FIXED: {fixed}")
        LOGGER.info(f"WORK_DIR: {work_dir}")

        __setup__()

        project = projects.get_project(project_name, bug_id)
        if not fixed:
            project.buggy = True
        api.checkout_project(
            project, work_dir=work_dir, update=update, force=force, report=report
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_compile(
    work_dir: Path = None,
    recompile: bool = False,
    force: bool = False,
    verbose: bool = True,
) -> CompileReport:
    report = CompileReport()
    __init_logger__(verbose=verbose)

    if work_dir is None:
        work_dir = Path.cwd()
    try:
        if not work_dir.exists():
            raise IOError(f"{work_dir} does not exist")
        api.compile_project(work_dir, recompile=recompile, force=force, report=report)
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_info(project_name: str = None, bug_id: int = None):
    report = InfoReport()
    try:
        api.info_project(project_name=project_name, bug_id=bug_id, report=report)
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_test(
    work_dir: Path = None,
    single_test: str = None,
    all_tests: bool = False,
    output: Path = None,
    coverage: bool = False,
    verbose=True,
) -> TestReport:
    report = TestReport()
    __init_logger__(verbose=verbose)

    if work_dir is None:
        work_dir = Path.cwd()
    try:
        api.test_project(
            work_dir,
            single_test=single_test,
            all_tests=all_tests,
            xml_output=output,
            coverage=coverage,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
