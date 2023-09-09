import os
from pathlib import Path
from typing import List, Optional

from tests4py.constants import PYTHON
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API

PROJECT_MAME = "expression"


class Expression(Project):
    def __init__(
        self,
        bug_id: int,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_files: List[Path],
        test_cases: List[str],
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_MAME,
            github_url="https://github.com/smythi93/expression",
            status=Status.OK,
            python_version="3.10.9",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar,
            loc=loc,
            setup=[[PYTHON, "-m", "pip", "install", "."]],
            included_files=[os.path.join("src", PROJECT_MAME)],
            relevant_test_files=relevant_test_files,
        )


def register():
    Expression(
        bug_id=1,
        buggy_commit_id="7b08a1dd737bd47c9be47258d2cd63bb7de72c47",
        fixed_commit_id="10356a6d3768db2ff7749408b7f3d12a773a18a9",
        test_files=[
            Path("tests", "test_evaluate.py"),
            Path("tests", "test_expression.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_evaluate.py")
            + "::TestEvaluate::test_eval_div_error",
            os.path.join("tests", "test_expression.py") + "::TestExpr::test_div_error",
        ],
    )


grammar: Grammar = {
    "<start>": [""],
}


assert is_valid_grammar(grammar)
