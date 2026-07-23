import ast
import os
import random
import string
import subprocess
from _ast import Call, ImportFrom, Assign, Expr
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "thefuck"


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
        skip_tests: Optional[List[str]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/nvbn/thefuck",
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
            test_base=Path(PROJECT_NAME, "tests"),
            included_files=[PROJECT_NAME],
            excluded_files=[os.path.join(PROJECT_NAME, "tests")],
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
            ],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )


def register():
    TheFuck(
        bug_id=1,
        buggy_commit_id="2ced7a7f33ae0bec3ffc7a43ce95330bdf6cfcb9",
        fixed_commit_id="444908ce1c17767ef4aaf9e0b4950497914f7f63",
        test_files=[Path("tests", "rules", "test_pip_unknown_command.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_pip_unknown_command.py::test_get_new_command"
                "[pip un+install thefuck-un+install-uninstall-pip uninstall thefuck]",
            )
        ],
        api=TheFuckAPI1(),
        unittests=TheFuckUnittestGenerator1(),
        systemtests=TheFuckSystemtestGenerator1(),
        loc=4249,
    )
    TheFuck(
        bug_id=2,
        buggy_commit_id="40ab4eb62db57627bff10cf029d29c94704086a2",
        fixed_commit_id="78ef9eec88f43d5727986be2237f6e0e250cbbbc",
        test_files=[Path("tests", "test_utils.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils.py::test_get_all_executables_pathsep"
                "[C:\\\\\\\\foo;C:\\\\\\\\bar;C:\\\\\\\\baz;C:\\\\\\\\foo\\\\\\\\bar-;]",
            )
        ],
        api=TheFuckAPI2(),
        unittests=TheFuckUnittestGenerator2(),
        systemtests=TheFuckSystemtestGenerator2(),
        loc=4028,
    )
    TheFuck(
        bug_id=3,
        buggy_commit_id="ac343fb1bd7dadbb9e1a9fd7e3071f5778e338a4",
        fixed_commit_id="ce5feaebf7fd5c1190b5e14fbc1e962cc8db5f39",
        test_files=[Path("tests", "shells", "test_fish.py")],
        test_cases=[
            os.path.join("tests", "shells", "test_fish.py::TestFish::test_info")
        ],
        api=TheFuckAPI3(),
        unittests=TheFuckUnittestGenerator3(),
        systemtests=TheFuckSystemtestGenerator3(),
        loc=3982,
    )
    TheFuck(
        bug_id=4,
        buggy_commit_id="68949a592248913b52bfd50036893553153fcddb",
        fixed_commit_id="8db3cf604865e559090412ce80b0640e290ad83a",
        test_files=[Path("tests", "shells", "test_fish.py")],
        test_cases=[
            os.path.join("tests", "shells", "test_fish.py::TestFish::test_get_aliases"),
            os.path.join(
                "tests",
                "shells",
                'test_fish.py::TestFish::test_from_shell[fuck-fish -ic "fuck"]',
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[find-find]"
            ),
            os.path.join(
                "tests",
                "shells",
                'test_fish.py::TestFish::test_from_shell[funced-fish -ic "funced"]',
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[cd-cd]"
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[grep-grep]"
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[man-man]"
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[pwd-pwd]"
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[vim-vim]"
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[ls-ls]"
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[g-git]"
            ),
            os.path.join(
                "tests",
                "shells",
                "test_fish.py::TestFish::test_from_shell"
                '[math "2 + 2"-fish -ic "math \\\\"2 + 2\\\\""]',
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[open-open]"
            ),
            os.path.join(
                "tests", "shells", "test_fish.py::TestFish::test_from_shell[awk-awk]"
            ),
            os.path.join(
                "tests",
                "shells",
                'test_fish.py::TestFish::test_from_shell[ll-fish -ic "ll"]',
            ),
        ],
        api=TheFuckAPI4(),
        unittests=TheFuckUnittestGenerator4(),
        systemtests=TheFuckSystemtestGenerator4(),
        loc=3834,
    )
    TheFuck(
        bug_id=5,
        buggy_commit_id="7c858fadb3458be829d3d43666ccb46c3ed5b8a0",
        fixed_commit_id="c205683a8df8a57e2db1e9816a5a7ce3255b08fc",
        test_files=[Path("tests", "rules", "test_git_push.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_git_push.py::test_match_bitbucket",
            )
        ],
        api=TheFuckAPI5(),
        unittests=TheFuckUnittestGenerator5(),
        systemtests=TheFuckSystemtestGenerator5(),
        loc=3791,
    )
    TheFuck(
        bug_id=6,
        buggy_commit_id="797ca1c5647c565f62e21a8e29515c8b0fbe275f",
        fixed_commit_id="7c858fadb3458be829d3d43666ccb46c3ed5b8a0",
        test_files=[Path("tests", "rules", "test_git_branch_exists.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_git_branch_exists.py::test_get_new_command"
                "[git checkout -b \"let's-push-this\"-let's-push-this-let\\\\'s-push-this]",
            )
        ],
        api=TheFuckAPI6(),
        unittests=TheFuckUnittestGenerator6(),
        systemtests=TheFuckSystemtestGenerator6(),
        loc=3790,
    )
    TheFuck(
        bug_id=7,
        buggy_commit_id="64d6835e15a22cf8803d398cbb593f748c550e8a",
        fixed_commit_id="75d2c43997ca703150cbdb4c46ed7b2e2e71fd11",
        test_files=[Path("tests", "rules", "test_php_s.py")],
        test_cases=[
            os.path.join("tests", "rules", "test_php_s.py::test_match[command1]")
        ],
        api=TheFuckAPI7(),
        unittests=TheFuckUnittestGenerator7(),
        systemtests=TheFuckSystemtestGenerator7(),
        loc=3658,
    )
    TheFuck(
        bug_id=8,
        buggy_commit_id="449cb9a00693c8b4d97d5fda8d732cf0978e117e",
        fixed_commit_id="be48f027847161f907def8987706041c65a1fd58",
        test_files=[Path("tests", "rules", "test_dnf_no_such_command.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_dnf_no_such_command.py::test_get_new_command"
                "[dnf isntall vim-No such command: isntall. Please use /usr/bin/dnf --help\\n"
                "It could be a DNF plugin command, try: \"dnf install 'dnf-command(isntall)'\"\\n"
                "-dnf install vim]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_dnf_no_such_command.py::test_get_new_command"
                "[dnf saerch vim-No such command: saerch. Please use /usr/bin/dnf --help\\n"
                "It could be a DNF plugin command, try: \"dnf install 'dnf-command(saerch)'\"\\n"
                "-dnf search vim]",
            ),
            os.path.join(
                "tests", "rules", "test_dnf_no_such_command.py::test_get_operations"
            ),
        ],
        api=TheFuckAPI8(),
        unittests=TheFuckUnittestGenerator8(),
        systemtests=TheFuckSystemtestGenerator8(),
        loc=3523,
    )
    TheFuck(
        bug_id=9,
        buggy_commit_id="ce6b82c92d78ae283cb3db001766b76f6647bc47",
        fixed_commit_id="feb36ede5c518fdc3b6eddf945b2d8b1e2294d15",
        test_files=[Path("tests", "rules", "test_git_push.py")],
        test_cases=[
            os.path.join("tests", "rules", "test_git_push.py::test_get_new_command")
        ],
        api=TheFuckAPI9(),
        unittests=TheFuckUnittestGenerator9(),
        systemtests=TheFuckSystemtestGenerator9(),
        loc=2735,
    )
    TheFuck(
        bug_id=10,
        buggy_commit_id="8bd6c5da67e55c64257345efa4e3cc454c42475c",
        fixed_commit_id="0c84eefa55fc1b4bc4940b41d74568884344e35c",
        test_files=[Path("tests", "rules", "test_man.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_man.py::test_get_new_command[command0-new_command0]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_man.py::test_get_new_command[command1-new_command1]",
            ),
        ],
        api=TheFuckAPI10(),
        unittests=TheFuckUnittestGenerator10(),
        systemtests=TheFuckSystemtestGenerator10(),
        loc=2727,
    )
    TheFuck(
        bug_id=11,
        buggy_commit_id="92f3c8fb52b32b79005b4864c31a5c2d8c45f4b1",
        fixed_commit_id="db7dffdb44ae5c7be8de088765463fbda96197d1",
        test_files=[Path("tests", "rules", "test_git_push.py")],
        test_cases=[
            os.path.join("tests", "rules", "test_git_push.py::test_get_new_command")
        ],
        # fixed_commit_id db7dffdb... is a MERGE commit whose first parent is the
        # buggy commit 92f3c8fb...; the merge-aware checkout (git diff buggy..fixed)
        # now overlays the source fix so the "fixed" build genuinely differs.
        api=TheFuckAPI11(),
        unittests=TheFuckUnittestGenerator11(),
        systemtests=TheFuckSystemtestGenerator11(),
        loc=2710,
    )
    TheFuck(
        bug_id=12,
        buggy_commit_id="4c2fc490f280ca3921785d8f58a37274ced35ce6",
        fixed_commit_id="ca787a1cba3cc9b26b43919c5e60acb40ebcd919",
        test_files=[Path("tests", "rules", "test_no_command.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_no_command.py::test_not_match[vim file.py-vim: not found-vim]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_no_command.py::test_not_match[qweqwe-qweqwe: not found-None]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_no_command.py::test_not_match[vom file.py-some text-None]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_no_command.py::test_match[fucck-fucck: not found]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_no_command.py::test_match[got commit-got: command not found]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_no_command.py::test_match[vom file.py-vom: not found]",
            ),
        ],
        api=TheFuckAPI12(),
        unittests=TheFuckUnittestGenerator12(),
        systemtests=TheFuckSystemtestGenerator12(),
        loc=2452,
    )
    TheFuck(
        bug_id=13,
        buggy_commit_id="2af65071d84a7d1d14a4126364d9b4c9b5241f3c",
        fixed_commit_id="237bc579994de633fe104714156ddfa925a50b6e",
        test_files=[Path("tests", "rules", "test_git_branch_exists.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_git_branch_exists.py::test_match[git checkout bar-bar]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_git_branch_exists.py::test_get_new_command[git branch foo-foo]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_git_branch_exists.py::test_get_new_command[git checkout bar-bar]",
            ),
        ],
        api=TheFuckAPI13(),
        unittests=TheFuckUnittestGenerator13(),
        systemtests=TheFuckSystemtestGenerator13(),
        loc=2431,
    )
    TheFuck(
        bug_id=14,
        buggy_commit_id="183b70c8b8885843efefd2bd4e74dc0a7d42d173",
        fixed_commit_id="db6053b301e2b3f4363401e457b5dc4ad2e8429b",
        test_files=[Path("tests", "shells", "test_fish.py")],
        test_cases=[
            os.path.join(
                "tests",
                "shells",
                "test_fish.py::TestFish::test_get_overridden_aliases[\\ncut,\\n\\ngit,\\tsed\\r]",
            ),
            os.path.join(
                "tests",
                "shells",
                "test_fish.py::TestFish::test_get_overridden_aliases[cut, git, sed]",
            ),
            os.path.join(
                "tests",
                "shells",
                "test_fish.py::TestFish::test_get_overridden_aliases[cut,git,sed]",
            ),
            os.path.join(
                "tests",
                "shells",
                "test_fish.py::TestFish::test_get_overridden_aliases[ cut,\\tgit,sed\\n]",
            ),
        ],
        api=TheFuckAPI14(),
        unittests=TheFuckUnittestGenerator14(),
        systemtests=TheFuckSystemtestGenerator14(),
        loc=2348,
    )
    TheFuck(
        bug_id=15,
        buggy_commit_id="3a39deb485995e67afb1919972cd1c9aaedf4c32",
        fixed_commit_id="41707b80c61acadb7c87b0efcbf10f4186dc5937",
        test_files=[Path("tests", "rules", "test_git_add.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_git_add.py::test_match[git submodule update unknown-unknown]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_git_add.py::test_match[git commit unknown-unknown]",
            ),
        ],
        api=TheFuckAPI15(),
        unittests=TheFuckUnittestGenerator15(),
        systemtests=TheFuckSystemtestGenerator15(),
        loc=2328,
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
            os.path.join(
                "tests",
                "shells",
                "test_bash.py::TestBash::test_app_alias_variables_correctly_set",
            ),
            os.path.join(
                "tests",
                "shells",
                "test_zsh.py::TestZsh::test_app_alias_variables_correctly_set",
            ),
        ],
        api=TheFuckAPI16(),
        unittests=TheFuckUnittestGenerator16(),
        systemtests=TheFuckSystemtestGenerator16(),
        loc=2269,
    )
    TheFuck(
        bug_id=17,
        buggy_commit_id="f7f0660114a02fe49578ec5684dd02c81042d175",
        fixed_commit_id="7ce4307c87c1e2e4106db2c961e48e249be987be",
        test_files=[Path("tests", "shells", "test_bash.py")],
        test_cases=[
            os.path.join("tests", "shells", "test_bash.py::TestBash::test_get_aliases"),
            os.path.join(
                "tests",
                "shells",
                "test_bash.py::TestBash::test_from_shell[fuck-eval $(thefuck $(fc -ln -1))]",
            ),
            os.path.join(
                "tests", "shells", "test_bash.py::TestBash::test_from_shell[ll-ls -alF]"
            ),
        ],
        api=TheFuckAPI17(),
        unittests=TheFuckUnittestGenerator17(),
        systemtests=TheFuckSystemtestGenerator17(),
        loc=2256,
    )
    TheFuck(
        bug_id=18,
        buggy_commit_id="b65a9a0a4fd9bef394b45a1d367d29aa1e1c403e",
        fixed_commit_id="c3b1ba763708b8faaaf55717c436c4cd4c57a7ea",
        test_files=[Path("tests", "rules", "test_sudo.py")],
        test_cases=[os.path.join("tests", "rules", "test_sudo.py::test_not_match")],
        api=TheFuckAPI18(),
        unittests=TheFuckUnittestGenerator18(),
        systemtests=TheFuckSystemtestGenerator18(),
        loc=2123,
    )
    TheFuck(
        bug_id=19,
        buggy_commit_id="959b96cf6ec8cedda05dc58efe0e0f3bd6ed2f4e",
        fixed_commit_id="dc23d67a42dad54308a753639edd1ea0d15cb2e7",
        test_files=[Path("tests", "rules", "test_git_push_force.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_git_push_force.py::test_get_new_command"
                "[command2-git push --force-with-lease nvbn master]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_git_push_force.py::test_get_new_command"
                "[command1-git push --force-with-lease nvbn]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_git_push_force.py::test_get_new_command"
                "[command0-git push --force-with-lease]",
            ),
        ],
        api=TheFuckAPI19(),
        unittests=TheFuckUnittestGenerator19(),
        systemtests=TheFuckSystemtestGenerator19(),
        loc=2047,
    )
    TheFuck(
        bug_id=20,
        buggy_commit_id="0a6a3db65d2fc480c5b2f1135137f34c9f06b742",
        fixed_commit_id="280751b36e715b006c631ba6c08de99ccc74f6d2",
        test_files=[Path("tests", "rules", "test_dirty_unzip.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_dirty_unzip.py::test_get_new_command"
                "[unzip foo\\\\ bar.zip-unzip foo\\\\ bar.zip -d 'foo bar']",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_dirty_unzip.py::test_get_new_command"
                "[unzip 'foo bar.zip'-unzip 'foo bar.zip' -d 'foo bar']",
            ),
        ],
        api=TheFuckAPI20(),
        unittests=TheFuckUnittestGenerator20(),
        systemtests=TheFuckSystemtestGenerator20(),
        loc=2034,
    )
    TheFuck(
        bug_id=21,
        buggy_commit_id="71dc2666ccf62e653291d9a7a08e2c6c3320425b",
        fixed_commit_id="213791d3c2af379ffa37a140735998736b41912e",
        test_files=[Path("tests", "rules", "test_git_fix_stash.py")],
        test_cases=[
            os.path.join("tests", "rules", "test_git_fix_stash.py::test_not_match")
        ],
        api=TheFuckAPI21(),
        unittests=TheFuckUnittestGenerator21(),
        systemtests=TheFuckSystemtestGenerator21(),
        loc=1980,
    )
    TheFuck(
        bug_id=22,
        buggy_commit_id="faa7ee603057fa98c25507d30180c055d10d13d4",
        fixed_commit_id="e2e8b6fc865452b4cfc1bed70e5b9b49807258ae",
        test_files=[Path("tests", "test_types.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_types.py::TestSortedCorrectedCommandsSequence::test_with_blank",
            )
        ],
        api=TheFuckAPI22(),
        unittests=TheFuckUnittestGenerator22(),
        systemtests=TheFuckSystemtestGenerator22(),
        loc=1871,
    )
    TheFuck(
        bug_id=23,
        buggy_commit_id="4129ff2717cc6e6fa51d70cc4e6c31d56ef8e2c9",
        fixed_commit_id="9a02e821cdc58a4aba2c0acc521fb25cacab87a5",
        test_files=[Path("tests", "test_utils.py")],
        test_cases=[
            os.path.join("tests", "test_utils.py::TestCache::test_when_etag_changed"),
            os.path.join("tests", "test_utils.py::TestCache::test_with_filled_cache"),
            os.path.join("tests", "test_utils.py::TestCache::test_with_blank_cache"),
        ],
        skip_tests=["test_get_all_callables"],
        api=TheFuckAPI23(),
        unittests=TheFuckUnittestGenerator23(),
        systemtests=TheFuckSystemtestGenerator23(),
        loc=1870,
    )
    TheFuck(
        bug_id=24,
        buggy_commit_id="12394ca8423a438915fed996383b44471fc1139d",
        fixed_commit_id="5d74344994da89ed01afd448f1c9d86b85e85351",
        test_files=[Path("tests", "test_types.py")],
        test_cases=[
            os.path.join("tests", "test_types.py::TestCorrectedCommand::test_equality"),
            os.path.join("tests", "test_types.py::TestCorrectedCommand::test_hashable"),
        ],
        api=TheFuckAPI24(),
        unittests=TheFuckUnittestGenerator24(),
        systemtests=TheFuckSystemtestGenerator24(),
        loc=1852,
    )
    TheFuck(
        bug_id=25,
        buggy_commit_id="42a8b4f639269886e468762e6d100b6f01aad8ab",
        fixed_commit_id="298c04f89c081dc16c8653aa017ca85dd14bfad6",
        test_files=[Path("tests", "rules", "test_mkdir_p.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_mkdir_p.py::test_get_new_command[command2-./bin/hdfs dfs -mkdir -p foo/bar/baz]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_mkdir_p.py::test_get_new_command[command1-hdfs dfs -mkdir -p foo/bar/baz]",
            ),
        ],
        api=TheFuckAPI25(),
        unittests=TheFuckUnittestGenerator25(),
        systemtests=TheFuckSystemtestGenerator25(),
        loc=1716,
    )
    TheFuck(
        bug_id=26,
        buggy_commit_id="7cb0388ed0845545e878b29783bbf8e901a02745",
        fixed_commit_id="feb3eee2a08f0cba4552373d728509bc90b561ab",
        test_files=[Path("tests", "rules", "test_vagrant_up.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_vagrant_up.py::test_get_new_command[command3-new_command3]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_vagrant_up.py::test_get_new_command[command0-vagrant up && vagrant ssh]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_vagrant_up.py::test_get_new_command[command1-new_command1]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_vagrant_up.py::test_get_new_command[command2-vagrant up && vagrant rdp]",
            ),
        ],
        api=TheFuckAPI26(),
        unittests=TheFuckUnittestGenerator26(),
        systemtests=TheFuckSystemtestGenerator26(),
        loc=1722,
    )
    # noinspection HttpUrlsUsage
    TheFuck(
        bug_id=27,
        buggy_commit_id="bc6b107066d3f1e60b4cfcaa8cf6399e98cf1b1c",
        fixed_commit_id="1becd92b126a368d6e7d93aa8eea209414ce4aa2",
        test_files=[Path("tests", "rules", "test_open.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_open.py::test_get_new_command[command6-xdg-open http://foo.io]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_open.py::test_get_new_command[command7-gnome-open http://foo.io]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_open.py::test_get_new_command[command8-kde-open http://foo.io]",
            ),
        ],
        api=TheFuckAPI27(),
        unittests=TheFuckUnittestGenerator27(),
        systemtests=TheFuckSystemtestGenerator27(),
        loc=1705,
    )
    TheFuck(
        bug_id=28,
        buggy_commit_id="88831c424f569e6a55fc98883d3eeecc7d425b18",
        fixed_commit_id="9b30ae0424607a4e268bd26eaee8ccb91a5588f9",
        test_files=[Path("tests", "rules", "test_fix_file.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test0]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test1]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test7]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test8]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test15]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test16]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test19]",
            ),
            os.path.join(
                "tests",
                "rules",
                "test_fix_file.py::test_get_new_command_with_settings[test20]",
            ),
        ],
        api=TheFuckAPI28(),
        unittests=TheFuckUnittestGenerator28(),
        systemtests=TheFuckSystemtestGenerator28(),
        loc=1697,
    )
    TheFuck(
        bug_id=29,
        buggy_commit_id="4a2f869c6d6ef03d8d7ada1121cc6631d7ef979e",
        fixed_commit_id="88831c424f569e6a55fc98883d3eeecc7d425b18",
        test_files=[Path("tests", "test_types.py"), Path("tests", "test_utils.py")],
        test_cases=[
            os.path.join("tests", "test_types.py::test_update_settings"),
            os.path.join(
                "tests", "test_utils.py::test_wrap_settings[override2-old2-new2]"
            ),
            os.path.join(
                "tests", "test_utils.py::test_wrap_settings[override1-old1-new1]"
            ),
        ],
        skip_tests=["test_get_all_callables"],
        api=TheFuckAPI29(),
        unittests=TheFuckUnittestGenerator29(),
        systemtests=TheFuckSystemtestGenerator29(),
        loc=1697,
    )
    TheFuck(
        bug_id=30,
        buggy_commit_id="de513cacb150049e3f95434f8d6d30b7ed1e0ea7",
        fixed_commit_id="43fead02d3a24fef71534116c5550def0f56830c",
        test_files=[Path("tests", "rules", "test_fix_file.py")],
        test_cases=[
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test1]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test4]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test15]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test19]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test13]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test7]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test14]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test17]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test18]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test11]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test3]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test9]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test6]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test8]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test12]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test16]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test5]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test10]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test2]"),
            os.path.join("tests", "rules", "test_fix_file.py::test_not_file[test0]"),
        ],
        api=TheFuckAPI30(),
        unittests=TheFuckUnittestGenerator30(),
        systemtests=TheFuckSystemtestGenerator30(),
        loc=1545,
    )
    TheFuck(
        bug_id=31,
        buggy_commit_id="66e2ec7e3f0d3f848c01d87bb3503b0ff90fc78a",
        fixed_commit_id="1285303363bc420bd7606bd5f808e3f2b4f0e83f",
        test_files=[Path("tests", "rules", "test_git_diff_staged.py")],
        test_cases=[
            os.path.join(
                "tests",
                "rules",
                "test_git_diff_staged.py::test_get_new_command[command1-git diff --staged foo]",
            )
        ],
        api=TheFuckAPI31(),
        unittests=TheFuckUnittestGenerator31(),
        systemtests=TheFuckSystemtestGenerator31(),
        loc=1336,
    )
    TheFuck(
        bug_id=32,
        buggy_commit_id="cb33c912e5f2f4c2da6b70d708ff0437bfcd3b94",
        fixed_commit_id="25cc98a21a3450a046caf418f08713c82a290805",
        test_files=[Path("tests", "rules", "test_ls_lah.py")],
        test_cases=[os.path.join("tests", "rules", "test_ls_lah.py::test_match")],
        api=TheFuckAPI32(),
        unittests=TheFuckUnittestGenerator32(),
        systemtests=TheFuckSystemtestGenerator32(),
        loc=1067,
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
        # The first serialized token is the expected Fish().info() string
        # ("Fish Shell <ver>", the fixed-build result). The buggy build emits the
        # raw echo output instead, so a mismatched raw_echo yields a FAILING.
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
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
        # The first serialized token is the expected (fixed-build) output; the
        # harness prints the space-joined parsed operations (fixed) or crashes
        # with a TypeError (buggy) for "parse" tests, and prints match()'s bool
        # for the invariant "match" tests.
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
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
        # The first serialized token is the expected len(get_new_command(...)):
        # "1" for the fixed "No manual entry" special case (buggy still returns
        # 3), "3" for the invariant digit-less path.
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
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
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class TheFuckAPI23(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        # The first serialized token is the cached value the harness prints. In
        # "nocm" mode the buggy build crashes (no output) while the fixed build
        # prints the value; in "cm" mode both builds print the value.
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
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
        # The first serialized token is the expected isinstance(result, list)
        # boolean the harness prints ("True" when the fixed build returns a list
        # of suggestions for a machine-scoped command, "False" otherwise).
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
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
        # The first serialized token is the expected "COLMARKER in output"
        # boolean: "True" when the fixed build honours the fixcolcmd setting
        # (buggy ignores it -> "False"), "False" when no fixcolcmd is supplied.
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8").strip()
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
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
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


# noinspection HttpUrlsUsage
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
                f'ERROR: unknown command "{pip_failing_inputs[randomise_int]}", '
                f'maybe you meant "{pip_commands[randomise_int]}"',
            ),
            (
                f"pip {pip_commands[randomise_int]} {randomise_string}",
                f"pip {pip_failing_inputs_2[randomise_int]} {randomise_string}",
                f'ERROR: unknown command "{pip_failing_inputs_2[randomise_int]}", '
                f'maybe you meant "{pip_commands[randomise_int]}"',
            ),
        )

        passing = (
            (
                f"pip {pip_commands[randomise_int]} {randomise_string}",
                f"pip {pip_passing_inputs[randomise_int]} {randomise_string}",
                f'ERROR: unknown command "{pip_passing_inputs[randomise_int]}", '
                f'maybe you meant "{pip_commands[randomise_int]}"',
            ),
            (
                f"pip {pip_commands[randomise_int]} {randomise_string}",
                f"pip {pip_passing_inputs_2[randomise_int]} {randomise_string}",
                f'ERROR: unknown command "{pip_passing_inputs_2[randomise_int]}", '
                f'maybe you meant "{pip_commands[randomise_int]}"',
            ),
        )
        return (
            passing[random.randint(0, len(passing) - 1)],
            failing[random.randint(0, len(failing) - 1)],
        )

    @staticmethod
    def thefuck2_generate_():
        # Collect real executable names from system directories that are always
        # present on ``PATH`` (so they are also visible to the built subject's
        # ``get_all_executables``, regardless of which venv the generator runs
        # in). Names are restricted to simple characters so they survive the
        # shell-style argument splitting used by the harness.
        safe_chars = set(string.ascii_letters + string.digits + "_-.")
        executables = []
        for path_dir in ("/usr/bin", "/bin", "/usr/sbin", "/sbin"):
            if not os.path.isdir(path_dir):
                continue
            try:
                for filename in os.listdir(path_dir):
                    if (
                        filename
                        and filename not in ("thefuck", "fuck")
                        and all(c in safe_chars for c in filename)
                    ):
                        executables.append(filename)
            except OSError:
                continue
        if not executables:
            executables = ["ls", "cat", "echo", "env", "cp", "mv", "rm", "date"]
        passing = random.choice(executables)
        # A random mixed string that is not a substring of any executable name.
        failing = "Zq9" + "".join(
            random.choices(string.ascii_letters + string.digits, k=random.randint(8, 16))
        )
        return passing, failing

    @staticmethod
    def thefuck3_generate_():
        # fish.info() reads the version differently on each build: buggy runs
        # `echo $FISH_VERSION` and strips, fixed runs `fish --version` and takes
        # the last whitespace token. Via a Popen monkeypatch the harness feeds
        # raw_echo to the buggy form and "fish, version <ver>" to the fixed form.
        # FAILING: raw_echo ("e...") != ver ("v...") -> buggy differs from the
        # expected "Fish Shell <ver>". PASSING: raw_echo == ver -> both agree.
        raw_echo = "e" + TheFuckTestGenerator.generate_random_string()
        ver = "v" + TheFuckTestGenerator.generate_random_string()
        failing = f"'Fish Shell {ver}' '{raw_echo}' '{ver}'"
        same = TheFuckTestGenerator.generate_random_string()
        passing = f"'Fish Shell {same}' '{same}' '{same}'"
        return passing, failing

    @staticmethod
    def thefuck4_generate_():
        # fish._get_aliases parses a canned `alias` line (injected via a Popen
        # monkeypatch in the harness). FAILING: an ``alias name=value`` line
        # (fish '=' form) makes the buggy single-separator parser raise ("ERR")
        # while the fixed multi-separator parser succeeds ("OK"); expected "OK".
        # PASSING: an ``alias name value`` line parses identically on both.
        name = TheFuckTestGenerator.generate_random_string()
        value = TheFuckTestGenerator.generate_random_string()
        failing = f"'OK' 'alias {name}={value}'"
        name2 = TheFuckTestGenerator.generate_random_string()
        value2 = TheFuckTestGenerator.generate_random_string()
        passing = f"'OK' 'alias {name2} {value2}'"
        return passing, failing

    @staticmethod
    def thefuck5_generate_():
        randomise_branch_name = TheFuckTestGenerator.generate_random_string()
        passing = (
            (
                True,
                f"git push --set-upstream <remote> <{randomise_branch_name}>",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current "
                f"branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
            ),
            (
                False,
                f"git pull --set-upstream <remote> <{randomise_branch_name}>",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current "
                f"branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
            ),
        )

        failing = (
            (
                True,
                f"git pushpull --set-upstream <remote> <{randomise_branch_name}>",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current "
                f"branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
            ),
            (
                False,
                f"git push --set-upstream <remote> <{randomise_branch_name}> SELECT * FROM users",
                f"fatal: The current branch [{randomise_branch_name}] has no upstream branch.To push the current "
                f"branch and set the remote as upstream, use git push --set-upstream origin [{randomise_branch_name}]",
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
                [
                    f"git branch -d {randomise_branch_name}, git branch {randomise_branch_name}"
                ],
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
            (
                [
                    f"git branch -d {randomise_branch_name}, git checkout -b {randomise_branch_name}"
                ],
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
                [
                    f"git branch -d {randomise_branch_name}, git branch {randomise_branch_name}"
                ],
                f"git branch -d {randomise_branch_name}",
                f"fatal: A branch named '{randomise_branch_name}' already exists.",
            ),
            (
                [
                    f"git branch -d {randomise_branch_name}, git checkout -b {randomise_branch_name}"
                ],
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

    # Real lower-case dnf operations (a-z and '-' only, so the fixed str regex
    # ``^([a-z-]+) +`` matches each in the synthetic help text the harness
    # builds).
    DNF_OPERATIONS = (
        "autoremove",
        "check",
        "check-update",
        "clean",
        "deplist",
        "distro-sync",
        "downgrade",
        "group",
        "help",
        "history",
        "info",
        "install",
        "list",
        "makecache",
        "mark",
        "provides",
        "reinstall",
        "remove",
        "repolist",
        "repoquery",
        "search",
        "shell",
        "swap",
        "updateinfo",
        "upgrade",
        "builddep",
        "config-manager",
        "copr",
        "download",
        "playground",
        "repoclosure",
        "repograph",
        "repomanage",
        "reposync",
    )

    @staticmethod
    def thefuck8_generate_():
        # FAILING ("parse" mode): feed a str help text to _parse_operations.
        # Buggy build -> bytes regex on str -> TypeError -> crash -> FAILING;
        # fixed build -> str regex -> returns the operation list -> PASSING.
        ops = random.sample(
            TheFuckTestGenerator.DNF_OPERATIONS, random.randint(2, 6)
        )
        expected = " ".join(ops)
        failing = f"'{expected}' parse {','.join(ops)}"
        # PASSING ("match" mode): match() only checks 'no such command' in the
        # output and is identical on both builds.
        op = random.choice(TheFuckTestGenerator.DNF_OPERATIONS)
        word = TheFuckTestGenerator.generate_random_string()
        passing = f"'True' match 'dnf {op} {word}' 'No such command: {op}.'"
        return passing, failing

    @staticmethod
    def thefuck9_generate_():
        randomise_branch_name = TheFuckTestGenerator.generate_random_string()
        stderr = f"""fatal: The current branch {randomise_branch_name} has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin {randomise_branch_name}

"""
        passing = (
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push",
                "",
                stderr,
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push -u origin",
                "",
                stderr,
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push --set-upstream origin",
                "",
                stderr,
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name} --quiet",
                "git push --quiet",
                "",
                stderr,
            ),
        )

        failing = (
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push -u",
                "",
                stderr,
            ),
            (
                f"git push --set-upstream origin {randomise_branch_name}",
                "git push --force",
                "",
                stderr,
            ),
        )

        return (
            passing[random.randint(0, len(passing) - 1)],
            failing[random.randint(0, len(failing) - 1)],
        )

    @staticmethod
    def thefuck10_generate_():
        # man.get_new_command, for a digit-less command, gained a "No manual
        # entry for X" special case on the fixed build: it then returns the
        # single suggestion [X + ' --help'] (length 1) instead of the buggy
        # three-suggestion list (length 3). The harness prints len(result).
        word = TheFuckTestGenerator.generate_random_string()
        # FAILING: stderr triggers the fixed special case -> len 1 (fixed) vs
        # len 3 (buggy); expected "1".
        failing = f"'1' 'man {word}' 'No manual entry for {word}'"
        # PASSING: non-matching stderr -> both builds return a 3-element list;
        # expected "3".
        word2 = TheFuckTestGenerator.generate_random_string()
        tail = TheFuckTestGenerator.generate_random_string()
        passing = f"'3' 'man {word2}' 'some output {tail}'"
        return passing, failing

    @staticmethod
    def thefuck11_generate_():
        # git stderr suggests `git push --set-upstream origin master`; the rule
        # derives push_upstream='push --set-upstream origin master' from its
        # third-from-last line. Each triple is (expected, command, std_err).
        word = TheFuckTestGenerator.generate_random_string()
        std_err = (
            "fatal: The current branch master has no upstream branch.\n"
            "To push the current branch and set the remote as upstream use\n"
            "\n"
            "    git push --set-upstream origin master\n"
            "\n"
        )
        # PASSING: no --set-upstream/-u option to strip, so the buggy and fixed
        # builds produce the same output (the plain push->push... substitution).
        passing = (
            ("git push --set-upstream origin master", "git push", std_err),
            (
                f"git push --set-upstream origin master origin {word}",
                f"git push origin {word}",
                std_err,
            ),
            (
                f"git push --set-upstream origin master {word} extra",
                f"git push {word} extra",
                std_err,
            ),
        )
        # FAILING: command carries --set-upstream/-u plus its argument; only the
        # fixed build strips them before substituting, so the buggy output keeps
        # the duplicated option and differs from the expected (fixed) command.
        failing = (
            (
                f"git push --set-upstream origin master {word}",
                f"git push --set-upstream origin {word}",
                std_err,
            ),
            (
                f"git push --set-upstream origin master {word}",
                f"git push -u origin {word}",
                std_err,
            ),
        )
        return (
            passing[random.randint(0, len(passing) - 1)],
            failing[random.randint(0, len(failing) - 1)],
        )

    # Typos of common executables: each is NOT itself an executable but is a
    # close match of one, so ``no_command.match`` returns True on the buggy
    # build (which omits the ``which`` check).
    THEFUCK12_TYPOS = (
        "gitt",
        "lss",
        "catt",
        "echoo",
        "grepp",
        "sortt",
        "datee",
        "wcc",
        "headd",
        "rmm",
        "envv",
        "pwdd",
        "sedd",
        "uniqq",
    )

    @staticmethod
    def thefuck12_generate_():
        def _triple(expected):
            typo = random.choice(TheFuckTestGenerator.THEFUCK12_TYPOS)
            suffix = TheFuckTestGenerator.generate_random_string()
            return expected, f"{typo} {suffix}", f"{typo}: not found"

        # match() returns True on the buggy build for both, so labelling the
        # expected value True yields a passing test and False a failing one.
        return _triple(True), _triple(False)

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

    # The five aliases Fish._get_overridden_aliases returns as its built-in
    # default. On the buggy build a non-empty TF_OVERRIDDEN_ALIASES *replaces*
    # this default; on the fixed build the default is always unioned in.
    FISH_DEFAULT_ALIASES = ("cd", "grep", "ls", "man", "open")

    @staticmethod
    def _fish_env_tokens(k: int) -> list:
        # Non-default alias tokens (the "zz" prefix guarantees they are never one
        # of the FISH_DEFAULT_ALIASES).
        return [
            "zz" + "".join(random.choices(string.ascii_letters, k=random.randint(3, 7)))
            for _ in range(k)
        ]

    @staticmethod
    def thefuck14_generate_():
        # FAILING: TF_OVERRIDDEN_ALIASES holds only non-default aliases and we
        # probe for a DEFAULT alias. Buggy build returns just the env aliases
        # (default missing -> "False"); fixed build unions in the default
        # (present -> "True"). Expected is "True", so buggy -> FAILING, fixed ->
        # PASSING.
        env_fail = TheFuckTestGenerator._fish_env_tokens(random.randint(2, 4))
        needle_fail = random.choice(TheFuckTestGenerator.FISH_DEFAULT_ALIASES)
        failing = f"'True' '{','.join(env_fail)}' '{needle_fail}'"
        # PASSING: probe for one of the env aliases, present on both builds.
        env_pass = TheFuckTestGenerator._fish_env_tokens(random.randint(2, 4))
        needle_pass = random.choice(env_pass)
        passing = f"'True' '{','.join(env_pass)}' '{needle_pass}'"
        return passing, failing

    @staticmethod
    def thefuck15_generate_():
        randomise_ = TheFuckTestGenerator.generate_random_string()
        match_passing = (
            (
                True,
                f"git submodule update {randomise_}",
                f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?",
            ),
            (
                True,
                f"git commit {randomise_}",
                f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?",
            ),
        )

        match_failing = (
            (True, f"git submodule update {randomise_}", ""),
            (True, f"git commit {randomise_}", ""),
        )

        get_new_command_passing = (
            (
                f"git add -- {randomise_} && git submodule update {randomise_}",
                f"git submodule update {randomise_}",
                f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?",
            ),
            (
                f"git add -- {randomise_} && git commit {randomise_}",
                f"git commit {randomise_}",
                f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?",
            ),
        )

        get_new_command_failing = (
            (
                f"git add -- {randomise_} && git submodule update {randomise_}",
                f"GIT SUBMODULE UPDATE {randomise_}",
                f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?",
            ),
            (
                f"git add -- {randomise_} && git commit {randomise_}",
                f"GIT COMMIT {randomise_}",
                f"error: pathspec '{randomise_}' did not match any file(s) known to git. Did you forget to 'git add'?",
            ),
        )

        return (
            match_passing[random.randint(0, len(match_passing) - 1)],
            get_new_command_passing[
                random.randint(0, len(get_new_command_passing) - 1)
            ],
            match_failing[random.randint(0, len(match_failing) - 1)],
            get_new_command_failing[
                random.randint(0, len(get_new_command_failing) - 1)
            ],
        )

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
            ("1", "PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES", f"{randomise}"),
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

        return (
            passing_bash_[random.randint(0, len(passing_bash_) - 1)],
            passing_zsh_[random.randint(0, len(passing_zsh_) - 1)],
            failing_bash_[random.randint(0, len(failing_bash_) - 1)],
            failing_zsh_[random.randint(0, len(failing_zsh_) - 1)],
        )

    @staticmethod
    def thefuck17_generate_():
        randomise_alias_name = TheFuckTestGenerator.generate_random_string()
        passing = (
            (f"alias {randomise_alias_name}", randomise_alias_name),
            (f"TF_ALIAS={randomise_alias_name}", randomise_alias_name),
        )
        failing = (f"the{randomise_alias_name}", randomise_alias_name)
        return passing[random.randint(0, 1)], failing

    @staticmethod
    def thefuck18_generate_():
        randomise = "".join(
            random.choices(string.ascii_lowercase, k=random.randint(1, 1))
        )
        randomise_ = "".join(
            random.choices(string.ascii_lowercase, k=random.randint(2, 2))
        )
        passing_ = (
            (True, f"sudo {randomise_} -{randomise}", "Permission denied", ""),
            (True, f"sudo {randomise_} -{randomise}", "permission denied", ""),
            (
                True,
                f"sudo {randomise_} -{randomise}",
                "npm ERR! Error: EACCES, unlink",
                "",
            ),
            (
                True,
                f"sudo {randomise_} -{randomise}",
                "requested operation requires superuser privilege",
                "",
            ),
            (True, f"sudo {randomise_} -{randomise}", "need to be root", ""),
            (True, f"sudo {randomise_} -{randomise}", "need root", ""),
            (True, f"sudo {randomise_} -{randomise}", "must be root", ""),
            (
                True,
                f"sudo {randomise_} -{randomise}",
                "You don't have access to the history DB.",
                "",
            ),
            (
                True,
                f"sudo {randomise_} -{randomise}",
                "",
                "error: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/ipaddr.py'",
            ),
        )

        failing_ = (
            (False, f"sudo {randomise_} -{randomise}", " PERMISSION DENIED ", ""),
            (
                False,
                f"sudo {randomise_} -{randomise}",
                " NPM ERR! ERROR: EACCES, UNLINK ",
                "",
            ),
            (
                False,
                f"sudo {randomise_} -{randomise}",
                " REQUESTED OPERATION REQUIRES SUPERUSER PRIVILEGE ",
                "",
            ),
            (False, f"sudo {randomise_} -{randomise}", " NEED TO BE ROOT ", ""),
            (False, f"sudo {randomise_} -{randomise}", " NEED ROOT ", ""),
            (False, f"sudo {randomise_} -{randomise}", " MUST BE ROOT ", ""),
            (
                False,
                f"sudo {randomise_} -{randomise}",
                " YOU DON'T HAVE ACCESS TO THE HISTORY DB. ",
                "",
            ),
            (
                False,
                f"sudo {randomise_} -{randomise}",
                "",
                " ERROR: [ERRNO 13] PERMISSION DENIED: '/USR/LOCAL/LIB/PYTHON2.7/DIST-PACKAGES/IPADDR.PY' ",
            ),
        )

        return (
            passing_[random.randint(0, len(passing_) - 1)],
            failing_[random.randint(0, len(failing_) - 1)],
        )

    @staticmethod
    def thefuck19_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        git_err = """
        To /tmp/foo
         ! [rejected]        master -> master (non-fast-forward)
         error: failed to push some refs to '/tmp/bar'
         hint: Updates were rejected because the tip of your current branch is behind
         hint: its remote counterpart. Integrate the remote changes (e.g.
         hint: 'git pull ...') before pushing again.
         hint: See the 'Note about fast-forwards' in 'git push --help' for details.
        """
        it_uptodate = "Everything up-to-date"
        git_ok = """
        Counting objects: 3, done.
        Delta compression using up to 4 threads.
        Compressing objects: 100% (2/2), done.
        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.
        Total 3 (delta 0), reused 0 (delta 0)
        To /tmp/bar
           514eed3..f269c79  master -> master
        """
        passing_match_ = (True, f"git push {randomise}", "", git_err)

        failing_match_ = (
            (True, f"git push {randomise}", "", it_uptodate),
            (True, f"git push {randomise}", "", git_ok),
        )

        passing_get_new_command_ = (
            f"git push --force {randomise}",
            f"git push {randomise}",
            "",
            "",
        )

        failing_get_new_command_ = (
            f"git push --force {randomise}",
            f"git PUSH {randomise}",
            "",
            "",
        )

        return (
            passing_match_,
            passing_get_new_command_,
            failing_match_[random.randint(0, len(failing_match_) - 1)],
            failing_get_new_command_,
        )

    @staticmethod
    def thefuck20_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        randomise2 = TheFuckTestGenerator.generate_random_string()

        passing_zip_file_ = (
            (f"{randomise}.zip", f"unzip {randomise}.zip"),
            (f"{randomise}.zip", f"unzip {randomise}"),
        )

        failing_zip_file_ = (
            f"{randomise}, {randomise2}",
            f"unzip {randomise}.zip, {randomise2}.zip",
        )

        passing_get_new_command = (
            (f"unzip {randomise} -d {randomise}", f"unzip {randomise}"),
            (f"unzip {randomise}.zip -d {randomise}", f"unzip {randomise}.zip"),
        )

        failing_get_new_command = (
            (
                Rf"unzip {randomise}\ {randomise2}.zip -d '{randomise} {randomise2}'",
                Rf"unzip {randomise}\ {randomise2}.zip",
            ),
            (
                Rf"unzip '{randomise} {randomise2}.zip' -d '{randomise} {randomise2}'",
                Rf"unzip '{randomise} {randomise2}.zip'",
            ),
        )

        return (
            passing_zip_file_[random.randint(0, len(passing_zip_file_) - 1)],
            passing_get_new_command[
                random.randint(0, len(passing_get_new_command) - 1)
            ],
            failing_zip_file_,
            failing_get_new_command[
                random.randint(0, len(failing_get_new_command) - 1)
            ],
        )

    @staticmethod
    def thefuck21_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()
        stash_commands = (
            "apply",
            "branch",
            "clear",
            "drop",
            "list",
            "pop",
            "save",
            "show",
        )

        git_stash_err = """
        usage: git stash list [<options>]
           or: git stash show [<stash>]
           or: git stash drop [-q|--quiet] [<stash>]
           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
           or: git stash branch <branchname> [<stash>]
           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]
        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]
           or: git stash clear
        """
        passing_match_ = (
            True,
            f"git stash {stash_commands[random.randint(0, len(stash_commands) - 1)]} {randomise}",
            git_stash_err,
        )
        failing_match_ = (
            True,
            f"git {stash_commands[random.randint(0, len(stash_commands) - 1)]} {randomise}",
            git_stash_err,
        )

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

        passing_ = (
            expected,
            randomise_script1,
            side_effect,
            randomise_priority_passing1,
            randomise_script2,
            side_effect,
            randomise_priority_passing2,
            randomise_script3,
            side_effect,
            randomise_priority_passing3,
        )
        # failing test has priority of None or string
        failing_ = (
            (
                expected,
                randomise_script1,
                side_effect,
                "",
                randomise_script2,
                side_effect,
                "",
                randomise_script3,
                side_effect,
                "",
            ),
            (
                expected,
                randomise_script1,
                side_effect,
                None,
                randomise_script2,
                side_effect,
                None,
                randomise_script3,
                side_effect,
                None,
            ),
        )

        return passing_, failing_[random.randint(0, 1)]

    @staticmethod
    def thefuck23_generate_():
        # FAILING ("nocm"): fake shelf without the context-manager protocol ->
        # buggy crash, fixed survives. PASSING ("cm"): fake shelf with the
        # protocol -> both survive.
        value = TheFuckTestGenerator.generate_random_string()
        failing = f"'{value}' 'nocm'"
        value2 = TheFuckTestGenerator.generate_random_string()
        passing = f"'{value2}' 'cm'"
        return passing, failing

    @staticmethod
    def thefuck24_generate_():
        randomise1 = "".join(
            random.choices(string.ascii_letters, k=random.randint(4, 8))
        )
        randomise2 = "".join(
            random.choices(string.ascii_letters, k=random.randint(4, 8))
        )
        randomise3 = "".join(
            random.choices(string.ascii_letters, k=random.randint(4, 8))
        )
        passing_ = (randomise1, [randomise1, randomise2])
        failing_ = (randomise3, [randomise1, randomise2])
        return passing_, failing_

    @staticmethod
    def thefuck25_generate_():
        randomise1 = "".join(
            random.choices(string.ascii_letters, k=random.randint(3, 6))
        )
        randomise2 = "".join(
            random.choices(string.ascii_letters, k=random.randint(3, 6))
        )
        randomise3 = "".join(
            random.choices(string.ascii_letters, k=random.randint(3, 6))
        )
        passing = (
            f"mkdir -p {randomise1}/{randomise2}/{randomise3}",
            f"mkdir {randomise1}/{randomise2}/{randomise3}",
        )

        failing = (
            (
                f"hdfs dfs -mkdir -p {randomise1}/{randomise2}/{randomise3}",
                f"hdfs dfs -mkdir {randomise1}/{randomise2}/{randomise3}",
            ),
            (
                f"./bin/hdfs dfs -mkdir -p {randomise1}/{randomise2}/{randomise3}",
                f"./bin/hdfs dfs -mkdir {randomise1}/{randomise2}/{randomise3}",
            ),
        )
        return passing, failing[random.randint(0, len(failing) - 1)]

    @staticmethod
    def thefuck26_generate_():
        # vagrant_up.get_new_command changed shape: for a command that names a
        # machine (>= 3 whitespace-separated parts) the fixed build returns a
        # LIST of two suggestions while the buggy build returns a single STRING;
        # for a command without a machine both builds return a STRING. The
        # harness prints isinstance(result, list), which is build-invariant to
        # the exact ``shells.and_`` formatting.
        sub = TheFuckTestGenerator.generate_random_string()
        machine = TheFuckTestGenerator.generate_random_string()
        # FAILING: machine present -> fixed returns list ("True"), buggy returns
        # str ("False"); expected "True".
        failing = f"'True' 'vagrant {sub} {machine}'"
        # PASSING: no machine -> both builds return str ("False"); expected
        # "False".
        passing = f"'False' 'vagrant {TheFuckTestGenerator.generate_random_string()}'"
        return passing, failing

    @staticmethod
    def thefuck27_generate_():
        randomise = "".join(
            random.choices(string.ascii_lowercase, k=random.randint(5, 10))
        )
        passing = (
            (f"open http://{randomise}.com", f"open {randomise}.com"),
            (f"open http://{randomise}.io", f"open {randomise}.io"),
        )
        failing = (
            (f"xdg-open http://{randomise}.io", f"xdg-open {randomise}.io"),
            (
                f"gnome-open http://{randomise}.io",
                f"gnome-open {randomise}.io",
            ),
        )

        return (
            passing[random.randint(0, len(passing) - 1)],
            failing[random.randint(0, len(failing) - 1)],
        )

    @staticmethod
    def thefuck28_generate_():
        # fix_file.get_new_command honours a fixcolcmd setting only on the fixed
        # build. FAILING ("col"): pass a fixcolcmd embedding COLMARKER -> the
        # fixed build emits it ("True"), the buggy build ignores settings
        # ("False"); expected "True". PASSING ("nocol"): no fixcolcmd -> both
        # emit the line command without COLMARKER; expected "False".
        line = random.randint(1, 400)
        col = random.randint(1, 400)
        failing = f"'True' 'col' '{line}' '{col}'"
        line2 = random.randint(1, 400)
        col2 = random.randint(1, 400)
        passing = f"'False' 'nocol' '{line2}' '{col2}'"
        return passing, failing

    @staticmethod
    def thefuck29_generate_():
        random_key = TheFuckTestGenerator.generate_random_string()
        random_value = TheFuckTestGenerator.generate_random_string()
        passing_ = {f"{random_key}": f"{random_value}"}
        failing_ = {f"{random_key}, {random_value}"}
        return passing_, failing_

    @staticmethod
    def thefuck30_generate_():
        randomise = TheFuckTestGenerator.generate_random_string()

        # (script, file, line, col (or None), stderr)
        tests = (
            (
                f"{randomise} a.c",
                "a.c",
                3,
                1,
                """
             a.c: In function 'main':
             a.c:3:1: error: expected expression before '}' token
              }
               ^
             """,
            ),
            (
                f"{randomise} a.c",
                "a.c",
                3,
                1,
                """
             a.c:3:1: error: expected expression
             }
             ^
             """,
            ),
            (
                f"{randomise} a.pl",
                "a.pl",
                3,
                None,
                """
             syntax error at a.pl line 3, at EOF
             Execution of a.pl aborted due to compilation errors.
             """,
            ),
            (
                f"{randomise} a.pl",
                "a.pl",
                2,
                None,
                """
             Search pattern not terminated at a.pl line 2.
             """,
            ),
            (
                f"{randomise} a.sh",
                "a.sh",
                2,
                None,
                """
             a.sh: line 2: foo: command not found
             """,
            ),
            (
                f"{randomise} a.sh",
                "a.sh",
                2,
                None,
                """
             a.sh:2: command not found: foo
             """,
            ),
            (
                f"{randomise} a.sh",
                "a.sh",
                2,
                None,
                """
             a.sh: line 2: foo: command not found
             """,
            ),
            (
                f"{randomise} a.rs",
                "a.rs",
                2,
                5,
                """
             a.rs:2:5: 2:6 error: unexpected token: `+`
             a.rs:2     +
                        ^
             """,
            ),
            (
                f"{randomise}",
                "src/lib.rs",
                3,
                5,
                """
                Compiling test v0.1.0 (file:///tmp/fix-error/test)
                src/lib.rs:3:5: 3:6 error: unexpected token: `+`
                src/lib.rs:3     +
                                 ^
             Could not compile `test`.

             To learn more, run the command again with --verbose.
             """,
            ),
            (
                f"{randomise} a.py",
                "a.py",
                2,
                None,
                """
               File "a.py", line 2
                   +
                       ^
             SyntaxError: invalid syntax
             """,
            ),
            (
                f"{randomise} a.py",
                "a.py",
                8,
                None,
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
             """,
            ),
            (
                f"{randomise} a.rb",
                "a.rb",
                3,
                None,
                """
             a.rb:3: syntax error, unexpected keyword_end
             """,
            ),
            (
                f"{randomise} a.lua",
                "a.lua",
                2,
                None,
                """
             lua: a.lua:2: unexpected symbol near '+'
             """,
            ),
            (
                f"{randomise} a.sh",
                "/tmp/fix-error/a.sh",
                2,
                None,
                """
             fish: Unknown command 'foo'
             /tmp/fix-error/a.sh (line 2): foo
                                           ^
             """,
            ),
            (
                f"./a",
                "./a",
                2,
                None,
                """
             awk: ./a:2: BEGIN { print "Hello, world!" + }
             awk: ./a:2:                                 ^ syntax error
             """,
            ),
            (
                f"{randomise} a.ll",
                "a.ll",
                1,
                None,
                """
             llc: a.ll:1:1: error: expected top-level entity
             +
             ^
             """,
            ),
            (
                f"{randomise} build a.go",
                "a.go",
                1,
                None,
                """
             can't load package:
             a.go:1:1: expected 'package', found '+'
             """,
            ),
            (
                f"{randomise}",
                "Makefile",
                2,
                None,
                """
             bidule
             make: bidule: Command not found
             Makefile:2: recipe for target 'target' failed
             make: *** [target] Error 127
             """,
            ),
            (
                f"{randomise} st",
                "/home/martin/.config/git/config",
                1,
                None,
                """
             fatal: bad config file line 1 in /home/martin/.config/git/config
             """,
            ),
            (
                f"{randomise} fuck.js asdf qwer",
                "/Users/pablo/Workspace/barebones/fuck.js",
                "2",
                5,
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
             """,
            ),
        )
        script = tests[random.randint(0, len(tests) - 1)][0]
        error = tests[random.randint(0, len(tests) - 1)][4]
        if "EDITOR" in os.environ:
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
        passing_ = ((True, f"ls {randomise_str}.py"), (True, f"ls /{randomise_str}"))
        failing_ = (
            (True, f"ls -lah /{randomise_str}"),
            (True, f"pacman -s {randomise_str}"),
        )
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
    def get_imports(self) -> list:
        return []

    @staticmethod
    def _body(raw_echo: str, ver: str, expected: str) -> list:
        # Monkeypatch fish's Popen so info() sees canned output for both the
        # buggy command form (echo $FISH_VERSION -> raw_echo) and the fixed one
        # (fish --version -> "fish, version <ver>"). The buggy build strips the
        # echo output while the fixed build takes the last whitespace token of
        # --version, so a raw_echo != ver distinguishes the builds.
        return ast.parse(
            "import io\n"
            "import thefuck.shells.fish as _f\n"
            "from thefuck.utils import cache as _cache, memoize as _memoize\n"
            "_cache.disabled = True\n"
            "_memoize.disabled = True\n"
            "class _P:\n"
            "    def __init__(self, d):\n"
            "        self.stdout = io.BytesIO(d)\n"
            "    def wait(self, *a, **k):\n"
            "        return 0\n"
            "def _fp(args, *a, **k):\n"
            "    if '--version' in args:\n"
            f"        return _P({('fish, version ' + ver).encode('utf-8')!r})\n"
            f"    return _P({raw_echo.encode('utf-8')!r})\n"
            "_f.Popen = _fp\n"
            f"self.assertEqual({expected!r}, _f.Fish().info())\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        raw_echo = "e" + self.generate_random_string()
        ver = "v" + self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(raw_echo, ver, "Fish Shell " + ver)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        ver = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(ver, ver, "Fish Shell " + ver)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator4(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def get_imports(self) -> list:
        return []

    @staticmethod
    def _body(name: str, value: str, separator: str) -> list:
        # Feed fish._get_aliases a canned "alias name<sep>value" line via a Popen
        # monkeypatch. With '=' the buggy single-separator parser raises (test
        # errors -> FAILING) while the fixed build parses it; with ' ' both parse
        # identically -> PASSING.
        alias_line = "alias " + name + separator + value
        return ast.parse(
            "import io\n"
            "import thefuck.shells.fish as _f\n"
            "from thefuck.utils import cache as _cache, memoize as _memoize\n"
            "_cache.disabled = True\n"
            "_memoize.disabled = True\n"
            "class _P:\n"
            "    def __init__(self, d):\n"
            "        self.stdout = io.BytesIO(d)\n"
            "    def wait(self, *a, **k):\n"
            "        return 0\n"
            f"_f.Popen = lambda *a, **k: _P({alias_line.encode('utf-8')!r})\n"
            f"self.assertEqual({{{name!r}: {value!r}}}, _f._get_aliases(set()))\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(
            self.generate_random_string(), self.generate_random_string(), "="
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(
            self.generate_random_string(), self.generate_random_string(), " "
        )
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
    @staticmethod
    def _get_parse_assert(ops: list) -> list[Call]:
        # assertEqual(ops, _parse_operations("<help text>")). The str help text
        # makes _parse_operations raise TypeError on the buggy build (bytes
        # regex on str) -> test errors -> FAILING; the fixed build returns the
        # ops list -> PASSING.
        help_text = "\n".join("{}    description".format(op) for op in ops)
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.List(elts=[ast.Constant(value=o) for o in ops]),
                    ast.Call(
                        func=ast.Name(id="_parse_operations"),
                        args=[ast.Constant(value=help_text)],
                        keywords=[],
                    ),
                ],
                keywords=[],
            )
        ]

    @staticmethod
    def _get_match_assert(script: str, output: str) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Constant(value=True),
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
                names=[
                    ast.alias(name="match"),
                    ast.alias(name="_parse_operations"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        ops = random.sample(
            TheFuckTestGenerator.DNF_OPERATIONS, random.randint(2, 6)
        )
        test = self.get_empty_test()
        test.body = self._get_parse_assert(ops)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        op = random.choice(TheFuckTestGenerator.DNF_OPERATIONS)
        word = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._get_match_assert(
            f"dnf {op} {word}", f"No such command: {op}."
        )
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

    @staticmethod
    def _body(script: str, stderr: str, expected_len: int) -> list:
        # assertEqual(<len>, len(get_new_command(Command(script, '', stderr)))).
        # The "No manual entry" stderr makes the fixed build return a 1-element
        # list; the buggy build always returns 3.
        return ast.parse(
            f"self.assertEqual({expected_len!r}, "
            f"len(get_new_command(Command({script!r}, '', {stderr!r}))))"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(
            f"man {word}", f"No manual entry for {word}", 1
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self.generate_random_string()
        tail = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(f"man {word}", f"some output {tail}", 3)
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
    def _get_assert(
        expected: bool | str, script: str, std_out: str, std_err: str
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
        expected: str | bool, script: str, std_out: str, std_err: str
    ) -> list[Call]:
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
    def get_imports(self) -> list:
        return [
            ast.Import(names=[ast.alias(name="os")]),
            ast.ImportFrom(
                module="thefuck.shells.fish",
                names=[ast.alias(name="Fish")],
                level=0,
            ),
        ]

    @staticmethod
    def _body(needle: str, env: str) -> list:
        # Inject the env aliases, then assert membership. On the buggy build a
        # non-empty env replaces the default set, so a default needle is absent
        # (assertIn fails -> FAILING); the fixed build always unions the default
        # in (present -> PASSING).
        return ast.parse(
            f"os.environ['TF_OVERRIDDEN_ALIASES'] = {env!r}\n"
            f"self.assertIn({needle!r}, Fish()._get_overridden_aliases())"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        env = ",".join(
            TheFuckTestGenerator._fish_env_tokens(random.randint(2, 4))
        )
        needle = random.choice(TheFuckTestGenerator.FISH_DEFAULT_ALIASES)
        test = self.get_empty_test()
        test.body = self._body(needle, env)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        tokens = TheFuckTestGenerator._fish_env_tokens(random.randint(2, 4))
        env = ",".join(tokens)
        needle = random.choice(tokens)
        test = self.get_empty_test()
        test.body = self._body(needle, env)
        return test, TestResult.PASSING


class TheFuckUnittestGenerator15(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def _generate_one(
        self,
    ) -> str:
        return self.generate_values(self.thefuck15_generate_)

    @staticmethod
    def _get_assert(
        expected: bool, script: str, std_out: str, std_err: str
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
    def _get_assert(result: str, text: str) -> list[Assign | Expr]:
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
                            args=[
                                ast.Constant(value=text),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                ),
                lineno=2,
            ),
        ]

    @staticmethod
    def _get_assert_2(result: str, text: str) -> list[Assign | Expr]:
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
                            args=[
                                ast.Constant(value=text),
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
    def _get_assert(result: Any, alias: Any) -> list[Assign | Expr]:
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
            ),
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
            ),
        ]

        iter_command_call = ast.Call(
            func=ast.Name(id="iter"),
            args=[ast.List(elts=command_calls, ctx=ast.Load())],
            keywords=[],
        )

        args_list = [
            iter_command_call,
            ast.Call(
                func=ast.Name(id="Settings"),
                args=[
                    ast.Constant(value=debug),
                ],
                keywords=[],
            ),
        ]

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

    @staticmethod
    def _body(mode, script):
        if mode == "empty":
            gen = "iter([])"
        else:
            gen = f"iter([CorrectedCommand({script!r}, '', 1)])"
        code = (
            "try:\n"
            f"    SortedCorrectedCommandsSequence({gen}, "
            f"Settings({{{script!r}: 'v'}}))._realise()\n"
            "    _out = 'OK'\n"
            "except Exception:\n"
            "    _out = 'RAISED'\n"
            "self.assertEqual('OK', _out)"
        )
        return ast.parse(code).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("empty", self.generate_random_string())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("full", self.generate_random_string())
        return test, TestResult.PASSING


class TheFuckUnittestGenerator23(
    python.PythonGenerator, UnittestGenerator, TheFuckTestGenerator
):
    def get_imports(self) -> list:
        return []

    @staticmethod
    def _body(value: str, protocol: bool) -> list:
        # Patch shelve.open to return a fake shelf, cache-decorate a function and
        # call it. Without the context-manager protocol the buggy build raises
        # AttributeError inside cache's ``with shelve.open(...)`` (test errors ->
        # FAILING) while the fixed build's ``closing`` wrapper survives (PASSING).
        extra = (
            "    def __enter__(self):\n"
            "        return self\n"
            "    def __exit__(self, *a):\n"
            "        self.close()\n"
            if protocol
            else ""
        )
        return ast.parse(
            "import shelve\n"
            "import thefuck.utils as _u\n"
            "class _Shelf(dict):\n"
            "    def close(self):\n"
            "        pass\n"
            f"{extra}"
            "shelve.open = lambda *a, **k: _Shelf()\n"
            "@_u.cache()\n"
            "def _compute():\n"
            f"    return {value!r}\n"
            f"self.assertEqual({value!r}, _compute())\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_random_string(), protocol=False)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_random_string(), protocol=True)
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
        rules_name_list: list,
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertIn"),
                args=[
                    ast.Call(
                        func=ast.Name(id="Rule"),
                        args=[
                            ast.Constant(value=rule_name),
                            ast.Constant(value=rule_match),
                            ast.Constant(value=rule_get_new_command),
                            ast.Constant(value=rule_enabled_by_default),
                            ast.Constant(value=rule_side_effect),
                            ast.Constant(value=rule_priority),
                            ast.Constant(value=requires_output),
                        ],
                        keywords=[],
                    ),
                    ast.Call(
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
                names=[ast.alias(name="CorrectedCommand")],
                level=0,
            ),
        ]

    @staticmethod
    def _body(script, side_effect, p1, p2):
        code = (
            f"self.assertEqual(True, "
            f"CorrectedCommand({script!r}, {side_effect!r}, {p1}) == "
            f"CorrectedCommand({script!r}, {side_effect!r}, {p2}))"
        )
        return ast.parse(code).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        s = self.generate_random_string()
        se = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(s, se, 1, 2)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        s = self.generate_random_string()
        se = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(s, se, 5, 5)
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
            ),
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
    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="thefuck.types",
                names=[ast.alias(name="Command"), ast.alias(name="Settings")],
                level=0,
            ),
            ast.ImportFrom(
                module="thefuck.rules.vagrant_up",
                names=[ast.alias(name="get_new_command")],
                level=0,
            ),
        ]

    @staticmethod
    def _body(script: str, expected: bool) -> list:
        # assertEqual(<bool>, isinstance(get_new_command(...), list)). A
        # machine-scoped command yields a list only on the fixed build; a plain
        # command yields a str on both builds.
        return ast.parse(
            f"self.assertEqual({expected!r}, isinstance("
            f"get_new_command(Command({script!r}, '', ''), Settings()), list))"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        sub = self.generate_random_string()
        machine = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(f"vagrant {sub} {machine}", True)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        sub = self.generate_random_string()
        test = self.get_empty_test()
        test.body = self._body(f"vagrant {sub}", False)
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
            ),
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
    def get_imports(self) -> list:
        return []

    @staticmethod
    def _body(line: int, col: int, mode: str) -> list:
        # Build a real temp file, set EDITOR, feed fix_file.get_new_command a
        # column-bearing error. With a fixcolcmd embedding COLMARKER the fixed
        # build honours it (COLMARKER present) while the buggy build ignores
        # settings (absent). Without a fixcolcmd both omit COLMARKER.
        settings_expr = (
            "Settings({'fixcolcmd': '{editor} {file} COLMARKER'})"
            if mode == "col"
            else "Settings()"
        )
        expected = "True" if mode == "col" else "False"
        src = (
            "import os, tempfile\n"
            "from thefuck.types import Command, Settings\n"
            "from thefuck.rules.fix_file import get_new_command\n"
            "os.environ['EDITOR'] = 'nano'\n"
            "fd, path = tempfile.mkstemp(suffix='.c')\n"
            "os.close(fd)\n"
            "stderr = path + ':" + str(line) + ":" + str(col) + ": error'\n"
            "settings = " + settings_expr + "\n"
            "result = get_new_command(Command('gcc a.c', '', stderr), settings)\n"
            "self.assertEqual(" + expected + ", 'COLMARKER' in str(result))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(
            random.randint(1, 400), random.randint(1, 400), "col"
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(
            random.randint(1, 400), random.randint(1, 400), "nocol"
        )
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
                    args=[],
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

    @staticmethod
    def _body(old, key, new):
        code = (
            f"self.assertEqual({old!r}, "
            f"Settings({{{key!r}: {old!r}}}).update(**{{{key!r}: {new!r}}})[{key!r}])"
        )
        return ast.parse(code).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key = self.generate_random_string().lower()
        old = self.generate_random_string().lower()
        new = self.generate_random_string().lower() + "x"
        test = self.get_empty_test()
        test.body = self._body(old, key, new)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key = self.generate_random_string().lower()
        old = self.generate_random_string().lower()
        test = self.get_empty_test()
        test.body = self._body(old, key, old)
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
            ),
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
            ),
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
            ),
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
    # The harness expects "<name> <mode>": in "semi" mode PATH uses ';' so the
    # buggy ':'-split finds nothing (fails), the fixed os.pathsep-split finds the
    # executable (passes); in "plain" mode both behave the same.
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        real_exe, _ = self.generate_values(self.thefuck2_generate_)
        return f"{real_exe} semi", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        real_exe, _ = self.generate_values(self.thefuck2_generate_)
        return f"{real_exe} plain", TestResult.PASSING


