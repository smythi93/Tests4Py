import logging
import os
import subprocess
from pathlib import Path
from typing import Union

from Tests4Py.framework import utils
from Tests4Py.projects import TestingFramework

DEFAULT_SUB_PATH = 'bugstest_unittests.py'


class UnittestGenerateReport(utils.GenerateReport):
    def __init__(self):
        super().__init__(utils.UNITTEST, subcommand=utils.GENERATE)


class UnittestTestReport(utils.TestingReport):
    def __init__(self):
        super().__init__(utils.UNITTEST, subcommand=utils.TEST)


def bugstest_generate(work_dir: Path = None, path: Path = None, n: int = 1, p: Union[int, float] = 0.5,
                      is_only_passing: bool = False, is_only_failing: bool = False, append: bool = False,
                      verify: bool = False, verbose=True) -> UnittestGenerateReport:
    report = UnittestGenerateReport()
    if verbose:
        utils.LOGGER.setLevel(logging.INFO)
    else:
        utils.LOGGER.setLevel(logging.WARNING)

    if work_dir is None:
        work_dir = Path.cwd()

    current_dir = Path.cwd()
    try:
        project, _, _, _ = utils.__get_project__(work_dir)
        report.project = project

        if project.unittests is None:
            raise NotImplementedError(
                f'Unittest generation is not enabled for {project.project_name}_{project.bug_id}')

        if is_only_passing and is_only_failing:
            raise ValueError(f'Generate of only passing and failing tests at the same time not possible')

        if path is None:
            path = work_dir / DEFAULT_SUB_PATH
        if path.exists() and path.is_dir():
            raise ValueError(f'Generation of unittest is not possible because {path} is a directory')

        if p < 1:
            project.unittests.failing_probability = p
        else:
            project.unittests.failing_probability = p / n

        if is_only_passing:
            utils.LOGGER.info(
                f'Generate {n} only passing tests for {project.project_name}_{project.bug_id} to {path}')
            result = project.unittests.generate_only_passing_tests(n=n, path=path, append=append)
        elif is_only_failing:
            utils.LOGGER.info(
                f'Generate {n} only failing tests for {project.project_name}_{project.bug_id} to {path}')
            result = project.unittests.generate_only_failing_tests(n=n, path=path, append=append)
        else:
            if n < p:
                raise ValueError(f'Cannot generate {n} tests with a failing probability '
                                 f'{project.unittests.failing_probability}>1')
            utils.LOGGER.info(
                f'Generate {n} passing and failing tests with failing probability '
                f'{project.unittests.failing_probability} for {project.project_name}_{project.bug_id} to {path}')
            result = project.unittests.generate_tests(n=n, path=path, append=append)

        report.passing = result.passing
        report.failing = result.failing
        report.total = n
        if verify:
            utils.__env_on__(project, verbose=verbose)
            utils.__activating_venv__(work_dir / utils.VENV)

            command = ['python', '-m', TestingFramework.PYTEST.value, path]
            output = subprocess.run(command, stdout=subprocess.PIPE).stdout
            report.successful, _, report.verify_failing, report.verify_passing = utils.__get_pytest_result__(output)
            utils.LOGGER.info(f'Verify: {report.verify_passing} passed --- {report.verify_failing} failed')
        else:
            report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    finally:
        utils.__deactivating_venv__(verbose=verbose)
        os.chdir(current_dir)
    return report


def bugstest_test(work_dir: Path = None, path: Path = None, diversity: bool = True, output: Path = None,
                  verbose=True) -> UnittestTestReport:
    report = UnittestTestReport()
    if verbose:
        utils.LOGGER.setLevel(logging.INFO)
    else:
        utils.LOGGER.setLevel(logging.WARNING)

    if work_dir is None:
        work_dir = Path.cwd()

    current_dir = Path.cwd()
    try:
        project, _, _, _ = utils.__get_project__(work_dir)
        report.project = project

        if project.unittests is None:
            raise NotImplementedError(
                f'Unittest testing is not enabled for {project.project_name}_{project.bug_id}')

        if path is None and not diversity:
            path = work_dir / DEFAULT_SUB_PATH
        if path and path.exists() and path.is_dir():
            raise ValueError(f'Running of unittest is not possible because {path} is a directory')

        utils.__env_on__(project, verbose=verbose)
        utils.__activating_venv__(work_dir / utils.VENV)

        command = ['python', '-m', TestingFramework.PYTEST.value]
        if output:
            command.append(f'--junit-xml={output.absolute()}')
        if diversity and (work_dir / utils.DEFAULT_UNITTESTS_DIVERSITY_PATH).exists():
            command.append(work_dir / utils.DEFAULT_UNITTESTS_DIVERSITY_PATH)
        if path:
            command.append(path)
        output = subprocess.run(command, stdout=subprocess.PIPE).stdout
        report.successful, report.total, report.failing, report.passing = utils.__get_pytest_result__(
            output)
        utils.LOGGER.info(f'Ran {report.total} tests')
        utils.LOGGER.info(f'{report.passing} passed --- {report.failing} failed')
    except BaseException as e:
        report.raised = e
        report.successful = False
    finally:
        utils.__deactivating_venv__(verbose=verbose)
        os.chdir(current_dir)
    return report
