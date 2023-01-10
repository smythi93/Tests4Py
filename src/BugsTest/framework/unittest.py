import logging
import os
import subprocess
from pathlib import Path
from typing import Union

from BugsTest import framework
from BugsTest.projects import TestingFramework

DEFAULT_SUB_PATH = 'bugs_test_unittests.py'


class UnittestGenerateReport(framework.GenerateReport):
    def __init__(self):
        super().__init__(framework.UNITTEST, subcommand=framework.GENERATE)


class UnittestTestReport(framework.GenerateReport):
    def __init__(self):
        super().__init__(framework.UNITTEST, subcommand=framework.TEST)


def bugstest_generate(work_dir: Path = None, path: Path = None, n: int = 1, failing: Union[int, float] = 1,
                      is_only_passing: bool = False, is_only_failing: bool = False, append: bool = False,
                      verify: bool = False, verbose=True) -> UnittestGenerateReport:
    report = UnittestGenerateReport()
    if verbose:
        framework.LOGGER.setLevel(logging.INFO)
    else:
        framework.LOGGER.setLevel(logging.WARNING)

    try:
        if work_dir is None:
            work_dir = Path.cwd()

        current_dir = Path.cwd()
        try:
            project = framework.__get_project__(work_dir)
            report.project = project

            if project.unittests is None:
                raise NotImplementedError(
                    f'Unittest generation is not enabled for {project.project_name}_{project.bug_id}')

            if is_only_passing and is_only_failing:
                raise ValueError(f'Generate of only passing and failing tests at the same time not possible')

            if path is None:
                path = work_dir / 'bugs_test_unittests.py'
            if path.exists() and path.is_dir():
                raise ValueError(f'Generation of unittest is not possible because {path} is a directory')

            if failing < 1:
                project.unittests.failing_probability = failing
            else:
                project.unittests.failing_probability = failing / n

            if is_only_passing:
                framework.LOGGER.info(
                    f'Generate {n} only passing tests for {project.project_name}_{project.bug_id} to {path}')
                result = project.unittests.generate_only_passing_tests(n=n, path=path, append=append)
            elif is_only_failing:
                framework.LOGGER.info(
                    f'Generate {n} only failing tests for {project.project_name}_{project.bug_id} to {path}')
                result = project.unittests.generate_only_failing_tests(n=n, path=path, append=append)
            else:
                framework.LOGGER.info(
                    f'Generate {n} passing and failing tests with failing probability '
                    f'{project.unittests.failing_probability} for {project.project_name}_{project.bug_id} to {path}')
                result = project.unittests.generate_tests(n=n, path=path, append=append)

            report.passing = result.passing
            report.failing = result.failing
            report.total = n

            successful = False
            if verify:
                framework.__env_on__(project, verbose=verbose)
                framework.__activating_venv__(Path('env'))

                command = ['python', '-m', TestingFramework.PYTEST.value, path]
                output = subprocess.run(command, stdout=subprocess.PIPE).stdout
                if project.testing_framework == TestingFramework.PYTEST:
                    match = framework.PYTEST_PATTERN.search(output)
                    if match:
                        if match.group('f'):
                            report.varify_failing = int(match.group('f'))
                        else:
                            report.varify_failing = 0
                        if match.group('p'):
                            report.varify_passing = int(match.group('p'))
                        else:
                            report.varify_failing = 0
                        successful = True
            else:
                successful = True

            report.successful = successful
        finally:
            framework.__deactivating_venv__(verbose=verbose)
            os.chdir(current_dir)
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report