class TheFuckSystemtestGenerator3(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck3_generate_)
        return fail_, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck3_generate_)
        return pass_, TestResult.PASSING


class TheFuckSystemtestGenerator4(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck4_generate_)
        return fail_, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck4_generate_)
        return pass_, TestResult.PASSING


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
        _, fail_ = self.generate_values(self.thefuck8_generate_)
        return fail_, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck8_generate_)
        return pass_, TestResult.PASSING


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
    @staticmethod
    def _serialize(triple) -> str:
        expected, command, std_err = triple
        return f"'{expected}' '{command}' '{std_err}'"

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck12_generate_)
        return self._serialize(fail_), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck12_generate_)
        return self._serialize(pass_), TestResult.PASSING


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
        _, fail_ = self.generate_values(self.thefuck14_generate_)
        return fail_, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck14_generate_)
        return pass_, TestResult.PASSING


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
    # Format: 'OK' 'mode' 'script' 'priority'. "empty" mode realises an empty
    # SortedCorrectedCommandsSequence (buggy IndexError, fixed guarded); "full"
    # mode realises a single-command sequence (OK on both builds).
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        s = self.generate_random_string()
        return f"'OK' 'empty' '{s}' '1'", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        s = self.generate_random_string()
        return f"'OK' 'full' '{s}' '1'", TestResult.PASSING


