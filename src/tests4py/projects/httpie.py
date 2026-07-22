import abc
import ast
import os
import random
import re
import string
from pathlib import Path
from typing import Any, List, Optional, Tuple

from tests4py.constants import PYTHON
from tests4py.grammars.fuzzer import Grammar, srange, is_valid_grammar
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "httpie"


class Httpie(Project):
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
        test_base: Optional[os.PathLike] = None,
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
        skip_tests: Optional[List[str]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/jakubroztocil/httpie/",
            status=Status.OK,
            python_version="3.7.8",
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
            api=api or HttpieAPI(),
            grammar=grammar_request,
            source_base=Path(PROJECT_NAME),
            test_base=test_base or Path("tests"),
            loc=loc,
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
                # The framework runs unit tests with `pytest --rootdir=...`; the
                # `--rootdir` CLI flag only exists in pytest >= 3.9, while the
                # cached venv ships pytest 3.2.1. Force a compatible pytest so
                # unit-test running/generation works. This runs on every build,
                # even when the (older) venv is restored from cache.
                [PYTHON, "-m", "pip", "install", "pytest==5.4.2", "pytest-httpbin==1.0.0"],
            ],
            included_files=[PROJECT_NAME],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
            set_rootdir=False,
        )


def register():
    Httpie(
        bug_id=1,
        buggy_commit_id="001bda19450ad85c91345eea3cfa3991e1d492ba",
        fixed_commit_id="5300b0b490b8db48fac30b5e32164be93dc574b7",
        test_files=[
            Path("tests", "test_downloads.py"),
        ],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename[foo.bar-0-foo.bar]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename[foo.bar-1-foo.bar-1]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename[foo.bar-10-foo.bar-10]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename[AAAAAAAAAAAAAAAAAAAA-0-AAAAAAAAAA]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename[AAAAAAAAAAAAAAAAAAAA-1-AAAAAAAA-1]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename"
                "[AAAAAAAAAAAAAAAAAAAA-10-AAAAAAA-10]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename"
                "[AAAAAAAAAAAAAAAAAAAA.txt-0-AAAAAA.txt]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename"
                "[AAAAAAAAAAAAAAAAAAAA.txt-1-AAAA.txt-1]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename"
                "[foo.AAAAAAAAAAAAAAAAAAAA-0-foo.AAAAAA]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename"
                "[foo.AAAAAAAAAAAAAAAAAAAA-1-foo.AAAA-1]",
            ),
            os.path.join(
                "tests",
                "test_downloads.py::TestDownloadUtils::test_unique_filename"
                "[foo.AAAAAAAAAAAAAAAAAAAA-10-foo.AAA-10]",
            ),
        ],
        api=Httpie1API(),
        systemtests=Httpie1SystemtestGenerator(),
        unittests=Httpie1UnittestGenerator(),
        loc=2432,
    )
    Httpie(
        bug_id=2,
        buggy_commit_id="356e0436510fee70b4071fac58be81c0a0a7db59",
        fixed_commit_id="e18b609ef7d867d6efa0efe42c832be5e0d09338",
        test_files=[
            Path("tests", "test_redirects.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_redirects.py::TestRedirects::test_max_redirects"
            ),
        ],
        relevant_test_files=[
            Path("tests", "test_exit_status.py"),
            Path("tests", "test_redirects.py"),
        ],
        api=Httpie2API(),
        systemtests=Httpie2SystemtestGenerator(),
        unittests=Httpie2UnittestGenerator(),
        loc=2281,
    )
    Httpie(
        bug_id=3,
        buggy_commit_id="8c33e5e3d31d3cd6476c4d9bc963a4c529f883d2",
        fixed_commit_id="589887939507ff26d36ec74bd2c045819cfa3d56",
        test_files=[
            Path("tests", "test_sessions.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_sessions.py::TestSession::test_download_in_session"
            ),
        ],
        relevant_test_files=[
            Path("tests", "test_downloads.py"),
            Path("tests", "test_sessions.py"),
        ],
        skip_tests=["test_session_ignored_header_prefixes"],
        api=Httpie3API(),
        systemtests=Httpie3SystemtestGenerator(),
        unittests=Httpie3UnittestGenerator(),
        loc=2255,
    )
    Httpie(
        bug_id=4,
        buggy_commit_id="8c892edd4fe700a7ca5cc733dcb4817831d253e2",
        fixed_commit_id="040d981f00c3f6830b2d0db3daf3c64c080e96e3",
        test_files=[
            Path("tests", "test_regressions.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_regressions.py::test_Host_header_overwrite"),
        ],
        relevant_test_files=[
            Path("tests", "test_cli.py"),
            Path("tests", "test_regressions.py"),
        ],
        api=Httpie4API(),
        systemtests=Httpie4SystemtestGenerator(),
        unittests=Httpie4UnittestGenerator(),
        loc=2125,
    )
    Httpie(
        bug_id=5,
        buggy_commit_id="16df8848e81eefac830f407e4b985f42b52970da",
        fixed_commit_id="90af1f742230831792d74d303d1e7ce56c96d4bd",
        test_files=[
            Path("tests", "tests.py"),
        ],
        test_cases=[
            os.path.join("tests", "tests.py::TestItemParsing::test_escape_longsep"),
        ],
        test_base=Path("tests", "tests.py"),
        skip_tests=["test_verbose"],
        api=Httpie5API(),
        systemtests=Httpie5SystemtestGenerator(),
        unittests=Httpie5UnittestGenerator(),
        loc=509,
    )


