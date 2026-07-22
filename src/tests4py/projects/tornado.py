import abc
import ast
import os
import random
import string
from pathlib import Path
from typing import Any, List, Optional, Tuple

from tests4py.constants import PYTHON
from tests4py.grammars.fuzzer import Grammar, srange, is_valid_grammar
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "tornado"


class Tornado(Project):
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
            github_url="https://github.com/tornadoweb/tornado",
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
            api=api,
            grammar=grammar,
            loc=loc,
            source_base=Path(PROJECT_NAME),
            test_base=Path(PROJECT_NAME, "test"),
            included_files=[PROJECT_NAME],
            excluded_files=[os.path.join(PROJECT_NAME, "test")],
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
            ],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )


def register():
    Tornado(
        bug_id=1,
        buggy_commit_id="6a5a0bfa370b6c0d3dbbf9589a560a98202d2baa",
        fixed_commit_id="4677c54cc18bbfbdf0f4dadf11610fab6203fd63",
        test_files=[Path("tornado", "test", "websocket_test.py")],
        test_cases=[
            os.path.join(
                "tornado", "test", "websocket_test.py::WebSocketTest::test_nodelay"
            )
        ],
        api=Tornado1API(),
        systemtests=Tornado1SystemtestGenerator(),
        unittests=Tornado1UnittestGenerator(),
        grammar=grammar_printable,
        loc=12043,
    )
    Tornado(
        bug_id=2,
        buggy_commit_id="2ca8821d006f6693f920a4b183a3a7c985a5c8ad",
        fixed_commit_id="4f486a4aec746e9d66441600ee3b0743228b061c",
        test_files=[Path("tornado", "test", "httpclient_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "httpclient_test.py::HTTPClientCommonTestCase::test_redirect_put_without_body",
            )
        ],
        api=Tornado2API(),
        systemtests=Tornado2SystemtestGenerator(),
        unittests=Tornado2UnittestGenerator(),
        grammar=grammar_printable,
        loc=12025,
    )
    Tornado(
        bug_id=3,
        buggy_commit_id="940fd87fe9145d1154c8457221f86d56ea063c65",
        fixed_commit_id="aa622e724f80e0f7fcee369f75d69d1db13d72f2",
        test_files=[Path("tornado", "test", "httpclient_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "httpclient_test.py::SyncHTTPClientSubprocessTest::test_destructor_log",
            )
        ],
        api=Tornado3API(),
        systemtests=Tornado3SystemtestGenerator(),
        unittests=Tornado3UnittestGenerator(),
        grammar=grammar_printable,
        loc=11987,
    )
    Tornado(
        bug_id=4,
        buggy_commit_id="a8420fc681c5423d072978f00eab4d0645057d16",
        fixed_commit_id="db529031a1e1a6e951826aba0b7d0b18f05cd4c7",
        test_files=[Path("tornado", "test", "web_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "web_test.py::StaticFileTest::test_static_with_range_neg_past_start",
            ),
            os.path.join(
                "tornado",
                "test",
                "web_test.py::StaticFileTest::test_static_unsatisfiable_range_end_less_than_start",
            ),
        ],
        relevant_test_files=[
            os.path.join("tornado", "test", "web_test.py::StaticFileTest"),
        ],
        api=Tornado4API(),
        systemtests=Tornado4SystemtestGenerator(),
        unittests=Tornado4UnittestGenerator(),
        grammar=grammar_printable,
        loc=11970,
    )
    Tornado(
        bug_id=5,
        buggy_commit_id="2d4053daa56c609d642b214399e046671d4a593e",
        fixed_commit_id="886643965b5cb782503d8d7b374b7a794ec2077b",
        test_files=[Path("tornado", "test", "ioloop_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "ioloop_test.py::TestPeriodicCallbackMath::test_clock_backwards",
            )
        ],
        api=Tornado5API(),
        systemtests=Tornado5SystemtestGenerator(),
        unittests=Tornado5UnittestGenerator(),
        grammar=grammar_printable,
        loc=11937,
    )
    Tornado(
        bug_id=6,
        buggy_commit_id="fb74e4816ccfa7fc6a7abd8c8aab1f415cfc1b13",
        fixed_commit_id="2905ee4fb3c283d40b10f609359e189c83a0dc06",
        test_files=[Path("tornado", "test", "asyncio_test.py")],
        test_cases=[
            os.path.join(
                "tornado", "test", "asyncio_test.py::LeakTest::test_ioloop_close_leak"
            ),
            os.path.join(
                "tornado", "test", "asyncio_test.py::LeakTest::test_asyncio_close_leak"
            ),
        ],
        api=Tornado6API(),
        systemtests=Tornado6SystemtestGenerator(),
        unittests=Tornado6UnittestGenerator(),
        grammar=grammar_printable,
        loc=11926,
    )
    Tornado(
        bug_id=7,
        buggy_commit_id="fa3409179588536f2f743d16e537f6f9827fa92f",
        fixed_commit_id="a3b44cd701e0e82693363701bc0346b0125d2362",
        test_files=[Path("tornado", "test", "ioloop_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "ioloop_test.py::TestIOLoopFutures::test_run_in_executor_native",
            )
        ],
        api=Tornado7API(),
        systemtests=Tornado7SystemtestGenerator(),
        unittests=Tornado7UnittestGenerator(),
        grammar=grammar_printable,
        loc=11712,
    )
    Tornado(
        bug_id=8,
        buggy_commit_id="34c43f4775971ab9b2b8ed43356f218add6387b2",
        fixed_commit_id="5d4a9ab26372efd255bbb29fde55c41395ed17b1",
        test_files=[Path("tornado", "test", "websocket_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "websocket_test.py::WebSocketTest::test_missing_websocket_key",
            )
        ],
        api=Tornado8API(),
        systemtests=Tornado8SystemtestGenerator(),
        unittests=Tornado8UnittestGenerator(),
        grammar=grammar_printable,
        loc=11679,
    )
    Tornado(
        bug_id=9,
        buggy_commit_id="c9d2a3fa573987629ad576e991c2f3b65f4daab4",
        fixed_commit_id="86cc31f52992fb9d11f92de6fd5496842fea2265",
        test_files=[Path("tornado", "test", "httputil_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "httputil_test.py::TestUrlConcat::test_url_concat_none_params",
            )
        ],
        api=Tornado9API(),
        systemtests=Tornado9SystemtestGenerator(),
        unittests=Tornado9UnittestGenerator(),
        grammar=grammar_printable,
        loc=11632,
    )
    Tornado(
        bug_id=10,
        buggy_commit_id="ecd8968c5135b810cd607b5902dda2cd32122b39",
        fixed_commit_id="5931d913b4ea250891a0b582f1f8b2901b868c79",
        test_files=[Path("tornado", "test", "websocket_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "websocket_test.py::WebSocketTest::test_render_message",
            )
        ],
        api=Tornado10API(),
        systemtests=Tornado10SystemtestGenerator(),
        unittests=Tornado10UnittestGenerator(),
        grammar=grammar_printable,
        loc=11626,
    )
    Tornado(
        bug_id=11,
        buggy_commit_id="79ef301eb05cac82c075198e502d94dad296f6aa",
        fixed_commit_id="1131c9b50a6a4c0868d0d6fa5e0be077cf8fd1ca",
        test_files=[Path("tornado", "test", "httpserver_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "httpserver_test.py::HTTPServerRawTest::test_chunked_request_uppercase",
            )
        ],
        relevant_test_files=[
            os.path.join("tornado", "test", "httpserver_test.py::HTTPServerRawTest"),
            os.path.join("tornado", "test", "httpserver_test.py::HTTPServerTest"),
        ],
        skip_tests=[
            "test_invalid_content_length",
            "test_malformed_first_line",
            "test_malformed_headers",
        ],
        api=Tornado11API(),
        systemtests=Tornado11SystemtestGenerator(),
        unittests=Tornado11UnittestGenerator(),
        grammar=grammar_printable,
        loc=11233,
    )
    Tornado(
        bug_id=12,
        buggy_commit_id="4ee9ba94de11aaa4f932560fa2b3d8ceb8c61d2a",
        fixed_commit_id="301f52b532c071a0d2fec1eb7c23f2714bb38567",
        test_files=[Path("tornado", "test", "auth_test.py")],
        test_cases=[
            os.path.join(
                "tornado", "test", "auth_test.py::AuthTest::test_facebook_login"
            )
        ],
        api=Tornado12API(),
        systemtests=Tornado12SystemtestGenerator(),
        unittests=Tornado12UnittestGenerator(),
        grammar=grammar_printable,
        loc=11115,
    )
    Tornado(
        bug_id=13,
        buggy_commit_id="d7d9c467cda38f4c9352172ba7411edc29a85196",
        fixed_commit_id="34903f9e1a99441b2729bbe6f1d65d46cf352ea7",
        test_files=[
            Path("tornado", "test", "http1connection_test.py"),
            Path("tornado", "test", "simple_httpclient_test.py"),
        ],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "http1connection_test.py::HTTP1ConnectionTest::test_http10_no_content_length",
            )
        ],
        skip_tests=[
            "SimpleHTTPClientTest",
            "SimpleHTTPSClientTest",
            "MaxHeaderSizeTest",
            "MaxBodySizeTest",
            "ChunkedWithContentLengthTest",
        ],
        api=Tornado13API(),
        systemtests=Tornado13SystemtestGenerator(),
        unittests=Tornado13UnittestGenerator(),
        grammar=grammar_printable,
        loc=11187,
    )
    Tornado(
        bug_id=14,
        buggy_commit_id="81ee310adcd905fbdf7c98d9fb6ef0c5a46026c2",
        fixed_commit_id="1d02ed606f1c52636462633d009bdcbaac644331",
        test_files=[Path("tornado", "test", "ioloop_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "ioloop_test.py::TestIOLoopCurrent::test_force_current",
            )
        ],
        api=Tornado14API(),
        systemtests=Tornado14SystemtestGenerator(),
        unittests=Tornado14UnittestGenerator(),
        grammar=grammar_printable,
        loc=10942,
    )
    Tornado(
        bug_id=15,
        buggy_commit_id="fdfaf3dffa49479c7461050eacca07bc5ee8d207",
        fixed_commit_id="ecb3ea7543cc942659faf3d2144853018afa6139",
        test_files=[Path("tornado", "test", "web_test.py")],
        test_cases=[
            os.path.join(
                "tornado",
                "test",
                "web_test.py::StaticFileTest::test_path_traversal_protection",
            )
        ],
        relevant_test_files=[
            os.path.join("tornado", "test", "web_test.py::StaticFileTest"),
        ],
        api=Tornado15API(),
        systemtests=Tornado15SystemtestGenerator(),
        unittests=Tornado15UnittestGenerator(),
        grammar=grammar_printable,
        loc=10835,
    )
    Tornado(
        bug_id=16,
        buggy_commit_id="b450ff270df0395ee80f4ee5896a92bfe7f9b6ae",
        fixed_commit_id="d1676810ef5972c4defb0a710a1d8f8a0018983b",
        test_files=[Path("tornado", "test", "gen_test.py")],
        test_cases=[
            os.path.join(
                "tornado", "test", "gen_test.py::WaitIteratorTest::test_no_ref"
            )
        ],
        relevant_test_files=[
            os.path.join("tornado", "test", "gen_test.py::WaitIteratorTest"),
        ],
        api=Tornado16API(),
        systemtests=Tornado16SystemtestGenerator(),
        unittests=Tornado16UnittestGenerator(),
        grammar=grammar_printable,
        loc=10796,
    )


