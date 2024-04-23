import ast
import random
import string
import subprocess
from _ast import Call, ImportFrom, Assign, Expr
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

PROJECT_MAME = "spacy"


class SpaCy(Project):
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
            github_url="https://github.com/explosion/spaCy",
            status=Status.OK,
            python_version="3.7.7",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version="3.7.8",
            python_fallback_version="3.7.8",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
            loc=loc,
            relevant_test_files=relevant_test_files,
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
            ],
        )  # TODO adjust parameters

    def patch(self, location: Path):
        with open(location / "pyproject.toml", "r") as fp:
            content = fp.read()
        content = content.replace(
            "cython>=0.25",
            "cython==0.29.19",
        )
        with open(location / "pyproject.toml", "w") as fp:
            fp.write(content)


def register():
    SpaCy(
        bug_id=1,
        buggy_commit_id="9ce059dd067ecc3f097d04023e3cfa0d70d35bb8",
        fixed_commit_id="a987e9e45d4084f30964a4cec9914ae6ed25a73c",
        test_files=[Path("spacy", "tests", "test_errors.py")],
        test_cases=["spacy/tests/test_errors.py::test_add_codes"],
        api=SpaCyAPI1(),
        unittests=SpaCyUnittestGenerator1(),
        systemtests=SpaCySystemtestGenerator1(),
    )
    SpaCy(
        bug_id=2,
        buggy_commit_id="efec28ce70a0ff69471cc379867deebe7eb881e0",
        fixed_commit_id="cfdaf99b8029d6762730c5d5bd2b6f6c173c1241",
        test_files=[Path("spacy", "tests", "regression", "test_issue5137.py")],
        test_cases=["spacy/tests/regression/test_issue5137.py::test_issue5137"],
        api=SpaCyAPI2(),
        unittests=SpaCyUnittestGenerator2(),
        systemtests=SpaCySystemtestGenerator2(),

    )
    SpaCy(
        bug_id=3,
        buggy_commit_id="dac70f29eb3b1f21ae9e2c6346666bf6a46307b6",
        fixed_commit_id="663333c3b2bad90915d1a48a626ca1275b7ef077",
        test_files=[Path("spacy", "tests", "regression", "test_issue5314.py")],
        test_cases=["spacy/tests/regression/test_issue5314.py::test_issue5314"],
        api=SpaCyAPI3(),
        unittests=SpaCyUnittestGenerator3(),
        systemtests=SpaCySystemtestGenerator3(),
    )
    SpaCy(
        bug_id=4,
        buggy_commit_id="abd5c06374eab5db0cf897b73543b1f3eb007e12",
        fixed_commit_id="9fa9d7f2cb52ce6a70c264d4e57c7f190d7686bf",
        test_files=[Path("spacy", "tests", "regression", "test_issue4665.py")],
        test_cases=["spacy/tests/regression/test_issue4665.py::test_issue4665"],
        api=SpaCyAPI4(),
        unittests=SpaCyUnittestGenerator4(),
        systemtests=SpaCySystemtestGenerator4(),
    )
    SpaCy(
        bug_id=5,
        buggy_commit_id="bdfb696677a7591ced018e7597c00929e97c6837",
        fixed_commit_id="3bd15055ce74b04dcaf3b9abe2adeb01fb595776",
        test_files=[Path("spacy", "tests", "test_language.py")],
        test_cases=["spacy/tests/test_language.py::test_evaluate_no_pipe"],
    )
    SpaCy(
        bug_id=6,
        buggy_commit_id="6b874ef09611ac32ad038203423d44087cbeb3ae",
        fixed_commit_id="afe4a428f78abe45d6104d74ef42a066570fa43d",
        test_files=[Path("spacy", "tests", "pipeline", "test_analysis.py")],
        test_cases=[
            "spacy/tests/pipeline/test_analysis.py::test_analysis_validate_attrs_remove_pipe"
        ],
    )
    SpaCy(
        bug_id=7,
        buggy_commit_id="da6e0de34f4947fdebc839df3969c641014cfa97",
        fixed_commit_id="6f54e59fe7ccb3bacce896ed33d36b39f11cbfaf",
        test_files=[Path("spacy", "tests", "doc", "test_span.py")],
        test_cases=["spacy/tests/doc/test_span.py::test_filter_spans"],
    )
    SpaCy(
        bug_id=8,
        buggy_commit_id="fa95c030a511337935d1a2e930cb954c7a4cd376",
        fixed_commit_id="5efae495f18f37316bd641a05ca26e62cb78e242",
        test_files=[Path("spacy", "tests", "matcher", "test_matcher_logic.py")],
        test_cases=["spacy/tests/matcher/test_matcher_logic.py::test_matcher_remove"],
    )
    SpaCy(
        bug_id=9,
        buggy_commit_id="bc7e7db208d351fae2982afbcdff7633f9636779",
        fixed_commit_id="3297a19545027c8d8550b1ae793ce290567eff32",
        test_files=[Path("spacy", "tests", "pipeline", "test_tagger.py")],
        test_cases=[
            "spacy/tests/pipeline/test_tagger.py::test_tagger_warns_no_lemma_lookups"
        ],
    )
    SpaCy(
        bug_id=10,
        buggy_commit_id="38de08c7a99d5d8c490223126071afe7dd4f4b67",
        fixed_commit_id="52904b72700a3f301a26563d3f94493bad96a446",
        test_files=[Path("spacy", "tests", "matcher", "test_matcher_api.py")],
        test_cases=[
            "spacy/tests/matcher/test_matcher_api.py::test_matcher_valid_callback"
        ],
    )


