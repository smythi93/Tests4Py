import ast
import os
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

PROJECT_MAME = "markup"


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
            project_name=PROJECT_MAME,
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
            included_files=[os.path.join("src", PROJECT_MAME)],
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
        unittests=MarkupUnittestGenerator(),
        systemtests=MarkupSystemtestGenerator(),
        api=Markup1API(),
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
        unittests=MarkupUnittestGenerator(),
        systemtests=MarkupSystemtestGenerator(),
        api=Markup2API(),
    )


class Markup1API(API):
    def __init__(self, default_timeout=5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = list(map(str, process.args[0:]))
        result = str(process.stdout.decode("utf8"))
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class Markup2API(CLIAPI):
    def __init__(self, default_timeout=5):
        super().__init__(["markup"], default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = (str, process.args[1:])
        result = str(process.stdout.decode("utf8"))
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class MarkupTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> Tuple[str]:
        return str((producer()))

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
            '"Language"',
            '"Code"',
            '"Program"',
            '"Syntax"',
            '"Error"',
            '"Project"',
            '"Fundamental"',
            '"Book"',
            '"Usage"',
            "'Language'",
            "'Code'",
            "'Program'",
            "'Syntax'",
            "'Error'",
            "'Project'",
            "'Fundamental'",
            "'Book'",
            "'Usage'",
        ]

        l3 = [
            "is easy.",
            "is difficult.",
            "is hard.",
            "is complex.",
            "is good.",
            "is controversial.",
            "is cool.",
        ]

        return random.choice(l1) + " " + random.choice(l2) + " " + random.choice(l3)

    @staticmethod
    def html_markup_generator():
        html_markups = [
            ["<head>", "</head>"],
            ["<title>", "</title>"],
            ["<body>", "</body>"],
            ["<header>", "</header>"],
            ["<footer>", "</footer>"],
            ["<article>", "</article>"],
            ["<section>", "</section>"],
            ["<p>", "</p>"],
            ["<div>", "</div>"],
            ["<span>", "</span>"],
            ["<img>", "</img>"],
            ["<aside>", "</aside>"],
            ["<canvas>", "</canvas>"],
            ["<datalist>", "</datalist>"],
            ["<audio>", "</audio>"],
            ["<details>", "</details>"],
            ["<nav>", "</nav>"],
            ["<embed>", "</embed>"],
            ["<search>", "</search>"],
            ["<output>", "</output>"],
            ["<progress>", "</progress>"],
            ["<video>", "</video>"],
            ["<ul>", "</ul>"],
            ["<ol>", "</ol>"],
            ["<li>", "</li>"],
            ["<b>", "</b>"],
            ["<i>", "</i>"],
            ["<q>", "</q>"],
            ["<h1>", "</h1>"],
            ["<h5>", "</h5>"],
            ["<hr>", "</hr>"],
        ]
        number = random.randint(0, 30)
        first_tag, last_tag = html_markups[number]
        return first_tag, last_tag

    def generate_html_example(self) -> str:
        generated_string = self.generate_random_string()
        return generated_string


class MarkupUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, MarkupTestGenerator
):
    def generate_one(
        self,
    ) -> str:
        return self.generate_values(self.generate_html_example)

    @staticmethod
    def _get_assert(
        expected: str,
        result: str,
    ) -> List[ast.stmt]:
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

    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="markup",
                names=[ast.alias(name="remove_html_markup")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        without_tag = self.generate_one()
        if without_tag.__contains__('"'):
            without_tag = without_tag
        else:
            while not without_tag.__contains__('"'):
                without_tag = self.generate_one()
        first_tag, last_tag = self.html_markup_generator()
        with_tag = first_tag + without_tag + last_tag
        test = self.get_empty_test()
        test.body = self._get_assert(without_tag, with_tag)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        without_tag = self.generate_one()
        if not without_tag.__contains__('"'):
            without_tag = without_tag
        else:
            while without_tag.__contains__('"'):
                without_tag = self.generate_one()
        first_tag, last_tag = self.html_markup_generator()
        with_tag = first_tag + without_tag + last_tag
        test = self.get_empty_test()
        test.body = self._get_assert(without_tag, with_tag)
        return test, TestResult.PASSING


class MarkupSystemtestGenerator(SystemtestGenerator, MarkupTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        without_tag = self.generate_html_example()
        if without_tag.__contains__('"'):
            without_tag = without_tag
        else:
            while not without_tag.__contains__('"'):
                without_tag = self.generate_html_example()
        first_tag, last_tag = self.html_markup_generator()
        with_tag = first_tag + without_tag + last_tag
        return f"{with_tag}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        without_tag = self.generate_html_example()
        if without_tag.__contains__("'") or not without_tag.__contains__('"'):
            print("works")
        else:
            while not without_tag.__contains__("'"):
                without_tag = self.generate_html_example()
        first_tag, last_tag = self.html_markup_generator()
        with_tag = first_tag + without_tag + last_tag
        return f"{with_tag}", TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<html_>"],
    "<html_>": ["<structure>", "<quoted_structure>", "<keys_>"],
    "<quoted_structure>": ['"' "<structure>" '"'],
    "<structure>": ["<opening><keys_><closing>"],
    "<opening>": ["<" "<tag>" ">"],
    "<closing>": ["</" "<tag>" ">"],
    "<tag>": [
        "head",
        "title",
        "body",
        "header",
        "footer",
        "article",
        "section",
        "p",
        "div",
        "span",
        "img",
        "aside",
        "audio",
        "canvas",
        "datalist",
        "details",
        "embed",
        "nav",
        "search",
        "output",
        "progress",
        "video",
        "ul",
        "ol",
        "li",
        "b",
        "i",
        "q",
        "h1",
        "h5",
        "hr",
    ],
    "<keys_>": ["<key_><keys_>", "", " "],
    "<key_>": srange(string.printable),
}

assert is_valid_grammar(grammar)
