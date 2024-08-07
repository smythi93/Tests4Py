import abc
import os
import string
from pathlib import Path
from typing import List, Optional, Tuple

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
            api=HttpieAPI(),
            grammar=grammar_request,
            source_base=Path(PROJECT_NAME),
            test_base=test_base or Path("tests"),
            loc=loc,
            setup=[[PYTHON, "-m", "pip", "install", "-e", "."]],
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
        # systemtests=Httpie1SystemtestGenerator(),
        # unittests=Httpie1UnittestGenerator(),
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
        # systemtests=Httpie2SystemtestGenerator(),
        # unittests=Httpie2UnittestGenerator(),
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
        # systemtests=Httpie3SystemtestGenerator(),
        # unittests=Httpie3UnittestGenerator(),
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
        # systemtests=Httpie4SystemtestGenerator(),
        # unittests=Httpie4UnittestGenerator(),
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
        # systemtests=Httpie5SystemtestGenerator(),
        # unittests=Httpie5UnittestGenerator(),
        loc=509,
    )


class HttpieAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


class HttpieSystemtestGenerator(SystemtestGenerator, abc.ABC):
    pass


class Httpie1SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie2SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie3SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie4SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie5SystemtestGenerator(HttpieSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class HttpieUnittestGenerator(UnittestGenerator, abc.ABC):
    pass


class Httpie1UnittestGenerator(HttpieUnittestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie2UnittestGenerator(HttpieUnittestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie3UnittestGenerator(HttpieUnittestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie4UnittestGenerator(HttpieUnittestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class Httpie5UnittestGenerator(HttpieUnittestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


grammar_request: Grammar = {
    "<start>": ["<options>"],
    "<options>": ["", "<option_list>"],
    "<option_list>": ["<option>", "<option_list>\n<option>"],
    "<option>": [
        "<url>",
        "<mode>",
        "<data>",
        "<alias>",
        "<override>",
        "<users>",
    ],
    # OPTIONS
    "<url>": ["-p<path>"],
    "<mode>": ["-m<r_mode>"],
    "<data>": ["-d<json>"],
    "<alias>": ["-a"],
    "<override>": ["-o"],
    "<users>": ["-u"],
    # UTILS
    "<path>": ["/<chars>", "/<chars>/", "/<chars><path>"],
    "<r_mode>": ["get", "post", "websocket"],
    "<json>": ["<json_object>", "<json_list>", "<json_value>"],
    "<json_object>": ["{}", "{<pairs>}"],
    "<pairs>": ["<pair>", "<pairs>,<pair>"],
    "<pair>": ["<key>:<json_value>"],
    "<json_list>": ["[]", "[<json_values>]"],
    "<json_values>": ["<json_value>", "<json_values>,<json_value>"],
    "<json_value>": ["<number>", "<str>", "<json_object>", "<json_list>"],
    "<key>": ["<str>"],
    "<str>": ['""', '"<chars>"'],
    "<chars>": ["<char>", "<chars><char>"],
    "<char>": srange(string.ascii_letters + string.digits + "_-. "),
    "<number>": ["<int>", "<float>"],
    "<int>": ["<nonzero><digits>", "-<nonzero><digits>", "0", "-0"],
    "<digit>": srange(string.digits),
    "<digits>": ["", "<digits><digit>"],
    "<nonzero>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<float>": ["<int>.<digit><digits>"],
}

assert is_valid_grammar(grammar_request)
