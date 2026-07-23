import abc
import ast
import base64
import os.path
import random
import string
import subprocess
from pathlib import Path
from typing import List, Optional, Any, Tuple

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "black"


class Black(Project):
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
        grammar: Optional[Grammar] = None,
        loc: int = 0,
        blackd: bool = False,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/psf/black",
            status=Status.OK,
            python_version="3.8.4",
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
            source_base=[Path("black.py"), Path("blib2to3")]
            + ([Path("blackd.py")] if blackd else []),
            test_base=Path("tests"),
            included_files=["black.py"] + (["blackd.py"] if blackd else list()),
            relevant_test_files=[Path("tests", "test_black.py")],
        )


def register():
    Black(
        bug_id=1,
        buggy_commit_id="26c9465a22c732ab1e17b0dec578fa3432e9b558",
        fixed_commit_id="c0a7582e3d4cc8bec3b7f5a6c52b36880dcb57d7",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_black.py::BlackTestCase::test_works_in_mono_process_only_environment",
            ),
        ],
        test_status_fixed=TestStatus.FAILING,
        api=Black1API(),
        unittests=Black1UnittestGenerator(),
        systemtests=Black1SystemtestGenerator(),
        grammar=grammar_black_mono,
        blackd=True,
        loc=5480,
    )
    Black(
        bug_id=2,
        buggy_commit_id="c8ca6b2b9ff3510bee12129824cebfc2fc51e5b2",
        fixed_commit_id="892eddacd215d685e136686b7f629ade70adca83",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_fmtonoff4"),
        ],
        api=Black2API(),
        unittests=Black2UnittestGenerator(),
        systemtests=Black2SystemtestGenerator(),
        grammar=grammar_black_pair,
        blackd=True,
        loc=4514,
    )
    Black(
        bug_id=3,
        buggy_commit_id="8126b4f6a9342290de4655e6a8a78cd288ce7daa",
        fixed_commit_id="7a14a37981862ef418f3cdb4a7e2375856f97529",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_invalid_config_return_code"
            ),
        ],
        api=Black3API(),
        unittests=Black3UnittestGenerator(),
        systemtests=Black3SystemtestGenerator(),
        grammar=grammar_black_config,
        blackd=True,
        loc=4508,
    )
    Black(
        bug_id=4,
        buggy_commit_id="65ea568e3301951f26e0e3b98f6d5dc80132e917",
        fixed_commit_id="c7495b9aa098ef7a358fc74556359d21c6a4ba11",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "beginning_backslash.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_beginning_backslash"
            ),
        ],
        api=Black4API(),
        unittests=Black4UnittestGenerator(),
        systemtests=Black4SystemtestGenerator(),
        grammar=grammar_black_pair,
        blackd=True,
        loc=4428,
    )
    Black(
        bug_id=5,
        buggy_commit_id="1bbb01b854d168d76ebe4bf78961c2152ae075d9",
        fixed_commit_id="9394de150ebf0adc426523f46dc08e8b2b2b0b63",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_function_trailing_comma"
            ),
        ],
        api=Black5API(),
        unittests=Black5UnittestGenerator(),
        systemtests=Black5SystemtestGenerator(),
        grammar=grammar_black_pair,
        blackd=True,
        loc=4392,
    )
    Black(
        bug_id=6,
        buggy_commit_id="8c8adedc2a74a494c24f93e405b6418ac32f54cd",
        fixed_commit_id="f8617f975d56e81cfb4070ce65584f7b29a77e7a",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comment_after_escaped_newline.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_async_as_identifier"
            ),
            os.path.join("tests", "test_black.py::BlackTestCase::test_python37"),
        ],
        api=Black6API(),
        unittests=Black6UnittestGenerator(),
        systemtests=Black6SystemtestGenerator(),
        grammar=grammar_black_pair,
        blackd=True,
        loc=4333,
    )
    Black(
        bug_id=7,
        buggy_commit_id="18119d38466652ae818436cb497f601294ed4558",
        fixed_commit_id="de806405d2934b629d67e2a6317ad7e826765a20",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "tupleassign.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_tuple_assign"),
        ],
        api=Black7API(),
        unittests=Black7UnittestGenerator(),
        systemtests=Black7SystemtestGenerator(),
        grammar=grammar_black_pair,
        blackd=True,
        loc=4311,
    )
    Black(
        bug_id=8,
        buggy_commit_id="e6ddb68c786256e1cb0c76b42d10c212ef34cb2a",
        fixed_commit_id="6b994fdb8ab70ce4c2eafb8f2f0ff2648f3ff1ef",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comments7.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_comments7"),
        ],
        api=Black8API(),
        unittests=Black8UnittestGenerator(),
        systemtests=Black8SystemtestGenerator(),
        grammar=grammar_black,
        blackd=True,
        loc=4305,
    )
    Black(
        bug_id=9,
        buggy_commit_id="026c81b83454f176a9f9253cbfb70be2c159d822",
        fixed_commit_id="d6db1c12a8e14833fe22da377cddc2bd1f43dc14",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "python2_print_function.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_python2_print_function"
            ),
        ],
        api=Black9API(),
        unittests=Black9UnittestGenerator(),
        systemtests=Black9SystemtestGenerator(),
        grammar=grammar_black,
        blackd=True,
        loc=4313,
    )
    Black(
        bug_id=10,
        buggy_commit_id="f6643c4f0cfbae1f2493fdfce46cfbae3d26f46b",
        fixed_commit_id="66aa676278948368dff251dffd58c850cb8b889e",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_comment_indentation"
            ),
        ],
        api=Black10API(),
        unittests=Black10UnittestGenerator(),
        systemtests=Black10SystemtestGenerator(),
        grammar=grammar_black_pair,
        blackd=True,
        loc=4232,
    )
    Black(
        bug_id=11,
        buggy_commit_id="283a5d53a8d57e8e186a08c9fbf249e1fbe7bc94",
        fixed_commit_id="024c9cab55da7bd3236fd88759c9735d6149b464",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comments6.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_comments6"),
        ],
        api=Black11API(),
        unittests=Black11UnittestGenerator(),
        systemtests=Black11SystemtestGenerator(),
        grammar=grammar_black,
        blackd=True,
        loc=4218,
    )
    Black(
        bug_id=12,
        buggy_commit_id="8b340e210271a8108995fd479c55dbc0a34466bd",
        fixed_commit_id="b53cb9474348e13533ccba3735191a55ef3da6c4",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "bracketmatch.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_bracket_match"),
        ],
        api=Black12API(),
        unittests=Black12UnittestGenerator(),
        systemtests=Black12SystemtestGenerator(),
        grammar=grammar_black,
        loc=4056,
    )
    Black(
        bug_id=13,
        buggy_commit_id="b719d85ccc330170e40b2617307a7e3b2a0bab14",
        fixed_commit_id="883689366ce0f0e0ddd66d81360c61abfd19b01a",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "python37.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_python37"),
        ],
        api=Black13API(),
        unittests=Black13UnittestGenerator(),
        systemtests=Black13SystemtestGenerator(),
        grammar=grammar_black,
        loc=4053,
    )
    Black(
        bug_id=14,
        buggy_commit_id="3bdd42389128bbbe8b64a8e050563f09bff99979",
        fixed_commit_id="dd8bde6d2fbfe8a7a11093e761a0cb5837efa96a",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_get_future_imports"
            ),
        ],
        api=Black14API(),
        unittests=Black14UnittestGenerator(),
        systemtests=Black14SystemtestGenerator(),
        grammar=grammar_black,
        loc=4046,
    )
    Black(
        bug_id=15,
        buggy_commit_id="8a8c58252cc023ae250d6febd24f50a8166450d4",
        fixed_commit_id="df2ae3bbe6c45298aabb6c04e85cb353205626f1",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "fmtonoff2.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_fmtonoff2"),
        ],
        api=Black15API(),
        unittests=Black15UnittestGenerator(),
        systemtests=Black15SystemtestGenerator(),
        grammar=grammar_black,
        loc=4110,
    )
    Black(
        bug_id=16,
        buggy_commit_id="fb34c9e19589d05f92084a28940837151251ebd6",
        fixed_commit_id="42a3fe53319a8c02858c2a96989ed1339f84515a",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_black.py::BlackTestCase::test_symlink_out_of_root_directory",
            ),
        ],
        api=Black16API(),
        unittests=Black16UnittestGenerator(),
        systemtests=Black16SystemtestGenerator(),
        grammar=grammar_black_symlink,
        loc=4058,
    )
    Black(
        bug_id=17,
        buggy_commit_id="bbc09a4f013f2a584f143f3f5e3f76f6082367d4",
        fixed_commit_id="7fc6ce990669464f5172b63fafa3724f5f308be3",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_empty"),
            os.path.join("tests", "test_black.py::BlackTestCase::test_empty_ff"),
        ],
        api=Black17API(),
        unittests=Black17UnittestGenerator(),
        systemtests=Black17SystemtestGenerator(),
        grammar=grammar_black_empty,
        loc=3973,
    )
    Black(
        bug_id=18,
        buggy_commit_id="dbe26161fa68632d608a440666a0960a32630902",
        fixed_commit_id="00a302560b92951c22f0f4c8d618cf63de39bd57",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_preserves_line_endings"
            ),
        ],
        api=Black18API(),
        unittests=Black18UnittestGenerator(),
        systemtests=Black18SystemtestGenerator(),
        grammar=grammar_black_newline,
        loc=3947,
    )
    Black(
        bug_id=19,
        buggy_commit_id="337a4199f90ca48a19cf26511e0cec330b13bd4e",
        fixed_commit_id="29e97d1d4a7717f1bd0ca35cacf2f2ce6d815b0c",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "comments6.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_black.py::BlackTestCase::test_comment_in_decorator"
            ),
        ],
        api=Black19API(),
        unittests=Black19UnittestGenerator(),
        systemtests=Black19SystemtestGenerator(),
        grammar=grammar_black,
        loc=3583,
    )
    Black(
        bug_id=20,
        buggy_commit_id="2e52a2b3ecc0fe025439c3db05a4457ab14f167b",
        fixed_commit_id="06e95b1e9bcd43c4574840f8174ba4b2c5d281bd",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_expression_diff"),
        ],
        api=Black20API(),
        unittests=Black20UnittestGenerator(),
        systemtests=Black20SystemtestGenerator(),
        grammar=grammar_black_diff,
        loc=3556,
    )
    Black(
        bug_id=21,
        buggy_commit_id="c071af761e1550c6e4ebab8e5af747d2d8fdd48e",
        fixed_commit_id="8e7848c63efe36f09e4651bece8c0efc34a1c3e1",
        test_files=[Path("tests", "test_black.py")],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_expression_ff"),
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=3514,
    )
    Black(
        bug_id=22,
        buggy_commit_id="728c56c986bc5aea4d9897d3fce3159f89991b8e",
        fixed_commit_id="c55d08d0b96c8de8bd867ca315e380d9e9d2d7ec",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "comments3.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_comments3"),
        ],
        api=Black22API(),
        unittests=Black22UnittestGenerator(),
        systemtests=Black22SystemtestGenerator(),
        grammar=grammar_black,
        loc=3438,
    )
    Black(
        bug_id=23,
        buggy_commit_id="8de552eb4f0fbf1ad84812cde71489cc00d3ed1f",
        fixed_commit_id="6316e293ac30a2837ec20eba289fd28a2a18cf89",
        test_files=[
            Path("tests", "test_black.py"),
            Path("tests", "python2.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_black.py::BlackTestCase::test_python2"),
        ],
        api=Black23API(),
        unittests=Black23UnittestGenerator(),
        systemtests=Black23SystemtestGenerator(),
        grammar=grammar_black,
        loc=3325,
    )