class SpaCyAPI1(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI2(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI3(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI4(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> str:
        return producer()

    @staticmethod
    def generate_random_string():
        return "".join(random.choices(string.ascii_letters, k=random.randint(5, 15)))

    @staticmethod
    def spacy1_generate():
        warnings_randomised1 = random.randint(1, 9)
        warnings_randomised2 = random.randint(10, 29)
        errors_randomised1 = random.randint(1, 9)
        errors_randomised2 = random.randint(10, 100)
        errors_randomised3 = random.randint(100, 197)

        passing = (f"W00{warnings_randomised1}", f"W0{warnings_randomised2}",
                   f"E00{errors_randomised1}", f"E0{errors_randomised2}", f"E{errors_randomised3}",
                   f"T003", f"T004", f"T007", f"T008")
        return passing[random.randint(0, len(passing) - 1)]

    @staticmethod
    def spacy2_generate():
        return ""

    @staticmethod
    def spacy3_generate():
        return ""

    @staticmethod
    def spacy4_generate():
        return ""


class SpaCyUnittestGenerator1(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy1_generate)

    @staticmethod
    def _get_assert(
            expected: str,
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="warnings_with_codes")],
                value=ast.Call(
                    func=ast.Name(id="add_codes"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="Warnings"),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id="errors_with_codes")],
                value=ast.Call(
                    func=ast.Name(id="add_codes"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="Errors"),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
            ast.Assign(
                targets=[ast.Name(id="temp_errors_with_codes")],
                value=ast.Call(
                    func=ast.Name(id="add_codes"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="TempErrors"),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=3,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"),
                        attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=""),
                        ast.Call(
                            func=ast.Name(id="__getattribute__"),
                            args=[
                                ast.Name(id="errors_with_codes"),
                                ast.Constant(value="E001")
                            ],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                ),
                lineno=4
            )]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="add_codes")],
                level=0,
            ),
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Warnings")],
                level=0,
            ),
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Errors")],
                level=0,
            ),
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="TempErrors")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert("")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert("")
        return test, TestResult.PASSING


class SpaCyUnittestGenerator2(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy2_generate)

    @staticmethod
    def _get_assert(
            expected: str,
            model_path: str,
            meta: bool,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="load_model_from_path"),
                        args=[
                            ast.Constant(value=model_path),
                            #ast.Constant(value=meta),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.util",
                names=[ast.alias(name="load_model_from_path")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert("", "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert("", "")
        return test, TestResult.PASSING


class SpaCyUnittestGenerator3(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy3_generate)

    @staticmethod
    def _get_assert(
            expected: str,
            article_title: str,
            article_text: str,
            wp_to_id: dict,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="_process_wp_text"),
                        args=[
                            ast.Constant(value=article_title),
                            ast.Constant(value=article_text),
                            ast.Constant(value=wp_to_id)
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="bin.wiki_entity_linking.wikipedia_processor",
                names=[ast.alias(name="_process_wp_text")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fail_ = self._generate_one()
        article_title = "Artificial intelligence"  # Title of the Wikipedia article
        article_text = """
            <text xml:space="preserve">
                Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.
                Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
                Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
            </text>
        """  # Raw text content of the Wikipedia article
        wp_to_id = {"Artificial intelligence": "Q11660", "Machine learning": "Q2539"}  # Dictionary mapping Wikipedia page titles to IDs
        test = self.get_empty_test()
        test.body = self._get_assert("", article_title, article_text, wp_to_id)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert("", "", "", "")
        return test, TestResult.PASSING


class SpaCyUnittestGenerator4(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy4_generate)

    @staticmethod
    def _get_assert(
            expected: str,
            article_title: str,
            article_text: str,
            wp_to_id: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="_process_wp_text"),
                        args=[
                            ast.Constant(value=article_title),
                            ast.Constant(value=article_text),
                            ast.Constant(value=wp_to_id)
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="bin.wiki_entity_linking.wikipedia_processor",
                names=[ast.alias(name="_process_wp_text")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fail_ = self._generate_one()

        test = self.get_empty_test()
        test.body = self._get_assert("", "", "", "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert("", "", "", "")
        return test, TestResult.PASSING


class SpaCySystemtestGenerator1(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy1_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy1_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator2(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy2_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy2_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator3(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy3_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy3_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator4(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy4_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy4_generate)
        return f"{pass_}", TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<structure_>"],
    "<structure_>": ["<str_int_sym_><structure_>"],
    "<str_int_sym_>": [
        "<string_><str_int_sym_>",
        "<integer_><str_int_sym_>",
        "<symbols_><str_int_sym_>",
        " ",
    ],
    "<string_>": ["<char_><string_>", "<char_>", ""],
    "<integer_>": ["<digit_><integer_>", "<digit_>", ""],
    "<symbols_>": ["<symbol_><symbols_>", "<symbol_>", ""],
    "<symbol_>": srange(string.punctuation),
    "<digit_>": srange(string.digits),
    "<char_>": srange(string.ascii_letters),
}
assert is_valid_grammar(grammar)
