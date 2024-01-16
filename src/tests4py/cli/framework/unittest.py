from pathlib import Path
from typing import Union

from tests4py import api
from tests4py.api.report import UnittestGenerateReport, UnittestTestReport
from tests4py.logger import init_logger


def tests4py_generate(
    work_dir: Path = None,
    path: Path = None,
    n: int = 1,
    p: Union[int, float] = 0.5,
    is_only_passing: bool = False,
    is_only_failing: bool = False,
    append: bool = False,
    verify: bool = False,
    verbose=True,
) -> UnittestGenerateReport:
    report = UnittestGenerateReport()
    init_logger(verbose=verbose)
    try:
        api.unittest_generate(
            work_dir,
            path=path,
            n=n,
            p=p,
            is_only_passing=is_only_passing,
            is_only_failing=is_only_failing,
            append=append,
            verify=verify,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


def tests4py_test(
    work_dir: Path = None,
    path_or_str: Path = None,
    diversity: bool = True,
    output: Path = None,
    verbose=True,
) -> UnittestTestReport:
    report = UnittestTestReport()
    init_logger(verbose=verbose)
    try:
        api.unittest_test(
            work_dir,
            path=path_or_str,
            diversity=diversity,
            output=output,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