class BlackAPI(API, abc.ABC):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# Shared infrastructure
# ----------------------------------------------------------------------
# black is a pure code formatter.  The shared project-level harness
# (``resources/black/harness.py``) decodes a urlsafe-base64 source string
# from ``argv[1]``, runs ``black.format_str`` on it and prints
# ``OK:<base64-of-output>`` (or ``ERR:<exception>``).  A system test is a
# single base64 token; the per-bug oracle recomputes the CORRECT (fixed)
# output and compares.
#
# Most of these bugs make black *reformat* input that is already in its
# canonical (fixed-black) shape.  For those we use the "stability" oracle:
# the input is a canonical snippet, fixed black leaves it unchanged
# (``format_str(src) == src``) and buggy black reformats it.  This
# distinguishes buggy from fixed by construction: a failing test PASSES on
# the fixed build (stable) and FAILS on the buggy build (reformatted).
# ======================================================================


def _b64(s: str) -> str:
    return base64.urlsafe_b64encode(s.encode("utf-8")).decode("ascii")


def _b64d(s: str) -> str:
    return base64.urlsafe_b64decode(s.encode("ascii")).decode("utf-8")


# Grammar for a urlsafe-base64 payload (the encoded source string).
grammar_black: Grammar = clean_up(
    dict(
        {
            "<start>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_letters + string.digits + "-_="),
        }
    )
)

assert is_valid_grammar(grammar_black)


# ``run_black`` helper injected into unit tests (as ``get_utils``).  Mirrors
# the harness: robust to the ``line_length`` vs ``mode=`` signature change.
_RUN_BLACK_SRC = '''
@staticmethod
def run_black(src):
    import black

    try:
        return black.format_str(src, line_length=88)
    except TypeError:
        pass
    mode = None
    for attr in ("Mode", "FileMode"):
        if hasattr(black, attr):
            try:
                mode = getattr(black, attr)()
            except Exception:
                mode = None
            break
    if mode is None:
        return black.format_str(src)
    return black.format_str(src, mode=mode)
'''


class BlackStabilityAPI(BlackAPI):
    """Oracle for idempotency/stability bugs.

    The system-test input is a canonical (already fixed-black-formatted)
    snippet.  Correct black leaves it unchanged; buggy black reformats it.
    PASSING iff ``format_str(src) == src``.
    """

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            src = _b64d(process.args[2])
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if not out.startswith("OK:"):
            return TestResult.FAILING, f"black failed: {out!r}"
        try:
            formatted = _b64d(out[3:])
        except Exception:
            return TestResult.FAILING, f"Malformed output: {out!r}"
        if formatted == src:
            return TestResult.PASSING, "black output is stable"
        return TestResult.FAILING, "black reformatted a canonical input"


class BlackStabilityUnittestGenerator(python.PythonGenerator, UnittestGenerator):
    """Base unit generator for stability bugs.

    A failing test asserts that black leaves a canonical snippet unchanged
    (fails on buggy, passes on fixed).  A passing test asserts the same for a
    snippet that is canonical on both builds.
    """

    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_BLACK_SRC).body

    @staticmethod
    def _assert_stable(src: str) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=src),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="self"), attr="run_black"
                            ),
                            args=[ast.Constant(value=src)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    # subclasses (mixins) provide failing_source() / passing_source()

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert_stable(self.failing_source())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert_stable(self.passing_source())
        return test, TestResult.PASSING


class BlackStabilitySystemtestGenerator(SystemtestGenerator):
    """Base system generator for stability bugs.

    Mixins provide ``failing_source()`` / ``passing_source()``.
    """

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.failing_source()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.passing_source()), TestResult.PASSING


import keyword as _keyword


def _word(a: int = 3, b: int = 8) -> str:
    while True:
        w = "".join(random.choices(string.ascii_lowercase, k=random.randint(a, b)))
        if not _keyword.iskeyword(w) and not _keyword.issoftkeyword(w):
            return w


# ----------------------------------------------------------------------
# "known expected output" infrastructure for bugs where black changes an
# input in a way that fixed-output stability cannot distinguish (buggy black
# leaves the canonical output unchanged too).  A system test is
# ``<b64(source)> <b64(expected)>``; the oracle checks ``format_str(source)
# == expected``.  ``expected`` is fixed black's canonical output.  A failing
# case uses a ``source`` that buggy black formats differently from
# ``expected`` (fault triggered); a passing case uses ``source == expected``
# (canonical on both builds).
# ----------------------------------------------------------------------


