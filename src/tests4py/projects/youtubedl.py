import ast
import os
from abc import ABC
import subprocess
import traceback
from pathlib import Path
from typing import List, Optional, Tuple, Any

from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
from isla.fuzzer import GrammarFuzzer

from tests4py.grammars import python
from tests4py.framework.constants import Environment, HARNESS_FILE
from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult, ExpectErrAPI


class YoutubeDL(Project):
    def __init__(
        self,
        bug_id: int,
        python_version: str,
        python_path: str,
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
            project_name="youtubedl",
            github_url="https://github.com/ytdl-org/youtube-dl",
            status=Status.OK,
            cause="N.A.",
            python_version=python_version,
            python_path=python_path,
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
    YoutubeDL(
        bug_id=1,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='99036a1298089068dcf80c0985bfcc3f8c24f281',
        fixed_commit_id='1cc47c667419e0eadc0a6989256ab7b276852adf',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_match_str'],
        api=YoutubeDL1API(),
        unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDL1SystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=2,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='84f085d4bdb66ee025fb337bcd571eab7469da97',
        fixed_commit_id='9d6ac71c27b1dfb662c795ef598dbfd0286682da',
        test_file=[Path('test', 'test_InfoExtractor.py')],
        test_cases=['test.test_InfoExtractor.TestInfoExtractor.test_parse_mpd_formats'],
        test_status_buggy=TestStatus.PASSING,
    )

    YoutubeDL(
        bug_id=3,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='f5469da9e6e259c1690c7ef54f1da1c19f65036f',
        fixed_commit_id='95f3f7c20a05e7ac490e768b8470b20538ef8581',
        api=YoutubeDL3API(),
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_unescape_html'],
        unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDL1SystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=4,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='bc40b3a5ba44006c23daf7fe0ed872af5e33bdc5',
        fixed_commit_id='189935f15960300d316e8b07108b076ac6c2186a',
        test_file=[Path('test', 'test_jsinterp.py')],
        test_cases=['test.test_jsinterp.TestJSInterpreter.test_call']
    )

    YoutubeDL(
        bug_id=5,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='b02b960c6bba834d9e7199ac53430c7933079dc8',
        fixed_commit_id='7dc2a74e0ac9cfa74cc9de6f586ffd5cc8bac0d9',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_unified_timestamps']
    )

    YoutubeDL(
        bug_id=6,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='4f29fa99069760dc47ef9ca5dbf607a567d2982f',
        fixed_commit_id='d631d5f9f27f93767226192e4288990413fa9dbd',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_parse_dfxp_time_expr']
    )

    YoutubeDL(
        bug_id=7,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='63a64948342ebfe46db8c258765e698a04a61904',
        fixed_commit_id='d01949dc89feb2441f251e42e8a6bfa4711b9715',
        api=YoutubeDL7API(),
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_js_to_json_realworld'],
        unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDL1SystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=8,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='cf2ac6df6896dac4d23918867bb86fac1e1088d9',
        fixed_commit_id='f5f4a27a964b41646303921104f4d6d6fd2098e4',
        test_file=[Path('test', 'test_YoutubeDL.py')],
        test_cases=['test.test_YoutubeDL.TestFormatSelection.test_youtube_format_selection']
    )

    YoutubeDL(
        bug_id=9,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='0130afb76e5cb6f470f39f127c8d09eea3e82d0d',
        fixed_commit_id='cf2ac6df6896dac4d23918867bb86fac1e1088d9',
        test_file=[Path('test', 'test_YoutubeDL.py')],
        test_cases=['test.test_YoutubeDL.TestFormatSelection.test_youtube_format_selection']
    )

    # Performance Bug
    YoutubeDL(
        bug_id=10,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='85d586617750d38d742a24f141b099f6b898d269',
        fixed_commit_id='d305dd73a3d6927f0a2c63d08662a183fa173833',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_js_to_json_realworld'],
        test_status_buggy=TestStatus.PASSING
    )

    YoutubeDL(
        bug_id=11,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='b568561eba6f4aceb87419e21aba11567c5de7da',
        fixed_commit_id='348c6bf1c1a00eec323d6e21ff7b9b12699afe04',
        api=YoutubeDL11API(),
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_str_to_int'],
        unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDL1SystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=12,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='435e382423f860aca82a58d7c3db58cbfa242b40',
        fixed_commit_id='e118a8794ffe5a3a414afd489726f34d753b0b23',
        test_file=[Path('test', 'test_YoutubeDL.py')],
        test_cases=['test.test_YoutubeDL.TestFormatSelection.test_format_selection_string_ops']
    )

    YoutubeDL(
        bug_id=13,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='6945b9e78f38284eb4e440b7badea2fc60b66c2f',
        fixed_commit_id='fad4ceb53404227f471af2f3544c4c14a5df4acb',
        api=YoutubeDL13API(),
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_urljoin'],
        unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDL1SystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=14,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='562de77f41d0c08df9dbb08cfa86ba6c7d239c5a',
        fixed_commit_id='84213ea8d41d5fe1608333a16ac578dccdf9a915',
        test_file=[Path('test', 'test_youtube_chapters.py')],
        test_cases=['test.test_youtube_chapters.TestYoutubeChapters.test_youtube_chapters']
    )

    YoutubeDL(
        bug_id=15,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='e7f3529f68ee7c8ca78366d37f851cb31fa00f31',
        fixed_commit_id='c384d537f882efab10a78a56ce6dcb0a30f54b47',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_js_to_json_edgecases test.test_utils.TestUtil.test_js_to_json_realworld']
    )

    YoutubeDL(
        bug_id=16,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='68d43a61b552007a718894967b869c0f1d8ff00f',
        fixed_commit_id='3869028ffb6be6ab719e5cf1004276dfdfd1216d',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_dfxp2srt']
    )

    YoutubeDL(
        bug_id=17,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='4bf22f7a1014c55e3358b5a419945071b152eafc',
        fixed_commit_id='5b232f46dcbdc805507c02edd4fd598f31d544d5',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_cli_bool_option']
    )

    YoutubeDL(
        bug_id=18,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='dc6520aa3d1fe7afc52613e392f15dde90af4844',
        fixed_commit_id='0396806f671e5828c2abdeb8048acf8b654507b6',
        test_file=[Path('test', 'test_YoutubeDL.py')],
        test_cases=['test.test_YoutubeDL.TestYoutubeDL.test_do_not_override_ie_key_in_url_transparent']
    )

    YoutubeDL(
        bug_id=19,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='9a0942ad55bba714d6eaeb9ee4f66a138ec85e17',
        fixed_commit_id='15da37c7dc8cf14ba5ce880aa1805fceaa71fc44',
        test_file=[Path('test', 'test_YoutubeDL.py')],
        test_cases=['test.test_YoutubeDL.TestYoutubeDL.test_prepare_filename']
    )

    YoutubeDL(
        bug_id=20,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='b6c9fe416243373bcb59eb8aa5ef0baca8f3c97c',
        fixed_commit_id='609ff8ca19f1c4c168a81121074b91cc0f0d4c47',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_get_element_by_attribute']
    )

    # TODO 21-42 youtube-dl

    YoutubeDL(
        bug_id=43,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='cecaaf3f58ad9f544dbb79af1e565d9353fa2b2d',
        fixed_commit_id='d6c7a367e88096bb17e323954002c084477fe908',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_url_basename']
    )


class YoutubeDLAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def error_handling(self, process) -> bool:
        return process.returncode != 0 and process.returncode != 200

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return False

    # noinspection PyBroadException
    def execute(self, system_test_path, environ: Environment) -> TestResult:
        try:
            with open(system_test_path, "r") as fp:
                test = fp.read()
            if test:
                test = test.split("\n")
                for i in test:
                    i.strip()
            else:
                test = []

            process = subprocess.run(
                ["python", HARNESS_FILE] + test,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.default_timeout,
                env=environ,
            )
            if self.contains(process):
                return TestResult.FAILING
            else:
                if self.error_handling(process):
                    print(process)
                    return TestResult.UNDEFINED
                else:
                    return TestResult.PASSING
        except subprocess.TimeoutExpired:
            return TestResult.UNDEFINED
        except Exception as e:
            traceback.print_exception(e)
            return TestResult.UNDEFINED



class YoutubeDL1API(YoutubeDLAPI):

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"Input does not match the expected outcome!" in process.stderr)