class TornadoAPI(API):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


class TornadoSystemtestGenerator(SystemtestGenerator, abc.ABC):
    pass


class TornadoUnittestGenerator(UnittestGenerator, abc.ABC):
    pass


def _rand_word(k_min: int = 3, k_max: int = 8) -> str:
    return "".join(
        random.choices(string.ascii_lowercase, k=random.randint(k_min, k_max))
    )


# A permissive right-linear grammar over printable characters. Every tornado
# system-test input is a single line of printable characters, so this parses
# them all while staying fast for the Earley parser.
grammar_printable: Grammar = {
    "<start>": ["<chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.printable),
}

assert is_valid_grammar(grammar_printable)


# ---------------------------------------------------------------------------
# Bug 9: tornado.httputil.url_concat raised ``TypeError`` when ``args`` was
# None instead of returning the URL unchanged. The harness prints the value of
# ``url_concat(url, args)`` (or ``ERROR`` if it raised); the oracle compares it
# to the expected (correct) value.  System-test format:
#     <url> <arg> <arg> ...
# where each <arg> is ``key=value`` or the single token ``__NONE__`` (meaning
# ``args=None``).  A None case FAILS on the buggy build (it prints ERROR while
# the correct value is the url unchanged); ordinary key/value cases behave
# identically on both builds and PASS.
# ---------------------------------------------------------------------------

_BUG9_NONE = "__NONE__"


def _bug9_expected(url: str, arg_tokens: List[str]) -> str:
    if arg_tokens == [_BUG9_NONE]:
        return url
    # url has no query string in the passing case, so url_concat simply
    # appends ``?k1=v1&k2=v2`` for URL-safe (alphanumeric) key/value pairs.
    return url + "?" + "&".join(arg_tokens)


def _bug9_random_url(with_query: bool = False) -> str:
    host = _rand_word(4, 8)
    tld = random.choice(["com", "org", "net", "io"])
    path = "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
    url = f"https://{host}.{tld}/{path}"
    if with_query:
        q = "&".join(
            f"{_rand_word(1, 3)}={random.randint(1, 99)}"
            for _ in range(random.randint(1, 2))
        )
        url += "?" + q
    return url


def _bug9_random_pairs() -> List[str]:
    n = random.randint(1, 3)
    tokens = []
    used = set()
    while len(tokens) < n:
        k = _rand_word(1, 4)
        if k in used:
            continue
        used.add(k)
        v = random.choice([_rand_word(2, 6), str(random.randint(1, 999))])
        tokens.append(f"{k}={v}")
    return tokens


class Tornado9API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            url = process.args[2]
            arg_tokens = list(process.args[3:])
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        if not arg_tokens:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _bug9_expected(url, arg_tokens)
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected!r}, but was {result!r}"


class Tornado9SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        url = _bug9_random_url(with_query=random.random() < 0.5)
        return f"{url} {_BUG9_NONE}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        url = _bug9_random_url(with_query=False)
        return url + " " + " ".join(_bug9_random_pairs()), TestResult.PASSING


_BUG9_UNIT_IMPORT = "from tornado.httputil import url_concat\n"


