from os import PathLike
from pathlib import Path
from typing import List, Optional

from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
from isla.fuzzer import GrammarFuzzer

from tests4py.grammars import python
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
        unittests=YoutubeDl1UnittestGenerator(),
        systemtests=YoutubeDlSystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=2,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='84f085d4bdb66ee025fb337bcd571eab7469da97',
        fixed_commit_id='9d6ac71c27b1dfb662c795ef598dbfd0286682da',
        test_file=[Path('test', 'test_InfoExtractor.py')],
        test_cases=['test.test_InfoExtractor.TestInfoExtractor.test_parse_mpd_formats']
    )

    YoutubeDL(
        bug_id=3,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='f5469da9e6e259c1690c7ef54f1da1c19f65036f',
        fixed_commit_id='95f3f7c20a05e7ac490e768b8470b20538ef8581',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_unescape_html']
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
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_js_to_json_realworld']
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

    YoutubeDL(
        bug_id=10,
        python_version='3.7.0',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='85d586617750d38d742a24f141b099f6b898d269',
        fixed_commit_id='d305dd73a3d6927f0a2c63d08662a183fa173833',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_js_to_json_realworld']
    )

    YoutubeDL(
        bug_id=11,
        python_version='3.7.4',
        darwin_python_version='3.7.12',
        python_path='',
        buggy_commit_id='b568561eba6f4aceb87419e21aba11567c5de7da',
        fixed_commit_id='348c6bf1c1a00eec323d6e21ff7b9b12699afe04',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_str_to_int']
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
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_urljoin']
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

    # noinspection PyBroadException
    def run(self, system_test_path, environ) -> TestResult:
        return TestResult.UNDEFINED


class YoutubeDl1UnittestGenerator(python.PythonGenerator, UnittestGenerator):
    def __init__(self):
        python.PythonGenerator.__init__(
            self,
            limit_stmt_per_block=6,
            limit_stmt_depth=3,
            limit_expr_depth=2,
            limit_args_per_function=3,
        )
        UnittestGenerator.__init__(self)

    def _get_failing_args(self) -> List[ast.expr]:
        return []

    @staticmethod
    def _get_passing_args() -> List[ast.expr]:
        return []

    def _get_failing_keywords(self) -> List[ast.keyword]:
        return []

    @staticmethod
    def _get_passing_keywords() -> List[ast.keyword]:
        return []

    def _get_failing_prefix(self) -> List[ast.stmt]:
        return []

    def _get_passing_prefix(self) -> List[ast.stmt]:
        return []

    def _get_function_call(
        self, args: List[ast.expr] = None, keywords: List[ast.keyword] = None
    ) -> ast.FunctionDef:
        function = self._generate_FunctionDef()
        function.decorator_list = [
            ast.Call(
                ast.Attribute(
                    value=ast.Name(id="pysnooper"),
                    attr="snoop",
                ),
                args=[] if args is None else args,
                keywords=[] if keywords is None else keywords,
            )
        ]
        return function

    def _get_failing_body(
        self, function: ast.FunctionDef, prefix: List[ast.stmt] = None
    ) -> List[ast.stmt]:
        if prefix:
            return prefix + [function]
        return [function]

    def _get_passing_body(
        self, function: ast.FunctionDef, prefix: List[ast.stmt] = None
    ) -> List[ast.stmt]:
        if prefix:
            return prefix + [function]
        return [function]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        test = self.get_empty_test()
        prefix = self._get_failing_prefix()
        test.body = self._get_failing_body(
            self._get_function_call(
                self._get_failing_args(), self._get_failing_keywords()
            ),
            prefix=prefix,
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        test = self.get_empty_test()
        prefix = self._get_passing_prefix()
        test.body = self._get_passing_body(
            self._get_function_call(
                self._get_passing_args(), self._get_passing_keywords()
            ),
            prefix=prefix,
        )
        return test, TestResult.PASSING


class YoutubeDlSystemtestGenerator(SystemtestGenerator):
    def __init__(self):
        super().__init__()
        #self.variables_fuzzer = GrammarFuzzer(grammar, start_symbol="<variable_list>")
        #self.predicate_fuzzer = GrammarFuzzer(grammar, start_symbol="<predicate_list>")
        #self.str_fuzzer = GrammarFuzzer(grammar, start_symbol="<str>")

    def _generate_parameters(
        self, required: List[str], parameters: List[str], output_prob=0.5
    ):
        selection = required + random.sample(
            parameters, random.randint(0, len(parameters))
        )
        params = list()
        if "output" in selection:
            if random.random() < output_prob:
                params.append("-o")
            else:
                params.append("-otest.log")
        if "variables" in selection:
            params.append("-v" + self.variables_fuzzer.fuzz())
        if "depth" in selection:
            params.append(f"-d{random.randint(1, 5)}")
        if "prefix" in selection:
            params.append("-p" + self.str_fuzzer.fuzz())
        if "watch" in selection:
            params.append("-w" + self.variables_fuzzer.fuzz())
        if "custom_repr" in selection:
            params.append("-c" + self.predicate_fuzzer.fuzz())
        if "overwrite" in selection and "output" in selection and "-o" not in params:
            params.append("-O")
        if "thread_info" in selection:
            params.append("-T")
        return params

    @abstractmethod
    def _get_failing_params(self):
        return []

    @abstractmethod
    def _get_passing_params(self):
        return []

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        params = self._get_failing_params()
        random.shuffle(params)
        return "\n".join(params), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        params = self._get_passing_params()
        random.shuffle(params)
        return "\n".join(params), TestResult.PASSING