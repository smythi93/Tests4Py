import ast
import os
import random
import re
import string
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple, Any

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up, INTEGER, FLOAT, NUMBER
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "tqdm"


class TQDM(Project):
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
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/tqdm/tqdm",
            status=Status.OK,
            python_version="3.6.15",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version="3.6.15",
            python_fallback_version="3.6.15",
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
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
            ],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )


def register():
    TQDM(
        bug_id=1,
        buggy_commit_id="8cc777fe8401a05d07f2c97e65d15e4460feab88",
        fixed_commit_id="c0dcf39b046d1b4ff6de14ac99ad9a1b10487512",
        test_files=[Path("tqdm", "tests", "tests_contrib.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_contrib.py::test_enumerate")],
        unittests=TQDM1UnittestGenerator(),
        systemtests=TQDM1SystemtestGenerator(),
        api=TQDM1API(),
        grammar=grammar_1,
        loc=1910,
    )
    TQDM(
        bug_id=2,
        buggy_commit_id="bef86db56654d271838b145ad77f7040a73a7b4d",
        fixed_commit_id="127af5caf19e7d29c346f5ca8a9c7ef3004b664b",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_format_meter"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_si_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_all_defaults"),
            os.path.join(
                "tqdm", "tests", "tests_tqdm.py::test_native_string_io_for_default_file"
            ),
            os.path.join(
                "tqdm",
                "tests",
                "tests_tqdm.py::test_unicode_string_io_for_specified_file",
            ),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_write_bytes"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_file_output"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_leave_option"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_trange"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_min_interval"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_max_interval"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_min_iters"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_dynamic_min_iters"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_big_min_interval"),
            os.path.join(
                "tqdm", "tests", "tests_tqdm.py::test_smoothed_dynamic_min_iters"
            ),
            os.path.join(
                "tqdm",
                "tests",
                "tests_tqdm.py::test_smoothed_dynamic_min_iters_with_min_interval",
            ),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_nototal"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_unit"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_ascii"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_update"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_close"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_smoothing"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_bar_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_custom_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_unpause"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_reset"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_position"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_set_description"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_deprecated_gui"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_cmp"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_repr"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_autodisable_enable"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_file_redirection"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_external_write"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_unit_scale"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_bool"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_auto"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_float_progress"),
        ],
        skip_tests=["test_ansi_escape_codes"],
        unittests=TQDM2UnittestGenerator(),
        systemtests=TQDM2SystemtestGenerator(),
        api=TQDM2API(),
        grammar=grammar_2,
        loc=1759,
    )
    TQDM(
        bug_id=3,
        buggy_commit_id="c2599e3cd6087429f48bae34347ec5d2473c8392",
        fixed_commit_id="73962a47026dd980ac0758820efc9c41cbf938e0",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_bool")],
        unittests=TQDM3UnittestGenerator(),
        systemtests=TQDM3SystemtestGenerator(),
        api=TQDM3API(),
        grammar=grammar_3,
        loc=1567,
    )
    TQDM(
        bug_id=4,
        buggy_commit_id="03b347646492131d889871939b40457d29147216",
        fixed_commit_id="964dee631d0ed30e2f799b42fc58ba5e73795a08",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_nototal")],
        unittests=TQDM4UnittestGenerator(),
        systemtests=TQDM4SystemtestGenerator(),
        api=TQDM4API(),
        grammar=grammar_4,
        loc=1534,
    )
    TQDM(
        bug_id=5,
        buggy_commit_id="19b08ab34fdbfa0275bc5cb2430436c724c7e759",
        fixed_commit_id="4f340697af69b71850aad496387c9c5aa1904136",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_bool")],
        unittests=TQDM5UnittestGenerator(),
        systemtests=TQDM5SystemtestGenerator(),
        api=TQDM5API(),
        grammar=grammar_5,
        loc=1485,
    )
    TQDM(
        bug_id=6,
        buggy_commit_id="a4b9c86db548b2d0dbb5af7a6bbdc26ab47e1eec",
        fixed_commit_id="6dad2e89019317e875c46d5a3a82a811ad6de2f9",
        test_files=[Path("tqdm", "tests", "tests_synchronisation.py")],
        test_cases=[
            os.path.join("tqdm", "tests", "tests_synchronisation.py::test_imap")
        ],
        skip_tests=["test_monitoring_multi"],
        unittests=TQDM6UnittestGenerator(),
        systemtests=TQDM6SystemtestGenerator(),
        api=TQDM6API(),
        grammar=grammar_6,
        loc=1438,
    )
    TQDM(
        bug_id=7,
        buggy_commit_id="caefe02fd6f3165e5634460ab20caf4c60400120",
        fixed_commit_id="4efd35246c924236f34d8130b1055a3c3ba78605",
        test_files=[
            Path("tqdm", "tests", "tests_main.py"),
            Path("tqdm", "tests", "tests_tqdm.py"),
        ],
        test_cases=[os.path.join("tqdm", "tests", "tests_main.py::test_main")],
        unittests=TQDM7UnittestGenerator(),
        systemtests=TQDM7SystemtestGenerator(),
        api=TQDM7API(),
        grammar=grammar_7,
        loc=1389,
    )
    TQDM(
        bug_id=8,
        buggy_commit_id="08b8ad1ff3bd003ef8309faaa0cc108ffa40317d",
        fixed_commit_id="cae9d139c6df5614be3bf6e25ccbd600ee3286dc",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_format_meter")],
        unittests=TQDM8UnittestGenerator(),
        systemtests=TQDM8SystemtestGenerator(),
        api=TQDM8API(),
        grammar=grammar_8,
        loc=870,
    )
    TQDM(
        bug_id=9,
        buggy_commit_id="9da1d5d116aec7a23d8f6dc22d5e23ecb1c40a7c",
        fixed_commit_id="d877c1dfb4739852105f7b967a8fceb869ac5042",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_si_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_update"),
        ],
        unittests=TQDM9UnittestGenerator(),
        systemtests=TQDM9SystemtestGenerator(),
        api=TQDM9API(),
        grammar=grammar_9,
        loc=385,
    )


