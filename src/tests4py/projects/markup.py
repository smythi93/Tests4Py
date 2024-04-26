import ast
import os
import random
import re
import string
import subprocess
from _ast import Call, ImportFrom
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up, get_string_rule
from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_MAME = "markup"


class Markup(Project):
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
            github_url="https://github.com/smythi93/markup",
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
            relevant_test_files=relevant_test_files,
        )


def register():
    Markup(
        bug_id=1,
        buggy_commit_id="edce326b0518e08a1f296f8704bf97f4688be3d1",
        fixed_commit_id="638fdb1cf9f27136629b9240efbed08626f905fd",
        test_files=[
            Path("tests", "test_markup.py"),
        ],
        test_cases=[os.path.join("tests", "test_markup.py") + "::test_quoted_abc"],
        unittests=MarkupUnittestGenerator(),
        systemtests=MarkupSystemtestGenerator(),
        api=MarkupAPI(),
    )
    Markup(
        bug_id=2,
        buggy_commit_id="809eefd11860c0dd5c9b4911c1a8cf17e9e63624",
        fixed_commit_id="4a9dd7d2230ee361dfbfc7f53eb9e7db8ecaed42",
        test_files=[
            Path("tests", "test_markup.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_markup.py") + "::test_abc",
            os.path.join("tests", "test_markup.py") + "::test_quoted_abc",
        ],
        unittests=MarkupUnittestGenerator(),
        systemtests=MarkupSystemtestGenerator(),
        api=MarkupAPI(),
    )


class MarkupAPI(API):
    def __init__(self, default_timeout=5):
        super().__init__(default_timeout=default_timeout)
        self.pattern = re.compile("<[^<>]*>")

    def get_test_arguments_from_string(self, s: str) -> List[str]:
        return [s]

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = re.sub(self.pattern, "", process.args[2]).strip()
        expected = expected.replace("^", "")
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, f"Expected {expected}"
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class MarkupTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> str:
        return str(producer())

    @staticmethod
    def generate_random_string():
        return "".join(random.choices(string.ascii_letters, k=random.randint(10, 30)))

    @staticmethod
    def html_markup_generator():
        html_ = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 15)))
        if len(html_) == 1 and html_.startswith("h"):
            short_html_ = str(random.randint(1, 6))
            html_ = html_ + short_html_

        return html_


class MarkupUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, MarkupTestGenerator
):
    def generate_one(
        self,
    ) -> str:
        return self.generate_values(self.generate_random_string)

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
                        func=ast.Name(id="remove_html_markup"),
                        args=[ast.Constant(value=result)],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="markup",
                names=[ast.alias(name="remove_html_markup")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_string = self.generate_one()
        prospects = ([f'""{generated_string}""', f'""{generated_string}""'],)
        print("Failing Test : ", prospects[0])
        test = self.get_empty_test()
        test.body = self._get_assert(prospects[0][0], prospects[0][1])
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_string = self.generate_one()
        html_ = self.html_markup_generator()
        prospects = [f"{generated_string}", f"<{html_}>{generated_string}</{html_}>"]
        print("Passing Test : ", prospects[0])
        test = self.get_empty_test()
        test.body = self._get_assert(prospects[0], prospects[1])
        return test, TestResult.PASSING


class MarkupSystemtestGenerator(SystemtestGenerator, MarkupTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        generated_string = self.generate_values(self.generate_random_string)
        prospects = [f"'\"{generated_string}\"'"]
        print("Failing System Test : ", prospects[0])
        return f"{prospects[0]}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        generated_string = self.generate_values(self.generate_random_string)
        html_ = self.html_markup_generator()
        prospects = [f"<{html_}>{generated_string}</{html_}>"]
        print("Passing System Test : ", prospects[0])
        return f"{prospects[0]}", TestResult.PASSING


grammar: Grammar = clean_up(
    dict(
        **{
            "<start>": ["<structure>"],
            "<structure>": [
                "<string>",
                "<html><structure>",
                "<string><html><structure>",
            ],
            "<html>": ["<open><structure><close>"],
            "<open>": ["<LPAR><string><RPAR>"],
            "<close>": ["<LPAR>/<string><RPAR>"],
            "<LPAR>": ["<"],
            "<RPAR>": [">"],
            "<identifier>": ["<id_char><id_chars>"],
            "<id_char>": srange(string.ascii_letters),
            "<id_chars>": ["", "<id_char_follow><id_chars>"],
            "<id_char_follow>": srange(string.ascii_letters + string.digits + "_"),
        },
        **get_string_rule(srange(string.printable.replace("<", "").replace(">", ""))),
    )
)

assert is_valid_grammar(grammar)
