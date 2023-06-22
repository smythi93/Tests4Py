from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class TheFuck(Project):
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
            project_name="thefuck",
            github_url="https://github.com/nvbn/thefuck",
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
    TheFuck(
        bug_id=1,
        buggy_commit_id="2ced7a7f33ae0bec3ffc7a43ce95330bdf6cfcb9",
        fixed_commit_id="444908ce1c17767ef4aaf9e0b4950497914f7f63",
        test_file=[Path("tests", "rules", "test_pip_unknown_command.py")],
        test_cases=["tests/rules/test_pip_unknown_command.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=2,
        buggy_commit_id="40ab4eb62db57627bff10cf029d29c94704086a2",
        fixed_commit_id="78ef9eec88f43d5727986be2237f6e0e250cbbbc",
        test_file=[Path("tests", "test_utils.py")],
        test_cases=["tests/test_utils.py::test_get_all_executables_pathsep"],
    )
    TheFuck(
        bug_id=3,
        buggy_commit_id="ac343fb1bd7dadbb9e1a9fd7e3071f5778e338a4",
        fixed_commit_id="ce5feaebf7fd5c1190b5e14fbc1e962cc8db5f39",
        test_file=[Path("tests", "shells", "test_fish.py")],
        test_cases=["tests/shells/test_fish.py::TestFish::test_info"],
    )
    TheFuck(
        bug_id=4,
        buggy_commit_id="68949a592248913b52bfd50036893553153fcddb",
        fixed_commit_id="8db3cf604865e559090412ce80b0640e290ad83a",
        test_file=[Path("tests", "shells", "test_fish.py")],
        test_cases=["tests/shells/test_fish.py::TestFish::test_get_aliases"],
    )
    TheFuck(
        bug_id=5,
        buggy_commit_id="7c858fadb3458be829d3d43666ccb46c3ed5b8a0",
        fixed_commit_id="c205683a8df8a57e2db1e9816a5a7ce3255b08fc",
        test_file=[Path("tests", "rules", "test_git_push.py")],
        test_cases=["tests/rules/test_git_push.py::test_match_bitbucket"],
    )
    TheFuck(
        bug_id=6,
        buggy_commit_id="797ca1c5647c565f62e21a8e29515c8b0fbe275f",
        fixed_commit_id="7c858fadb3458be829d3d43666ccb46c3ed5b8a0",
        test_file=[Path("tests", "rules", "test_git_branch_exists.py")],
        test_cases=["tests/rules/test_git_branch_exists.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=7,
        buggy_commit_id="64d6835e15a22cf8803d398cbb593f748c550e8a",
        fixed_commit_id="75d2c43997ca703150cbdb4c46ed7b2e2e71fd11",
        test_file=[Path("tests", "rules", "test_php_s.py")],
        test_cases=["tests/rules/test_php_s.py::test_match"],
    )
    TheFuck(
        bug_id=8,
        buggy_commit_id="449cb9a00693c8b4d97d5fda8d732cf0978e117e",
        fixed_commit_id="be48f027847161f907def8987706041c65a1fd58",
        test_file=[Path("tests", "rules", "test_dnf_no_such_command.py")],
        test_cases=[
            "tests/rules/test_dnf_no_such_command.py::test_get_new_command",
            "tests/rules/test_dnf_no_such_command.py::test_get_operations",
        ],
    )
    TheFuck(
        bug_id=9,
        buggy_commit_id="ce6b82c92d78ae283cb3db001766b76f6647bc47",
        fixed_commit_id="feb36ede5c518fdc3b6eddf945b2d8b1e2294d15",
        test_file=[Path("tests", "rules", "test_git_push.py")],
        test_cases=["tests/rules/test_git_push.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=10,
        buggy_commit_id="8bd6c5da67e55c64257345efa4e3cc454c42475c",
        fixed_commit_id="0c84eefa55fc1b4bc4940b41d74568884344e35c",
        test_file=[Path("tests", "rules", "test_man.py")],
        test_cases=["tests/rules/test_man.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=11,
        buggy_commit_id="92f3c8fb52b32b79005b4864c31a5c2d8c45f4b1",
        fixed_commit_id="db7dffdb44ae5c7be8de088765463fbda96197d1",
        test_file=[Path("tests", "rules", "test_git_push.py")],
        test_cases=["tests/rules/test_git_push.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=12,
        buggy_commit_id="4c2fc490f280ca3921785d8f58a37274ced35ce6",
        fixed_commit_id="ca787a1cba3cc9b26b43919c5e60acb40ebcd919",
        test_file=[Path("tests", "rules", "test_no_command.py")],
        test_cases=[
            "tests/rules/test_no_command.py::test_not_match",
            "tests/rules/test_no_command.py::test_match",
        ],
    )
    TheFuck(
        bug_id=13,
        buggy_commit_id="2af65071d84a7d1d14a4126364d9b4c9b5241f3c",
        fixed_commit_id="237bc579994de633fe104714156ddfa925a50b6e",
        test_file=[Path("tests", "rules", "test_git_branch_exists.py")],
        test_cases=[
            "tests/rules/test_git_branch_exists.py::test_match",
            "tests/rules/test_git_branch_exists.py::test_get_new_command",
        ],
    )
    TheFuck(
        bug_id=14,
        buggy_commit_id="183b70c8b8885843efefd2bd4e74dc0a7d42d173",
        fixed_commit_id="db6053b301e2b3f4363401e457b5dc4ad2e8429b",
        test_file=[Path("tests", "shells", "test_fish.py")],
        test_cases=["tests/shells/test_fish.py::TestFish::test_get_overridden_aliases"],
    )
    TheFuck(
        bug_id=15,
        buggy_commit_id="3a39deb485995e67afb1919972cd1c9aaedf4c32",
        fixed_commit_id="41707b80c61acadb7c87b0efcbf10f4186dc5937",
        test_file=[Path("tests", "rules", "test_git_add.py")],
        test_cases=["tests/rules/test_git_add.py::test_match"],
    )
    TheFuck(
        bug_id=16,
        buggy_commit_id="d92765d5df6607cb2f2fb67cee7b63f64ac7aa6b",
        fixed_commit_id="bb5f6bb705a3b217eb682f3357ec6bbb709555c1",
        test_file=[
            Path("tests", "shells", "test_bash.py"),
            Path("tests", "shells", "test_zsh.py"),
        ],
        test_cases=[
            "tests/shells/test_bash.py::TestBash::test_app_alias_variables_correctly_set",
            "tests/shells/test_zsh.py::TestZsh::test_app_alias_variables_correctly_set",
        ],
    )
    TheFuck(
        bug_id=17,
        buggy_commit_id="f7f0660114a02fe49578ec5684dd02c81042d175",
        fixed_commit_id="7ce4307c87c1e2e4106db2c961e48e249be987be",
        test_file=[Path("tests", "shells", "test_bash.py")],
        test_cases=[
            "tests/shells/test_bash.py::TestBash::test_get_aliases",
            "tests/shells/test_bash.py::TestBash::test_from_shell",
        ],
    )
    TheFuck(
        bug_id=18,
        buggy_commit_id="b65a9a0a4fd9bef394b45a1d367d29aa1e1c403e",
        fixed_commit_id="c3b1ba763708b8faaaf55717c436c4cd4c57a7ea",
        test_file=[Path("tests", "rules", "test_sudo.py")],
        test_cases=["tests/rules/test_sudo.py::test_not_match"],
    )
    TheFuck(
        bug_id=19,
        buggy_commit_id="959b96cf6ec8cedda05dc58efe0e0f3bd6ed2f4e",
        fixed_commit_id="dc23d67a42dad54308a753639edd1ea0d15cb2e7",
        test_file=[Path("tests", "rules", "test_git_push_force.py")],
        test_cases=["tests/rules/test_git_push_force.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=20,
        buggy_commit_id="0a6a3db65d2fc480c5b2f1135137f34c9f06b742",
        fixed_commit_id="280751b36e715b006c631ba6c08de99ccc74f6d2",
        test_file=[Path("tests", "rules", "test_dirty_unzip.py")],
        test_cases=["tests/rules/test_dirty_unzip.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=21,
        buggy_commit_id="71dc2666ccf62e653291d9a7a08e2c6c3320425b",
        fixed_commit_id="213791d3c2af379ffa37a140735998736b41912e",
        test_file=[Path("tests", "rules", "test_git_fix_stash.py")],
        test_cases=["tests/rules/test_git_fix_stash.py::test_not_match"],
    )
    TheFuck(
        bug_id=22,
        buggy_commit_id="faa7ee603057fa98c25507d30180c055d10d13d4",
        fixed_commit_id="e2e8b6fc865452b4cfc1bed70e5b9b49807258ae",
        test_file=[Path("tests", "test_types.py")],
        test_cases=[
            "tests/test_types.py::TestSortedCorrectedCommandsSequence::test_with_blank"
        ],
    )
    TheFuck(
        bug_id=23,
        buggy_commit_id="4129ff2717cc6e6fa51d70cc4e6c31d56ef8e2c9",
        fixed_commit_id="9a02e821cdc58a4aba2c0acc521fb25cacab87a5",
        test_file=[Path("tests", "test_utils.py")],
        test_cases=[
            "tests/test_utils.py::TestCache::test_when_etag_changed",
            "tests/test_utils.py::TestCache::test_with_filled_cache",
            "tests/test_utils.py::TestCache::test_with_blank_cache",
        ],
    )
    TheFuck(
        bug_id=24,
        buggy_commit_id="12394ca8423a438915fed996383b44471fc1139d",
        fixed_commit_id="5d74344994da89ed01afd448f1c9d86b85e85351",
        test_file=[Path("tests", "test_types.py")],
        test_cases=[
            "tests/test_types.py::TestCorrectedCommand::test_equality",
            "tests/test_types.py::TestCorrectedCommand::test_hashable",
        ],
    )
    TheFuck(
        bug_id=25,
        buggy_commit_id="42a8b4f639269886e468762e6d100b6f01aad8ab",
        fixed_commit_id="298c04f89c081dc16c8653aa017ca85dd14bfad6",
        test_file=[Path("tests", "rules", "test_mkdir_p.py")],
        test_cases=["tests/rules/test_mkdir_p.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=26,
        buggy_commit_id="7cb0388ed0845545e878b29783bbf8e901a02745",
        fixed_commit_id="feb3eee2a08f0cba4552373d728509bc90b561ab",
        test_file=[Path("tests", "rules", "test_vagrant_up.py")],
        test_cases=["tests/rules/test_vagrant_up.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=27,
        buggy_commit_id="bc6b107066d3f1e60b4cfcaa8cf6399e98cf1b1c",
        fixed_commit_id="1becd92b126a368d6e7d93aa8eea209414ce4aa2",
        test_file=[Path("tests", "rules", "test_open.py")],
        test_cases=["tests/rules/test_open.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=28,
        buggy_commit_id="88831c424f569e6a55fc98883d3eeecc7d425b18",
        fixed_commit_id="9b30ae0424607a4e268bd26eaee8ccb91a5588f9",
        test_file=[Path("tests", "rules", "test_fix_file.py")],
        test_cases=["tests/rules/test_fix_file.py::test_get_new_command_with_settings"],
    )
    TheFuck(
        bug_id=29,
        buggy_commit_id="4a2f869c6d6ef03d8d7ada1121cc6631d7ef979e",
        fixed_commit_id="88831c424f569e6a55fc98883d3eeecc7d425b18",
        test_file=[Path("tests", "test_types.py"), Path("tests", "test_utils.py")],
        test_cases=[
            "tests/test_types.py::test_update_settings",
            "tests/test_utils.py::test_wrap_settings",
        ],
    )
    TheFuck(
        bug_id=30,
        buggy_commit_id="de513cacb150049e3f95434f8d6d30b7ed1e0ea7",
        fixed_commit_id="43fead02d3a24fef71534116c5550def0f56830c",
        test_file=[Path("tests", "rules", "test_fix_file.py")],
        test_cases=["tests/rules/test_fix_file.py::test_not_file"],
    )
    TheFuck(
        bug_id=31,
        buggy_commit_id="66e2ec7e3f0d3f848c01d87bb3503b0ff90fc78a",
        fixed_commit_id="1285303363bc420bd7606bd5f808e3f2b4f0e83f",
        test_file=[Path("tests", "rules", "test_git_diff_staged.py")],
        test_cases=["tests/rules/test_git_diff_staged.py::test_get_new_command"],
    )
    TheFuck(
        bug_id=32,
        buggy_commit_id="cb33c912e5f2f4c2da6b70d708ff0437bfcd3b94",
        fixed_commit_id="25cc98a21a3450a046caf418f08713c82a290805",
        test_file=[Path("tests", "rules", "test_ls_lah.py")],
        test_cases=["tests/rules/test_ls_lah.py::test_match"],
    )


class TheFuckAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
