from os import PathLike
from pathlib import Path
from typing import List, Optional, Any, Tuple

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult, ExpectErrAPI


class YoutubeDL(Project):
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
            loc: int = 0,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="youtubedl",
            github_url="https://github.com/ytdl-org/youtube-dl",
            status=Status.OK,
            cause="N.A.",
            python_version="3.7.0",
            darwin_python_version="3.7.12",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.UNITTEST,
            test_file=test_file,
            test_cases=test_cases,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
            loc=loc,
        )  # TODO adjust parameters


def register():

    YoutubeDL(
        bug_id=1,
        buggy_commit_id='99036a1298089068dcf80c0985bfcc3f8c24f281',
        fixed_commit_id='1cc47c667419e0eadc0a6989256ab7b276852adf',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_match_str'],
        api=YoutubeDLAPI(
            b"Input does not match the expected outcome!"
        ),
        # unittests=YoutubeDLUnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),

    )

    YoutubeDL(
        bug_id=3,
        buggy_commit_id='f5469da9e6e259c1690c7ef54f1da1c19f65036f',
        fixed_commit_id='95f3f7c20a05e7ac490e768b8470b20538ef8581',
        test_file=[Path('test', 'test_utils.py')],
        test_cases=['test.test_utils.TestUtil.test_unescape_html'],
        api=YoutubeDLAPI(
            b"Input does not match the expected outcome!"
        ),
        # unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),
    )


class YoutubeDLAPI(ExpectErrAPI):
    pass


class YoutubeDLSystemtestGenerator(SystemtestGenerator):
    pass