# Grammar for a ``<b64> <b64>`` pair.
grammar_black_pair: Grammar = clean_up(
    dict(
        {
            "<start>": ["<token> <token>"],
            "<token>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_letters + string.digits + "-_="),
        }
    )
)

assert is_valid_grammar(grammar_black_pair)


class BlackExpectedAPI(BlackAPI):
    """Oracle comparing black's output against a known expected output."""

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            expected = _b64d(process.args[3])
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if not out.startswith("OK:"):
            return TestResult.FAILING, f"black failed: {out!r}"
        try:
            formatted = _b64d(out[3:])
        except Exception:
            return TestResult.FAILING, f"Malformed output: {out!r}"
        if formatted == expected:
            return TestResult.PASSING, "black output matches expected"
        return TestResult.FAILING, "black output differs from expected"


class BlackExpectedSystemtestGenerator(SystemtestGenerator):
    """Base system generator for known-expected-output bugs.

    Mixins provide ``failing_case()`` / ``passing_case()`` returning a
    ``(source, expected)`` tuple.
    """

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        source, expected = self.failing_case()
        return f"{_b64(source)} {_b64(expected)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        source, expected = self.passing_case()
        return f"{_b64(source)} {_b64(expected)}", TestResult.PASSING


class BlackExpectedUnittestGenerator(python.PythonGenerator, UnittestGenerator):
    """Base unit generator for known-expected-output bugs."""

    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_BLACK_SRC).body

    @staticmethod
    def _assert_expected(source: str, expected: str) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="self"), attr="run_black"
                            ),
                            args=[ast.Constant(value=source)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        source, expected = self.failing_case()
        test = self.get_empty_test()
        test.body = self._assert_expected(source, expected)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        source, expected = self.passing_case()
        test = self.get_empty_test()
        test.body = self._assert_expected(source, expected)
        return test, TestResult.PASSING


# ======================================================================
# bug_19: ``EmptyLineTracker`` inserted blank lines before a decorator when
# the preceding line was a comment, so a decorator preceded by a comment
# (e.g. ``@property`` / ``# TODO`` / ``@property``) got spurious blank
# lines.  The fix returns ``0, 0`` for a decorator following a comment.
#
# Stability bug: a canonical decorator-comment-decorator snippet is a fixed
# point of fixed black; buggy black inserts blank lines.
# ======================================================================


class Black19API(BlackStabilityAPI):
    pass


class Black19TestGenerator:
    _DECORATORS = [
        "property",
        "staticmethod",
        "classmethod",
        "abstractmethod",
        "wraps",
        "cached",
        "login_required",
        "app.route",
        "pytest.fixture",
        "functools.lru_cache",
    ]

    def _decorator(self) -> str:
        if random.random() < 0.4:
            return "@" + random.choice(self._DECORATORS)
        return "@" + _word()

    def _comment(self) -> str:
        prefix = random.choice(("# TODO: ", "# NOTE ", "# ", "# FIXME ", "# handles "))
        return prefix + _word()

    def failing_source(self) -> str:
        # a decorator immediately followed by a comment then another
        # decorator triggers the fault
        func = _word()
        n_comments = random.randint(1, 3)
        comments = "\n".join(self._comment() for _ in range(n_comments))
        return (
            f"{self._decorator()}\n"
            f"{comments}\n"
            f"{self._decorator()}\n"
            f"def {func}():\n"
            f"    pass\n"
        )

    def passing_source(self) -> str:
        # canonical code without a comment directly preceding a decorator
        func = _word()
        kind = random.randint(0, 2)
        if kind == 0:
            return (
                f"{self._decorator()}\n"
                f"{self._decorator()}\n"
                f"def {func}():\n"
                f"    pass\n"
            )
        if kind == 1:
            return (
                f"{self._decorator()}\n"
                f"def {func}():\n"
                f"    # {_word()}\n"
                f"    return {random.randint(1, 99)}\n"
            )
        return f"def {func}({_word()}, {_word()}):\n    return {random.randint(1, 99)}\n"


class Black19SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black19TestGenerator
):
    pass


class Black19UnittestGenerator(BlackStabilityUnittestGenerator, Black19TestGenerator):
    pass


# ======================================================================
# bug_11: ``split_line`` short-circuited (``yield line; return``) whenever a
# line was short enough, even when it carried per-element ``# type:``
# comments after commas.  That collapsed an exploded collection onto one
# line and mangled the type comments.  The fix keeps such lines exploded by
# adding a ``has_special_comment`` guard.
#
# Stability bug: a canonical exploded collection with per-comma ``# type:``
# comments is a fixed point of fixed black; buggy black collapses it.
# ======================================================================


class Black11API(BlackStabilityAPI):
    pass


class Black11TestGenerator:
    _TYPES = ["int", "float", "bool", "str", "bytes"]

    @staticmethod
    def _name() -> str:
        return _word(2, 5)

    def failing_source(self) -> str:
        # The fault only triggers when the COLLAPSED one-line form (which
        # buggy black wrongly produces, appending every ``# type:`` comment)
        # is short enough (<= 88).  Build the exploded snippet and only keep
        # it when its collapsed form stays within the line length so the
        # fault is guaranteed.
        while True:
            var = self._name()
            n = random.randint(2, 3)
            names = [self._name() for _ in range(n)]
            elem_types = [random.choice(self._TYPES) for _ in range(n)]
            kind = random.randint(0, 2)
            if kind == 0:  # tuple assignment
                opening, closing = "(", ")"
                prefix = f"{var} = "
                close_type = "Tuple[" + ", ".join(elem_types) + "]"
            elif kind == 1:  # list assignment
                opening, closing = "[", "]"
                prefix = f"{var} = "
                close_type = "List[" + random.choice(self._TYPES) + "]"
            else:  # call assignment
                opening, closing = "(", ")"
                prefix = f"{var} = {self._name()}"
                close_type = random.choice(self._TYPES)
            collapsed = (
                prefix
                + opening
                + ", ".join(names)
                + closing
                + "".join(f"  # type: {t}" for t in elem_types + [close_type])
            )
            if len(collapsed) > 84:
                continue
            body = "\n".join(
                f"    {names[i]},  # type: {elem_types[i]}" for i in range(n)
            )
            return f"{prefix}{opening}\n{body}\n{closing}  # type: {close_type}\n"

    def passing_source(self) -> str:
        var = self._name()
        kind = random.randint(0, 2)
        if kind == 0:  # single-statement type comment (fits, unaffected)
            return f"{var} = []  # type: List[{random.choice(self._TYPES)}]\n"
        if kind == 1:
            return (
                f"def {self._name()}({self._name()}):\n"
                f"    {var} = compute()  # type: {random.choice(self._TYPES)}\n"
                f"    return {var}\n"
            )
        return f"{var} = {random.randint(1, 99)}\n"


class Black11SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black11TestGenerator
):
    pass


class Black11UnittestGenerator(BlackStabilityUnittestGenerator, Black11TestGenerator):
    pass


# ======================================================================
# bug_2: ``generate_ignored_nodes`` did not recognise a ``# fmt: on`` comment
# that appeared on a child node (e.g. after a ``# fmt: off`` block wrapping a
# decorator), so black kept treating the rest of the block as unformatted
# and left code after ``# fmt: on`` untouched.  The fix adds
# ``contains_fmt_on_at_column``.
#
# Known-expected bug: a ``# fmt: off`` block followed by ``# fmt: on`` and a
# collapsed ``def f(): pass``.  Fixed black re-formats the def (expected);
# buggy black leaves it collapsed (fault).
# ======================================================================


class Black2API(BlackExpectedAPI):
    pass


