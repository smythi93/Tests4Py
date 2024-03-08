import ast
import os
import random
import string
import subprocess
from _ast import Call, ImportFrom
from math import cos as rcos
from math import sin as rsin
from math import sqrt as rsqrt
from math import tan as rtan
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_MAME = "calculator"


class Calculator(Project):
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
            github_url="https://github.com/smythi93/calculator",
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
            test_base=Path("test"),
            included_files=[os.path.join("src", "calc")],
        )


def register():
    Calculator(
        bug_id=1,
        buggy_commit_id="5d7f01c5497940b7415db22864100d90c575300f",
        fixed_commit_id="063d988682e407ad25cd94854f1b4d5e3dc282f8",
        test_files=[
            Path("tests", "test_calc.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_main_sqrt_0",
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_main_sqrt_neg",
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_sqrt_0",
            os.path.join("tests", "test_calc.py") + "::TestCalc::test_sqrt_neg",
        ],
        loc=20,
        unittests=CalculatorUnittestGenerator(),
        systemtests=CalculatorSystemtestGenerator(),
        api=Calculator1API(),
    )


class Calculator1API(API):
    def __init__(self, default_timeout=5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        from math import sqrt, cos, sin, tan
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        if b'ZeroDivisionError' in process.stderr:
            return TestResult.FAILING, f"{process.stderr}"
        try:
            expected = eval(process.args[2], {"sqrt": sqrt, "cos": cos, "sin": sin, "tan": tan})
            result = float(process.stdout.decode("utf8").strip())
            if abs(result - expected) < 0.0001:
                return TestResult.PASSING, ""
            else:
                return TestResult.FAILING, f"Expected {expected}, but was {result}"
        except ValueError as e:
            if b'ValueError' in process.stderr:
                return TestResult.PASSING, f"Expected ValueError"
        except NameError as e:
            if b'NameError' in process.stderr:
                return TestResult.PASSING, f"Expected NameError"


class CalculatorTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> int:
        return producer()

    @staticmethod
    def _generate_int() -> int:
        return random.randint(-9999, 9999)

    def _generate_float(self) -> float:
        return self._generate_int() + random.random()

    @staticmethod
    def sqrt(value):
        return rsqrt(value)

    @staticmethod
    def cos(value):
        return rcos(value)

    @staticmethod
    def sin(value):
        return rsin(value)

    @staticmethod
    def tan(value):
        return rtan(value)

    @staticmethod
    def main(argument):
        return eval(argument)


class CalculatorUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, CalculatorTestGenerator
):
    def _generate_one(
        self,
    ) -> [int, float]:
        return self.generate_values(
            random.choice((self._generate_int, self._generate_float))
        )

    @staticmethod
    def _get_assert(
        expected: Any,
        result: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="main"),
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

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="calc",
                names=[
                    ast.alias(name="main"),
                    ast.alias(name="sin"),
                    ast.alias(name="cos"),
                    ast.alias(name="tan"),
                    ast.alias(name="sqrt"),
                ],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        # Negative values and zero that make "sqrt" fail
        generated_value = self._generate_one()
        if generated_value > 0:
            while generated_value > 0:
                generated_value = self._generate_one()
                if generated_value <= 0:
                    break
        # "sin(x)" values that turns out negative and used in "sqrt"
        generated_value_sin = self._generate_one()
        if rsin(generated_value_sin) > 0:
            while rsin(generated_value_sin) > 0:
                generated_value_sin = self._generate_one()
                if rsin(generated_value_sin) <= 0:
                    break
        # "cos(x)" values that turns out negative and used in "sqrt"
        generated_value_cos = self._generate_one()
        if rcos(generated_value_cos) > 0:
            while rcos(generated_value_cos) > 0:
                generated_value_cos = self._generate_one()
                if rcos(generated_value_cos) <= 0:
                    break
        # "tan(x)" values that turns out negative and used in "sqrt"
        generated_value_tan = self._generate_one()
        if rtan(generated_value_tan) > 0:
            while rtan(generated_value_tan) > 0:
                generated_value_tan = self._generate_one()
                if rtan(generated_value_tan) <= 0:
                    break

        prospects = (
            f"sqrt({round(generated_value, 5)})",
            f"sqrt(sin({round(generated_value_sin, 5)}))",
            f"sqrt(cos({round(generated_value_cos, 5)}))",
            f"sqrt(tan({round(generated_value_tan, 5)}))",
            "sqrt(%f)" % round(generated_value, 5),
        )

        dice = random.randint(0, 4)
        test = self.get_empty_test()
        test.body = self._get_assert(-1, prospects[dice])
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_value = self._generate_one()
        if generated_value <= 0:
            while generated_value <= 0:
                generated_value = self._generate_one()
                if generated_value > 0:
                    break

        generated_value = round(generated_value, 5)
        functions = (
            [self.sin(generated_value), f"rsin({generated_value})"],
            [self.cos(generated_value), f"rcos({generated_value})"],
            [self.tan(generated_value), f"rtan({generated_value})"],
            [self.sqrt(generated_value), f"rsqrt({generated_value})"],
            [self.sin(generated_value), "rsin(%f)" % generated_value],
            [self.cos(generated_value), "rcos(%f)" % generated_value],
            [self.tan(generated_value), "rtan(%f)" % generated_value],
            [self.sqrt(generated_value), "rsqrt(%f)" % generated_value],
        )

        dice = random.randint(0, 7)
        test = self.get_empty_test()
        test.body = self._get_assert(
            functions[dice][0], str(self.main(functions[dice][1]))
        )
        return test, TestResult.PASSING


class CalculatorSystemtestGenerator(SystemtestGenerator, CalculatorTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        generated_value = self.generate_values(self._generate_int)
        if generated_value > 0:
            while generated_value > 0:
                generated_value = self.generate_values(self._generate_int)
                if generated_value < 0:
                    break
        # generated_value = rsqrt(generated_value)
        return f"sqrt({generated_value})", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        generated_value = self.generate_values(self._generate_int)
        if generated_value <= 0:
            while generated_value <= 0:
                generated_value = self.generate_values(self._generate_int)
                if generated_value > 0:
                    break
        generated_value_sin = self.generate_values(self._generate_int)
        if rsin(generated_value_sin) > 0:
            while rsin(generated_value_sin) > 0:
                generated_value_sin = self.generate_values(self._generate_int)
                if rsin(generated_value_sin) <= 0:
                    break
        # "cos(x)" values that turns out negative and used in "sqrt"
        generated_value_cos = self.generate_values(self._generate_int)
        if rcos(generated_value_cos) > 0:
            while rcos(generated_value_cos) > 0:
                generated_value_cos = self.generate_values(self._generate_int)
                if rcos(generated_value_cos) <= 0:
                    break
        # "tan(x)" values that turns out negative and used in "sqrt"
        generated_value_tan = self.generate_values(self._generate_int)
        if rtan(generated_value_tan) > 0:
            while rtan(generated_value_tan) > 0:
                generated_value_tan = self.generate_values(self._generate_int)
                if rtan(generated_value_tan) <= 0:
                    break
        possibilities_ = (
            ["sqrt", generated_value],
            ["sin", generated_value_sin],
            ["cos", generated_value_cos],
            ["tan", generated_value_tan],
        )
        spin_ = random.randint(0, 3)
        return (
            f"{possibilities_[spin_][1]}",
            TestResult.PASSING,
        )


grammar: Grammar = {
    "<start>": ["<structure_>"],
    "<structure_>": [
        "<integers_>",
        "<floats_>",
        "<string_>",
        "<string_>(<integers_>)",
        "<string_>(<floats_>)",
        "<string_>(<string_>(<integers_>))",
        "<string_>(<string_>(<floats_>))",
    ],
    "<string_>": ["<letter_><string_>", "<letter_>"],
    "<letter_>": srange(string.ascii_letters),
    "<floats_>": ["<float_>", "-<float_>"],
    "<float_>": ["<integer_>.<integer_>"],
    "<integers_>": ["<integer_>", "-<integer_>"],
    "<integer_>": ["<digit_><integer_>", "<digit_>"],
    "<digit_>": srange(string.digits),
}


assert is_valid_grammar(grammar)
