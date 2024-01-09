from tests4py import projects
from tests4py.api.cache import clear_project, clear_venv
from tests4py.api.report import CacheReport, ClearReport
from tests4py.cli.framework.default import tests4py_checkout, tests4py_build
from tests4py.constants import DEFAULT_WORK_DIR
from tests4py.logger import init_logger, LOGGER


def tests4py_cache(
    project_name: str = None, bug_id: int = None, force: bool = True, verbose=True
) -> CacheReport:
    report = CacheReport()
    init_logger(verbose=verbose)
    if not force:
        LOGGER.warning("Deactivating a clean build may lead to unintended behavior.")
    try:
        project_list = projects.get_matching_projects(project_name, bug_id)
        for project in project_list:
            checkout_report = tests4py_checkout(
                project.project_name,
                project.bug_id,
                force=force,
                verbose=verbose,
            )
            report.checkout_reports[
                f"{project.project_name}_{project.bug_id}"
            ] = checkout_report
            compile_report = tests4py_build(
                DEFAULT_WORK_DIR / f"{project.project_name}_{project.bug_id}",
                force=force,
                verbose=verbose,
            )
            report.compile_reports[
                f"{project.project_name}_{project.bug_id}"
            ] = compile_report
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_clear(
    project_name: str = None,
    bug_id: int = None,
    project_and_venv: bool = False,
    verbose=True,
) -> ClearReport:
    report = ClearReport()
    init_logger(verbose=verbose)
    try:
        project_list = projects.get_matching_projects(project_name, bug_id)
        for project in project_list:
            report.project = project
            if bug_id is None:
                clear_project(project)
            elif project_and_venv:
                clear_project(project)
                clear_venv(project)
            else:
                clear_venv(project)
            break
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