class Black2TestGenerator:
    _DECOS = ["test", "register", "cache", "route", "check", "wrap", "given"]

    def _fmt_off_block(self) -> str:
        deco = random.choice(self._DECOS)
        nums = [random.randint(0, 9) for _ in range(4)]
        return (
            "# fmt: off\n"
            f"@{deco}([\n"
            f"    {nums[0]}, {nums[1]},\n"
            f"    {nums[2]}, {nums[3]},\n"
            "])\n"
            "# fmt: on\n"
        )

    def failing_case(self) -> Tuple[str, str]:
        name = _word()
        block = self._fmt_off_block()
        source = block + f"def {name}(): pass\n"
        expected = block + f"def {name}():\n    pass\n"
        return source, expected

    def passing_case(self) -> Tuple[str, str]:
        name = _word()
        block = self._fmt_off_block()
        # canonical on both builds: the def is already expanded
        text = block + f"def {name}():\n    pass\n"
        return text, text


class Black2SystemtestGenerator(BlackExpectedSystemtestGenerator, Black2TestGenerator):
    pass


class Black2UnittestGenerator(BlackExpectedUnittestGenerator, Black2TestGenerator):
    pass


# ======================================================================
# bug_4: ``EmptyLineTracker._maybe_empty_lines`` subtracted
# ``self.previous_after`` unconditionally, so a file beginning with a
# backslash line-continuation followed by blank lines got spurious empty
# lines inserted at the top.  The fix returns ``0`` empty lines when there is
# no previous line.
#
# Known-expected bug: a leading ``\`` continuation + blank lines before code.
# Fixed black strips them (expected == the canonical code); buggy black
# inserts leading blank lines (fault).
# ======================================================================


class Black4API(BlackExpectedAPI):
    pass


class _BlackSnippetMixin:
    """Random already-canonical top-level snippets shared by several bugs."""

    @staticmethod
    def canonical_stmt() -> str:
        """A canonical simple (non-def) statement."""
        kind = random.randint(0, 3)
        var = _word()
        if kind == 0:
            return f"{var} = {random.randint(0, 999)}\n"
        if kind == 1:
            ints = ", ".join(str(random.randint(0, 99)) for _ in range(random.randint(2, 4)))
            return f"{var} = [{ints}]\n"
        if kind == 2:
            return f'print("{_word()}")\n'
        return f'{var} = {{"{_word()}": {random.randint(0, 99)}}}\n'

    def canonical_snippet(self) -> str:
        if random.random() < 0.3:
            var = _word()
            return f"def {var}():\n    return {random.randint(0, 999)}\n"
        return self.canonical_stmt()


class Black4TestGenerator(_BlackSnippetMixin):
    def failing_case(self) -> Tuple[str, str]:
        # only simple statements trigger the spurious-leading-blank fault
        snippet = self.canonical_stmt()
        k = random.randint(2, 6)
        source = "\\\n" + "\n" * k + snippet
        return source, snippet

    def passing_case(self) -> Tuple[str, str]:
        snippet = self.canonical_snippet()
        if random.random() < 0.5:
            # plain leading blank lines (no backslash) are correctly stripped
            # by both builds
            source = "\n" * random.randint(1, 4) + snippet
        else:
            source = snippet
        return source, snippet


class Black4SystemtestGenerator(BlackExpectedSystemtestGenerator, Black4TestGenerator):
    pass


class Black4UnittestGenerator(BlackExpectedUnittestGenerator, Black4TestGenerator):
    pass


# ======================================================================
# bug_15: the ``# fmt: off`` / ``# fmt: on`` handling (built on FormatOn /
# FormatOff exceptions) mishandled a decorated ``def`` inside an off region,
# inserting spurious blank lines before ``# fmt: on`` instead of preserving
# the region verbatim.  The fix rewrote fmt on/off handling.
#
# Stability bug: a canonical ``# fmt: off`` block wrapping a decorated def is
# a fixed point of fixed black; buggy black reformats it.
# ======================================================================


class Black15API(BlackStabilityAPI):
    pass


class Black15TestGenerator(_BlackSnippetMixin):
    _DECOS = ["deco", "mark", "register", "parametrize", "route", "given"]

    def failing_source(self) -> str:
        deco = random.choice(self._DECOS)
        name = _word()
        arg = _word()
        nums = ", ".join(str(random.randint(0, 9)) for _ in range(random.randint(2, 4)))
        return (
            "# fmt: off\n"
            f"@{deco}([\n"
            f"    ({nums})\n"
            "])\n"
            f"def {name}({arg}):\n"
            "    pass\n"
            "# fmt: on\n"
        )

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        if kind == 0:
            # a fmt:off block WITHOUT a decorated def stays verbatim on both
            var = _word()
            a, b = random.randint(0, 9), random.randint(0, 9)
            return f"# fmt: off\n{var} = [{a},   {b}]\n# fmt: on\n"
        if kind == 1:
            return self.canonical_snippet()
        return f"import {_word()}\n\n\ndef {_word()}({_word()}):\n    pass\n"


class Black15SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black15TestGenerator
):
    pass


class Black15UnittestGenerator(BlackStabilityUnittestGenerator, Black15TestGenerator):
    pass


# ======================================================================
# bug_22: ``Line.comments`` was a ``Dict[LeafID, Leaf]`` holding a single
# comment per leaf, so a leaf carrying several comments lost all but one.
# That mis-formatted an exploded call wrapped by standalone comments (the
# internal comment was dropped and the call collapsed).  The fix stores
# comments as a ``List[Tuple[Index, Leaf]]``.
#
# Stability bug: a canonical outer-call wrapping an inner call that has an
# internal standalone comment is a fixed point of fixed black; buggy black
# collapses the inner call and relocates the comment.
# ======================================================================


class Black22API(BlackStabilityAPI):
    pass


class Black22TestGenerator(_BlackSnippetMixin):
    def failing_source(self) -> str:
        ov = _word()
        ofunc = _word()
        ifunc = f"{_word()}.{_word()}"
        args = [(_word(), random.randint(0, 99)) for _ in range(3)]
        lines = [f"        {k}={v}," for k, v in args]
        lines.insert(2, "        # keep this internal comment intact")
        body = "\n".join(lines)
        return (
            f"{ov} = {ofunc}(\n"
            "    # before comment here\n"
            f"    {ifunc}(\n"
            f"{body}\n"
            "    )\n"
            "    # after comment here\n"
            ")\n"
        )

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        if kind == 0:
            # a simple exploded call with one internal comment (unaffected)
            fn = _word()
            a, b = _word(), _word()
            return (
                f"{_word()} = {fn}(\n"
                f"    {a},\n"
                "    # inner comment\n"
                f"    {b},\n"
                ")\n"
            )
        if kind == 1:
            return self.canonical_snippet()
        return f"{_word()} = {_word()}({_word()}, {_word()})  # trailing comment\n"


class Black22SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black22TestGenerator
):
    pass


class Black22UnittestGenerator(BlackStabilityUnittestGenerator, Black22TestGenerator):
    pass


# ======================================================================
# bug_10: the lib2to3 driver counted a tab as 4 columns
# (``current_column += 4``) while indentation was normalised to spaces, so a
# comment indented with fewer tabs than the surrounding code was placed at
# the wrong indentation level.  The fix counts a tab as one column.
#
# Known-expected bug: tab-indented code with a comment one level out.  Fixed
# black places the comment at the outer level (expected); buggy black indents
# it too deeply (fault).
# ======================================================================


class Black10API(BlackExpectedAPI):
    pass


class Black10TestGenerator:
    @staticmethod
    def _stmt() -> str:
        if random.random() < 0.5:
            return "pass"
        return f"{_word()} = {random.randint(0, 9)}"

    def failing_case(self) -> Tuple[str, str]:
        c1 = random.randint(1, 5)
        c2 = random.randint(1, 5)
        inner = self._stmt()
        after = self._stmt()
        cmt = _word()
        source = f"if {c1}:\n\tif {c2}:\n\t\t{inner}\n\t# {cmt}\n\t{after}\n"
        expected = (
            f"if {c1}:\n    if {c2}:\n        {inner}\n    # {cmt}\n    {after}\n"
        )
        return source, expected

    def passing_case(self) -> Tuple[str, str]:
        c1 = random.randint(1, 5)
        c2 = random.randint(1, 5)
        inner = self._stmt()
        after = self._stmt()
        cmt = _word()
        expected = (
            f"if {c1}:\n    if {c2}:\n        {inner}\n        # {cmt}\n    {after}\n"
        )
        if random.random() < 0.5:
            # tab-indented but the comment sits at the same (inner) level, so
            # both builds convert it the same way
            source = f"if {c1}:\n\tif {c2}:\n\t\t{inner}\n\t\t# {cmt}\n\t{after}\n"
        else:
            # already canonical spaces
            source = expected
        return source, expected


