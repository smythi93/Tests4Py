import abc
from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Black(Project):
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
            project_name="black",
            github_url="https://github.com/psf/black",
            status=Status.OK,
            cause="N.A.",
            python_version=python_version,
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.UNITTEST,
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
    Black(
        bug_id=1,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="26c9465a22c732ab1e17b0dec578fa3432e9b558",
        fixed_commit_id="c0a7582e3d4cc8bec3b7f5a6c52b36880dcb57d7",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_works_in_mono_process_only_environment",
        ],
    )
    Black(
        bug_id=2,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="c8ca6b2b9ff3510bee12129824cebfc2fc51e5b2",
        fixed_commit_id="892eddacd215d685e136686b7f629ade70adca83",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_fmtonoff4",
        ],
    )
    Black(
        bug_id=3,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="8126b4f6a9342290de4655e6a8a78cd288ce7daa",
        fixed_commit_id="7a14a37981862ef418f3cdb4a7e2375856f97529",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_invalid_config_return_code",
        ],
    )
    Black(
        bug_id=4,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="65ea568e3301951f26e0e3b98f6d5dc80132e917",
        fixed_commit_id="c7495b9aa098ef7a358fc74556359d21c6a4ba11",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "beginning_backslash.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_beginning_backslash",
        ],
    )
    Black(
        bug_id=5,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="1bbb01b854d168d76ebe4bf78961c2152ae075d9",
        fixed_commit_id="9394de150ebf0adc426523f46dc08e8b2b2b0b63",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_function_trailing_comma",
        ],
    )
    Black(
        bug_id=6,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="8c8adedc2a74a494c24f93e405b6418ac32f54cd",
        fixed_commit_id="f8617f975d56e81cfb4070ce65584f7b29a77e7a",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comment_after_escaped_newline.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_async_as_identifier",
            "tests.test_black.BlackTestCase.test_python37",
        ],
    )
    Black(
        bug_id=7,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="18119d38466652ae818436cb497f601294ed4558",
        fixed_commit_id="de806405d2934b629d67e2a6317ad7e826765a20",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "tupleassign.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_tuple_assign",
        ],
    )
    Black(
        bug_id=8,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="e6ddb68c786256e1cb0c76b42d10c212ef34cb2a",
        fixed_commit_id="6b994fdb8ab70ce4c2eafb8f2f0ff2648f3ff1ef",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comments7.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_comments7",
        ],
    )
    Black(
        bug_id=9,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="026c81b83454f176a9f9253cbfb70be2c159d822",
        fixed_commit_id="d6db1c12a8e14833fe22da377cddc2bd1f43dc14",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "python2_print_function.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_python2_print_function",
        ],
    )
    Black(
        bug_id=10,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="f6643c4f0cfbae1f2493fdfce46cfbae3d26f46b",
        fixed_commit_id="66aa676278948368dff251dffd58c850cb8b889e",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_comment_indentation",
        ],
    )
    Black(
        bug_id=11,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="283a5d53a8d57e8e186a08c9fbf249e1fbe7bc94",
        fixed_commit_id="024c9cab55da7bd3236fd88759c9735d6149b464",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comments6.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_comments6",
        ],
    )
    Black(
        bug_id=12,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="8b340e210271a8108995fd479c55dbc0a34466bd",
        fixed_commit_id="b53cb9474348e13533ccba3735191a55ef3da6c4",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "bracketmatch.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_bracket_match",
        ],
    )
    Black(
        bug_id=13,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="b719d85ccc330170e40b2617307a7e3b2a0bab14",
        fixed_commit_id="883689366ce0f0e0ddd66d81360c61abfd19b01a",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "python37.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_python37",
        ],
    )
    Black(
        bug_id=14,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="3bdd42389128bbbe8b64a8e050563f09bff99979",
        fixed_commit_id="dd8bde6d2fbfe8a7a11093e761a0cb5837efa96a",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_get_future_imports",
        ],
    )
    Black(
        bug_id=15,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="8a8c58252cc023ae250d6febd24f50a8166450d4",
        fixed_commit_id="df2ae3bbe6c45298aabb6c04e85cb353205626f1",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "fmtonoff2.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_fmtonoff2",
        ],
    )
    Black(
        bug_id=16,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="fb34c9e19589d05f92084a28940837151251ebd6",
        fixed_commit_id="42a3fe53319a8c02858c2a96989ed1339f84515a",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_symlink_out_of_root_directory",
        ],
    )
    Black(
        bug_id=17,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="bbc09a4f013f2a584f143f3f5e3f76f6082367d4",
        fixed_commit_id="7fc6ce990669464f5172b63fafa3724f5f308be3",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_empty",
        ],
    )
    Black(
        bug_id=18,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="dbe26161fa68632d608a440666a0960a32630902",
        fixed_commit_id="00a302560b92951c22f0f4c8d618cf63de39bd57",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_preserves_line_endings",
        ],
    )
    Black(
        bug_id=19,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="337a4199f90ca48a19cf26511e0cec330b13bd4e",
        fixed_commit_id="29e97d1d4a7717f1bd0ca35cacf2f2ce6d815b0c",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comments6.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_comment_in_decorator",
        ],
    )
    Black(
        bug_id=20,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="2e52a2b3ecc0fe025439c3db05a4457ab14f167b",
        fixed_commit_id="06e95b1e9bcd43c4574840f8174ba4b2c5d281bd",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_expression_diff",
        ],
    )
    Black(
        bug_id=21,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="c071af761e1550c6e4ebab8e5af747d2d8fdd48e",
        fixed_commit_id="8e7848c63efe36f09e4651bece8c0efc34a1c3e1",
        test_file=[Path("tests", "test_black.py")],
        test_cases=[
            "tests.test_black.BlackTestCase.test_expression_ff",
        ],
    )
    Black(
        bug_id=22,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="728c56c986bc5aea4d9897d3fce3159f89991b8e",
        fixed_commit_id="c55d08d0b96c8de8bd867ca315e380d9e9d2d7ec",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "data", "comments3.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_comments3",
        ],
    )
    Black(
        bug_id=23,
        python_version="3.8.3",
        darwin_python_version="3.8.4",
        buggy_commit_id="8de552eb4f0fbf1ad84812cde71489cc00d3ed1f",
        fixed_commit_id="6316e293ac30a2837ec20eba289fd28a2a18cf89",
        test_file=[
            Path("tests", "test_black.py"),
            Path("tests", "python2.py"),
        ],
        test_cases=[
            "tests.test_black.BlackTestCase.test_python2",
        ],
    )


class BlackAPI(API, abc.ABC):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        return
