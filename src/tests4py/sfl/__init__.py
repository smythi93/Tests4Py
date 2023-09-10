from pathlib import Path
from typing import Union

from sflkit.runners import PytestRunner

from tests4py.api.utils import load_project, get_work_dir
from tests4py.environment import env_on, activate_venv
from tests4py.logger import LOGGER
from tests4py.projects import Project
from tests4py.sfl.utils import (
    instrument,
    create_config,
    SFLEventsReport,
    SFLInstrumentReport,
    get_events_path,
    SFLAnalyzeReport,
    analyze,
)

DEFAULT_TIME_OUT = 30


def sflkit_instrument(
    work_dir_or_project: Project,
    dst: Path,
    events: str = None,
    report: SFLInstrumentReport = None,
):
    report = report or SFLInstrumentReport()
    work_dir = get_work_dir(work_dir_or_project)
    try:
        if dst is None:
            raise ValueError("Destination required for instrument")
        project = load_project(work_dir, only_project=True)
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
    all_tests: bool = False,
    report: SFLEventsReport = None,
):
    report = report or SFLEventsReport()
    work_dir = get_work_dir(work_dir_or_project)
    try:
        project = load_project(work_dir, only_project=True)
        if output is None:
            output = get_events_path(project)
        report.project = project
        environ = env_on(project)
        environ = activate_venv(work_dir, environ)
        PytestRunner(timeout=DEFAULT_TIME_OUT).run(
            directory=work_dir,
            output=output,
            files=None if all_tests else project.relevant_test_files,
            base=project.test_base,
            environ=environ,
        )
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def sflkit_analyze(
    work_dir_or_project: Union[Path, Project] = None,
    src: Path = None,
    events_path: Path = None,
    metrics: str = None,
    predicates: str = None,
    suggestions: bool = False,
    report: SFLAnalyzeReport = None,
):
    report = report or SFLAnalyzeReport()
    work_dir = get_work_dir(work_dir_or_project)
    try:
        project = load_project(work_dir, only_project=True)
        report.project = project
        analyzer = analyze(
            create_config(
                project,
                src=src or work_dir,
                dst=work_dir,
                metrics=metrics,
                predicates=predicates,
                events_path=events_path,
            )
        )
        report.analyzer = analyzer
        if suggestions:
            for i, s in enumerate(analyzer.get_sorted_suggestions(src)[:10], start=1):
                LOGGER.info(f"Suggestion {i:>2}: {s}")
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
