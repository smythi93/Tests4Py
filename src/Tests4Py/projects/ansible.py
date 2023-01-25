from os import PathLike
from pathlib import Path
from typing import List, Optional

from Tests4Py.framework.typing import Environment
from Tests4Py.projects import Project, Status, TestingFramework, TestStatus
from Tests4Py.tests.generator import UnittestGenerator, SystemtestGenerator
from Tests4Py.tests.utils import API, TestResult


class Ansible(Project):

    def __init__(self, bug_id: int, python_version: str, python_path: str,
                 buggy_commit_id: str, fixed_commit_id: str, test_file: List[Path], test_cases: List[str],
                 darwin_python_version: Optional[str] = None,
                 test_status_fixed: TestStatus = TestStatus.PASSING,
                 test_status_buggy: TestStatus = TestStatus.FAILING,
                 unittests: Optional[UnittestGenerator] = None,
                 systemtests: Optional[SystemtestGenerator] = None,
                 api: Optional[API] = None):
        super().__init__(bug_id=bug_id, project_name='ansible', github_url='https://github.com/ansible/ansible',
                         status=Status.OK, cause='N.A.',
                         python_version=python_version, python_path=python_path, buggy_commit_id=buggy_commit_id,
                         fixed_commit_id=fixed_commit_id, testing_framework=TestingFramework.PYTEST,
                         test_file=test_file, test_cases=test_cases, darwin_python_version=darwin_python_version,
                         test_status_fixed=test_status_fixed, test_status_buggy=test_status_buggy,
                         unittests=unittests, systemtests=systemtests, api=api, grammar=None)  # TODO adjust parameters


# REGISTER BUGS

def register():
    Ansible(
        bug_id=1,
        python_version='3.6.9',
        darwin_python_version='3.6.15',
        python_path='ansible/build/lib/',
        buggy_commit_id='25c5388fdec9e56517a93feb5e8d485680946c25',
        fixed_commit_id='343ffaa18b63c92e182b16c3ad84b8d81ca4df69',
        test_file=[Path('test', 'units', 'galaxy', 'test_collection.py')],
        test_cases=['test/units/galaxy/test_collection.py::test_verify_collections_no_version'],
        test_status_buggy=TestStatus.PASSING,
    )
    Ansible(
        bug_id=2,
        python_version='3.6.9',
        darwin_python_version='3.6.15',
        python_path='ansible/build/lib/',
        buggy_commit_id='de59b17c7f69d5cfb72479b71776cc8b97e29a6b',
        fixed_commit_id='5b9418c06ca6d51507468124250bb58046886be6',
        test_file=[Path('test', 'units', 'utils', 'test_version.py')],
        test_cases=['test/units/utils/test_version.py::test_alpha', 'test/units/utils/test_version.py::test_numeric'],
        test_status_buggy=TestStatus.PASSING
    )
    # TODO implement the 18 bugs of black


class AnsibleAPI(API):

    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        return TestResult.UNKNOWN
