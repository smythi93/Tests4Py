import ast
import base64
import calendar
import codecs
import datetime
import email.utils
import json
import os
import random
import re
import string
import subprocess
from pathlib import Path
from typing import Any, List, Optional, Tuple

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up, INTEGER, NUMBER
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, ExpectErrAPI, TestResult

PROJECT_NAME = "youtubedl"


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
        grammar: Optional[Grammar] = None,
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
        skip_tests: Optional[List[str]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/ytdl-org/youtube-dl",
            status=Status.OK,
            python_version="3.7.12",
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
            source_base=Path("youtube_dl"),
            test_base=Path("test"),
            included_files=["youtube_dl"],
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
            ],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )

    def _path_import_error(self, location: Path, imported: str):
        with open(location / "test" / "test_utils.py", "r") as f:
            content = f.read()
        content = content.replace(f"\n    {imported},", "")
        content = content.replace(
            "from youtube_dl.utils import (",
            "try:\n"
            f"    from youtube_dl.utils import {imported}\n"
            "except ImportError:\n"
            "    pass\n"
            "from youtube_dl.utils import (",
        )
        with open(location / "test" / "test_utils.py", "w") as f:
            f.write(content)

    def patch(self, location: Path):
        if self.bug_id == 38:
            self._path_import_error(location, "urlencode_postdata")
        elif self.bug_id == 39:
            self._path_import_error(location, "limit_length")
        elif self.bug_id == 40:
            self._path_import_error(location, "struct_unpack")
        elif self.bug_id == 42:
            self._path_import_error(location, "fix_xml_ampersands")


def register():
    YoutubeDL(
        bug_id=1,
        buggy_commit_id="99036a1298089068dcf80c0985bfcc3f8c24f281",
        fixed_commit_id="1cc47c667419e0eadc0a6989256ab7b276852adf",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_match_str")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL1API(),
        unittests=YTDL1UnittestGenerator(),
        systemtests=YTDL1SystemtestGenerator(),
        grammar=grammar_base64,
        loc=105970,
    )
    YoutubeDL(
        bug_id=2,
        buggy_commit_id="84f085d4bdb66ee025fb337bcd571eab7469da97",
        fixed_commit_id="9d6ac71c27b1dfb662c795ef598dbfd0286682da",
        test_files=[Path("test", "test_InfoExtractor.py")],
        test_cases=[
            os.path.join(
                "test",
                "test_InfoExtractor.py::TestInfoExtractor::test_parse_mpd_formats",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "test",
                "test_InfoExtractor.py::TestInfoExtractor",
            )
        ],
        api=YTDL2API(),
        unittests=YTDL2UnittestGenerator(),
        systemtests=YTDL2SystemtestGenerator(),
        grammar=grammar_base64,
        loc=102715,
    )
    YoutubeDL(
        bug_id=3,
        buggy_commit_id="f5469da9e6e259c1690c7ef54f1da1c19f65036f",
        fixed_commit_id="95f3f7c20a05e7ac490e768b8470b20538ef8581",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_unescape_html")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL3API(),
        unittests=YTDL3UnittestGenerator(),
        systemtests=YTDL3SystemtestGenerator(),
        grammar=grammar_unescape,
        loc=99746,
    )
    YoutubeDL(
        bug_id=4,
        buggy_commit_id="bc40b3a5ba44006c23daf7fe0ed872af5e33bdc5",
        fixed_commit_id="189935f15960300d316e8b07108b076ac6c2186a",
        test_files=[Path("test", "test_jsinterp.py")],
        test_cases=[
            os.path.join("test", "test_jsinterp.py::TestJSInterpreter::test_call")
        ],
        relevant_test_files=[
            os.path.join("test", "test_jsinterp.py::TestJSInterpreter")
        ],
        api=YTDL4API(),
        unittests=YTDL4UnittestGenerator(),
        systemtests=YTDL4SystemtestGenerator(),
        grammar=grammar_base64,
        loc=88008,
    )
    YoutubeDL(
        bug_id=5,
        buggy_commit_id="b02b960c6bba834d9e7199ac53430c7933079dc8",
        fixed_commit_id="7dc2a74e0ac9cfa74cc9de6f586ffd5cc8bac0d9",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_unified_timestamps")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL5API(),
        unittests=YTDL5UnittestGenerator(),
        systemtests=YTDL5SystemtestGenerator(),
        grammar=grammar_base64,
        loc=81459,
    )
    YoutubeDL(
        bug_id=6,
        buggy_commit_id="4f29fa99069760dc47ef9ca5dbf607a567d2982f",
        fixed_commit_id="d631d5f9f27f93767226192e4288990413fa9dbd",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_parse_dfxp_time_expr")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL6API(),
        unittests=YTDL6UnittestGenerator(),
        systemtests=YTDL6SystemtestGenerator(),
        grammar=grammar_dfxp_time,
        loc=63540,
    )
    YoutubeDL(
        bug_id=7,
        buggy_commit_id="63a64948342ebfe46db8c258765e698a04a61904",
        fixed_commit_id="d01949dc89feb2441f251e42e8a6bfa4711b9715",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_js_to_json_realworld")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL7API(),
        unittests=YTDL7UnittestGenerator(),
        systemtests=YTDL7SystemtestGenerator(),
        grammar=grammar_base64,
        loc=61208,
    )
    YoutubeDL(
        bug_id=8,
        buggy_commit_id="cf2ac6df6896dac4d23918867bb86fac1e1088d9",
        fixed_commit_id="f5f4a27a964b41646303921104f4d6d6fd2098e4",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join(
                "test",
                "test_YoutubeDL.py::TestFormatSelection::test_youtube_format_selection",
            )
        ],
        relevant_test_files=[
            os.path.join("test", "test_YoutubeDL.py::TestFormatSelection")
        ],
        api=YTDL8API(),
        unittests=YTDL8UnittestGenerator(),
        systemtests=YTDL8SystemtestGenerator(),
        grammar=grammar_base64,
        loc=55356,
    )
    YoutubeDL(
        bug_id=9,
        buggy_commit_id="0130afb76e5cb6f470f39f127c8d09eea3e82d0d",
        fixed_commit_id="cf2ac6df6896dac4d23918867bb86fac1e1088d9",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join(
                "test",
                "test_YoutubeDL.py::TestFormatSelection::test_youtube_format_selection",
            )
        ],
        relevant_test_files=[
            os.path.join("test", "test_YoutubeDL.py::TestFormatSelection")
        ],
        api=YTDL9API(),
        unittests=YTDL9UnittestGenerator(),
        systemtests=YTDL9SystemtestGenerator(),
        grammar=grammar_base64,
        loc=55351,
    )
    YoutubeDL(
        bug_id=10,
        buggy_commit_id="85d586617750d38d742a24f141b099f6b898d269",
        fixed_commit_id="d305dd73a3d6927f0a2c63d08662a183fa173833",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_js_to_json_realworld")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL10API(),
        unittests=YTDL10UnittestGenerator(),
        systemtests=YTDL10SystemtestGenerator(),
        grammar=grammar_base64,
        loc=46060,
    )
    YoutubeDL(
        bug_id=11,
        buggy_commit_id="b568561eba6f4aceb87419e21aba11567c5de7da",
        fixed_commit_id="348c6bf1c1a00eec323d6e21ff7b9b12699afe04",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_str_to_int")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL11API(),
        unittests=YTDL11UnittestGenerator(),
        systemtests=YTDL11SystemtestGenerator(),
        grammar=grammar_11,
        loc=113981,
    )
    YoutubeDL(
        bug_id=12,
        buggy_commit_id="435e382423f860aca82a58d7c3db58cbfa242b40",
        fixed_commit_id="e118a8794ffe5a3a414afd489726f34d753b0b23",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join(
                "test",
                "test_YoutubeDL.py::TestFormatSelection::test_format_selection_string_ops",
            )
        ],
        relevant_test_files=[
            os.path.join("test", "test_YoutubeDL.py::TestFormatSelection")
        ],
        api=YTDL12API(),
        unittests=YTDL12UnittestGenerator(),
        systemtests=YTDL12SystemtestGenerator(),
        grammar=grammar_base64,
        loc=111758,
    )
    YoutubeDL(
        bug_id=13,
        buggy_commit_id="6945b9e78f38284eb4e440b7badea2fc60b66c2f",
        fixed_commit_id="fad4ceb53404227f471af2f3544c4c14a5df4acb",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_urljoin")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL13API(),
        unittests=YTDL13UnittestGenerator(),
        systemtests=YTDL13SystemtestGenerator(),
        grammar=grammar_url_pair,
        loc=111662,
    )
    YoutubeDL(
        bug_id=14,
        buggy_commit_id="562de77f41d0c08df9dbb08cfa86ba6c7d239c5a",
        fixed_commit_id="84213ea8d41d5fe1608333a16ac578dccdf9a915",
        test_files=[Path("test", "test_youtube_chapters.py")],
        test_cases=[
            os.path.join(
                "test",
                "test_youtube_chapters.py::TestYoutubeChapters::test_youtube_chapters",
            )
        ],
        relevant_test_files=[
            os.path.join("test", "test_youtube_chapters.py"),
            os.path.join("test", "test_youtube_lists.py"),
            os.path.join("test", "test_youtube_signature.py"),
        ],
        skip_tests=[
            "test_youtube_course",
            "test_youtube_mix",
        ],
        api=YTDL14API(),
        unittests=YTDL14UnittestGenerator(),
        systemtests=YTDL14SystemtestGenerator(),
        grammar=grammar_base64,
        loc=115095,
    )
    YoutubeDL(
        bug_id=15,
        buggy_commit_id="e7f3529f68ee7c8ca78366d37f851cb31fa00f31",
        fixed_commit_id="c384d537f882efab10a78a56ce6dcb0a30f54b47",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_js_to_json_edgecases"),
            os.path.join("test", "test_utils.py::TestUtil::test_js_to_json_realworld"),
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL15API(),
        unittests=YTDL15UnittestGenerator(),
        systemtests=YTDL15SystemtestGenerator(),
        grammar=grammar_base64,
        loc=103448,
    )
    YoutubeDL(
        bug_id=16,
        buggy_commit_id="68d43a61b552007a718894967b869c0f1d8ff00f",
        fixed_commit_id="3869028ffb6be6ab719e5cf1004276dfdfd1216d",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_dfxp2srt")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL16API(),
        unittests=YTDL16UnittestGenerator(),
        systemtests=YTDL16SystemtestGenerator(),
        grammar=grammar_base64,
        loc=100529,
    )
    YoutubeDL(
        bug_id=17,
        buggy_commit_id="4bf22f7a1014c55e3358b5a419945071b152eafc",
        fixed_commit_id="5b232f46dcbdc805507c02edd4fd598f31d544d5",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_cli_bool_option")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL17API(),
        unittests=YTDL17UnittestGenerator(),
        systemtests=YTDL17SystemtestGenerator(),
        grammar=grammar_17,
        loc=99349,
    )
    YoutubeDL(
        bug_id=18,
        buggy_commit_id="dc6520aa3d1fe7afc52613e392f15dde90af4844",
        fixed_commit_id="0396806f671e5828c2abdeb8048acf8b654507b6",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join(
                "test",
                "test_YoutubeDL.py::TestYoutubeDL::test_do_not_override_ie_key_in_url_transparent",
            )
        ],
        relevant_test_files=[os.path.join("test", "test_YoutubeDL.py::TestYoutubeDL")],
        api=YTDL18API(),
        unittests=YTDL18UnittestGenerator(),
        systemtests=YTDL18SystemtestGenerator(),
        grammar=grammar_base64,
        loc=98722,
    )
    YoutubeDL(
        bug_id=19,
        buggy_commit_id="9a0942ad55bba714d6eaeb9ee4f66a138ec85e17",
        fixed_commit_id="15da37c7dc8cf14ba5ce880aa1805fceaa71fc44",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join(
                "test", "test_YoutubeDL.py::TestYoutubeDL::test_prepare_filename"
            )
        ],
        relevant_test_files=[os.path.join("test", "test_YoutubeDL.py::TestYoutubeDL")],
        api=YTDL19API(),
        unittests=YTDL19UnittestGenerator(),
        systemtests=YTDL19SystemtestGenerator(),
        grammar=grammar_base64,
        loc=98372,
    )
    YoutubeDL(
        bug_id=20,
        buggy_commit_id="b6c9fe416243373bcb59eb8aa5ef0baca8f3c97c",
        fixed_commit_id="609ff8ca19f1c4c168a81121074b91cc0f0d4c47",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join(
                "test", "test_utils.py::TestUtil::test_get_element_by_attribute"
            )
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL20API(),
        unittests=YTDL20UnittestGenerator(),
        systemtests=YTDL20SystemtestGenerator(),
        grammar=grammar_base64,
        loc=98099,
    )
    YoutubeDL(
        bug_id=21,
        buggy_commit_id="96182695e4e37795a30ab143129c91dab18a9865",
        fixed_commit_id="4b5de77bdb7765df4797bf068592926285ba709a",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_urljoin")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL21API(),
        unittests=YTDL21UnittestGenerator(),
        systemtests=YTDL21SystemtestGenerator(),
        grammar=grammar_url_mode,
        loc=93977,
    )
    YoutubeDL(
        bug_id=22,
        buggy_commit_id="1bd05345ea4b91598ec04b8e0d33fd14f9e2eddc",
        fixed_commit_id="db13c16ef8968613680e2bbc85f373c3e74faf98",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join("test", "test_YoutubeDL.py::TestYoutubeDL::test_match_filter")
        ],
        relevant_test_files=[os.path.join("test", "test_YoutubeDL.py::TestYoutubeDL")],
        api=YTDL22API(),
        unittests=YTDL22UnittestGenerator(),
        systemtests=YTDL22SystemtestGenerator(),
        grammar=grammar_base64,
        loc=92521,
    )
    YoutubeDL(
        bug_id=23,
        buggy_commit_id="a22b2fd19bd8c08d50f884d1903486d4f00f76ec",
        fixed_commit_id="b3ee552e4b918fb720111b23147e24fa5475a74b",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_js_to_json_edgecases")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL23API(),
        unittests=YTDL23UnittestGenerator(),
        systemtests=YTDL23SystemtestGenerator(),
        grammar=grammar_base64,
        loc=91393,
    )
    YoutubeDL(
        bug_id=24,
        buggy_commit_id="2c6da7df4a4d69ec933688e3c53795fd3436a1c6",
        fixed_commit_id="e5a088dc4be4fdcc96927a9f1b7284d4cd49c415",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join("test", "test_YoutubeDL.py::TestYoutubeDL::test_match_filter")
        ],
        relevant_test_files=[os.path.join("test", "test_YoutubeDL.py::TestYoutubeDL")],
        api=YTDL24API(),
        unittests=YTDL24UnittestGenerator(),
        systemtests=YTDL24SystemtestGenerator(),
        grammar=grammar_base64,
        loc=87341,
    )
    YoutubeDL(
        bug_id=25,
        buggy_commit_id="9e5751b9fe72f7425e4cb3f22a56b6a95b59e41d",
        fixed_commit_id="e4659b45474acb563db0ab4284abdfc80837307e",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_js_to_json_realworld")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL25API(),
        unittests=YTDL25UnittestGenerator(),
        systemtests=YTDL25SystemtestGenerator(),
        grammar=grammar_base64,
        loc=82484,
    )
    YoutubeDL(
        bug_id=26,
        buggy_commit_id="4c93ee8d14dc081d413304d2d2eb694cb62cc71a",
        fixed_commit_id="47212f7bcbd59af40f91796562a6b72ba0439ac4",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_js_to_json_realworld")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL26API(),
        unittests=YTDL26UnittestGenerator(),
        systemtests=YTDL26SystemtestGenerator(),
        grammar=grammar_base64,
        loc=78267,
    )
    YoutubeDL(
        bug_id=27,
        buggy_commit_id="d631d5f9f27f93767226192e4288990413fa9dbd",
        fixed_commit_id="db2fe38b5508cbd28b89893219d9cccd41406851",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_parse_dfxp_time_expr")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL27API(),
        unittests=YTDL27UnittestGenerator(),
        systemtests=YTDL27SystemtestGenerator(),
        grammar=grammar_dfxp_time,
        loc=63545,
    )
    YoutubeDL(
        bug_id=28,
        buggy_commit_id="bd1512d19649c280197729814766d590ea6c023b",
        fixed_commit_id="7aefc49c4013efb5056b2c1237e22c52cb5d3c49",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_unescape_html")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL28API(),
        unittests=YTDL28UnittestGenerator(),
        systemtests=YTDL28SystemtestGenerator(),
        grammar=grammar_entity,
        loc=62209,
    )
    YoutubeDL(
        bug_id=29,
        buggy_commit_id="c514b0ec655b23e7804eb18df04daa863d973f32",
        fixed_commit_id="6a750402787dfc1f39a9ad347f2d78ae1c94c52c",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_unified_dates")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL29API(),
        unittests=YTDL29UnittestGenerator(),
        systemtests=YTDL29SystemtestGenerator(),
        grammar=grammar_base64,
        loc=61673,
    )
    YoutubeDL(
        bug_id=30,
        buggy_commit_id="f5f4a27a964b41646303921104f4d6d6fd2098e4",
        fixed_commit_id="bb8e55366289e0c129ef85abb8c1ac1cbae86a66",
        test_files=[Path("test", "test_YoutubeDL.py")],
        test_cases=[
            os.path.join(
                "test", "test_YoutubeDL.py::TestFormatSelection::test_format_filtering"
            )
        ],
        relevant_test_files=[
            os.path.join("test", "test_YoutubeDL.py::TestFormatSelection")
        ],
        api=YTDL30API(),
        unittests=YTDL30UnittestGenerator(),
        systemtests=YTDL30SystemtestGenerator(),
        grammar=grammar_base64,
        loc=55355,
    )
    YoutubeDL(
        bug_id=31,
        buggy_commit_id="ab07963b5cc79812c6fb7e4f9e363533d8123830",
        fixed_commit_id="e8df5cee12378acd708b6686130a73c5edc06f0e",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_parse_duration")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL31API(),
        unittests=YTDL31UnittestGenerator(),
        systemtests=YTDL31SystemtestGenerator(),
        grammar=grammar_duration,
        loc=38981,
    )
    YoutubeDL(
        bug_id=32,
        buggy_commit_id="bf951c5e29548cfed80480389762edd29fcc8825",
        fixed_commit_id="609a61e3e6fffce3d45e845f33ae2c5fa2d432ac",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_strip_jsonp")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL32API(),
        unittests=YTDL32UnittestGenerator(),
        systemtests=YTDL32SystemtestGenerator(),
        grammar=grammar_base64,
        loc=37509,
    )
    YoutubeDL(
        bug_id=33,
        buggy_commit_id="50c8266ef0b2b6d011257a909f47fd623dda8eb2",
        fixed_commit_id="6ad4013d40e839211e2896129eed05ccd40ee963",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_parse_iso8601")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        skip_tests=["test_compat_expanduser", "test_compat_getenv"],
        api=YTDL33API(),
        unittests=YTDL33UnittestGenerator(),
        systemtests=YTDL33SystemtestGenerator(),
        grammar=grammar_iso8601,
        loc=37170,
    )
    YoutubeDL(
        bug_id=34,
        buggy_commit_id="07e764439a1cdd3a3b95fbf21acc6a517c6a889e",
        fixed_commit_id="410f3e73ab268f74a455798ee39de5caba90caea",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_js_to_json")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL34API(),
        unittests=YTDL34UnittestGenerator(),
        systemtests=YTDL34SystemtestGenerator(),
        grammar=grammar_base64,
        loc=35342,
    )
    YoutubeDL(
        bug_id=35,
        buggy_commit_id="89294b5f50462ede8ba83463ff262eb2c5219e1b",
        fixed_commit_id="99b67fecc5ab6c57eada1e1678034dd71c57e338",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_unified_dates")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL35API(),
        unittests=YTDL35UnittestGenerator(),
        systemtests=YTDL35SystemtestGenerator(),
        grammar=grammar_base64,
        loc=35269,
    )
    YoutubeDL(
        bug_id=36,
        buggy_commit_id="173a7026d59bacfbfe7a8eea92e10ef6e89d1798",
        fixed_commit_id="a6da7b6b9657f621a927cb4c7bc46cf7c6c27b11",
        test_files=[Path("test", "test_all_urls.py")],
        test_cases=[
            os.path.join(
                "test", "test_all_urls.py::TestAllURLsMatching::test_facebook_matching"
            )
        ],
        relevant_test_files=[
            os.path.join("test", "test_all_urls.py::TestAllURLsMatching")
        ],
        api=YTDL36API(),
        unittests=YTDL36UnittestGenerator(),
        systemtests=YTDL36SystemtestGenerator(),
        grammar=grammar_base64,
        loc=29789,
    )
    YoutubeDL(
        bug_id=37,
        buggy_commit_id="98b7cf1acefe398f792ca6ff4c5f84f1b7785fcb",
        fixed_commit_id="676eb3f2dd542be3e84780b18388253382d3e465",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_uppercase_escpae")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL37API(),
        unittests=YTDL37UnittestGenerator(),
        systemtests=YTDL37SystemtestGenerator(),
        grammar=grammar_base64,
        loc=24035,
    )
    YoutubeDL(
        bug_id=38,
        buggy_commit_id="94eae04c94a43847e8ce7c9bf3d88dd029ef62f6",
        fixed_commit_id="b74fa8cd2c9deb412ac277c6cc44847c3839b844",
        test_files=[
            Path("test", "test_utils.py"),
        ],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_urlencode_postdata")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL38API(),
        unittests=YTDL38UnittestGenerator(),
        systemtests=YTDL38SystemtestGenerator(),
        grammar=grammar_postdata,
        loc=21863,
    )
    YoutubeDL(
        bug_id=39,
        buggy_commit_id="b04c8f735805ea2671429ac8d683c2887a6b4db8",
        fixed_commit_id="a020a0dc20ced6468ec46214c394f6f360735b1d",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_limit_length")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL39API(),
        unittests=YTDL39UnittestGenerator(),
        systemtests=YTDL39SystemtestGenerator(),
        grammar=grammar_limit,
        loc=33713,
    )
    YoutubeDL(
        bug_id=40,
        buggy_commit_id="6a7a38967976ea0d0b911c2965aaa74bed2976d7",
        fixed_commit_id="b53466e1680db3d710415329674c887d38af46c5",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_struct_unpack")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL40API(),
        unittests=YTDL40UnittestGenerator(),
        systemtests=YTDL40SystemtestGenerator(),
        grammar=grammar_struct,
        loc=20216,
    )
    YoutubeDL(
        bug_id=41,
        buggy_commit_id="81c2f20b5386d89a62dc27293654d75b77f47473",
        fixed_commit_id="026fcc04956f2077a50cd4b4e9b87f45d2bcddea",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_unified_dates")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL41API(),
        unittests=YTDL41UnittestGenerator(),
        systemtests=YTDL41SystemtestGenerator(),
        grammar=grammar_base64,
        loc=19672,
    )
    YoutubeDL(
        bug_id=42,
        buggy_commit_id="b853d2e1555dbb4a09fe3d7857c6d2bc044646f4",
        fixed_commit_id="5aafe895fce2a7be9595cb2e56b7bd73a748e6b6",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[
            os.path.join("test", "test_utils.py::TestUtil::test_fix_xml_ampersands")
        ],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL42API(),
        unittests=YTDL42UnittestGenerator(),
        systemtests=YTDL42SystemtestGenerator(),
        grammar=grammar_base64,
        loc=17770,
    )
    YoutubeDL(
        bug_id=43,
        buggy_commit_id="cecaaf3f58ad9f544dbb79af1e565d9353fa2b2d",
        fixed_commit_id="d6c7a367e88096bb17e323954002c084477fe908",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_url_basename")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YTDL43API(),
        unittests=YTDL43UnittestGenerator(),
        systemtests=YTDL43SystemtestGenerator(),
        grammar=grammar_url_single,
        loc=16339,
    )


