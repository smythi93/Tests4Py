import os
import ast
import random
import string
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable

from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult, CLIAPI

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
            setup=[[PYTHON, "-m", "pip", "install", "."]],
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

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        print("args", args)
        expected = process.args[2:]
        result = process.stdout.decode("utf8")
        print("Expected : ", expected)
        print("Result : ", result)
        if result == expected:
            return TestResult.PASSING, f"Expected {expected}, but was {result}"
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class ExpressionTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> Tuple[Any]:
        return producer()

    @staticmethod
    def _generate_int() -> int:
        value = random.randint(1, 101)
        #   if value < 0:
        #       value = "( %d )" % value
        return value

    @staticmethod
    def _generate_symbol() -> str:
        symbols_ = ["+", "-", "/", "*"]
        return symbols_[random.randint(0, 3)]

    def _generate_structure(self):
        structures_ = (
            f"{self._generate_int()}",
            f"{self._generate_int()} {self._generate_symbol()} {self._generate_int()}",
            f"( {self._generate_int()} {self._generate_symbol()} {self._generate_int()} )",
        )
        structures_2_ = (
            f"{self._generate_int()}",
            f"{self._generate_int()} {self._generate_symbol()} {self._generate_int()}",
            f"( {self._generate_int()} )",
            f"( {self._generate_int()} {self._generate_symbol()} {self._generate_int()} )",
        )

        structure_ = (
            " "
            + structures_[random.randint(0, 2)]
            + " "
            + self._generate_symbol()
            + " "
            + structures_2_[random.randint(0, 3)]
            + " "
        )
        print(structure_)
        return structure_


class ExpressionUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, ExpressionTestGenerator
):
    def _generate_one(
        self,
    ) -> str:
        return self.generate_values(self._generate_structure)

    @staticmethod
    def _get_assert(
        expected: Any,
        result: str,
    ) -> List[ast.stmt]:
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
            )
        ]

    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="expression.evaluate",
                names=[
                    ast.alias(name="evaluate"),
                ],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_value = self._generate_one()
        generated_value = generated_value.replace(" ", "")
        asssert: eval(generated_value)
        if ZeroDivisionError:
            generated_value = self._generate_one()
            generated_value = generated_value.replace(" ", "")
        print("gen value failing : ", generated_value)
        test = self.get_empty_test()
        test.body = self._get_assert(eval(str(generated_value)), generated_value)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_value = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(eval(str(generated_value)), generated_value)
        return test, TestResult.PASSING


class ExpressionSystemtestGenerator(SystemtestGenerator, ExpressionTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        generated_value = self.generate_values(self._generate_structure)
        generated_value = generated_value.replace(" ", "")
        print("generated_value : ", generated_value)
        generated_value = " ( 30 / 5 ) / ( 3 + 3 ) "
        print("generated_value : ", type(generated_value))
        return f"{generated_value}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        generated_value = self.generate_values(self._generate_structure)
        print("generated_value : ", generated_value)
        generated_value = " ( 30 / 5 ) / ( 3 + 3 ) "
        print("generated_value : ", type(generated_value))
        return f"{generated_value}", TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<expression_p>", "<expression_f>"],
    "<expression_p>": [
        " <integers_> ",
        " ( <integers_> ) ",
        " <integers_> <symbol_> <integers_> ",
        " ( <integers_> <symbol_> <integers_> ) <symbol_> <integers_> ",
        " <integers_> <symbol_> ( <integers_> <symbol_> <integers_> ) ",
        " <integers_> <symbol_> ( <integers_> ) <symbol_> <integers_> ",
        " <integers_> <symbol_> <integers_> <symbol_> ( <integers_> ) ",
        " ( <integers_> <symbol_> <integers_> ) ",
        " ( <integers_> <symbol_> <integers_> ) <symbol_> <integers_> <symbol_> <integers_> ",
        " <integers_> <symbol_> <integers_> <symbol_> ( <integers_> <symbol_> <integers_> ) ",
        " <integers_> <symbol_> ( <integers_> <symbol_> <integers_> ) <symbol_> <integers_> ",
        " <integers_> <symbol_> <integers_> <symbol_> <integers_> <symbol_> <integers_> ",
        " ( <integers_> <symbol_> <integers_> ) <symbol_> ( <integers_> <symbol_> <integers_> ) ",
    ],
    "<expression_f>": [
        "<integers_>",
        "(<integers_>)",
        "<integers_><symbol_><integers_>",
        "(<integers_><symbol_><integers_>)<symbol_><integers_>",
        "<integers_><symbol_>(<integers_><symbol_><integers_>)",
        "<integers_><symbol_>(<integers_>)<symbol_><integers_>",
        "<integers_><symbol_><integers_><symbol_>(<integers_>)",
        "(<integers_><symbol_><integers_>)",
        "(<integers_><symbol_><integers_>)<symbol_><integers_><symbol_><integers_>",
        "<integers_><symbol_><integers_><symbol_>(<integers_><symbol_><integers_>)",
        "<integers_><symbol_>(<integers_><symbol_><integers_>)<symbol_><integers_>",
        "<integers_><symbol_><integers_><symbol_><integers_><symbol_><integers_>",
        "(<integers_><symbol_><integers_>)<symbol_>(<integers_><symbol_><integers_>)",
    ],
    "<symbol_>": ["+", "-", "/", "*"],
    "<integers_>": ["<integer_>", "-<integer_>"],
    "<integer_>": ["<digit_><integer_>", "<digit_>"],
    "<digit_>": srange(string.digits),
}

assert is_valid_grammar(grammar)
