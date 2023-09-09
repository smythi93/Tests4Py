from pathlib import Path

from tests4py import projects, api
from tests4py.api import setup
from tests4py.api.report import CheckoutReport, CompileReport, InfoReport, TestReport
from tests4py.constants import (
    DEFAULT_WORK_DIR,
)
from tests4py.logger import LOGGER, init_logger


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
    init_logger(verbose=verbose)

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

        setup()

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
    init_logger(verbose=verbose)
    try:
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
    relevant_tests: bool = False,
    all_tests: bool = False,
    output: Path = None,
    coverage: bool = False,
    verbose=True,
) -> TestReport:
    report = TestReport()
    init_logger(verbose=verbose)
    try:
        api.test_project(
            work_dir,
            single_test=single_test,
            relevant_tests=relevant_tests,
            all_tests=all_tests,
            xml_output=output,
            coverage=coverage,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