class YoutubeDLAPI(ExpectErrAPI):
    pass


class YoutubeDLSystemtestGenerator(SystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class YTDLAPI(API):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# bug_11: ``str_to_int`` guarded only against ``None`` (``if int_str is
# None``) and then ran ``re.sub`` on its argument, so a non-string input
# such as an ``int`` raised ``TypeError``.  The fix returns the argument
# unchanged when it is not a ``compat_str``.
#
# System-test format:  ``<mode> <value>`` where ``<mode>`` is ``int`` (the
#   trigger: value is passed as an integer) or ``str`` (value is passed as
#   a numeric string).  The harness prints ``repr(str_to_int(value))``; the
#   oracle compares against the correct result.
# ======================================================================


class YTDL11API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            value = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "int":
            expected = repr(int(value))
        else:
            expected = repr(int(re.sub(r"[,\.\+]", "", value)))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL11TestGenerator:
    @staticmethod
    def generate_int() -> int:
        return random.randint(1, 10 ** random.randint(1, 7))

    @staticmethod
    def generate_numeric_string() -> Tuple[str, int]:
        n = random.randint(1000, 10 ** random.randint(4, 8))
        sep = random.choice((",", "."))
        text = f"{n:,}".replace(",", sep)
        return text, n


class YTDL11SystemtestGenerator(SystemtestGenerator, YTDL11TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"int {self.generate_int()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        text, _ = self.generate_numeric_string()
        return f"str {text}", TestResult.PASSING


class YTDL11UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL11TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="str_to_int")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(arg: ast.expr, expected: int) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="str_to_int"),
                            args=[arg],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self.generate_int()
        test = self.get_empty_test()
        test.body = self._assert(ast.Constant(value=n), n)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        text, n = self.generate_numeric_string()
        test = self.get_empty_test()
        test.body = self._assert(ast.Constant(value=text), n)
        return test, TestResult.PASSING


grammar_11: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <value>"],
            "<mode>": ["int", "str"],
            "<value>": ["<digit><rest>"],
            "<rest>": ["", "<sym><rest>"],
            "<sym>": srange(string.digits) + [",", ".", "+"],
            "<digit>": srange(string.digits),
        }
    )
)

assert is_valid_grammar(grammar_11)


# ======================================================================
# bug_13 & bug_21: ``urljoin`` recognised an absolute ``path`` only when it
# started with ``//`` or ``http(s)://`` (``^(?:https?:)?//``), so a path
# with any other scheme (e.g. ``rtmp://``) combined with a ``None``/non-http
# base returned ``None`` instead of the path.  The fix generalises the
# regex to ``^(?:[a-zA-Z][a-zA-Z0-9+-.]*:)?//``.
#
# System-test format:  ``<base> <path>`` where ``<base>`` is the literal
#   ``None`` (Python ``None``) or a URL.  The harness prints
#   ``repr(urljoin(base, path))``; the oracle compares against the fixed
#   ``urljoin``.  A scheme'd ``<path>`` with base ``None`` triggers the fault.
# ======================================================================


def _fixed_urljoin(base, path):
    if isinstance(path, bytes):
        path = path.decode("utf-8")
    if not isinstance(path, str) or not path:
        return None
    if re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+\-.]*:)?//", path):
        return path
    if isinstance(base, bytes):
        base = base.decode("utf-8")
    if not isinstance(base, str) or not re.match(r"^(?:https?:)?//", base):
        return None
    from urllib.parse import urljoin as _uj

    return _uj(base, path)


class YTDL13API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            base_tok = process.args[2]
            path = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        base = None if base_tok == "None" else base_tok
        expected = repr(_fixed_urljoin(base, path))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL13TestGenerator:
    _SCHEMES = ["rtmp", "rtsp", "ftp", "mms", "ftps", "rtmpe", "sftp", "rtmpt"]

    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def _host(self) -> str:
        return f"{self._word()}.{random.choice(('de', 'com', 'org', 'net', 'io'))}"

    def _rel_path(self) -> str:
        return "/" + "/".join(self._word() for _ in range(random.randint(1, 3)))

    def failing_pair(self) -> Tuple[str, str]:
        scheme = random.choice(self._SCHEMES)
        path = f"{scheme}://{self._host()}{self._rel_path()}"
        return "None", path

    def passing_pair(self) -> Tuple[str, str]:
        base = f"http://{self._host()}/"
        return base, self._rel_path()


class YTDL13SystemtestGenerator(SystemtestGenerator, YTDL13TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        base, path = self.failing_pair()
        return f"{base} {path}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        base, path = self.passing_pair()
        return f"{base} {path}", TestResult.PASSING


class YTDL13UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL13TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="urljoin")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(base, path: str, expected) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="urljoin"),
                            args=[ast.Constant(value=base), ast.Constant(value=path)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _base, path = self.failing_pair()
        test = self.get_empty_test()
        test.body = self._assert(None, path, _fixed_urljoin(None, path))
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        base, path = self.passing_pair()
        test = self.get_empty_test()
        test.body = self._assert(base, path, _fixed_urljoin(base, path))
        return test, TestResult.PASSING


grammar_url_pair: Grammar = clean_up(
    dict(
        {
            "<start>": ["<token> <token>"],
            "<token>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(
                string.ascii_letters + string.digits
            )
            + [":", "/", ".", "-", "+", "_"],
        }
    )
)

assert is_valid_grammar(grammar_url_pair)


# ======================================================================
# bug_21: ``urljoin`` did not decode ``bytes`` arguments, so a ``bytes``
# ``base`` or ``path`` failed the ``isinstance(..., compat_str)`` check and
# the function returned ``None`` instead of joining.  The fix decodes both
# ``base`` and ``path`` from ``bytes`` first.
#
# System-test format:  ``<mode> <base> <path>`` where ``<mode>`` is two
#   chars (``b``/``s`` for base and path) marking which argument is passed
#   as ``bytes``.  Any ``b`` triggers the fault; ``ss`` does not.  The
#   harness prints ``repr(urljoin(base, path))`` and the oracle compares to
#   the fixed ``urljoin``.
# ======================================================================


def _encode_pair(mode: str, base: str, path: str):
    b = base.encode("utf-8") if mode[0] == "b" else base
    p = path.encode("utf-8") if mode[1] == "b" else path
    return b, p


class YTDL21API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            base = process.args[3]
            path = process.args[4]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        b, p = _encode_pair(mode, base, path)
        expected = repr(_fixed_urljoin(b, p))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL21TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def _host(self) -> str:
        return f"{self._word()}.{random.choice(('de', 'com', 'org', 'net'))}"

    def _rel_path(self) -> str:
        return "/" + "/".join(self._word() for _ in range(random.randint(1, 3)))

    def failing_case(self) -> Tuple[str, str, str]:
        mode = random.choice(("bb", "bs", "sb"))
        return mode, f"http://{self._host()}/", self._rel_path()

    def passing_case(self) -> Tuple[str, str, str]:
        return "ss", f"http://{self._host()}/", self._rel_path()


class YTDL21SystemtestGenerator(SystemtestGenerator, YTDL21TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        mode, base, path = self.failing_case()
        return f"{mode} {base} {path}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode, base, path = self.passing_case()
        return f"{mode} {base} {path}", TestResult.PASSING


class YTDL21UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL21TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="urljoin")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(mode: str, base: str, path: str) -> List[ast.stmt]:
        b, p = _encode_pair(mode, base, path)
        expected = _fixed_urljoin(b, p)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="urljoin"),
                            args=[ast.Constant(value=b), ast.Constant(value=p)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        mode, base, path = self.failing_case()
        test = self.get_empty_test()
        test.body = self._assert(mode, base, path)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        mode, base, path = self.passing_case()
        test = self.get_empty_test()
        test.body = self._assert(mode, base, path)
        return test, TestResult.PASSING


grammar_url_mode: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <token> <token>"],
            "<mode>": ["bb", "bs", "sb", "ss"],
            "<token>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_letters + string.digits)
            + [":", "/", ".", "-", "+", "_"],
        }
    )
)

assert is_valid_grammar(grammar_url_mode)


# ======================================================================
# bug_17: ``cli_bool_option`` fetched ``param = params.get(param)`` and then
# ran ``assert isinstance(param, bool)``, so a missing key (``None``) raised
# ``AssertionError``.  The fix returns ``[]`` when ``param`` is ``None``.
#
# System-test format:  ``<present> <bool> <key> <option>`` where
#   ``<present>`` is ``yes``/``no`` (whether ``<key>`` is in the params
#   dict).  ``no`` triggers the fault.  The harness prints
#   ``repr(cli_bool_option(params, option, key))``; the oracle compares to
#   the fixed behaviour.
# ======================================================================


class YTDL17API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            present = process.args[2]
            boolval = process.args[3]
            option = process.args[5]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        if present == "no":
            expected = repr([])
        else:
            expected = repr([option, "true" if boolval == "True" else "false"])
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL17TestGenerator:
    @staticmethod
    def _key() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 10)))

    def _option(self) -> str:
        return "--" + "-".join(
            "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 6)))
            for _ in range(random.randint(1, 3))
        )

    def failing_case(self) -> Tuple[str, str, str, str]:
        return "no", random.choice(("True", "False")), self._key(), self._option()

    def passing_case(self) -> Tuple[str, str, str, str]:
        return (
            "yes",
            random.choice(("True", "False")),
            self._key(),
            self._option(),
        )