class Tornado9UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG9_UNIT_IMPORT).body

    @staticmethod
    def _make(body_src: str, result: TestResult):
        test = Tornado9UnittestGenerator.get_empty_test()
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        url = _bug9_random_url(with_query=random.random() < 0.5)
        body = f"self.assertEqual({url!r}, url_concat({url!r}, None))"
        return self._make(body, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        url = _bug9_random_url(with_query=False)
        tokens = _bug9_random_pairs()
        pairs = [tuple(t.split("=", 1)) for t in tokens]
        expected = _bug9_expected(url, tokens)
        body = f"self.assertEqual({expected!r}, url_concat({url!r}, {pairs!r}))"
        return self._make(body, TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 5: tornado.ioloop.PeriodicCallback._update_next did nothing when the
# clock jumped backwards (``_next_timeout > current_time``), so the callback
# schedule stalled.  The fix advances ``_next_timeout`` by one period in that
# case.  The harness replays a sequence of call durations against
# ``_update_next`` (mirroring the upstream ``simulate_calls`` helper) and
# prints the resulting list of scheduled times; the oracle recomputes the
# CORRECT (fixed) schedule and compares.  System-test format:
#     <callback_time_ms> <d1> <d2> ... <dn>
# A sequence containing a backwards jump (a negative duration before the last
# element) diverges on the buggy build -> FAILING; a purely forward sequence
# (all durations >= 0) behaves identically on both builds -> PASSING.
# ---------------------------------------------------------------------------

_BUG5_CB_TIMES = [1000, 2000, 5000, 10000]


def _bug5_fixed_schedule(callback_time: int, durations: List[int], now: int = 1000):
    import math

    cb = callback_time / 1000.0
    nt = float(now)
    calls = []
    for d in durations:
        if nt <= now:
            nt += (math.floor((now - nt) / cb) + 1) * cb
        else:
            nt += cb
        calls.append(nt)
        now = nt + d
    return [int(round(x)) for x in calls]


class Tornado5API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            callback_time = int(process.args[2])
            durations = [int(x) for x in process.args[3:]]
        except (IndexError, TypeError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if not durations:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _bug5_fixed_schedule(callback_time, durations)
        result = process.stdout.decode("utf8").strip()
        if result == str(expected):
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class Tornado5SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        cb = random.choice(_BUG5_CB_TIMES)
        n = random.randint(3, 6)
        # forward-ish durations, but force a backwards jump in a non-final slot
        durations = [random.randint(0, 15) for _ in range(n)]
        idx = random.randint(0, n - 2)
        durations[idx] = -random.randint(1, 120)
        return f"{cb} " + " ".join(str(d) for d in durations), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        cb = random.choice(_BUG5_CB_TIMES)
        n = random.randint(3, 6)
        durations = [random.randint(0, 40) for _ in range(n)]
        return f"{cb} " + " ".join(str(d) for d in durations), TestResult.PASSING


_BUG5_UNIT_HELPER = (
    "import math\n"
    "from tornado.ioloop import PeriodicCallback\n"
    "\n"
    "def run_periodic(callback_time, durations, now=1000):\n"
    "    pc = PeriodicCallback(None, callback_time)\n"
    "    pc._next_timeout = now\n"
    "    calls = []\n"
    "    for d in durations:\n"
    "        pc._update_next(now)\n"
    "        calls.append(pc._next_timeout)\n"
    "        now = pc._next_timeout + d\n"
    "    return [int(round(x)) for x in calls]\n"
)


class Tornado5UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG5_UNIT_HELPER).body

    @staticmethod
    def _make(cb: int, durations: List[int], expected, result: TestResult):
        test = Tornado5UnittestGenerator.get_empty_test()
        body = f"self.assertEqual({expected}, run_periodic({cb}, {durations}))"
        test.body = ast.parse(body).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        cb = random.choice(_BUG5_CB_TIMES)
        n = random.randint(3, 6)
        durations = [random.randint(0, 15) for _ in range(n)]
        idx = random.randint(0, n - 2)
        durations[idx] = -random.randint(1, 120)
        expected = _bug5_fixed_schedule(cb, durations)
        return self._make(cb, durations, expected, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        cb = random.choice(_BUG5_CB_TIMES)
        n = random.randint(3, 6)
        durations = [random.randint(0, 40) for _ in range(n)]
        expected = _bug5_fixed_schedule(cb, durations)
        return self._make(cb, durations, expected, TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 15: tornado.web.StaticFileHandler.validate_absolute_path computed the
# root prefix as ``os.path.abspath(root)`` WITHOUT a trailing separator, so a
# sibling directory/file whose name merely starts with the root's basename
# (e.g. root ``.../static`` and target ``.../static_foo.txt``) passed the
# ``startswith`` check and escaped the static root -> path traversal.  The fix
# appends ``os.path.sep`` to root.  The harness builds a temp filesystem, calls
# ``validate_absolute_path`` and prints ``403`` (HTTPError) or ``OK``.
# System-test format:  ``<rootname> <reqpath>``
#   - failing: ``<rootname> ../<rootname><suffix>.txt`` (existing sibling that
#     shares the root prefix) -> buggy returns OK, fixed raises 403 -> FAILING.
#   - passing: ``<rootname> <file>.txt`` (a genuine file inside root) -> both
#     builds return OK -> PASSING.
# ---------------------------------------------------------------------------

_BUG15_ROOTS = ["static", "assets", "public", "media", "files", "www", "dist"]


class Tornado15API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            reqpath = process.args[3]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "403" if reqpath.startswith("../") else "OK"
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class Tornado15SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        root = random.choice(_BUG15_ROOTS)
        suffix = random.choice(["_", ""]) + _rand_word(2, 6)
        return f"{root} ../{root}{suffix}.txt", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        root = random.choice(_BUG15_ROOTS)
        return f"{root} {_rand_word(3, 8)}.txt", TestResult.PASSING


_BUG15_UNIT_HELPER = (
    "import os\n"
    "import tempfile\n"
    "from tornado.web import Application, StaticFileHandler, HTTPError\n"
    "from tornado.httputil import HTTPServerRequest, HTTPConnection\n"
    "\n"
    "class _T4PFakeConn(HTTPConnection):\n"
    "    def set_close_callback(self, cb):\n"
    "        pass\n"
    "\n"
    "def run_validate(rootname, reqpath):\n"
    "    base = tempfile.mkdtemp()\n"
    "    root = os.path.join(base, rootname)\n"
    "    os.makedirs(root, exist_ok=True)\n"
    "    app = Application()\n"
    "    req = HTTPServerRequest(method='GET', uri='/x', connection=_T4PFakeConn())\n"
    "    h = StaticFileHandler(app, req, path=root)\n"
    "    h.path = reqpath\n"
    "    absolute_path = h.get_absolute_path(root, reqpath)\n"
    "    parent = os.path.dirname(absolute_path)\n"
    "    if parent and not os.path.isdir(parent):\n"
    "        os.makedirs(parent, exist_ok=True)\n"
    "    with open(absolute_path, 'w') as fp:\n"
    "        fp.write('data')\n"
    "    try:\n"
    "        h.validate_absolute_path(root, absolute_path)\n"
    "        return 'OK'\n"
    "    except HTTPError as e:\n"
    "        return str(e.status_code)\n"
)


class Tornado15UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG15_UNIT_HELPER).body

    @staticmethod
    def _make(rootname: str, reqpath: str, expected: str, result: TestResult):
        test = Tornado15UnittestGenerator.get_empty_test()
        body = f"self.assertEqual({expected!r}, run_validate({rootname!r}, {reqpath!r}))"
        test.body = ast.parse(body).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        root = random.choice(_BUG15_ROOTS)
        suffix = random.choice(["_", ""]) + _rand_word(2, 6)
        return self._make(root, f"../{root}{suffix}.txt", "403", TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        root = random.choice(_BUG15_ROOTS)
        return self._make(root, f"{_rand_word(3, 8)}.txt", "OK", TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 4: tornado.web.StaticFileHandler.get mishandled two Range-header cases:
# a suffix range reaching past the start of the file (``bytes=-N`` with N >
# size) and an unsatisfiable range whose end precedes its start
# (``bytes=A-B`` with B < A).  On the buggy build both crash the handler with
# a 500; the fix clamps the negative start to 0 (-> 200, whole file served)
# and treats end < start as unsatisfiable (-> 416).  The harness starts a
# StaticFileHandler server on a temp file of the given size and prints the HTTP
# status code for the request.  System-test format:  ``<size> <range-header>``.
# The oracle recomputes the CORRECT (fixed) status code.
# ---------------------------------------------------------------------------


def _bug4_int_or_none(v: str):
    v = v.strip()
    return None if not v else int(v)


def _bug4_parse_request_range(range_header: str):
    unit, _, value = range_header.partition("=")
    unit, value = unit.strip(), value.strip()
    if unit != "bytes":
        return None
    start_b, _, end_b = value.partition("-")
    try:
        start = _bug4_int_or_none(start_b)
        end = _bug4_int_or_none(end_b)
    except ValueError:
        return None
    if end is not None:
        if start is None:
            if end != 0:
                start = -end
                end = None
        else:
            end += 1
    return (start, end)


def _bug4_fixed_status(size: int, range_header: str) -> int:
    request_range = _bug4_parse_request_range(range_header) if range_header else None
    if not request_range:
        return 200
    start, end = request_range
    if start is not None and start < 0:
        start += size
        if start < 0:
            start = 0
    if (
        start is not None and (start >= size or (end is not None and start >= end))
    ) or end == 0:
        return 416
    if end is not None and end > size:
        end = size
    if size != (end or size) - (start or 0):
        return 206
    return 200


class Tornado4API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            size = int(process.args[2])
            range_header = process.args[3]
        except (IndexError, TypeError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _bug4_fixed_status(size, range_header)
        result = process.stdout.decode("utf8").strip()
        try:
            actual = int(result)
        except ValueError:
            return TestResult.UNDEFINED, f"Non-integer status: {result!r}"
        if actual == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected status {expected}, but was {actual}"


class Tornado4SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        size = random.randint(10, 200)
        if random.random() < 0.5:
            # suffix range past the start of the file
            n = size + random.randint(1, 1_000_000)
            rh = f"bytes=-{n}"
        else:
            # unsatisfiable range: end < start, with start inside the file
            a = random.randint(1, size - 1)
            b = random.randint(0, a - 1)
            rh = f"bytes={a}-{b}"
        return f"{size} {rh}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        size = random.randint(20, 200)
        if random.random() < 0.5:
            start = random.randint(0, size - 2)
            end = random.randint(start, size - 1)
            rh = f"bytes={start}-{end}"
        else:
            k = random.randint(1, size)
            rh = f"bytes=-{k}"
        return f"{size} {rh}", TestResult.PASSING


_BUG4_UNIT_HELPER = (
    "import os\n"
    "import tempfile\n"
    "import tornado.web\n"
    "import tornado.httpserver\n"
    "import tornado.ioloop\n"
    "from tornado.httpclient import AsyncHTTPClient, HTTPRequest\n"
    "from tornado.testing import bind_unused_port\n"
    "\n"
    "def run_range(size, range_header):\n"
    "    tmpdir = tempfile.mkdtemp()\n"
    "    with open(os.path.join(tmpdir, 'f.txt'), 'wb') as fp:\n"
    "        fp.write(b'A' * size)\n"
    "    async def _run():\n"
    "        app = tornado.web.Application([\n"
    "            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': tmpdir})])\n"
    "        sock, port = bind_unused_port()\n"
    "        server = tornado.httpserver.HTTPServer(app)\n"
    "        server.add_socket(sock)\n"
    "        client = AsyncHTTPClient()\n"
    "        req = HTTPRequest('http://127.0.0.1:%d/static/f.txt' % port,\n"
    "                          method='GET', headers={'Range': range_header})\n"
    "        resp = await client.fetch(req, raise_error=False)\n"
    "        server.stop()\n"
    "        return resp.code\n"
    "    return tornado.ioloop.IOLoop.current().run_sync(_run)\n"
)


class Tornado4UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG4_UNIT_HELPER).body

    @staticmethod
    def _make(size: int, range_header: str, expected: int, result: TestResult):
        test = Tornado4UnittestGenerator.get_empty_test()
        body = f"self.assertEqual({expected}, run_range({size}, {range_header!r}))"
        test.body = ast.parse(body).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        size = random.randint(10, 200)
        if random.random() < 0.5:
            n = size + random.randint(1, 1_000_000)
            rh = f"bytes=-{n}"
        else:
            a = random.randint(1, size - 1)
            b = random.randint(0, a - 1)
            rh = f"bytes={a}-{b}"
        expected = _bug4_fixed_status(size, rh)
        return self._make(size, rh, expected, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        size = random.randint(20, 200)
        if random.random() < 0.5:
            start = random.randint(0, size - 2)
            end = random.randint(start, size - 1)
            rh = f"bytes={start}-{end}"
        else:
            k = random.randint(1, size)
            rh = f"bytes=-{k}"
        expected = _bug4_fixed_status(size, rh)
        return self._make(size, rh, expected, TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 8: tornado.websocket.WebSocketProtocol13.accept_connection let a
# ``ValueError`` raised while validating the WebSocket handshake headers (e.g.
# a missing or empty ``Sec-WebSocket-Key``) escape, so the server answered a
# malformed upgrade request with a 500.  The fix catches that ValueError and
# responds with 400.  The harness starts a WebSocketHandler server and issues a
# plain HTTP request for one of several handshake scenarios, printing the
# status code.  System-test format:  ``<scenario> <nonce>``.  A malformed
# handshake (missing/empty key) yields 500 on the buggy build vs the expected
# 400 -> FAILING; benign scenarios (plain GET -> 400, bad version -> 426)
# behave identically on both builds -> PASSING.  The ``<nonce>`` only makes the
# generated tests distinct.
# ---------------------------------------------------------------------------

_BUG8_EXPECTED = {
    "MISSING_KEY": 400,
    "EMPTY_KEY": 400,
    "PLAIN": 400,
    "BAD_VERSION": 426,
}
_BUG8_FAILING = ["MISSING_KEY", "EMPTY_KEY"]
# Only PLAIN is used for passing tests: it deterministically yields 400 on both
# builds.  BAD_VERSION is kept in the expected map for completeness but not
# generated, as its handshake can occasionally race to a transport-level error.
_BUG8_PASSING = ["PLAIN"]


class Tornado8API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            scenario = process.args[2]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _BUG8_EXPECTED.get(scenario)
        if expected is None:
            return TestResult.UNDEFINED, f"Unknown scenario {scenario!r}"
        result = process.stdout.decode("utf8").strip()
        try:
            actual = int(result)
        except ValueError:
            return TestResult.UNDEFINED, f"Non-integer status: {result!r}"
        if actual == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected status {expected}, but was {actual}"


class Tornado8SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(_BUG8_FAILING)} {_rand_word(4, 8)}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(_BUG8_PASSING)} {_rand_word(4, 8)}",
            TestResult.PASSING,
        )


_BUG8_UNIT_HELPER = (
    "import tornado.web\n"
    "import tornado.httpserver\n"
    "import tornado.ioloop\n"
    "import tornado.websocket\n"
    "from tornado.httpclient import AsyncHTTPClient, HTTPRequest\n"
    "from tornado.testing import bind_unused_port\n"
    "\n"
    "class _T4PEchoHandler(tornado.websocket.WebSocketHandler):\n"
    "    def on_message(self, message):\n"
    "        self.write_message(message)\n"
    "\n"
    "_T4P_WS_SCENARIOS = {\n"
    "    'MISSING_KEY': {'Connection': 'Upgrade', 'Upgrade': 'WebSocket',\n"
    "                    'Sec-WebSocket-Version': '13'},\n"
    "    'EMPTY_KEY': {'Connection': 'Upgrade', 'Upgrade': 'WebSocket',\n"
    "                  'Sec-WebSocket-Version': '13', 'Sec-WebSocket-Key': ''},\n"
    "    'PLAIN': {},\n"
    "    'BAD_VERSION': {'Connection': 'Upgrade', 'Upgrade': 'WebSocket',\n"
    "                    'Sec-WebSocket-Version': '8', 'Sec-WebSocket-Key': 'abc'},\n"
    "}\n"
    "\n"
    "def run_ws(scenario, nonce=''):\n"
    "    headers = _T4P_WS_SCENARIOS[scenario]\n"
    "    async def _run():\n"
    "        app = tornado.web.Application([(r'/echo', _T4PEchoHandler)])\n"
    "        sock, port = bind_unused_port()\n"
    "        server = tornado.httpserver.HTTPServer(app)\n"
    "        server.add_socket(sock)\n"
    "        resp = await AsyncHTTPClient().fetch(\n"
    "            HTTPRequest('http://127.0.0.1:%d/echo' % port, headers=headers),\n"
    "            raise_error=False)\n"
    "        server.stop()\n"
    "        return resp.code\n"
    "    return tornado.ioloop.IOLoop.current().run_sync(_run)\n"
)


class Tornado8UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG8_UNIT_HELPER).body

    @staticmethod
    def _make(scenario: str, nonce: str, result: TestResult):
        expected = _BUG8_EXPECTED[scenario]
        test = Tornado8UnittestGenerator.get_empty_test()
        body = f"self.assertEqual({expected}, run_ws({scenario!r}, {nonce!r}))"
        test.body = ast.parse(body).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            random.choice(_BUG8_FAILING), _rand_word(4, 8), TestResult.FAILING
        )

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            random.choice(_BUG8_PASSING), _rand_word(4, 8), TestResult.PASSING
        )


# ---------------------------------------------------------------------------
# Bug 14: tornado.ioloop.IOLoop.__init__ inverted the ``make_current=True``
# guard: it raised "current IOLoop already exists" when NO current loop existed
# (and silently succeeded when one did), the exact opposite of the intended
# behaviour.  The harness runs a construction scenario and prints ``OK`` (no
# RuntimeError) or ``RAISED``.  System-test format:  ``<scenario> <nonce>``.
#   - SINGLE_TRUE: build IOLoop(make_current=True) on a cleared state -> fixed
#     OK, buggy RAISED -> FAILING.
#   - DEFAULT_THEN_TRUE: a default IOLoop (becomes current) then another with
#     make_current=True -> fixed RAISED, buggy OK -> FAILING.
#   - MC_FALSE / DEFAULT / DOUBLE_DEFAULT: no make_current=True conflict, so
#     both builds succeed (OK) -> PASSING.
# ---------------------------------------------------------------------------

_BUG14_EXPECTED = {
    "SINGLE_TRUE": "OK",
    "DEFAULT_THEN_TRUE": "RAISED",
    "MC_FALSE": "OK",
    "DEFAULT": "OK",
    "DOUBLE_DEFAULT": "OK",
}
_BUG14_FAILING = ["SINGLE_TRUE", "DEFAULT_THEN_TRUE"]
_BUG14_PASSING = ["MC_FALSE", "DEFAULT", "DOUBLE_DEFAULT"]


class Tornado14API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            scenario = process.args[2]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _BUG14_EXPECTED.get(scenario)
        if expected is None:
            return TestResult.UNDEFINED, f"Unknown scenario {scenario!r}"
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class Tornado14SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(_BUG14_FAILING)} {_rand_word(4, 8)}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(_BUG14_PASSING)} {_rand_word(4, 8)}",
            TestResult.PASSING,
        )


