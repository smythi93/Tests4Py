import os
from pathlib import Path
from typing import Optional, Dict, List, Set

import sflkit
from sflkit.analysis.suggestion import Suggestion
from sflkit.runners import Runner
from sflkit.runners.run import Environment, DEFAULT_TIMEOUT
from sflkit.runners.run import TestResult
from sflkitlib.events import EventType

from tests4py.api import build
from tests4py.api.report import ProjectReport
from tests4py.constants import SRC_FILE
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
        self.passing: Set[str] = set()
        self.failing: Set[str] = set()
        self.undefined: Set[str] = set()


class SFLAnalyzeReport(ProjectReport):
    def __init__(self):
        super().__init__(command=SFL, subcommand=ANALYZE)
        self.analyzer: Optional[sflkit.Analyzer] = None
        self.suggestions: Optional[Dict[str, List[Suggestion]]] = None


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
    mapping: Optional[Path] = None,
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
        path=str(src.absolute()),
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
        working=str(dst.absolute()),
        include='"' + '","'.join(includes) + '"',
        exclude='"' + '","'.join(excludes) + '"',
        mapping_path=str(mapping.absolute()) if mapping else "",
    )


def instrument(config: sflkit.Config):
    sflkit.instrument_config(config)
    working = Path(config.instrument_working)
    with open(working / SRC_FILE, "w") as fp:
        fp.write(str(config.target_path.absolute()))
    report = build(working, rebuild=True, sfl=True)
    if report.raised:
        raise report.raised


def analyze(config: sflkit.Config) -> sflkit.Analyzer:
    analyzer = sflkit.Analyzer(config.failing, config.passing, config.factory)
    analyzer.analyze()
    return analyzer


def read_src(work_dir: Path) -> Optional[Path]:
    src = work_dir / SRC_FILE
    if src.exists():
        return Path(src.read_text().rstrip("\n"))


class OracleInputRunner(Runner):
    def __init__(
        self,
        project: Project,
        relative: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
    ):
        super().__init__(timeout=timeout)
        self.project = project
        self.relative = relative

    def get_tests(
        self,
        directory: Path,
        files: Optional[List[os.PathLike] | os.PathLike] = None,
        base: Optional[os.PathLike] = None,
        environ: Environment = None,
    ) -> List[str]:
        if not files:
            return []
        if isinstance(files, list):
            if self.relative:
                return map(lambda test: os.path.join(directory, test), files)
            else:
                return files
        if self.relative:
            files = directory / files
        else:
            files = Path(files)
        if files.exists():
            if files.is_dir():
                return list(
                    map(lambda test: os.path.join(files, test), os.listdir(files))
                )
            elif os.path.isfile(files):
                return [str(files)]
            else:
                raise ValueError("tests must be a file or a directory")
        else:
            raise ValueError("tests must be a list of paths or a path that exists")

    def run_test(
        self, directory: Path, test: str, environ: Environment = None
    ) -> TestResult:
        result, _, _, _ = self.project.api.run(
            test, environ, work_dir=directory, invoke_oracle=True
        )
        return TestResult[result.value]