class YTDL17SystemtestGenerator(SystemtestGenerator, YTDL17TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        present, boolval, key, option = self.failing_case()
        return f"{present} {boolval} {key} {option}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        present, boolval, key, option = self.passing_case()
        return f"{present} {boolval} {key} {option}", TestResult.PASSING


class YTDL17UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL17TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="cli_bool_option")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(present: str, boolval: str, key: str, option: str) -> List[ast.stmt]:
        if present == "no":
            params = {}
            expected = []
        else:
            params = {key: boolval == "True"}
            expected = [option, "true" if boolval == "True" else "false"]
        params_ast = ast.Dict(
            keys=[ast.Constant(value=k) for k in params],
            values=[ast.Constant(value=v) for v in params.values()],
        )
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.List(elts=[ast.Constant(value=e) for e in expected]),
                        ast.Call(
                            func=ast.Name(id="cli_bool_option"),
                            args=[
                                params_ast,
                                ast.Constant(value=option),
                                ast.Constant(value=key),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        present, boolval, key, option = self.failing_case()
        test = self.get_empty_test()
        test.body = self._assert(present, boolval, key, option)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        present, boolval, key, option = self.passing_case()
        test = self.get_empty_test()
        test.body = self._assert(present, boolval, key, option)
        return test, TestResult.PASSING


grammar_17: Grammar = clean_up(
    dict(
        {
            "<start>": ["<present> <bool> <key> <option>"],
            "<present>": ["yes", "no"],
            "<bool>": ["True", "False"],
            "<key>": ["<lower><lowers>"],
            "<lowers>": ["", "<lower><lowers>"],
            "<lower>": srange(string.ascii_lowercase),
            "<option>": ["--<seg>"],
            "<seg>": ["<lower><segrest>"],
            "<segrest>": ["", "<segc><segrest>"],
            "<segc>": srange(string.ascii_lowercase) + ["-"],
        }
    )
)

assert is_valid_grammar(grammar_17)


# ======================================================================
# bug_31: ``parse_duration`` required a trailing seconds group, so
# minutes-only / hours-only strings such as ``"3 min"`` or ``"2.5 hours"``
# did not match and returned ``None``.  The fix adds ``only_mins`` /
# ``only_hours`` alternatives.
#
# System-test format:  a duration string (may contain a space, e.g.
#   ``"3 min"``; the harness re-joins argv).  Minutes/hours-only strings
#   trigger the fault; colon / seconds strings do not.  The harness prints
#   ``repr(parse_duration(s))`` and the oracle compares to the fixed impl.
# ======================================================================


def _float_or_none(v, scale=1, invscale=1, default=None):
    if v is None:
        return default
    try:
        return float(v) * invscale / scale
    except (ValueError, TypeError):
        return default


def _fixed_parse_duration(s):
    if s is None:
        return None
    s = s.strip()
    m = re.match(
        r"""(?ix)T?
        (?:
            (?P<only_mins>[0-9.]+)\s*(?:mins?|minutes?)\s*|
            (?P<only_hours>[0-9.]+)\s*(?:hours?)|

            (?:
                (?:(?P<hours>[0-9]+)\s*(?:[:h]|hours?)\s*)?
                (?P<mins>[0-9]+)\s*(?:[:m]|mins?|minutes?)\s*
            )?
            (?P<secs>[0-9]+)(?P<ms>\.[0-9]+)?\s*(?:s|secs?|seconds?)?
        )$""",
        s,
    )
    if not m:
        return None
    if m.group("only_mins"):
        return _float_or_none(m.group("only_mins"), invscale=60)
    if m.group("only_hours"):
        return _float_or_none(m.group("only_hours"), invscale=60 * 60)
    res = 0
    if m.group("secs"):
        res += int(m.group("secs"))
    if m.group("mins"):
        res += int(m.group("mins")) * 60
    if m.group("hours"):
        res += int(m.group("hours")) * 60 * 60
    if m.group("ms"):
        res += float(m.group("ms"))
    return res


class YTDL31API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        s = " ".join(process.args[2:])
        expected = repr(_fixed_parse_duration(s))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL31TestGenerator:
    _MIN_UNITS = ["min", "mins", "minute", "minutes"]
    _HOUR_UNITS = ["hour", "hours"]

    @staticmethod
    def _num() -> str:
        if random.random() < 0.5:
            return str(random.randint(1, 300))
        return f"{random.randint(1, 20)}.{random.randint(1, 9)}"

    def failing_str(self) -> str:
        unit = random.choice(self._MIN_UNITS + self._HOUR_UNITS)
        sep = random.choice((" ", ""))
        return f"{self._num()}{sep}{unit}"

    def passing_str(self) -> str:
        kind = random.choice(("hms", "ms", "s"))
        if kind == "hms":
            return f"{random.randint(0, 23)}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
        if kind == "ms":
            return f"{random.randint(0, 59)}:{random.randint(0, 59):02d}"
        return f"{random.randint(1, 5000)}s"


class YTDL31SystemtestGenerator(SystemtestGenerator, YTDL31TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.failing_str(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.passing_str(), TestResult.PASSING


class YTDL31UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL31TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="parse_duration")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(s: str) -> List[ast.stmt]:
        expected = _fixed_parse_duration(s)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="parse_duration"),
                            args=[ast.Constant(value=s)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.failing_str())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.passing_str())
        return test, TestResult.PASSING


grammar_duration: Grammar = clean_up(
    dict(
        {
            "<start>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_lowercase + string.digits + ": ."),
        }
    )
)

assert is_valid_grammar(grammar_duration)


# A base64 (urlsafe) payload grammar reused where the raw test input would
# otherwise contain shell-hostile characters (quotes, newlines, parens).
grammar_base64: Grammar = clean_up(
    dict(
        {
            "<start>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_letters + string.digits + "-_="),
        }
    )
)

assert is_valid_grammar(grammar_base64)


# ======================================================================
# bug_32: ``strip_jsonp`` did not strip trailing ``// ...`` comment lines,
# so a JSONP payload ending in a comment was returned unchanged.  The fix
# appends ``(?://[^\n]*)*`` to the regex.
#
# System-test format:  a urlsafe-base64 encoding of the JSONP code (chosen
#   to survive shlex splitting).  A code with a trailing ``//comment``
#   triggers the fault.  The harness decodes, runs ``strip_jsonp`` and
#   prints ``repr(result)``; the oracle compares to the fixed impl.
# ======================================================================


def _fixed_strip_jsonp(code):
    return re.sub(
        r"(?s)^[a-zA-Z0-9_]+\s*\(\s*(.*)\);?\s*?(?://[^\n]*)*$", r"\1", code
    )


def _b64(s: str) -> str:
    return base64.urlsafe_b64encode(s.encode("utf-8")).decode("ascii")


class YTDL32API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            code = base64.urlsafe_b64decode(process.args[2]).decode("utf-8")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_strip_jsonp(code))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL32TestGenerator:
    @staticmethod
    def _ident() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))

    def _json(self) -> str:
        keys = [self._ident() for _ in range(random.randint(1, 3))]
        parts = []
        for k in keys:
            if random.random() < 0.5:
                parts.append(f'"{k}":{random.randint(0, 9999)}')
            else:
                parts.append(f'"{k}":"{self._ident()}"')
        return "{" + ",".join(parts) + "}"

    def failing_code(self) -> str:
        return f"{self._ident()}({self._json()})//{self._ident()}"

    def passing_code(self) -> str:
        tail = random.choice(("", ";"))
        return f"{self._ident()}({self._json()}){tail}"


class YTDL32SystemtestGenerator(SystemtestGenerator, YTDL32TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.failing_code()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.passing_code()), TestResult.PASSING


class YTDL32UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL32TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="strip_jsonp")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(code: str) -> List[ast.stmt]:
        expected = _fixed_strip_jsonp(code)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="strip_jsonp"),
                            args=[ast.Constant(value=code)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.failing_code())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.passing_code())
        return test, TestResult.PASSING


# ======================================================================
# bug_43: ``url_basename`` used ``(?:[^/?#]+/)?`` for the path prefix, which
# only allowed a single path segment, so URLs with 3+ segments (e.g.
# ``.../2010/05/sintel/trailer.mp4``) failed to match and returned ``''``.
# The fix relaxes the prefix to ``(?:[^?#]+/)?``.
#
# System-test format:  a URL string.  A URL with 3+ path segments triggers
#   the fault; a URL with 0-2 segments does not.  The harness prints
#   ``repr(url_basename(url))``; the oracle compares to the fixed impl.
# ======================================================================


def _fixed_url_basename(url):
    m = re.match(r"(?:https?:|)//[^/]+/(?:[^?#]+/)?([^/?#]+)/?(?:[?#]|$)", url)
    if not m:
        return ""
    return m.group(1)


class YTDL43API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            url = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_url_basename(url))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL43TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def _host(self) -> str:
        return f"{self._word()}.{random.choice(('de', 'com', 'org', 'net'))}"

    def _base(self) -> str:
        return f"{self._word()}.{random.choice(('mp4', 'txt', 'html', 'json'))}"

    def failing_url(self) -> str:
        segs = [self._word() for _ in range(random.randint(2, 4))]
        return f"http://{self._host()}/" + "/".join(segs) + "/" + self._base()

    def passing_url(self) -> str:
        if random.random() < 0.5:
            return f"http://{self._host()}/{self._base()}"
        return f"http://{self._host()}/{self._word()}/{self._base()}"


class YTDL43SystemtestGenerator(SystemtestGenerator, YTDL43TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.failing_url(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.passing_url(), TestResult.PASSING


class YTDL43UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL43TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="url_basename")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(url: str) -> List[ast.stmt]:
        expected = _fixed_url_basename(url)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="url_basename"),
                            args=[ast.Constant(value=url)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.failing_url())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.passing_url())
        return test, TestResult.PASSING


grammar_url_single: Grammar = clean_up(
    dict(
        {
            "<start>": ["<token>"],
            "<token>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.ascii_letters + string.digits)
            + [":", "/", ".", "-", "_", "?", "#", "="],
        }
    )
)

assert is_valid_grammar(grammar_url_single)


# ======================================================================
# bug_3 & bug_28: ``unescapeHTML`` used ``&([^;]+;)`` to find entities, so a
# ``&`` inside an entity-like run (e.g. ``&a&quot;``) was swallowed and the
# real trailing entity was never decoded.  The fix uses ``&([^&;]+;)`` so a
# ``&`` terminates the run.
#
# System-test format:  ``fail <junk> <entity>`` (builds ``&<junk>&<entity>;``
#   — the trigger) or ``pass <word>`` (a plain word).  The harness prints
#   ``repr(unescapeHTML(s))``; the oracle knows the decoded value of the few
#   entities used and compares to the fixed behaviour.
# ======================================================================

_HTML_ENTITY_MAP = {"quot": '"', "amp": "&", "lt": "<", "gt": ">", "apos": "'"}


class _UnescapeAPI(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            if mode == "fail":
                junk = process.args[3]
                entity = process.args[4]
                expected = repr(f"&{junk}{_HTML_ENTITY_MAP[entity]}")
            else:
                expected = repr(process.args[3])
        except (IndexError, KeyError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class _UnescapeTestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 8)))

    def failing_case(self) -> Tuple[str, str]:
        return self._word(), random.choice(list(_HTML_ENTITY_MAP))

    def passing_word(self) -> str:
        return self._word()


class _UnescapeSystemtestGenerator(SystemtestGenerator, _UnescapeTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        junk, entity = self.failing_case()
        return f"fail {junk} {entity}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"pass {self.passing_word()}", TestResult.PASSING


class _UnescapeUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, _UnescapeTestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="unescapeHTML")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(s: str, expected: str) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="unescapeHTML"),
                            args=[ast.Constant(value=s)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        junk, entity = self.failing_case()
        s = f"&{junk}&{entity};"
        expected = f"&{junk}{_HTML_ENTITY_MAP[entity]}"
        test = self.get_empty_test()
        test.body = self._assert(s, expected)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self.passing_word()
        test = self.get_empty_test()
        test.body = self._assert(word, word)
        return test, TestResult.PASSING


grammar_unescape: Grammar = clean_up(
    dict(
        {
            "<start>": ["fail <word> <entity>", "pass <word>"],
            "<entity>": list(_HTML_ENTITY_MAP),
            "<word>": ["<lower><lowers>"],
            "<lowers>": ["", "<lower><lowers>"],
            "<lower>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_unescape)


class YTDL3API(_UnescapeAPI):
    pass


class YTDL3SystemtestGenerator(_UnescapeSystemtestGenerator):
    pass


class YTDL3UnittestGenerator(_UnescapeUnittestGenerator):
    pass


# ======================================================================
# bug_28: ``_htmlentity_transform`` called ``compat_chr(int(numstr, base))``
# for numeric entities without guarding against out-of-range code points,
# so an entity like ``&#2013266066;`` raised ``ValueError``.  The fix wraps
# the conversion in ``try/except ValueError`` and falls back to the literal.
#
# System-test format:  ``<form> <value>`` where ``<form>`` is ``dec``/``hex``
#   and ``<value>`` is a decimal code point.  A value >= 0x110000 triggers
#   the fault.  The harness prints ``repr(unescapeHTML(entity))``; the
#   oracle compares to the fixed behaviour (literal for out-of-range).
# ======================================================================


def _entity_string(form: str, value: int) -> str:
    return f"&#{value};" if form == "dec" else f"&#x{value:x};"


class YTDL28API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            form = process.args[2]
            value = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        s = _entity_string(form, value)
        if value < 0x110000:
            expected = repr(chr(value))
        else:
            expected = repr(s)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL28TestGenerator:
    @staticmethod
    def _valid_value() -> int:
        # printable-ish code points below the surrogate range
        return random.randint(33, 55000)

    @staticmethod
    def _overflow_value() -> int:
        return random.randint(0x110000, 0x7FFFFFFF)

    def failing_case(self) -> Tuple[str, int]:
        return random.choice(("dec", "hex")), self._overflow_value()

    def passing_case(self) -> Tuple[str, int]:
        return random.choice(("dec", "hex")), self._valid_value()


class YTDL28SystemtestGenerator(SystemtestGenerator, YTDL28TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        form, value = self.failing_case()
        return f"{form} {value}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        form, value = self.passing_case()
        return f"{form} {value}", TestResult.PASSING


class YTDL28UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL28TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="unescapeHTML")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(form: str, value: int) -> List[ast.stmt]:
        s = _entity_string(form, value)
        expected = chr(value) if value < 0x110000 else s
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="unescapeHTML"),
                            args=[ast.Constant(value=s)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        form, value = self.failing_case()
        test = self.get_empty_test()
        test.body = self._assert(form, value)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        form, value = self.passing_case()
        test = self.get_empty_test()
        test.body = self._assert(form, value)
        return test, TestResult.PASSING


grammar_entity: Grammar = clean_up(
    dict({"<start>": ["<form> <integer>"], "<form>": ["dec", "hex"]}, **INTEGER)
)

assert is_valid_grammar(grammar_entity)


# ======================================================================
# bug_37: ``uppercase_escape`` used ``m.group(0).decode('unicode-escape')``,
# a Python-2 idiom; on Python 3 ``str`` has no ``.decode`` so any string
# containing a ``\\U########`` escape raised ``AttributeError``.  The fix
# uses ``codecs.getdecoder('unicode_escape')``.
#
# System-test format:  a urlsafe-base64 encoding of the input string (it
#   contains a backslash, hostile to shlex).  A string with a
#   ``\\U########`` escape triggers the fault.  The harness decodes and
#   prints ``repr(uppercase_escape(s))``; the oracle compares to the fix.
# ======================================================================


def _fixed_uppercase_escape(s: str) -> str:
    unicode_escape = codecs.getdecoder("unicode_escape")
    return re.sub(
        r"\\U[0-9a-fA-F]{8}", lambda m: unicode_escape(m.group(0))[0], s
    )


class YTDL37API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            s = base64.urlsafe_b64decode(process.args[2]).decode("utf-8")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_uppercase_escape(s))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL37TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 6)))

    def _escape(self) -> str:
        # a code point below the surrogate range, as an 8-hex \\U escape
        cp = random.randint(0x100, 0xD000)
        return "\\U%08x" % cp

    def failing_str(self) -> str:
        return f"{self._word()}{self._escape()}{self._word()}"

    def passing_str(self) -> str:
        return "".join(self._word() for _ in range(random.randint(2, 4)))


class YTDL37SystemtestGenerator(SystemtestGenerator, YTDL37TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.failing_str()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.passing_str()), TestResult.PASSING


class YTDL37UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL37TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="uppercase_escape")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(s: str) -> List[ast.stmt]:
        expected = _fixed_uppercase_escape(s)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="uppercase_escape"),
                            args=[ast.Constant(value=s)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.failing_str())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.passing_str())
        return test, TestResult.PASSING


