import ast
import os.path
import random
import string
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple, Any

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "spacy"


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
        grammar: Optional[Grammar] = None,
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
        skip_tests: Optional[List[str]] = None,
    ):
        setup = [[PYTHON, "setup.py", "build_ext", "--inplace"]]
        if bug_id == 6:
            # This commit reads factory entry points via
            # ``importlib_metadata.entry_points().get(...)``.  The build env
            # otherwise pulls importlib-metadata>=5 (via pytest), whose
            # ``entry_points()`` returns a group object without ``.get``, so
            # even ``Language()`` fails.  Pin a version that still returns a
            # dict.  ``setup`` runs last, so this sticks.
            setup = [
                [PYTHON, "-m", "pip", "install", "importlib-metadata==4.13.0"]
            ] + setup
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
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
            grammar=grammar,
            loc=loc,
            source_base=Path(PROJECT_NAME),
            test_base=Path(PROJECT_NAME, "tests"),
            included_files=[PROJECT_NAME],
            excluded_files=[os.path.join(PROJECT_NAME, "tests")],
            setup=setup,
            # The pinned CPython 3.7.8 is x86_64 (via Rosetta on Apple
            # Silicon); force the Cython extensions to the same architecture so
            # the compiled .so files are loadable.  Ignored on Linux.
            setup_env={"ARCHFLAGS": "-arch x86_64"}
            if sys.platform == "darwin"
            else None,
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )

    def patch(self, location: Path):
        with open(location / "pyproject.toml", "r") as fp:
            content = fp.read()
        content = content.replace(
            "cython>=0.25",
            "cython==0.29.19",
        )
        with open(location / "pyproject.toml", "w") as fp:
            fp.write(content)
        if self.bug_id in (4, 5, 6, 7, 8, 9):
            with open(location / "setup.cfg", "r") as fp:
                content = fp.read()
            if self.bug_id == 9:
                content = content.replace(
                    "spacy_lookups_data>=0.0.4<0.2.0",
                    "spacy_lookups_data>=0.0.4,<0.2.0",
                )
            else:
                content = content.replace(
                    "spacy_lookups_data>=0.0.5<0.2.0",
                    "spacy_lookups_data>=0.0.5,<0.2.0",
                )
            with open(location / "setup.cfg", "w") as fp:
                fp.write(content)


