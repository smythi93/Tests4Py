import ast
import os
import subprocess
import tempfile
from os import PathLike
from pathlib import Path
from typing import List, Optional

from BugsTest.grammars import python
from BugsTest.projects import Project, Status, TestingFramework, TestStatus
from BugsTest.tests.generator import UnitTestGenerator, SystemTestGenerator
from BugsTest.tests.utils import API, TestResult


class PySnooper(Project):

    def __init__(self, bug_id: int, python_version: str, python_path: str,
                 buggy_commit_id: str, fixed_commit_id: str, test_file: List[Path], test_cases: List[str],
                 darwin_python_version: Optional[str] = None,
                 test_status_fixed: TestStatus = TestStatus.PASSING,
                 test_status_buggy: TestStatus = TestStatus.FAILING,
                 unittests: Optional[UnitTestGenerator] = None,
                 systemtests: Optional[SystemTestGenerator] = None,
                 api: Optional[API] = None):
        super().__init__(bug_id=bug_id, project_name='pysnooper', github_url='https://github.com/cool-RR/PySnooper',
                         status=Status.OK, cause='N.A.',
                         python_version=python_version, python_path=python_path, buggy_commit_id=buggy_commit_id,
                         fixed_commit_id=fixed_commit_id, testing_framework=TestingFramework.PYTEST,
                         test_file=test_file, test_cases=test_cases, darwin_python_version=darwin_python_version,
                         test_status_fixed=test_status_fixed, test_status_buggy=test_status_buggy,
                         unittests=unittests, systemtests=systemtests, api=api)


class PySnooperApi(API):

    def __init__(self, default_timeout: int = 5):
        self.translator = python.ToASTVisitor(python.GENERATIVE_GRAMMAR)
        super().__init__(default_timeout=default_timeout)

    def run(self, system_test_path: PathLike) -> TestResult:
        try:
            with open(system_test_path, 'r') as fp:
                test = fp.read()
            test = ast.unparse(self.translator.visit_string(test))
            with tempfile.NamedTemporaryFile('w+', suffix='.py', delete=False) as fp:
                fp.write(test)
            process = subprocess.run(['python3.8', fp.name], stdout=subprocess.PIPE, timeout=self.default_timeout)
            os.remove(fp.name)
            if process.returncode:
                if b"NameError: name 'output_path' is not defined" in process.stdout:
                    return TestResult.FAILING
                else:
                    return TestResult.UNKNOWN
            else:
                return TestResult.PASSING
        except (subprocess.TimeoutExpired, SyntaxError):
            return TestResult.UNKNOWN


def register():
    PySnooper(
        bug_id=1,
        python_version='3.8.1',
        darwin_python_version='3.8.4',  # version 3.8.1-3 do not work on mac os
        python_path='',
        buggy_commit_id='e21a31162f4c54be693d8ca8260e42393b39abd3',
        fixed_commit_id='56f22f8ffe1c6b2be4d2cf3ad1987fdb66113da2',
        test_file=[Path('tests', 'test_chinese.py')],
        test_cases=['tests/test_chinese.py::test_chinese'],
        test_status_buggy=TestStatus.PASSING,
    )
    PySnooper(
        bug_id=2,
        python_version='3.8.1',
        darwin_python_version='3.8.4',  # version 3.8.1-3 do not work on mac os
        python_path='',
        buggy_commit_id='e21a31162f4c54be693d8ca8260e42393b39abd3',
        fixed_commit_id='814abc34a098c1b98cb327105ac396f985d2413e',
        test_file=[Path('tests', 'test_pysnooper.py')],
        test_cases=['tests/test_pysnooper.py::test_custom_repr_single'],
        test_status_fixed=TestStatus.ERROR,
        test_status_buggy=TestStatus.ERROR,
    )
    PySnooper(
        bug_id=3,
        python_version='3.8.1',
        darwin_python_version='3.8.4',  # version 3.8.1-3 do not work on mac os
        python_path='',
        buggy_commit_id='6e3d797be3fa0a746fb5b1b7c7fea78eb926c208',
        fixed_commit_id='15555ed760000b049aff8fecc79d29339c1224c3',
        test_file=[Path('tests', 'test_pysnooper.py')],
        test_cases=['tests/test_pysnooper.py::test_file_output'],
        api=PySnooperApi(),
    )
