from pathlib import Path
from typing import List, Optional

import sflkit
from sflkit.events import EventType

from tests4py.api import compile_project
from tests4py.framework.utils import ProjectReport
from tests4py.projects import Project
from tests4py.sfl.constants import (
    EVENTS_PATH,
    DEFAULT_EXCLUDES,
    SFL,
    INSTRUMENT,
    EVENTS,
)


class SFLInstrumentReport(ProjectReport):
    def __init__(self):
        super().__init__(command=SFL, subcommand=INSTRUMENT)


class SFLEventsReport(ProjectReport):
    def __init__(self):
        super().__init__(command=SFL, subcommand=EVENTS)


def get_events_path(project: Project, passing: Optional[bool] = None):
    if passing is None:
        return EVENTS_PATH / project.project_name / str(project.bug_id)
    else:
        return (
            EVENTS_PATH
            / project.project_name
            / str(project.bug_id)
            / ("passing" if passing else "failing")
        )


def create_config(
    project: Project,
    src: Path,
    dst: Path,
    events: List[str] = None,
    metrics: List[str] = None,
    excludes: List[str] = None,
):
    if events is None:
        events = [event.name for event in EventType]
    if metrics is None:
        metrics = []
    if excludes is None:
        excludes = DEFAULT_EXCLUDES
    return sflkit.Config.create(
        path=str(src),
        language="python",
        events=",".join(events),
        metrics=",".join(metrics),
        passing=str(get_events_path(project=project, passing=True)),
        failing=str(get_events_path(project=project, passing=False)),
        working=str(dst),
        exclude='"' + '","'.join(excludes) + '"',
    )


def instrument(config: sflkit.Config):
    sflkit.instrument_config(config)
    report = compile_project(Path(config.instrument_working), sfl=True)
    if report.raised:
        raise report.raised