class TQDMAPI(API):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# bug_1: tqdm.contrib.tenumerate lost the ``start`` offset
# (buggy passed ``start`` as the tqdm ``desc`` positional and enumerated
#  from 0; the fix enumerates from ``start``).
#
# System-test format:  ``<start> <item> <item> ...``
#   the harness prints ``[i for i, _ in tenumerate(items, start=start)]``
#   the oracle compares against ``list(range(start, start + len(items)))``.
# ======================================================================


class TQDM1API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            start = int(process.args[2])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        n = len(process.args[3:])
        expected = list(range(start, start + n))
        result = process.stdout.decode("utf8").strip()
        if result == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class TQDM1TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_letters, k=random.randint(1, 8)))

    def generate_items(self) -> List[str]:
        return [self.generate_word() for _ in range(random.randint(2, 6))]

    @staticmethod
    def generate_nonzero_start() -> int:
        start = random.randint(1, 500)
        return start * random.choice((1, -1))


class TQDM1SystemtestGenerator(SystemtestGenerator, TQDM1TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        start = self.generate_nonzero_start()
        items = self.generate_items()
        return f"{start} " + " ".join(items), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        items = self.generate_items()
        return "0 " + " ".join(items), TestResult.PASSING


class TQDM1UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM1TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm.contrib",
                names=[ast.alias(name="tenumerate")],
                level=0,
            )
        ]

    @staticmethod
    def _get_assert(expected: List[int], items: List[str], start: int) -> List[ast.stmt]:
        comprehension = ast.ListComp(
            elt=ast.Name(id="i"),
            generators=[
                ast.comprehension(
                    target=ast.Tuple(elts=[ast.Name(id="i"), ast.Name(id="_")]),
                    iter=ast.Call(
                        func=ast.Name(id="tenumerate"),
                        args=[ast.List(elts=[ast.Constant(value=w) for w in items])],
                        keywords=[
                            ast.keyword(arg="start", value=ast.Constant(value=start)),
                            ast.keyword(
                                arg="disable", value=ast.Constant(value=True)
                            ),
                        ],
                    ),
                    ifs=[],
                    is_async=0,
                )
            ],
        )
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.List(elts=[ast.Constant(value=v) for v in expected]),
                        comprehension,
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        start = self.generate_nonzero_start()
        items = self.generate_items()
        expected = list(range(start, start + len(items)))
        test = self.get_empty_test()
        test.body = self._get_assert(expected, items, start)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        items = self.generate_items()
        expected = list(range(len(items)))
        test = self.get_empty_test()
        test.body = self._get_assert(expected, items, 0)
        return test, TestResult.PASSING


