from pathlib import Path
from typing import List, Optional

from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, ExpectErrAPI

PROJECT_MAME = "youtubedl"


class YoutubeDL(Project):
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
            github_url="https://github.com/ytdl-org/youtube-dl",
            status=Status.OK,
            python_version="3.7.0",
            darwin_python_version="3.7.12",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.UNITTEST,
            test_files=test_files,
            test_cases=test_cases,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
            loc=loc,
            relevant_test_files=relevant_test_files,
        )  # TODO adjust parameters


def register():
    YoutubeDL(
        bug_id=1,
        buggy_commit_id="99036a1298089068dcf80c0985bfcc3f8c24f281",
        fixed_commit_id="1cc47c667419e0eadc0a6989256ab7b276852adf",
        test_files=[Path("test", "test_utils.py")],
        test_cases=["test.test_utils.TestUtil.test_match_str"],
        api=YoutubeDLAPI(b"Input does not match the expected outcome!"),
        # unittests=YoutubeDLUnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=3,
        buggy_commit_id="f5469da9e6e259c1690c7ef54f1da1c19f65036f",
        fixed_commit_id="95f3f7c20a05e7ac490e768b8470b20538ef8581",
        test_files=[Path("test", "test_utils.py")],
        test_cases=["test.test_utils.TestUtil.test_unescape_html"],
        api=YoutubeDLAPI(b"Input does not match the expected outcome!"),
        # unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),
    )

    YoutubeDL(
        bug_id=43,
        buggy_commit_id="cecaaf3f58ad9f544dbb79af1e565d9353fa2b2d",
        fixed_commit_id="d6c7a367e88096bb17e323954002c084477fe908",
        test_files=[Path("test", "test_utils.py")],
        test_cases=["test.test_utils.TestUtil.test_url_basename"],
        api=YoutubeDLAPI(b"Input does not match the expected outcome!"),
        # unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),
    )


class YoutubeDLAPI(ExpectErrAPI):
    pass


class YoutubeDLSystemtestGenerator(SystemtestGenerator):
    pass
