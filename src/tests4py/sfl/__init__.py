from pathlib import Path
from typing import List, Union

from sflkit.runners import PytestRunner

from tests4py.api.utils import load_project
from tests4py.constants import DEFAULT_WORK_DIR
from tests4py.environment import env_on, activate_venv
from tests4py.projects import Project
from tests4py.sfl.utils import (
    instrument,
    create_config,
    SFLEventsReport,
    SFLInstrumentReport,
    get_events_path,
)


def sflkit_instrument(
    work_dir_or_project: Project,
    dst: Path,
    events: List[str] = None,
    report: SFLInstrumentReport = None,
):
    if report is None:
        report = SFLInstrumentReport()
    current_dir = Path.cwd()
    if work_dir_or_project is None:
        work_dir = current_dir
    elif isinstance(work_dir_or_project, Project):
        work_dir = DEFAULT_WORK_DIR / work_dir_or_project.get_identifier()
    else:
        work_dir = work_dir_or_project
    try:
        project, _, _ = load_project(work_dir)
        report.project = project
        instrument(
            create_config(
                project,
                work_dir,
                dst,
                events=events,
            ),
        )
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def sflkit_get_events(
    work_dir_or_project: Union[Path, Project] = None,
    output: Path = None,
    report: SFLEventsReport = None,
):
    if report is None:
        report = SFLEventsReport()
    if work_dir_or_project is None:
        work_dir = Path.cwd()
    elif isinstance(work_dir_or_project, Project):
        work_dir = DEFAULT_WORK_DIR / work_dir_or_project.get_identifier()
    else:
        work_dir = work_dir_or_project
    try:
        project, _, _ = load_project(work_dir)
        if output is None:
            output = get_events_path(project)
        report.project = project
        environ = env_on(project)
        environ = activate_venv(work_dir, environ)
        PytestRunner().run(
            directory=work_dir,
            output=output,
            base=project.test_base,
            environ=environ,
        )
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