_BUG14_UNIT_HELPER = (
    "from tornado.ioloop import IOLoop\n"
    "\n"
    "def run_ioloop(scenario, nonce=''):\n"
    "    IOLoop.clear_current()\n"
    "    loops = []\n"
    "    raised = False\n"
    "    try:\n"
    "        if scenario == 'SINGLE_TRUE':\n"
    "            loops.append(IOLoop(make_current=True))\n"
    "        elif scenario == 'DEFAULT_THEN_TRUE':\n"
    "            loops.append(IOLoop())\n"
    "            loops.append(IOLoop(make_current=True))\n"
    "        elif scenario == 'MC_FALSE':\n"
    "            loops.append(IOLoop(make_current=False))\n"
    "        elif scenario == 'DEFAULT':\n"
    "            loops.append(IOLoop())\n"
    "        elif scenario == 'DOUBLE_DEFAULT':\n"
    "            loops.append(IOLoop())\n"
    "            loops.append(IOLoop())\n"
    "    except RuntimeError:\n"
    "        raised = True\n"
    "    finally:\n"
    "        for _loop in loops:\n"
    "            try:\n"
    "                _loop.close()\n"
    "            except Exception:\n"
    "                pass\n"
    "        IOLoop.clear_current()\n"
    "    return 'RAISED' if raised else 'OK'\n"
)


class Tornado14UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG14_UNIT_HELPER).body

    @staticmethod
    def _make(scenario: str, nonce: str, result: TestResult):
        expected = _BUG14_EXPECTED[scenario]
        test = Tornado14UnittestGenerator.get_empty_test()
        body = f"self.assertEqual({expected!r}, run_ioloop({scenario!r}, {nonce!r}))"
        test.body = ast.parse(body).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            random.choice(_BUG14_FAILING), _rand_word(4, 8), TestResult.FAILING
        )

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            random.choice(_BUG14_PASSING), _rand_word(4, 8), TestResult.PASSING
        )


# ---------------------------------------------------------------------------
# Bug 11: tornado.http1connection compared the Transfer-Encoding header with a
# case-sensitive ``== "chunked"`` instead of ``.lower() == "chunked"``, so a
# request whose Transfer-Encoding value contained any uppercase letter (e.g.
# ``Chunked``) was not dechunked and its body was dropped.  The harness POSTs a
# single-chunk ``key=value`` body with a chosen Transfer-Encoding casing and
# prints the echoed, form-parsed arguments as JSON.  System-test format:
#     <te_casing> <key> <value>
#   - failing: a casing with an uppercase letter -> buggy echoes ``{}`` while
#     the fixed build echoes ``{"key": ["value"]}`` -> FAILING.
#   - passing: the exact lowercase ``chunked`` -> both echo the parsed body
#     -> PASSING.
# ---------------------------------------------------------------------------