def register():
    SpaCy(
        bug_id=1,
        buggy_commit_id="9ce059dd067ecc3f097d04023e3cfa0d70d35bb8",
        fixed_commit_id="a987e9e45d4084f30964a4cec9914ae6ed25a73c",
        test_files=[
            Path("spacy", "tests", "test_errors.py"),
            Path("spacy", "tests", "test_architectures.py"),
        ],
        test_cases=[os.path.join("spacy", "tests", "test_errors.py::test_add_codes")],
        api=SpaCyAPI1(),
        unittests=SpaCyUnittestGenerator1(),
        systemtests=SpaCySystemtestGenerator1(),
        grammar=grammar_1,
        loc=80165,
    )
    SpaCy(
        bug_id=2,
        buggy_commit_id="efec28ce70a0ff69471cc379867deebe7eb881e0",
        fixed_commit_id="cfdaf99b8029d6762730c5d5bd2b6f6c173c1241",
        test_files=[
            Path("spacy", "tests", "regression", "test_issue5137.py"),
            Path("spacy", "tests", "pipeline", "test_analysis.py"),
        ],
        test_cases=[
            os.path.join(
                "spacy", "tests", "regression", "test_issue5137.py::test_issue5137"
            )
        ],
        skip_tests=[
            "test_component_decorator_assigns",
            "test_component_factories_from_nlp",
        ],
        api=SpaCyAPI2(),
        unittests=SpaCyUnittestGenerator2(),
        systemtests=SpaCySystemtestGenerator2(),
        grammar=grammar_2,
        loc=80024,
    )
    SpaCy(
        bug_id=3,
        buggy_commit_id="dac70f29eb3b1f21ae9e2c6346666bf6a46307b6",
        fixed_commit_id="663333c3b2bad90915d1a48a626ca1275b7ef077",
        test_files=[Path("spacy", "tests", "regression", "test_issue5314.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "regression",
                "test_issue5314.py::test_issue5314"
                '[<text bytes="11456" xml:space="preserve">[[Fil:Arch\\xe4ologie '
                "schichtengrabung.jpg|thumb|Ark\\xe6ologisk [[udgravning]] med profil."
                "]] '''Ark\\xe6ologi''' er studiet af tidligere tiders "
                "[[menneske]]lige [[aktivitet]], prim\\xe6rt gennem studiet af "
                "menneskets materielle levn.</text>0]",
            ),
            os.path.join(
                "spacy",
                "tests",
                "regression",
                "test_issue5314.py::test_issue5314"
                '[<text bytes="11456" xml:space="preserve">[[Fil:Arch\\xe4ologie schichtengrabung.jpg|thumb|Ark'
                "\\xe6ologisk [[udgravning]] med profil.]] '''Ark\\xe6ologi''' er studiet af tidligere tiders "
                "[[menneske]]lige [[aktivitet]], prim\\xe6rt gennem studiet af menneskets materielle levn.</text>1]",
            ),
        ],
        api=SpaCyAPI3(),
        unittests=SpaCyUnittestGenerator3(),
        systemtests=SpaCySystemtestGenerator3(),
        grammar=grammar_3,
        loc=79665,
    )
    SpaCy(
        bug_id=4,
        buggy_commit_id="abd5c06374eab5db0cf897b73543b1f3eb007e12",
        fixed_commit_id="9fa9d7f2cb52ce6a70c264d4e57c7f190d7686bf",
        test_files=[
            Path("spacy", "tests", "regression", "test_issue4665.py"),
            Path("spacy", "tests", "test_cli.py"),
        ],
        test_cases=[
            os.path.join(
                "spacy", "tests", "regression", "test_issue4665.py::test_issue4665"
            )
        ],
        api=SpaCyAPI4(),
        unittests=SpaCyUnittestGenerator4(),
        systemtests=SpaCySystemtestGenerator4(),
        grammar=grammar_4,
        loc=73718,
    )
    SpaCy(
        bug_id=5,
        buggy_commit_id="bdfb696677a7591ced018e7597c00929e97c6837",
        fixed_commit_id="3bd15055ce74b04dcaf3b9abe2adeb01fb595776",
        test_files=[Path("spacy", "tests", "test_language.py")],
        test_cases=[
            os.path.join("spacy", "tests", "test_language.py::test_evaluate_no_pipe")
        ],
        api=SpaCyAPI5(),
        unittests=SpaCyUnittestGenerator5(),
        systemtests=SpaCySystemtestGenerator5(),
        grammar=grammar_5,
        loc=73083,
    )
    SpaCy(
        bug_id=6,
        buggy_commit_id="6b874ef09611ac32ad038203423d44087cbeb3ae",
        fixed_commit_id="afe4a428f78abe45d6104d74ef42a066570fa43d",
        test_files=[Path("spacy", "tests", "pipeline", "test_analysis.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "pipeline",
                "test_analysis.py::test_analysis_validate_attrs_remove_pipe",
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        api=SpaCyAPI6(),
        unittests=SpaCyUnittestGenerator6(),
        systemtests=SpaCySystemtestGenerator6(),
        grammar=grammar_6,
        loc=72871,
    )
    SpaCy(
        bug_id=7,
        buggy_commit_id="da6e0de34f4947fdebc839df3969c641014cfa97",
        fixed_commit_id="6f54e59fe7ccb3bacce896ed33d36b39f11cbfaf",
        test_files=[Path("spacy", "tests", "doc", "test_span.py")],
        test_cases=[
            os.path.join("spacy", "tests", "doc", "test_span.py::test_filter_spans")
        ],
        api=SpaCyAPI7(),
        unittests=SpaCyUnittestGenerator7(),
        systemtests=SpaCySystemtestGenerator7(),
        grammar=grammar_7,
        loc=72264,
    )
    SpaCy(
        bug_id=8,
        buggy_commit_id="fa95c030a511337935d1a2e930cb954c7a4cd376",
        fixed_commit_id="5efae495f18f37316bd641a05ca26e62cb78e242",
        test_files=[Path("spacy", "tests", "matcher", "test_matcher_logic.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "matcher",
                "test_matcher_logic.py::test_matcher_remove",
            )
        ],
        api=SpaCyAPI8(),
        unittests=SpaCyUnittestGenerator8(),
        systemtests=SpaCySystemtestGenerator8(),
        grammar=grammar_errcode,
        loc=72263,
    )
    SpaCy(
        bug_id=9,
        buggy_commit_id="bc7e7db208d351fae2982afbcdff7633f9636779",
        fixed_commit_id="3297a19545027c8d8550b1ae793ce290567eff32",
        test_files=[
            Path("spacy", "tests", "pipeline", "test_tagger.py"),
            Path("spacy", "tests", "regression", "test_issue2501-3000.py"),
        ],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "pipeline",
                "test_tagger.py::test_tagger_warns_no_lemma_lookups",
            )
        ],
        api=SpaCyAPI9(),
        unittests=SpaCyUnittestGenerator9(),
        systemtests=SpaCySystemtestGenerator9(),
        grammar=grammar_errcode,
        loc=72195,
    )
    SpaCy(
        bug_id=10,
        buggy_commit_id="38de08c7a99d5d8c490223126071afe7dd4f4b67",
        fixed_commit_id="52904b72700a3f301a26563d3f94493bad96a446",
        test_files=[Path("spacy", "tests", "matcher", "test_matcher_api.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "matcher",
                "test_matcher_api.py::test_matcher_valid_callback",
            )
        ],
        api=SpaCyAPI10(),
        unittests=SpaCyUnittestGenerator10(),
        systemtests=SpaCySystemtestGenerator10(),
        grammar=grammar_errcode,
        loc=72240,
    )