grammar_1: Grammar = clean_up(
    dict(
        {
            "<start>": ["<integer> <words>"],
            "<words>": ["<word>", "<word> <words>"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_letters),
        },
        **INTEGER,
    )
)

assert is_valid_grammar(grammar_1)


# ======================================================================
# bug_9: tqdm.format_sizeof used integer decade thresholds (10/100/1000)
# so values that round up at a lower precision (e.g. 9.999 -> "10.00")
# were formatted with the wrong precision / missing SI-prefix.  The fix
# lowered the thresholds to 9.995/99.95/999.95.
#
# System-test format:  a single number, e.g. ``999.99``.
#   the harness prints ``format_sizeof(num)``; the oracle compares to the
#   correct (fixed) SI formatting computed independently.
# ======================================================================


def _correct_format_sizeof(num: float, suffix: str = "") -> str:
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 999.95:
            if abs(num) < 99.95:
                if abs(num) < 9.995:
                    return "{0:1.2f}".format(num) + unit + suffix
                return "{0:2.1f}".format(num) + unit + suffix
            return "{0:3.0f}".format(num) + unit + suffix
        num /= 1000.0
    return "{0:3.1f}Y".format(num) + suffix


def _buggy_format_sizeof(num: float, suffix: str = "") -> str:
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1000.0:
            if abs(num) < 100.0:
                if abs(num) < 10.0:
                    return "{0:1.2f}".format(num) + unit + suffix
                return "{0:2.1f}".format(num) + unit + suffix
            return "{0:3.0f}".format(num) + unit + suffix
        num /= 1000.0
    return "{0:3.1f}Y".format(num) + suffix


class TQDM9API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            num = float(process.args[2])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _correct_format_sizeof(num)
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {result!r}"


class TQDM9TestGenerator:
    # boundaries where the buggy and fixed thresholds diverge
    _BOUNDARIES = (10.0, 100.0, 1000.0)
    _SCALES = (1.0, 1e3, 1e6, 1e9)

    def generate_failing_number(self) -> str:
        while True:
            boundary = random.choice(self._BOUNDARIES)
            scale = random.choice(self._SCALES)
            # a value just below the decade boundary that rounds up
            delta = random.choice((0.04, 0.03, 0.02, 0.01))
            num = (boundary - delta) * scale
            text = repr(round(num, 6))
            if _buggy_format_sizeof(float(text)) != _correct_format_sizeof(
                float(text)
            ):
                return text

    def generate_passing_number(self) -> str:
        while True:
            magnitude = random.choice((1.0, 1e3, 1e6, 1e9))
            base = round(random.uniform(1.1, 8.9), random.choice((1, 2)))
            num = base * magnitude
            text = repr(round(num, 6))
            if _buggy_format_sizeof(float(text)) == _correct_format_sizeof(
                float(text)
            ):
                return text


