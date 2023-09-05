import csv
from pathlib import Path
from typing import List

from sflkitlib.events import EventType

from tests4py import sfl
from tests4py.logger import init_logger
from tests4py.sfl import SFLInstrumentReport, SFLEventsReport


def tests4py_sfl_instrument(
    work_dir: Path,
    dst: Path,
    events: str = None,
    excludes: List[str] = None,
    verbose: bool = True,
):
    report = SFLInstrumentReport()
    init_logger(verbose=verbose)

    if work_dir is None:
        work_dir = Path.cwd()
    if dst is None:
        raise ValueError("Destination required for instrument")
    try:
        if not work_dir.exists():
            raise IOError(f"{work_dir} does not exist")
        sfl.sflkit_instrument(
            work_dir,
            dst=dst,
            events=list(
                map(
                    lambda event: EventType[event.upper()],
                    list(csv.reader([events]))[0],
                )
            )
            if events
            else None,
            excludes=list(csv.reader([excludes]))[0] if excludes else None,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_sfl_events(
    work_dir: Path = None, output: Path = None, verbose: bool = True
):
    report = SFLEventsReport()
    init_logger(verbose=verbose)

    if work_dir is None:
        work_dir = Path.cwd()
    try:
        if not work_dir.exists():
            raise IOError(f"{work_dir} does not exist")
        sfl.sflkit_get_events(
            work_dir,
            output=output,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