def _bug11_upper_casing() -> str:
    # a casing of "chunked" with at least one uppercase letter
    word = "chunked"
    while True:
        cased = "".join(
            c.upper() if random.random() < 0.5 else c for c in word
        )
        if cased != word:
            return cased


class Tornado11API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            key = process.args[3]
            value = process.args[4]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = '{"%s": ["%s"]}' % (key, value)
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class Tornado11SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{_bug11_upper_casing()} {_rand_word(3, 6)} {_rand_word(3, 6)}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"chunked {_rand_word(3, 6)} {_rand_word(3, 6)}",
            TestResult.PASSING,
        )


_BUG11_UNIT_HELPER = (
    "import socket\n"
    "import threading\n"
    "import tornado.web\n"
    "import tornado.httpserver\n"
    "import tornado.ioloop\n"
    "from tornado.testing import bind_unused_port\n"
    "from tornado.web import RequestHandler\n"
    "from tornado.escape import recursive_unicode\n"
    "\n"
    "class _T4PEcho(RequestHandler):\n"
    "    def post(self):\n"
    "        self.write(recursive_unicode(self.request.arguments))\n"
    "\n"
    "def run_chunked(te_casing, key, value):\n"
    "    holder = {}\n"
    "    started = threading.Event()\n"
    "    def _serve():\n"
    "        io = tornado.ioloop.IOLoop()\n"
    "        io.make_current()\n"
    "        app = tornado.web.Application([('/echo', _T4PEcho)])\n"
    "        sock, port = bind_unused_port()\n"
    "        server = tornado.httpserver.HTTPServer(app)\n"
    "        server.add_socket(sock)\n"
    "        holder['port'] = port\n"
    "        holder['io'] = io\n"
    "        started.set()\n"
    "        io.start()\n"
    "    t = threading.Thread(target=_serve, daemon=True)\n"
    "    t.start()\n"
    "    started.wait(10)\n"
    "    try:\n"
    "        body = '%s=%s' % (key, value)\n"
    "        chunk = '%x\\r\\n%s\\r\\n0\\r\\n\\r\\n' % (len(body), body)\n"
    "        req = ('POST /echo HTTP/1.1\\r\\nTransfer-Encoding: %s\\r\\n'\n"
    "               'Content-Type: application/x-www-form-urlencoded\\r\\n\\r\\n%s'\n"
    "               % (te_casing, chunk))\n"
    "        s = socket.create_connection(('127.0.0.1', holder['port']), timeout=10)\n"
    "        s.settimeout(10)\n"
    "        s.sendall(req.encode())\n"
    "        data = b''\n"
    "        while b'\\r\\n\\r\\n' not in data:\n"
    "            data += s.recv(4096)\n"
    "        header, _, rest = data.partition(b'\\r\\n\\r\\n')\n"
    "        cl = 0\n"
    "        for line in header.split(b'\\r\\n'):\n"
    "            if line.lower().startswith(b'content-length:'):\n"
    "                cl = int(line.split(b':')[1].strip())\n"
    "        body_bytes = rest\n"
    "        while len(body_bytes) < cl:\n"
    "            body_bytes += s.recv(4096)\n"
    "        s.close()\n"
    "        return body_bytes[:cl].decode()\n"
    "    finally:\n"
    "        holder['io'].add_callback(holder['io'].stop)\n"
    "        t.join(10)\n"
)


class Tornado11UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG11_UNIT_HELPER).body

    @staticmethod
    def _make(te_casing: str, key: str, value: str, result: TestResult):
        expected = '{"%s": ["%s"]}' % (key, value)
        test = Tornado11UnittestGenerator.get_empty_test()
        body = (
            f"self.assertEqual({expected!r}, "
            f"run_chunked({te_casing!r}, {key!r}, {value!r}))"
        )
        test.body = ast.parse(body).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            _bug11_upper_casing(), _rand_word(3, 6), _rand_word(3, 6),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            "chunked", _rand_word(3, 6), _rand_word(3, 6), TestResult.PASSING
        )


# ---------------------------------------------------------------------------
# Bug 13: tornado.http1connection.HTTP1Connection._can_keep_alive accessed
# ``start_line.method`` unconditionally, but a *response* start line has no
# ``method`` attribute -> reading an HTTP/1.0 response without a Content-Length
# crashed with AttributeError.  The fix uses ``getattr(start_line, 'method',
# None)``.  The harness drives ``read_response`` over a pair of connected
# streams against a raw server response and prints ``"<code>,<body>"`` (or
# ``ERROR:<type>``).  System-test format:  ``<mode> <body>``.
#   - failing: HTTP10_NOCL (HTTP/1.0, no Content-Length) -> buggy AttributeError
#     vs fixed ``200,<body>`` -> FAILING.
#   - passing: HTTP11_CL / HTTP10_CL (a Content-Length header short-circuits the
#     keep-alive check before ``.method``) -> both builds return ``200,<body>``
#     -> PASSING.
# ---------------------------------------------------------------------------

_BUG13_FAILING = ["HTTP10_NOCL"]
_BUG13_PASSING = ["HTTP11_CL", "HTTP10_CL"]


class Tornado13API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            body = process.args[3]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = f"200,{body}"
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class Tornado13SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(_BUG13_FAILING)} {_rand_word(3, 8)}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(_BUG13_PASSING)} {_rand_word(3, 8)}",
            TestResult.PASSING,
        )


_BUG13_UNIT_HELPER = (
    "import socket\n"
    "import tornado.ioloop\n"
    "from tornado.iostream import IOStream\n"
    "from tornado.testing import bind_unused_port\n"
    "from tornado.netutil import add_accept_handler\n"
    "from tornado.http1connection import HTTP1Connection\n"
    "from tornado.httputil import HTTPMessageDelegate\n"
    "from tornado.locks import Event\n"
    "from tornado import gen\n"
    "\n"
    "def run_response(mode, body):\n"
    "    io = tornado.ioloop.IOLoop()\n"
    "    io.make_current()\n"
    "    result = {}\n"
    "    @gen.coroutine\n"
    "    def _main():\n"
    "        listener, port = bind_unused_port()\n"
    "        ev = Event()\n"
    "        holder = {}\n"
    "        def _accept(conn, addr):\n"
    "            holder['server'] = IOStream(conn)\n"
    "            ev.set()\n"
    "        add_accept_handler(listener, _accept, io_loop=io)\n"
    "        client = IOStream(socket.socket())\n"
    "        yield [client.connect(('127.0.0.1', port)), ev.wait()]\n"
    "        io.remove_handler(listener)\n"
    "        listener.close()\n"
    "        server = holder['server']\n"
    "        conn = HTTP1Connection(client, True)\n"
    "        b = body.encode()\n"
    "        if mode == 'HTTP10_NOCL':\n"
    "            server.write(b'HTTP/1.0 200 OK\\r\\n\\r\\n' + b)\n"
    "        elif mode == 'HTTP11_CL':\n"
    "            server.write(b'HTTP/1.1 200 OK\\r\\nContent-Length: %d\\r\\n\\r\\n' % len(b) + b)\n"
    "        elif mode == 'HTTP10_CL':\n"
    "            server.write(b'HTTP/1.0 200 OK\\r\\nContent-Length: %d\\r\\n\\r\\n' % len(b) + b)\n"
    "        server.close()\n"
    "        code = [None]\n"
    "        got = []\n"
    "        done = Event()\n"
    "        class _D(HTTPMessageDelegate):\n"
    "            def headers_received(self, start_line, headers):\n"
    "                code[0] = start_line.code\n"
    "            def data_received(self, data):\n"
    "                got.append(data)\n"
    "            def finish(self):\n"
    "                done.set()\n"
    "        try:\n"
    "            yield conn.read_response(_D())\n"
    "            yield done.wait()\n"
    "            result['out'] = '%s,%s' % (code[0], b''.join(got).decode())\n"
    "        except Exception as e:\n"
    "            result['out'] = 'ERROR:%s' % type(e).__name__\n"
    "    io.run_sync(_main)\n"
    "    return result['out']\n"
)


class Tornado13UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG13_UNIT_HELPER).body

    @staticmethod
    def _make(mode: str, body: str, result: TestResult):
        test = Tornado13UnittestGenerator.get_empty_test()
        src = (
            f"self.assertEqual('200,{body}', run_response({mode!r}, {body!r}))"
        )
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            random.choice(_BUG13_FAILING), _rand_word(3, 8), TestResult.FAILING
        )

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            random.choice(_BUG13_PASSING), _rand_word(3, 8), TestResult.PASSING
        )