# ======================================================================
# bug_42: the XML-ampersand fixer was named ``fix_xml_all_ampersand`` and
# naively replaced every ``&`` with ``&amp;`` (double-escaping already
# escaped entities).  The fix renames it ``fix_xml_ampersands`` and uses a
# negative-lookahead regex so existing entities are left intact.
#
# System-test format:  a urlsafe-base64 encoding of the XML string.  A
#   string containing an already-escaped entity (``&amp;`` etc.) triggers
#   the fault.  The harness (which falls back to the old name on the buggy
#   build) prints ``repr(fix(s))``; the oracle compares to the fixed impl.
# ======================================================================

_FIX_XML_FALLBACK_IMPORT = (
    "try:\n"
    "    from youtube_dl.utils import fix_xml_ampersands\n"
    "except ImportError:\n"
    "    from youtube_dl.utils import fix_xml_all_ampersand as fix_xml_ampersands\n"
)


def _fixed_fix_xml_ampersands(xml_str: str) -> str:
    return re.sub(
        r"&(?!amp;|lt;|gt;|apos;|quot;|#x[0-9a-fA-F]{,4};|#[0-9]{,4};)",
        "&amp;",
        xml_str,
    )


class YTDL42API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            s = base64.urlsafe_b64decode(process.args[2]).decode("utf-8")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_fix_xml_ampersands(s))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL42TestGenerator:
    _ENTITIES = ["amp;", "lt;", "gt;", "quot;", "apos;", "#65;", "#x41;"]

    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 6)))

    def failing_str(self) -> str:
        return f"{self._word()} &{random.choice(self._ENTITIES)} {self._word()}"

    def passing_str(self) -> str:
        if random.random() < 0.5:
            return f"{self._word()} & {self._word()}"
        return f"{self._word()} {self._word()}"


class YTDL42SystemtestGenerator(SystemtestGenerator, YTDL42TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.failing_str()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self.passing_str()), TestResult.PASSING


class YTDL42UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL42TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_FIX_XML_FALLBACK_IMPORT).body

    @staticmethod
    def _assert(s: str) -> List[ast.stmt]:
        expected = _fixed_fix_xml_ampersands(s)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="fix_xml_ampersands"),
                            args=[ast.Constant(value=s)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.failing_str())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.passing_str())
        return test, TestResult.PASSING


# ======================================================================
# bug_40: ``struct_unpack`` / ``struct_pack`` (compat wrappers around
# ``struct``) did not exist in utils.py, so code importing them failed with
# ``ImportError``.  The fix adds them.
#
# System-test format:  ``<mode> <fmt> <value>`` where ``<mode>`` is ``ytdl``
#   (imports ``struct_unpack`` from youtube_dl.utils — the trigger) or
#   ``std`` (uses stdlib ``struct``).  Both round-trip ``value``; the oracle
#   expects ``value`` back.  The missing import makes ``ytdl`` fail on the
#   buggy build.
# ======================================================================

_STRUCT_MAX = {"!B": 0xFF, "!H": 0xFFFF, "!I": 0xFFFFFFFF, "!Q": 0xFFFFFFFFFFFFFFFF}


class YTDL40API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            value = int(process.args[4])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(value)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL40TestGenerator:
    def _case(self) -> Tuple[str, int]:
        fmt = random.choice(list(_STRUCT_MAX))
        return fmt, random.randint(0, _STRUCT_MAX[fmt])


class YTDL40SystemtestGenerator(SystemtestGenerator, YTDL40TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fmt, value = self._case()
        return f"ytdl {fmt} {value}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        fmt, value = self._case()
        return f"std {fmt} {value}", TestResult.PASSING


class YTDL40UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL40TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(fmt: str, value: int, failing: bool) -> List[ast.stmt]:
        if failing:
            src = (
                "import struct\n"
                "from youtube_dl.utils import struct_unpack\n"
                f"self.assertEqual({value}, struct_unpack({fmt!r}, struct.pack({fmt!r}, {value}))[0])\n"
            )
        else:
            src = (
                "import struct\n"
                f"self.assertEqual({value}, struct.unpack({fmt!r}, struct.pack({fmt!r}, {value}))[0])\n"
            )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, value = self._case()
        test = self.get_empty_test()
        test.body = self._body(fmt, value, True)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, value = self._case()
        test = self.get_empty_test()
        test.body = self._body(fmt, value, False)
        return test, TestResult.PASSING


grammar_struct: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <fmt> <integer>"],
            "<mode>": ["ytdl", "std"],
            "<fmt>": ["!B", "!H", "!I", "!Q"],
        },
        **INTEGER,
    )
)

assert is_valid_grammar(grammar_struct)


# ======================================================================
# bug_39: ``limit_length`` (truncate an over-long string with an ellipsis)
# did not exist in utils.py, so code importing it failed with
# ``ImportError``.  The fix adds it.
#
# System-test format:  ``<mode> <length> <word>`` where ``<mode>`` is
#   ``ytdl`` (imports ``limit_length`` — the trigger) or ``local`` (uses an
#   inline equivalent).  The oracle expects the correctly-truncated string.
# ======================================================================


def _fixed_limit_length(s, length):
    if s is None:
        return None
    ellipses = "..."
    if len(s) > length:
        return s[: length - len(ellipses)] + ellipses
    return s


class YTDL39API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            length = int(process.args[3])
            word = process.args[4]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_limit_length(word, length))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL39TestGenerator:
    @staticmethod
    def _case() -> Tuple[int, str]:
        length = random.randint(6, 20)
        word = "".join(
            random.choices(string.ascii_lowercase, k=length + random.randint(4, 20))
        )
        return length, word


class YTDL39SystemtestGenerator(SystemtestGenerator, YTDL39TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        length, word = self._case()
        return f"ytdl {length} {word}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        length, word = self._case()
        return f"local {length} {word}", TestResult.PASSING


class YTDL39UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL39TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(length: int, word: str, failing: bool) -> List[ast.stmt]:
        expected = _fixed_limit_length(word, length)
        if failing:
            src = (
                "from youtube_dl.utils import limit_length\n"
                f"self.assertEqual({expected!r}, limit_length({word!r}, {length}))\n"
            )
        else:
            src = (
                "def _limit(s, length):\n"
                "    ellipses = '...'\n"
                "    if s is None:\n"
                "        return None\n"
                "    if len(s) > length:\n"
                "        return s[:length - len(ellipses)] + ellipses\n"
                "    return s\n"
                f"self.assertEqual({expected!r}, _limit({word!r}, {length}))\n"
            )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        length, word = self._case()
        test = self.get_empty_test()
        test.body = self._body(length, word, True)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        length, word = self._case()
        test = self.get_empty_test()
        test.body = self._body(length, word, False)
        return test, TestResult.PASSING


grammar_limit: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <word>"],
            "<mode>": ["ytdl", "local"],
            "<word>": ["<lower><lowers>"],
            "<lowers>": ["", "<lower><lowers>"],
            "<lower>": srange(string.ascii_lowercase),
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_limit)


# ======================================================================
# bug_38: ``urlencode_postdata`` (urlencode a dict and ASCII-encode to
# bytes) did not exist in utils.py, so code importing it failed with
# ``ImportError``.  The fix adds it.
#
# System-test format:  ``<mode> <key> <value>`` where ``<mode>`` is ``ytdl``
#   (imports ``urlencode_postdata`` — the trigger) or ``std`` (uses stdlib
#   ``urlencode``).  The oracle expects ``b"key=value"``.
# ======================================================================


def _fixed_urlencode_postdata(key: str, value: str) -> bytes:
    from urllib.parse import urlencode

    return urlencode({key: value}).encode("ascii")


class YTDL38API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            key = process.args[3]
            value = process.args[4]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_urlencode_postdata(key, value))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL38TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 9)))

    def _case(self) -> Tuple[str, str]:
        return self._word(), self._word()


class YTDL38SystemtestGenerator(SystemtestGenerator, YTDL38TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        key, value = self._case()
        return f"ytdl {key} {value}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        key, value = self._case()
        return f"std {key} {value}", TestResult.PASSING


class YTDL38UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL38TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(key: str, value: str, failing: bool) -> List[ast.stmt]:
        expected = _fixed_urlencode_postdata(key, value)
        if failing:
            src = (
                "from youtube_dl.utils import urlencode_postdata\n"
                f"self.assertEqual({expected!r}, urlencode_postdata({{{key!r}: {value!r}}}))\n"
            )
        else:
            src = (
                "from urllib.parse import urlencode\n"
                f"self.assertEqual({expected!r}, urlencode({{{key!r}: {value!r}}}).encode('ascii'))\n"
            )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key, value = self._case()
        test = self.get_empty_test()
        test.body = self._body(key, value, True)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key, value = self._case()
        test = self.get_empty_test()
        test.body = self._body(key, value, False)
        return test, TestResult.PASSING


grammar_postdata: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word> <word>"],
            "<mode>": ["ytdl", "std"],
            "<word>": ["<lower><lowers>"],
            "<lowers>": ["", "<lower><lowers>"],
            "<lower>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_postdata)


# ======================================================================
# bug_6 & bug_27: ``parse_dfxp_time_expr`` returned ``0.0`` for an empty /
# ``None`` argument instead of ``None`` (a bare ``return``).  The fix makes
# empty input yield ``None`` so callers can distinguish "no time" from 0s.
#
# System-test format:  ``none <salt>`` / ``empty <salt>`` (the trigger — the
#   salt only diversifies the input) or ``value <expr>`` (a valid time
#   expression).  The harness prints ``repr(parse_dfxp_time_expr(te))``; the
#   oracle compares to the fixed impl (``None`` for empty).
# ======================================================================


def _fixed_parse_dfxp_time_expr(time_expr):
    if not time_expr:
        return None
    mobj = re.match(r"^(?P<time_offset>\d+(?:\.\d+)?)s?$", time_expr)
    if mobj:
        return float(mobj.group("time_offset"))
    mobj = re.match(r"^(\d+):(\d\d):(\d\d(?:\.\d+)?)$", time_expr)
    if mobj:
        return (
            3600 * int(mobj.group(1))
            + 60 * int(mobj.group(2))
            + float(mobj.group(3))
        )
    return None


class _DfxpTimeAPI(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            if mode == "none":
                te = None
            elif mode == "empty":
                te = ""
            else:
                te = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_parse_dfxp_time_expr(te))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class _DfxpTimeTestGenerator:
    @staticmethod
    def _salt() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    @staticmethod
    def valid_expr() -> str:
        kind = random.choice(("secs", "secs_s", "int", "hms", "hms_ms"))
        if kind == "secs":
            return f"{random.randint(0, 600)}.{random.randint(0, 9)}"
        if kind == "secs_s":
            return f"{random.randint(0, 600)}.{random.randint(0, 9)}s"
        if kind == "int":
            return f"{random.randint(0, 600)}{random.choice(('', 's'))}"
        if kind == "hms":
            return f"{random.randint(0, 9):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
        return f"{random.randint(0, 9):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}.{random.randint(0, 999):03d}"


class _DfxpTimeSystemtestGenerator(SystemtestGenerator, _DfxpTimeTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(("none", "empty"))
        return f"{mode} {self._salt()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"value {self.valid_expr()}", TestResult.PASSING


class _DfxpTimeUnittestGenerator(
    python.PythonGenerator, UnittestGenerator, _DfxpTimeTestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="parse_dfxp_time_expr")],
                level=0,
            )
        ]

    @staticmethod
    def _call(arg: ast.expr) -> ast.Call:
        return ast.Call(
            func=ast.Name(id="parse_dfxp_time_expr"), args=[arg], keywords=[]
        )

    def _eq(self, expected, arg: ast.expr) -> ast.stmt:
        return ast.Expr(
            value=ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[ast.Constant(value=expected), self._call(arg)],
                keywords=[],
            )
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        empty_arg = ast.Constant(value=None) if random.random() < 0.5 else ast.Constant(value="")
        expr = self.valid_expr()
        val = _fixed_parse_dfxp_time_expr(expr)
        test = self.get_empty_test()
        test.body = [
            self._eq(None, empty_arg),
            self._eq(val, ast.Constant(value=expr)),
        ]
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        expr = self.valid_expr()
        val = _fixed_parse_dfxp_time_expr(expr)
        test = self.get_empty_test()
        test.body = [self._eq(val, ast.Constant(value=expr))]
        return test, TestResult.PASSING


grammar_dfxp_time: Grammar = clean_up(
    dict(
        {
            "<start>": ["none <salt>", "empty <salt>", "value <expr>"],
            "<salt>": ["<lower><lowers>"],
            "<lowers>": ["", "<lower><lowers>"],
            "<lower>": srange(string.ascii_lowercase),
            "<expr>": ["<echar><echars>"],
            "<echars>": ["", "<echar><echars>"],
            "<echar>": srange(string.digits + ":.s"),
        }
    )
)

assert is_valid_grammar(grammar_dfxp_time)


class YTDL6API(_DfxpTimeAPI):
    pass


class YTDL6SystemtestGenerator(_DfxpTimeSystemtestGenerator):
    pass


class YTDL6UnittestGenerator(_DfxpTimeUnittestGenerator):
    pass


# ======================================================================
# bug_27: the colon time form of ``parse_dfxp_time_expr`` accepted only a
# ``.`` before the fractional seconds (``\d\d(?:\.\d+)?``), so a value using
# a ``:`` separator (e.g. ``00:00:01:100``) failed to match and returned
# ``None``.  The fix accepts ``:`` too and normalises it to ``.``.
#
# System-test format:  ``value <expr>``; an ``H:MM:SS:fff`` expression
#   triggers the fault while dot / plain forms do not.
# ======================================================================


def _fixed_parse_dfxp_time_expr_v27(time_expr):
    if not time_expr:
        return None
    mobj = re.match(r"^(?P<time_offset>\d+(?:\.\d+)?)s?$", time_expr)
    if mobj:
        return float(mobj.group("time_offset"))
    mobj = re.match(r"^(\d+):(\d\d):(\d\d(?:(?:\.|:)\d+)?)$", time_expr)
    if mobj:
        return (
            3600 * int(mobj.group(1))
            + 60 * int(mobj.group(2))
            + float(mobj.group(3).replace(":", "."))
        )
    return None


class YTDL27API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            te = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_parse_dfxp_time_expr_v27(te))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL27TestGenerator(_DfxpTimeTestGenerator):
    @staticmethod
    def colon_frac_expr() -> str:
        return (
            f"{random.randint(0, 9):02d}:{random.randint(0, 59):02d}:"
            f"{random.randint(0, 59):02d}:{random.randint(1, 999):03d}"
        )


class YTDL27SystemtestGenerator(SystemtestGenerator, YTDL27TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"value {self.colon_frac_expr()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"value {self.valid_expr()}", TestResult.PASSING


class YTDL27UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL27TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="parse_dfxp_time_expr")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(expr: str) -> List[ast.stmt]:
        val = _fixed_parse_dfxp_time_expr_v27(expr)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=val),
                        ast.Call(
                            func=ast.Name(id="parse_dfxp_time_expr"),
                            args=[ast.Constant(value=expr)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.colon_frac_expr())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.valid_expr())
        return test, TestResult.PASSING


# ======================================================================
# bug_20: the ``get_elements_by_attribute`` regex required every attribute
# to have a value, so a tag carrying a valueless (boolean) attribute such
# as ``itemscope`` failed to match and the lookup returned ``None``.  The
# fix adds an empty alternative to the attribute group.
#
# System-test format:  a urlsafe-base64 JSON ``{attr, value, html,
#   expected}``.  HTML containing a boolean attribute on the target tag
#   triggers the fault.  The harness prints
#   ``repr(get_element_by_attribute(attr, value, html))``; the oracle
#   compares to ``expected`` (the fixed content).
# ======================================================================

_BOOL_ATTRS = ["itemscope", "disabled", "checked", "hidden", "selected", "required"]
_TAGS = ["div", "span", "p", "a", "section"]
_ATTRS = ["itemprop", "id", "name", "role", "rel"]


def _b64json(d: dict) -> str:
    return base64.urlsafe_b64encode(json.dumps(d).encode("utf-8")).decode("ascii")


class YTDL20API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            d = json.loads(base64.urlsafe_b64decode(process.args[2]).decode("utf-8"))
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(d["expected"])
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL20TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def _case(self, boolean: bool) -> dict:
        tag = random.choice(_TAGS)
        attr = random.choice(_ATTRS)
        value = self._word()
        content = self._word()
        target = f'{attr}="{value}"'
        if boolean:
            bool_attr = random.choice(_BOOL_ATTRS)
            if random.random() < 0.5:
                attrs = f"{target} {bool_attr}"
            else:
                attrs = f"{bool_attr} {target}"
        else:
            attrs = target
        html = f"<{tag} {attrs}>{content}</{tag}>"
        return {"attr": attr, "value": value, "html": html, "expected": content}