class SpaCyAPI(API):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# bug_1: spacy/errors.py ``add_codes`` wrapped *every* attribute access into
# a ``"[code] msg"`` string, including dunder attributes such as
# ``__class__``.  The fix delegates dunder access to
# ``super().__getattribute__``.  So on the buggy build ``wrapped.__class__``
# is a formatted *string*, while on the fixed build it is the genuine class.
#
# System-test format:
#   ``dunder <__attr__>``      -> failing: the genuine (non-str) dunder value.
#   ``code <CODE> <message>``  -> passing: ``getattr`` of a real code works on
#                                 both builds and returns ``"[CODE] message"``.
# ======================================================================


_BUG1_DUNDERS = [
    "__class__",
    "__dict__",
    "__doc__",
    "__init__",
    "__hash__",
    "__repr__",
    "__str__",
    "__sizeof__",
    "__dir__",
    "__format__",
    "__reduce__",
    "__reduce_ex__",
    "__delattr__",
    "__ne__",
    "__eq__",
    "__setattr__",
]


class SpaCyAPI1(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if mode == "dunder":
            expected = "GENUINE"
        else:  # code
            code = process.args[3]
            message = " ".join(process.args[4:])
            expected = f"[{code}] {message}"
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class SpaCy1TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_letters, k=random.randint(3, 8)))

    def generate_message(self) -> str:
        return " ".join(self.generate_word() for _ in range(random.randint(1, 4)))

    @staticmethod
    def generate_code() -> str:
        return random.choice("EWT") + "".join(
            random.choices(string.digits, k=3)
        )

    @staticmethod
    def generate_dunder() -> str:
        return random.choice(_BUG1_DUNDERS)


class SpaCySystemtestGenerator1(SystemtestGenerator, SpaCy1TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"dunder {self.generate_dunder()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"code {self.generate_code()} {self.generate_message()}",
            TestResult.PASSING,
        )


class SpaCyUnittestGenerator1(
    python.PythonGenerator, UnittestGenerator, SpaCy1TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="add_codes")],
                level=0,
            )
        ]

    @staticmethod
    def _failing_body(dunder: str) -> List[ast.stmt]:
        src = (
            "wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))\n"
            f"self.assertNotIsInstance(getattr(wrapped, {dunder!r}), str)\n"
        )
        return ast.parse(src).body

    @staticmethod
    def _passing_body(code: str, message: str) -> List[ast.stmt]:
        src = (
            f"wrapped = add_codes(type('Errors', (object,), {{{code!r}: {message!r}}}))\n"
            f"self.assertEqual({('[' + code + '] ' + message)!r}, getattr(wrapped, {code!r}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._failing_body(self.generate_dunder())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._passing_body(self.generate_code(), self.generate_message())
        return test, TestResult.PASSING


grammar_1: Grammar = {
    "<start>": ["dunder <dunder>", "code <code> <message>"],
    "<dunder>": _BUG1_DUNDERS,
    "<code>": ["<letter><digit><digit><digit>"],
    "<letter>": ["E", "W", "T"],
    "<message>": ["<word>", "<word> <message>"],
    "<word>": ["<char><chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.ascii_letters),
    "<digit>": srange(string.digits),
}
assert is_valid_grammar(grammar_1)


# ======================================================================
# bugs 8, 10 (spacy/errors.py::Errors) and bug 9 (spacy/errors.py::Warnings):
# a new error / warning code was *added* by the fix (E175, E171, W022).  On
# the buggy build the code is missing, so ``getattr(Errors, "E175")`` raises
# ``AttributeError`` (via ``add_codes``); on the fixed build it returns
# ``"[E175] ...message..."``.
#
# System-test format:  ``<cls> <code> <tag>`` where ``<cls>`` is ``Errors`` or
#   ``Warnings`` and ``<tag>`` is an ignored token that keeps inputs distinct.
#   The harness prints the wrapped attribute (or ``ERR`` on failure).  The
#   oracle checks the output starts with ``"[<code>] "`` -- true iff the code
#   exists and is add_codes-wrapped, which is exactly the fault.
# ======================================================================


class _ErrCodeAPI(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            code = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        prefix = f"[{code}] "
        if process.returncode == 0 and out.startswith(prefix) and len(out) > len(prefix):
            return TestResult.PASSING, f"code {code} present"
        return TestResult.FAILING, f"Expected message for {code}, but was {out!r}"


class _ErrCodeTestGenerator:
    # error codes that already exist on every one of these commits -> passing
    EXISTING_ERRORS = [f"E{n:03d}" for n in range(1, 40)]
    EXISTING_WARNINGS = [f"W{n:03d}" for n in range(1, 20)]

    NEW_CODE = "E000"  # overridden per bug
    CLS = "Errors"  # overridden per bug

    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 10)))

    def existing_codes(self) -> List[str]:
        return self.EXISTING_WARNINGS if self.CLS == "Warnings" else self.EXISTING_ERRORS

    def failing_string(self) -> str:
        return f"{self.CLS} {self.NEW_CODE} {self.generate_tag()}"

    def passing_string(self) -> str:
        return f"{self.CLS} {random.choice(self.existing_codes())} {self.generate_tag()}"


