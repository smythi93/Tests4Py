import os
from pathlib import Path
from typing import List, Optional, Tuple

from tests4py.constants import PYTHON
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
            grammar=None,
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
        loc=10796,
    )


class TornadoAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""
