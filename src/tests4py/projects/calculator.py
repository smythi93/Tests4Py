import os
from pathlib import Path
from typing import List, Optional

from tests4py.constants import PYTHON
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API


class Calculator(Project):
    def __init__(
        self,
        bug_id: int,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_file: List[Path],
        test_cases: List[str],
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
        loc: int = 0,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="calculator",
            github_url="https://github.com/smythi93/calculator",
            status=Status.OK,
            cause="N.A.",
            python_version="3.10.9",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar,
            loc=loc,
            setup=[[PYTHON, "-m", "pip", "install", "."]],
        )


def register():
    Calculator(
        bug_id=1,
        buggy_commit_id="5d7f01c5497940b7415db22864100d90c575300f",
        fixed_commit_id="063d988682e407ad25cd94854f1b4d5e3dc282f8",
        test_file=[
            Path("tests", "test_calc.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_main_sqrt_0",
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_main_sqrt_neg",
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_sqrt_0",
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_sqrt_neg",
        ],
    )


grammar: Grammar = {
    "<start>": [""],
}


assert is_valid_grammar(grammar)
