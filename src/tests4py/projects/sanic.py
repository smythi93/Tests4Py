import abc
import ast
import os.path
import random
import string
from pathlib import Path
from typing import Any, List, Optional, Tuple

from tests4py.grammars.fuzzer import Grammar, srange, is_valid_grammar
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "sanic"


class Sanic(Project):
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
        python_version: Optional[str] = None,
        init: bool = False,
        setup: Optional[List[List[str]]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/huge-success/sanic",
            status=Status.OK,
            python_version=python_version or "3.8.3",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version=python_version or "3.8.4",
            python_fallback_version=python_version or "3.8.4",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar,
            loc=loc,
            source_base=Path(PROJECT_NAME),
            test_base=Path("tests"),
            included_files=[PROJECT_NAME],
            excluded_files=[
                os.path.join(PROJECT_NAME, "__init__.py" if init else "__version__.py")
            ],
            setup=setup
            or [
                ["python", "-m", "pip", "install", "-e", "."],
            ],
            relevant_test_files=relevant_test_files,
        )


def register():
    Sanic(
        bug_id=1,
        buggy_commit_id="e7001b00747b659f7042b0534802b936ee8a53e0",
        fixed_commit_id="44973125c15304b4262c51c78b5a86bd1daafa86",
        test_files=[Path("tests", "test_blueprints.py")],
        test_cases=[
            os.path.join("tests", "test_blueprints.py::test_bp_middleware_order")
        ],
        api=Sanic1API(),
        systemtests=Sanic1SystemtestGenerator(),
        unittests=Sanic1UnittestGenerator(),
        grammar=grammar_1,
        loc=4763,
    )
    Sanic(
        bug_id=2,
        buggy_commit_id="ba9b432993019b0af0c4827a5ed42aaa091bd17d",
        fixed_commit_id="801595e24acdf8050b8d3ffa512d424147848d32",
        test_files=[Path("tests", "test_app.py")],
        test_cases=[
            os.path.join("tests", "test_app.py::test_asyncio_server_start_serving")
        ],
        test_status_buggy=TestStatus.PASSING,
        api=Sanic2API(),
        systemtests=Sanic2SystemtestGenerator(),
        unittests=Sanic2UnittestGenerator(),
        grammar=grammar_2,
        loc=4861,
    )
    Sanic(
        bug_id=3,
        buggy_commit_id="91f6abaa81248189fbcbdf685e8bdcbb7846609f",
        fixed_commit_id="861e87347a2d373d6ffa387965a6887c83af632c",
        test_files=[Path("tests", "test_url_for.py")],
        test_cases=[os.path.join("tests", "test_url_for.py::test_routes_with_host")],
        relevant_test_files=[
            Path("tests", "test_url_for.py"),
            Path("tests", "test_url_for_static.py"),
        ],
        api=Sanic3API(),
        systemtests=Sanic3SystemtestGenerator(),
        unittests=Sanic3UnittestGenerator(),
        grammar=grammar_3,
        loc=4889,
    )
    Sanic(
        bug_id=4,
        buggy_commit_id="e506c89304948bba593e8603ecace1c495b06fd5",
        fixed_commit_id="e81a8ce07329e95d3d0899b1d774f21759c28e0e",
        test_files=[Path("tests", "test_requests.py")],
        test_cases=[
            os.path.join("tests", "test_requests.py::test_url_for_without_server_name")
        ],
        api=Sanic4API(),
        systemtests=Sanic4SystemtestGenerator(),
        unittests=Sanic4UnittestGenerator(),
        grammar=grammar_4,
        # sanic 19.9.0 pins ``requests-async==0.5.0`` which is no longer on
        # PyPI; install it from its GitHub tag and install sanic itself without
        # re-resolving dependencies (the cached venv already has the rest).
        setup=[
            [
                "python",
                "-m",
                "pip",
                "install",
                "git+https://github.com/encode/requests-async@0.5.0",
            ],
            ["python", "-m", "pip", "install", "-e", ".", "--no-deps"],
        ],
        loc=4870,
    )
    Sanic(
        bug_id=5,
        buggy_commit_id="e3a27c2cc485d57aa1ff87d9f69098e4ab12727e",
        fixed_commit_id="b63c06c75a54752d7f3115d3c635580db44b8399",
        test_files=[Path("tests", "test_logging.py")],
        test_cases=[
            os.path.join(
                "tests", "test_logging.py::test_logging_modified_root_logger_config"
            )
        ],
        api=Sanic5API(),
        systemtests=Sanic5SystemtestGenerator(),
        unittests=Sanic5UnittestGenerator(),
        grammar=grammar_5,
        python_version="3.7.8",
        init=True,
        loc=3755,
    )