class YTDL20SystemtestGenerator(SystemtestGenerator, YTDL20TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64json(self._case(True)), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64json(self._case(False)), TestResult.PASSING


class YTDL20UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL20TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="get_element_by_attribute")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(d: dict) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=d["expected"]),
                        ast.Call(
                            func=ast.Name(id="get_element_by_attribute"),
                            args=[
                                ast.Constant(value=d["attr"]),
                                ast.Constant(value=d["value"]),
                                ast.Constant(value=d["html"]),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._case(True))
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._case(False))
        return test, TestResult.PASSING


# ======================================================================
# bug_34: ``js_to_json`` matched a nested ``{``/``[`` value by CONSUMING it
# (``...|\[|\{``), so the nested object's single-quoted keys/values were
# skipped and never converted, producing invalid JSON.  The fix uses a
# lookahead ``(?=\[|\{)`` so nested structures are recursed into.
#
# System-test format:  a urlsafe-base64 JSON ``{code, expected}`` where
#   ``code`` is JS-object notation.  A nested object triggers the fault.
#   The harness prints ``js_to_json(code)``; the oracle parses it as JSON
#   and compares to ``expected`` (invalid JSON on the buggy build fails).
# ======================================================================


class YTDL34API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            d = json.loads(base64.urlsafe_b64decode(process.args[2]).decode("utf-8"))
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode != 0:
            return TestResult.FAILING, f"process failed: {out!r}"
        try:
            got = json.loads(out)
        except ValueError:
            return TestResult.FAILING, f"not valid JSON: {out!r}"
        if got == d["expected"]:
            return TestResult.PASSING, f"Parsed {got!r}"
        return TestResult.FAILING, f"Expected {d['expected']!r}, but was {got!r}"


class YTDL34TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def _distinct_keys(self, n: int) -> List[str]:
        keys = set()
        while len(keys) < n:
            keys.add(self._word())
        return list(keys)

    def _value(self):
        if random.random() < 0.5:
            return self._word()
        return random.randint(0, 9999)

    @staticmethod
    def _js_value(v) -> str:
        return f"'{v}'" if isinstance(v, str) else str(v)

    def flat_case(self) -> Tuple[str, dict]:
        keys = self._distinct_keys(random.randint(1, 3))
        obj = {}
        parts = []
        for k in keys:
            v = self._value()
            obj[k] = v
            parts.append(f"'{k}':{self._js_value(v)}")
        return "{" + ",".join(parts) + "}", obj

    def nested_case(self) -> Tuple[str, dict]:
        k1, k2 = self._distinct_keys(2)
        v = self._word()
        return "{'%s':{'%s':'%s'}}" % (k1, k2, v), {k1: {k2: v}}