class TQDM9SystemtestGenerator(SystemtestGenerator, TQDM9TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.generate_failing_number(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.generate_passing_number(), TestResult.PASSING


class TQDM9UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM9TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm._tqdm",
                names=[ast.alias(name="format_sizeof")],
                level=0,
            )
        ]

    @staticmethod
    def _get_assert(expected: str, num: float) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="format_sizeof"),
                            args=[ast.Constant(value=num)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        text = self.generate_failing_number()
        num = float(text)
        test = self.get_empty_test()
        test.body = self._get_assert(_correct_format_sizeof(num), num)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        text = self.generate_passing_number()
        num = float(text)
        test = self.get_empty_test()
        test.body = self._get_assert(_correct_format_sizeof(num), num)
        return test, TestResult.PASSING


grammar_9: Grammar = clean_up(dict({"<start>": ["<float>"]}, **FLOAT))

assert is_valid_grammar(grammar_9)


# ======================================================================
# bug_4: format_meter applied ``total *= unit_scale`` unconditionally, so
# a call with ``total=None`` and a numeric ``unit_scale`` raised a
# TypeError.  The fix guards the multiplication with ``if total:``.
#
# System-test format:  ``<n> <total> <elapsed> <unit_scale>`` where
#   ``<total>`` is either ``None`` or an integer.  The harness calls
#   format_meter and prints the result, or a sentinel on exception; the
#   oracle treats "did not raise" as PASSING.
# ======================================================================


class TQDM4API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        err = process.stderr.decode("utf8").strip()
        if process.returncode == 0 and not out.startswith("TQDM_ERROR"):
            return TestResult.PASSING, out
        return TestResult.FAILING, out or err


class TQDM4TestGenerator:
    @staticmethod
    def generate_unit_scale() -> str:
        return repr(round(random.uniform(2.0, 1000.0), random.choice((0, 1, 2))))

    @staticmethod
    def generate_n() -> str:
        return str(random.randint(1, 5000))

    @staticmethod
    def generate_elapsed() -> str:
        return repr(round(random.uniform(0.1, 100.0), 2))

    def make_failing(self) -> str:
        # total=None with a numeric unit_scale triggers the fault
        return f"{self.generate_n()} None {self.generate_elapsed()} {self.generate_unit_scale()}"

    def make_passing(self) -> str:
        # a concrete total >= n never triggers the fault (format_meter only
        # resets total to None when n > total)
        n = random.randint(1, 5000)
        total = random.randint(n, n + 5000)
        return f"{n} {total} {self.generate_elapsed()} {self.generate_unit_scale()}"


class TQDM4SystemtestGenerator(SystemtestGenerator, TQDM4TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class TQDM4UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM4TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm",
                names=[ast.alias(name="tqdm")],
                level=0,
            )
        ]

    @staticmethod
    def _get_assert(n: int, total, elapsed: float, unit_scale: float) -> List[ast.stmt]:
        call = ast.Call(
            func=ast.Attribute(value=ast.Name(id="tqdm"), attr="format_meter"),
            args=[
                ast.Constant(value=n),
                ast.Constant(value=total),
                ast.Constant(value=elapsed),
            ],
            keywords=[
                ast.keyword(arg="unit_scale", value=ast.Constant(value=unit_scale))
            ],
        )
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertIsInstance"
                    ),
                    args=[call, ast.Name(id="str")],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = int(self.generate_n())
        elapsed = float(self.generate_elapsed())
        unit_scale = float(self.generate_unit_scale())
        test = self.get_empty_test()
        test.body = self._get_assert(n, None, elapsed, unit_scale)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = random.randint(1, 5000)
        total = random.randint(n, n + 5000)
        elapsed = float(self.generate_elapsed())
        unit_scale = float(self.generate_unit_scale())
        test = self.get_empty_test()
        test.body = self._get_assert(n, total, elapsed, unit_scale)
        return test, TestResult.PASSING