class _ErrCodeSystemtestGenerator(SystemtestGenerator, _ErrCodeTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.failing_string(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.passing_string(), TestResult.PASSING


class _ErrCodeUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, _ErrCodeTestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name=self.CLS)],
                level=0,
            )
        ]

    def _body(self, code: str, tag: str) -> List[ast.stmt]:
        # ``tag`` is an inert distinct token so repeated failing tests (which
        # all reference the same new code) have distinct bodies.
        src = (
            f"tag = {tag!r}\n"
            f"value = getattr({self.CLS}, {code!r})\n"
            f"self.assertTrue(value.startswith('[' + {code!r} + '] '))\n"
            f"self.assertGreater(len(value), len({code!r}) + 3)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.NEW_CODE, self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(random.choice(self.existing_codes()), self.generate_tag())
        return test, TestResult.PASSING


class SpaCyAPI8(_ErrCodeAPI):
    pass


class SpaCySystemtestGenerator8(_ErrCodeSystemtestGenerator):
    CLS = "Errors"
    NEW_CODE = "E175"


class SpaCyUnittestGenerator8(_ErrCodeUnittestGenerator):
    CLS = "Errors"
    NEW_CODE = "E175"


class SpaCyAPI9(_ErrCodeAPI):
    pass


class SpaCySystemtestGenerator9(_ErrCodeSystemtestGenerator):
    CLS = "Warnings"
    NEW_CODE = "W022"


class SpaCyUnittestGenerator9(_ErrCodeUnittestGenerator):
    CLS = "Warnings"
    NEW_CODE = "W022"


class SpaCyAPI10(_ErrCodeAPI):
    pass


class SpaCySystemtestGenerator10(_ErrCodeSystemtestGenerator):
    CLS = "Errors"
    NEW_CODE = "E171"


class SpaCyUnittestGenerator10(_ErrCodeUnittestGenerator):
    CLS = "Errors"
    NEW_CODE = "E171"


grammar_errcode: Grammar = {
    "<start>": ["<cls> <code> <tag>"],
    "<cls>": ["Errors", "Warnings"],
    "<code>": ["<letter><digit><digit><digit>"],
    "<letter>": ["E", "W"],
    "<tag>": ["<lower><lowers>"],
    "<lowers>": ["", "<lower><lowers>"],
    "<lower>": srange(string.ascii_lowercase),
    "<digit>": srange(string.digits),
}
assert is_valid_grammar(grammar_errcode)


# ======================================================================
# bug_7: spacy/util.py ``filter_spans`` used ``(len, start)`` as the sort key,
# so for two equal-length overlapping spans the tie-break kept the *later*
# span; the fix uses ``(len, -start)`` (keep the earlier span) and sorts the
# result by start.  ``filter_spans`` is a pure function over ``Span`` objects,
# which we build from a blank ``Doc``/``Vocab`` (no model needed).
#
# System-test format:  ``<n_tokens> <a_start> <a_end> <b_start> <b_end>`` --
#   two spans over a doc of ``n_tokens`` blank words.  The harness prints the
#   ``(start, end)`` pairs that survive ``filter_spans``; the oracle compares
#   against the fixed implementation.  Two equal-length overlapping spans
#   trigger the fault; non-overlapping / different-length spans do not.
# ======================================================================


def _fixed_filter_spans(spans):
    get_sort_key = lambda span: (span[1] - span[0], -span[0])
    sorted_spans = sorted(spans, key=get_sort_key, reverse=True)
    result = []
    seen_tokens = set()
    for span in sorted_spans:
        if span[0] not in seen_tokens and span[1] - 1 not in seen_tokens:
            result.append(span)
        seen_tokens.update(range(span[0], span[1]))
    result = sorted(result, key=lambda span: span[0])
    return result


class SpaCyAPI7(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            spans = [
                (int(process.args[3]), int(process.args[4])),
                (int(process.args[5]), int(process.args[6])),
            ]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(_fixed_filter_spans(spans))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class SpaCy7TestGenerator:
    def failing_case(self) -> Tuple[int, int, int, int, int]:
        # two equal-length overlapping spans: the tie-break (buggy keeps the
        # later span, fixed keeps the earlier one) makes the surviving span
        # differ between the two builds.
        length = random.randint(2, 4)
        k = random.randint(1, length - 1)  # overlap offset, b starts after a
        n = length + k + random.randint(2, 6)
        a_start = random.randint(0, n - (length + k))
        b_start = a_start + k
        return n, a_start, a_start + length, b_start, b_start + length

    def passing_case(self) -> Tuple[int, int, int, int, int]:
        # a longer span with a strictly shorter span nested inside it: only the
        # longer span survives on *both* builds, so the single-element result
        # is identical (no ordering ambiguity).
        outer_len = random.randint(3, 5)
        n = outer_len + random.randint(2, 6)
        a_start = random.randint(0, n - outer_len)
        a_end = a_start + outer_len
        inner_len = random.randint(1, outer_len - 1)
        b_start = a_start + random.randint(0, outer_len - inner_len)
        return n, a_start, a_end, b_start, b_start + inner_len


class SpaCySystemtestGenerator7(SystemtestGenerator, SpaCy7TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        n, a0, a1, b0, b1 = self.failing_case()
        return f"{n} {a0} {a1} {b0} {b1}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        n, a0, a1, b0, b1 = self.passing_case()
        return f"{n} {a0} {a1} {b0} {b1}", TestResult.PASSING


class SpaCyUnittestGenerator7(
    python.PythonGenerator, UnittestGenerator, SpaCy7TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="spacy.util", names=[ast.alias(name="filter_spans")], level=0
            ),
            ast.ImportFrom(
                module="spacy.tokens", names=[ast.alias(name="Doc")], level=0
            ),
            ast.ImportFrom(
                module="spacy.vocab", names=[ast.alias(name="Vocab")], level=0
            ),
        ]

    def _body(self, n: int, a0: int, a1: int, b0: int, b1: int) -> List[ast.stmt]:
        expected = _fixed_filter_spans([(a0, a1), (b0, b1)])
        expected_pairs = [(s[0], s[1]) for s in expected]
        src = (
            f"doc = Doc(Vocab(), words=[str(i) for i in range({n})])\n"
            f"spans = [doc[{a0}:{a1}], doc[{b0}:{b1}]]\n"
            "kept = [(s.start, s.end) for s in filter_spans(spans)]\n"
            f"self.assertEqual({expected_pairs!r}, kept)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(*self.failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(*self.passing_case())
        return test, TestResult.PASSING


grammar_7: Grammar = {
    "<start>": ["<n> <a0> <a1> <b0> <b1>"],
    "<n>": ["<nonzero><digits>", "<nonzero>"],
    "<a0>": ["<number>"],
    "<a1>": ["<number>"],
    "<b0>": ["<number>"],
    "<b1>": ["<number>"],
    "<number>": ["<digit><digits>", "<digit>"],
    "<digits>": ["", "<digit><digits>"],
    "<nonzero>": srange("123456789"),
    "<digit>": srange(string.digits),
}
assert is_valid_grammar(grammar_7)


# ======================================================================
# bug_4: spacy/cli/converters/conllu2json.py ``read_conllx`` computed the
# head as ``(int(head) - 1) if head != "0" else id_``, so a CoNLL-U token
# whose HEAD field is the placeholder ``"_"`` triggered ``int("_")`` and
# raised ``ValueError``.  The fix guards with ``head not in ["0", "_"]``.
#
# System-test format:  a space-separated list of HEAD values (each a number
#   or ``"_"``); the harness builds a one-sentence CoNLL-U document with one
#   token per head and prints ``PARSED_OK`` iff ``read_conllx`` parses it.
#   A list containing ``"_"`` triggers the fault; an all-numeric list does
#   not.  The oracle treats "parsed without error" (fixed behaviour) as
#   PASSING.
# ======================================================================


class SpaCyAPI4(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8")
        if "PARSED_OK" in out:
            return TestResult.PASSING, "read_conllx parsed the document"
        return TestResult.FAILING, f"read_conllx did not parse: {out.strip()!r}"


class SpaCy4TestGenerator:
    @staticmethod
    def _heads(n: int, include_underscore: bool) -> List[str]:
        heads = [str(random.randint(0, n)) for _ in range(n)]
        if include_underscore:
            heads[random.randrange(n)] = "_"
        return heads

    def failing_heads(self) -> List[str]:
        return self._heads(random.randint(2, 6), True)

    def passing_heads(self) -> List[str]:
        return self._heads(random.randint(2, 6), False)


class SpaCySystemtestGenerator4(SystemtestGenerator, SpaCy4TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self.failing_heads()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self.passing_heads()), TestResult.PASSING


class SpaCyUnittestGenerator4(
    python.PythonGenerator, UnittestGenerator, SpaCy4TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="spacy.cli.converters.conllu2json",
                names=[ast.alias(name="read_conllx")],
                level=0,
            )
        ]

    @staticmethod
    def _conllu(heads: List[str]) -> str:
        rows = []
        for i, h in enumerate(heads):
            cols = [str(i + 1), "w%d" % i, "_", "NOUN", "NN", "_", h, "dep", "_", "_"]
            rows.append("\t".join(cols))
        return "\n".join(rows)

    def _body(self, heads: List[str]) -> List[ast.stmt]:
        text = self._conllu(heads)
        src = (
            f"text = {text!r}\n"
            "result = list(read_conllx(text))\n"
            "self.assertEqual(1, len(result))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.failing_heads())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.passing_heads())
        return test, TestResult.PASSING


grammar_4: Grammar = {
    "<start>": ["<heads>"],
    "<heads>": ["<head>", "<head> <heads>"],
    "<head>": ["<number>", "_"],
    "<number>": ["<digit>", "<digit><number>"],
    "<digit>": srange(string.digits),
}
assert is_valid_grammar(grammar_4)


# ======================================================================
# bug_3: bin/wiki_entity_linking/wikipedia_processor.py ``_process_wp_text``
# extracted the article body with ``text_regex`` whose look-behind required
# the literal tag ``<text xml:space="preserve">``.  A ``<text ...>`` tag with
# any additional attribute (e.g. ``bytes="11456"``) did not match, so the
# function returned ``(None, None)`` instead of the text.  The fix first
# strips the tag attributes (``text_tag_regex``) then matches ``<text>``.
#
# System-test format:  ``<mode> <title> <content...>`` where ``<mode>`` is
#   ``extra`` (a ``<text>`` tag with an extra attribute -- the trigger) or
#   ``exact`` (the bare ``xml:space`` tag).  The harness prints
#   ``RESULT:EXTRACTED`` iff the body was extracted; the oracle treats
#   "extracted" (fixed behaviour) as PASSING.
# ======================================================================


class SpaCyAPI3(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if marker == "EXTRACTED":
            return TestResult.PASSING, "article body extracted"
        return TestResult.FAILING, f"expected EXTRACTED, got {marker!r}"


class SpaCy3TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_letters, k=random.randint(3, 8)))

    def _title(self) -> str:
        return self._word()

    def _content(self) -> str:
        return " ".join(self._word() for _ in range(random.randint(2, 6)))


class SpaCySystemtestGenerator3(SystemtestGenerator, SpaCy3TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"extra {self._title()} {self._content()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"exact {self._title()} {self._content()}", TestResult.PASSING


class SpaCyUnittestGenerator3(
    python.PythonGenerator, UnittestGenerator, SpaCy3TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="bin.wiki_entity_linking.wikipedia_processor",
                names=[ast.alias(name="_process_wp_text")],
                level=0,
            )
        ]

    @staticmethod
    def _article(mode: str, content: str) -> str:
        tag = (
            '<text bytes="11456" xml:space="preserve">'
            if mode == "extra"
            else '<text xml:space="preserve">'
        )
        return tag + content + "</text>"

    def _body(self, mode: str, title: str, content: str) -> List[ast.stmt]:
        article_text = self._article(mode, content)
        src = (
            f"clean_text, entities = _process_wp_text({title!r}, {article_text!r}, {{}})\n"
            "self.assertIsNotNone(clean_text)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("extra", self._title(), self._content())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("exact", self._title(), self._content())
        return test, TestResult.PASSING


grammar_3: Grammar = {
    "<start>": ["<mode> <title> <content>"],
    "<mode>": ["exact", "extra"],
    "<title>": ["<word>"],
    "<content>": ["<word>", "<word> <content>"],
    "<word>": ["<char><chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.ascii_letters),
}
assert is_valid_grammar(grammar_3)


# ======================================================================
# bug_5: spacy/language.py ``Language.evaluate`` called
# ``_pipe(pipe, docs, kwargs)`` for a pipeline component that does not expose
# a ``.pipe`` method, but ``_pipe`` is defined as ``_pipe(docs, proc, kwargs)``
# -- the arguments were swapped, so evaluating a pipeline containing a plain
# callable component raised ``TypeError``.  The fix passes ``_pipe(docs, pipe,
# kwargs)``.
#
# System-test format:  ``<mode> <text...>`` where ``<mode>`` is ``nopipe``
#   (add a plain ``def pipe(doc)`` component -- the trigger), ``withpipe``
#   (a component exposing ``.pipe``) or ``empty`` (no component).  The harness
#   builds ``Language(Vocab())`` and prints ``RESULT:OK`` iff ``evaluate``
#   succeeds; the oracle treats success (fixed behaviour) as PASSING.
# ======================================================================


class SpaCyAPI5(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if marker == "OK":
            return TestResult.PASSING, "evaluate succeeded"
        return TestResult.FAILING, f"expected OK, got {marker!r}"


class SpaCy5TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def _text(self) -> str:
        return " ".join(self._word() for _ in range(random.randint(1, 4)))


class SpaCySystemtestGenerator5(SystemtestGenerator, SpaCy5TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"nopipe {self._text()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(('withpipe', 'empty'))} {self._text()}",
            TestResult.PASSING,
        )


_BUG5_ANNOTS = "{'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}"


class SpaCyUnittestGenerator5(
    python.PythonGenerator, UnittestGenerator, SpaCy5TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="spacy.language", names=[ast.alias(name="Language")], level=0
            ),
            ast.ImportFrom(
                module="spacy.vocab", names=[ast.alias(name="Vocab")], level=0
            ),
        ]

    @staticmethod
    def _body(mode: str, text: str) -> List[ast.stmt]:
        setup = "nlp = Language(Vocab())\n"
        if mode == "nopipe":
            setup += (
                "def pipe(doc):\n"
                "    return doc\n"
                "nlp.add_pipe(pipe, name='plain')\n"
            )
        elif mode == "withpipe":
            setup += (
                "class PipeWithPipe(object):\n"
                "    name = 'withpipe'\n"
                "    def __call__(self, doc):\n"
                "        return doc\n"
                "    def pipe(self, docs, **kwargs):\n"
                "        for doc in docs:\n"
                "            yield doc\n"
                "nlp.add_pipe(PipeWithPipe(), name='withpipe')\n"
            )
        src = (
            setup
            + f"nlp.evaluate([({text!r}, {_BUG5_ANNOTS})])\n"
            + "self.assertTrue(True)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("nopipe", self._text())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(random.choice(("withpipe", "empty")), self._text())
        return test, TestResult.PASSING


grammar_5: Grammar = {
    "<start>": ["<mode> <text>"],
    "<mode>": ["nopipe", "withpipe", "empty"],
    "<text>": ["<word>", "<word> <text>"],
    "<word>": ["<char><chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.ascii_lowercase),
}
assert is_valid_grammar(grammar_5)


# ======================================================================
# bug_2: spacy/util.py ``load_model_from_path`` built each pipeline
# component's config from the model meta only, ignoring the ``**overrides``
# passed to ``spacy.load``.  So a keyword override (e.g.
# ``spacy.load(path, categories="x")``) never reached the component.  The fix
# adds ``config.update(overrides)``.
#
# System-test format:  ``<override> <tag>`` where ``<override>`` is the value
#   passed as ``categories=`` to ``spacy.load`` (``all_categories`` -- the
#   component default -- for the passing case, any other word for the failing
#   case) and ``<tag>`` keeps inputs distinct.  The harness saves a blank
#   English pipeline with a custom component and reloads it with the override;
#   the oracle expects the component's ``categories`` to equal ``<override>``
#   (fixed behaviour).
# ======================================================================


class SpaCyAPI2(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            expected = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if marker == expected:
            return TestResult.PASSING, f"categories={marker}"
        return TestResult.FAILING, f"expected {expected!r}, got {marker!r}"


class SpaCy2TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 10)))

    def generate_override(self) -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 10)))


class SpaCySystemtestGenerator2(SystemtestGenerator, SpaCy2TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"{self.generate_override()} {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"all_categories {self.generate_tag()}", TestResult.PASSING


_BUG2_COMPONENT = (
    "class MyComponent(object):\n"
    "    name = 'my_component'\n"
    "    def __init__(self, nlp, **cfg):\n"
    "        self.nlp = nlp\n"
    "        self.categories = cfg.get('categories', 'all_categories')\n"
    "    def __call__(self, doc):\n"
    "        return doc\n"
    "    def to_disk(self, path, **kwargs):\n"
    "        pass\n"
    "    def from_disk(self, path, **cfg):\n"
    "        return self\n"
    "Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)\n"
)


class SpaCyUnittestGenerator2(
    python.PythonGenerator, UnittestGenerator, SpaCy2TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="spacy")]),
            ast.Import(names=[ast.alias(name="tempfile")]),
            ast.ImportFrom(
                module="spacy.language", names=[ast.alias(name="Language")], level=0
            ),
            ast.ImportFrom(
                module="spacy.lang.en", names=[ast.alias(name="English")], level=0
            ),
        ]

    @staticmethod
    def _body(override: str, tag: str) -> List[ast.stmt]:
        src = (
            f"tag = {tag!r}\n"
            + _BUG2_COMPONENT
            + "nlp = English()\n"
            "nlp.add_pipe(nlp.create_pipe('my_component'))\n"
            "tmpdir = tempfile.mkdtemp()\n"
            "nlp.to_disk(tmpdir)\n"
            f"nlp2 = spacy.load(tmpdir, categories={override!r})\n"
            f"self.assertEqual({override!r}, nlp2.get_pipe('my_component').categories)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_override(), self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("all_categories", self.generate_tag())
        return test, TestResult.PASSING


grammar_2: Grammar = {
    "<start>": ["<override> <tag>"],
    "<override>": ["all_categories", "<word>"],
    "<tag>": ["<word>"],
    "<word>": ["<char><chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.ascii_lowercase),
}
assert is_valid_grammar(grammar_2)


# ======================================================================
# bug_6: spacy/language.py ``Language.remove_pipe`` ran
# ``analyze_all_pipes(self.pipeline)`` BEFORE popping the component, so (with
# ENABLE_PIPELINE_ANALYSIS) removing a component whose own requirement was
# unsatisfied re-emitted the requirement warning even though the component
# was on its way out.  The fix pops first, then analyzes the reduced pipeline.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``unsat`` (remove
#   a component that requires an unassigned attribute -- the trigger) or
#   ``sat`` (remove a component whose requirement is satisfied).  ``<tag>``
#   keeps inputs distinct.  The harness records warnings emitted during
#   ``remove_pipe`` and prints ``RESULT:NOWARN``/``RESULT:WARN``; the oracle
#   treats "no warning" (fixed behaviour) as PASSING.
# ======================================================================


class SpaCyAPI6(SpaCyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if marker == "NOWARN":
            return TestResult.PASSING, "no requirement warning on remove"
        return TestResult.FAILING, f"expected NOWARN, got {marker!r}"


class SpaCy6TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 10)))