class Black10SystemtestGenerator(BlackExpectedSystemtestGenerator, Black10TestGenerator):
    pass


class Black10UnittestGenerator(BlackExpectedUnittestGenerator, Black10TestGenerator):
    pass


# ======================================================================
# bug_12: ``BracketTracker`` tracked for-loop / lambda argument regions with
# plain counters instead of depth stacks, so a ``for`` target containing
# nested brackets (e.g. ``for ((x in {}) or {})["a"] in x:``) mis-decremented
# the depth and popped a non-existent bracket, raising ``KeyError``.  The fix
# uses depth stacks.
#
# Stability bug (crash): a canonical construct with a bracketed for-target is
# a fixed point of fixed black; buggy black raises ``KeyError`` (the harness
# reports the failure, so the oracle marks it FAILING).
# ======================================================================


class Black12API(BlackStabilityAPI):
    pass


class Black12TestGenerator(_BlackSnippetMixin):
    def failing_source(self) -> str:
        var = _word()
        it = _word()
        key = random.choice([f'"{_word()}"', str(random.randint(0, 9))])
        body = random.choice(["pass", f"{_word()} = {random.randint(0, 9)}"])
        return f"for (({var} in {{}}) or {{}})[{key}] in {it}:\n    {body}\n"

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        if kind == 0:
            return f"for {_word()} in {_word()}:\n    pass\n"
        if kind == 1:
            return f"{_word()} = lambda {_word()}: {random.randint(0, 9)}\n"
        return self.canonical_snippet()


class Black12SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black12TestGenerator
):
    pass


class Black12UnittestGenerator(BlackStabilityUnittestGenerator, Black12TestGenerator):
    pass


# ======================================================================
# bug_8: ``bracket_split_build_line`` appended the import trailing comma at
# the very end of the leaves, i.e. after trailing standalone comments, so an
# exploded import whose last name was followed by comment lines got a comma
# on its own line after the comments.  The fix inserts the comma right after
# the last real leaf.
#
# Stability bug: a canonical exploded import (last name has a trailing comma,
# then comment lines) is a fixed point of fixed black; buggy black appends a
# spurious extra comma after the comments.
# ======================================================================


class Black8API(BlackStabilityAPI):
    pass


class Black8TestGenerator(_BlackSnippetMixin):
    def failing_source(self) -> str:
        mod = _word()
        names = [_word() for _ in range(random.randint(2, 4))]
        cmts = [_word() for _ in range(random.randint(1, 3))]
        body = "".join(f"    {n},\n" for n in names)
        cm = "".join(f"    #  {c}\n" for c in cmts)
        return f"from {mod} import (\n{body}{cm})\n"

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        if kind == 0:
            return f"from {_word()} import {_word()}, {_word()}\n"
        if kind == 1:
            return f"import {_word()}\n"
        return self.canonical_snippet()


class Black8SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black8TestGenerator
):
    pass


class Black8UnittestGenerator(BlackStabilityUnittestGenerator, Black8TestGenerator):
    pass


# ======================================================================
# bug_5: ``bracket_split_build_line`` only added a trailing comma for
# imports, so a ``def`` with a single argument long enough to be exploded got
# no trailing comma.  The fix also adds a comma for standalone function
# arguments (``no_commas = original.is_def and not any comma``).
#
# Known-expected bug: a long single-argument ``def`` on one line.  Fixed
# black explodes it WITH a trailing comma (expected); buggy black explodes it
# WITHOUT the comma (fault).
# ======================================================================


class Black5API(BlackExpectedAPI):
    pass


class Black5TestGenerator(_BlackSnippetMixin):
    @staticmethod
    def _body() -> str:
        return random.choice(["pass", "...", f"return {random.randint(0, 9)}"])

    def failing_case(self) -> Tuple[str, str]:
        name = _word(3, 7)
        # long enough that "def name(arg):" exceeds 88 columns and must explode
        arg = _word(80, 95)
        body = self._body()
        source = f"def {name}({arg}):\n    {body}\n"
        expected = f"def {name}(\n    {arg},\n):\n    {body}\n"
        return source, expected

    def passing_case(self) -> Tuple[str, str]:
        kind = random.randint(0, 2)
        if kind == 0:
            # short def, fits on one line -> canonical on both builds
            text = f"def {_word()}({_word()}, {_word()}):\n    {self._body()}\n"
        elif kind == 1:
            text = f"def {_word()}({_word()}):\n    {self._body()}\n"
        else:
            text = self.canonical_snippet()
        return text, text


class Black5SystemtestGenerator(BlackExpectedSystemtestGenerator, Black5TestGenerator):
    pass


class Black5UnittestGenerator(BlackExpectedUnittestGenerator, Black5TestGenerator):
    pass


# ======================================================================
# bug_7: ``normalize_invisible_parens`` did not wrap a long left-hand-side
# tuple unpacking (``testlist_star_expr``) in parentheses, so a long
# multi-target assignment could not be split.  The fix adds parentheses
# around the targets.
#
# Known-expected bug: a long ``a, b, c, d = 1, 2, 3`` assignment.  Fixed
# black wraps the targets in parens and explodes them (expected); buggy black
# leaves the assignment on one over-long line (fault).
# ======================================================================


class Black7API(BlackExpectedAPI):
    pass


class Black7TestGenerator(_BlackSnippetMixin):
    def failing_case(self) -> Tuple[str, str]:
        values = ", ".join(str(random.randint(0, 9)) for _ in range(3))
        # the single-line assignment must exceed 88 columns so that (only)
        # fixed black wraps the targets in parentheses
        while True:
            n = random.randint(4, 6)
            targets = [_word(14, 20) for _ in range(n)]
            one_line = ", ".join(targets) + f" = {values}"
            if len(one_line) > 90:
                break
        source = one_line + "\n"
        expected = (
            "(\n"
            + "".join(f"    {t},\n" for t in targets)
            + f") = ({values})\n"
        )
        return source, expected

    def passing_case(self) -> Tuple[str, str]:
        kind = random.randint(0, 2)
        if kind == 0:
            # short tuple unpacking that fits -> canonical on both builds
            a, b = _word(), _word()
            text = f"{a}, {b} = {random.randint(0, 9)}, {random.randint(0, 9)}\n"
        elif kind == 1:
            text = f"{_word()} = {random.randint(0, 999)}\n"
        else:
            text = self.canonical_snippet()
        return text, text


class Black7SystemtestGenerator(BlackExpectedSystemtestGenerator, Black7TestGenerator):
    pass


class Black7UnittestGenerator(BlackExpectedUnittestGenerator, Black7TestGenerator):
    pass


# ======================================================================
# bug_9: ``get_grammars`` returned only the print-statement grammar
# (``[pygram.python_grammar]``) when a Python-2 target was requested, so a
# ``print(...)`` call using keyword arguments (only valid as a function) did
# not parse.  The fix also tries the no-print-statement grammar.
#
# Stability bug (crash) with a PY27 harness: a canonical Python file using
# ``print(...kwargs)`` is a fixed point of fixed black; buggy black raises
# ``InvalidInput``.  ``run_black`` in the unit test mirrors the harness by
# forcing ``target_versions={PY27}``.
# ======================================================================

# ``run_black`` variant that forces the PY27 target (mirrors bug_9's harness).
_RUN_BLACK_PY27_SRC = '''
@staticmethod
def run_black(src):
    import black

    mode = black.FileMode(target_versions={black.TargetVersion.PY27})
    return black.format_str(src, mode=mode)
'''