# ---------------------------------------------------------------------------
# Bug 7: tornado.ioloop.IOLoop.run_in_executor returned the raw
# ``concurrent.futures.Future`` from ``executor.submit`` instead of wrapping it
# in a Tornado Future, so ``await run_in_executor(...)`` raised TypeError in a
# native coroutine.  The fix chains it into a TracebackFuture.  The harness runs
# a native coroutine on an IOLoop and prints its result (or ``ERROR:<type>``).
# System-test format:  ``<mode> <word>``.
#   - failing: EXECUTOR awaits ``run_in_executor(None, len, word)`` -> buggy
#     TypeError vs fixed ``str(len(word))`` -> FAILING.
#   - passing: DIRECT returns ``word`` from the coroutine without the executor
#     -> both builds return ``word`` -> PASSING.
# ---------------------------------------------------------------------------

_BUG7_FAILING = ["EXECUTOR"]
_BUG7_PASSING = ["DIRECT"]


class Tornado7API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            mode = process.args[2]
            word = process.args[3]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(len(word)) if mode == "EXECUTOR" else word
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected!r}, but was {result!r}"


class Tornado7SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"EXECUTOR {_rand_word(3, 10)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"DIRECT {_rand_word(3, 10)}", TestResult.PASSING


_BUG7_UNIT_HELPER = (
    "from tornado.ioloop import IOLoop\n"
    "\n"
    "def run_executor(mode, word):\n"
    "    io = IOLoop()\n"
    "    io.make_current()\n"
    "    async def _run():\n"
    "        if mode == 'EXECUTOR':\n"
    "            return str(await io.run_in_executor(None, len, word))\n"
    "        return word\n"
    "    try:\n"
    "        return io.run_sync(_run)\n"
    "    finally:\n"
    "        io.close()\n"
)


class Tornado7UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG7_UNIT_HELPER).body

    @staticmethod
    def _make(mode: str, word: str, result: TestResult):
        expected = str(len(word)) if mode == "EXECUTOR" else word
        test = Tornado7UnittestGenerator.get_empty_test()
        src = f"self.assertEqual({expected!r}, run_executor({mode!r}, {word!r}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("EXECUTOR", _rand_word(3, 10), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("DIRECT", _rand_word(3, 10), TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 1: tornado.websocket.WebSocketHandler.set_nodelay asserted on and used
# ``self.stream`` (which is None on a WebSocketHandler) instead of delegating
# to ``self.ws_connection``, so calling ``set_nodelay`` inside ``open()`` raised
# and tore the connection down.  The harness starts a WebSocket server and reads
# the message the handler sends on open, printing it (or ``ERROR:<...>``).
# System-test format:  ``<mode> <word>``.
#   - failing: NODELAY handler calls ``set_nodelay(True)`` in open -> buggy
#     drops the connection (no message) vs fixed delivers ``word`` -> FAILING.
#   - passing: PLAIN handler just sends ``word`` -> both builds deliver it
#     -> PASSING.
# ---------------------------------------------------------------------------

_BUG1_FAILING = ["NODELAY"]
_BUG1_PASSING = ["PLAIN"]


class Tornado1API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            word = process.args[3]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        result = process.stdout.decode("utf8").strip()
        if result == word:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {word!r}, but was {result!r}"


class Tornado1SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"NODELAY {_rand_word(3, 10)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"PLAIN {_rand_word(3, 10)}", TestResult.PASSING


_BUG1_UNIT_HELPER = (
    "import tornado.web\n"
    "import tornado.httpserver\n"
    "import tornado.ioloop\n"
    "from tornado.testing import bind_unused_port\n"
    "from tornado.websocket import websocket_connect, WebSocketHandler\n"
    "from tornado import gen\n"
    "\n"
    "def run_nodelay(mode, word):\n"
    "    io = tornado.ioloop.IOLoop()\n"
    "    io.make_current()\n"
    "    holder = {}\n"
    "    class _NoDelay(WebSocketHandler):\n"
    "        def open(self):\n"
    "            self.set_nodelay(True)\n"
    "            self.write_message(word)\n"
    "    class _Plain(WebSocketHandler):\n"
    "        def open(self):\n"
    "            self.write_message(word)\n"
    "    handler = _NoDelay if mode == 'NODELAY' else _Plain\n"
    "    @gen.coroutine\n"
    "    def _main():\n"
    "        app = tornado.web.Application([('/ws', handler)])\n"
    "        sock, port = bind_unused_port()\n"
    "        server = tornado.httpserver.HTTPServer(app)\n"
    "        server.add_socket(sock)\n"
    "        try:\n"
    "            ws = yield websocket_connect('ws://127.0.0.1:%d/ws' % port)\n"
    "            msg = yield ws.read_message()\n"
    "            holder['out'] = msg if msg is not None else 'ERROR:None'\n"
    "        except Exception as e:\n"
    "            holder['out'] = 'ERROR:%s' % type(e).__name__\n"
    "    io.run_sync(_main)\n"
    "    return holder['out']\n"
)


class Tornado1UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG1_UNIT_HELPER).body

    @staticmethod
    def _make(mode: str, word: str, result: TestResult):
        test = Tornado1UnittestGenerator.get_empty_test()
        src = f"self.assertEqual({word!r}, run_nodelay({mode!r}, {word!r}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("NODELAY", _rand_word(3, 10), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("PLAIN", _rand_word(3, 10), TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 10: tornado.web.RequestHandler broke reference cycles (nulling
# ``self.ui`` etc.) inside ``finish()``; because a WebSocketHandler calls
# ``finish()`` during the handshake, ``self.ui`` was gone by the time an
# established connection tried to ``render_string`` in ``on_message`` -> the
# render failed and the connection dropped.  The fix defers cycle-breaking for
# WebSocket handlers until the connection is really closed.  The harness sends a
# message to a WebSocket handler and prints the reply.  System-test format:
#     <mode> <word>
#   - failing: RENDER handler replies with ``render_string('message.html',
#     message=word)`` -> buggy drops the connection vs fixed ``<b>word</b>``
#     -> FAILING.
#   - passing: ECHO handler replies with ``word`` -> both builds deliver it
#     -> PASSING.
# ---------------------------------------------------------------------------


class Tornado10API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            mode = process.args[2]
            word = process.args[3]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = f"<b>{word}</b>" if mode == "RENDER" else word
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected!r}, but was {result!r}"


class Tornado10SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"RENDER {_rand_word(3, 10)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"ECHO {_rand_word(3, 10)}", TestResult.PASSING


_BUG10_UNIT_HELPER = (
    "import tornado.web\n"
    "import tornado.httpserver\n"
    "import tornado.ioloop\n"
    "from tornado.testing import bind_unused_port\n"
    "from tornado.websocket import websocket_connect, WebSocketHandler\n"
    "from tornado.template import DictLoader\n"
    "from tornado import gen\n"
    "\n"
    "def run_render(mode, word):\n"
    "    io = tornado.ioloop.IOLoop()\n"
    "    io.make_current()\n"
    "    holder = {}\n"
    "    class _Render(WebSocketHandler):\n"
    "        def on_message(self, message):\n"
    "            self.write_message(self.render_string('message.html', message=message))\n"
    "    class _Echo(WebSocketHandler):\n"
    "        def on_message(self, message):\n"
    "            self.write_message(message)\n"
    "    handler = _Render if mode == 'RENDER' else _Echo\n"
    "    @gen.coroutine\n"
    "    def _main():\n"
    "        app = tornado.web.Application([('/ws', handler)],\n"
    "            template_loader=DictLoader({'message.html': '<b>{{ message }}</b>'}))\n"
    "        sock, port = bind_unused_port()\n"
    "        server = tornado.httpserver.HTTPServer(app)\n"
    "        server.add_socket(sock)\n"
    "        try:\n"
    "            ws = yield websocket_connect('ws://127.0.0.1:%d/ws' % port)\n"
    "            ws.write_message(word)\n"
    "            msg = yield ws.read_message()\n"
    "            holder['out'] = msg if msg is not None else 'ERROR:None'\n"
    "        except Exception as e:\n"
    "            holder['out'] = 'ERROR:%s' % type(e).__name__\n"
    "    io.run_sync(_main)\n"
    "    return holder['out']\n"
)


class Tornado10UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG10_UNIT_HELPER).body

    @staticmethod
    def _make(mode: str, word: str, result: TestResult):
        expected = f"<b>{word}</b>" if mode == "RENDER" else word
        test = Tornado10UnittestGenerator.get_empty_test()
        src = f"self.assertEqual({expected!r}, run_render({mode!r}, {word!r}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("RENDER", _rand_word(3, 10), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("ECHO", _rand_word(3, 10), TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 6: tornado.platform.asyncio.BaseAsyncIOLoop never removed its entry from
# ``IOLoop._ioloop_for_asyncio`` when the loop was closed, so repeatedly
# creating and closing loops leaked one map entry per loop.  The fix deletes the
# entry on close and prunes closed loops on creation.  The harness runs a
# create/close scenario and prints the growth of ``len(_ioloop_for_asyncio)``.
# System-test format:  ``<scenario> <n>``.
#   - failing: IOLOOP_CLOSE (create+close n Tornado loops -> fixed leaks 0,
#     buggy leaks n) and ASYNCIO_CLOSE (create+close n asyncio loops -> fixed
#     leaves exactly 1 dangling, buggy leaves n) -> FAILING.
#   - passing: KEEP (create n loops WITHOUT closing -> both builds hold n live
#     entries) -> PASSING.
# ---------------------------------------------------------------------------