class SpaCySystemtestGenerator6(SystemtestGenerator, SpaCy6TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"unsat {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"sat {self.generate_tag()}", TestResult.PASSING


class SpaCyUnittestGenerator6(
    python.PythonGenerator, UnittestGenerator, SpaCy6TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="warnings")]),
            ast.Import(names=[ast.alias(name="spacy.language")]),
            ast.ImportFrom(
                module="spacy.language",
                names=[ast.alias(name="Language"), ast.alias(name="component")],
                level=0,
            ),
        ]

    @staticmethod
    def _body(mode: str, tag: str) -> List[ast.stmt]:
        # ``requires`` is unsatisfied (token.pos) for the failing mode and
        # satisfied (token.tag, assigned by c1) for the passing mode.
        req = "token.pos" if mode == "unsat" else "token.tag"
        src = (
            "spacy.language.ENABLE_PIPELINE_ANALYSIS = True\n"
            f"@component('c1_{tag}', assigns=['token.tag'])\n"
            f"def c1_{tag}(doc):\n"
            "    return doc\n"
            f"@component('c2_{tag}', requires=[{req!r}])\n"
            f"def c2_{tag}(doc):\n"
            "    return doc\n"
            "nlp = Language()\n"
            f"nlp.add_pipe(c1_{tag})\n"
            "with warnings.catch_warnings(record=True):\n"
            "    warnings.simplefilter('always')\n"
            f"    nlp.add_pipe(c2_{tag})\n"
            "with warnings.catch_warnings(record=True) as rec:\n"
            "    warnings.simplefilter('always')\n"
            f"    nlp.remove_pipe('c2_{tag}')\n"
            "warned = any('requires' in str(w.message) and 'to be assigned' "
            "in str(w.message) for w in rec)\n"
            "self.assertFalse(warned)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("unsat", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("sat", self.generate_tag())
        return test, TestResult.PASSING


grammar_6: Grammar = {
    "<start>": ["<mode> <tag>"],
    "<mode>": ["unsat", "sat"],
    "<tag>": ["<word>"],
    "<word>": ["<char><chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.ascii_lowercase),
}
assert is_valid_grammar(grammar_6)