class YoutubeDL3API(YoutubeDLAPI):
    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"Input does not match the expected outcome!" in process.stderr)


class YoutubeDL7API(YoutubeDLAPI):
    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"Input does not match the expected outcome!" in process.stderr)


class YoutubeDL11API(YoutubeDLAPI):
    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"TypeError: expected string or bytes-like object" in process.stderr)


class YoutubeDL13API(YoutubeDLAPI):
    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"Input does not match the expected outcome!" in process.stderr)


class YoutubeDLUnittestGenerator(UnittestGenerator, ABC):
    pass


class YoutubeDL1UnittestGenerator(YoutubeDLUnittestGenerator, ABC):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class YoutubeDL2UnittestGenerator(YoutubeDLUnittestGenerator, ABC):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class YoutubeDL3UnittestGenerator(YoutubeDLUnittestGenerator, ABC):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class YoutubeDL7UnittestGenerator(YoutubeDLUnittestGenerator, ABC):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class YoutubeDLSystemtestGenerator(SystemtestGenerator, ABC):
   pass


class YoutubeDL1SystemtestGenerator(YoutubeDLSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


youtubedl_1_grammar: Grammar = {
    "<start>": ["<match_str>"],
    "<match_str>": ["(<par><stmt_list><par>, {<dict_list>})"],
    "<stmt_list>": ["<stmt> & <stmt_list>", "<stmt>"],
    "<stmt>": ["<bool_stmt>", "<comp_stmt>"],
    "<bool_stmt>": ["<unary_op><name>"],
    "<unary_op>": ["!", ""],
    "<comp_stmt>": ["<name> <comp_op><optional> <int>"],
    "<optional>": ["?"],
    "<comp_op>": ["<", ">", "<=", ">=", "=", "!="],
    "<dict_list>": ["<kv>, <dict_list>", "<kv>"],
    "<kv>": ["<par><key><par>: <value>"],
    "<par>": ["'"],
    "<key>": ["is_live", "like_count", "description", "title", "dislike_count"],
    "<value>": ['<bool>', "<int>"],
    "<bool>": ["True", "False"],
    "<name>": ["is_live", "like_count", "description", "title", "dislike_count"],
    "<int>": [str(i) for i in range(10)],
}