class Tornado6API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            scenario = process.args[2]
            n = int(process.args[3])
        except (IndexError, TypeError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if scenario == "IOLOOP_CLOSE":
            expected = 0
        elif scenario == "ASYNCIO_CLOSE":
            expected = 1
        elif scenario == "KEEP":
            expected = n
        else:
            return TestResult.UNDEFINED, f"Unknown scenario {scenario!r}"
        result = process.stdout.decode("utf8").strip()
        try:
            actual = int(result)
        except ValueError:
            return TestResult.UNDEFINED, f"Non-integer count: {result!r}"
        if actual == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected leak {expected}, but was {actual}"


class Tornado6SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        # Only IOLOOP_CLOSE is generated: it deterministically leaks exactly n
        # entries on the buggy build (0 on the fixed build).  ASYNCIO_CLOSE is
        # left in the oracle for completeness but not generated, as its leak
        # count can vary with GC/loop-reuse timing.
        return f"IOLOOP_CLOSE {random.randint(3, 20)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"KEEP {random.randint(1, 20)}", TestResult.PASSING


_BUG6_UNIT_HELPER = (
    "import asyncio\n"
    "from tornado.ioloop import IOLoop\n"
    "from tornado.platform.asyncio import AsyncIOLoop\n"
    "\n"
    "def run_leak(scenario, n):\n"
    "    AsyncIOLoop().close()\n"
    "    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())\n"
    "    orig = len(IOLoop._ioloop_for_asyncio)\n"
    "    if scenario == 'IOLOOP_CLOSE':\n"
    "        for _ in range(n):\n"
    "            loop = AsyncIOLoop()\n"
    "            loop.close()\n"
    "        return len(IOLoop._ioloop_for_asyncio) - orig\n"
    "    if scenario == 'ASYNCIO_CLOSE':\n"
    "        for _ in range(n):\n"
    "            loop = asyncio.new_event_loop()\n"
    "            loop.call_soon(IOLoop.current)\n"
    "            loop.call_soon(loop.stop)\n"
    "            loop.run_forever()\n"
    "            loop.close()\n"
    "        return len(IOLoop._ioloop_for_asyncio) - orig\n"
    "    loops = []\n"
    "    for _ in range(n):\n"
    "        loops.append(AsyncIOLoop())\n"
    "    count = len(IOLoop._ioloop_for_asyncio) - orig\n"
    "    for loop in loops:\n"
    "        loop.close()\n"
    "    return count\n"
)


class Tornado6UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG6_UNIT_HELPER).body

    @staticmethod
    def _make(scenario: str, n: int, expected: int, result: TestResult):
        test = Tornado6UnittestGenerator.get_empty_test()
        src = f"self.assertEqual({expected}, run_leak({scenario!r}, {n}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = random.randint(3, 20)
        return self._make("IOLOOP_CLOSE", n, 0, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = random.randint(1, 20)
        return self._make("KEEP", n, n, TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 16: tornado.gen.WaitIterator used only weak references to itself, so when
# it was constructed inline (with no strong reference other than the Future its
# ``next()`` returns) it could be garbage-collected before its callback fired,
# leaving ``next()`` unresolved forever.  The fix adds a hard self-reference on
# the running future.  The harness awaits ``WaitIterator(...).next()`` under a
# short timeout and prints ``OK`` (resolved) or ``TIMEOUT``.  System-test
# format:  ``<scenario> <nonce>``.
#   - failing: WAIT_NOREF constructs the iterator inline (no strong ref) ->
#     buggy is GC'd and times out vs fixed resolves -> FAILING.
#   - passing: WAIT_REF keeps a strong reference to the iterator -> both builds
#     resolve -> PASSING.  The ``<nonce>`` only makes tests distinct.
# ---------------------------------------------------------------------------

_BUG16_FAILING = ["WAIT_NOREF"]
_BUG16_PASSING = ["WAIT_REF"]


class Tornado16API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            scenario = process.args[2]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        if scenario not in ("WAIT_NOREF", "WAIT_REF"):
            return TestResult.UNDEFINED, f"Unknown scenario {scenario!r}"
        result = process.stdout.decode("utf8").strip()
        if result == "OK":
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected OK, but was {result!r}"


class Tornado16SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"WAIT_NOREF {_rand_word(4, 8)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"WAIT_REF {_rand_word(4, 8)}", TestResult.PASSING


_BUG16_UNIT_HELPER = (
    "import datetime\n"
    "from tornado.ioloop import IOLoop\n"
    "from tornado import gen\n"
    "\n"
    "def run_wait(scenario, nonce=''):\n"
    "    io = IOLoop()\n"
    "    io.make_current()\n"
    "    @gen.coroutine\n"
    "    def _main():\n"
    "        try:\n"
    "            if scenario == 'WAIT_NOREF':\n"
    "                yield gen.with_timeout(datetime.timedelta(seconds=0.5),\n"
    "                                       gen.WaitIterator(gen.sleep(0)).next())\n"
    "            else:\n"
    "                wi = gen.WaitIterator(gen.sleep(0))\n"
    "                yield gen.with_timeout(datetime.timedelta(seconds=0.5), wi.next())\n"
    "            raise gen.Return('OK')\n"
    "        except gen.TimeoutError:\n"
    "            raise gen.Return('TIMEOUT')\n"
    "    try:\n"
    "        return io.run_sync(_main)\n"
    "    finally:\n"
    "        io.close()\n"
)


class Tornado16UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG16_UNIT_HELPER).body

    @staticmethod
    def _make(scenario: str, nonce: str, result: TestResult):
        test = Tornado16UnittestGenerator.get_empty_test()
        src = f"self.assertEqual('OK', run_wait({scenario!r}, {nonce!r}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("WAIT_NOREF", _rand_word(4, 8), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("WAIT_REF", _rand_word(4, 8), TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 3: tornado.httpclient.AsyncHTTPClient.close raised (and logged from the
# HTTPClient destructor) "inconsistent AsyncHTTPClient cache" during
# interpreter shutdown, because the weakref-based instance cache could already
# hold None for the io_loop.  The fix pops the cache entry and only errors when
# a *different* live client is found.  The harness runs the upstream repro in a
# fresh subprocess and prints ``CLEAN`` (no output) or ``OUTPUT``.  System-test
# format:  ``<mode> <nonce>``.
#   - failing: LAMBDA runs ``... f = lambda: None; c = HTTPClient()`` whose
#     shutdown triggers the destructor error on the buggy build -> ``OUTPUT``
#     vs fixed ``CLEAN`` -> FAILING.
#   - passing: INT runs the same with ``f`` bound to an int, which never
#     triggers the error -> both builds are ``CLEAN`` -> PASSING.
# ---------------------------------------------------------------------------

_BUG3_SNIPPETS = {
    "LAMBDA": "from tornado.httpclient import HTTPClient; f = lambda: None; c = HTTPClient()",
    "INT": "from tornado.httpclient import HTTPClient; f = 5; c = HTTPClient()",
}


class Tornado3API(TornadoAPI):
    def __init__(self, default_timeout: int = 30):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            mode = process.args[2]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode not in _BUG3_SNIPPETS:
            return TestResult.UNDEFINED, f"Unknown mode {mode!r}"
        result = process.stdout.decode("utf8").strip()
        if result == "CLEAN":
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected CLEAN, but was {result!r}"


class Tornado3SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"LAMBDA {_rand_word(4, 8)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"INT {_rand_word(4, 8)}", TestResult.PASSING


_BUG3_UNIT_HELPER = (
    "import subprocess\n"
    "import sys\n"
    "\n"
    "_T4P_BUG3_SNIPPETS = {\n"
    "    'LAMBDA': 'from tornado.httpclient import HTTPClient; f = lambda: None; c = HTTPClient()',\n"
    "    'INT': 'from tornado.httpclient import HTTPClient; f = 5; c = HTTPClient()',\n"
    "}\n"
    "\n"
    "def run_destructor(mode, nonce=''):\n"
    "    proc = subprocess.run(\n"
    "        [sys.executable, '-c', _T4P_BUG3_SNIPPETS[mode]],\n"
    "        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)\n"
    "    return 'OUTPUT' if proc.stdout.strip() else 'CLEAN'\n"
)


class Tornado3UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG3_UNIT_HELPER).body

    @staticmethod
    def _make(mode: str, nonce: str, result: TestResult):
        test = Tornado3UnittestGenerator.get_empty_test()
        src = f"self.assertEqual('CLEAN', run_destructor({mode!r}, {nonce!r}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("LAMBDA", _rand_word(4, 8), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("INT", _rand_word(4, 8), TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 2: tornado.http1connection.HTTP1Connection.write_headers disabled chunked
