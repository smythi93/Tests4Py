import ast
import random
import string
import subprocess
import os
from _ast import Call, ImportFrom, Assign, Expr
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable
from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.grammars import python
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_MAME = "thefuck"


class TheFuck(Project):
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
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_MAME,
            github_url="https://github.com/nvbn/thefuck",
            status=Status.OK,
            python_version="3.7.0",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version="3.7.8",
            python_fallback_version="3.7.8",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
            loc=loc,
            relevant_test_files=relevant_test_files,
        )


def register():
    TheFuck(
        bug_id=1,
        buggy_commit_id="2ced7a7f33ae0bec3ffc7a43ce95330bdf6cfcb9",
        fixed_commit_id="444908ce1c17767ef4aaf9e0b4950497914f7f63",
        test_files=[Path("tests", "rules", "test_pip_unknown_command.py")],
        test_cases=["tests/rules/test_pip_unknown_command.py::test_get_new_command"],
        api=TheFuckAPI1(),
        unittests=TheFuckUnittestGenerator1(),
        systemtests=TheFuckSystemtestGenerator1(),
    )
    TheFuck(
        bug_id=2,
        buggy_commit_id="40ab4eb62db57627bff10cf029d29c94704086a2",
        fixed_commit_id="78ef9eec88f43d5727986be2237f6e0e250cbbbc",
        test_files=[Path("tests", "test_utils.py")],
        test_cases=["tests/test_utils.py::test_get_all_executables_pathsep"],
        api=TheFuckAPI2(),
        unittests=TheFuckUnittestGenerator2(),
        systemtests=TheFuckSystemtestGenerator2(),
    )
    TheFuck(
        bug_id=3,
        buggy_commit_id="ac343fb1bd7dadbb9e1a9fd7e3071f5778e338a4",
        fixed_commit_id="ce5feaebf7fd5c1190b5e14fbc1e962cc8db5f39",
        test_files=[Path("tests", "shells", "test_fish.py")],
        test_cases=["tests/shells/test_fish.py::TestFish::test_info"],
        api=TheFuckAPI3(),
        unittests=TheFuckUnittestGenerator3(),
        systemtests=TheFuckSystemtestGenerator3(),
    )
    TheFuck(
        bug_id=4,
        buggy_commit_id="68949a592248913b52bfd50036893553153fcddb",
        fixed_commit_id="8db3cf604865e559090412ce80b0640e290ad83a",
        test_files=[Path("tests", "shells", "test_fish.py")],
        test_cases=["tests/shells/test_fish.py::TestFish::test_get_aliases"],
        api=TheFuckAPI4(),
        unittests=TheFuckUnittestGenerator4(),
        systemtests=TheFuckSystemtestGenerator4(),
    )
    TheFuck(
        bug_id=5,
        buggy_commit_id="7c858fadb3458be829d3d43666ccb46c3ed5b8a0",
        fixed_commit_id="c205683a8df8a57e2db1e9816a5a7ce3255b08fc",
        test_files=[Path("tests", "rules", "test_git_push.py")],
        test_cases=["tests/rules/test_git_push.py::test_match_bitbucket"],
        api=TheFuckAPI5(),
        unittests=TheFuckUnittestGenerator5(),
        systemtests=TheFuckSystemtestGenerator5(),
    )
    TheFuck(
        bug_id=6,
        buggy_commit_id="797ca1c5647c565f62e21a8e29515c8b0fbe275f",
        fixed_commit_id="7c858fadb3458be829d3d43666ccb46c3ed5b8a0",
        test_files=[Path("tests", "rules", "test_git_branch_exists.py")],
        test_cases=["tests/rules/test_git_branch_exists.py::test_get_new_command"],
        api=TheFuckAPI6(),
        unittests=TheFuckUnittestGenerator6(),
        systemtests=TheFuckSystemtestGenerator6(),
    )
    TheFuck(
        bug_id=7,
        buggy_commit_id="64d6835e15a22cf8803d398cbb593f748c550e8a",
        fixed_commit_id="75d2c43997ca703150cbdb4c46ed7b2e2e71fd11",
        test_files=[Path("tests", "rules", "test_php_s.py")],
        test_cases=["tests/rules/test_php_s.py::test_match"],
        api=TheFuckAPI7(),
        unittests=TheFuckUnittestGenerator7(),
        systemtests=TheFuckSystemtestGenerator7(),
    )
    TheFuck(
        bug_id=8,
        buggy_commit_id="449cb9a00693c8b4d97d5fda8d732cf0978e117e",
        fixed_commit_id="be48f027847161f907def8987706041c65a1fd58",
        test_files=[Path("tests", "rules", "test_dnf_no_such_command.py")],
        test_cases=[
            "tests/rules/test_dnf_no_such_command.py::test_get_new_command",
            "tests/rules/test_dnf_no_such_command.py::test_get_operations",
        ],
        api=TheFuckAPI8(),
        unittests=TheFuckUnittestGenerator8(),
        systemtests=TheFuckSystemtestGenerator8(),
    )
    TheFuck(
        bug_id=9,
        buggy_commit_id="ce6b82c92d78ae283cb3db001766b76f6647bc47",
        fixed_commit_id="feb36ede5c518fdc3b6eddf945b2d8b1e2294d15",
        test_files=[Path("tests", "rules", "test_git_push.py")],
        test_cases=["tests/rules/test_git_push.py::test_get_new_command"],
        api=TheFuckAPI9(),
        unittests=TheFuckUnittestGenerator9(),
        systemtests=TheFuckSystemtestGenerator9(),
    )
    TheFuck(
        bug_id=10,
        buggy_commit_id="8bd6c5da67e55c64257345efa4e3cc454c42475c",
        fixed_commit_id="0c84eefa55fc1b4bc4940b41d74568884344e35c",
        test_files=[Path("tests", "rules", "test_man.py")],
        test_cases=["tests/rules/test_man.py::test_get_new_command"],
        api=TheFuckAPI10(),
        unittests=TheFuckUnittestGenerator10(),
        systemtests=TheFuckSystemtestGenerator10(),
    )
    TheFuck(
        bug_id=11,
        buggy_commit_id="92f3c8fb52b32b79005b4864c31a5c2d8c45f4b1",
        fixed_commit_id="db7dffdb44ae5c7be8de088765463fbda96197d1",
        test_files=[Path("tests", "rules", "test_git_push.py")],
        test_cases=["tests/rules/test_git_push.py::test_get_new_command"],
        api=TheFuckAPI11(),
        unittests=TheFuckUnittestGenerator11(),
        systemtests=TheFuckSystemtestGenerator11(),
    )
    TheFuck(
        bug_id=12,
        buggy_commit_id="4c2fc490f280ca3921785d8f58a37274ced35ce6",
        fixed_commit_id="ca787a1cba3cc9b26b43919c5e60acb40ebcd919",
        test_files=[Path("tests", "rules", "test_no_command.py")],
        test_cases=[
            "tests/rules/test_no_command.py::test_not_match",
            "tests/rules/test_no_command.py::test_match",
        ],
        api=TheFuckAPI12(),
        unittests=TheFuckUnittestGenerator12(),
        systemtests=TheFuckSystemtestGenerator12(),
    )
    TheFuck(
        bug_id=13,
        buggy_commit_id="2af65071d84a7d1d14a4126364d9b4c9b5241f3c",
        fixed_commit_id="237bc579994de633fe104714156ddfa925a50b6e",
        test_files=[Path("tests", "rules", "test_git_branch_exists.py")],
        test_cases=[
            "tests/rules/test_git_branch_exists.py::test_match",
            "tests/rules/test_git_branch_exists.py::test_get_new_command",
        ],
        api=TheFuckAPI13(),
        unittests=TheFuckUnittestGenerator13(),
        systemtests=TheFuckSystemtestGenerator13(),
    )
    TheFuck(
        bug_id=14,
        buggy_commit_id="183b70c8b8885843efefd2bd4e74dc0a7d42d173",
        fixed_commit_id="db6053b301e2b3f4363401e457b5dc4ad2e8429b",
        test_files=[Path("tests", "shells", "test_fish.py")],
        test_cases=["tests/shells/test_fish.py::TestFish::test_get_overridden_aliases"],
        api=TheFuckAPI14(),
        unittests=TheFuckUnittestGenerator14(),
        systemtests=TheFuckSystemtestGenerator14(),
    )
    TheFuck(
        bug_id=15,
        buggy_commit_id="3a39deb485995e67afb1919972cd1c9aaedf4c32",
        fixed_commit_id="41707b80c61acadb7c87b0efcbf10f4186dc5937",
        test_files=[Path("tests", "rules", "test_git_add.py")],
        test_cases=["tests/rules/test_git_add.py::test_match"],
        api=TheFuckAPI15(),
        unittests=TheFuckUnittestGenerator15(),
        systemtests=TheFuckSystemtestGenerator15(),
    )
    TheFuck(
        bug_id=16,
        buggy_commit_id="d92765d5df6607cb2f2fb67cee7b63f64ac7aa6b",
        fixed_commit_id="bb5f6bb705a3b217eb682f3357ec6bbb709555c1",
        test_files=[
            Path("tests", "shells", "test_bash.py"),
            Path("tests", "shells", "test_zsh.py"),
        ],
        test_cases=[
            "tests/shells/test_bash.py::TestBash::test_app_alias_variables_correctly_set",
            "tests/shells/test_zsh.py::TestZsh::test_app_alias_variables_correctly_set",
        ],
        api=TheFuckAPI16(),
        unittests=TheFuckUnittestGenerator16(),
        systemtests=TheFuckSystemtestGenerator16(),
    )
    TheFuck(
        bug_id=17,
        buggy_commit_id="f7f0660114a02fe49578ec5684dd02c81042d175",
        fixed_commit_id="7ce4307c87c1e2e4106db2c961e48e249be987be",
        test_files=[Path("tests", "shells", "test_bash.py")],
        test_cases=[
            "tests/shells/test_bash.py::TestBash::test_get_aliases",
            "tests/shells/test_bash.py::TestBash::test_from_shell",
        ],
        api=TheFuckAPI17(),
        unittests=TheFuckUnittestGenerator17(),
        systemtests=TheFuckSystemtestGenerator17(),
    )
    TheFuck(
        bug_id=18,
        buggy_commit_id="b65a9a0a4fd9bef394b45a1d367d29aa1e1c403e",
        fixed_commit_id="c3b1ba763708b8faaaf55717c436c4cd4c57a7ea",
        test_files=[Path("tests", "rules", "test_sudo.py")],
        test_cases=["tests/rules/test_sudo.py::test_not_match"],
        api=TheFuckAPI18(),
        unittests=TheFuckUnittestGenerator18(),
        systemtests=TheFuckSystemtestGenerator18(),

    )
    TheFuck(
        bug_id=19,
        buggy_commit_id="959b96cf6ec8cedda05dc58efe0e0f3bd6ed2f4e",
        fixed_commit_id="dc23d67a42dad54308a753639edd1ea0d15cb2e7",
        test_files=[Path("tests", "rules", "test_git_push_force.py")],
        test_cases=["tests/rules/test_git_push_force.py::test_get_new_command"],
        api=TheFuckAPI19(),
        unittests=TheFuckUnittestGenerator19(),
        systemtests=TheFuckSystemtestGenerator19(),
    )
    TheFuck(
        bug_id=20,
        buggy_commit_id="0a6a3db65d2fc480c5b2f1135137f34c9f06b742",
        fixed_commit_id="280751b36e715b006c631ba6c08de99ccc74f6d2",
        test_files=[Path("tests", "rules", "test_dirty_unzip.py")],
        test_cases=["tests/rules/test_dirty_unzip.py::test_get_new_command"],
        api=TheFuckAPI20(),
        unittests=TheFuckUnittestGenerator20(),
        systemtests=TheFuckSystemtestGenerator20(),
    )
    TheFuck(
        bug_id=21,
        buggy_commit_id="71dc2666ccf62e653291d9a7a08e2c6c3320425b",
        fixed_commit_id="213791d3c2af379ffa37a140735998736b41912e",
        test_files=[Path("tests", "rules", "test_git_fix_stash.py")],
        test_cases=["tests/rules/test_git_fix_stash.py::test_not_match"],
        api=TheFuckAPI21(),
        unittests=TheFuckUnittestGenerator21(),
        systemtests=TheFuckSystemtestGenerator21(),
    )
    TheFuck(
        bug_id=22,
        buggy_commit_id="faa7ee603057fa98c25507d30180c055d10d13d4",
        fixed_commit_id="e2e8b6fc865452b4cfc1bed70e5b9b49807258ae",
        test_files=[Path("tests", "test_types.py")],
        test_cases=[
            "tests/test_types.py::TestSortedCorrectedCommandsSequence::test_with_blank"
        ],
        api=TheFuckAPI22(),
        unittests=TheFuckUnittestGenerator22(),
        systemtests=TheFuckSystemtestGenerator22(),
    )
    TheFuck(
        bug_id=23,
        buggy_commit_id="4129ff2717cc6e6fa51d70cc4e6c31d56ef8e2c9",
        fixed_commit_id="9a02e821cdc58a4aba2c0acc521fb25cacab87a5",
        test_files=[Path("tests", "test_utils.py")],
        test_cases=[
            "tests/test_utils.py::TestCache::test_when_etag_changed",
            "tests/test_utils.py::TestCache::test_with_filled_cache",
            "tests/test_utils.py::TestCache::test_with_blank_cache",
        ],
        api=TheFuckAPI23(),
        unittests=TheFuckUnittestGenerator23(),
        systemtests=TheFuckSystemtestGenerator23(),
    )
    TheFuck(
        bug_id=24,
        buggy_commit_id="12394ca8423a438915fed996383b44471fc1139d",
        fixed_commit_id="5d74344994da89ed01afd448f1c9d86b85e85351",
        test_files=[Path("tests", "test_types.py")],
        test_cases=[
            "tests/test_types.py::TestCorrectedCommand::test_equality",
            "tests/test_types.py::TestCorrectedCommand::test_hashable",
        ],
        api=TheFuckAPI24(),
        unittests=TheFuckUnittestGenerator24(),
        systemtests=TheFuckSystemtestGenerator24(),
    )
    TheFuck(
        bug_id=25,
        buggy_commit_id="42a8b4f639269886e468762e6d100b6f01aad8ab",
        fixed_commit_id="298c04f89c081dc16c8653aa017ca85dd14bfad6",
        test_files=[Path("tests", "rules", "test_mkdir_p.py")],
        test_cases=["tests/rules/test_mkdir_p.py::test_get_new_command"],
        api=TheFuckAPI25(),
        unittests=TheFuckUnittestGenerator25(),
        systemtests=TheFuckSystemtestGenerator25(),
    )
    TheFuck(
        bug_id=26,
        buggy_commit_id="7cb0388ed0845545e878b29783bbf8e901a02745",
        fixed_commit_id="feb3eee2a08f0cba4552373d728509bc90b561ab",
        test_files=[Path("tests", "rules", "test_vagrant_up.py")],
        test_cases=["tests/rules/test_vagrant_up.py::test_get_new_command"],
        api=TheFuckAPI26(),
        unittests=TheFuckUnittestGenerator26(),
        systemtests=TheFuckSystemtestGenerator26(),
    )
    TheFuck(
        bug_id=27,
        buggy_commit_id="bc6b107066d3f1e60b4cfcaa8cf6399e98cf1b1c",
        fixed_commit_id="1becd92b126a368d6e7d93aa8eea209414ce4aa2",
        test_files=[Path("tests", "rules", "test_open.py")],
        test_cases=["tests/rules/test_open.py::test_get_new_command"],
        api=TheFuckAPI27(),
        unittests=TheFuckUnittestGenerator27(),
        systemtests=TheFuckSystemtestGenerator27(),
    )
    TheFuck(
        bug_id=28,
        buggy_commit_id="88831c424f569e6a55fc98883d3eeecc7d425b18",
        fixed_commit_id="9b30ae0424607a4e268bd26eaee8ccb91a5588f9",
        test_files=[Path("tests", "rules", "test_fix_file.py")],
        test_cases=["tests/rules/test_fix_file.py::test_get_new_command_with_settings"],
        api=TheFuckAPI28(),
        unittests=TheFuckUnittestGenerator28(),
        systemtests=TheFuckSystemtestGenerator28(),
    )
    TheFuck(
        bug_id=29,
        buggy_commit_id="4a2f869c6d6ef03d8d7ada1121cc6631d7ef979e",
        fixed_commit_id="88831c424f569e6a55fc98883d3eeecc7d425b18",
        test_files=[Path("tests", "test_types.py"), Path("tests", "test_utils.py")],
        test_cases=[
            "tests/test_types.py::test_update_settings",
            "tests/test_utils.py::test_wrap_settings",
        ],
        api=TheFuckAPI29(),
        unittests=TheFuckUnittestGenerator29(),
        systemtests=TheFuckSystemtestGenerator29(),
    )
    TheFuck(
        bug_id=30,
        buggy_commit_id="de513cacb150049e3f95434f8d6d30b7ed1e0ea7",
        fixed_commit_id="43fead02d3a24fef71534116c5550def0f56830c",
        test_files=[Path("tests", "rules", "test_fix_file.py")],
        test_cases=["tests/rules/test_fix_file.py::test_not_file"],
        api=TheFuckAPI30(),
        unittests=TheFuckUnittestGenerator30(),
        systemtests=TheFuckSystemtestGenerator30(),
    )
    TheFuck(
        bug_id=31,
        buggy_commit_id="66e2ec7e3f0d3f848c01d87bb3503b0ff90fc78a",
        fixed_commit_id="1285303363bc420bd7606bd5f808e3f2b4f0e83f",
        test_files=[Path("tests", "rules", "test_git_diff_staged.py")],
        test_cases=["tests/rules/test_git_diff_staged.py::test_get_new_command"],
        api=TheFuckAPI31(),
        unittests=TheFuckUnittestGenerator31(),
        systemtests=TheFuckSystemtestGenerator31(),
    )
    TheFuck(
        bug_id=32,
        buggy_commit_id="cb33c912e5f2f4c2da6b70d708ff0437bfcd3b94",
        fixed_commit_id="25cc98a21a3450a046caf418f08713c82a290805",
        test_files=[Path("tests", "rules", "test_ls_lah.py")],
        test_cases=["tests/rules/test_ls_lah.py::test_match"],
        api=TheFuckAPI32(),
        unittests=TheFuckUnittestGenerator32(),
        systemtests=TheFuckSystemtestGenerator32(),
    )