class Black9API(BlackStabilityAPI):
    pass


class Black9TestGenerator:
    _KWARGS = ["file=sys.stderr", 'end=""', 'sep=", "', "flush=True"]

    def failing_source(self) -> str:
        n = random.randint(1, 3)
        args = ", ".join(_word() for _ in range(n))
        kw = random.choice(self._KWARGS)
        return f"from __future__ import print_function\n\nprint({args}, {kw})\n"

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        var = _word()
        if kind == 0:
            return f"{var} = {random.randint(0, 9)}\n"
        if kind == 1:
            return f"def {var}({_word()}):\n    return {random.randint(0, 9)}\n"
        return f"{var} = [{random.randint(0, 9)}, {random.randint(0, 9)}]\n"


class Black9SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black9TestGenerator
):
    pass


class Black9UnittestGenerator(BlackStabilityUnittestGenerator, Black9TestGenerator):
    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_BLACK_PY27_SRC).body


# ======================================================================
# bug_23: ``lib2to3_parse`` only tried the ``no_print_statement`` grammar, so
# Python-2 ``print`` statements (``print "x"``, ``print a, b``) failed to
# parse.  The fix tries a list of grammars.
#
# Stability bug: a canonical Python-2 ``print`` statement is a fixed point of
# fixed black; buggy black raises ``ValueError`` (for ``print "x"``) or
# mis-parses ``print >>stream`` as an expression and reformats it.
# ======================================================================


class Black23API(BlackStabilityAPI):
    pass


class Black23TestGenerator:
    def failing_source(self) -> str:
        # Python-2 print statements that the buggy (no_print_statement-only)
        # grammar cannot parse; fixed black parses and leaves them unchanged.
        kind = random.randint(0, 3)
        if kind == 0:
            return f'print "{_word()}"\n'
        if kind == 1:
            return f"print {_word()}, {_word()}\n"
        if kind == 2:
            return f"print {_word()}\n"
        return f'print "{_word()}", {_word()}\n'

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        var = _word()
        if kind == 0:
            return f"{var} = {random.randint(0, 9)}\n"
        if kind == 1:
            return f'print("{_word()}")\n'
        return f"def {var}({_word()}):\n    return {random.randint(0, 9)}\n"


class Black23SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black23TestGenerator
):
    pass


class Black23UnittestGenerator(BlackStabilityUnittestGenerator, Black23TestGenerator):
    pass


# ======================================================================
# bug_14: ``get_future_imports`` asserted every ``from __future__`` child was
# an ``import_as_names`` node, so a single aliased import
# (``from __future__ import x as y``) — parsed as ``import_as_name`` — hit the
# assertion and made formatting raise.  The fix walks the children properly.
#
# Stability bug (crash): a canonical ``from __future__ import x as y`` line is
# a fixed point of fixed black; buggy black raises ``AssertionError``.
# ======================================================================


class Black14API(BlackStabilityAPI):
    pass


class Black14TestGenerator:
    _FEATURES = [
        "unicode_literals",
        "division",
        "print_function",
        "absolute_import",
        "generator_stop",
        "nested_scopes",
        "with_statement",
        "generators",
    ]

    def failing_source(self) -> str:
        feature = random.choice(self._FEATURES)
        alias = "_" + _word()
        return f"from __future__ import {feature} as {alias}\n"

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        if kind == 0:
            return f"from __future__ import {random.choice(self._FEATURES)}\n"
        if kind == 1:
            a, b = random.sample(self._FEATURES, 2)
            return f"from __future__ import {a}, {b}\n"
        return f"{_word()} = {random.randint(0, 9)}\n"


class Black14SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black14TestGenerator
):
    pass


class Black14UnittestGenerator(BlackStabilityUnittestGenerator, Black14TestGenerator):
    pass


# ======================================================================
# bug_6: async/await handling.  Under a Python-3.7 target, ``async`` and
# ``await`` are reserved keywords, so code using them as identifiers
# (``def async(): ...``) must be REJECTED.  The buggy tokenizer accepted such
# code; the fix (feature flags + TokenizerConfig) makes py37 reject it.
#
# Inverted oracle with a PY37 harness: a failing test carries async-identifier
# source and expects black to RAISE (``err``).  Fixed black raises (PASS);
# buggy black formats it anyway (FAIL).  A passing test carries valid py37
# source and expects success (``ok``) on both builds.  System test is
# ``<b64(source)> <expect>``.
# ======================================================================

# ``run_black`` variant forcing the PY37 target (mirrors bug_6's harness).
_RUN_BLACK_PY37_SRC = '''
@staticmethod
def run_black(src):
    import black

    mode = black.FileMode(target_versions={black.TargetVersion.PY37})
    return black.format_str(src, mode=mode)
'''


