import ast
import os
import random
import string
import subprocess
from _ast import Call, ImportFrom
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

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
            setup=[[PYTHON, "-m", "pip", "install", "-e", "."]],
            included_files=[os.path.join("src", PROJECT_MAME)],
            test_base=Path("tests"),
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
        loc=108,
        unittests=ExpressionUnittestGenerator(),
        systemtests=ExpressionSystemtestGenerator(),
        api=ExpressionAPI(),
    )


class ExpressionAPI(API):
    def __init__(self, default_timeout=5):
        super().__init__(default_timeout=default_timeout)

    def get_test_arguments_from_string(self, s: str) -> List[str]:
        return [s]

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        if process.returncode != 0 and b"ValueError" not in process.stderr:
            return TestResult.FAILING, f"Process failed with {process.returncode}"
        elif process.returncode != 0:
            return (
                TestResult.PASSING,
                f"Process failed with ValueError and code {process.returncode}",
            )
        expected = process.args[2]
        expected = "".join(expected).strip()
        result = process.stdout.decode("utf8")
        result = float(result)
        try:
            expected = eval(expected.replace("~", "-"))
        except ZeroDivisionError:
            return (
                TestResult.FAILING,
                "ZeroDivisionError for evaluation but no ValueError for subject.",
            )
        if result == expected:
            return TestResult.PASSING, f"Expected {expected}, and was {result}"
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class ExpressionTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> Tuple[Any, Any]:
        return tuple(producer())

    @staticmethod
    def _generate_int() -> int:
        value = random.randint(1, 1001)
        return value

    @staticmethod
    def _generate_symbol() -> str:
        symbols_ = ["+", "-", "/", "*"]
        return symbols_[random.randint(0, 3)]

    def generate_structure_(self):
        structure_ = (
            f"{self._generate_int()}",
            f"{self._generate_int()} {self._generate_symbol()} {self._generate_int()}",
        )
        structure_zero_div_ = " " + "/" + " " + "0" + " "
        value_for_sub = self._generate_int()
        structure_sub_zero_div_ = (
            "(" + str(value_for_sub) + " - " + str(value_for_sub) + ")"
        )
        structure_passing_ = (
            "("
            + (
                structure_[1]
                + ")"
                + " "
                + self._generate_symbol()
                + " "
                + structure_[0]
            ),
            (structure_[1]),
            ("(" + structure_[1] + ")"),
            (
                structure_[0]
                + " "
                + self._generate_symbol()
                + " "
                + "("
                + structure_[1]
                + ")"
            ),
        )
        structure_failing_ = (
            ("(" + structure_[1] + ")" + structure_zero_div_),
            (
                structure_[0]
                + structure_zero_div_
                + self._generate_symbol()
                + " "
                + structure_[0]
            ),
            (structure_[0] + structure_zero_div_),
            (structure_[0] + " / " + structure_sub_zero_div_),
        )
        return (
            structure_passing_[random.randint(0, 3)],
            structure_failing_[random.randint(0, 3)],
        )


class ExpressionUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, ExpressionTestGenerator
):
    def _generate_one(
        self,
    ) -> tuple:
        return self.generate_values(self.generate_structure_)

    @staticmethod
    def _get_assert(
        expected: str,
        result: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="evaluate"),
                        args=(
                            [
                                ast.Constant(value=result),
                            ],
                        ),
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
        ]

    @staticmethod
    def _get_assert_with_error_(
        expected: ZeroDivisionError | str,
        result: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertRaises"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="evaluate"),
                        args=(
                            [
                                ast.Constant(value=result),
                            ],
                        ),
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="expression.evaluate",
                names=[
                    ast.alias(name="evaluate"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="expression.expr.arithmetic",
                names=[
                    ast.alias(name="Constant"),
                    ast.alias(name="Div"),
                    ast.alias(name="Add"),
                    ast.alias(name="Mul"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="expression.expr.parse",
                names=[
                    ast.alias(name="parse"),
                ],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, generated_value = self._generate_one()
        print("fail :", generated_value)
        test = self.get_empty_test()
        test.body = self._get_assert_with_error_("ZeroDivisionError", generated_value)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_value, _ = self._generate_one()
        print("pass :", generated_value)
        test = self.get_empty_test()
        test.body = self._get_assert(eval(generated_value), generated_value)
        return test, TestResult.PASSING


class ExpressionSystemtestGenerator(SystemtestGenerator, ExpressionTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, generated_value = self.generate_values(self.generate_structure_)
        return f"{generated_value}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        generated_value, _ = self.generate_values(self.generate_structure_)
        return f"{generated_value}", TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<add_term>"],
    "<add_term>": ["<add_term> <add> <mul_term>", "<mul_term>"],
    "<mul_term>": ["<mul_term> <mul> <neg_term>", "<neg_term>"],
    "<neg_term>": ["<terminal>", "~ <terminal>"],
    "<terminal>": ["<int>", "(<add_term>)"],
    "<add>": srange("+-"),
    "<mul>": srange("*/"),
    "<int>": ["<digit><int>", "<digit>"],
    "<digit>": srange(string.digits),
}

assert is_valid_grammar(grammar)