class HttpieAPI(API):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ---------------------------------------------------------------------------
# Bug 1: httpie.downloads.get_unique_filename did not trim overly long
# filenames to the maximum length supported by the target directory.
# The harness prints the filename produced by get_unique_filename; the oracle
# compares it against the expected (correctly trimmed) value passed as the last
# argument.  On the buggy build long names are returned untrimmed, so a test
# whose expected value is the trimmed name FAILS, while short names (no trimming
# required) behave identically on both builds and PASS.
# ---------------------------------------------------------------------------


def _bug1_trim_filename(filename: str, max_len: int) -> str:
    if len(filename) > max_len:
        trim_by = len(filename) - max_len
        name, ext = os.path.splitext(filename)
        if trim_by >= len(name):
            filename = filename[:-trim_by]
        else:
            filename = name[:-trim_by] + ext
    return filename


def _bug1_expected(orig: str, attempt: int, max_len: int) -> str:
    suffix = "-" + str(attempt) if attempt > 0 else ""
    eff = max_len - len(suffix)
    trimmed = _bug1_trim_filename(orig, eff) if len(orig) > eff else orig
    return trimmed + suffix


class Httpie1API(HttpieAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        # argv: [python, harness, orig, attempt, max_len, expected]
        try:
            expected = process.args[5]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result}"


class HttpieSystemtestGenerator(SystemtestGenerator, abc.ABC):
    pass


class Httpie1SystemtestGenerator(HttpieSystemtestGenerator):
    @staticmethod
    def _rand_name(alphabet, k_min, k_max):
        return "".join(
            random.choices(alphabet, k=random.randint(k_min, k_max))
        )

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        # A long filename that must be trimmed. The buggy build returns it
        # untrimmed, differing from the expected (trimmed) value -> FAILING.
        base = random.choice(string.ascii_uppercase)
        length = random.randint(15, 30)
        ext = random.choice(["", "", ".txt", ".dat", ".log", ".json"])
        orig = base * length + ext
        attempt = random.choice([0, 1, 2, 5, 10])
        max_len = random.randint(6, 12)
        expected = _bug1_expected(orig, attempt, max_len)
        return f"{orig} {attempt} {max_len} {expected}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        # A short filename that never needs trimming: identical on both builds.
        name = self._rand_name(string.ascii_lowercase, 3, 8)
        ext = random.choice(["", ".txt", ".bar", ".png"])
        orig = name + ext
        attempt = random.choice([0, 1, 2, 5, 10])
        max_len = 255
        expected = _bug1_expected(orig, attempt, max_len)
        return f"{orig} {attempt} {max_len} {expected}", TestResult.PASSING


class HttpieUnittestGenerator(UnittestGenerator, abc.ABC):
    pass


_BUG1_HELPER_SRC = (
    "import httpie.downloads\n"
    "\n"
    "def run_unique_filename(orig, attempt, max_len):\n"
    "    httpie.downloads.get_filename_max_length = lambda directory: max_len\n"
    "    def exists(filename):\n"
    "        if exists.attempt == attempt:\n"
    "            return False\n"
    "        exists.attempt += 1\n"
    "        return True\n"
    "    exists.attempt = 0\n"
    "    return httpie.downloads.get_unique_filename(orig, exists)\n"
)


