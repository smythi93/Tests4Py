import os
from pathlib import Path
from typing import Union, Optional

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
    read_src,
    OracleInputRunner,
)

DEFAULT_TIME_OUT = 10


def sflkit_instrument(
    dst: os.PathLike,
    work_dir_or_project: Optional[Union[os.PathLike, Project]] = None,
    events: str = None,
    mapping: os.PathLike = None,
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
                Path(dst),
                events=events,
                mapping=Path(mapping) if mapping else None,
            ),
        )
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def sflkit_unittest(
    work_dir: os.PathLike,
    output: Path = None,
    all_tests: bool = False,
    report: SFLEventsReport = None,
):
    report = report or SFLEventsReport()
    work_dir = Path(work_dir)
    try:
        project = load_project(work_dir, only_project=True)
        if output is None:
            output = get_events_path(project)
        report.project = project
        environ = env_on(project)
        environ = activate_venv(work_dir, environ)
        runner = PytestRunner(timeout=DEFAULT_TIME_OUT)
        runner.run(
            directory=work_dir,
            output=output,
            files=None if all_tests else project.relevant_test_files,
            base=project.test_base,
            environ=environ,
        )
        report.successful = True
        report.passing = runner.passing_tests
        report.failing = runner.failing_tests
        report.undefined = runner.undefined_tests
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def sflkit_systemtest(
    work_dir: os.PathLike,
    tests: os.PathLike | list[os.PathLike],
    relative: bool = False,
    output: Path = None,
    report: SFLEventsReport = None,
):
    report = report or SFLEventsReport()
    work_dir = Path(work_dir)
    try:
        project = load_project(work_dir, only_project=True)
        if output is None:
            output = get_events_path(project)
        report.project = project
        environ = env_on(project)
        environ = activate_venv(work_dir, environ)
        runner = OracleInputRunner(
            project=project, relative=relative, timeout=DEFAULT_TIME_OUT
        )
        runner.run(work_dir, output, files=tests, environ=environ)
        report.successful = True
        report.passing = runner.passing_tests
        report.failing = runner.failing_tests
        report.undefined = runner.undefined_tests
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def sflkit_analyze(
    work_dir: os.PathLike,
    src: os.PathLike = None,
    events_path: os.PathLike = None,
    metrics: str = None,
    predicates: str = None,
    suggestions: bool = False,
    report: SFLAnalyzeReport = None,
):
    report = report or SFLAnalyzeReport()
    work_dir = Path(work_dir)
    try:
        project = load_project(work_dir, only_project=True)
        report.project = project
        src = Path(src) if src else read_src(work_dir)
        events_path = Path(events_path) if events_path else None
        config = create_config(
            project,
            src=src or work_dir,
            dst=work_dir,
            metrics=metrics,
            predicates=predicates,
            events_path=events_path,
        )
        analyzer = analyze(config)
        report.analyzer = analyzer
        report.suggestions = {
            metric.__name__: analyzer.get_sorted_suggestions(
                base_dir=src or work_dir, metric=metric
            )
            for metric in config.metrics
        }
        if suggestions:
            for metric in config.metrics:
                LOGGER.info(f"Metric: {metric.__name__}")
                for i, s in enumerate(
                    report.suggestions[metric.__name__][:10], start=1
                ):
                    LOGGER.info(f"Suggestion {i:>2}: {s}")
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
