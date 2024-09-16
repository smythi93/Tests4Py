import os.path
from pathlib import Path
from typing import List, Optional, Tuple

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
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
        python_version: Optional[str] = None,
        init: bool = False,
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
            grammar=None,
            loc=loc,
            source_base=Path(PROJECT_NAME),
            test_base=Path("tests"),
            included_files=[PROJECT_NAME],
            excluded_files=[
                os.path.join(PROJECT_NAME, "__init__.py" if init else "__version__.py")
            ],
            setup=[
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
        python_version="3.7.8",
        init=True,
        loc=3755,
    )


class SanicAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""