class TheFuckAPI1(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = str(process.args[2])
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        result = str(process.stdout.decode("utf8"))
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI2(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI3(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = " ".join(process.args[2:5])
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI4(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI5(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI6(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        if os.name == "nt":
            expected = process.args[2]
            expected = expected[1:]
            expected = expected.replace(",", "")
            result = process.stdout.decode("utf8").strip()
        else:
            expected = process.args[2]
            expected = expected.replace("(", "")
            expected = expected.replace(",", "")
            result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI7(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI8(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI9(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI10(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        result = process.stdout.decode("utf8").strip()
        if len(process.args) == 6:
            expected = process.args[2]
            expected = expected.replace(expected[len(expected) - 1], "")
            expected = expected.replace(expected[0], "")
        else:
            expected = str(process.args[2:5])
            expected = expected.replace("([", "")
            expected = expected.replace("],", "")
            expected = expected.replace("help,", "help")
            expected = expected.replace("read,", "read")
            expected = expected.replace("missing,", "missing")

        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI11(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = str(process.stdout.decode("utf8"))
        result = result.strip()
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI12(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI13(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        if os.name == "nt":
            expected = process.args[2]
            expected = expected[1:]
            expected = expected.replace(",", "")
            result = process.stdout.decode("utf8").strip()
        else:
            expected = process.args[2]
            expected = expected.replace("(", "")
            expected = expected.replace(",", "")
            result = process.stdout.decode("utf8").strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI14(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI15(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected.replace(expected[len(expected) - 1], "")
        expected = expected.replace(expected[0], "")
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI16(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[3]
        result = process.stdout.decode("utf8")
        expected = expected.replace(",", "")
        result = result.strip()
        expected = expected.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI17(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI18(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI19(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected.replace("(", "")
        expected = expected.replace(",", "")
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI20(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected.replace("(", "")
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI21(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected.replace("(", "")
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI22(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI23(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI24(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI25(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI26(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI27(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI28(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI29(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = " ".join(process.args[2:])
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected.replace("{", "")
        expected = expected.replace("}", "")
        if ":" in expected:
            split1, split2 = expected.split(":")
            expected = str({split1: split2})
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI30(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[4]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI31(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI32(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> str:
        return producer()

    @staticmethod
    def generate_random_string():
        return "".join(random.choices(string.ascii_letters, k=random.randint(5, 15)))

    @staticmethod
    def thefuck1_generate_():
        pip_commands = (
            "install",
            "uninstall",
            "inspect",
            "list",
            "show",
            "freeze",
            "check",
            "download",
            "wheel",
            "hash",
            "search",
            "cache",
            "config",
            "debug",
        )

        pip_passing_inputs = (
            "instl",
            "unstal",
            "spect",
            "lst",
            "shw",
            "freze",
            "chck",
            "downld",
            "whel",
            "hsh",
            "serch",
            "cach",
            "cnfig",
            "dbug",
        )

        pip_passing_inputs_2 = (
            "instal",
            "uninstal",
            "spct",
            "liist",
            "shoow",
            "frezee",
            "checke",
            "dwnload",
            "whell",
            "hassh",
            "serche",
            "cachee",
            "konfig",
            "dibug",
        )

        pip_failing_inputs = (
            "inst@ll",
            "uninst4LLL",
            "1nsp3ct",
            "l1st",
            "sh0w->",
            "FR33ze",
            "CHECK=",
            "-dowNLoad",
            "wh33l",
            "h4sh",
            "sEArch",
            "*cAch3",
            "c0nf1g",
            "~deBUG",
        )

        pip_failing_inputs_2 = (
            "1nstaLL",
            "UNinst4ll",
            "iNSPcT",
            "l1SSt",
            "ShOw->",
            "frEEz3",
            "che3kk=",
            "d0wNLo4d",
            "&WHeel",
            "-hAsh-",
            "@sEArch",
            "*CACh3",
            "c0nf1g-",
            "~deBUG",
        )

        randomise_int = random.randint(0, 13)
        randomise_string = TheFuckTestGenerator.generate_random_string()
        failing = (
            (
                f"pip {pip_commands[randomise_int]} {randomise_string}",
                f"pip {pip_failing_inputs[randomise_int]} {randomise_string}",
                f'ERROR: unknown command "{pip_failing_inputs[randomise_int]}", maybe you meant "{pip_commands[randomise_int]}"',
            ),
            (
                f"pip {pip_commands[randomise_int]} {randomise_string}",
                f"pip {pip_failing_inputs_2[randomise_int]} {randomise_string}",
                f'ERROR: unknown command "{pip_failing_inputs_2[randomise_int]}", maybe you meant "{pip_commands[randomise_int]}"',
            ),
        )

        passing = (
            (
                f"pip {pip_commands[randomise_int]} {randomise_string}",
                f"pip {pip_passing_inputs[randomise_int]} {randomise_string}",
                f'ERROR: unknown command "{pip_passing_inputs[randomise_int]}", maybe you meant "{pip_commands[randomise_int]}"',
            ),
            (
                f"pip {pip_commands[randomise_int]} {randomise_string}",
                f"pip {pip_passing_inputs_2[randomise_int]} {randomise_string}",
                f'ERROR: unknown command "{pip_passing_inputs_2[randomise_int]}", maybe you meant "{pip_commands[randomise_int]}"',
            ),
        )
        return passing[random.randint(0, len(passing) - 1)], failing[random.randint(0, len(failing) - 1)]

    @staticmethod
    def thefuck2_generate_():
        executables = []
        executable_paths = []
        path_dirs = os.environ.get("PATH", "").split(os.pathsep)

        for path_dir in path_dirs:
            for filename in os.listdir(path_dir):
                executables.append(filename)
                file_path = os.path.join(path_dir, filename)
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    executable_paths.append(file_path)

        passing = executables[random.randint(0, len(executables))]
        randomise = "".join(random.choices(string.ascii_letters, k=random.randint(5, 20)))
        failing = randomise
        return passing, failing

    @staticmethod
    def thefuck3_generate_():
        try:
            result = subprocess.run(
                ["fish", "-v"], capture_output=True, text=True, check=True
            )
            version_info = result.stdout[14:19]
            return f"Fish Shell {version_info}"

        except subprocess.CalledProcessError as err:
            return f"Error Retrieving Shell {err}"

    @staticmethod
    def thefuck4_generate_():
        alias = {}
        overriddens = []
        try:
            proc = subprocess.run(
                ["fish", "-ic", "alias"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
            )

            alias_out = proc.stdout.strip().split("\n")
            alias_out = [i.removeprefix("alias ") for i in alias_out]
            alias_split = [j.split("'") for j in alias_out]
            for k in alias_split:
                if len(k) >= 2:
                    first_ = k[0]
                    second_ = k[1]
                    first_ = first_.replace(" ", "")
                    alias[first_] = second_
                    overriddens = list(alias)
        except SystemError:
            "Cannot retrieve Fish Shell overridden"

        for overridden in overriddens:
            if overridden == "ls":
                overriddens.remove(overridden)
        return overriddens[random.randint(0, len(overriddens) - 1)]

    @staticmethod
    def thefuck5_generate_():
        randomise_branch_name = TheFuckTestGenerator.generate_random_string()
        passing = (
            (
                True,
                f"git push --set-upstream <remote> <{randomise_branch_name}>",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
            ),
            (
                False,
                f"git pull --set-upstream <remote> <{randomise_branch_name}>",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
            ),
        )

        failing = (
            (
                True,
                f"git pushpull --set-upstream <remote> <{randomise_branch_name}>",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
            ),
            (
                False,
                f"git push --set-upstream <remote> <{randomise_branch_name}> SELECT * FROM users",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
            ),
        )

        return passing[random.randint(0, 1)], failing[random.randint(0, 1)]

    @staticmethod
    def thefuck6_generate_():
        randomise_branch_name = TheFuckTestGenerator.generate_random_string()
        # Passing 1 and Failing 1 for match() function, the others are for get_command() function
        failing_ = (
            (
                False,
                f"git branch -d {randomise_branch_name} SELECT * FROM database",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
            (
                False,
                f"git branch -D {randomise_branch_name} SELECT * FROM database",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
        )

        failing2_ = (
            (
                [f"git branch -d {randomise_branch_name}, git branch {randomise_branch_name}"],
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
            (
                [f"git branch -d {randomise_branch_name}, git checkout -b {randomise_branch_name}"],
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
        )

        passing_ = (
            (
                True,
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name} already exists.",
            ),
            (
                True,
                f"git branch -D {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name} already exists.",
            ),
        )

        passing2_ = (
            (
                f"git branch -d {randomise_branch_name} && git branch {randomise_branch_name}",
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
            (
                f"git branch -d {randomise_branch_name} && git checkout -b {randomise_branch_name}",
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
        )

        passing2_windows_ = (
            (
                f"(git branch -d {randomise_branch_name}) -and (git branch {randomise_branch_name})",
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
            (
                f"(git branch -d {randomise_branch_name}) -and (git checkout -b {randomise_branch_name})",
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
        )

        failing2_windows_ = (
            (
                [f"git branch -d {randomise_branch_name}, git branch {randomise_branch_name}"],
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
            (
                [f"git branch -d {randomise_branch_name}, git checkout -b {randomise_branch_name}"],
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
        )
        # If system is Windows, we need to use like : (git branch -d branch_name) -and (git checkout -b branch_name)
        # In macOS, we can use like : git branch -d branch_name && git branch branch_name
        if os.name == "nt":
            return (
                passing_[random.randint(0, 1)],
                passing2_windows_[random.randint(0, 1)],
                failing_[random.randint(0, 1)],
                failing2_windows_[random.randint(0, 1)],
            )
        else:
            return (
                passing_[random.randint(0, 1)],
                passing2_[random.randint(0, 1)],
                failing_[random.randint(0, 1)],
                failing2_[random.randint(0, 1)],
            )

    @staticmethod
    def thefuck7_generate_():
        randomise_port_no = random.randint(50, 5000)
        passing_ = (
            f"php -s 127.0.0.0:{randomise_port_no}",
            f"php -s 127.1.1.1:{randomise_port_no}",
            f"php -s 127.1.0.1:{randomise_port_no}",
            f"php -s 127.0.1.0:{randomise_port_no}",
            f"php -s localhost:{randomise_port_no}",
            f"php -s localhost:{randomise_port_no} -c /path/to/php.ini",
            f"php -s localhost:{randomise_port_no} -t /path/to/your/project",
            f"php -s localhost:{randomise_port_no} router.php",
        )
        failing_ = (
            f"PHP -s 127.0.0.0:{randomise_port_no}",
            f"php -S 127.1.1.1:{randomise_port_no}",
            f"PHP -s 127.1.0.1:{randomise_port_no}",
            f"php -S 127.0.1.0:{randomise_port_no}",
            f"PHP -s localhost:{randomise_port_no}",
            f"php -S localhost:{randomise_port_no} -c /path/to/php.ini",
            f"PHP -s localhost:{randomise_port_no} -t /path/to/your/project",
            f"php -S localhost:{randomise_port_no} router.php",
        )
        return (
            passing_[random.randint(0, len(passing_) - 1)],
            failing_[random.randint(0, len(failing_) - 1)],
        )

    @staticmethod
    def thefuck8_generate_():
        dnf_operations_wrong = ['autooremove', 'cheeck', 'cheeck-updaate', 'cleean', 'deeplist',
                                'distroo-sync', 'downgraade', 'grooup', 'hellp', 'histoory',
                                'infoo', 'instaall', 'lisst', 'makecaache', 'maark', 'proovides',
                                'reinstaall', 'remoove', 'repoolist', 'repooquery',
                                'repoository-packages', 'seaarch', 'sheell', 'swaap', 'updateinfoo',
                                'upgrrade', 'upgrade-minimale', 'buuilddeep', 'config-manageer',
                                'coopr', 'debug-dumpe', 'debug-restoree', 'debuginfoo-install',
                                'downlooad', 'needss-restarting', 'plaayground', 'repocloosure',
                                'repoograph', 'repoomanage', 'repoosync']

        dnf_operations_correct = ['autoremove', 'check', 'check-update', 'clean', 'deplist',
                                  'distro-sync', 'downgrade', 'group', 'help', 'history',
                                  'info', 'install', 'list', 'makecache', 'mark', 'provides',
                                  'reinstall', 'remove', 'repolist', 'repoquery',
                                  'repository-packages', 'search', 'shell', 'swap', 'updateinfo',
                                  'upgrade', 'upgrade-minimal', 'builddep', 'config-manager',
                                  'copr', 'debug-dump', 'debug-restore', 'debuginfo-install',
                                  'download', 'needs-restarting', 'playground', 'repoclosure',
                                  'repograph', 'repomanage', 'reposync']

        app_random = TheFuckTestGenerator.generate_random_string()

        chosen_dnf_ = random.randint(0, len(dnf_operations_correct) - 1)

        script_passing_ = f"dnf {dnf_operations_wrong[chosen_dnf_]} {app_random}"

        script_failing_ = f"dnf {dnf_operations_correct[chosen_dnf_]} {app_random}"

        output_passing_ = """No such command: %s. Please use /usr/bin/dnf --help
        It could be a DNF plugin command, try: dnf install "dnf-command %s" 
        """ % (dnf_operations_wrong[chosen_dnf_], dnf_operations_correct[chosen_dnf_])

        output_failing_ = "No such command"

        return True, script_passing_, output_passing_, False, script_failing_, output_failing_

    @staticmethod
    def thefuck9_generate_():
        randomise_branch_name = TheFuckTestGenerator.generate_random_string()
        stderr = f'''fatal: The current branch {randomise_branch_name} has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin {randomise_branch_name}

'''
        passing = (
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push",
                "",
                stderr
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push -u origin",
                "",
                stderr
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push --set-upstream origin",
                "",
                stderr
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name} --quiet",
                "git push --quiet",
                "",
                stderr
            ),
        )

        failing = (
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push -u",
                "",
                stderr
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push --force",
                "",
                stderr
            ),
        )

        return (
            passing[random.randint(0, len(passing) - 1)],
            failing[random.randint(0, len(failing) - 1)],
        )

    @staticmethod
    def thefuck10_generate_():
        stdout = "Output Message: " + TheFuckTestGenerator.generate_random_string()
        passing = (
            ('man 3 read', 'man 2 read', stdout, ""),
            ('man 2 read', 'man 3 read', stdout, ""),
            ('man -s3 read', 'man -s2 read', stdout, ""),
            ('man -s2 read', 'man -s3 read', stdout, ""),
            ('man -s 3 read', 'man -s 2 read', stdout, ""),
            ('man -s 2 read', 'man -s 3 read', stdout, ""),
            ('man 3 write', 'man 2 write', stdout, ""),
            ('man 2 write', 'man 3 write', stdout, ""),
            ('man -s3 write', 'man -s2 write', stdout, ""),
            ('man -s2 write', 'man -s3 write', stdout, ""),
            ('man -s 3 write', 'man -s 2 write', stdout, ""),
            ('man -s 2 write', 'man -s 3 write', stdout, ""),
            (['read --help', 'man 3 read', 'man 2 read'], 'man read', stdout, ""),
            (['missing --help', 'man 3 missing', 'man 2 missing'], 'man missing', stdout,
             'No manual entry for missing\n'),

        )
        failing = (
            ('man 5 read', 'man 4 read', stdout, ""),
            ('man 4 read', 'man 5 read', stdout, ""),
            ('man -s5 read', 'man -s4 read', stdout, ""),
            ('man -s4 read', 'man -s5 read', stdout, ""),
            ('man -s 5 read', 'man -s 4 read', stdout, ""),
            ('man -s 4 read', 'man -s 5 read', stdout, ""),
            ('man 5 write', 'man 4 write', stdout, ""),
            ('man 4 write', 'man 5 write', stdout, ""),
            ('man -s5 write', 'man -s4 write', stdout, ""),
            ('man -s4 write', 'man -s5 write', stdout, ""),
            ('man -s 5 write', 'man -s 4 write', stdout, ""),
            ('man -s 4 write', 'man -s 5 write', stdout, ""),
            (['read --help', 'man 5 read', 'man 4 read'], 'man read', stdout, ""),
            (['missing --help', 'man 5 missing', 'man 4 missing'], 'man missing', stdout,
             'No manual entry for missing\n')
        )

        return passing[random.randint(0, len(passing) - 1)], failing[random.randint(0, len(failing) - 1)],

    @staticmethod
    def thefuck11_generate_():
        randomise_branch_name = TheFuckTestGenerator.generate_random_string()

        std_err = f'''fatal: The current branch has no upstream {randomise_branch_name}.
        To push the current branch and set the remote as upstream, use

            git push --set-upstream origin master

        '''
        passing = (
            (
                f"git push --set-upstream origin master",
                "git push",
                std_err
            ),
            (
                f"git push --set-upstream origin master -u origin",
                'git push -u origin',
                std_err
            ),
            (
                f"git push --set-upstream origin master --set-upstream origin",
                f'git push --set-upstream origin',
                std_err
            ),
            (
                "git push --set-upstream origin master --quiet",
                'git push --quiet',
                std_err
            ),
        )

        failing = (
            (
                f"git push --set-upstream origin master",
                std_err,
                "git push",
            ),
            (
                f"git push --set-upstream origin master -u origin",
                std_err,
                'git push -u origin',
            ),
            (
                f"git push --set-upstream origin master --set-upstream origin",
                std_err,
                f'git push --set-upstream origin',
            ),
            (
                "git push --set-upstream origin master --quiet",
                std_err,
                'git push --quiet',
            ),
        )
        return passing[random.randint(0, len(passing) - 1)], failing[random.randint(0, len(failing) - 1)]

    @staticmethod
    def thefuck12_generate_():
        randomise_string = TheFuckTestGenerator.generate_random_string()
        passing = (
            (
                True,
                f"got commit -m {randomise_string}",
                'got: not found, maybe you meant "git"'
            ),
            (
                True,
                f"sudo fucck {randomise_string}",
                'fuckk: not found, maybe you meant "fsck"'
            ),
            (
                True,
                f"vom {randomise_string}.py",
                'vom: not found, maybe you meant "vim"'
            ),
        )

        failing = (
            (
                True,
                f"gu run {randomise_string}.go",
                'gu: not found, maybe you meant "go"'
            ),
        )
        return passing[random.randint(0, len(passing) - 1)], failing[0]

    @staticmethod
    def thefuck13_generate_():
        branch_name = TheFuckTestGenerator.generate_random_string()
        # Passing 1 and Failing 1 for def match() function, the others are for def get_command() function
        passing_ = (
            (
                True,
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name} already exists.",
            ),
            (
                True,
                f"git branch -D {branch_name}",
                f"fatal: A branch named '{branch_name} already exists.",
            ),
        )

        passing2_ = (
            (
                f"git branch -d {branch_name} && git branch {branch_name}",
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
            (
                f"git branch -d {branch_name} && git branch {branch_name}",
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
        )

        failing_ = (
            (
                False,
                f"git branch -d {branch_name} SELECT * FROM database",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
            (
                False,
                f"git branch -D {branch_name} SELECT * FROM database",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
        )

        failing2_ = (
            (
                [f"git branch -d {branch_name}, git branch {branch_name}"],
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
            (
                [f"git branch -d {branch_name}, git checkout -b {branch_name}"],
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
        )

        passing2_windows_ = (
            (
                f"(git branch -d {branch_name}) -and (git branch {branch_name})",
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
            (
                f"(git branch -d {branch_name}) -and (git branch {branch_name})",
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
        )

        failing2_windows_ = (
            (
                [f"git branch -d {branch_name}, git branch {branch_name}"],
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
            (
                [f"git branch -d {branch_name}, git checkout -b {branch_name}"],
                f"git branch -d {branch_name}",
                f"fatal: A branch named '{branch_name}' already exists.",
            ),
        )
        # If system is Windows, we need to use like : (git branch -d branch_name) -and (git checkout -b branch_name)
        # In macOS, we can use like : git branch -d branch_name && git branch branch_name
        if os.name == "nt":
            return (
                passing_[random.randint(0, 1)],
                passing2_windows_[random.randint(0, 1)],
                failing_[random.randint(0, 1)],
                failing2_windows_[random.randint(0, 1)],
            )
        else:
            return (
                passing_[random.randint(0, 1)],
                passing2_[random.randint(0, 1)],
                failing_[random.randint(0, 1)],
                failing2_[random.randint(0, 1)],
            )

    @staticmethod
    def thefuck14_generate_():
        overridden_ = []
        overridden_alias = {'cd', 'grep', 'ls', 'man', 'open'}
        try:
            for alias in os.environ.get('TF_OVERRIDDEN_ALIASES', '').split(','):
                overridden_alias.add(alias.strip())
            for item in overridden_alias:
                if item != "":
                    overridden_.append(item)
            return overridden_[random.randint(0, len(overridden_) - 1)]

        except SystemError or OSError:
            return "Error Retrieving Fish Shell Overridden"

    @staticmethod
    def thefuck15_generate_():
        randomise_ = TheFuckTestGenerator.generate_random_string()
        match_passing = ((True, f"git submodule update {randomise_}",
                          f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?"),
                         (True, f"git commit {randomise_}",
                          f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?"))

        match_failing = ((True, f"git submodule update {randomise_}", ""),
                         (True, f"git commit {randomise_}", ""))

        get_new_command_passing = (
            (f"git add -- {randomise_} && git submodule update {randomise_}", f"git submodule update {randomise_}",
             f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?"),
            (f"git add -- {randomise_} && git commit {randomise_}", f"git commit {randomise_}",
             f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?"))

        get_new_command_failing = (
            (f"git add -- {randomise_} && git submodule update {randomise_}", f"GIT SUBMODULE UPDATE {randomise_}",
             f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?"),
            (f"git add -- {randomise_} && git commit {randomise_}", f"GIT COMMIT {randomise_}",
             f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?"))

        return (match_passing[random.randint(0, len(match_passing) - 1)],
                get_new_command_passing[random.randint(0, len(get_new_command_passing) - 1)],
                match_failing[random.randint(0, len(match_failing) - 1)],
                get_new_command_failing[random.randint(0, len(get_new_command_failing) - 1)])

    @staticmethod
    def thefuck16_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        passing_bash_ = (
            ("1", f"TF_ALIAS={randomise}", f"{randomise}"),
            ("1", "PYTHONIOENCODING=utf-8", f"{randomise}"),
            ("1", " history -s $TF_CMD", f"{randomise}"),
            ("1", "  eval $TF_CMD ", f"{randomise}"),
            ("1", f"alias {randomise}", f"{randomise}"),
        )
        failing_bash_ = (
            ("1", f"alias {randomise}='TF_CMD=$(TF_ALIAS", f"{randomise}"),
            ("1", f"$(TF_ALIAS={randomise} PYTHONIOENCODING", f"{randomise}"),
            ("1", "PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES", f"{randomise}")
        )

        passing_zsh_ = (
            ("2", f"TF_ALIAS={randomise}", f"{randomise}"),
            ("2", "PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES", f"{randomise}"),
            ("2", "PYTHONIOENCODING=utf-8", f"{randomise}"),
            ("2", f"alias {randomise}", f"{randomise}"),
        )
        failing_zsh_ = (
            ("2", f"alias {randomise}='TF_CMD=$(TF_ALIAS", f"{randomise}"),
            ("2", " history -s $TF_CMD", f"{randomise}"),
            ("2", "  eval $TF_CMD ", f"{randomise}"),
            ("2", f"$(TF_ALIAS={randomise} PYTHONIOENCODING", f"{randomise}"),
        )

        return (passing_bash_[random.randint(0, len(passing_bash_) - 1)],
                passing_zsh_[random.randint(0, len(passing_zsh_) - 1)],
                failing_bash_[random.randint(0, len(failing_bash_) - 1)],
                failing_zsh_[random.randint(0, len(failing_zsh_) - 1)])

    @staticmethod
    def thefuck17_generate_():
        randomise_alias_name = TheFuckTestGenerator.generate_random_string()
        passing = (
            (f"alias {randomise_alias_name}", randomise_alias_name),
            (f"TF_ALIAS={randomise_alias_name}", randomise_alias_name))
        failing = (f"the{randomise_alias_name}", randomise_alias_name)
        return passing[random.randint(0, 1)], failing

    @staticmethod
    def thefuck18_generate_():
        randomise = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 1)))
        randomise_ = "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 2)))
        passing_ = (
            (True, f'sudo {randomise_} -{randomise}', 'Permission denied', ''),
            (True, f'sudo {randomise_} -{randomise}', 'permission denied', ''),
            (True, f'sudo {randomise_} -{randomise}', "npm ERR! Error: EACCES, unlink", ''),
            (True, f'sudo {randomise_} -{randomise}', 'requested operation requires superuser privilege', ''),
            (True, f'sudo {randomise_} -{randomise}', 'need to be root', ''),
            (True, f'sudo {randomise_} -{randomise}', 'need root', ''),
            (True, f'sudo {randomise_} -{randomise}', 'must be root', ''),
            (True, f'sudo {randomise_} -{randomise}', 'You don\'t have access to the history DB.', ''),
            (True, f'sudo {randomise_} -{randomise}', '',
             "error: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/ipaddr.py'"))

        failing_ = (
            (False, f'sudo {randomise_} -{randomise}', ' PERMISSION DENIED ', ''),
            (False, f'sudo {randomise_} -{randomise}', " NPM ERR! ERROR: EACCES, UNLINK ", ''),
            (False, f'sudo {randomise_} -{randomise}', ' REQUESTED OPERATION REQUIRES SUPERUSER PRIVILEGE ', ''),
            (False, f'sudo {randomise_} -{randomise}', ' NEED TO BE ROOT ', ''),
            (False, f'sudo {randomise_} -{randomise}', ' NEED ROOT ', ''),
            (False, f'sudo {randomise_} -{randomise}', ' MUST BE ROOT ', ''),
            (False, f'sudo {randomise_} -{randomise}', ' YOU DON\'T HAVE ACCESS TO THE HISTORY DB. ', ''),
            (False, f'sudo {randomise_} -{randomise}', '',
             " ERROR: [ERRNO 13] PERMISSION DENIED: '/USR/LOCAL/LIB/PYTHON2.7/DIST-PACKAGES/IPADDR.PY' "))

        return passing_[random.randint(0, len(passing_) - 1)], failing_[random.randint(0, len(failing_) - 1)],

    @staticmethod
    def thefuck19_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        git_err = '''
        To /tmp/foo
         ! [rejected]        master -> master (non-fast-forward)
         error: failed to push some refs to '/tmp/bar'
         hint: Updates were rejected because the tip of your current branch is behind
         hint: its remote counterpart. Integrate the remote changes (e.g.
         hint: 'git pull ...') before pushing again.
         hint: See the 'Note about fast-forwards' in 'git push --help' for details.
        '''
        it_uptodate = 'Everything up-to-date'
        git_ok = '''
        Counting objects: 3, done.
        Delta compression using up to 4 threads.
        Compressing objects: 100% (2/2), done.
        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.
        Total 3 (delta 0), reused 0 (delta 0)
        To /tmp/bar
           514eed3..f269c79  master -> master
        '''
        passing_match_ = (True, f"git push {randomise}", "", git_err)

        failing_match_ = (
            (True, f"git push {randomise}", "", it_uptodate),
            (True, f"git push {randomise}", "", git_ok))

        passing_get_new_command_ = (f"git push --force {randomise}", f"git push {randomise}", "", "")

        failing_get_new_command_ = (
            (f"git push --force {randomise}", f"git PUSH {randomise}", "", ""))

        return (passing_match_, passing_get_new_command_,
                failing_match_[random.randint(0, len(failing_match_) - 1)], failing_get_new_command_)

    @staticmethod
    def thefuck20_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        randomise2 = TheFuckTestGenerator.generate_random_string()

        passing_zip_file_ = (
            (f"{randomise}.zip", f"unzip {randomise}.zip"),
            (f"{randomise}.zip", f"unzip {randomise}"))

        failing_zip_file_ = (f"{randomise}, {randomise2}", f"unzip {randomise}.zip, {randomise2}.zip")

        passing_get_new_command = (
            (f'unzip {randomise} -d {randomise}', f'unzip {randomise}'),
            (f'unzip {randomise}.zip -d {randomise}', f'unzip {randomise}.zip'))

        failing_get_new_command = (
            (fR"unzip {randomise}\ {randomise2}.zip -d '{randomise} {randomise2}'",
             fR"unzip {randomise}\ {randomise2}.zip"),
            (fR"unzip '{randomise} {randomise2}.zip' -d '{randomise} {randomise2}'",
             fR"unzip '{randomise} {randomise2}.zip'"))

        return (passing_zip_file_[random.randint(0, len(passing_zip_file_) - 1)],
                passing_get_new_command[random.randint(0, len(passing_get_new_command) - 1)],
                failing_zip_file_, failing_get_new_command[random.randint(0, len(failing_get_new_command) - 1)])

    @staticmethod
    def thefuck21_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        stash_commands = (
            'apply',
            'branch',
            'clear',
            'drop',
            'list',
            'pop',
            'save',
            'show')

        git_stash_err = '''
        usage: git stash list [<options>]
           or: git stash show [<stash>]
           or: git stash drop [-q|--quiet] [<stash>]
           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
           or: git stash branch <branchname> [<stash>]
           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]
        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]
           or: git stash clear
        '''
        passing_match_ = (
            True, f"git stash {stash_commands[random.randint(0, len(stash_commands) - 1)]} {randomise}", git_stash_err)
        failing_match_ = (
            True, f"git {stash_commands[random.randint(0, len(stash_commands) - 1)]} {randomise}", git_stash_err)

        return passing_match_, failing_match_

    @staticmethod
    def thefuck22_generate_():
        randomise1 = TheFuckTestGenerator.generate_random_string()
        randomise2 = TheFuckTestGenerator.generate_random_string()
        randomise3 = TheFuckTestGenerator.generate_random_string()

        randomise_script1 = f"git commit {randomise1}"
        randomise_script2 = f"git checkout {randomise2}"
        randomise_script3 = f"git branch {randomise3}"

        randomise_priority_passing1 = random.randint(1, 1000)
        randomise_priority_passing2 = random.randint(1, 1000)
        randomise_priority_passing3 = random.randint(1, 1000)

        side_effect = None
        expected = None

        passing_ = (expected,
                    randomise_script1, side_effect, randomise_priority_passing1,
                    randomise_script2, side_effect, randomise_priority_passing2,
                    randomise_script3, side_effect, randomise_priority_passing3)
        # failing test has priority of None or string
        failing_ = (
            (expected,
             randomise_script1, side_effect, "",
             randomise_script2, side_effect, "",
             randomise_script3, side_effect, ""),
            (expected,
             randomise_script1, side_effect, None,
             randomise_script2, side_effect, None,
             randomise_script3, side_effect, None))

        return passing_, failing_[random.randint(0, 1)]

    @staticmethod
    def thefuck23_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        passing_ = ({'key': {'etag': '0', 'value': f'{randomise}'}}, f'{randomise}', {})
        failing_ = ({}, f'{randomise}', {})
        return passing_, failing_

    @staticmethod
    def thefuck24_generate_():
        randomise1 = "".join(random.choices(string.ascii_letters, k=random.randint(4, 8)))
        randomise2 = "".join(random.choices(string.ascii_letters, k=random.randint(4, 8)))
        randomise3 = "".join(random.choices(string.ascii_letters, k=random.randint(4, 8)))
        passing_ = (randomise1, [randomise1, randomise2])
        failing_ = (randomise3, [randomise1, randomise2])
        return passing_, failing_

    @staticmethod
    def thefuck25_generate_():
        randomise1 = "".join(random.choices(string.ascii_letters, k=random.randint(3, 6)))
        randomise2 = "".join(random.choices(string.ascii_letters, k=random.randint(3, 6)))
        randomise3 = "".join(random.choices(string.ascii_letters, k=random.randint(3, 6)))
        passing = (f'mkdir -p {randomise1}/{randomise2}/{randomise3}', f'mkdir {randomise1}/{randomise2}/{randomise3}')

        failing = (
            (f'hdfs dfs -mkdir -p {randomise1}/{randomise2}/{randomise3}',
             f'hdfs dfs -mkdir {randomise1}/{randomise2}/{randomise3}'),
            (f'./bin/hdfs dfs -mkdir -p {randomise1}/{randomise2}/{randomise3}',
             f'./bin/hdfs dfs -mkdir {randomise1}/{randomise2}/{randomise3}'))
        return passing, failing[random.randint(0, len(failing) - 1)]

    @staticmethod
    def thefuck26_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        passing = ((f'vagrant up  && vagrant {randomise}', f'vagrant {randomise}',
                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                   (f'vagrant up devbox && vagrant {randomise} devbox', f'vagrant {randomise} devbox',
                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'))
        failing = ([f'vagrant up devbox  && vagrant {randomise} devbox', f'vagrant up  && vagrant {randomise} devbox'],
                   f'vagrant {randomise} devbox',
                   'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.')

        return passing[random.randint(0, len(passing) - 1)], failing

    @staticmethod
    def thefuck27_generate_():
        randomise = "".join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
        passing = ((f'open http://{randomise}.com', f'open {randomise}.com'),
                   (f'open http://{randomise}.io', f'open {randomise}.io'))
        failing = (
            (f'xdg-open http://{randomise}.io', f'xdg-open {randomise}.io'),
            (f'gnome-open http://{randomise}.io', f'gnome-open {randomise}.io',))

        return passing[random.randint(0, len(passing) - 1)], failing[random.randint(0, len(failing) - 1)]

    @staticmethod
    def thefuck28_generate_():
        randomise_int = random.randint(1, 101)
        randomise_int_2 = random.randint(1, 101)
        # (script, file, line, col (or None), stdout, stderr)
        tests = (
            ('gcc a.c', 'a.c', randomise_int, randomise_int_2, '',
             """
             a.c: In function 'main':
             a.c:3:1: error: expected expression before '}' token
              }
               ^
             """),

            ('clang a.c', 'a.c', randomise_int, randomise_int_2, '',
             """
             a.c:3:1: error: expected expression
             }
             ^
             """),

            ('perl a.pl', 'a.pl', randomise_int, randomise_int_2, '',
             """
             syntax error at a.pl line 3, at EOF
             Execution of a.pl aborted due to compilation errors.
             """),

            ('perl a.pl', 'a.pl', randomise_int, randomise_int_2, '',
             """
             Search pattern not terminated at a.pl line 2.
             """),

            ('sh a.sh', 'a.sh', randomise_int, randomise_int_2, '',
             """
             a.sh: line 2: foo: command not found
             """),

            ('zsh a.sh', 'a.sh', randomise_int, randomise_int_2, '',
             """
             a.sh:2: command not found: foo
             """),

            ('bash a.sh', 'a.sh', randomise_int, randomise_int_2, '',
             """
             a.sh: line 2: foo: command not found
             """),

            ('rustc a.rs', 'a.rs', randomise_int, randomise_int_2, '',
             """
             a.rs:2:5: 2:6 error: unexpected token: `+`
             a.rs:2     +
                        ^
             """),

            ('cargo build', 'src/lib.rs', randomise_int, randomise_int_2, '',
             """
                Compiling test v0.1.0 (file:///tmp/fix-error/test)
                src/lib.rs:3:5: 3:6 error: unexpected token: `+`
                src/lib.rs:3     +
                                 ^
             Could not compile `test`.
     
             To learn more, run the command again with --verbose.
             """),

            ('python a.py', 'a.py', randomise_int, randomise_int_2, '',
             """
               File "a.py", line 2
                   +
                       ^
             SyntaxError: invalid syntax
             """),

            ('python a.py', 'a.py', randomise_int, randomise_int_2, '',
             """
             Traceback (most recent call last):
               File "a.py", line 8, in <module>
                 match("foo")
               File "a.py", line 5, in match
                 m = re.search(None, command)
               File "/usr/lib/python3.4/re.py", line 170, in search
                 return _compile(pattern, flags).search(string)
               File "/usr/lib/python3.4/re.py", line 293, in _compile
                 raise TypeError("first argument must be string or compiled pattern")
             TypeError: first argument must be string or compiled pattern
             """),

            ('ruby a.rb', 'a.rb', randomise_int, randomise_int_2, '',
             """
             a.rb:3: syntax error, unexpected keyword_end
             """),

            ('lua a.lua', 'a.lua', randomise_int, randomise_int_2, '',
             """
             lua: a.lua:2: unexpected symbol near '+'
             """),

            ('fish a.sh', '/tmp/fix-error/a.sh', randomise_int, randomise_int_2, '',
             """
             fish: Unknown command 'foo'
             /tmp/fix-error/a.sh (line 2): foo
                                           ^
             """),

            ('./a', './a', randomise_int_2, randomise_int_2, '',
             """
             awk: ./a:2: BEGIN { print "Hello, world!" + }
             awk: ./a:2:                                 ^ syntax error
             """),

            ('llc a.ll', 'a.ll', randomise_int, randomise_int_2, '',
             """
             llc: a.ll:1:2: error: expected top-level entity
             +
             ^
             """),

            ('go build a.go', 'a.go', randomise_int, randomise_int_2, '',
             """
             can't load package:
             a.go:1:2: expected 'package', found '+'
             """),

            ('make', 'Makefile', randomise_int, randomise_int_2, '',
             """
             bidule
             make: bidule: Command not found
             Makefile:2: recipe for target 'target' failed
             make: *** [target] Error 127
             """),

            ('git st', '/home/martin/.config/git/config', randomise_int, randomise_int_2, '',
             """
             fatal: bad config file line 1 in /home/martin/.config/git/config
             """),

            ('node fuck.js asdf qwer', '/Users/pablo/Workspace/barebones/fuck.js', f'{randomise_int}', randomise_int_2,
             '',
             """
             /Users/pablo/Workspace/barebones/fuck.js:2
             conole.log(arg);  // this should read console.log(arg);
             ^
             ReferenceError: conole is not defined
                 at /Users/pablo/Workspace/barebones/fuck.js:2:5
                 at Array.forEach (native)
                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)
                 at Module._compile (module.js:460:26)
                 at Object.Module._extensions..js (module.js:478:10)
                 at Module.load (module.js:355:32)
                 at Function.Module._load (module.js:310:12)
                 at Function.Module.runMain (module.js:501:10)
                 at startup (node.js:129:16)
                 at node.js:814:3
             """)
        )

        # print(os.environ)
        script = tests[random.randint(0, len(tests) - 1)][0]
        out = tests[random.randint(0, len(tests) - 1)][4]
        error = tests[random.randint(0, len(tests) - 1)][5]
        failing = True, script, out, error
        passing = False, script, out, error
        return passing, failing

    @staticmethod
    def thefuck29_generate_():
        random_key = TheFuckTestGenerator.generate_random_string()
        random_value = TheFuckTestGenerator.generate_random_string()
        passing_ = {f'{random_key}': f'{random_value}'}
        failing_ = {f'{random_key}, {random_value}'}
        return passing_, failing_

    @staticmethod
    def thefuck30_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()

        # (script, file, line, col (or None), stderr)
        tests = (
            (f'{randomise} a.c', 'a.c', 3, 1,
             """
             a.c: In function 'main':
             a.c:3:1: error: expected expression before '}' token
              }
               ^
             """),

            (f'{randomise} a.c', 'a.c', 3, 1,
             """
             a.c:3:1: error: expected expression
             }
             ^
             """),

            (f'{randomise} a.pl', 'a.pl', 3, None,
             """
             syntax error at a.pl line 3, at EOF
             Execution of a.pl aborted due to compilation errors.
             """),

            (f'{randomise} a.pl', 'a.pl', 2, None,
             """
             Search pattern not terminated at a.pl line 2.
             """),

            (f'{randomise} a.sh', 'a.sh', 2, None,
             """
             a.sh: line 2: foo: command not found
             """),

            (f'{randomise} a.sh', 'a.sh', 2, None,
             """
             a.sh:2: command not found: foo
             """),

            (f'{randomise} a.sh', 'a.sh', 2, None,
             """
             a.sh: line 2: foo: command not found
             """),

            (f'{randomise} a.rs', 'a.rs', 2, 5,
             """
             a.rs:2:5: 2:6 error: unexpected token: `+`
             a.rs:2     +
                        ^
             """),

            (f'{randomise}', 'src/lib.rs', 3, 5,
             """
                Compiling test v0.1.0 (file:///tmp/fix-error/test)
                src/lib.rs:3:5: 3:6 error: unexpected token: `+`
                src/lib.rs:3     +
                                 ^
             Could not compile `test`.

             To learn more, run the command again with --verbose.
             """),

            (f'{randomise} a.py', 'a.py', 2, None,
             """
               File "a.py", line 2
                   +
                       ^
             SyntaxError: invalid syntax
             """),

            (f'{randomise} a.py', 'a.py', 8, None,
             """
             Traceback (most recent call last):
               File "a.py", line 8, in <module>
                 match("foo")
               File "a.py", line 5, in match
                 m = re.search(None, command)
               File "/usr/lib/python3.4/re.py", line 170, in search
                 return _compile(pattern, flags).search(string)
               File "/usr/lib/python3.4/re.py", line 293, in _compile
                 raise TypeError("first argument must be string or compiled pattern")
             TypeError: first argument must be string or compiled pattern
             """
             ),

            (f'{randomise} a.rb', 'a.rb', 3, None,
             """
             a.rb:3: syntax error, unexpected keyword_end
             """),

            (f'{randomise} a.lua', 'a.lua', 2, None,
             """
             lua: a.lua:2: unexpected symbol near '+'
             """),

            (f'{randomise} a.sh', '/tmp/fix-error/a.sh', 2, None,
             """
             fish: Unknown command 'foo'
             /tmp/fix-error/a.sh (line 2): foo
                                           ^
             """),

            (f'./a', './a', 2, None,
             """
             awk: ./a:2: BEGIN { print "Hello, world!" + }
             awk: ./a:2:                                 ^ syntax error
             """),

            (f'{randomise} a.ll', 'a.ll', 1, None,
             """
             llc: a.ll:1:1: error: expected top-level entity
             +
             ^
             """),

            (f'{randomise} build a.go', 'a.go', 1, None,
             """
             can't load package:
             a.go:1:1: expected 'package', found '+'
             """),

            (f'{randomise}', 'Makefile', 2, None,
             """
             bidule
             make: bidule: Command not found
             Makefile:2: recipe for target 'target' failed
             make: *** [target] Error 127
             """),

            (f'{randomise} st', '/home/martin/.config/git/config', 1, None,
             """
             fatal: bad config file line 1 in /home/martin/.config/git/config
             """),

            (f'{randomise} fuck.js asdf qwer', '/Users/pablo/Workspace/barebones/fuck.js', '2', 5,
             """
             /Users/pablo/Workspace/barebones/fuck.js:2
             conole.log(arg);  // this should read console.log(arg);
             ^
             ReferenceError: conole is not defined
                 at /Users/pablo/Workspace/barebones/fuck.js:2:5
                 at Array.forEach (native)
                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)
                 at Module._compile (module.js:460:26)
                 at Object.Module._extensions..js (module.js:478:10)
                 at Module.load (module.js:355:32)
                 at Function.Module._load (module.js:310:12)
                 at Function.Module.runMain (module.js:501:10)
                 at startup (node.js:129:16)
                 at node.js:814:3
             """),
        )
        script = tests[random.randint(0, len(tests) - 1)][0]
        error = tests[random.randint(0, len(tests) - 1)][4]
        if 'EDITOR' in os.environ:
            return script, error, True
        else:
            return script, error, False

    @staticmethod
    def thefuck31_generate_():
        randomise_int = random.randint(1, 9999)
        randomise_str = TheFuckTestGenerator.generate_random_string()
        passing_ = (f"git diff {randomise_str} --staged", f"git diff {randomise_str}")
        failing_ = ("Integer value cannot be used", randomise_int)
        return passing_, failing_

    @staticmethod
    def thefuck32_generate_():
        randomise_str = TheFuckTestGenerator.generate_random_string()
        dice = random.randint(0, 1)
        passing_ = ((True, f"ls {randomise_str}.py"),
                    (True, f"ls /{randomise_str}"))
        failing_ = ((True, f"ls -lah /{randomise_str}"),
                    (True, f"pacman -s {randomise_str}"))
        return passing_[dice], failing_[dice]


class TheFuckUnittestGenerator1(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck1_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            script: str,
            output: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=output),
                                ],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.rules.pip_unknown_command",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        expected, script, output = fail_
        test.body = self._get_assert(expected, script, output)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        expected, script, output = pass_
        test.body = self._get_assert(expected, script, output)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator2(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck2_generate_)

    @staticmethod
    def _get_assert(
            result: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                args=[
                    ast.Constant(value=result),
                    ast.Call(
                        func=ast.Name(id="get_all_executables"),
                        args=[],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.utils",
                names=[ast.alias(name="get_all_executables")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator3(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck3_generate_)

    @staticmethod
    def _get_assert(
            result: str,
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="f")],
                value=ast.Call(
                    func=ast.Name(id="Fish"),
                    args=[],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=result),
                        ast.Call(
                            func=ast.Attribute(value=ast.Name(id="f"), attr="info"),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.shells.fish",
                names=[ast.alias(name="Fish")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fail_ = self._generate_one()
        if fail_[0:4] == "Fish":
            fail_ = "Error Retrieving Shell"
        test = self.get_empty_test()
        test.body = self._get_assert(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator4(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck4_generate_)

    @staticmethod
    def _get_assert(
            result: Any,
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="f")],
                value=ast.Call(
                    func=ast.Name(id="Fish"),
                    args=[],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                    args=[
                        ast.Constant(value=result),
                        ast.Call(
                            func=ast.Name(id="_get_aliases"),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id="f"),
                                        attr="_get_overridden_aliases",
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.shells.fish",
                names=[ast.alias(name="Fish")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.shells.fish",
                names=[ast.alias(name="_get_aliases")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _ = self._generate_one()
        test = self.get_empty_test()
        fail_ = "Error Retrieving Fish Shell Overridden"
        test.body = self._get_assert(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator5(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck5_generate_)

    @staticmethod
    def _get_assert(
            expected: bool,
            script_parts: str,
            output: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script_parts),
                                    ast.Constant(value=output),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_push",
                names=[ast.alias(name="match")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script_parts, output = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script_parts, output)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script_parts, output = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script_parts, output)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator6(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck6_generate_)

    @staticmethod
    def _get_assert(expected: str | bool, script: str, std_err: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_assert_2(expected: bool | str, script: str, std_err: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.rules.git_branch_exists",
                names=[ast.alias(name="match")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_branch_exists",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, _, fail_, fail2_ = self._generate_one()
        # There are two functions to be tested so dice_ will decide
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            expected, script, output = fail_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, output)
        else:
            expected, script, output = fail2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(expected, script, output)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, pass2_, _, _ = self._generate_one()
        # There are two functions to be tested so dice_ will decide
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            expected, script, output = pass_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, output)
        else:
            expected, script, output = pass2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(expected, script, output)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator7(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck7_generate_)

    @staticmethod
    def _get_assert(
            expected: bool,
            script: str,
            output: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=output),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.php_s",
                names=[ast.alias(name="match")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(True, fail_, "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(True, pass_, "")
        return test, TestResult.PASSING


class TheFuckUnittestGenerator8(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck8_generate_)

    @staticmethod
    def _get_assert(expected: Any, script: str, output: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=output),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.rules.dnf_no_such_command",
                names=[ast.alias(name="match")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),

        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, _, _, expected, script, output = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, output)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        expected, script, output, _, _, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, output)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator9(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck9_generate_)

    @staticmethod
    def _get_assert(
            expected: str, script_parts: str, output_stdout: str, output_stderr: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script_parts),
                                    ast.Constant(value=output_stdout),
                                    ast.Constant(value=output_stderr),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_push",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script_parts, output_stdout, output_stderr = fail_

        test = self.get_empty_test()
        test.body = self._get_assert(
            expected, script_parts, output_stdout, output_stderr
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script_parts, output_stdout, output_stderr = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(
            expected, script_parts, output_stdout, output_stderr
        )
        return test, TestResult.PASSING


class TheFuckUnittestGenerator10(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck10_generate_)

    @staticmethod
    def _get_assert(
            expected: str | list, script: str, std_out: str, std_err: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.man",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script, std_out, std_err = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, std_out, std_err)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script, std_out, std_err = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, std_out, std_err)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator11(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck11_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            command: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=command),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.rules.git_push",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        expected, command, std_err = fail_
        test.body = self._get_assert(expected, command, "", std_err)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        expected, command, std_err = pass_
        test.body = self._get_assert(expected, command, "", std_err)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator12(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck12_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            command: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=command),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.rules.no_command",
                names=[ast.alias(name="match")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        expected, command, std_err = fail_
        test.body = self._get_assert(expected, command, "", std_err)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        expected, command, std_err = pass_
        test.body = self._get_assert(expected, command, "", std_err)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator13(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck13_generate_)

    @staticmethod
    def _get_assert(expected: bool | str, script: str, std_out: str, std_err: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_assert_2(expected: str | bool, script: str, std_out: str, std_err: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_branch_exists",
                names=[ast.alias(name="match")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_branch_exists",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, _, fail_, fail2_ = self._generate_one()
        # There are two functions to be tested so dice_ will decide
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            expected, script, std_err = fail_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, "", std_err)
        else:
            expected, script, std_err = fail2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(expected, script, "", std_err)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, pass2_, _, _ = self._generate_one()
        # There are two functions to be tested so dice_ will decide
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            expected, script, std_err = pass_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, "", std_err)
        else:
            expected, script, std_err = pass2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(expected, script, "", std_err)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator14(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck14_generate_)

    @staticmethod
    def _get_assert(
            result: Any,
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="f")],
                value=ast.Call(
                    func=ast.Name(id="Fish"),
                    args=[],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                    args=[
                        ast.Constant(value=result),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="f"),
                                attr="_get_overridden_aliases",
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.shells.fish",
                names=[ast.alias(name="Fish")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        fail_ = "Error Retrieving Fish Shell Overridden"
        test.body = self._get_assert(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator15(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck15_generate_)

    @staticmethod
    def _get_assert(expected: bool, script: str, std_out: str, std_err: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_assert_2(expected: str, script: str, std_out: str, std_err: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_add",
                names=[ast.alias(name="match")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_add",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, _, fail_, fail2_ = self._generate_one()
        # There are two functions to be tested so dice_ will decide
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            expected, script, std_err = fail_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, "", std_err)
        else:
            expected, script, std_err = fail2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(expected, script, "", std_err)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, pass2_, _, _ = self._generate_one()
        # There are two functions to be tested so dice_ will decide
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            expected, script, std_err = pass_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, "", std_err)
        else:
            expected, script, std_err = pass2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(expected, script, "", std_err)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator16(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck16_generate_)

    @staticmethod
    def _get_assert(
            result: str,
            text: str
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="b")],
                value=ast.Call(
                    func=ast.Name(id="Bash"),
                    args=[],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                    args=[
                        ast.Constant(value=result),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="b"),
                                attr="app_alias",
                            ),
                            args=[ast.Constant(value=text), ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    @staticmethod
    def _get_assert_2(
            result: str,
            text: str
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="z")],
                value=ast.Call(
                    func=ast.Name(id="Zsh"),
                    args=[],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                    args=[
                        ast.Constant(value=result),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="z"),
                                attr="app_alias",
                            ),
                            args=[ast.Constant(value=text), ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.shells.bash",
                names=[ast.alias(name="Bash")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.shells.zsh",
                names=[ast.alias(name="Zsh")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, _, fail_, fail2_ = self._generate_one()
        dice = random.randint(0, 1)
        if dice == 0:
            _, result, text = fail_
            test = self.get_empty_test()
            test.body = self._get_assert(result, text)
            return test, TestResult.FAILING
        else:
            _, result, text = fail2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(result, text)
            return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, pass2_, _, _ = self._generate_one()
        dice = random.randint(0, 1)
        if dice == 0:
            _, result, text = pass_
            test = self.get_empty_test()
            test.body = self._get_assert(result, text)
            return test, TestResult.PASSING
        else:
            _, result, text = pass2_
            test = self.get_empty_test()
            test.body = self._get_assert_2(result, text)
            return test, TestResult.PASSING


class TheFuckUnittestGenerator17(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck17_generate_)

    @staticmethod
    def _get_assert(
            result: Any,
            alias: Any
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="bash")],
                value=ast.Call(
                    func=ast.Name(id="Bash"),
                    args=[],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                    args=[
                        ast.Constant(value=result),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="bash"),
                                attr="app_alias",
                            ),
                            args=[ast.Constant(value=alias)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.shells.zsh",
                names=[ast.alias(name="Zsh")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.shells.bash",
                names=[ast.alias(name="Bash")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        result, alias = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(result, alias)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        result, alias = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(result, alias)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator18(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck18_generate_)

    @staticmethod
    def _get_assert(
            expected: str, script: str, std_out: str, std_err: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_err),
                                    ast.Constant(value=std_out),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.sudo",
                names=[ast.alias(name="match")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script, std_out, std_err = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, std_err, std_out)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script, std_out, std_err = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, std_err, std_out)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator19(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck19_generate_)

    @staticmethod
    def _get_assert(
            expected: str, script: str, std_out: str, std_err: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_assert_2(
            expected: str, script: str, std_out: str, std_err: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_push_force",
                names=[ast.alias(name="match")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_push_force",
                names=[ast.alias(name="get_new_command")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, _, fail_, fail2_ = self._generate_one()
        test = self.get_empty_test()
        dice = random.randint(0, 1)
        if dice == 0:
            expected, script, std_out, std_err = fail_
            test.body = self._get_assert(expected, script, std_out, std_err)
            return test, TestResult.FAILING

        else:
            expected, script, std_out, std_err = fail2_
            test.body = self._get_assert_2(expected, script, std_out, std_err)
            return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, pass2_, _, _ = self._generate_one()
        test = self.get_empty_test()
        dice = random.randint(0, 1)
        if dice == 0:
            expected, script, std_out, std_err = pass_
            test.body = self._get_assert(expected, script, std_out, std_err)
            return test, TestResult.PASSING

        else:
            expected, script, std_out, std_err = pass2_
            test.body = self._get_assert_2(expected, script, std_out, std_err)
            return test, TestResult.PASSING


class TheFuckUnittestGenerator20(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck20_generate_)

    @staticmethod
    def _get_assert(
            expected: str, script: str, std_out: str, std_err: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="_zip_file"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_err),
                                    ast.Constant(value=std_out),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_assert2(
            expected: str, script: str, std_out: str, std_err: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_err),
                                    ast.Constant(value=std_out),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.dirty_unzip",
                names=[ast.alias(name="_zip_file")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.dirty_unzip",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, _, fail_, fail2_ = self._generate_one()
        dice = random.randint(0, 1)
        if dice == 0:
            expected, script = fail_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, "", "")
            return test, TestResult.FAILING
        else:
            expected, script = fail2_
            test = self.get_empty_test()
            test.body = self._get_assert2(expected, script, "", "")
            return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, pass2_, _, _ = self._generate_one()
        dice = random.randint(0, 1)
        if dice == 0:
            expected, script = pass_
            test = self.get_empty_test()
            test.body = self._get_assert(expected, script, "", "")
            return test, TestResult.PASSING
        else:
            expected, script = pass2_
            test = self.get_empty_test()
            test.body = self._get_assert2(expected, script, "", "")
            return test, TestResult.PASSING


class TheFuckUnittestGenerator21(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck21_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.rules.git_fix_stash",
                names=[ast.alias(name="match")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        expected, script, std_out = fail_
        test.body = self._get_assert(expected, script, "", std_out)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        expected, script, std_out = pass_
        test.body = self._get_assert(expected, script, "", std_out)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator22(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck22_generate_)

    @staticmethod
    def _get_assert(
            expected: None,
            script1: str,
            side_effect1: None,
            priority1: Any,
            script2: str,
            side_effect2: None,
            priority2: Any,
            script3: str,
            side_effect3: None,
            priority3: Any,
            debug: dict,

    ) -> list[ast.Assign | ast.Expr]:
        command_calls = [
            ast.Call(
                func=ast.Name(id="CorrectedCommand"),
                args=[
                    ast.Constant(value=script1),
                    ast.Constant(value=side_effect1),
                    ast.Constant(value=priority1),
                ],
                keywords=[],
            ),
            ast.Call(
                func=ast.Name(id="CorrectedCommand"),
                args=[
                    ast.Constant(value=script2),
                    ast.Constant(value=side_effect2),
                    ast.Constant(value=priority2),
                ],
                keywords=[],
            ),
            ast.Call(
                func=ast.Name(id="CorrectedCommand"),
                args=[
                    ast.Constant(value=script3),
                    ast.Constant(value=side_effect3),
                    ast.Constant(value=priority3),
                ],
                keywords=[],
            )
        ]

        iter_command_call = ast.Call(
            func=ast.Name(id="iter"),
            args=[ast.List(elts=command_calls, ctx=ast.Load())],
            keywords=[],
        )

        args_list = [iter_command_call, ast.Call(
            func=ast.Name(id="Settings"),
            args=[
                ast.Constant(value=debug),
            ],
            keywords=[], )]

        return [
            ast.Assign(
                targets=[ast.Name(id="sort_corr_cmd_seq")],
                value=ast.Call(
                    func=ast.Name(id="SortedCorrectedCommandsSequence"),
                    args=args_list,
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="sort_corr_cmd_seq"),
                                attr="_realise",
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="SortedCorrectedCommandsSequence")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="CorrectedCommand")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script1, side_effect1, priority1, script2, side_effect2, priority2, script3, side_effect3, priority3 = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected,
                                     script1, side_effect1, priority1,
                                     script2, side_effect2, priority2,
                                     script3, side_effect3, priority3,
                                     {'key': 'val'})
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script1, side_effect1, priority1, script2, side_effect2, priority2, script3, side_effect3, priority3 = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected,
                                     script1, side_effect1, priority1,
                                     script2, side_effect2, priority2,
                                     script3, side_effect3, priority3,
                                     {'key': 'val'})
        return test, TestResult.PASSING


class TheFuckUnittestGenerator23(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck23_generate_)

    @staticmethod
    def _get_assert(
            shelve: Any,
            fn: Any,
            key: dict,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertIsNotNone"),
                args=[
                    ast.Call(
                        func=ast.Name(id="cache"),

                        args=[ast.Constant(value=shelve),
                              ast.Constant(value=fn),
                              ast.Constant(value=key)],
                        keywords=[],

                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_assert_2(
            shelve: Any,
            fn: Any,
            key: dict,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertIsNone"),
                args=[
                    ast.Call(
                        func=ast.Name(id="cache"),

                        args=[ast.Constant(value=shelve),
                              ast.Constant(value=fn),
                              ast.Constant(value=key)],
                        keywords=[],

                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.utils",
                names=[ast.alias(name="cache")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        shelve, fn, key = fail_
        test = self.get_empty_test()
        test.body = self._get_assert_2(shelve, fn, key)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        shelve, fn, key = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(shelve, fn, key)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator24(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck24_generate_)

    @staticmethod
    def _get_assert(
            # expected: str,
            rule_name: str,
            rule_match: Any,
            rule_get_new_command: Any,
            rule_enabled_by_default: Any,
            rule_side_effect: Any,
            rule_priority: Any,
            requires_output: Any,
            rules_name_list: list
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                args=[
                    ast.Call(
                        func=ast.Name(id="Rule"),
                        args=[ast.Constant(value=rule_name),
                              ast.Constant(value=rule_match),
                              ast.Constant(value=rule_get_new_command),
                              ast.Constant(value=rule_enabled_by_default),
                              ast.Constant(value=rule_side_effect),
                              ast.Constant(value=rule_priority),
                              ast.Constant(value=requires_output)],
                        keywords=[],
                    ), ast.Call(
                        func=ast.Name(id="RulesNamesList"),
                        args=[ast.Constant(value=rules_name_list)],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="RulesNamesList")],
                level=0,
            ),

            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Rule")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        rule, rules = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(rule, "", "", "", "", "", "", rules)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        rule, rules = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(rule, "", "", "", "", "", "", rules)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator25(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck25_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.mkdir_p",
                names=[ast.alias(name="get_new_command")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.PASSING


class TheFuckUnittestGenerator26(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck26_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.vagrant_up",
                names=[ast.alias(name="get_new_command")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script, std_err = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", std_err)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script, std_err = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", std_err)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator27(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck27_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.open",
                names=[ast.alias(name="get_new_command")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.PASSING


class TheFuckUnittestGenerator28(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck28_generate_)

    @staticmethod
    def _get_assert(
            expected: bool,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_assert_2(
            expected: bool,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.fix_file",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.fix_file",
                names=[ast.alias(name="match")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        _, script, out, error = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(True, script, out, error)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        _, script, out, error = pass_
        test = self.get_empty_test()
        test.body = self._get_assert_2(False, script, out, error)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator29(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck29_generate_)

    @staticmethod
    def _get_assert(
            expected: Any,
            sett: Any,
    ) -> list[Assign | Expr]:
        return [
            ast.Assign(
                targets=[ast.Name(id="settings")],
                value=ast.Call(
                    func=ast.Name(id="Settings"),
                    args=[ast.Constant(value=sett)],
                    keywords=[],
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id="new_settings")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="settings"),
                        attr="update",
                    ),
                    args=[
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Name(id="new_settings"),
                    ],
                    keywords=[],
                ),
                lineno=3,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(fail_, fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_, pass_)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator30(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck30_generate_)

    @staticmethod
    def _get_assert(
            expected: bool,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.fix_file",
                names=[ast.alias(name="match")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        scr, err, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(False, scr, "", err)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        scr, err, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(True, scr, "", err)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator31(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck31_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="get_new_command"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.git_diff_staged",
                names=[ast.alias(name="get_new_command")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.PASSING


class TheFuckUnittestGenerator32(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.thefuck32_generate_)

    @staticmethod
    def _get_assert(
            expected: str,
            script: str,
            std_out: str,
            std_err: str,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=expected),
                    ast.Call(
                        func=ast.Name(id="match"),
                        args=[
                            ast.Call(
                                func=ast.Name(id="Command"),
                                args=[
                                    ast.Constant(value=script),
                                    ast.Constant(value=std_out),
                                    ast.Constant(value=std_err),
                                ],
                                keywords=[],
                            ),
                            ast.Call(
                                func=ast.Name(id="Settings"),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.ls_lah",
                names=[ast.alias(name="match")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        expected, script = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        expected, script = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(expected, script, "", "")
        return test, TestResult.PASSING


class TheFuckSystemtestGenerator1(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck1_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck1_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator2(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck2_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck2_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator3(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fail_ = self.generate_values(self.thefuck3_generate_)
        if fail_[0:4] == "Fish":
            fail_ = "Error Retrieving Shell"
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_ = self.generate_values(self.thefuck3_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator4(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _ = self.generate_values(self.thefuck4_generate_)
        fail_ = "Error"
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_ = self.generate_values(self.thefuck4_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator5(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck5_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck5_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator6(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, _, fail_, fail2_ = self.generate_values(self.thefuck6_generate_)
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            return f"{fail_}", TestResult.FAILING
        else:
            return f"{fail2_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, pass2_, _, _ = self.generate_values(self.thefuck6_generate_)
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            return f"{pass_}", TestResult.PASSING
        else:
            return f"{pass2_}", TestResult.PASSING


class TheFuckSystemtestGenerator7(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck7_generate_)
        return f"True {fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck7_generate_)
        return f"True {pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator8(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, _, _, expected, script, output = self.generate_values(self.thefuck8_generate_)
        fail_ = expected, script, output
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        expected, script, output, _, _, _ = self.generate_values(self.thefuck8_generate_)
        pass_ = expected, script, output
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator9(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck9_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck9_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator10(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck10_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck10_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator11(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck11_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck11_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator12(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck12_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck12_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator13(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, _, fail_, fail2_ = self.generate_values(self.thefuck13_generate_)
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            return f"{fail_}", TestResult.FAILING
        else:
            return f"{fail2_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, pass2_, _, _ = self.generate_values(self.thefuck13_generate_)
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            return f"{pass_}", TestResult.PASSING
        else:
            return f"{pass2_}", TestResult.PASSING


class TheFuckSystemtestGenerator14(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fail_ = "Error Retrieving Fish Shell Overridden"
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_ = self.generate_values(self.thefuck14_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator15(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, _, fail_, fail2_ = self.generate_values(self.thefuck15_generate_)
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            return f"{fail_}", TestResult.FAILING
        else:
            return f"{fail2_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, pass2_, _, _ = self.generate_values(self.thefuck15_generate_)
        dice_ = random.randint(0, 1)
        if dice_ == 0:
            return f"{pass_}", TestResult.PASSING
        else:
            return f"{pass2_}", TestResult.PASSING


class TheFuckSystemtestGenerator16(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, _, fail_, fail2_ = self.generate_values(self.thefuck16_generate_)
        dice = random.randint(0, 1)
        if dice == 0:
            return f"{fail_}", TestResult.FAILING
        else:
            return f"{fail2_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, pass2_, _, _ = self.generate_values(self.thefuck16_generate_)
        dice = random.randint(0, 1)
        if dice == 0:
            return f"{pass_}", TestResult.PASSING
        else:
            return f"{pass2_}", TestResult.PASSING


class TheFuckSystemtestGenerator17(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck17_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck17_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator18(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck18_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck18_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator19(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, _, fail_, fail2_ = self.generate_values(self.thefuck19_generate_)
        dice = random.randint(0, 1)
        if dice == 0:
            return f"{fail_}", TestResult.FAILING
        else:
            return f"{fail2_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, pass2_, _, _ = self.generate_values(self.thefuck19_generate_)
        dice = random.randint(0, 1)
        if dice == 0:
            return f"{pass_}", TestResult.PASSING
        else:
            return f"{pass2_}", TestResult.PASSING


class TheFuckSystemtestGenerator20(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, _, fail_, fail2_ = self.generate_values(self.thefuck20_generate_)
        dice = random.randint(0, 1)
        if dice == 0:
            return f"{fail_}", TestResult.FAILING
        else:
            return f"{fail2_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, pass2_, _, _ = self.generate_values(self.thefuck20_generate_)
        dice = random.randint(0, 1)
        if dice == 0:
            return f"{pass_}", TestResult.PASSING
        else:
            return f"{pass2_}", TestResult.PASSING


class TheFuckSystemtestGenerator21(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck21_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck21_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator22(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck22_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck22_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator23(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck23_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck23_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator24(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck24_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck24_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator25(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck25_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck25_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator26(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck26_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck26_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator27(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck27_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck27_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator28(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck28_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck28_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator29(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck29_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck29_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator30(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fail_script, fail_error, _ = self.generate_values(self.thefuck30_generate_)
        fail_ = fail_script, fail_error, True
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_script, pass_error, _ = self.generate_values(self.thefuck30_generate_)
        pass_ = pass_script, pass_error, False
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator31(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck31_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck31_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator32(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck32_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck32_generate_)
        return f"{pass_}", TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<structure_>"],
    "<structure_>": ["<str_int_sym_><structure_>"],
    "<str_int_sym_>": [
        "<string_><str_int_sym_>",
        "<integer_><str_int_sym_>",
        "<symbols_><str_int_sym_>",
        "",
    ],
    "<string_>": ["<char_><string_>", "<char_>", " "],
    "<integer_>": ["<digit_><integer_>", "<digit_>", " "],
    "<symbols_>": ["<symbol_><symbols_>", "<symbol_>", " "],
    "<symbol_>": srange(string.punctuation),
    "<digit_>": srange(string.digits),
    "<char_>": srange(string.ascii_letters),
}
assert is_valid_grammar(grammar)
