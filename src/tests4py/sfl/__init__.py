from pathlib import Path
from typing import List

from tests4py.projects import Project
from tests4py.sfl.utils import instrument, create_config


def sflkit_instrument(
    project: Project,
    src: Path,
    dst: Path,
    events: List[str] = None,
    metrics: List[str] = None,
    excludes: List[str] = None,
):
    instrument(
        create_config(
            project, src, dst, events=events, metrics=metrics, excludes=excludes
        ),
        dst,
    )


def sflkit_get_events():
    pass