class SanicAPI(API):
    def __init__(self, default_timeout: int = 30):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


class SanicSystemtestGenerator(SystemtestGenerator, abc.ABC):
    pass


class SanicUnittestGenerator(UnittestGenerator, abc.ABC):
    pass


def _rand_token(k_min: int = 4, k_max: int = 8) -> str:
    return "".join(
        random.choices(string.ascii_lowercase, k=random.randint(k_min, k_max))
    )


# ---------------------------------------------------------------------------
# Bug 1: Sanic.register_named_middleware appended (rather than prepended)
# blueprint *response* middleware, so named response middleware ran in
# registration order instead of reverse-registration order.  The fix uses
# ``appendleft``.  The harness registers ``n`` named middleware of a given
# kind on a single route and prints the resulting deque order (by index).
# For request middleware the order is forward on both builds; for response
# middleware the *fixed* order is reversed while the buggy build keeps it
# forward.  A response case with n >= 2 therefore FAILS on the buggy build.
# ---------------------------------------------------------------------------


def _bug1_expected(kind: str, n: int) -> List[int]:
    if kind == "response":
        return list(reversed(range(n)))
    return list(range(n))


class Sanic1API(SanicAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            kind = process.args[2]
            n = int(process.args[3])
        except (IndexError, TypeError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _bug1_expected(kind, n)
        result_line = None
        for line in process.stdout.decode("utf8").splitlines():
            if line.startswith("RESULT"):
                result_line = line[len("RESULT"):].strip()
                break
        if result_line is None:
            return TestResult.FAILING, "No RESULT produced"
        actual = [int(x) for x in result_line.split()] if result_line else []
        if actual == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {actual}"


class Sanic1SystemtestGenerator(SanicSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        n = random.randint(2, 20)
        return f"response {n}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        if random.random() < 0.7:
            # request middleware: forward order on both builds
            n = random.randint(2, 20)
            return f"request {n}", TestResult.PASSING
        # a single (or no) response middleware: reverse == forward
        n = random.randint(0, 1)
        return f"response {n}", TestResult.PASSING


_BUG1_HELPER_SRC = (
    "import logging\n"
    "logging.disable(logging.CRITICAL)\n"
    "from sanic import Sanic\n"
    "\n"
    "def run_named_middleware_order(name, kind, n):\n"
    "    def make(i):\n"
    "        def mw(request, response=None):\n"
    "            return None\n"
    "        mw.idx = i\n"
    "        return mw\n"
    "    app = Sanic(name)\n"
    "    for i in range(n):\n"
    "        app.register_named_middleware(make(i), ['route'], attach_to=kind)\n"
    "    if kind == 'response':\n"
    "        dq = app.named_response_middleware.get('route')\n"
    "    else:\n"
    "        dq = app.named_request_middleware.get('route')\n"
    "    return [m.idx for m in dq] if dq else []\n"
)


class Sanic1UnittestGenerator(SanicUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG1_HELPER_SRC).body

    def _make(self, kind: str, n: int, result: TestResult):
        expected = _bug1_expected(kind, n)
        name = f"t4p_b1_{kind}_{n}_{_rand_token()}"
        test = self.get_empty_test()
        body_src = (
            f"self.assertEqual({expected!r}, "
            f"run_named_middleware_order({name!r}, {kind!r}, {n}))"
        )
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("response", random.randint(2, 20), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        if random.random() < 0.7:
            return self._make("request", random.randint(2, 20), TestResult.PASSING)
        return self._make("response", random.randint(0, 1), TestResult.PASSING)


grammar_1: Grammar = {
    "<start>": ["<kind> <number>"],
    "<kind>": ["request", "response"],
    "<number>": ["<digit>", "<digit><number>"],
    "<digit>": srange(string.digits),
}

assert is_valid_grammar(grammar_1)


# ---------------------------------------------------------------------------
# Bug 3: Sanic.url_for did not split the host component off a route that was
# registered with an explicit ``host=`` (the host is stored as a prefix of the
# route's uri).  As a result ``url_for`` for such a route returned a malformed
# path (e.g. ``example.com/`` instead of ``/`` and ``http:///example.com``
# instead of ``http://example.com/``).  The fix splits the host off and uses it
# as the netloc.  The harness registers a route with an optional host and prints
# ``url_for``; a route WITH a host therefore FAILS on the buggy build while a
# host-less route behaves identically on both.
# ---------------------------------------------------------------------------


def _bug3_expected(mode: str, host: str, path: str) -> str:
    if host == "-":
        return path
    if mode == "ext":
        return "http://" + host + path
    return path


class Sanic3API(SanicAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            mode = process.args[2]
            host = process.args[3]
            path = process.args[4]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _bug3_expected(mode, host, path)
        result_line = None
        for line in process.stdout.decode("utf8").splitlines():
            if line.startswith("RESULT"):
                result_line = line[len("RESULT"):].strip()
                break
        if result_line is None:
            return TestResult.FAILING, "No RESULT produced"
        if result_line == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected!r}, but was {result_line!r}"


def _bug3_host() -> str:
    labels = [_rand_token(3, 8) for _ in range(random.randint(1, 3))]
    return ".".join(labels)


def _bug3_path() -> str:
    segs = [_rand_token(1, 6) for _ in range(random.randint(0, 3))]
    return "/" + "/".join(segs)


class Sanic3SystemtestGenerator(SanicSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(["ext", "noext"])
        return f"{mode} {_bug3_host()} {_bug3_path()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"noext - {_bug3_path()}", TestResult.PASSING


_BUG3_HELPER_SRC = (
    "import logging\n"
    "logging.disable(logging.CRITICAL)\n"
    "from sanic import Sanic\n"
    "\n"
    "def run_url_for(name, mode, host, path):\n"
    "    app = Sanic(name)\n"
    "    h = None if host == '-' else host\n"
    "    app.add_route(lambda request: None, path, name='r', host=h)\n"
    "    return app.url_for('r', _external=(mode == 'ext'))\n"
)


class Sanic3UnittestGenerator(SanicUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG3_HELPER_SRC).body

    def _make(self, mode: str, host: str, path: str, result: TestResult):
        expected = _bug3_expected(mode, host, path)
        name = f"t4p_b3_{_rand_token()}"
        test = self.get_empty_test()
        body_src = (
            f"self.assertEqual({expected!r}, "
            f"run_url_for({name!r}, {mode!r}, {host!r}, {path!r}))"
        )
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        mode = random.choice(["ext", "noext"])
        return self._make(mode, _bug3_host(), _bug3_path(), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("noext", "-", _bug3_path(), TestResult.PASSING)


grammar_3: Grammar = {
    "<start>": ["<mode> <hosttok> <path>"],
    "<mode>": ["ext", "noext"],
    "<hosttok>": ["-", "<domain>"],
    "<domain>": ["<label>", "<label>.<domain>"],
    "<label>": ["<lchar>", "<lchar><label>"],
    "<lchar>": srange(string.ascii_lowercase),
    "<path>": ["/<segs>"],
    "<segs>": ["", "<seg>", "<seg>/<segs>"],
    "<seg>": ["<lchar>", "<lchar><seg>"],
}

assert is_valid_grammar(grammar_3)


# ---------------------------------------------------------------------------
# Bug 5: sanic.log.LOGGING_CONFIG_DEFAULTS defined its root-level logger under
# the key ``"root"`` instead of ``"sanic.root"``.  Consequently sanic's default
# logging configuration never exposed a configurable ``sanic.root`` logger.
# The harness forces the real root logger to ``<base>`` and tries to set the
# ``sanic.root`` logger to ``<target>`` through the defaults; on the fixed build
# the effective level of ``sanic.root`` becomes ``<target>`` while on the buggy
# build it stays at the inherited ``<base>``.  A test with ``target != base``
# therefore FAILS on the buggy build.
# ---------------------------------------------------------------------------

_BUG5_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Sanic5API(SanicAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            target = process.args[3]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        result_line = None
        for line in process.stdout.decode("utf8").splitlines():
            if line.startswith("RESULT"):
                result_line = line[len("RESULT"):].strip()
                break
        if result_line is None:
            return TestResult.FAILING, "No RESULT produced"
        if result_line == target:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {target!r}, but was {result_line!r}"


class Sanic5SystemtestGenerator(SanicSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        base, target = random.sample(_BUG5_LEVELS, 2)
        return f"{base} {target} {_rand_token()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        level = random.choice(_BUG5_LEVELS)
        return f"{level} {level} {_rand_token()}", TestResult.PASSING


_BUG5_HELPER_SRC = (
    "import logging\n"
    "from sanic.log import LOGGING_CONFIG_DEFAULTS\n"
    "\n"
    "def run_sanic_root_level(name, base, target):\n"
    "    logging.getLogger().setLevel(base)\n"
    "    cfg = LOGGING_CONFIG_DEFAULTS\n"
    "    if 'sanic.root' in cfg['loggers']:\n"
    "        cfg['loggers']['sanic.root']['level'] = target\n"
    "    from sanic import Sanic\n"
    "    app = Sanic(name, log_config=cfg)\n"
    "    return logging.getLevelName("
    "logging.getLogger('sanic.root').getEffectiveLevel())\n"
)


class Sanic5UnittestGenerator(SanicUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG5_HELPER_SRC).body

    def _make(self, base: str, target: str, result: TestResult):
        name = f"t4p_b5_{_rand_token()}"
        test = self.get_empty_test()
        body_src = (
            f"self.assertEqual({target!r}, "
            f"run_sanic_root_level({name!r}, {base!r}, {target!r}))"
        )
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        base, target = random.sample(_BUG5_LEVELS, 2)
        return self._make(base, target, TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        level = random.choice(_BUG5_LEVELS)
        return self._make(level, level, TestResult.PASSING)


grammar_5: Grammar = {
    "<start>": ["<level> <level> <word>"],
    "<level>": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    "<word>": ["<lchar>", "<lchar><word>"],
    "<lchar>": srange(string.ascii_lowercase),
}

assert is_valid_grammar(grammar_5)


# ---------------------------------------------------------------------------
# Bug 4: Request.url_for accessed ``self.app.config.SERVER_NAME`` directly, so
# a request calling ``url_for`` while SERVER_NAME was not configured raised
# ``AttributeError`` (Config has no such attribute).  The fix wraps the access
# in ``try/except AttributeError``.  The harness builds a request against a
# route and calls ``url_for``; with SERVER_NAME unset the buggy build raises
# (RESULT ERR) while the fixed build returns a URL (RESULT OK).  With
# SERVER_NAME set both builds return a URL.
# ---------------------------------------------------------------------------


class Sanic4API(SanicAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        result_line = None
        for line in process.stdout.decode("utf8").splitlines():
            if line.startswith("RESULT"):
                result_line = line[len("RESULT"):].strip()
                break
        if result_line is None:
            return TestResult.FAILING, "No RESULT produced"
        if result_line.startswith("OK"):
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"url_for failed: {result_line}"


def _bug4_domain() -> str:
    labels = [_rand_token(3, 8) for _ in range(random.randint(1, 3))]
    return ".".join(labels)


def _bug4_hostport() -> str:
    return f"{_bug4_domain()}:{random.randint(1000, 60000)}"


def _bug4_path() -> str:
    segs = [_rand_token(1, 6) for _ in range(random.randint(1, 3))]
    return "/" + "/".join(segs)


class Sanic4SystemtestGenerator(SanicSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"- {_bug4_path()} {_bug4_hostport()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{_bug4_hostport()} {_bug4_path()} {_bug4_hostport()}",
            TestResult.PASSING,
        )


_BUG4_HELPER_SRC = (
    "import logging\n"
    "logging.disable(logging.CRITICAL)\n"
    "from sanic import Sanic\n"
    "from sanic.request import Request\n"
    "from sanic.compat import Header\n"
    "\n"
    "class _Transport:\n"
    "    def get_extra_info(self, key):\n"
    "        if key == 'sockname':\n"
    "            return ('127.0.0.1', 8000)\n"
    "        return None\n"
    "\n"
    "def run_request_url_for(name, server_name, path, host_header):\n"
    "    app = Sanic(name)\n"
    "    if server_name != '-':\n"
    "        app.config.SERVER_NAME = server_name\n"
    "    app.add_route(lambda request: None, path, name='target')\n"
    "    headers = Header()\n"
    "    headers['Host'] = host_header\n"
    "    req = Request(b'/sample', headers, '1.1', 'GET', _Transport(), app)\n"
    "    return req.url_for('target')\n"
)


class Sanic4UnittestGenerator(SanicUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG4_HELPER_SRC).body

    def _make(self, server_name: str, path: str, host: str, result: TestResult):
        name = f"t4p_b4_{_rand_token()}"
        test = self.get_empty_test()
        body_src = (
            "self.assertTrue("
            f"run_request_url_for({name!r}, {server_name!r}, {path!r}, {host!r})"
            ".startswith('http'))"
        )
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("-", _bug4_path(), _bug4_hostport(), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(
            _bug4_hostport(), _bug4_path(), _bug4_hostport(), TestResult.PASSING
        )


grammar_4: Grammar = {
    "<start>": ["<server> <path> <hostport>"],
    "<server>": ["-", "<hostport>"],
    "<hostport>": ["<domain>:<port>"],
    "<domain>": ["<label>", "<label>.<domain>"],
    "<label>": ["<lchar>", "<lchar><label>"],
    "<lchar>": srange(string.ascii_lowercase),
    "<port>": ["<digit>", "<digit><port>"],
    "<digit>": srange(string.digits),
    "<path>": ["/<segs>"],
    "<segs>": ["<seg>", "<seg>/<segs>"],
    "<seg>": ["<lchar>", "<lchar><seg>"],
}

assert is_valid_grammar(grammar_4)


# ---------------------------------------------------------------------------
# Bug 2: AsyncioServer lacked ``start_serving`` and ``serve_forever`` methods,
# so a user managing the server lifecycle manually could not start/serve it and
# calling those methods raised AttributeError.  The fix adds both methods, which
# delegate to the wrapped asyncio server.  The harness wraps a fake server and
# invokes the requested method: the missing methods (start_serving/serve_forever)
# FAIL on the buggy build while the pre-existing ones (is_serving/wait_closed)
# behave identically on both.
# ---------------------------------------------------------------------------

_BUG2_MISSING = ["start_serving", "serve_forever"]
_BUG2_PRESENT = ["is_serving", "wait_closed"]


class Sanic2API(SanicAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process = args
        try:
            method = process.args[2]
            token = process.args[3]
        except (IndexError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = f"{method}:{token}"
        result_line = None
        for line in process.stdout.decode("utf8").splitlines():
            if line.startswith("RESULT"):
                result_line = line[len("RESULT"):].strip()
                break
        if result_line is None:
            return TestResult.FAILING, "No RESULT produced"
        if result_line == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected!r}, but was {result_line!r}"


class Sanic2SystemtestGenerator(SanicSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        method = random.choice(_BUG2_MISSING)
        return f"{method} {_rand_token()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        method = random.choice(_BUG2_PRESENT)
        return f"{method} {_rand_token()}", TestResult.PASSING


_BUG2_HELPER_SRC = (
    "import logging\n"
    "logging.disable(logging.CRITICAL)\n"
    "from sanic.server import AsyncioServer\n"
    "\n"
    "class _FakeServer:\n"
    "    def __init__(self, token):\n"
    "        self.token = token\n"
    "    def start_serving(self):\n"
    "        return 'start_serving:' + self.token\n"
    "    def serve_forever(self):\n"
    "        return 'serve_forever:' + self.token\n"
    "    def is_serving(self):\n"
    "        return 'is_serving:' + self.token\n"
    "    def wait_closed(self):\n"
    "        return 'wait_closed:' + self.token\n"
    "\n"
    "def run_asyncio_server_method(method, token):\n"
    "    srv = AsyncioServer(None, None, set(), None, None, None)\n"
    "    srv.server = _FakeServer(token)\n"
    "    return getattr(srv, method)()\n"
)


class Sanic2UnittestGenerator(SanicUnittestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_BUG2_HELPER_SRC).body

    def _make(self, method: str, result: TestResult):
        token = _rand_token()
        expected = f"{method}:{token}"
        test = self.get_empty_test()
        body_src = (
            f"self.assertEqual({expected!r}, "
            f"run_asyncio_server_method({method!r}, {token!r}))"
        )
        test.body = ast.parse(body_src).body
        return test, result

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(random.choice(_BUG2_MISSING), TestResult.FAILING)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(random.choice(_BUG2_PRESENT), TestResult.PASSING)


grammar_2: Grammar = {
    "<start>": ["<method> <token>"],
    "<method>": ["start_serving", "serve_forever", "is_serving", "wait_closed"],
    "<token>": ["<lchar>", "<lchar><token>"],
    "<lchar>": srange(string.ascii_lowercase),
}

assert is_valid_grammar(grammar_2)