grammar_4: Grammar = clean_up(
    dict(
        {
            "<start>": ["<integer> <total> <float> <float>"],
            "<total>": ["None", "<integer>"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_4)


# ======================================================================
# bug_8: when a custom ``bar_format`` contains ``{bar}``, format_meter
# split it into ``l_bar_user``/``r_bar_user`` but then formatted the
# DEFAULT ``l_bar``/``r_bar`` instead, dropping the user's surrounding
# text.  The fix formats ``l_bar_user``/``r_bar_user``.
#
# System-test format:  ``<n> <total> <elapsed> <left> <mode> <right>``
#   where ``<mode>`` is ``bar`` (bar_format = left+"{bar}"+right, the
#   trigger) or ``nobar`` (left+"{n_fmt}"+right, unaffected).  The oracle
#   requires the output to start with ``left`` and end with ``right``.
# ======================================================================


class TQDM8API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            left = process.args[5]
            right = process.args[7]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out.startswith(left) and out.endswith(right):
            return TestResult.PASSING, out
        return TestResult.FAILING, f"Expected {left!r}...{right!r}, but was {out!r}"


class TQDM8TestGenerator:
    @staticmethod
    def generate_marker() -> str:
        return "".join(random.choices(string.ascii_letters, k=random.randint(3, 8)))

    def generate_case(self, mode: str) -> str:
        total = random.randint(1, 5000)
        n = random.randint(0, total)
        elapsed = round(random.uniform(0.1, 200.0), 2)
        left = self.generate_marker()
        right = self.generate_marker()
        return f"{n} {total} {elapsed!r} {left} {mode} {right}"


class TQDM8SystemtestGenerator(SystemtestGenerator, TQDM8TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.generate_case("bar"), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.generate_case("nobar"), TestResult.PASSING


class TQDM8UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM8TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm", names=[ast.alias(name="tqdm")], level=0
            )
        ]

    @staticmethod
    def _get_body(
        n: int, total: int, elapsed: float, left: str, field: str, right: str
    ) -> List[ast.stmt]:
        bar_format = left + field + right
        call = ast.Call(
            func=ast.Attribute(value=ast.Name(id="tqdm"), attr="format_meter"),
            args=[
                ast.Constant(value=n),
                ast.Constant(value=total),
                ast.Constant(value=elapsed),
            ],
            keywords=[
                ast.keyword(
                    arg="bar_format", value=ast.Constant(value=bar_format)
                )
            ],
        )
        return [
            ast.Assign(
                targets=[ast.Name(id="res")], value=call, lineno=0
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertTrue"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="res"), attr="startswith"
                            ),
                            args=[ast.Constant(value=left)],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertTrue"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="res"), attr="endswith"
                            ),
                            args=[ast.Constant(value=right)],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        total = random.randint(1, 5000)
        n = random.randint(0, total)
        elapsed = round(random.uniform(0.1, 200.0), 2)
        test = self.get_empty_test()
        test.body = self._get_body(
            n, total, elapsed, self.generate_marker(), "{bar}", self.generate_marker()
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        total = random.randint(1, 5000)
        n = random.randint(0, total)
        elapsed = round(random.uniform(0.1, 200.0), 2)
        test = self.get_empty_test()
        test.body = self._get_body(
            n, total, elapsed, self.generate_marker(), "{n_fmt}", self.generate_marker()
        )
        return test, TestResult.PASSING


grammar_8: Grammar = clean_up(
    dict(
        {
            "<start>": ["<integer> <integer> <float> <word> <mode> <word>"],
            "<mode>": ["bar", "nobar"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_letters),
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_8)


# ======================================================================
# bug_3: the tqdm class had no ``__bool__``, so ``bool(t)`` fell back to
# ``__len__`` which returned ``self.total`` (None for an iterable without
# ``__len__``, e.g. a generator) and raised ``TypeError``.  The fix adds
# ``__bool__`` returning ``total > 0`` / ``bool(iterable)``.
#
# System-test format:  ``<mode> <n>`` where ``<mode>`` is ``gen`` (the
#   trigger: a generator with no length), ``list`` or ``total``.  The
#   oracle expects ``bool`` to be True for a generator and ``n > 0`` for
#   the sized cases.
# ======================================================================


class TQDM3API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            n = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = True if mode == "gen" else (n > 0)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class TQDM3TestGenerator:
    @staticmethod
    def generate_n() -> int:
        return random.randint(0, 1000)


class TQDM3SystemtestGenerator(SystemtestGenerator, TQDM3TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"gen {self.generate_n()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(("list", "total"))
        return f"{mode} {self.generate_n()}", TestResult.PASSING


class TQDM3UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM3TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm", names=[ast.alias(name="tqdm")], level=0
            )
        ]

    @staticmethod
    def _tqdm_bool(iterable: Optional[ast.expr], total: Optional[int]) -> ast.Call:
        keywords = [ast.keyword(arg="disable", value=ast.Constant(value=True))]
        args = []
        if iterable is not None:
            args.append(iterable)
        if total is not None:
            keywords.insert(
                0, ast.keyword(arg="total", value=ast.Constant(value=total))
            )
        return ast.Call(
            func=ast.Name(id="bool"),
            args=[
                ast.Call(func=ast.Name(id="tqdm"), args=args, keywords=keywords)
            ],
            keywords=[],
        )

    @staticmethod
    def _range_call(n: int) -> ast.Call:
        return ast.Call(func=ast.Name(id="range"), args=[ast.Constant(value=n)], keywords=[])

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self.generate_n()
        gen = ast.GeneratorExp(
            elt=ast.Name(id="x"),
            generators=[
                ast.comprehension(
                    target=ast.Name(id="x"),
                    iter=self._range_call(n),
                    ifs=[],
                    is_async=0,
                )
            ],
        )
        bool_call = self._tqdm_bool(gen, None)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[bool_call],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self.generate_n()
        if random.random() < 0.5:
            iterable = ast.Call(
                func=ast.Name(id="list"), args=[self._range_call(n)], keywords=[]
            )
            bool_call = self._tqdm_bool(iterable, None)
        else:
            bool_call = self._tqdm_bool(None, n)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[ast.Constant(value=n > 0), bool_call],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.PASSING


grammar_3: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number>"],
            "<mode>": ["gen", "list", "total"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_3)


# ======================================================================
# bug_5: the disabled ``__init__`` fast-path never set ``self.total``, so
# a disabled tqdm created with only ``total=`` (no iterable) raised
# ``AttributeError`` when its length / truth value was queried.  The fix
# sets ``self.total = total`` in the disable branch.
#
# System-test format:  ``<mode> <n>`` where ``<mode>`` is ``total_dis``
#   (the trigger: total-only + disabled), ``list_dis`` or ``range_dis``.
#   The oracle expects the truth value to equal ``n > 0``.
# ======================================================================


class TQDM5API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            n = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = n > 0
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class TQDM5TestGenerator:
    @staticmethod
    def generate_n() -> int:
        return random.randint(0, 1000)


class TQDM5SystemtestGenerator(SystemtestGenerator, TQDM5TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"total_dis {self.generate_n()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(("list_dis", "range_dis"))
        return f"{mode} {self.generate_n()}", TestResult.PASSING


class TQDM5UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM5TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm", names=[ast.alias(name="tqdm")], level=0
            )
        ]

    @staticmethod
    def _range_list(n: int) -> ast.Call:
        return ast.Call(
            func=ast.Name(id="list"),
            args=[
                ast.Call(
                    func=ast.Name(id="range"),
                    args=[ast.Constant(value=n)],
                    keywords=[],
                )
            ],
            keywords=[],
        )

    def _bool_of(self, mode: str, n: int) -> ast.Call:
        if mode == "list_dis":
            args = [self._range_list(n)]
            keywords = [ast.keyword(arg="disable", value=ast.Constant(value=True))]
        elif mode == "range_dis":
            args = [
                ast.Call(
                    func=ast.Name(id="range"),
                    args=[ast.Constant(value=n)],
                    keywords=[],
                )
            ]
            keywords = [ast.keyword(arg="disable", value=ast.Constant(value=True))]
        else:  # total_dis
            args = []
            keywords = [
                ast.keyword(arg="total", value=ast.Constant(value=n)),
                ast.keyword(arg="disable", value=ast.Constant(value=True)),
            ]
        return ast.Call(
            func=ast.Name(id="bool"),
            args=[ast.Call(func=ast.Name(id="tqdm"), args=args, keywords=keywords)],
            keywords=[],
        )

    def _assert_eq(self, mode: str, n: int) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[ast.Constant(value=n > 0), self._bool_of(mode, n)],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self.generate_n()
        test = self.get_empty_test()
        test.body = self._assert_eq("total_dis", n)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self.generate_n()
        mode = random.choice(("list_dis", "range_dis"))
        test = self.get_empty_test()
        test.body = self._assert_eq(mode, n)
        return test, TestResult.PASSING


grammar_5: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number>"],
            "<mode>": ["total_dis", "list_dis", "range_dis"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_5)


# ======================================================================
# bug_7: the CLI option-splitting regex ``RE_SHLEX`` matched ``--?``
# anywhere, so a hyphen inside an option VALUE (e.g. ``--desc Foo-Bar``)
# was mistaken for a new option, raising ``TqdmKeyError``.  The fix adds a
# ``(?<!\S)`` lookbehind so only hyphens at a word boundary start options.
#
# System-test format:  ``<desc> <data>`` (two words).  The harness runs
#   the tqdm CLI (``main``) with ``--desc <desc>`` piping ``<data>`` and
#   prints ``OUT:<data>`` on success; the oracle expects the passthrough.
#   A ``<desc>`` with an internal hyphen triggers the fault.
# ======================================================================


class TQDM7API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            data = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OUT:" + data
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class TQDM7TestGenerator:
    _OPTIONS = {
        "desc", "total", "leave", "ncols", "ascii", "unit", "disable", "delim",
        "bytes", "smoothing", "initial", "position", "postfix", "help", "version",
    }

    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))

    def generate_plain(self) -> str:
        while True:
            w = self.generate_word()
            if w not in self._OPTIONS:
                return w

    def generate_hyphenated(self) -> str:
        return f"{self.generate_plain()}-{self.generate_plain()}"


class TQDM7SystemtestGenerator(SystemtestGenerator, TQDM7TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"{self.generate_hyphenated()} {self.generate_plain()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"{self.generate_plain()} {self.generate_plain()}", TestResult.PASSING


class TQDM7UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM7TestGenerator
):
    @staticmethod
    def _body(desc: str, data: str) -> List[ast.stmt]:
        src = (
            "import io, sys\n"
            "from tqdm import main\n"
            f"sys.argv = ['', '--desc', {desc!r}]\n"
            f"sys.stdin = io.StringIO({data!r} + '\\n')\n"
            "cap = io.StringIO()\n"
            "real = sys.stdout\n"
            "sys.stdout = cap\n"
            "try:\n"
            "    main(fp=io.StringIO())\n"
            "finally:\n"
            "    sys.stdout = real\n"
            f"self.assertEqual({data!r}, cap.getvalue().rstrip('\\n'))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_hyphenated(), self.generate_plain())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_plain(), self.generate_plain())
        return test, TestResult.PASSING


grammar_7: Grammar = clean_up(
    dict(
        {
            "<start>": ["<token> <token>"],
            "<token>": ["<letter><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase) + ["-"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_7)


# ======================================================================
# bug_2: ``disp_trim`` appended an ANSI reset (``\x1b[0m``) whenever ANSI
# codes were present, even if the string already ended with a reset,
# producing a doubled reset.  The fix only appends when not already
# ending with a reset.
#
# System-test format:  ``<length> <mode> <color> <word>`` where
#   ``<mode>`` is ``ansi`` (data = ``\x1b[<color>m<word>\x1b[0m`` — the
#   trigger, since it already ends with a reset) or ``plain`` (data =
#   ``<word>``).  ``<length>`` is large so no trimming happens.  The
#   oracle compares against the correct (non-doubled) result.
# ======================================================================

_RESET = "\x1b[0m"
_RE_ANSI = re.compile("\x1b\\[[0-9;]*m")


def _build_disp_data(mode: str, color: str, word: str) -> str:
    if mode == "ansi":
        return "\x1b[" + color + "m" + word + _RESET
    return word


def _correct_disp_trim(data: str, length: int) -> str:
    # valid only when ``length`` >= the display length of ``data`` (no trim)
    if not _RE_ANSI.search(data):
        return data[:length]
    return data if data.endswith(_RESET) else data + _RESET


class TQDM2API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            length = int(process.args[2])
            mode = process.args[3]
            color = process.args[4]
            word = process.args[5]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        data = _build_disp_data(mode, color, word)
        expected = repr(_correct_disp_trim(data, length))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class TQDM2TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_uppercase, k=random.randint(3, 10)))

    @staticmethod
    def generate_length() -> int:
        return random.randint(200, 999)

    @staticmethod
    def generate_color() -> str:
        return str(random.choice([0, 1, 4] + list(range(30, 38)) + list(range(90, 98))))


class TQDM2SystemtestGenerator(SystemtestGenerator, TQDM2TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{self.generate_length()} ansi {self.generate_color()} {self.generate_word()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{self.generate_length()} plain {self.generate_color()} {self.generate_word()}",
            TestResult.PASSING,
        )


class TQDM2UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM2TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm.utils",
                names=[ast.alias(name="disp_trim")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(data: str, length: int) -> List[ast.stmt]:
        expected = _correct_disp_trim(data, length)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="disp_trim"),
                            args=[
                                ast.Constant(value=data),
                                ast.Constant(value=length),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        length = self.generate_length()
        data = _build_disp_data("ansi", self.generate_color(), self.generate_word())
        test = self.get_empty_test()
        test.body = self._assert(data, length)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        length = self.generate_length()
        data = _build_disp_data("plain", self.generate_color(), self.generate_word())
        test = self.get_empty_test()
        test.body = self._assert(data, length)
        return test, TestResult.PASSING


grammar_2: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <mode> <number> <word>"],
            "<mode>": ["ansi", "plain"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_letters),
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_2)


# ======================================================================
# bug_6: ``__len__`` returned the bare ``self.total`` for an iterable
# without ``__len__`` (e.g. a generator / map / imap), raising
# ``AttributeError`` when ``self.total`` was never set (disabled tqdm).
# The fix uses ``getattr(self, "total", None)``.
#
# System-test format:  ``<mode> <n>`` where ``<mode>`` is ``gen`` (the
#   trigger: an iterable without ``__len__``), ``list`` or ``range``.
#   The harness prints ``repr(t.__len__())``; the oracle expects ``None``
#   for a generator and ``n`` for the sized cases.
# ======================================================================


class TQDM6API(TQDMAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            n = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "None" if mode == "gen" else str(n)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class TQDM6TestGenerator:
    @staticmethod
    def generate_n() -> int:
        return random.randint(0, 1000)


class TQDM6SystemtestGenerator(SystemtestGenerator, TQDM6TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"gen {self.generate_n()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(("list", "range"))
        return f"{mode} {self.generate_n()}", TestResult.PASSING


class TQDM6UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, TQDM6TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="tqdm", names=[ast.alias(name="tqdm")], level=0
            )
        ]

    @staticmethod
    def _range_call(n: int) -> ast.Call:
        return ast.Call(
            func=ast.Name(id="range"), args=[ast.Constant(value=n)], keywords=[]
        )

    def _len_call(self, mode: str, n: int) -> ast.Call:
        if mode == "gen":
            iterable = ast.GeneratorExp(
                elt=ast.Name(id="x"),
                generators=[
                    ast.comprehension(
                        target=ast.Name(id="x"),
                        iter=self._range_call(n),
                        ifs=[],
                        is_async=0,
                    )
                ],
            )
        elif mode == "list":
            iterable = ast.Call(
                func=ast.Name(id="list"), args=[self._range_call(n)], keywords=[]
            )
        else:  # range
            iterable = self._range_call(n)
        tqdm_call = ast.Call(
            func=ast.Name(id="tqdm"),
            args=[iterable],
            keywords=[ast.keyword(arg="disable", value=ast.Constant(value=True))],
        )
        return ast.Call(
            func=ast.Attribute(value=tqdm_call, attr="__len__"), args=[], keywords=[]
        )

    def _assert(self, mode: str, n: int, expected) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[ast.Constant(value=expected), self._len_call(mode, n)],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self.generate_n()
        test = self.get_empty_test()
        test.body = self._assert("gen", n, None)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self.generate_n()
        mode = random.choice(("list", "range"))
        test = self.get_empty_test()
        test.body = self._assert(mode, n, n)
        return test, TestResult.PASSING


grammar_6: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number>"],
            "<mode>": ["gen", "list", "range"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_6)