class YTDL34SystemtestGenerator(SystemtestGenerator, YTDL34TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.nested_case()
        return _b64json({"code": code, "expected": obj}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.flat_case()
        return _b64json({"code": code, "expected": obj}), TestResult.PASSING


class YTDL34UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL34TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(code: str, obj: dict) -> List[ast.stmt]:
        src = (
            "import json\n"
            "from youtube_dl.utils import js_to_json\n"
            f"self.assertEqual({obj!r}, json.loads(js_to_json({code!r})))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.nested_case()
        test = self.get_empty_test()
        test.body = self._body(code, obj)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.flat_case()
        test = self.get_empty_test()
        test.body = self._body(code, obj)
        return test, TestResult.PASSING


# ======================================================================
# bug_7: ``js_to_json`` returned a double-quoted string value unchanged, so
# a JS ``"..."`` string containing an escaped single quote (``\'``) stayed
# in the output as ``\'`` which is not a valid JSON escape.  The fix
# unescapes ``\'`` inside double-quoted strings.
#
# Reuses the js_to_json JSON-equality oracle (YTDL34API): the harness prints
# ``js_to_json(code)`` and the oracle parses it and compares to ``expected``.
# ======================================================================


class YTDL7API(YTDL34API):
    pass


class YTDL7TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def failing_case(self) -> Tuple[str, dict]:
        key = self._word()
        w1, w2 = self._word(), self._word()
        value = w1 + "'" + w2
        # JS code: {"key":"w1\'w2"}  (double-quoted value with an escaped ')
        code = '{"' + key + '":"' + w1 + "\\'" + w2 + '"}'
        return code, {key: value}

    def passing_case(self) -> Tuple[str, dict]:
        key, val = self._word(), self._word()
        code = '{"' + key + '":"' + val + '"}'
        return code, {key: val}


class YTDL7SystemtestGenerator(SystemtestGenerator, YTDL7TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.failing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.passing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.PASSING


class YTDL7UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL7TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.failing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.passing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.PASSING


# ======================================================================
# bug_23: ``js_to_json`` did not strip ``//`` line comments (only ``/* */``),
# so a ``//`` comment survived into the output and produced invalid JSON.
# The fix adds ``//[^\n]*`` handling.
#
# Reuses the js_to_json JSON-equality oracle (YTDL34API).
# ======================================================================


class YTDL23API(YTDL34API):
    pass


class YTDL23TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _pair(self):
        k = self._word()
        v = self._word() if random.random() < 0.5 else random.randint(0, 999)
        return k, v

    def failing_case(self) -> Tuple[str, dict]:
        (k1, v1), (k2, v2) = self._pair(), self._pair()
        while k2 == k1:
            k2, v2 = self._pair()
        comment = self._word()
        code = (
            "{"
            + f'"{k1}":{v1!r} , //{comment}\n'.replace("'", '"')
            + f'"{k2}":{v2!r}'.replace("'", '"')
            + "}"
        )
        return code, {k1: v1, k2: v2}

    def passing_case(self) -> Tuple[str, dict]:
        (k1, v1), (k2, v2) = self._pair(), self._pair()
        while k2 == k1:
            k2, v2 = self._pair()
        code = (
            "{"
            + f'"{k1}":{v1!r},"{k2}":{v2!r}'.replace("'", '"')
            + "}"
        )
        return code, {k1: v1, k2: v2}


class YTDL23SystemtestGenerator(SystemtestGenerator, YTDL23TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.failing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.passing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.PASSING


class YTDL23UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL23TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.failing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.passing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.PASSING


# ======================================================================
# bug_33: ``parse_iso8601`` did not account for fractional seconds before
# the timezone, so a date such as ``2014-03-23T22:04:26.1234Z`` left the
# ``.1234`` in the string and ``strptime`` raised ``ValueError``.  The fix
# consumes an optional ``(\.[0-9]+)?`` in the timezone regex.
#
# System-test format:  an ISO-8601 datetime string.  A value with a
#   fractional-seconds component triggers the fault.  The harness prints
#   ``repr(parse_iso8601(s))``; the oracle compares to the fixed impl.
# ======================================================================


def _fixed_parse_iso8601(date_str, delimiter="T"):
    if date_str is None:
        return None
    m = re.search(
        r"(\.[0-9]+)?(?:Z$| ?(?P<sign>\+|-)(?P<hours>[0-9]{2}):?(?P<minutes>[0-9]{2})$)",
        date_str,
    )
    if not m:
        timezone = datetime.timedelta()
    else:
        date_str = date_str[: -len(m.group(0))]
        if not m.group("sign"):
            timezone = datetime.timedelta()
        else:
            sign = 1 if m.group("sign") == "+" else -1
            timezone = datetime.timedelta(
                hours=sign * int(m.group("hours")),
                minutes=sign * int(m.group("minutes")),
            )
    date_format = "%Y-%m-%d{0}%H:%M:%S".format(delimiter)
    dt = datetime.datetime.strptime(date_str, date_format) - timezone
    return calendar.timegm(dt.timetuple())


class YTDL33API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            date_str = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(_fixed_parse_iso8601(date_str))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL33TestGenerator:
    @staticmethod
    def _base() -> str:
        y = random.randint(2000, 2020)
        mo = random.randint(1, 12)
        d = random.randint(1, 28)
        h = random.randint(0, 23)
        mi = random.randint(0, 59)
        s = random.randint(0, 59)
        return f"{y:04d}-{mo:02d}-{d:02d}T{h:02d}:{mi:02d}:{s:02d}"

    @staticmethod
    def _tz() -> str:
        choice = random.randint(0, 2)
        if choice == 0:
            return "Z"
        sign = "+" if choice == 1 else "-"
        return f"{sign}{random.randint(0, 12):02d}{random.choice((0, 30)):02d}"

    def failing_str(self) -> str:
        frac = "".join(random.choices(string.digits, k=random.randint(1, 6)))
        return f"{self._base()}.{frac}{self._tz()}"

    def passing_str(self) -> str:
        return f"{self._base()}{self._tz()}"


class YTDL33SystemtestGenerator(SystemtestGenerator, YTDL33TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.failing_str(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.passing_str(), TestResult.PASSING


class YTDL33UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL33TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="parse_iso8601")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(s: str) -> List[ast.stmt]:
        expected = _fixed_parse_iso8601(s)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="parse_iso8601"),
                            args=[ast.Constant(value=s)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.failing_str())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self.passing_str())
        return test, TestResult.PASSING


grammar_iso8601: Grammar = clean_up(
    dict(
        {
            "<start>": ["<char><chars>"],
            "<chars>": ["", "<char><chars>"],
            "<char>": srange(string.digits + "-:TZ.+"),
        }
    )
)

assert is_valid_grammar(grammar_iso8601)


# ======================================================================
# bug_41: ``unified_strdate`` stripped a trailing timezone with the greedy
# regex ``' ?(\+|-)[0-9:]*$'``, which also ate the ``-DD`` of an ISO date
# like ``1968-12-10`` and made parsing fail (returning ``None``).  The fix
# requires a full ``[0-9]{2}:?[0-9]{2}`` offset.
#
# System-test format:  a urlsafe-base64 JSON ``{date, expected}``.  An ISO
#   ``YYYY-MM-DD`` date triggers the fault.  The harness prints
#   ``repr(unified_strdate(date))``; the oracle compares to ``expected``.
# ======================================================================


class YTDL41API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            d = json.loads(base64.urlsafe_b64decode(process.args[2]).decode("utf-8"))
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(d["expected"])
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL41TestGenerator:
    @staticmethod
    def _ymd() -> Tuple[int, int, int]:
        return random.randint(1970, 2020), random.randint(1, 12), random.randint(1, 28)

    def failing_case(self) -> Tuple[str, str]:
        y, m, d = self._ymd()
        return f"{y:04d}-{m:02d}-{d:02d}", f"{y:04d}{m:02d}{d:02d}"

    def passing_case(self) -> Tuple[str, str]:
        y, m, d = self._ymd()
        expected = f"{y:04d}{m:02d}{d:02d}"
        if random.random() < 0.5:
            return f"{calendar.month_name[m]} {d}, {y}", expected
        return f"{d} {calendar.month_name[m]} {y}", expected


class YTDL41SystemtestGenerator(SystemtestGenerator, YTDL41TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        date, expected = self.failing_case()
        return _b64json({"date": date, "expected": expected}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        date, expected = self.passing_case()
        return _b64json({"date": date, "expected": expected}), TestResult.PASSING


class YTDL41UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL41TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="unified_strdate")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(date: str, expected: str) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="unified_strdate"),
                            args=[ast.Constant(value=date)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        date, expected = self.failing_case()
        test = self.get_empty_test()
        test.body = self._assert(date, expected)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        date, expected = self.passing_case()
        test = self.get_empty_test()
        test.body = self._assert(date, expected)
        return test, TestResult.PASSING


# ======================================================================
# bug_35: ``unified_strdate`` lacked the ``'%d/%m/%Y %H:%M:%S'`` format, so
# a ``DD/MM/YYYY HH:MM:SS`` date failed to parse and returned ``None``.  The
# fix adds that format expression.
#
# Reuses the base64-JSON date oracle (YTDL41API).
# ======================================================================


class YTDL35API(YTDL41API):
    pass


class YTDL35TestGenerator:
    @staticmethod
    def _ymd() -> Tuple[int, int, int]:
        return random.randint(1970, 2020), random.randint(1, 12), random.randint(1, 28)

    @staticmethod
    def _hms() -> str:
        return f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"

    def failing_case(self) -> Tuple[str, str]:
        y, m, d = self._ymd()
        return f"{d:02d}/{m:02d}/{y:04d} {self._hms()}", f"{y:04d}{m:02d}{d:02d}"

    def passing_case(self) -> Tuple[str, str]:
        y, m, d = self._ymd()
        expected = f"{y:04d}{m:02d}{d:02d}"
        if random.random() < 0.5:
            return f"{y:04d}/{m:02d}/{d:02d} {self._hms()}", expected
        return f"{calendar.month_name[m]} {d}, {y}", expected


class YTDL35SystemtestGenerator(SystemtestGenerator, YTDL35TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        date, expected = self.failing_case()
        return _b64json({"date": date, "expected": expected}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        date, expected = self.passing_case()
        return _b64json({"date": date, "expected": expected}), TestResult.PASSING


class YTDL35UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL35TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="unified_strdate")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        date, expected = self.failing_case()
        test = self.get_empty_test()
        test.body = YTDL41UnittestGenerator._assert(date, expected)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        date, expected = self.passing_case()
        test = self.get_empty_test()
        test.body = YTDL41UnittestGenerator._assert(date, expected)
        return test, TestResult.PASSING


# ======================================================================
# bug_29: ``unified_strdate`` ended with ``return compat_str(upload_date)``
# so an unparseable date produced the literal string ``"None"`` instead of
# ``None``.  The fix returns ``None`` when no format matched.
#
# Reuses the base64-JSON date oracle (YTDL41API).  Failing inputs are
# consonant-only garbage (unparseable, expected ``None``); passing inputs
# are valid month-name dates.
# ======================================================================

_CONSONANTS = "bcdfghjklmnpqrstvwxyz"


class YTDL29API(YTDL41API):
    pass


class YTDL29TestGenerator:
    def garbage(self) -> str:
        return " ".join(
            "".join(random.choices(_CONSONANTS, k=random.randint(4, 9)))
            for _ in range(random.randint(1, 2))
        )

    @staticmethod
    def valid(self=None) -> Tuple[str, str]:
        y, m, d = random.randint(1970, 2020), random.randint(1, 12), random.randint(1, 28)
        return f"{calendar.month_name[m]} {d}, {y}", f"{y:04d}{m:02d}{d:02d}"


class YTDL29SystemtestGenerator(SystemtestGenerator, YTDL29TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64json({"date": self.garbage(), "expected": None}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        date, expected = self.valid()
        return _b64json({"date": date, "expected": expected}), TestResult.PASSING


class YTDL29UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL29TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="unified_strdate")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = YTDL41UnittestGenerator._assert(self.garbage(), None)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        date, expected = self.valid()
        test = self.get_empty_test()
        test.body = YTDL41UnittestGenerator._assert(date, expected)
        return test, TestResult.PASSING


# ======================================================================
# bug_5: ``unified_timestamp`` fell back to ``email.utils.parsedate_tz`` and
# then called ``timetuple.timetuple()`` on the returned tuple, raising
# ``AttributeError``.  The fix uses ``calendar.timegm(timetuple)`` directly.
#
# System-test format:  a urlsafe-base64 JSON ``{date, expected}``.  An
#   RFC-2822 style date reaches the fallback and triggers the fault; a
#   ``YYYY/MM/DD HH:MM:SS +0000`` date is handled by ``strptime`` and does
#   not.  The harness prints ``repr(unified_timestamp(date))``; the oracle
#   compares to ``expected``.
# ======================================================================


class YTDL5API(YTDL41API):
    pass


class YTDL5TestGenerator:
    @staticmethod
    def _dt() -> Tuple[int, int, int, int, int, int]:
        return (
            random.randint(1971, 2030),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59),
        )

    def failing_case(self) -> Tuple[str, int]:
        y, mo, d, h, mi, s = self._dt()
        wday = random.choice(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        date = f"{wday}, {d:02d} {calendar.month_abbr[mo]} {y} {h:02d}:{mi:02d}:{s:02d} +0000"
        expected = calendar.timegm(email.utils.parsedate_tz(date))
        return date, expected

    def passing_case(self) -> Tuple[str, int]:
        y, mo, d, h, mi, s = self._dt()
        date = f"{y:04d}/{mo:02d}/{d:02d} {h:02d}:{mi:02d}:{s:02d} +0000"
        expected = calendar.timegm((y, mo, d, h, mi, s, 0, 0, 0))
        return date, expected


class YTDL5SystemtestGenerator(SystemtestGenerator, YTDL5TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        date, expected = self.failing_case()
        return _b64json({"date": date, "expected": expected}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        date, expected = self.passing_case()
        return _b64json({"date": date, "expected": expected}), TestResult.PASSING


class YTDL5UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL5TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="youtube_dl.utils",
                names=[ast.alias(name="unified_timestamp")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(date: str, expected: int) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="unified_timestamp"),
                            args=[ast.Constant(value=date)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        date, expected = self.failing_case()
        test = self.get_empty_test()
        test.body = self._assert(date, expected)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        date, expected = self.passing_case()
        test = self.get_empty_test()
        test.body = self._assert(date, expected)
        return test, TestResult.PASSING


# ======================================================================
# bug_10: ``js_to_json``'s string regex only allowed ``\\`` and ``\"`` as
# escapes, so a string value containing another escape (e.g. ``\n``) broke
# tokenisation and produced invalid JSON.  The fix accepts ``\\['"nu]``.
#
# Reuses the js_to_json JSON-equality oracle (YTDL34API).  Failing inputs
# embed a ``\n`` escape; passing inputs are plain strings.
# ======================================================================


class YTDL10API(YTDL34API):
    pass


class YTDL10TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def failing_case(self) -> Tuple[str, dict]:
        key, pre, post = self._word(), self._word(), self._word()
        # JS code: {"key":"pre\npost"}  (a newline escape inside the string)
        code = '{"' + key + '":"' + pre + "\\n" + post + '"}'
        return code, {key: pre + "\n" + post}

    def passing_case(self) -> Tuple[str, dict]:
        key, val = self._word(), self._word()
        code = '{"' + key + '":"' + val + '"}'
        return code, {key: val}


class YTDL10SystemtestGenerator(SystemtestGenerator, YTDL10TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.failing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.passing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.PASSING


class YTDL10UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL10TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.failing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.passing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.PASSING


# ======================================================================
# bug_26: ``js_to_json``'s octal/hex number alternative lacked a leading
# ``\b``, so the ``0+[0-7]+`` pattern matched a run of zeros INSIDE an
# ordinary decimal value (e.g. ``100000`` -> ``10``).  The fix anchors it
# with ``\b``.
#
# Reuses the js_to_json JSON-equality oracle (YTDL34API).  Failing inputs
# are decimals with 2+ trailing zeros; passing inputs are zero-free
# decimals.
# ======================================================================


class YTDL26API(YTDL34API):
    pass


class YTDL26TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def failing_case(self) -> Tuple[str, dict]:
        key = self._word()
        value = int(str(random.randint(1, 9)) + "0" * random.randint(2, 4))
        return f'{{"{key}":{value}}}', {key: value}

    def passing_case(self) -> Tuple[str, dict]:
        key = self._word()
        value = int("".join(random.choices("123456789", k=random.randint(2, 4))))
        return f'{{"{key}":{value}}}', {key: value}


class YTDL26SystemtestGenerator(SystemtestGenerator, YTDL26TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.failing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.passing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.PASSING


class YTDL26UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL26TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.failing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.passing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.PASSING


# ======================================================================
# bug_15: ``js_to_json``'s bareword/identifier alternative matched the
# ``e``/``E`` of a number in scientific notation as the start of an
# identifier, so a value like ``1e10`` was split and produced invalid JSON.
# The fix excludes a leading ``[eE]`` that follows a digit.
#
# Reuses the js_to_json JSON-equality oracle (YTDL34API).  Failing inputs
# are numbers in scientific notation; passing inputs are plain integers.
# ======================================================================


class YTDL15API(YTDL34API):
    pass


class YTDL15TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def failing_case(self) -> Tuple[str, dict]:
        key = self._word()
        mant = random.randint(1, 9)
        exp = random.randint(1, 9)
        e = random.choice(("e", "E"))
        value = float(f"{mant}e{exp}")
        return f'{{"{key}":{mant}{e}{exp}}}', {key: value}

    def passing_case(self) -> Tuple[str, dict]:
        key = self._word()
        value = random.randint(1, 9999)
        return f'{{"{key}":{value}}}', {key: value}


class YTDL15SystemtestGenerator(SystemtestGenerator, YTDL15TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.failing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.passing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.PASSING


class YTDL15UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL15TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.failing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.passing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.PASSING


# ======================================================================
# bug_4: ``JSInterpreter`` could not interpret a zero-argument function call
# ``f()`` inside a function body because the call regex required at least
# one argument (``[a-zA-Z0-9_$,]+``), so ``f()`` raised ``ExtractorError:
# Unsupported JS expression``.  The fix accepts an empty argument list
# (``*``) and evaluates it to an empty tuple.
#
# System-test format:  a urlsafe-base64 JSON ``{code, func, expected}``.  A
#   ``code`` whose evaluated function performs a zero-argument call triggers
#   the fault.  The harness prints ``repr(JSInterpreter(code).call_function
#   (func))``; the oracle compares to ``repr(expected)`` (the fixed result).
# ======================================================================


class YTDL4API(YTDL20API):
    pass


class YTDL4TestGenerator:
    @staticmethod
    def _name() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 5)))

    def _two_names(self) -> Tuple[str, str]:
        a = self._name()
        b = self._name()
        while b == a:
            b = self._name()
        return a, b

    def failing_case(self) -> Tuple[str, str, int]:
        inner, outer = self._two_names()
        c = random.randint(1, 999)
        code = "function %s(){return %d;}\nfunction %s(){return %s();}" % (
            inner,
            c,
            outer,
            inner,
        )
        return code, outer, c

    def passing_case(self) -> Tuple[str, str, int]:
        inner, outer = self._two_names()
        k = random.randint(1, 99)
        v = random.randint(1, 99)
        code = "function %s(a){return a+%d;}\nfunction %s(){return %s(%d);}" % (
            inner,
            k,
            outer,
            inner,
            v,
        )
        return code, outer, v + k


class YTDL4SystemtestGenerator(SystemtestGenerator, YTDL4TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, func, exp = self.failing_case()
        return (
            _b64json({"code": code, "func": func, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, func, exp = self.passing_case()
        return (
            _b64json({"code": code, "func": func, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL4UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL4TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(code: str, func: str, exp: int) -> List[ast.stmt]:
        src = (
            "from youtube_dl.jsinterp import JSInterpreter\n"
            f"self.assertEqual({exp!r}, JSInterpreter({code!r}).call_function({func!r}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, func, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(code, func, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, func, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(code, func, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_1: ``match_str``'s unary operators (``''`` = present, ``'!'`` = absent)
# used ``v is not None`` / ``v is None`` and so treated a boolean ``False``
# field as "present" (matching ``field``) and "not absent" (not matching
# ``!field``).  The fix special-cases booleans: ``''`` -> ``v is True`` and
# ``'!'`` -> ``v is False``.
#
# System-test format:  a urlsafe-base64 JSON ``{filter, dct, expected}``.  A
#   filter over a field whose value is boolean ``False`` triggers the fault.
#   The harness prints ``repr(match_str(filter, dct))``; the oracle compares
#   to ``repr(expected)`` (the fixed result).
# ======================================================================


class YTDL1API(YTDL20API):
    pass


class YTDL1TestGenerator:
    @staticmethod
    def _field() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    def failing_case(self) -> Tuple[str, dict, bool]:
        field = self._field()
        if random.random() < 0.5:
            # bare field, value False: buggy True, fixed False
            return field, {field: False}, False
        # negated field, value False: buggy False, fixed True
        return "!" + field, {field: False}, True

    def passing_case(self) -> Tuple[str, dict, bool]:
        field = self._field()
        r = random.random()
        if r < 0.34:
            return field, {field: True}, True
        if r < 0.67:
            return "!" + field, {field: True}, False
        n = random.randint(2, 1000)
        return f"{field}>{n // 2}", {field: n}, True


class YTDL1SystemtestGenerator(SystemtestGenerator, YTDL1TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        filt, dct, exp = self.failing_case()
        return (
            _b64json({"filter": filt, "dct": dct, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        filt, dct, exp = self.passing_case()
        return (
            _b64json({"filter": filt, "dct": dct, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL1UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL1TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(filt: str, dct: dict, exp: bool) -> List[ast.stmt]:
        src = (
            "from youtube_dl.utils import match_str\n"
            f"self.assertEqual({exp!r}, match_str({filt!r}, {dct!r}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        filt, dct, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(filt, dct, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        filt, dct, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(filt, dct, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_24: ``_match_one`` (used by ``match_str``) parsed a numeric comparison
# value as an ``int`` even when the actual field value was a string, so a
# filter like ``x=1280`` never matched a field whose value was the string
# ``'1280'``.  The fix keeps the comparison value as a string when the
# actual field value is a string.
#
# System-test format:  a urlsafe-base64 JSON ``{filter, dct, expected}``.  A
#   ``field=<int>`` filter over a field whose value is the equivalent string
#   triggers the fault.  The harness prints ``repr(match_str(filter, dct))``;
#   the oracle compares to ``repr(expected)`` (the fixed result).
# ======================================================================


class YTDL24API(YTDL20API):
    pass


class YTDL24TestGenerator:
    @staticmethod
    def _field() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def failing_case(self) -> Tuple[str, dict, bool]:
        field = self._field()
        n = random.randint(1, 99999)
        if random.random() < 0.5:
            # field=N vs string value str(N): buggy False, fixed True
            return f"{field}={n}", {field: str(n)}, True
        # field!=N vs string value str(N): buggy True, fixed False
        return f"{field}!={n}", {field: str(n)}, False

    def passing_case(self) -> Tuple[str, dict, bool]:
        field = self._field()
        r = random.random()
        if r < 0.34:
            n = random.randint(1, 99999)
            return f"{field}={n}", {field: n}, True  # int field, both True
        if r < 0.67:
            w = self._word()
            return f"{field}={w}", {field: w}, True  # string==string, both True
        n = random.randint(1, 500)
        m = n + random.randint(1, 500)
        return f"{field}={n}", {field: str(m)}, False  # mismatch, both False


class YTDL24SystemtestGenerator(SystemtestGenerator, YTDL24TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        filt, dct, exp = self.failing_case()
        return (
            _b64json({"filter": filt, "dct": dct, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        filt, dct, exp = self.passing_case()
        return (
            _b64json({"filter": filt, "dct": dct, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL24UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL24TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(filt: str, dct: dict, exp: bool) -> List[ast.stmt]:
        src = (
            "from youtube_dl.utils import match_str\n"
            f"self.assertEqual({exp!r}, match_str({filt!r}, {dct!r}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        filt, dct, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(filt, dct, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        filt, dct, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(filt, dct, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_22: ``_match_one`` (used by ``match_str``) had no grammar for quoted
# string comparison values, so a filter such as ``title='foo bar'`` failed
# to parse and ``match_str`` raised ``ValueError: Invalid filter part``.
# The fix adds a ``quotedstrval`` alternative that accepts quoted strings
# (and unescapes the quote character).
#
# System-test format:  a urlsafe-base64 JSON ``{filter, dct, expected}``.  A
#   filter with a quoted string comparison value triggers the fault (the
#   buggy build raises).  The harness prints ``repr(match_str(filter, dct))``;
#   the oracle compares to ``repr(expected)`` (the fixed result).
# ======================================================================


class YTDL22API(YTDL20API):
    pass


class YTDL22TestGenerator:
    @staticmethod
    def _field() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _val(self) -> str:
        v = self._word()
        if random.random() < 0.4:
            v = v + " " + self._word()
        return v

    def failing_case(self) -> Tuple[str, dict, bool]:
        field = self._field()
        v = self._val()
        r = random.random()
        if r < 0.34:
            return f"{field}='{v}'", {field: v}, True  # eq match
        if r < 0.67:
            return f"{field}!='{v}'", {field: v}, False  # ne non-match
        w = self._val()
        while w == v:
            w = self._val()
        return f"{field}!='{v}'", {field: w}, True  # ne match

    def passing_case(self) -> Tuple[str, dict, bool]:
        field = self._field()
        r = random.random()
        if r < 0.34:
            w = self._word()
            return f"{field}={w}", {field: w}, True
        if r < 0.67:
            n = random.randint(1, 99999)
            return f"{field}={n}", {field: n}, True
        n = random.randint(1, 99999)
        return f"{field}={n}", {field: str(n)}, True


class YTDL22SystemtestGenerator(SystemtestGenerator, YTDL22TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        filt, dct, exp = self.failing_case()
        return (
            _b64json({"filter": filt, "dct": dct, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        filt, dct, exp = self.passing_case()
        return (
            _b64json({"filter": filt, "dct": dct, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL22UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL22TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(filt: str, dct: dict, exp: bool) -> List[ast.stmt]:
        src = (
            "from youtube_dl.utils import match_str\n"
            f"self.assertEqual({exp!r}, match_str({filt!r}, {dct!r}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        filt, dct, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(filt, dct, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        filt, dct, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(filt, dct, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_25: ``js_to_json``'s INTEGER_TABLE regexes for hex/octal literals were
# unanchored and used ``im.group(0)``, so a *quoted string* whose contents
# merely started with octal-looking digits (e.g. ``"00:01:07"``) was
# truncated at the first non-octal char and rewritten as a bare number,
# corrupting the value.  The fix anchors the regex (``\s*:?$``) so only a
# whole octal/hex token is converted.
#
# Reuses the js_to_json JSON-equality oracle (YTDL34API): the harness prints
# ``js_to_json(code)`` and the oracle parses it and compares to ``expected``.
# A quoted value like ``"0<d>:<mm>:<ss>"`` triggers the fault.
# ======================================================================


class YTDL25API(YTDL34API):
    pass


class YTDL25TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def failing_case(self) -> Tuple[str, dict]:
        key = self._word()
        h = random.randint(0, 9)
        m = random.randint(0, 59)
        s = random.randint(0, 59)
        val = "0%d:%02d:%02d" % (h, m, s)  # leading-zero octal prefix then colon
        code = '{"%s": "%s"}' % (key, val)
        return code, {key: val}

    def passing_case(self) -> Tuple[str, dict]:
        key = self._word()
        if random.random() < 0.5:
            val = self._word()
            return '{"%s": "%s"}' % (key, val), {key: val}
        n = random.randint(1, 99999)
        return '{"%s": %d}' % (key, n), {key: n}


class YTDL25SystemtestGenerator(SystemtestGenerator, YTDL25TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.failing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        code, obj = self.passing_case()
        return _b64json({"code": code, "expected": obj}), TestResult.PASSING


class YTDL25UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL25TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.failing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        code, obj = self.passing_case()
        test = self.get_empty_test()
        test.body = YTDL34UnittestGenerator._body(code, obj)
        return test, TestResult.PASSING


# ======================================================================
# bug_16: ``dfxp2srt`` operated on a decoded ``unicode`` string and internally
# did ``compat_etree_fromstring(dfxp_data.encode('utf-8'))`` with str legacy
# namespaces, so it could not accept the ``bytes`` payload the caller now
# feeds it.  The fix makes ``dfxp2srt`` take a bytes-like object (bytes
# namespaces, no inner ``.encode``).
#
# System-test format:  a urlsafe-base64 JSON ``{xml, expected, mode}`` where
#   ``mode`` is ``bytes`` (the fixed signature — triggers the fault on the
#   buggy build, which crashes on ``bytes``) or ``str``.  The harness prints
#   ``repr(dfxp2srt(<bytes|str>))``; the oracle (YTDL20API) compares to
#   ``repr(expected)``.
# ======================================================================


def _dfxp_timecode(total: int) -> str:
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return "%02d:%02d:%02d,000" % (h, m, s)


def _dfxp_build(cues: List[Tuple[int, int, str]]) -> Tuple[str, str]:
    body = "\n".join(
        '<p begin="%d" end="%d">%s</p>' % (b, e, t) for b, e, t in cues
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n'
        "<body><div xml:lang=\"en\">\n"
        f"{body}\n"
        "</div></body></tt>"
    )
    srt = "".join(
        "%d\n%s --> %s\n%s\n\n" % (i, _dfxp_timecode(b), _dfxp_timecode(e), t)
        for i, (b, e, t) in enumerate(cues, 1)
    )
    return xml, srt


class YTDL16API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            d = json.loads(base64.urlsafe_b64decode(process.args[2]).decode("utf-8"))
            _xml, srt = _dfxp_build([tuple(c) for c in d["cues"]])
        except (IndexError, ValueError, KeyError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(srt)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL16TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    def _text(self) -> str:
        return " ".join(self._word() for _ in range(random.randint(1, 2)))

    def _cues(self) -> List[Tuple[int, int, str]]:
        cues = []
        for _ in range(random.randint(1, 3)):
            b = random.randint(0, 3400)
            e = b + random.randint(1, 200)
            cues.append((b, e, self._text()))
        return cues

    def failing_case(self) -> Tuple[list, str]:
        # bytes mode: the fixed signature; crashes on the buggy build
        return self._cues(), "bytes"

    def passing_case(self) -> Tuple[list, str]:
        return self._cues(), "str"


class YTDL16SystemtestGenerator(SystemtestGenerator, YTDL16TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        cues, mode = self.failing_case()
        return _b64json({"cues": cues, "mode": mode}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        cues, mode = self.passing_case()
        return _b64json({"cues": cues, "mode": mode}), TestResult.PASSING


class YTDL16UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL16TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(cues: list, mode: str) -> List[ast.stmt]:
        xml, srt = _dfxp_build([tuple(c) for c in cues])
        arg = f"{xml!r}.encode('utf-8')" if mode == "bytes" else f"{xml!r}"
        src = (
            "from youtube_dl.utils import dfxp2srt\n"
            f"self.assertEqual({srt!r}, dfxp2srt({arg}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        cues, mode = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(cues, mode)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        cues, mode = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(cues, mode)
        return test, TestResult.PASSING


# ======================================================================
# bug_36: ``FacebookIE._VALID_URL`` used ``(?:[^#?]*\#!/)?`` for the optional
# fragment-shebang prefix, so a URL with a ``?query`` segment *before* the
# ``#!/`` (e.g. ``.../name?fref=ts#!/photo.php?v=123``) did not match and
# ``FacebookIE.suitable`` returned ``False``.  The fix uses ``(?:[^#]*?\#!/)?``
# which allows the ``?`` before ``#!/``.
#
# System-test format:  a urlsafe-base64 JSON ``{url, expected}``.  A Facebook
#   URL with a query before ``#!/`` triggers the fault.  The harness prints
#   ``repr(FacebookIE.suitable(url))``; the oracle (YTDL20API) compares to
#   ``repr(expected)`` (the fixed result, ``True``).
# ======================================================================

_FB_PATHS = ["photo.php", "video/video.php", "video/embed"]
_FB_VPARAMS = ["v", "video_id"]


class YTDL36API(YTDL20API):
    pass


class YTDL36TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))

    def failing_case(self) -> Tuple[str, bool]:
        name = self._word()
        query = f"{self._word()}={self._word()}"
        path = random.choice(_FB_PATHS)
        vp = random.choice(_FB_VPARAMS)
        vid = random.randint(1, 10 ** 15)
        url = f"https://www.facebook.com/{name}?{query}#!/{path}?{vp}={vid}"
        return url, True

    def passing_case(self) -> Tuple[str, bool]:
        path = random.choice(_FB_PATHS)
        vp = random.choice(_FB_VPARAMS)
        vid = random.randint(1, 10 ** 15)
        if random.random() < 0.5:
            url = f"https://www.facebook.com/{path}?{vp}={vid}"
        else:
            url = f"https://www.facebook.com/{self._word()}#!/{path}?{vp}={vid}"
        return url, True


class YTDL36SystemtestGenerator(SystemtestGenerator, YTDL36TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        url, exp = self.failing_case()
        return _b64json({"url": url, "expected": exp}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        url, exp = self.passing_case()
        return _b64json({"url": url, "expected": exp}), TestResult.PASSING


class YTDL36UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL36TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(url: str, exp: bool) -> List[ast.stmt]:
        src = (
            "from youtube_dl.extractor.facebook import FacebookIE\n"
            f"self.assertEqual({exp!r}, FacebookIE.suitable({url!r}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        url, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(url, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        url, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(url, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_12: In ``build_format_selector``, a *negated* string operator built its
# comparator as ``op = lambda attr, value: not str_op`` (negating the function
# object, always ``False``) instead of ``not str_op(attr, value)``.  So any
# negated string filter (``!=``, ``!^=``, ``!$=``, ``!*=``) matched nothing and
# ``process_ie_result`` raised ``ExtractorError: requested format not available``.
#
# System-test format:  a urlsafe-base64 JSON ``{format, formats, expected}``.
#   A ``[format_id!=<id>]`` filter over two formats triggers the fault (the
#   buggy build raises).  The harness prints ``repr(<selected format_id>)``;
#   the oracle (YTDL20API) compares to ``repr(expected)`` (the fixed choice).
# ======================================================================

_FMT_TEST_URL = "http://localhost/sample.mp4"
_FMT_EXTS = ["mp4", "webm", "flv"]


class YTDL12API(YTDL20API):
    pass


class YTDL12TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _fid(self) -> str:
        return f"{self._word()}-{self._word()}"

    def _two(self) -> Tuple[str, str]:
        a = self._fid()
        b = self._fid()
        while b == a:
            b = self._fid()
        return a, b

    def _formats(self, a: str, b: str) -> list:
        return [
            {"format_id": a, "ext": random.choice(_FMT_EXTS), "url": _FMT_TEST_URL},
            {"format_id": b, "ext": random.choice(_FMT_EXTS), "url": _FMT_TEST_URL},
        ]

    def failing_case(self) -> Tuple[str, list, str]:
        a, b = self._two()
        formats = self._formats(a, b)
        if random.random() < 0.5:
            return f"[format_id!={a}]", formats, b
        return f"[format_id!={b}]", formats, a

    def passing_case(self) -> Tuple[str, list, str]:
        a, b = self._two()
        formats = self._formats(a, b)
        if random.random() < 0.5:
            return f"[format_id={a}]", formats, a
        return f"[format_id={b}]", formats, b


class YTDL12SystemtestGenerator(SystemtestGenerator, YTDL12TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fmt, formats, exp = self.failing_case()
        return (
            _b64json({"format": fmt, "formats": formats, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        fmt, formats, exp = self.passing_case()
        return (
            _b64json({"format": fmt, "formats": formats, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL12UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL12TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(fmt: str, formats: list, exp: str) -> List[ast.stmt]:
        info = {
            "formats": formats,
            "id": "testid",
            "title": "t",
            "extractor": "testex",
            "extractor_key": "TestEx",
        }
        src = (
            "from test.helper import FakeYDL\n"
            "class _YDL(FakeYDL):\n"
            "    def __init__(self, *a, **k):\n"
            "        super(_YDL, self).__init__(*a, **k)\n"
            "        self.downloaded_info_dicts = []\n"
            "    def process_info(self, info_dict):\n"
            "        self.downloaded_info_dicts.append(info_dict)\n"
            "    def to_screen(self, msg):\n"
            "        pass\n"
            f"_ydl = _YDL({{'format': {fmt!r}}})\n"
            f"_ydl.process_ie_result(dict({info!r}))\n"
            f"self.assertEqual({exp!r}, _ydl.downloaded_info_dicts[0]['format_id'])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, formats, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, formats, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, formats, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, formats, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_30: the per-format ``selector_function`` did not materialise/guard an
# empty ``formats`` iterable, so a ``best``/``worst`` selection combined with
# a filter that matched no format raised ``IndexError: list index out of
# range`` instead of yielding nothing.  The fix does ``formats =
# list(formats); if not formats: return``.
#
# System-test format:  a urlsafe-base64 JSON ``{format, formats, expected}``.
#   A ``best[<impossible filter>]`` triggers the fault (the buggy build raises
#   IndexError).  The harness catches only ``ExtractorError`` and prints
#   ``repr([<downloaded format_id>...])``; the oracle (YTDL20API) compares to
#   ``repr(expected)`` (the fixed result, an empty list for the failing case).
# ======================================================================


class YTDL30API(YTDL20API):
    pass


class YTDL30TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _formats(self) -> list:
        n = random.randint(3, 5)
        ids, widths = [], []
        while len(ids) < n:
            w = self._word()
            if w not in ids:
                ids.append(w)
        while len(widths) < n:
            x = random.randint(100, 2000)
            if x not in widths:
                widths.append(x)
        return [
            {"format_id": i, "width": w, "url": "http://_/", "ext": "unknown"}
            for i, w in zip(ids, widths)
        ]

    def failing_case(self) -> Tuple[str, list, list]:
        fmts = self._formats()
        maxw = max(f["width"] for f in fmts)
        sel = random.choice(("best", "worst"))
        return f"{sel}[width>{maxw + 1000}]", fmts, []

    def passing_case(self) -> Tuple[str, list, list]:
        fmts = self._formats()
        if random.random() < 0.5:
            minw = min(f["width"] for f in fmts)
            return (
                f"all[width>={minw}]",
                fmts,
                [f["format_id"] for f in fmts],
            )
        chosen = random.choice(fmts)
        return f"best[width={chosen['width']}]", fmts, [chosen["format_id"]]


class YTDL30SystemtestGenerator(SystemtestGenerator, YTDL30TestGenerator):
    @staticmethod
    def _compact(formats: list) -> list:
        return [[f["format_id"], f["width"]] for f in formats]

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fmt, formats, exp = self.failing_case()
        return (
            _b64json({"format": fmt, "fmts": self._compact(formats), "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        fmt, formats, exp = self.passing_case()
        return (
            _b64json({"format": fmt, "fmts": self._compact(formats), "expected": exp}),
            TestResult.PASSING,
        )


class YTDL30UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL30TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(fmt: str, formats: list, exp: list) -> List[ast.stmt]:
        info = {
            "formats": formats,
            "id": "testid",
            "title": "t",
            "extractor": "testex",
            "extractor_key": "TestEx",
        }
        src = (
            "from test.helper import FakeYDL\n"
            "from youtube_dl.utils import ExtractorError\n"
            "class _YDL(FakeYDL):\n"
            "    def __init__(self, *a, **k):\n"
            "        super(_YDL, self).__init__(*a, **k)\n"
            "        self.downloaded_info_dicts = []\n"
            "    def process_info(self, info_dict):\n"
            "        self.downloaded_info_dicts.append(info_dict)\n"
            "    def to_screen(self, msg):\n"
            "        pass\n"
            f"_ydl = _YDL({{'format': {fmt!r}}})\n"
            "try:\n"
            f"    _ydl.process_ie_result(dict({info!r}))\n"
            "except ExtractorError:\n"
            "    pass\n"
            f"self.assertEqual({exp!r}, [d['format_id'] for d in _ydl.downloaded_info_dicts])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, formats, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, formats, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, formats, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, formats, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_8: in ``_parse_format_selection`` the PICKFIRST (``/``) branch did
# ``current_selector = None; selectors.append(FormatSelector(PICKFIRST, ...))``
# instead of ``current_selector = FormatSelector(PICKFIRST, ...)``.  So when a
# ``/`` expression was followed by ``,`` (e.g. ``best/worst,worst``) a ``None``
# selector was appended and later dereferenced -> ``AttributeError: 'NoneType'
# object has no attribute 'type'``.
#
# System-test format:  a urlsafe-base64 JSON ``{format, fmts, expected}`` where
#   ``fmts`` is a list of ``[format_id, tbr]`` progressive mp4 formats.  A
#   ``<sel>/<sel>,<sel>`` format string triggers the fault.  The harness prints
#   ``repr([<downloaded format_id>...])``; the oracle (YTDL20API) compares to
#   ``repr(expected)`` (the fixed download list).
# ======================================================================


class YTDL8API(YTDL20API):
    pass


class YTDL8TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _fmts(self) -> Tuple[list, str, str]:
        n = random.randint(2, 4)
        ids, tbrs = [], []
        while len(ids) < n:
            w = self._word()
            if w not in ids:
                ids.append(w)
        while len(tbrs) < n:
            t = random.randint(50, 3000)
            if t not in tbrs:
                tbrs.append(t)
        fmts = list(zip(ids, tbrs))
        # Formats are not _sort_formats'd, so 'best' == last, 'worst' == first.
        hi = ids[-1]
        lo = ids[0]
        return fmts, hi, lo

    def failing_case(self) -> Tuple[str, list, list]:
        fmts, hi, lo = self._fmts()
        mid = random.choice(("best", "worst"))
        if random.random() < 0.5:
            fmt = f"best/{mid},worst"
            exp = [hi, lo]
        else:
            fmt = f"worst/{mid},best"
            exp = [lo, hi]
        return fmt, fmts, exp

    def passing_case(self) -> Tuple[str, list, list]:
        fmts, hi, lo = self._fmts()
        r = random.random()
        if r < 0.34:
            return "best/worst", fmts, [hi]
        if r < 0.67:
            return "best,worst", fmts, [hi, lo]
        return "worst,best", fmts, [lo, hi]


class YTDL8SystemtestGenerator(SystemtestGenerator, YTDL8TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fmt, fmts, exp = self.failing_case()
        return (
            _b64json({"format": fmt, "fmts": fmts, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        fmt, fmts, exp = self.passing_case()
        return (
            _b64json({"format": fmt, "fmts": fmts, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL8UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL8TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(fmt: str, fmts: list, exp: list) -> List[ast.stmt]:
        formats = [
            {
                "format_id": i,
                "ext": "mp4",
                "url": "http://_/",
                "vcodec": "h264",
                "acodec": "aac",
                "tbr": t,
            }
            for i, t in fmts
        ]
        info = {
            "formats": formats,
            "id": "testid",
            "title": "t",
            "extractor": "testex",
            "extractor_key": "TestEx",
        }
        src = (
            "from test.helper import FakeYDL\n"
            "class _YDL(FakeYDL):\n"
            "    def __init__(self, *a, **k):\n"
            "        super(_YDL, self).__init__(*a, **k)\n"
            "        self.downloaded_info_dicts = []\n"
            "    def process_info(self, info_dict):\n"
            "        self.downloaded_info_dicts.append(info_dict)\n"
            "    def to_screen(self, msg):\n"
            "        pass\n"
            f"_ydl = _YDL({{'format': {fmt!r}}})\n"
            f"_ydl.process_ie_result(dict({info!r}))\n"
            f"self.assertEqual({exp!r}, [d['format_id'] for d in _ydl.downloaded_info_dicts])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, fmts, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, fmts, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, fmts, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, fmts, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_9: the older ``_parse_format_selection(tokens, endwith=[])`` parser
# consumed the ``/`` fallback into the *audio* side of a ``+`` merge, so
# ``bestvideo[<impossible>]+bestaudio/best`` was parsed as
# ``MERGE(video, PICKFIRST(audio, best))`` instead of
# ``PICKFIRST(MERGE(video, audio), best)``.  With an impossible video side the
# merge failed and, lacking the outer fallback, raised ``ExtractorError:
# requested format not available``.  The fix reworks the parser with explicit
# ``inside_merge``/``inside_choice``/``inside_group`` boundaries.
#
# System-test format:  a urlsafe-base64 JSON ``{format, ids, expected}`` where
#   ``ids`` is ``[video_only, audio_only, progressive]``.  A
#   ``bestvideo[<absent-field>>=<big>]+bestaudio/<fallback>`` triggers the
#   fault (the buggy build raises).  The harness prints ``repr([<downloaded
#   format_id>...])``; the oracle (YTDL20API) compares to ``repr(expected)``.
# ======================================================================


class YTDL9API(YTDL20API):
    pass


class YTDL9TestGenerator:
    _FIELDS = ["height", "width", "filesize", "fps", "abr"]

    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _ids(self) -> Tuple[str, str, str]:
        s = set()
        while len(s) < 3:
            s.add(self._word())
        return tuple(s)

    def failing_case(self) -> Tuple[str, list, list]:
        vv, aa, pp = self._ids()
        field = random.choice(self._FIELDS)
        big = random.randint(100000, 999999999)
        audiosel = random.choice(("bestaudio", "worstaudio"))
        fallback = random.choice(("best", "worst"))
        fmt = f"bestvideo[{field}>={big}]+{audiosel}/{fallback}"
        return fmt, [vv, aa, pp], [pp]

    def passing_case(self) -> Tuple[str, list, list]:
        vv, aa, pp = self._ids()
        r = random.random()
        if r < 0.25:
            return "best", [vv, aa, pp], [pp]
        if r < 0.5:
            return "worst", [vv, aa, pp], [pp]
        if r < 0.75:
            return "bestvideo+bestaudio", [vv, aa, pp], [f"{vv}+{aa}"]
        return "bestvideo", [vv, aa, pp], [vv]


class YTDL9SystemtestGenerator(SystemtestGenerator, YTDL9TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        fmt, ids, exp = self.failing_case()
        return (
            _b64json({"format": fmt, "ids": ids, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        fmt, ids, exp = self.passing_case()
        return (
            _b64json({"format": fmt, "ids": ids, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL9UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL9TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(fmt: str, ids: list, exp: list) -> List[ast.stmt]:
        vv, aa, pp = ids
        formats = [
            {"format_id": vv, "ext": "mp4", "url": "http://_/",
             "vcodec": "h264", "acodec": "none", "tbr": 100},
            {"format_id": aa, "ext": "m4a", "url": "http://_/",
             "vcodec": "none", "acodec": "aac", "tbr": 50},
            {"format_id": pp, "ext": "mp4", "url": "http://_/",
             "vcodec": "h264", "acodec": "aac", "tbr": 150},
        ]
        info = {
            "formats": formats,
            "id": "testid",
            "title": "t",
            "extractor": "testex",
            "extractor_key": "TestEx",
        }
        src = (
            "from test.helper import FakeYDL\n"
            "class _YDL(FakeYDL):\n"
            "    def __init__(self, *a, **k):\n"
            "        super(_YDL, self).__init__(*a, **k)\n"
            "        self.downloaded_info_dicts = []\n"
            "    def process_info(self, info_dict):\n"
            "        self.downloaded_info_dicts.append(info_dict)\n"
            "    def to_screen(self, msg):\n"
            "        pass\n"
            f"_ydl = _YDL({{'format': {fmt!r}}})\n"
            f"_ydl.process_ie_result(dict({info!r}))\n"
            f"self.assertEqual({exp!r}, [d['format_id'] for d in _ydl.downloaded_info_dicts])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, ids, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, ids, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        fmt, ids, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(fmt, ids, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_19: ``prepare_filename`` applied ``expand_path`` *after* the ``outtmpl %
# template_dict`` substitution, so a meta field value containing an env-var
# reference (e.g. a title of ``foo $HOME bar``) was wrongly expanded.  The fix
# expands the template BEFORE substitution (protecting ``%%``/``$$`` with a
# random separator), so field values are left literal.
#
# System-test format:  a urlsafe-base64 JSON ``{outtmpl, info, expected}``.
#   The harness pre-sets an env var ``T4PVAR=XPANDED`` and a field value
#   contains ``$T4PVAR`` followed by a boundary, so the buggy build expands it
#   to ``XPANDED`` while the fixed build keeps ``$T4PVAR`` literal.  The harness
#   prints ``repr(prepare_filename(info))``; the oracle (YTDL20API) compares to
#   ``repr(expected)`` (the fixed, literal filename).
# ======================================================================


class YTDL19API(YTDL20API):
    pass


class YTDL19TestGenerator:
    _EXTS = ["mp4", "webm", "mkv", "m4a"]

    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def failing_case(self) -> Tuple[str, dict, str]:
        w1, w2 = self._word(), self._word()
        ext = random.choice(self._EXTS)
        vid = str(random.randint(1, 999999))
        title = f"{w1} $T4PVAR {w2}"
        info = {"id": vid, "ext": ext, "title": title}
        # fixed keeps $T4PVAR literal
        expected = f"{title}.{ext}"
        return "%(title)s.%(ext)s", info, expected

    def passing_case(self) -> Tuple[str, dict, str]:
        w1, w2 = self._word(), self._word()
        ext = random.choice(self._EXTS)
        vid = str(random.randint(1, 999999))
        title = f"{w1} {w2}"  # no env-var reference: identical on both builds
        info = {"id": vid, "ext": ext, "title": title}
        if random.random() < 0.5:
            return "%(title)s.%(ext)s", info, f"{title}.{ext}"
        return "%(title)s-%(id)s.%(ext)s", info, f"{title}-{vid}.{ext}"


class YTDL19SystemtestGenerator(SystemtestGenerator, YTDL19TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        outtmpl, info, exp = self.failing_case()
        return (
            _b64json({"outtmpl": outtmpl, "info": info, "expected": exp}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        outtmpl, info, exp = self.passing_case()
        return (
            _b64json({"outtmpl": outtmpl, "info": info, "expected": exp}),
            TestResult.PASSING,
        )


class YTDL19UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL19TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(outtmpl: str, info: dict, exp: str) -> List[ast.stmt]:
        src = (
            "import os\n"
            "os.environ['T4PVAR'] = 'XPANDED'\n"
            "from youtube_dl import YoutubeDL\n"
            f"_fn = YoutubeDL({{'outtmpl': {outtmpl!r}}}).prepare_filename({info!r})\n"
            f"self.assertEqual({exp!r}, _fn)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        outtmpl, info, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(outtmpl, info, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        outtmpl, info, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(outtmpl, info, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_2: ``InfoExtractor._parse_mpd_formats`` de-duplicated DASH formats by
# ``format_id`` (``existing_format.update(f)``), but a DASH manifest may
# legitimately contain several Representations sharing the same ``id`` (in
# different AdaptationSets).  The buggy build merged them into one format,
# dropping the rest.  The fix always appends each Representation.
#
# System-test format:  a urlsafe-base64 JSON ``{reps, expected}`` where
#   ``reps`` is a list of ``[mime_code, rep_id, bandwidth]`` (``a``/``v``).  A
#   duplicate ``rep_id`` triggers the fault.  The harness builds the MPD,
#   parses it and prints ``repr(sorted(format_ids))``; the oracle (YTDL20API)
#   compares to ``repr(expected)`` (the fixed, non-collapsed id multiset).
# ======================================================================

_MPD_MIME = {"a": "audio/mp4", "v": "video/mp4"}


def _mpd_build(reps: list) -> str:
    sets = ""
    for code, rid, bw in reps:
        sets += (
            '<AdaptationSet mimeType="%s" codecs="mp4a.40.2">'
            '<SegmentTemplate timescale="1000000" '
            'initialization="i_$RepresentationID$.m4d" '
            'media="s_$RepresentationID$_$Number$.m4d" '
            'duration="2000000" startNumber="0"></SegmentTemplate>'
            '<Representation id="%s" bandwidth="%d"></Representation>'
            "</AdaptationSet>"
        ) % (_MPD_MIME[code], rid, bw)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" '
        'mediaPresentationDuration="PT10S">'
        "<Period>" + sets + "</Period></MPD>"
    )


class YTDL2API(YTDL20API):
    pass


class YTDL2TestGenerator:
    @staticmethod
    def _id() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _distinct_ids(self, n: int) -> list:
        s = []
        while len(s) < n:
            w = self._id()
            if w not in s:
                s.append(w)
        return s

    def failing_case(self) -> Tuple[list, list]:
        ids = self._distinct_ids(random.randint(2, 3))
        dup = random.choice(ids)
        reps = [["v", i, random.randint(50000, 6000000)] for i in ids]
        reps.insert(
            random.randint(0, len(reps)),
            ["a", dup, random.randint(50000, 200000)],
        )
        expected = sorted([r[1] for r in reps])
        return reps, expected

    def passing_case(self) -> Tuple[list, list]:
        ids = self._distinct_ids(random.randint(2, 4))
        reps = [
            [random.choice(("a", "v")), i, random.randint(50000, 6000000)]
            for i in ids
        ]
        expected = sorted(ids)
        return reps, expected


class YTDL2SystemtestGenerator(SystemtestGenerator, YTDL2TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        reps, exp = self.failing_case()
        return _b64json({"reps": reps, "expected": exp}), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        reps, exp = self.passing_case()
        return _b64json({"reps": reps, "expected": exp}), TestResult.PASSING


class YTDL2UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL2TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(reps: list, exp: list) -> List[ast.stmt]:
        xml = _mpd_build(reps)
        src = (
            "from test.helper import FakeYDL\n"
            "from youtube_dl.extractor.common import InfoExtractor\n"
            "from youtube_dl.compat import compat_etree_fromstring\n"
            "class _IE(InfoExtractor):\n"
            "    _VALID_URL = 'https?://.*'\n"
            "_ie = _IE(FakeYDL())\n"
            f"_formats = _ie._parse_mpd_formats(compat_etree_fromstring({xml!r}.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')\n"
            f"self.assertEqual({exp!r}, sorted(f['format_id'] for f in _formats))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        reps, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(reps, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        reps, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(reps, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_18: when resolving a ``url_transparent`` result, ``YoutubeDL`` deleted
# only ``('_type', 'url', 'ie_key')`` from the transparent result's
# ``force_properties`` before overlaying them onto the final result, so the
# transparent entry's ``id``/``extractor``/``extractor_key`` wrongly
# overrode the real extractor's values.  The fix also deletes ``id``,
# ``extractor`` and ``extractor_key``.
#
# System-test format:  a urlsafe-base64 JSON ``{t_id, t_title, final_id, field,
#   expected}``.  A ``url_transparent`` chain is built in-memory (no network);
#   for ``field == 'id'`` the buggy build reports the transparent ``t_id``
#   instead of the real ``final_id``.  The harness prints
#   ``repr(downloaded[field])``; the oracle (YTDL20API) compares to
#   ``repr(expected)`` (the fixed value).
# ======================================================================


class YTDL18API(YTDL20API):
    pass


class YTDL18TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))

    def failing_case(self) -> Tuple[str, str, str, str, str]:
        t_id = "t_" + self._word()
        final_id = "f_" + self._word()
        t_title = self._word() + " " + self._word()
        # buggy reports t_id, fixed reports final_id
        return t_id, t_title, final_id, "id", final_id

    def passing_case(self) -> Tuple[str, str, str, str, str]:
        t_id = "t_" + self._word()
        final_id = "f_" + self._word()
        t_title = self._word() + " " + self._word()
        # title propagates from the transparent entry on both builds
        return t_id, t_title, final_id, "title", t_title


class YTDL18SystemtestGenerator(SystemtestGenerator, YTDL18TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        t_id, t_title, final_id, field, exp = self.failing_case()
        return (
            _b64json(
                {
                    "t_id": t_id,
                    "t_title": t_title,
                    "final_id": final_id,
                    "field": field,
                    "expected": exp,
                }
            ),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        t_id, t_title, final_id, field, exp = self.passing_case()
        return (
            _b64json(
                {
                    "t_id": t_id,
                    "t_title": t_title,
                    "final_id": final_id,
                    "field": field,
                    "expected": exp,
                }
            ),
            TestResult.PASSING,
        )


class YTDL18UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL18TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(t_id, t_title, final_id, field, exp) -> List[ast.stmt]:
        src = (
            "from test.helper import FakeYDL\n"
            "from youtube_dl.extractor.common import InfoExtractor\n"
            "class _YDL(FakeYDL):\n"
            "    def __init__(self, *a, **k):\n"
            "        super(_YDL, self).__init__(*a, **k)\n"
            "        self.downloaded_info_dicts = []\n"
            "    def process_info(self, info_dict):\n"
            "        self.downloaded_info_dicts.append(info_dict)\n"
            "    def to_screen(self, msg):\n"
            "        pass\n"
            "_ydl = _YDL()\n"
            "class Foo1IE(InfoExtractor):\n"
            "    _VALID_URL = 'foo1:'\n"
            "    def _real_extract(self, url):\n"
            f"        return {{'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': {t_title!r}, 'id': {t_id!r}}}\n"
            "class Foo2IE(InfoExtractor):\n"
            "    _VALID_URL = 'foo2:'\n"
            "    def _real_extract(self, url):\n"
            "        return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}\n"
            "class Foo3IE(InfoExtractor):\n"
            "    _VALID_URL = 'foo3:'\n"
            "    def _real_extract(self, url):\n"
            f"        return {{'formats': [{{'url': 'http://localhost/sample.mp4'}}], 'id': {final_id!r}, 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}}\n"
            "_ydl.add_info_extractor(Foo1IE(_ydl))\n"
            "_ydl.add_info_extractor(Foo2IE(_ydl))\n"
            "_ydl.add_info_extractor(Foo3IE(_ydl))\n"
            "_ydl.extract_info('foo1:')\n"
            f"self.assertEqual({exp!r}, _ydl.downloaded_info_dicts[0][{field!r}])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        t_id, t_title, final_id, field, exp = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(t_id, t_title, final_id, field, exp)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        t_id, t_title, final_id, field, exp = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(t_id, t_title, final_id, field, exp)
        return test, TestResult.PASSING


# ======================================================================
# bug_14: ``YoutubeIE._extract_chapters(description, duration)`` (a
# staticmethod) was renamed to ``_extract_chapters_from_description`` (and a
# new instance method ``_extract_chapters`` with a different signature added)
# so YouTube chapters could also be sourced from the watch-next JSON.  On the
# buggy build ``_extract_chapters_from_description`` does not exist, so the
# description-based chapter extraction the test exercises raises
# ``AttributeError``.
#
# System-test format:  a urlsafe-base64 JSON ``{chapters, dur, method}`` where
#   ``chapters`` is a list of ``[start_seconds, title]``.  ``method == 'new'``
#   (failing) calls ``_extract_chapters_from_description`` -> AttributeError on
#   the buggy build; ``method == 'old'`` (passing) calls the extant
#   ``_extract_chapters``.  The harness rebuilds the description, runs the
#   chosen method and prints ``repr(result)``; the oracle recomputes the
#   correct chapters and compares.
# ======================================================================


def _ytc_pdur(t: str) -> float:
    parts = [float(p) for p in t.split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def _ytc_fmt(s: int) -> str:
    if s >= 3600:
        return "%d:%02d:%02d" % (s // 3600, (s % 3600) // 60, s % 60)
    return "%d:%02d" % (s // 60, s % 60)


def _ytc_build(chapters: list) -> str:
    lines = []
    for sec, title in chapters:
        lines.append(
            '<a href="#" onclick="yt.www.watch.player.seekTo(%d);return false;">'
            "%s</a> - %s" % (sec, _ytc_fmt(sec), title)
        )
    return "<br />".join(lines)


def _ytc_extract(description: str, duration):
    if not description:
        return None
    chapter_lines = re.findall(
        r'(?:^|<br\s*/>)([^<]*<a[^>]+onclick=["\']yt\.www\.watch\.player\.seekTo'
        r'[^>]+>(\d{1,2}:\d{1,2}(?::\d{1,2})?)</a>[^>]*)(?=$|<br\s*/>)',
        description,
    )
    if not chapter_lines:
        return None
    chapters = []
    for next_num, (chapter_line, time_point) in enumerate(chapter_lines, start=1):
        start_time = _ytc_pdur(time_point)
        if start_time is None:
            continue
        if start_time > duration:
            break
        end_time = (
            duration
            if next_num == len(chapter_lines)
            else _ytc_pdur(chapter_lines[next_num][1])
        )
        if end_time is None:
            continue
        if end_time > duration:
            end_time = duration
        if start_time > end_time:
            break
        chapter_title = re.sub(r"<a[^>]+>[^<]+</a>", "", chapter_line).strip(" \t-")
        chapter_title = re.sub(r"\s+", " ", chapter_title)
        chapters.append(
            {"start_time": start_time, "end_time": end_time, "title": chapter_title}
        )
    return chapters


class YTDL14API(YTDLAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            d = json.loads(base64.urlsafe_b64decode(process.args[2]).decode("utf-8"))
            desc = _ytc_build([tuple(c) for c in d["chapters"]])
            expected = repr(_ytc_extract(desc, d["dur"]))
        except (IndexError, ValueError, KeyError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class YTDL14TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_letters, k=random.randint(3, 8)))

    def _title(self) -> str:
        return " ".join(self._word() for _ in range(random.randint(1, 3)))

    def _chapters(self) -> Tuple[list, int]:
        n = random.randint(1, 3)
        secs = sorted(random.sample(range(0, 3000), n))
        chapters = [[s, self._title()] for s in secs]
        dur = secs[-1] + random.randint(1, 500)
        return chapters, dur

    def failing_case(self) -> Tuple[list, int, str]:
        chapters, dur = self._chapters()
        return chapters, dur, "new"

    def passing_case(self) -> Tuple[list, int, str]:
        chapters, dur = self._chapters()
        return chapters, dur, "old"


class YTDL14SystemtestGenerator(SystemtestGenerator, YTDL14TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        chapters, dur, method = self.failing_case()
        return (
            _b64json({"chapters": chapters, "dur": dur, "method": method}),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        chapters, dur, method = self.passing_case()
        return (
            _b64json({"chapters": chapters, "dur": dur, "method": method}),
            TestResult.PASSING,
        )


class YTDL14UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, YTDL14TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return []

    @staticmethod
    def _body(chapters: list, dur: int, method: str) -> List[ast.stmt]:
        desc = _ytc_build([tuple(c) for c in chapters])
        expected = _ytc_extract(desc, dur)
        call = (
            "_extract_chapters_from_description"
            if method == "new"
            else "_extract_chapters"
        )
        src = (
            "from youtube_dl.extractor import YoutubeIE\n"
            f"_res = YoutubeIE.{call}({desc!r}, {dur!r})\n"
            f"self.assertEqual({expected!r}, _res)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        chapters, dur, method = self.failing_case()
        test = self.get_empty_test()
        test.body = self._body(chapters, dur, method)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        chapters, dur, method = self.passing_case()
        test = self.get_empty_test()
        test.body = self._body(chapters, dur, method)
        return test, TestResult.PASSING
