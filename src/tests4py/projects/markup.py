import ast
import os
import random
import string
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable

from tests4py.grammars import python
from tests4py.constants import PYTHON
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult, CLIAPI


class Markup(Project):
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
            project_name="markup",
            github_url="https://github.com/smythi93/markup",
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
    Markup(
        bug_id=1,
        buggy_commit_id="edce326b0518e08a1f296f8704bf97f4688be3d1",
        fixed_commit_id="638fdb1cf9f27136629b9240efbed08626f905fd",
        test_file=[
            Path("tests", "test_markup.py"),
        ],
        test_cases=[os.path.join("tests", "test_markup.py") + "::test_quoted_abc"],
    )
    Markup(
        bug_id=2,
        buggy_commit_id="809eefd11860c0dd5c9b4911c1a8cf17e9e63624",
        fixed_commit_id="4a9dd7d2230ee361dfbfc7f53eb9e7db8ecaed42",
        test_file=[
            Path("tests", "test_markup.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_markup.py") + "::test_abc",
            os.path.join("tests", "test_markup.py") + "::test_quoted_abc",
        ],
    )


class MarkupTestGenerator:
    @staticmethod
    def remove_html_markup_correctly(self, s):
        in_tag = False
        in_quote = False
        out = []

        for char in s:
            print(char)
            if char == "<" and not in_quote:
                in_tag = True
            elif char == ">" and not in_quote:
                in_tag = False
                continue
            elif (char == '"' or char == "'") and in_tag:
                in_quote = not in_quote
            elif not in_tag:
                out.append(char)

        return "".join(out)

    @staticmethod
    def remove_html_markup_wrongly(self, s):
        out = ""
        quote = False
        tag = True

        for c in s:
            if c == "<" and not quote:
                tag = True
            elif c == ">" and not quote:
                tag = False
            elif c == '"' or c == "'" and tag:
                quote = not quote
            elif not tag:
                out = out + c

        return out

    @staticmethod
    def generate_random_string():
        l1 = [
            "Python",
            "Java",
            "C++",
            "JavaScript",
            "Ruby",
            "C",
            "Rust",
            "Pearl",
            "Matlab",
            "PHP",
            "C#",
            "R",
        ]

        l2 = [
            "Language",
            "Code",
            "Program",
            "Syntax",
            "Error",
            "Project",
            "Fundamental",
            "Book",
            "Usage",
        ]

        l3 = [
            "is easy.",
            "is difficult",
            "is hard",
            "is complex",
            "is good",
            "is controversial",
            "is cool",
        ]

        return random.choice(l1) + " " + random.choice(l2) + " " + random.choice(l3)

    @staticmethod
    def html_markup_generator():
        html_markups = [
            "<head>",
            "<title>",
            "<body>",
            "<header>",
            "<footer>",
            "<article>",
            "<section>",
            "<p>",
            "<div>",
            "<span>",
            "<img>",
            "<aside>",
            "<audio>",
            "<canvas>",
            "<datalist>",
            "<details>",
            "<embed>",
            "<nav>",
            "<search>",
            "<output>",
            "<progress>",
            "<video>",
            "<ul>",
            "<ol>",
            "<li>",
            "<b>",
            "<i>",
            "<q>",
            "<h1>",
            "<h5>",
            "<hr>",
        ]
        chosen_markup = random.choice(html_markups)
        return chosen_markup

    @staticmethod
    def generate_html_example(self):
        return self.chosen_markup + self.generate_random_string() + self.chosen_markup


class MarkupUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, MarkupTestGenerator
):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_value = self.generate_html_example()
        wrong_value = self.remove_html_markup_wrongly(generated_value)
        test = self.get_empty_test()
        test.body = self._get_assert(wrong_value, generated_value)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        generated_value = self.generate_html_example()
        correct_value = self.remove_html_markup_correctly(generated_value)
        test = self.get_empty_test()
        test.body = self._get_assert(correct_value, generated_value)
        return test, TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<string>"],
    "<string>": ["<string>"],
}


assert is_valid_grammar(grammar)
