from pathlib import Path
from typing import List

import sflkit

from tests4py.api import compile_project
from tests4py.projects import Project
from tests4py.sfl.constants import EVENTS_PATH, DEFAULT_EXCLUDES


def get_events_path(project: Project, passing: bool = True):
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
        events = ["line"]
    if metrics is None:
        metrics = ["Ochiai"]
    if excludes is None:
        excludes = DEFAULT_EXCLUDES
    return sflkit.Config.create(
        path=str(src),
        language="python",
        events=",".join(events),
        metrics=",".join(metrics),
        passing=get_events_path(project=project, passing=True),
        failing=get_events_path(project=project, passing=False),
        working=str(dst),
        exclude='"' + '","'.join(excludes) + '"',
    )


def instrument(config: sflkit.Config, dst: Path):
    sflkit.instrument_config(config)
    compile_project(dst)
