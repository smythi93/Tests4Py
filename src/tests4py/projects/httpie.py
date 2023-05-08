from os import PathLike
from pathlib import Path
from typing import List, Optional

from tests4py.framework.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Httpie(Project):
    def __init__(
        self,
        bug_id: int,
        python_version: str,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_file: List[Path],
        test_cases: List[str],
        darwin_python_version: Optional[str] = None,
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="httpie",
            github_url="https://github.com/jakubroztocil/httpie/",
            status=Status.OK,
            cause="N.A.",
            python_version=python_version,
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version=darwin_python_version,
            python_fallback_version=darwin_python_version,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


def register():
    Httpie(
        bug_id=1,
        python_version="3.7.3",
        darwin_python_version="3.7.8",
        buggy_commit_id="001bda19450ad85c91345eea3cfa3991e1d492ba",
        fixed_commit_id="5300b0b490b8db48fac30b5e32164be93dc574b7",
        test_file=[
            Path("tests", "test_downloads.py"),
        ],
        test_cases=[
            "tests/test_downloads.py::TestDownloadUtils::test_unique_filename",
        ],
    )
    Httpie(
        bug_id=2,
        python_version="3.7.3",
        darwin_python_version="3.7.8",
        buggy_commit_id="356e0436510fee70b4071fac58be81c0a0a7db59",
        fixed_commit_id="e18b609ef7d867d6efa0efe42c832be5e0d09338",
        test_file=[
            Path("tests", "test_redirects.py"),
        ],
        test_cases=[
            "tests/test_redirects.py::TestRedirects::test_max_redirects",
        ],
    )
    Httpie(
        bug_id=3,
        python_version="3.7.3",
        darwin_python_version="3.7.8",
        buggy_commit_id="8c33e5e3d31d3cd6476c4d9bc963a4c529f883d2",
        fixed_commit_id="589887939507ff26d36ec74bd2c045819cfa3d56",
        test_file=[
            Path("tests", "test_sessions.py"),
        ],
        test_cases=[
            "tests/test_sessions.py::TestSession::test_download_in_session",
        ],
    )
    Httpie(
        bug_id=4,
        python_version="3.7.3",
        darwin_python_version="3.7.8",
        buggy_commit_id="8c892edd4fe700a7ca5cc733dcb4817831d253e2",
        fixed_commit_id="040d981f00c3f6830b2d0db3daf3c64c080e96e3",
        test_file=[
            Path("tests", "test_regressions.py"),
        ],
        test_cases=[
            "tests/test_regressions.py::test_Host_header_overwrite",
        ],
    )
    Httpie(
        bug_id=5,
        python_version="3.7.3",
        darwin_python_version="3.7.8",
        buggy_commit_id="16df8848e81eefac830f407e4b985f42b52970da",
        fixed_commit_id="90af1f742230831792d74d303d1e7ce56c96d4bd",
        test_file=[
            Path("tests", "tests.py"),
        ],
        test_cases=[
            "tests/tests.py::TestItemParsing::test_escape_longsep",
        ],
    )


class HttpieAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        return TestResult.UNDEFINED