class TheFuckSystemtestGenerator23(SystemtestGenerator, TheFuckTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.thefuck23_generate_)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.thefuck23_generate_)
        return f"{pass_}", TestResult.PASSING


class TheFuckSystemtestGenerator24(SystemtestGenerator, TheFuckTestGenerator):
    # Format: 'expected' 'script' 'side_effect' 'p1' 'p2'. The harness compares
    # CorrectedCommand(script, se, p1) == CorrectedCommand(script, se, p2): buggy
    # (namedtuple) is False when p1 != p2, fixed ignores priority so it is True.
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        s = self.generate_random_string()
        se = self.generate_random_string()
        return f"'True' '{s}' '{se}' '1' '2'", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        s = self.generate_random_string()
        se = self.generate_random_string()
        return f"'True' '{s}' '{se}' '5' '5'", TestResult.PASSING


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
    # System test format: 'expected' 'key' 'oldval' 'newval'. The harness builds
    # Settings({key: oldval}) and calls update(key=newval): buggy -> newval,
    # fixed -> oldval. Failing tests use oldval != newval, passing use equal.
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        key = self.generate_random_string().lower()
        old = self.generate_random_string().lower()
        new = self.generate_random_string().lower() + "x"
        return f"'{old}' '{key}' '{old}' '{new}'", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        key = self.generate_random_string().lower()
        old = self.generate_random_string().lower()
        return f"'{old}' '{key}' '{old}' '{old}'", TestResult.PASSING


class TheFuckSystemtestGenerator30(SystemtestGenerator, TheFuckTestGenerator):
    # The harness sets EDITOR and calls fix_file.match: the buggy match reports a
    # fixable file whenever the stderr matches a pattern, the fixed match also
    # requires the file to exist. Failing inputs reference a non-existent file
    # (buggy prints a fix, fixed prints False); passing inputs match no pattern.
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        error = f"{self.generate_random_string()}zz.py:3:"
        fail_ = ("fix", error, "False")
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        error = f"just some text {self.generate_random_string()} with no file pattern"
        pass_ = ("fix", error, "False")
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


# thefuck bundles 32 unrelated correction rules, each with its own input format,
# so a single meaningful per-project grammar is not possible. A system test is
# the repr of an ``(expected, script, output)`` triple that the harness parses;
# this permissive grammar accepts that serialized form (any printable content,
# including the empty input some rules use) and is fast to verify.
grammar: Grammar = {
    "<start>": ["<chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.printable),
}
assert is_valid_grammar(grammar)
