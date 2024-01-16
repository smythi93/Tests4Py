from pathlib import Path

from tests4py import sfl
from tests4py.logger import init_logger
from tests4py.sfl import SFLInstrumentReport, SFLEventsReport
from tests4py.sfl.utils import SFLAnalyzeReport


def tests4py_sfl_instrument(
    work_dir: Path,
    dst: Path,
    events: str = None,
    verbose: bool = True,
):
    report = SFLInstrumentReport()
    init_logger(verbose=verbose)
    try:
        sfl.sflkit_instrument(
            work_dir,
            dst=dst,
            events=events,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_sfl_events(
    work_dir: Path = None,
    output: Path = None,
    all_tests: bool = False,
    verbose: bool = True,
):
    report = SFLEventsReport()
    init_logger(verbose=verbose)
    try:
        sfl.sflkit_get_events(
            work_dir,
            output=output,
            all_tests=all_tests,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_sfl_analyze(
    work_dir: Path = None,
    src: Path = None,
    events_path: Path = None,
    metrics: str = None,
    predicates: str = None,
    suggestions: bool = False,
    verbose: bool = True,
) -> SFLAnalyzeReport:
    report = SFLAnalyzeReport()
    init_logger(verbose=verbose)
    try:
        sfl.sflkit_analyze(
            work_dir,
            src=src,
            events_path=events_path,
            metrics=metrics,
            predicates=predicates,
            suggestions=suggestions,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