class Black6API(BlackAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            expect = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        is_ok = out.startswith("OK:")
        if expect == "err":
            # correct behaviour: black rejects async-as-identifier under py37
            if not is_ok:
                return TestResult.PASSING, "black correctly rejected the input"
            return TestResult.FAILING, "black accepted invalid py37 async identifier"
        # expect == "ok": valid py37 code must format
        if is_ok:
            return TestResult.PASSING, "black formatted the input"
        return TestResult.FAILING, f"black failed on valid input: {out!r}"


class Black6TestGenerator:
    def failing_source(self) -> str:
        # every branch embeds a random value so distinct calls stay distinct
        kind = random.randint(0, 3)
        keyword_id = random.choice(("async", "await"))
        var = _word()
        n = random.randint(0, 999)
        if kind == 0:
            # async/await used as a function name
            return f"def {keyword_id}():\n    {var} = {n}\n    return {var}\n"
        if kind == 1:
            # async/await used as an assignment target + call
            return f"{keyword_id} = {n}\n{keyword_id}()\n"
        if kind == 2:
            return f"{keyword_id} = lambda: {n}\n{keyword_id}()\n"
        # async/await used as a local variable
        return f"def {var}():\n    {keyword_id} = {n}\n    return {keyword_id}\n"

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        name = _word()
        if kind == 0:
            return f"{name} = {random.randint(0, 9)}\n"
        if kind == 1:
            return f"async def {name}():\n    await {_word()}()\n"
        return f"def {name}({_word()}):\n    return {random.randint(0, 9)}\n"


class Black6SystemtestGenerator(SystemtestGenerator, Black6TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"{_b64(self.failing_source())} err", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"{_b64(self.passing_source())} ok", TestResult.PASSING


class Black6UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Black6TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_BLACK_PY37_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        src = self.failing_source()
        test = self.get_empty_test()
        # correct behaviour: black raises on async-as-identifier under py37
        test.body = ast.parse(
            f"self.assertRaises(Exception, self.run_black, {src!r})"
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        src = self.passing_source()
        test = self.get_empty_test()
        test.body = ast.parse(
            f"self.assertEqual({src!r}, self.run_black({src!r}))"
        ).body
        return test, TestResult.PASSING


# ======================================================================
# bug_13: the tokenizer only emitted an ``ASYNC`` token for ``async`` before
# ``def``, so an ``async for`` comprehension inside a *non-async* context
# (e.g. an async generator returned from a regular ``def``) failed to
# tokenize and could not be parsed.  The fix also handles ``async`` before
# ``for``.
#
# Stability bug (crash): a canonical async comprehension inside a regular
# ``def`` / at module level is a fixed point of fixed black; buggy black
# raises ``ValueError``.
# ======================================================================


class Black13API(BlackStabilityAPI):
    pass


class Black13TestGenerator:
    def failing_source(self) -> str:
        kind = random.randint(0, 3)
        var = _word()
        it = _word()
        name = _word()
        if kind == 0:
            return f"def {name}():\n    return ({var} async for {var} in {it}())\n"
        if kind == 1:
            return f"def {name}():\n    return [{var} async for {var} in {it}()]\n"
        if kind == 2:
            return f"def {name}():\n    return {{{var} async for {var} in {it}()}}\n"
        return f"{name} = [{var} async for {var} in {it}()]\n"

    def passing_source(self) -> str:
        kind = random.randint(0, 2)
        var = _word()
        it = _word()
        name = _word()
        if kind == 0:
            return f"def {name}():\n    return [{var} for {var} in {it}()]\n"
        if kind == 1:
            return f"async def {name}():\n    return [{var} async for {var} in {it}()]\n"
        return f"{var} = {random.randint(0, 9)}\n"


class Black13SystemtestGenerator(
    BlackStabilitySystemtestGenerator, Black13TestGenerator
):
    pass


class Black13UnittestGenerator(BlackStabilityUnittestGenerator, Black13TestGenerator):
    pass


# ======================================================================
# bug_3: the ``--config`` click option used ``exists=False``, so black
# accepted a nonexistent config path and then failed while trying to read it
# (exit code 1) instead of rejecting the argument up front.  The fix sets
# ``exists=True`` so click validates the path and exits with code 2.
#
# CLI bug: a nonexistent ``--config`` path should make black exit with code 2
# (fixed); buggy black exits with code 1 (config-read error).  The harness
# runs the black CLI and prints ``RC:<returncode>``.  System test is
# ``<kind> <nonce>`` with ``kind`` in {invalid, valid}.
# ======================================================================

# ``run_black_config`` helper injected into unit tests: invokes the black CLI
# via click's CliRunner and returns the exit code.
_RUN_BLACK_CONFIG_SRC = '''
@staticmethod
def run_black_config(kind, nonce=""):
    import os
    import tempfile
    from click.testing import CliRunner
    import black

    d = tempfile.mkdtemp()
    src = os.path.join(d, "s.py")
    with open(src, "w") as f:
        f.write("x = 1\\n")
    if kind == "invalid":
        config = os.path.join(d, "does_not_exist.toml")
    else:
        config = os.path.join(d, "cfg.toml")
        with open(config, "w") as f:
            f.write("")
    result = CliRunner().invoke(black.main, ["--config", config, "--check", src])
    return result.exit_code
'''


grammar_black_config: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <nonce>"],
            "<kind>": ["invalid", "valid"],
            "<nonce>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_black_config)


class Black3API(BlackAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            kind = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if not out.startswith("RC:"):
            return TestResult.UNDEFINED, f"Malformed output: {out!r}"
        try:
            rc = int(out[3:])
        except ValueError:
            return TestResult.UNDEFINED, f"Malformed output: {out!r}"
        if kind == "invalid":
            # correct behaviour: click rejects the nonexistent config (exit 2)
            if rc == 2:
                return TestResult.PASSING, "config path correctly rejected"
            return TestResult.FAILING, f"expected exit 2, got {rc}"
        # valid config: black runs cleanly on already-formatted input (exit 0)
        if rc == 0:
            return TestResult.PASSING, "valid config accepted"
        return TestResult.FAILING, f"expected exit 0, got {rc}"


class Black3TestGenerator:
    @staticmethod
    def _nonce() -> str:
        return _word(6, 10)


class Black3SystemtestGenerator(SystemtestGenerator, Black3TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"invalid {self._nonce()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"valid {self._nonce()}", TestResult.PASSING


class Black3UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Black3TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_BLACK_CONFIG_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        # correct behaviour: nonexistent config -> exit code 2
        test.body = ast.parse(
            f"self.assertEqual(2, self.run_black_config('invalid', {nonce!r}))"
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        test.body = ast.parse(
            f"self.assertEqual(0, self.run_black_config('valid', {nonce!r}))"
        ).body
        return test, TestResult.PASSING


# ======================================================================
# bug_20: ``format_file_in_place`` built the diff header from ``src.name``
# (the basename) instead of ``src`` (the full path), so the unified-diff
# header dropped the directory.  The fix uses the full path.
#
# CLI bug: for a file given by an absolute path the diff header must show the
# full path (fixed); buggy black shows only the basename.  The harness runs
# ``black --diff`` and reports the path in the header.  System test is
# ``<kind> <nonce>`` with ``kind`` in {subdir (failing), relative (passing)}.
# ======================================================================

grammar_black_diff: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <nonce>"],
            "<kind>": ["subdir", "relative"],
            "<nonce>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_black_diff)

_RUN_DIFF_HEADER_SRC = '''
@staticmethod
def run_diff_header(kind, nonce):
    import os
    import sys as _sys
    import tempfile
    from io import StringIO
    from pathlib import Path
    import black

    d = tempfile.mkdtemp()
    name = "f_" + nonce + ".py"
    with open(os.path.join(d, name), "w") as f:
        f.write("x=1\\n")
    cwd = None
    if kind == "subdir":
        src = Path(os.path.join(d, name))
    else:
        cwd = os.getcwd()
        os.chdir(d)
        src = Path(name)
    expected = str(src)
    hold = _sys.stdout
    _sys.stdout = StringIO()
    try:
        black.format_file_in_place(src, 88, False, black.WriteBack.DIFF)
        _sys.stdout.seek(0)
        out = _sys.stdout.read()
    finally:
        _sys.stdout = hold
        if cwd is not None:
            os.chdir(cwd)
    first = out.splitlines()[0] if out else ""
    marker = "  (original)"
    header = first[4 : first.index(marker)] if first.startswith("--- ") and marker in first else ""
    return header, expected
'''


class Black20API(BlackAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        try:
            parts = dict(p.split(":", 1) for p in out.split(" "))
            expected = _b64d(parts["EXP"])
            header = _b64d(parts["HDR"])
        except Exception:
            return TestResult.UNDEFINED, f"Malformed output: {out!r}"
        # correct behaviour: the diff header shows the exact path given to black
        if header == expected:
            return TestResult.PASSING, "diff header shows the full path"
        return TestResult.FAILING, f"diff header {header!r} != path {expected!r}"


class Black20TestGenerator:
    @staticmethod
    def _nonce() -> str:
        return _word(6, 10)


class Black20SystemtestGenerator(SystemtestGenerator, Black20TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"subdir {self._nonce()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"relative {self._nonce()}", TestResult.PASSING


class Black20UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Black20TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_DIFF_HEADER_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        test.body = ast.parse(
            "header, expected = self.run_diff_header('subdir', %r)\n"
            "self.assertEqual(expected, header)" % nonce
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        test.body = ast.parse(
            "header, expected = self.run_diff_header('relative', %r)\n"
            "self.assertEqual(expected, header)" % nonce
        ).body
        return test, TestResult.PASSING


# ======================================================================
# bug_18: ``format_file_in_place`` opened files with ``tokenize.open`` and
# wrote them back without remembering the original newline, so a file using
# ``\r\n`` (CRLF) line endings was rewritten with ``\n`` (LF).  The fix reads
# the raw bytes, detects the newline and preserves it on write.
#
# CLI bug: black must preserve a file's line endings.  A CRLF file must stay
# CRLF (fixed); buggy black converts it to LF.  The harness reformats a file
# in place and reports whether the output still contains CRLF.  System test is
# ``<kind> <nonce>`` with ``kind`` in {crlf (failing), lf (passing)}.
# ======================================================================

grammar_black_newline: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <nonce>"],
            "<kind>": ["crlf", "lf"],
            "<nonce>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_black_newline)

_RUN_NEWLINE_SRC = '''
@staticmethod
def run_newline(kind, nonce):
    import os
    import tempfile
    from pathlib import Path
    import black

    d = tempfile.mkdtemp()
    path = Path(os.path.join(d, "f_" + nonce + ".py"))
    newline = b"\\r\\n" if kind == "crlf" else b"\\n"
    path.write_bytes(newline.join([b"def f(  ):", b"    pass"]))
    black.format_file_in_place(path, 88, False, black.WriteBack.YES)
    return b"\\r\\n" in path.read_bytes()
'''


class Black18API(BlackAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            kind = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if "CRLF:" not in out:
            return TestResult.UNDEFINED, f"Malformed output: {out!r}"
        has_crlf = out.rsplit("CRLF:", 1)[1].strip() == "1"
        # correct behaviour: the output preserves the input's line ending
        if kind == "crlf":
            if has_crlf:
                return TestResult.PASSING, "CRLF preserved"
            return TestResult.FAILING, "CRLF line endings were lost"
        # lf input: output must not contain CRLF
        if not has_crlf:
            return TestResult.PASSING, "LF preserved"
        return TestResult.FAILING, "unexpected CRLF introduced"


class Black18TestGenerator:
    @staticmethod
    def _nonce() -> str:
        return _word(6, 10)


class Black18SystemtestGenerator(SystemtestGenerator, Black18TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"crlf {self._nonce()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"lf {self._nonce()}", TestResult.PASSING


class Black18UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Black18TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_NEWLINE_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        # correct behaviour: a CRLF file stays CRLF
        test.body = ast.parse(
            "self.assertTrue(self.run_newline('crlf', %r))" % nonce
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        test.body = ast.parse(
            "self.assertFalse(self.run_newline('lf', %r))" % nonce
        ).body
        return test, TestResult.PASSING


# ======================================================================
# bug_16: ``gen_python_files_in_dir`` computed ``child.resolve().relative_to
# (root)`` unconditionally, so a symbolic link resolving OUTSIDE the root
# directory raised ``ValueError`` and aborted the whole run.  The fix catches
# the ``ValueError`` and, for a symlink, ignores it (re-raising otherwise).
#
# CLI/API bug: walking a directory that contains a symlink pointing outside
# the root must not raise (fixed); buggy black raises ``ValueError``.  The
# harness builds such a directory and reports OK / ERR.  System test is
# ``<kind> <nonce>`` with ``kind`` in {symlink (failing), normal (passing)}.
# ======================================================================

grammar_black_symlink: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <nonce>"],
            "<kind>": ["symlink", "normal"],
            "<nonce>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_black_symlink)

_RUN_SYMLINK_SRC = '''
@staticmethod
def run_symlink(kind, nonce):
    import os
    import re
    import tempfile
    from pathlib import Path
    import black

    root = Path(tempfile.mkdtemp()).resolve()
    child = root / ("link_" + nonce + ".py")
    if kind == "symlink":
        outside = Path(tempfile.mkdtemp()).resolve() / "target.py"
        outside.write_text("x = 1\\n")
        os.symlink(str(outside), str(child))
    else:
        child.write_text("x = 1\\n")
    include = re.compile(black.DEFAULT_INCLUDES)
    exclude = re.compile(black.DEFAULT_EXCLUDES)
    report = black.Report()
    try:
        list(black.gen_python_files_in_dir(root, root, include, exclude, report))
        return True
    except Exception:
        return False
'''


class Black16API(BlackAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        # correct behaviour: no exception is raised while walking the directory
        if out == "OK":
            return TestResult.PASSING, "directory walked without error"
        return TestResult.FAILING, f"gen_python_files_in_dir failed: {out!r}"


class Black16TestGenerator:
    @staticmethod
    def _nonce() -> str:
        return _word(6, 10)


class Black16SystemtestGenerator(SystemtestGenerator, Black16TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"symlink {self._nonce()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"normal {self._nonce()}", TestResult.PASSING


class Black16UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Black16TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_SYMLINK_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        # correct behaviour: a symlink out of root is ignored, not an error
        test.body = ast.parse(
            "self.assertTrue(self.run_symlink('symlink', %r))" % nonce
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        test.body = ast.parse(
            "self.assertTrue(self.run_symlink('normal', %r))" % nonce
        ).body
        return test, TestResult.PASSING


# ======================================================================
# bug_1: ``reformat_many`` created a ``ProcessPoolExecutor`` unconditionally,
# so on a system without multiprocessing support (e.g. AWS Lambda, where the
# constructor raises ``OSError``) black crashed instead of formatting.  The
# fix catches the ``OSError`` and falls back to the mono-process executor.
#
# CLI bug: when ``ProcessPoolExecutor`` raises ``OSError`` black must still
# format the files (fixed); buggy black crashes and leaves them unformatted.
# The harness patches ``ProcessPoolExecutor`` to raise ``OSError`` and reports
# whether the files were formatted.  System test is ``<kind> <nonce>`` with
# ``kind`` in {patched (failing), normal (passing)}.
# ======================================================================

grammar_black_mono: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <nonce>"],
            "<kind>": ["patched", "normal"],
            "<nonce>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_black_mono)

_RUN_MONO_SRC = '''
@staticmethod
def run_mono(kind, nonce):
    import asyncio
    import os
    import tempfile
    from unittest.mock import patch
    from click.testing import CliRunner
    import black

    asyncio.set_event_loop(asyncio.new_event_loop())
    d = tempfile.mkdtemp()
    files = [os.path.join(d, "f_" + nonce + "_" + str(i) + ".py") for i in range(2)]
    for f in files:
        with open(f, "w") as fh:
            fh.write("print('hello')")
    if kind == "patched":
        with patch("black.ProcessPoolExecutor") as mock_executor:
            mock_executor.side_effect = OSError()
            CliRunner().invoke(black.main, [d])
    else:
        CliRunner().invoke(black.main, [d])
    return all(open(f).read() == 'print("hello")\\n' for f in files)
'''


class Black1API(BlackAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        # correct behaviour: the files are formatted even without multiprocessing
        if out == "OK":
            return TestResult.PASSING, "files formatted (mono-process fallback works)"
        return TestResult.FAILING, f"files were not formatted: {out!r}"


class Black1TestGenerator:
    @staticmethod
    def _nonce() -> str:
        return _word(6, 10)


class Black1SystemtestGenerator(SystemtestGenerator, Black1TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"patched {self._nonce()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"normal {self._nonce()}", TestResult.PASSING


class Black1UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Black1TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_MONO_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        # correct behaviour: files are still formatted when multiprocessing fails
        test.body = ast.parse(
            "self.assertTrue(self.run_mono('patched', %r))" % nonce
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        test.body = ast.parse(
            "self.assertTrue(self.run_mono('normal', %r))" % nonce
        ).body
        return test, TestResult.PASSING


# ======================================================================
# bug_17: ``decode_bytes`` indexed ``lines[0]`` and ``lib2to3_parse`` indexed
# ``src_txt[-1]`` without guarding against empty input, so formatting an
# EMPTY file raised ``IndexError``.  The fix returns early for empty content
# (and uses ``src_txt[-1:]``).
#
# CLI/API bug: formatting an empty file must succeed and leave it empty
# (fixed); buggy black raises ``IndexError``.  The harness formats a file in
# place and reports OK / ERR.  System test is ``<kind> <nonce>`` with ``kind``
# in {empty (failing), nonempty (passing)}.
# ======================================================================

grammar_black_empty: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <nonce>"],
            "<kind>": ["empty", "nonempty"],
            "<nonce>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_black_empty)

_RUN_EMPTY_SRC = '''
@staticmethod
def run_empty(kind, nonce):
    import tempfile
    from pathlib import Path
    import black

    path = Path(tempfile.mkdtemp()) / ("f_" + nonce + ".py")
    if kind == "empty":
        path.write_bytes(b"")
    else:
        path.write_bytes(b"x = 1\\n")
    try:
        black.format_file_in_place(path, 88, False, black.WriteBack.YES)
        return True
    except Exception:
        return False
'''


class Black17API(BlackAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        # correct behaviour: formatting the file does not raise
        if out == "OK":
            return TestResult.PASSING, "file formatted without error"
        return TestResult.FAILING, f"formatting raised: {out!r}"


class Black17TestGenerator:
    @staticmethod
    def _nonce() -> str:
        return _word(6, 10)


class Black17SystemtestGenerator(SystemtestGenerator, Black17TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"empty {self._nonce()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"nonempty {self._nonce()}", TestResult.PASSING


class Black17UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Black17TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="black")])]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_RUN_EMPTY_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        # correct behaviour: an empty file is formatted without error
        test.body = ast.parse(
            "self.assertTrue(self.run_empty('empty', %r))" % nonce
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nonce = self._nonce()
        test = self.get_empty_test()
        test.body = ast.parse(
            "self.assertTrue(self.run_empty('nonempty', %r))" % nonce
        ).body
        return test, TestResult.PASSING