class Httpie1UnittestGenerator(HttpieUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG1_HELPER_SRC).body

    @staticmethod
    def _make_test(orig, attempt, max_len, expected, result):
        test = Httpie1UnittestGenerator.get_empty_test()
        body_src = (
            f"self.assertEqual({expected!r}, "
            f"run_unique_filename({orig!r}, {attempt}, {max_len}))"
        )
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        base = random.choice(string.ascii_uppercase)
        length = random.randint(15, 30)
        ext = random.choice(["", "", ".txt", ".dat", ".log"])
        orig = base * length + ext
        attempt = random.choice([0, 1, 2, 5, 10])
        max_len = random.randint(6, 12)
        expected = _bug1_expected(orig, attempt, max_len)
        return self._make_test(orig, attempt, max_len, expected, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        name = "".join(
            random.choices(string.ascii_lowercase, k=random.randint(3, 8))
        )
        ext = random.choice(["", ".txt", ".bar", ".png"])
        orig = name + ext
        attempt = random.choice([0, 1, 2, 5, 10])
        max_len = 255
        expected = _bug1_expected(orig, attempt, max_len)
        return self._make_test(orig, attempt, max_len, expected, TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 2: httpie.client.get_response never propagated ``args.max_redirects`` to
# the requests session, so ``--max-redirects`` was ignored (the session kept
# requests' default of 30). The harness drives httpie against a local redirect
# chain of length ``n`` with ``--max-redirects=m`` and prints the resulting
# exit status. The oracle expects ERROR_TOO_MANY_REDIRECTS (6) when n > m and
# OK (0) otherwise. On the buggy build the limit is ignored -> always 0, so the
# n > m cases FAIL.
# ---------------------------------------------------------------------------

_BUG2_TOO_MANY_REDIRECTS = 6


class Httpie2API(HttpieAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            m = int(process.args[2])
            n = int(process.args[3])
        except (IndexError, TypeError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _BUG2_TOO_MANY_REDIRECTS if n > m else 0
        result = process.stdout.decode("utf8").strip()
        try:
            actual = int(result)
        except ValueError:
            return TestResult.UNDEFINED, f"Non-integer exit status: {result!r}"
        if actual == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected exit {expected}, but was {actual}"


class Httpie2SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        m = random.randint(0, 3)
        n = m + random.randint(1, 4)  # n > m -> should raise TooManyRedirects
        return f"{m} {n}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        m = random.randint(2, 6)
        n = random.randint(0, m)  # n <= m -> no redirect error
        return f"{m} {n}", TestResult.PASSING


# ---------------------------------------------------------------------------
# Bug 3: httpie.sessions.Session.update_headers called ``value.decode('utf8')``
# on every header value, crashing with AttributeError when a header value was
# explicitly set to None (an unset header). The fix skips None values. The
# harness prints "OK" only if update_headers completes; a None value therefore
# crashes the buggy build (no "OK") while the fixed build succeeds.
# ---------------------------------------------------------------------------

_BUG3_HEADER_NAMES = [
    "Foo", "Bar", "X-Test", "Accept", "X-Custom", "X-Token",
    "Authorization", "Referer", "Origin", "X-Api", "Cache", "X-Trace",
]


def _bug3_word(k_min=3, k_max=8):
    return "".join(
        random.choices(string.ascii_lowercase, k=random.randint(k_min, k_max))
    )


class Httpie3API(HttpieAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        result = process.stdout.decode("utf8").strip()
        if result == "OK":
            return TestResult.PASSING, ""
        return TestResult.FAILING, "update_headers did not complete"


class Httpie3SystemtestGenerator(HttpieSystemtestGenerator):
    @staticmethod
    def _byte_headers(names):
        return [f"{n}={_bug3_word()}" for n in names]

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        names = random.sample(_BUG3_HEADER_NAMES, k=random.randint(2, 4))
        # The last name carries an explicit None; the others are byte values.
        # Distinct names guarantee the None header is not overwritten.
        none_name = names[-1]
        tokens = self._byte_headers(names[:-1])
        tokens.append(f"{none_name}=__NONE__")
        random.shuffle(tokens)
        return " ".join(tokens), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        names = random.sample(_BUG3_HEADER_NAMES, k=random.randint(1, 3))
        return " ".join(self._byte_headers(names)), TestResult.PASSING


# ---------------------------------------------------------------------------
# Bug 4: httpie.models.HTTPRequest.headers checked ``'Host' not in headers``
# against a *plain* dict built from the (case-insensitive) request headers.
# A user-supplied host header with any casing other than exactly ``Host``
# (e.g. ``host``) was therefore not detected, so a second Host header was
# appended -> the dump contained two host headers. The fix tests membership
# against the original case-insensitive mapping. The oracle checks that the
# dump contains exactly one host header.
# ---------------------------------------------------------------------------

# Non-exact casings that are still case-insensitively equal to "host": the
# buggy build fails to detect them (plain dict, case-sensitive) and appends a
# second Host header, while the fixed build (case-insensitive check) does not.
_BUG4_HOST_CASINGS = ["host", "HOST", "hOst", "hOST", "HOsT", "hosT", "HoST", "hoSt"]


def _bug4_random_host():
    labels = ["example", "httpbin", "service", "api", "test", "server"]
    tld = random.choice(["com", "org", "net", "io"])
    return f"{random.choice(labels)}{random.randint(1, 999)}.{tld}"


def _bug4_random_url():
    ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
    path = "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
    return f"http://{ip}/{path}"


class Httpie4API(HttpieAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        result = process.stdout.decode("utf8")
        count = result.lower().count("host:")
        if count == 1:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected exactly one Host header, found {count}"


class Httpie4SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        url = _bug4_random_url()
        name = random.choice(_BUG4_HOST_CASINGS)
        value = _bug4_random_host()
        return f"{url} {name} {value}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        url = _bug4_random_url()
        if random.random() < 0.5:
            # Exact 'Host' casing: detected on both builds -> one header.
            return f"{url} Host {_bug4_random_host()}", TestResult.PASSING
        # No host header at all: both builds add exactly one.
        return f"{url} - {_bug4_random_host()}", TestResult.PASSING


# ---------------------------------------------------------------------------
# Bug 5: httpie.cli.KeyValueType located the key/value separator with the naive
# regex ``[^\\]`` + sep, which mishandles an escaped long separator (e.g. the
# ``\:=`` in ``bob\:==foo``). The fix records the spans of escaped separators
# and ignores separators that fall inside them. The harness prints the parsed
# ``(key, value, sep)`` tuple; the oracle recomputes the *correct* parse and
# compares. Items where the buggy parser diverges FAIL on the buggy build.
# ---------------------------------------------------------------------------

_BUG5_SEPS = (":", "=", ":=", "@")


def _bug5_fixed_parse(item, separators=_BUG5_SEPS):
    """Faithful re-implementation of the fixed KeyValueType.__call__."""
    found = {}
    escapes = ["\\\\" + sep for sep in separators]
    found_escapes = []
    for esc in escapes:
        found_escapes += [m.span() for m in re.finditer(esc, item)]
    for sep in separators:
        for match in re.finditer(sep, item):
            start, end = match.span()
            inside = False
            for estart, eend in found_escapes:
                if start >= estart and end <= eend:
                    inside = True
                    break
            if not inside:
                found[start] = sep
    if not found:
        return "ERROR"
    seploc = min(found.keys())
    sep = found[seploc]
    key = item[:seploc]
    value = item[seploc + len(sep):]
    for sepstr in separators:
        key = key.replace("\\" + sepstr, sepstr)
        value = value.replace("\\" + sepstr, sepstr)
    return (key, value, sep)


class Httpie5API(HttpieAPI):
    def get_test_arguments_from_string(self, s: str) -> List[str]:
        # The item may contain backslashes and separator characters; pass it
        # through verbatim as a single argument (no shell-style splitting).
        return [s.rstrip("\n")]

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            item = process.args[2]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _bug5_fixed_parse(item)
        expected_str = "ERROR" if expected == "ERROR" else repr(expected)
        result = process.stdout.decode("utf8").strip()
        if result == expected_str:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected_str}, but was {result}"


def _bug5_random_word(k_min=3, k_max=8):
    return "".join(
        random.choices(string.ascii_lowercase, k=random.randint(k_min, k_max))
    )


class Httpie5SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        # Escaped long separator followed by another separator -> the buggy
        # parser splits at the wrong position.
        key = _bug5_random_word()
        value = _bug5_random_word()
        trailing = random.choice(["=", ":", "@"])
        item = f"{key}\\:={trailing}{value}"
        return item, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        key = _bug5_random_word()
        value = _bug5_random_word()
        item = random.choice(
            [
                f"{key}={value}",
                f"{key}:{value}",
                f"{key}:={value}",
                f"{key}\\:{value}:{value}",
                f"{key}\\={value}={value}",
            ]
        )
        return item, TestResult.PASSING


_BUG2_HELPER_SRC = '''
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from httpie.context import Environment
from httpie.core import main


class _RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            n = int(self.path.rstrip("/").split("/")[-1])
        except ValueError:
            n = 0
        if n > 0:
            self.send_response(302)
            self.send_header("Location", "/redirect/%d" % (n - 1))
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"done")

    def log_message(self, *args):
        pass


def run_redirects(max_redirects, chain_length):
    server = HTTPServer(("127.0.0.1", 0), _RedirectHandler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    env = Environment(
        stdout=tempfile.TemporaryFile("w+b"),
        stderr=tempfile.TemporaryFile("w+t"),
        stdin_isatty=True,
        stdout_isatty=False,
        colors=0,
        config_dir=tempfile.mkdtemp(),
    )
    try:
        return main(
            ["--max-redirects=%d" % max_redirects, "--follow",
             "http://127.0.0.1:%d/redirect/%d" % (port, chain_length)],
            env=env,
        )
    finally:
        server.shutdown()
'''


class Httpie2UnittestGenerator(HttpieUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG2_HELPER_SRC).body

    def _make(self, m, n, expected, result):
        test = self.get_empty_test()
        body_src = f"self.assertEqual({expected}, run_redirects({m}, {n}))"
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        m = random.randint(0, 3)
        n = m + random.randint(1, 4)
        return self._make(m, n, 6, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        m = random.randint(2, 6)
        n = random.randint(0, m)
        return self._make(m, n, 0, TestResult.PASSING)


_BUG3_HELPER_SRC = (
    "from httpie.sessions import Session\n"
    "\n"
    "def run_update(pairs):\n"
    "    s = Session('/tmp/t4p_httpie_bug3_unit.json')\n"
    "    s['headers'] = {}\n"
    "    headers = {}\n"
    "    for name, value in pairs:\n"
    "        headers[name] = None if value is None else value.encode('utf8')\n"
    "    s.update_headers(headers)\n"
    "    return True\n"
)


class Httpie3UnittestGenerator(HttpieUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG3_HELPER_SRC).body

    def _make(self, pairs, result):
        test = self.get_empty_test()
        body_src = f"self.assertTrue(run_update({pairs!r}))"
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        names = random.sample(_BUG3_HEADER_NAMES, k=random.randint(2, 4))
        pairs = [(n, _bug3_word()) for n in names[:-1]]
        pairs.append((names[-1], None))
        random.shuffle(pairs)
        return self._make(pairs, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        names = random.sample(_BUG3_HEADER_NAMES, k=random.randint(1, 3))
        pairs = [(n, _bug3_word()) for n in names]
        return self._make(pairs, TestResult.PASSING)


_BUG4_HELPER_SRC = (
    "import requests\n"
    "from httpie.models import HTTPRequest\n"
    "\n"
    "def run_host_count(url, name, value):\n"
    "    headers = {}\n"
    "    if name != '-':\n"
    "        headers[name] = value\n"
    "    req = requests.Request('GET', url, headers=headers).prepare()\n"
    "    return HTTPRequest(req).headers.lower().count('host:')\n"
)


class Httpie4UnittestGenerator(HttpieUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG4_HELPER_SRC).body

    def _make(self, url, name, value, result):
        test = self.get_empty_test()
        body_src = (
            f"self.assertEqual(1, run_host_count({url!r}, {name!r}, {value!r}))"
        )
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            _bug4_random_url(),
            random.choice(_BUG4_HOST_CASINGS),
            _bug4_random_host(),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        url = _bug4_random_url()
        if random.random() < 0.5:
            return self._make(url, "Host", _bug4_random_host(), TestResult.PASSING)
        return self._make(url, "-", _bug4_random_host(), TestResult.PASSING)


_BUG5_HELPER_SRC = (
    "from httpie import cli\n"
    "\n"
    "def run_parse(item):\n"
    "    kt = cli.KeyValueType(cli.SEP_HEADERS, cli.SEP_DATA, "
    "cli.SEP_DATA_RAW_JSON, cli.SEP_FILES)\n"
    "    kv = kt(item)\n"
    "    return (kv.key, kv.value, kv.sep)\n"
)


class Httpie5UnittestGenerator(HttpieUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG5_HELPER_SRC).body

    def _make(self, item, result):
        expected = _bug5_fixed_parse(item)
        test = self.get_empty_test()
        body_src = f"self.assertEqual({expected!r}, run_parse({item!r}))"
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key = _bug5_random_word()
        value = _bug5_random_word()
        trailing = random.choice(["=", ":", "@"])
        item = f"{key}\\:={trailing}{value}"
        return self._make(item, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key = _bug5_random_word()
        value = _bug5_random_word()
        item = random.choice(
            [
                f"{key}={value}",
                f"{key}:{value}",
                f"{key}:={value}",
                f"{key}\\:{value}:{value}",
                f"{key}\\={value}={value}",
            ]
        )
        return self._make(item, TestResult.PASSING)


# A permissive right-linear grammar over printable characters. Every system
# test input for every httpie bug is a line of printable characters, so this
# parses them all while remaining fast for the Earley parser.
grammar_request: Grammar = {
    "<start>": ["<chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.printable),
}

assert is_valid_grammar(grammar_request)
