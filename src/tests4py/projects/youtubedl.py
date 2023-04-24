from os import PathLike
from pathlib import Path
from typing import List, Optional

from tests4py.framework.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


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
        test_cases=['test.test_utils.TestUtil.test_match_str']
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
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        return TestResult.UNDEFINED
