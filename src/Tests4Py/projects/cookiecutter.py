from os import PathLike
from pathlib import Path
from typing import List, Optional

from Tests4Py.grammars import python
from Tests4Py.projects import Project, Status, TestingFramework, TestStatus
from Tests4Py.tests.generator import UnittestGenerator, SystemtestGenerator
from Tests4Py.tests.utils import API, TestResult


class CookieCutter(Project):

    def __init__(self, bug_id: int, python_version: str, python_path: str,
                 buggy_commit_id: str, fixed_commit_id: str, test_file: List[Path], test_cases: List[str],
                 darwin_python_version: Optional[str] = None,
                 test_status_fixed: TestStatus = TestStatus.PASSING,
                 test_status_buggy: TestStatus = TestStatus.FAILING,
                 unittests: Optional[UnittestGenerator] = None,
                 systemtests: Optional[SystemtestGenerator] = None,
                 api: Optional[API] = None):
        super().__init__(bug_id=bug_id, project_name='cookiecutter',
                         github_url='https://github.com/cookiecutter/cookiecutter',
                         status=Status.OK, cause='N.A.',
                         python_version=python_version, python_path=python_path, buggy_commit_id=buggy_commit_id,
                         fixed_commit_id=fixed_commit_id, testing_framework=TestingFramework.PYTEST,
                         test_file=test_file, test_cases=test_cases, darwin_python_version=darwin_python_version,
                         test_status_fixed=test_status_fixed, test_status_buggy=test_status_buggy,
                         unittests=unittests, systemtests=systemtests, api=api, grammar=None)  # TODO adjust parameters


def register():
    CookieCutter(
        bug_id=1,
        python_version='3.6.9',
        darwin_python_version='3.6.15',  # version 3.6.9 do not work on mac os
        python_path='cookiecutter/build/lib/',
        buggy_commit_id='c15633745df6abdb24e02746b82aadb20b8cdf8c',
        fixed_commit_id='7f6804c4953a18386809f11faf4d86898570debc',
        test_file=[Path('tests', 'test_generate_context.py'), Path('tests', 'test-generate-context', 'non_ascii.json')],
        test_cases=['tests/test_generate_context.py::test_generate_context_decodes_non_ascii_chars'],
        test_status_buggy=TestStatus.PASSING,  # It was just a missing test file
    )
    CookieCutter(
        bug_id=2,
        python_version='3.6.9',
        darwin_python_version='3.6.15',  # version 3.8.1-3 do not work on mac os
        python_path='cookiecutter/build/lib/',
        buggy_commit_id='d7e7b28811e474e14d1bed747115e47dcdd15ba3',
        fixed_commit_id='90434ff4ea4477941444f1e83313beb414838535',
        test_file=[Path('tests', 'test_hooks.py')],
        test_cases=['tests/test_hooks.py::TestFindHooks::test_find_hook',
                    'tests/test_hooks.py::TestExternalHooks::test_run_hook'],
        systemtests=None,  # Bug does not propagate
    )
    CookieCutter(
        bug_id=3,
        python_version='3.6.9',
        darwin_python_version='3.6.15',  # version 3.8.1-3 do not work on mac os
        python_path='cookiecutter/build/lib/',
        buggy_commit_id='5c282f020a8db7e5e7c4e7b51b010556ca31fb7f',
        fixed_commit_id='7129d474206761a6156925db78eee4b62a0e3944',
        test_file=[Path('tests', 'test_read_user_choice.py')],
        test_cases=['tests/test_read_user_choice.py::test_click_invocation'],
        systemtests=None,  # Bug does not propagate
    )
    CookieCutter(
        bug_id=4,
        python_version='3.6.9',
        darwin_python_version='3.6.15',  # version 3.8.1-3 do not work on mac os
        python_path='cookiecutter/build/lib/',
        buggy_commit_id='9568ab6ecd2d6836646006c59473c4a4ac0dee04',
        fixed_commit_id='457a1a4e862aab4102b644ff1d2b2e2b5a766b3c',
        test_file=[Path('tests', 'test_hooks.py')],
        test_cases=['tests/test_hooks.py::TestExternalHooks::test_run_failing_hook'],
        systemtests=None,  # Bug does not propagate
    )
    # TODO implement the 4 bugs of cookiecutter


class CookieCutterAPI(API):

    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike) -> TestResult:
        return TestResult.UNKNOWN
