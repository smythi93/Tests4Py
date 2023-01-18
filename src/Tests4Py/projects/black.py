from os import PathLike
from pathlib import Path
from typing import List, Optional

from Tests4Py.grammars import python
from Tests4Py.projects import Project, Status, TestingFramework, TestStatus
from Tests4Py.tests.generator import UnittestGenerator, SystemtestGenerator
from Tests4Py.tests.utils import API, TestResult


class Black(Project):

    def __init__(self, bug_id: int, python_version: str, python_path: str,
                 buggy_commit_id: str, fixed_commit_id: str, test_file: List[Path], test_cases: List[str],
                 darwin_python_version: Optional[str] = None,
                 test_status_fixed: TestStatus = TestStatus.PASSING,
                 test_status_buggy: TestStatus = TestStatus.FAILING,
                 unittests: Optional[UnittestGenerator] = None,
                 systemtests: Optional[SystemtestGenerator] = None,
                 api: Optional[API] = None):
        super().__init__(bug_id=bug_id, project_name='black', github_url='https://github.com/psf/black',
                         status=Status.OK, cause='N.A.',
                         python_version=python_version, python_path=python_path, buggy_commit_id=buggy_commit_id,
                         fixed_commit_id=fixed_commit_id, testing_framework=TestingFramework.UNITTEST,
                         test_file=test_file, test_cases=test_cases, darwin_python_version=darwin_python_version,
                         test_status_fixed=test_status_fixed, test_status_buggy=test_status_buggy,
                         unittests=unittests, systemtests=systemtests, api=api, grammar=None)  # TODO adjust parameters


def register():
    Black(
        bug_id=1,
        python_version='3.8.3',
        darwin_python_version='3.8.3',
        python_path='',
        buggy_commit_id='26c9465a22c732ab1e17b0dec578fa3432e9b558',
        fixed_commit_id='c0a7582e3d4cc8bec3b7f5a6c52b36880dcb57d7',
        test_file=[Path('tests', 'test_black.py')],
        test_cases=['']
    )


class BlackAPI(API):

    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike) -> TestResult:
        return TestResult.UNKNOWN
