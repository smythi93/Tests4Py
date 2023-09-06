from pathlib import Path
from typing import Optional

import sflkit
from sflkitlib.events import EventType

from tests4py.api import compile_project
from tests4py.api.report import ProjectReport
from tests4py.projects import Project
from tests4py.sfl.constants import (
    EVENTS_PATH,
    DEFAULT_EXCLUDES,
    SFL,
    INSTRUMENT,
    EVENTS,
    ANALYZE,
)


class SFLInstrumentReport(ProjectReport):
    def __init__(self):
        super().__init__(command=SFL, subcommand=INSTRUMENT)


class SFLEventsReport(ProjectReport):
    def __init__(self):
        super().__init__(command=SFL, subcommand=EVENTS)


class SFLAnalyzeReport(ProjectReport):
    def __init__(self):
        super().__init__(command=SFL, subcommand=ANALYZE)
        self.analyzer: Optional[sflkit.Analyzer] = None


def get_events_path(
    project: Project, passing: Optional[bool] = None, events_path: Optional[Path] = None
):
    if passing is None:
        return (events_path or EVENTS_PATH) / project.project_name / str(project.bug_id)
    else:
        return (
            (events_path or EVENTS_PATH)
            / project.project_name
            / str(project.bug_id)
            / ("passing" if passing else "failing")
        )


def create_config(
    project: Project,
    src: Path,
    dst: Path,
    events: str = None,
    metrics: str = None,
    predicates: str = None,
    events_path: Optional[Path] = None,
):
    if project.included_files:
        includes = project.included_files
        excludes = project.excluded_files
    elif project.excluded_files:
        includes = list()
        excludes = project.excluded_files
    else:
        includes = list()
        excludes = DEFAULT_EXCLUDES
    return sflkit.Config.create(
        path=str(src),
        language="python",
        events=events or ",".join([event.name for event in EventType]),
        metrics=metrics or "",
        predicates=predicates or "",
        passing=str(
            get_events_path(project=project, passing=True, events_path=events_path)
        ),
        failing=str(
            get_events_path(project=project, passing=False, events_path=events_path)
        ),
        working=str(dst),
        include='"' + '","'.join(includes) + '"',
        exclude='"' + '","'.join(excludes) + '"',
    )


def instrument(config: sflkit.Config):
    sflkit.instrument_config(config)
    report = compile_project(Path(config.instrument_working), sfl=True)
    if report.raised:
        raise report.raised


def analyze(config: sflkit.Config) -> sflkit.Analyzer:
    analyzer = sflkit.Analyzer(config.failing, config.passing, config.factory)
    analyzer.analyze()
    return analyzer
