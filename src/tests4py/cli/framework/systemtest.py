from pathlib import Path
from typing import Union, Sequence

from tests4py import api
from tests4py.api.report import (
    SystemtestGenerateReport,
    SystemtestTestReport,
    RunReport,
)
from tests4py.logger import init_logger


def tests4py_run(
    work_dir: Path = None,
    inputs: Sequence[str] = None,
    invoke_oracle: bool = False,
    verbose=True,
) -> RunReport:
    report = RunReport()
    init_logger(verbose=verbose)
    try:
        input_path = Path(inputs[0])
        if len(inputs) == 1 and len(inputs[0]) <= 256 and input_path.exists():
            args = input_path
        else:
            args = inputs
        api.run(work_dir, args_or_path=args, report=report, invoke_oracle=invoke_oracle)
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report


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
    init_logger(verbose=verbose)
    try:
        api.systemtest_generate(
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
    path_or_str: Path | str = None,
    diversity: bool = False,
    output: Path = None,
    verbose=True,
) -> SystemtestTestReport:
    report = SystemtestTestReport()
    init_logger(verbose=verbose)
    try:
        api.systemtest_test(
            work_dir,
            path_or_str=path_or_str,
            diversity=diversity,
            output=output,
            report=report,
        )
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
