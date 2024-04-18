import ast
import os
import random
import string
import subprocess
from _ast import Call
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up, CLI_GRAMMAR, INTEGER
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult, CLIAPI

PROJECT_MAME = "middle"


class Middle(Project):
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
            github_url="https://github.com/smythi93/middle",
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
            relevant_test_files=relevant_test_files,
        )


def register():
    Middle(
        bug_id=1,
        buggy_commit_id="15350ede14501997656f2fd49bd5b9af2c8d2582",
        fixed_commit_id="c0e7b35b1fba9320fe40fe143c89f6b4c7c8979d",
        test_files=[
            Path("tests", "test_middle.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_middle.py::TestMiddle::test_middle_213")
        ],
        relevant_test_files=[Path("tests", "test_middle.py")],
        unittests=MiddleUnittestGenerator(),
        systemtests=MiddleSystemtestGenerator(),
        api=Middle1API(),
        loc=25,
    )
    Middle(
        bug_id=2,
        buggy_commit_id="eed99fa2741bd28744231dfcac0ea34679532bf9",
        fixed_commit_id="029cb8beb7bfc0f2853dfa9504dcdfcc753b051e",
        test_files=[
            Path("tests", "test_middle.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_middle.py::TestMiddle::test_middle_213"),
        ],
        relevant_test_files=[Path("tests", "test_middle.py")],
        unittests=MiddleUnittestGenerator(),
        systemtests=MiddleSystemtestGenerator(),
        api=Middle2API(),
        loc=12,
    )


class MiddleAPI:
    @staticmethod
    def support_oracle(
        args: Any, num_args_to_ignore: int = 1
    ) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        _, expected, _ = sorted(list(map(int, process.args[num_args_to_ignore:])))
        result = int(process.stdout.decode("utf8"))
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class Middle1API(CLIAPI, MiddleAPI):
    def __init__(self, default_timeout=5):
        super().__init__(["middle"], default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        return self.support_oracle(args, 1)


class Middle2API(API, MiddleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        return self.support_oracle(args, 2)


class MiddleTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> Tuple[Any, Any, Any]:
        return tuple(sorted((producer(), producer(), producer())))

    @staticmethod
    def generate_int() -> int:
        return random.randint(-9999, 9999)


class MiddleUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, MiddleTestGenerator
):
    def _generate_float(self) -> float:
        return self.generate_int() + random.random()

    @staticmethod
    def _generate_str():
        return "".join(random.choices(string.printable, k=random.randint(0, 100)))

    def _generate_bytes(self):
        return self._generate_str().encode("utf8")

    def _generate_three(
        self,
    ) -> (
        Tuple[int, int, int]
        | Tuple[float, float, float]
        | Tuple[str, str, str]
        | Tuple[bytes, bytes, bytes]
    ):
        return self.generate_values(
            random.choice(
                (
                    self.generate_int,
                    self._generate_float,
                    self._generate_str,
                    self._generate_bytes,
                )
            )
        )

    @staticmethod
    def _get_assert(
        expected: int | float | str | bytes,
        x: int | float | str | bytes,
        y: int | float | str | bytes,
        z: int | float | str | bytes,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="middle"),
                        args=[
                            ast.Constant(value=x),
                            ast.Constant(value=y),
                            ast.Constant(value=z),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="middle",
                names=[ast.alias(name="middle")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        x, y, z = self._generate_three()
        while not x < y < z:
            x, y, z = self._generate_three()
        test = self.get_empty_test()
        test.body = self._get_assert(y, y, x, z)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        values = list(self._generate_three())
        middle = values[1]
        while values[1] < values[0] < values[2]:
            random.shuffle(values)
        test = self.get_empty_test()
        x, y, z = values
        test.body = self._get_assert(middle, x, y, z)
        return test, TestResult.PASSING


class MiddleSystemtestGenerator(SystemtestGenerator, MiddleTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        x, y, z = self.generate_values(self.generate_int)
        while not x < y < z:
            x, y, z = self.generate_values(self.generate_int)
        return f"{y}\n{x}\n{z}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        values = list(self.generate_values(self.generate_int))
        while values[1] < values[0] < values[2]:
            random.shuffle(values)
        x, y, z = values
        return f"{x}\n{y}\n{z}", TestResult.PASSING


grammar: Grammar = clean_up(
    dict(
        CLI_GRAMMAR,
        **{
            "<start>": ["<arg> <arg> <arg>"],
            "<escaped>": ["<integer>"],
            "<unescaped>": ["<integer>"],
        },
        **INTEGER,
    )
)


assert is_valid_grammar(grammar)