# output framing whenever ANY ``Transfer-Encoding`` header was present, even
# when it was explicitly ``chunked`` -- so a PUT/POST/PATCH body sent with a
# user-supplied ``Transfer-Encoding: chunked`` was written unframed (no
# ``0\r\n\r\n`` terminator), corrupting the request.  The fix keeps chunked
# framing when the encoding is ``chunked``.  The harness writes a request body
# over an HTTP1Connection with a chosen framing header and inspects the raw
# bytes the peer receives, printing ``CHUNKED`` or ``RAW``.  System-test format:
#     <mode> <body>
#   - failing: TE_CHUNKED sends ``Transfer-Encoding: chunked`` -> buggy writes
#     an unframed (RAW) body vs fixed writes proper chunk framing (CHUNKED)
#     -> FAILING.
#   - passing: CONTENT_LENGTH sends a ``Content-Length`` header (never chunked)
#     -> both builds write a RAW body -> PASSING.
# ---------------------------------------------------------------------------


class Tornado2API(TornadoAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            mode = process.args[2]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "TE_CHUNKED":
            expected = "CHUNKED"
        elif mode == "CONTENT_LENGTH":
            expected = "RAW"
        else:
            return TestResult.UNDEFINED, f"Unknown mode {mode!r}"
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class Tornado2SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"TE_CHUNKED {_rand_word(3, 10)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"CONTENT_LENGTH {_rand_word(3, 10)}", TestResult.PASSING


_BUG2_UNIT_HELPER = (
    "import socket\n"
    "import tornado.ioloop\n"
    "from tornado.iostream import IOStream\n"
    "from tornado.testing import bind_unused_port\n"
    "from tornado.netutil import add_accept_handler\n"
    "from tornado.http1connection import HTTP1Connection\n"
    "from tornado.httputil import RequestStartLine, HTTPHeaders\n"
    "from tornado.locks import Event\n"
    "from tornado import gen\n"
    "\n"
    "def run_write(mode, body):\n"
    "    io = tornado.ioloop.IOLoop()\n"
    "    io.make_current()\n"
    "    holder = {}\n"
    "    @gen.coroutine\n"
    "    def _main():\n"
    "        listener, port = bind_unused_port()\n"
    "        ev = Event()\n"
    "        h = {}\n"
    "        def _accept(conn, addr):\n"
    "            h['server'] = IOStream(conn)\n"
    "            ev.set()\n"
    "        add_accept_handler(listener, _accept)\n"
    "        client = IOStream(socket.socket())\n"
    "        yield [client.connect(('127.0.0.1', port)), ev.wait()]\n"
    "        io.remove_handler(listener)\n"
    "        listener.close()\n"
    "        server = h['server']\n"
    "        conn = HTTP1Connection(client, True)\n"
    "        headers = HTTPHeaders()\n"
    "        if mode == 'TE_CHUNKED':\n"
    "            headers.add('Transfer-Encoding', 'chunked')\n"
    "        else:\n"
    "            headers.add('Content-Length', str(len(body)))\n"
    "        yield conn.write_headers(RequestStartLine('PUT', '/put', 'HTTP/1.1'), headers)\n"
    "        yield conn.write(body.encode())\n"
    "        conn.finish()\n"
    "        data = b''\n"
    "        while b'\\r\\n\\r\\n' not in data:\n"
    "            data += yield server.read_bytes(1, partial=True)\n"
    "        for _ in range(400):\n"
    "            try:\n"
    "                chunk = yield gen.with_timeout(io.time() + 0.5,\n"
    "                                               server.read_bytes(1, partial=True))\n"
    "                data += chunk\n"
    "            except Exception:\n"
    "                break\n"
    "        _, _, rest = data.partition(b'\\r\\n\\r\\n')\n"
    "        holder['out'] = 'CHUNKED' if b'0\\r\\n\\r\\n' in rest else 'RAW'\n"
    "    io.run_sync(_main)\n"
    "    return holder['out']\n"
)


class Tornado2UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG2_UNIT_HELPER).body

    @staticmethod
    def _make(mode: str, body: str, result: TestResult):
        expected = "CHUNKED" if mode == "TE_CHUNKED" else "RAW"
        test = Tornado2UnittestGenerator.get_empty_test()
        src = f"self.assertEqual({expected!r}, run_write({mode!r}, {body!r}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("TE_CHUNKED", _rand_word(3, 10), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("CONTENT_LENGTH", _rand_word(3, 10), TestResult.PASSING)


# ---------------------------------------------------------------------------
# Bug 12: tornado.auth.FacebookGraphMixin.get_authenticated_user parsed the
# access-token response with the non-existent ``escape.parse_qs_bytes`` and
# passed the ``_auth_return_future`` callback straight into ``oauth2_request``
# instead of chaining futures, so completing the Facebook OAuth flow
# (``/facebook/client/login?code=...``) errored out.  The fix uses
# ``urlparse.parse_qs`` and chains the request future.  The harness runs a
# minimal Facebook OAuth app and prints the HTTP status of a login request.
# System-test format:  ``<mode> <nonce>``.
#   - failing: CODE completes the token exchange (``?code=1234``) -> buggy fails
#     (non-200) vs fixed 200 -> FAILING.
#   - passing: REDIRECT starts the flow with no code -> both builds answer 302
#     -> PASSING.  The ``<nonce>`` only makes tests distinct.
# ---------------------------------------------------------------------------


class Tornado12API(TornadoAPI):
    def __init__(self, default_timeout: int = 30):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            mode = process.args[2]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "CODE":
            expected = "200"
        elif mode == "REDIRECT":
            expected = "302"
        else:
            return TestResult.UNDEFINED, f"Unknown mode {mode!r}"
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {result!r}"


class Tornado12SystemtestGenerator(TornadoSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"CODE {_rand_word(4, 8)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"REDIRECT {_rand_word(4, 8)}", TestResult.PASSING


_BUG12_UNIT_HELPER = (
    "import tornado.web\n"
    "import tornado.httpserver\n"
    "import tornado.ioloop\n"
    "from tornado.testing import bind_unused_port\n"
    "from tornado.httpclient import AsyncHTTPClient, HTTPRequest\n"
    "from tornado.web import RequestHandler\n"
    "from tornado.auth import FacebookGraphMixin\n"
    "from tornado import gen\n"
    "\n"
    "class _T4PFacebookLogin(RequestHandler, FacebookGraphMixin):\n"
    "    def initialize(self, base):\n"
    "        self._OAUTH_AUTHORIZE_URL = base + '/facebook/server/authorize'\n"
    "        self._OAUTH_ACCESS_TOKEN_URL = base + '/facebook/server/access_token'\n"
    "        self._FACEBOOK_BASE_URL = base + '/facebook/server'\n"
    "    @gen.coroutine\n"
    "    def get(self):\n"
    "        if self.get_argument('code', None):\n"
    "            user = yield self.get_authenticated_user(\n"
    "                redirect_uri=self.request.full_url(),\n"
    "                client_id=self.settings['facebook_api_key'],\n"
    "                client_secret=self.settings['facebook_secret'],\n"
    "                code=self.get_argument('code'))\n"
    "            self.write(user)\n"
    "        else:\n"
    "            yield self.authorize_redirect(\n"
    "                redirect_uri=self.request.full_url(),\n"
    "                client_id=self.settings['facebook_api_key'],\n"
    "                extra_params={'scope': 'read_stream'})\n"
    "\n"
    "class _T4PAccessToken(RequestHandler):\n"
    "    def get(self):\n"
    "        self.write('access_token=asdf')\n"
    "\n"
    "class _T4PMe(RequestHandler):\n"
    "    def get(self):\n"
    "        self.write('{}')\n"
    "\n"
    "def run_facebook(mode, nonce=''):\n"
    "    io = tornado.ioloop.IOLoop()\n"
    "    io.make_current()\n"
    "    holder = {}\n"
    "    @gen.coroutine\n"
    "    def _main():\n"
    "        sock, port = bind_unused_port()\n"
    "        base = 'http://127.0.0.1:%d' % port\n"
    "        app = tornado.web.Application([\n"
    "            ('/facebook/client/login', _T4PFacebookLogin, dict(base=base)),\n"
    "            ('/facebook/server/access_token', _T4PAccessToken),\n"
    "            ('/facebook/server/me', _T4PMe),\n"
    "        ], facebook_api_key='test_key', facebook_secret='test_secret')\n"
    "        server = tornado.httpserver.HTTPServer(app)\n"
    "        server.add_socket(sock)\n"
    "        client = AsyncHTTPClient()\n"
    "        suffix = '?code=1234' if mode == 'CODE' else ''\n"
    "        url = base + '/facebook/client/login' + suffix\n"
    "        resp = yield client.fetch(\n"
    "            HTTPRequest(url, follow_redirects=False, request_timeout=10),\n"
    "            raise_error=False)\n"
    "        holder['out'] = resp.code\n"
    "    io.run_sync(_main)\n"
    "    return holder['out']\n"
)


class Tornado12UnittestGenerator(TornadoUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG12_UNIT_HELPER).body

    @staticmethod
    def _make(mode: str, nonce: str, result: TestResult):
        expected = 200 if mode == "CODE" else 302
        test = Tornado12UnittestGenerator.get_empty_test()
        src = f"self.assertEqual({expected}, run_facebook({mode!r}, {nonce!r}))"
        test.body = ast.parse(src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("CODE", _rand_word(4, 8), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("REDIRECT", _rand_word(4, 8), TestResult.PASSING)
