import logging
import os
from pathlib import Path
from typing import Union, Tuple, Dict

from tests4py.framework import utils, environment
from tests4py.constants import (
    DEFAULT_SUB_PATH_SYSTEMTESTS,
    SYSTEMTEST,
    GENERATE,
    DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
    TEST,
)
from tests4py.framework.logger import LOGGER
from tests4py.projects import Project
from tests4py.tests.utils import TestResult


class SystemtestGenerateReport(utils.GenerateReport):
    def __init__(self):
        super().__init__(
            SYSTEMTEST,
            subcommand=GENERATE,
        )


class SystemtestTestReport(utils.TestingReport):
    def __init__(self):
        super().__init__(
            SYSTEMTEST,
            subcommand=TEST,
        )


def _get_system_runs(
    project: Project, path: os.PathLike, environ: Dict[str, str]
) -> Tuple[int, int, int]:
    total, passing, failing = 0, 0, 0
    for _, result in project.api.runs(path, environ):
        if TestResult.PASSING == result:
            passing += 1
        elif TestResult.FAILING == result:
            failing += 1
        total += 1
    return total, passing, failing


def tests4py_generate(
    work_dir: Path = None,
    path: Path = None,
    n: int = 1,
    p: Union[int, float] = 1,
    is_only_passing: bool = False,
    is_only_failing: bool = False,
    append: bool = False,
    verify: bool = False,
    verbose=True,
) -> SystemtestGenerateReport:
    report = SystemtestGenerateReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    if work_dir is None:
        work_dir = Path.cwd()

    current_dir = Path.cwd()
    try:
        project, _, _, _ = utils.__get_project__(work_dir)
        report.project = project

        if project.systemtests is None:
            raise NotImplementedError(
                f"Systemtest generation is not enabled for {project.project_name}_{project.bug_id}"
            )

        if is_only_passing and is_only_failing:
            raise ValueError(
                f"Generate of only passing and failing tests at the same time not possible"
            )

        if path is None:
            path = work_dir / DEFAULT_SUB_PATH_SYSTEMTESTS
        if path.exists() and not path.is_dir():
            raise ValueError(
                f"Generation of unittest is not possible because {path} is a directory"
            )

        if p < 1:
            project.systemtests.failing_probability = p
        else:
            project.systemtests.failing_probability = p / n

        if is_only_passing:
            LOGGER.info(
                f"Generate {n} only passing tests for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.systemtests.generate_only_passing_tests(
                n=n, path=path, append=append
            )
        elif is_only_failing:
            LOGGER.info(
                f"Generate {n} only failing tests for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.systemtests.generate_only_failing_tests(
                n=n, path=path, append=append
            )
        else:
            LOGGER.info(
                f"Generate {n} passing and failing tests with failing probability "
                f"{project.systemtests.failing_probability} for {project.project_name}_{project.bug_id} to {path}"
            )
            result = project.systemtests.generate_tests(n=n, path=path, append=append)

        report.passing = result.passing
        report.failing = result.failing
        report.total = n
        if verify:
            environ = environment.__env_on__(project)
            environ = environment.__activate_venv__(work_dir, environ)

            _, report.verify_passing, report.verify_failing = _get_system_runs(
                project, path, environ
            )
            LOGGER.info(
                f"Verify: {report.verify_passing} passed --- {report.verify_failing} failed"
            )
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    finally:
        os.chdir(current_dir)
    return report


def tests4py_test(
    work_dir: Path = None,
    path: Path = None,
    diversity: bool = True,
    output: Path = None,
    verbose=True,
) -> SystemtestTestReport:
    report = SystemtestTestReport()
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    if work_dir is None:
        work_dir = Path.cwd()

    current_dir = Path.cwd()
    try:
        project, _, _, _ = utils.__get_project__(work_dir)
        report.project = project

        if project.systemtests is None:
            raise NotImplementedError(
                f"Systemtest testing is not enabled for {project.project_name}_{project.bug_id}"
            )

        if path is None and not diversity:
            path = work_dir / DEFAULT_SUB_PATH_SYSTEMTESTS
        if path and not path.exists():
            raise ValueError(
                f"Running of systemtests is not possible because {path} does not exist"
            )

        environ = environment.__env_on__(project)
        environ = environment.__activate_venv__(work_dir, environ)

        report.total, report.passing, report.failing = 0, 0, 0

        if path:
            if path.is_dir():
                report.total, report.passing, report.failing = _get_system_runs(
                    project, path, environ
                )
            else:
                report.total = 1
                _, result = project.api.run(path, environ)
                if TestResult.PASSING == result:
                    report.passing = 1
                elif TestResult.FAILING == result:
                    report.failing = 1
        if diversity and (work_dir / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH).exists():
            t, p, f = _get_system_runs(
                project,
                work_dir / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
                environ,
            )
            report.total += t
            report.passing += p
            report.failing += f
        LOGGER.info(f"Ran {report.total} tests")
        LOGGER.info(f"{report.passing} passed --- {report.failing} failed")
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    finally:
        os.chdir(current_dir)
    return report
