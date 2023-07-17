from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Tornado(Project):
    def __init__(
        self,
        bug_id: int,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_file: List[Path],
        test_cases: List[str],
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="tornado",
            github_url="https://github.com/tornadoweb/tornado",
            status=Status.OK,
            cause="N.A.",
            python_version="3.7.0",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version="3.7.8",
            python_fallback_version="3.7.8",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


def register():
    Tornado(
        bug_id=1,
        buggy_commit_id="6a5a0bfa370b6c0d3dbbf9589a560a98202d2baa",
        fixed_commit_id="4677c54cc18bbfbdf0f4dadf11610fab6203fd63",
        test_file=[Path("tornado", "test", "websocket_test.py")],
        test_cases=["tornado.test.websocket_test.WebSocketTest.test_nodelay"],
    )
    Tornado(
        bug_id=2,
        buggy_commit_id="2ca8821d006f6693f920a4b183a3a7c985a5c8ad",
        fixed_commit_id="4f486a4aec746e9d66441600ee3b0743228b061c",
        test_file=[Path("tornado", "test", "httpclient_test.py")],
        test_cases=[
            "tornado.test.httpclient_test.HTTPClientCommonTestCase.test_redirect_put_without_body"
        ],
    )
    Tornado(
        bug_id=3,
        buggy_commit_id="940fd87fe9145d1154c8457221f86d56ea063c65",
        fixed_commit_id="aa622e724f80e0f7fcee369f75d69d1db13d72f2",
        test_file=[Path("tornado", "test", "httpclient_test.py")],
        test_cases=["tornado.test.httpclient_test.SyncHTTPClientSubprocessTest"],
    )
    Tornado(
        bug_id=4,
        buggy_commit_id="a8420fc681c5423d072978f00eab4d0645057d16",
        fixed_commit_id="db529031a1e1a6e951826aba0b7d0b18f05cd4c7",
        test_file=[Path("tornado", "test", "web_test.py")],
        test_cases=[
            "tornado.test.web_test.StaticFileTest.test_static_with_range_neg_past_start",
            "tornado.test.web_test.StaticFileTest.test_static_unsatisfiable_range_end_less_than_start",
        ],
    )
    Tornado(
        bug_id=5,
        buggy_commit_id="2d4053daa56c609d642b214399e046671d4a593e",
        fixed_commit_id="886643965b5cb782503d8d7b374b7a794ec2077b",
        test_file=[Path("tornado", "test", "ioloop_test.py")],
        test_cases=[
            "tornado.test.ioloop_test.TestPeriodicCallbackMath.test_clock_backwards"
        ],
    )
    Tornado(
        bug_id=6,
        buggy_commit_id="fb74e4816ccfa7fc6a7abd8c8aab1f415cfc1b13",
        fixed_commit_id="2905ee4fb3c283d40b10f609359e189c83a0dc06",
        test_file=[Path("tornado", "test", "asyncio_test.py")],
        test_cases=[
            "tornado.test.asyncio_test.LeakTest.test_ioloop_close_leak",
            "tornado.test.asyncio_test.LeakTest.test_asyncio_close_leak",
        ],
    )
    Tornado(
        bug_id=7,
        buggy_commit_id="fa3409179588536f2f743d16e537f6f9827fa92f",
        fixed_commit_id="a3b44cd701e0e82693363701bc0346b0125d2362",
        test_file=[Path("tornado", "test", "ioloop_test.py")],
        test_cases=[
            "tornado.test.ioloop_test.TestIOLoopFutures.test_run_in_executor_native"
        ],
    )
    Tornado(
        bug_id=8,
        buggy_commit_id="34c43f4775971ab9b2b8ed43356f218add6387b2",
        fixed_commit_id="5d4a9ab26372efd255bbb29fde55c41395ed17b1",
        test_file=[Path("tornado", "test", "websocket_test.py")],
        test_cases=[
            "tornado.test.websocket_test.WebSocketTest.test_missing_websocket_key"
        ],
    )
    Tornado(
        bug_id=9,
        buggy_commit_id="c9d2a3fa573987629ad576e991c2f3b65f4daab4",
        fixed_commit_id="86cc31f52992fb9d11f92de6fd5496842fea2265",
        test_file=[Path("tornado", "test", "httputil_test.py")],
        test_cases=[
            "tornado.test.httputil_test.TestUrlConcat.test_url_concat_none_params"
        ],
    )
    Tornado(
        bug_id=10,
        buggy_commit_id="ecd8968c5135b810cd607b5902dda2cd32122b39",
        fixed_commit_id="5931d913b4ea250891a0b582f1f8b2901b868c79",
        test_file=[Path("tornado", "test", "websocket_test.py")],
        test_cases=["tornado.test.websocket_test.WebSocketTest.test_render_message"],
    )
    Tornado(
        bug_id=11,
        buggy_commit_id="79ef301eb05cac82c075198e502d94dad296f6aa",
        fixed_commit_id="1131c9b50a6a4c0868d0d6fa5e0be077cf8fd1ca",
        test_file=[Path("tornado", "test", "httpserver_test.py")],
        test_cases=[
            "tornado.test.httpserver_test.HTTPServerRawTest.test_chunked_request_uppercase"
        ],
    )
    Tornado(
        bug_id=12,
        buggy_commit_id="4ee9ba94de11aaa4f932560fa2b3d8ceb8c61d2a",
        fixed_commit_id="301f52b532c071a0d2fec1eb7c23f2714bb38567",
        test_file=[Path("tornado", "test", "auth_test.py")],
        test_cases=["tornado.test.auth_test.AuthTest.test_facebook_login"],
    )
    Tornado(
        bug_id=13,
        buggy_commit_id="d7d9c467cda38f4c9352172ba7411edc29a85196",
        fixed_commit_id="34903f9e1a99441b2729bbe6f1d65d46cf352ea7",
        test_file=[Path("tornado", "test", "http1connection_test.py")],
        test_cases=[
            "tornado.test.http1connection_test.HTTP1ConnectionTest.test_http10_no_content_length"
        ],
    )
    Tornado(
        bug_id=14,
        buggy_commit_id="81ee310adcd905fbdf7c98d9fb6ef0c5a46026c2",
        fixed_commit_id="1d02ed606f1c52636462633d009bdcbaac644331",
        test_file=[Path("tornado", "test", "ioloop_test.py")],
        test_cases=["tornado.test.ioloop_test.TestIOLoopCurrent.test_force_current"],
    )
    Tornado(
        bug_id=15,
        buggy_commit_id="fdfaf3dffa49479c7461050eacca07bc5ee8d207",
        fixed_commit_id="ecb3ea7543cc942659faf3d2144853018afa6139",
        test_file=[Path("tornado", "test", "web_test.py")],
        test_cases=[
            "tornado.test.web_test.StaticFileTest.test_path_traversal_protection"
        ],
    )
    Tornado(
        bug_id=16,
        buggy_commit_id="b450ff270df0395ee80f4ee5896a92bfe7f9b6ae",
        fixed_commit_id="d1676810ef5972c4defb0a710a1d8f8a0018983b",
        test_file=[Path("tornado", "test", "gen_test.py")],
        test_cases=["tornado.test.gen_test.WaitIteratorTest.test_no_ref"],
    )


class TornadoAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
