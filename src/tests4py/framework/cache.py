from tests4py import projects
from tests4py.constants import DEFAULT_WORK_DIR
from tests4py.framework.default import tests4py_checkout, tests4py_compile
from tests4py.framework.utils import (
    CacheReport,
    __setup__,
    __init_logger__,
)


def tests4py_cache(
    project_name: str = None, bug_id: int = None, force: bool = False, verbose=True
) -> CacheReport:
    report = CacheReport()
    __init_logger__(verbose=verbose)
    try:
        __setup__()
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
            compile_report = tests4py_compile(
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
