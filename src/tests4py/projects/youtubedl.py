import os
from pathlib import Path
from typing import List, Optional, Tuple

from tests4py.constants import PYTHON
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
            grammar=None,
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
        api=YoutubeDLAPI(b"Input does not match the expected outcome!"),
        # unittests=YoutubeDLUnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),
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
        api=YoutubeDLAPI(b"Input does not match the expected outcome!"),
        # unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),
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
        loc=46060,
    )
    YoutubeDL(
        bug_id=11,
        buggy_commit_id="b568561eba6f4aceb87419e21aba11567c5de7da",
        fixed_commit_id="348c6bf1c1a00eec323d6e21ff7b9b12699afe04",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_str_to_int")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
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
        loc=111758,
    )
    YoutubeDL(
        bug_id=13,
        buggy_commit_id="6945b9e78f38284eb4e440b7badea2fc60b66c2f",
        fixed_commit_id="fad4ceb53404227f471af2f3544c4c14a5df4acb",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_urljoin")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
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
        loc=103448,
    )
    YoutubeDL(
        bug_id=16,
        buggy_commit_id="68d43a61b552007a718894967b869c0f1d8ff00f",
        fixed_commit_id="3869028ffb6be6ab719e5cf1004276dfdfd1216d",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_dfxp2srt")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
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
        loc=98099,
    )
    YoutubeDL(
        bug_id=21,
        buggy_commit_id="96182695e4e37795a30ab143129c91dab18a9865",
        fixed_commit_id="4b5de77bdb7765df4797bf068592926285ba709a",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_urljoin")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
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
        loc=38981,
    )
    YoutubeDL(
        bug_id=32,
        buggy_commit_id="bf951c5e29548cfed80480389762edd29fcc8825",
        fixed_commit_id="609a61e3e6fffce3d45e845f33ae2c5fa2d432ac",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_strip_jsonp")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
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
        loc=37170,
    )
    YoutubeDL(
        bug_id=34,
        buggy_commit_id="07e764439a1cdd3a3b95fbf21acc6a517c6a889e",
        fixed_commit_id="410f3e73ab268f74a455798ee39de5caba90caea",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_js_to_json")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
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
        loc=21863,
    )
    YoutubeDL(
        bug_id=39,
        buggy_commit_id="b04c8f735805ea2671429ac8d683c2887a6b4db8",
        fixed_commit_id="a020a0dc20ced6468ec46214c394f6f360735b1d",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_limit_length")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
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
        loc=17770,
    )
    YoutubeDL(
        bug_id=43,
        buggy_commit_id="cecaaf3f58ad9f544dbb79af1e565d9353fa2b2d",
        fixed_commit_id="d6c7a367e88096bb17e323954002c084477fe908",
        test_files=[Path("test", "test_utils.py")],
        test_cases=[os.path.join("test", "test_utils.py::TestUtil::test_url_basename")],
        relevant_test_files=[os.path.join("test", "test_utils.py::TestUtil")],
        api=YoutubeDLAPI(b"Input does not match the expected outcome!"),
        # unittests=YoutubeDL1UnittestGenerator(),
        systemtests=YoutubeDLSystemtestGenerator(),
        loc=16339,
    )


class YoutubeDLAPI(ExpectErrAPI):
    pass


class YoutubeDLSystemtestGenerator(SystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass
