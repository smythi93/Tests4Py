import ast
import base64
import os.path
import random
import string
import subprocess
from collections import OrderedDict
from pathlib import Path
from typing import Any, List, Optional, Tuple

from tests4py.grammars.default import clean_up
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "scrapy"


class Scrapy(Project):
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
            github_url="https://github.com/scrapy/scrapy",
            status=Status.OK,
            python_version="3.8.3",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version="3.8.4",
            python_fallback_version="3.8.4",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar,
            loc=loc,
            source_base=Path(PROJECT_NAME),
            test_base=Path("tests"),
            included_files=[PROJECT_NAME],
            setup=[
                ["python", "-m", "pip", "install", "-e", "."],
            ],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
            test_command_arguments=["--reactor=asyncio"],
        )

    def patch(self, location: Path):
        if self.bug_id in (6, 13):
            path = location / "tests" / "test_pipeline_images.py"
            with open(path, "r") as f:
                content = f.read()
            content = content.replace("\nskip = False", "")
            content = content.replace("\n\n    skip = skip", "")
            with open(path, "w") as f:
                f.write(content)

            path = location / "scrapy" / "pipelines" / "images.py"
            with open(path, "r") as f:
                content = f.read()
            content = content.replace("ANTIALIAS", "LANCZOS")
            with open(path, "w") as f:
                f.write(content)


def register():
    Scrapy(
        bug_id=1,
        buggy_commit_id="c57512fa669e6f6b1b766a7639206a380f0d10ce",
        fixed_commit_id="9d9dea0d69709ef0f7aef67ddba1bd7bda25d273",
        test_files=[Path("tests", "test_spidermiddleware_offsite.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_spidermiddleware_offsite.py::TestOffsiteMiddleware4::test_process_spider_output",
            ),
            os.path.join(
                "tests",
                "test_spidermiddleware_offsite.py::TestOffsiteMiddleware5::test_get_host_regex",
            ),
            os.path.join(
                "tests",
                "test_spidermiddleware_offsite.py::TestOffsiteMiddleware5::test_process_spider_output",
            ),
        ],
        loc=11497,
    )
    Scrapy(
        bug_id=2,
        buggy_commit_id="f02c3d1dcf3e4880388d19e961e7911be5dc54ff",
        fixed_commit_id="439a3e59b8e858441f8d97dbc32f398db392330d",
        test_files=[Path("tests", "test_utils_datatypes.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils_datatypes.py::LocalCacheTest::test_cache_without_limit",
            )
        ],
        api=Scrapy2API(),
        unittests=Scrapy2UnittestGenerator(),
        systemtests=Scrapy2SystemtestGenerator(),
        grammar=grammar_local_cache,
        loc=11308,
    )
    Scrapy(
        bug_id=3,
        buggy_commit_id="be2e910dd06ba4904e7b10eb5a7e3251e8dab099",
        fixed_commit_id="66cbceeb0a9104fc0fa238898e38d0d9ce9cbcf6",
        test_files=[Path("tests", "test_downloadermiddleware_redirect.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloadermiddleware_redirect.py::RedirectMiddlewareTest::test_redirect_302_relative",
            )
        ],
        loc=11360,
    )
    Scrapy(
        bug_id=4,
        buggy_commit_id="c8f3d07e86dd41074971b5423fb932c2eda6db1e",
        fixed_commit_id="16dad81715d3970149c0cf7a318e73a0d84be1ff",
        test_files=[Path("tests", "test_contracts.py")],
        test_cases=[
            os.path.join(
                "tests", "test_contracts.py::ContractsManagerTest::test_errback"
            )
        ],
        loc=10929,
    )
    Scrapy(
        bug_id=5,
        buggy_commit_id="426da0ed07637e7efbcfb0fe49546e187d5d7f67",
        fixed_commit_id="acd2b8d43b5ebec7ffd364b6f335427041a0b98d",
        test_files=[Path("tests", "test_http_response.py")],
        test_cases=[
            os.path.join(
                "tests", "test_http_response.py::BaseResponseTest::test_follow_None_url"
            )
        ],
        relevant_test_files=[
            os.path.join("tests", "test_http_response.py::BaseResponseTest")
        ],
        skip_tests=["test_follow_whitespace_link", "test_follow_whitespace_url"],
        api=Scrapy5API(),
        unittests=Scrapy5UnittestGenerator(),
        systemtests=Scrapy5SystemtestGenerator(),
        grammar=grammar_follow,
        loc=11279,
    )
    Scrapy(
        bug_id=6,
        buggy_commit_id="8aa2e4f9976d31bbe3a0014b4f1f96ace1b87043",
        fixed_commit_id="25f609e2a3c27ca7d7d98dbfddb2c049735935bb",
        test_files=[Path("tests", "test_pipeline_images.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_pipeline_images.py::ImagesPipelineTestCase::test_convert_image",
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=11094,
    )
    Scrapy(
        bug_id=7,
        buggy_commit_id="e1ceaf3b5fa29326f032c4ed3f50943384b9e63d",
        fixed_commit_id="074caf434e255bc96f106e57e3e288028f372485",
        test_files=[Path("tests", "test_http_request.py")],
        test_cases=[
            os.path.join(
                "tests", "test_http_request.py::FormRequestTest::test_spaces_in_action"
            )
        ],
        relevant_test_files=[
            os.path.join("tests", "test_http_request.py::FormRequestTest")
        ],
        api=Scrapy7API(),
        unittests=Scrapy7UnittestGenerator(),
        systemtests=Scrapy7SystemtestGenerator(),
        grammar=grammar_form_action,
        loc=10630,
    )
    Scrapy(
        bug_id=8,
        buggy_commit_id="f2f9350c47db73bdfb60773601b59b0633e1595a",
        fixed_commit_id="4e765acaed7a914630ee5320fa6f6523890a2b9d",
        test_files=[Path("tests", "test_item.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_item.py::ItemMetaTest::test_new_method_propagates_classcell",
            ),
            os.path.join(
                "tests",
                "test_item.py::ItemMetaClassCellRegression::test_item_meta_classcell_regression",
            ),
        ],
        loc=10604,
    )
    Scrapy(
        bug_id=9,
        buggy_commit_id="a9c69458ff1667cc4d20ba25bb6a0dd9a5a08ce6",
        fixed_commit_id="ff3aec661355a82a6f77355a95e1f391fa586c2b",
        test_files=[Path("tests", "test_mail.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_mail.py::MailSenderTest::test_send_single_values_to_and_cc",
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=12317,
    )
    Scrapy(
        bug_id=10,
        buggy_commit_id="6cc83c041eac36e7688dbd9c4c55487a43b622e0",
        fixed_commit_id="db408528928b2d15043593032913fe40d6eb6783",
        test_files=[Path("tests", "test_downloadermiddleware_redirect.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloadermiddleware_redirect.py::RedirectMiddlewareTest::test_latin1_location",
            ),
            os.path.join(
                "tests",
                "test_downloadermiddleware_redirect.py::RedirectMiddlewareTest::test_utf8_location",
            ),
        ],
        loc=12289,
    )
    Scrapy(
        bug_id=11,
        buggy_commit_id="241bd00e76df142a24699819f8496bdec8f5c83a",
        fixed_commit_id="9de6f1ca757b7f200d15e94840c9d431cf202276",
        test_files=[
            Path("tests", "test_utils_gz.py"),
            Path("tests", "sample_data", "compressed", "unexpected-eof.gz"),
            Path("tests", "sample_data", "compressed", "unexpected-eof-output.txt"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_utils_gz.py::GunzipTest::test_gunzip_illegal_eof"
            )
        ],
        relevant_test_files=[
            Path("tests", "test_utils_gz.py"),
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=12258,
    )
    Scrapy(
        bug_id=12,
        buggy_commit_id="34e7dadf38ba1796094c0c76e92ea8d9837681cc",
        fixed_commit_id="2c9a38d1f54a12c33d7c9a19e021c840c4a32dee",
        test_files=[
            Path("tests", "test_selector.py"),
            Path("tests", "test_selector_csstranslator.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_selector.py::SelectorTestCase::test_selector_bad_args"
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=12321,
    )
    Scrapy(
        bug_id=13,
        buggy_commit_id="fa78849e335994a1617ed63221a70940c21cca20",
        fixed_commit_id="414857a593ad5b82fa21d6344928f43f93dc9f14",
        test_files=[Path("tests", "test_pipeline_images.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_pipeline_images.py::ImagesPipelineTestCaseCustomSettings::"
                "test_different_settings_for_different_instances",
            ),
            os.path.join(
                "tests",
                "test_pipeline_images.py::ImagesPipelineTestCaseCustomSettings::"
                "test_no_custom_settings_for_subclasses",
            ),
        ],
        loc=12324,
    )
    Scrapy(
        bug_id=14,
        buggy_commit_id="b7553d921afe356ec858bb1d2e5b1702df05ea24",
        fixed_commit_id="d43a35735a062a4260b002cfbcd3236c77ef9399",
        test_files=[Path("tests", "test_utils_gz.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils_gz.py::GunzipTest::test_is_gzipped_case_insensitive",
            ),
            os.path.join(
                "tests", "test_utils_gz.py::GunzipTest::test_is_gzipped_with_charset"
            ),
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=12222,
    )
    Scrapy(
        bug_id=15,
        buggy_commit_id="b7925e42202d79d2ba9d00b6aded3a451c92fe81",
        fixed_commit_id="1aec5200bc81493623f2a4e077b4e80e104e47d5",
        test_files=[Path("tests", "test_utils_url.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_canonicalize_url_idna_exceptions",
            )
        ],
        relevant_test_files=[
            os.path.join("tests", "test_utils_url.py::CanonicalizeUrlTest")
        ],
        api=Scrapy15API(),
        unittests=Scrapy15UnittestGenerator(),
        systemtests=Scrapy15SystemtestGenerator(),
        grammar=grammar_b64,
        loc=12209,
    )
    Scrapy(
        bug_id=16,
        buggy_commit_id="73a5571c6044d5aea47b4f973e325c2f3d4e25dc",
        fixed_commit_id="68dedf54cb27847f6d035099b61aa06226549fad",
        test_files=[Path("tests", "test_utils_url.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_canonicalize_url_unicode_query_string",
            ),
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_normalize_percent_encoding_in_paths",
            ),
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_normalize_percent_encoding_in_query_arguments",
            ),
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_canonicalize_idns",
            ),
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_canonicalize_urlparsed",
            ),
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_canonicalize_parse_url",
            ),
            os.path.join(
                "tests",
                "test_utils_url.py::CanonicalizeUrlTest::test_safe_characters_unicode",
            ),
        ],
        relevant_test_files=[
            os.path.join("tests", "test_utils_url.py::CanonicalizeUrlTest")
        ],
        loc=12154,
    )
    Scrapy(
        bug_id=17,
        buggy_commit_id="ebef6d7c6dd8922210db8a4a44f48fe27ee0cd16",
        fixed_commit_id="65c7c05060fd2d1fc161d4904243d5e0b31e202b",
        test_files=[Path("tests", "test_utils_response.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils_response.py::ResponseUtilsTest::test_response_status_message",
            )
        ],
        api=Scrapy17API(),
        unittests=Scrapy17UnittestGenerator(),
        systemtests=Scrapy17SystemtestGenerator(),
        grammar=grammar_status,
        loc=12107,
    )
    Scrapy(
        bug_id=18,
        buggy_commit_id="41588397c04356f2b0c393b61ed68271a08d6ccd",
        fixed_commit_id="cabed6f183cfb2ab778c57be8c75802fec5e54d4",
        test_files=[Path("tests", "test_responsetypes.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_responsetypes.py::ResponseTypesTest::test_from_content_disposition",
            )
        ],
        api=Scrapy18API(),
        unittests=Scrapy18UnittestGenerator(),
        systemtests=Scrapy18SystemtestGenerator(),
        grammar=grammar_b64,
        loc=11899,
    )
    Scrapy(
        bug_id=19,
        buggy_commit_id="e328a9b9dfa4fbc79c59ed4f45f757e998301c31",
        fixed_commit_id="1f743996ff00a7b728d59b93d0967e1eb50072f0",
        test_files=[Path("tests", "test_http_cookies.py")],
        test_cases=[
            os.path.join(
                "tests", "test_http_cookies.py::WrappedRequestTest::test_get_full_url"
            ),
            os.path.join(
                "tests", "test_http_cookies.py::WrappedRequestTest::test_get_host"
            ),
            os.path.join(
                "tests", "test_http_cookies.py::WrappedRequestTest::test_get_type"
            ),
            os.path.join(
                "tests",
                "test_http_cookies.py::WrappedRequestTest::test_get_origin_req_host",
            ),
        ],
        api=Scrapy19API(),
        unittests=Scrapy19UnittestGenerator(),
        systemtests=Scrapy19SystemtestGenerator(),
        grammar=grammar_wrapped_request,
        loc=11868,
    )
    Scrapy(
        bug_id=20,
        buggy_commit_id="e328a9b9dfa4fbc79c59ed4f45f757e998301c31",
        fixed_commit_id="25c56159b86288311630cc0cf6db9d755aeeff1e",
        test_files=[Path("tests", "test_spider.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_spider.py::SitemapSpiderTest::test_get_sitemap_urls_from_robotstxt",
            )
        ],
        relevant_test_files=[
            os.path.join("tests", "test_spider.py::SitemapSpiderTest"),
        ],
        loc=11868,
    )
    Scrapy(
        bug_id=21,
        buggy_commit_id="43a53aca1207a82b663fe7a90c375546ce340a8e",
        fixed_commit_id="a8a6f050e71fbb7881076a8d6e2867e868d26016",
        test_files=[Path("tests", "test_downloadermiddleware_robotstxt.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloadermiddleware_robotstxt.py::RobotsTxtMiddlewareTest::test_robotstxt_immediate_error",
            )
        ],
        loc=11861,
    )
    Scrapy(
        bug_id=22,
        buggy_commit_id="a35aec71e96b0c0288c370afa425e8e700dca8b3",
        fixed_commit_id="bb2cf7c0d7199fffe0aa100e5c8a51c6b4b82fc2",
        test_files=[Path("tests", "test_exporters.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_exporters.py::XmlItemExporterTest::test_nonstring_types_item",
            )
        ],
        relevant_test_files=[
            os.path.join("tests", "test_exporters.py::XmlItemExporterTest")
        ],
        loc=11845,
    )
    Scrapy(
        bug_id=23,
        buggy_commit_id="c9e046d11dc63fbdc40effce4e6d15bcecd44593",
        fixed_commit_id="f042ad0f39594d59a1a2032e6294ff1890638138",
        test_files=[Path("tests", "test_downloadermiddleware_httpproxy.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloadermiddleware_httpproxy.py::TestDefaultHeadersMiddleware::test_proxy_auth",
            ),
            os.path.join(
                "tests",
                "test_downloadermiddleware_httpproxy.py::TestDefaultHeadersMiddleware::test_proxy_auth_empty_passwd",
            ),
        ],
        loc=11770,
    )
    Scrapy(
        bug_id=24,
        buggy_commit_id="98c060d0b2cc76934e16abc03a033f21850fd565",
        fixed_commit_id="0f527849f2e8eddaf5d756b061699f2eca522a18",
        test_files=[Path("tests", "test_downloader_handlers.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloader_handlers.py::HttpProxyTestCase::test_download_with_proxy_https_timeout",
            )
        ],
        relevant_test_files=[
            os.path.join("tests", "test_downloader_handlers.py::HttpProxyTestCase")
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=11841,
    )
    Scrapy(
        bug_id=25,
        buggy_commit_id="57f87b95d4d705f8afdd8fb9f7551033a7d88ee2",
        fixed_commit_id="9548691fdd47077a53f85daace091ef4af599cb9",
        test_files=[Path("tests", "test_http_request.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_http_request.py::FormRequestTest::test_html_base_form_action",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "tests",
                "test_http_request.py::FormRequestTest",
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=11814,
    )
    Scrapy(
        bug_id=26,
        buggy_commit_id="f249b309ab779b5ab518f54f309d7a4ac6661ec7",
        fixed_commit_id="03f1720afb4a437314659a306286f440df664a0b",
        test_files=[Path("tests", "test_settings", "__init__.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_settings",
                "__init__.py::BaseSettingsTest::test_getcomposite",
            )
        ],
        loc=11794,
    )
    Scrapy(
        bug_id=27,
        buggy_commit_id="280eab241680c93a763a3ef3a9ccd0c257259ca0",
        fixed_commit_id="d164398a27736f75286cc435eca69b06ff7c1c06",
        test_files=[Path("tests", "test_downloadermiddleware_redirect.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloadermiddleware_redirect.py::RedirectMiddlewareTest::test_request_meta_handling",
            )
        ],
        skip_tests=[
            "test_max_redirect_times",
            "test_priority_adjust",
            "test_redirect_301",
            "test_redirect_302",
            "test_redirect_302_head",
            "test_redirect_urls",
            "test_ttl",
            "MetaRefreshMiddlewareTest",
        ],
        loc=11599,
    )
    Scrapy(
        bug_id=28,
        buggy_commit_id="e2f31f3018c0037f65982209c22f93b80a5d6e7b",
        fixed_commit_id="457b97c13ccf9a84f3dc7800c180cf059822c09a",
        test_files=[Path("tests", "test_dupefilters.py")],
        test_cases=[
            os.path.join(
                "tests", "test_dupefilters.py::RFPDupeFilterTest::test_dupefilter_path"
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=11737,
    )
    Scrapy(
        bug_id=29,
        buggy_commit_id="5c4666a3d489bd3efa2e188de58721a125a5bfad",
        fixed_commit_id="8d45b3c4810cb5304ba1193b45697a0df1157326",
        test_files=[Path("tests", "test_utils_request.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils_request.py::UtilsRequestTest::test_request_httprepr_for_non_http_request",
            )
        ],
        api=Scrapy29API(),
        unittests=Scrapy29UnittestGenerator(),
        systemtests=Scrapy29SystemtestGenerator(),
        grammar=grammar_b64,
        loc=11711,
    )
    Scrapy(
        bug_id=30,
        buggy_commit_id="4d41cc0dc4821da07d467b368528c61ce48a0df2",
        fixed_commit_id="3e6d6c43ac0763adf2cd92efdb4a1dc2ba165440",
        test_files=[
            Path("tests", "test_command_version.py"),
            Path("tests", "test_toplevel.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_command_version.py::VersionTest::test_output")
        ],
        loc=11700,
    )
    Scrapy(
        bug_id=31,
        buggy_commit_id="5f02ef82e8560242eb34b336f385addfdef3211d",
        fixed_commit_id="dba7e39f61cbe2c22d3c9064f32f6e36d74f14b2",
        test_files=[
            Path("tests", "test_downloadermiddleware_cookies.py"),
        ],
        test_cases=[
            os.path.join(
                "tests",
                "test_downloadermiddleware_cookies.py::CookiesMiddlewareTest::test_do_not_break_on_non_utf8_header",
            )
        ],
        loc=11681,
    )
    Scrapy(
        bug_id=32,
        buggy_commit_id="342cb622f1ea93268477da557099010bbd72529a",
        fixed_commit_id="aa6a72707daabfb6217f52e4774f2ff038f83dcc",
        test_files=[Path("tests", "test_crawler.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_crawler.py::CrawlerProcessTest::test_crawler_process_accepts_dict",
            )
        ],
        skip_tests=["test_spider_manager_verify_interface"],
        loc=11870,
    )
    Scrapy(
        bug_id=33,
        buggy_commit_id="2d216771976cd7aedfb88ae97418c2d4dcc84917",
        fixed_commit_id="6dccb3a9b320a8d0808764ac8e6e88e663e2d52c",
        test_files=[
            Path("tests", "test_pipeline_media.py"),
            Path("tests", "test_utils_log.py"),
            Path("scrapy", "utils", "log.py"),
        ],
        test_cases=[
            os.path.join(
                "tests",
                "test_pipeline_media.py::BaseMediaPipelineTestCase::test_default_item_completed",
            ),
        ],
        relevant_test_files=[
            Path("tests", "test_pipeline_media.py"),
            Path("tests", "test_utils_log.py"),
        ],
        skip_tests=["(MediaPipelineTestCase and not BaseMediaPipelineTestCase)"],
        loc=11839,
    )
    Scrapy(
        bug_id=34,
        buggy_commit_id="e521740b3951bacc80d3c9c1db8652ed5e914b89",
        fixed_commit_id="773ea5a5ef76426dd91a8669542d2602082a5746",
        test_files=[Path("tests", "test_item.py")],
        test_cases=[
            os.path.join(
                "tests", "test_item.py::ItemTest::test_metaclass_with_fields_attribute"
            ),
            os.path.join(
                "tests",
                "test_item.py::ItemTest::test_metaclass_multiple_inheritance_simple",
            ),
            os.path.join(
                "tests",
                "test_item.py::ItemTest::test_metaclass_multiple_inheritance_diamond",
            ),
        ],
        loc=11834,
    )
    Scrapy(
        bug_id=35,
        buggy_commit_id="0a5bbbaed3e182d2151b6b34357667901ece353f",
        fixed_commit_id="c3d3a9491412d2a91b0927a05908593dcd329e4a",
        test_files=[Path("tests", "test_crawler.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_crawler.py::CrawlerRunnerTestCase::test_spidermanager_deprecation",
            )
        ],
        skip_tests=["test_spider_manager_verify_interface"],
        loc=11359,
    )
    Scrapy(
        bug_id=36,
        buggy_commit_id="cb8140a42a27ede87b0880372024f2f1804618b8",
        fixed_commit_id="cf9be5344a89dd8e14f8241ec69de9c984ec1e05",
        test_files=[Path("tests", "test_utils_misc", "__init__.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_utils_misc",
                "__init__.py::UtilsMiscTestCase::test_create_instance",
            )
        ],
        loc=11664,
    )
    Scrapy(
        bug_id=37,
        buggy_commit_id="1d5c270ce8caf954ce83c8db262e2a35707e0c5e",
        fixed_commit_id="f701f5b0db10faef08e4ed9a21b98fd72f9cfc9a",
        test_files=[Path("tests", "test_http_request.py")],
        test_cases=[
            os.path.join(
                "tests", "test_http_request.py::RequestTest::test_url_no_scheme"
            ),
            os.path.join(
                "tests", "test_http_request.py::FormRequestTest::test_url_no_scheme"
            ),
            os.path.join(
                "tests", "test_http_request.py::XmlRpcRequestTest::test_url_no_scheme"
            ),
            os.path.join(
                "tests", "test_http_request.py::JsonRequestTest::test_url_no_scheme"
            ),
        ],
        skip_tests=["not test_url"],
        loc=11356,
    )
    Scrapy(
        bug_id=38,
        buggy_commit_id="6cc6bbb5fc5c102271829a554772effb0444023c",
        fixed_commit_id="6c3970e6722191b642fd99c6c1bfed0d93010cab",
        test_files=[Path("tests", "test_http_request.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_http_request.py::FormRequestTest::test_from_response_clickdata_does_not_ignore_image",
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=11286,
    )
    Scrapy(
        bug_id=39,
        buggy_commit_id="692975acb40c6394424dfb728b1ffa46b3b3c55d",
        fixed_commit_id="a1e8a8525d2312842c7e1cca8ba6e4e1a83084b7",
        test_files=[Path("tests", "test_spider.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_spider.py::DeprecationTest::test_make_requests_from_url_deprecated",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "tests",
                "test_spider.py::DeprecationTest",
            )
        ],
        loc=10639,
    )
    Scrapy(
        bug_id=40,
        buggy_commit_id="7d24df37380cd5a5b7394cd2534e240bd2eff0ca",
        fixed_commit_id="f1d971a5c0cdfe0f4fe5619146cd6818324fc98e",
        test_files=[Path("tests", "test_exporters.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_exporters.py::PythonItemExporterTest::test_other_python_types_item",
            )
        ],
        api=Scrapy40API(),
        unittests=Scrapy40UnittestGenerator(),
        systemtests=Scrapy40SystemtestGenerator(),
        grammar=grammar_b64,
        loc=11837,
    )


class ScrapyAPI(API):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# Shared helpers
# ======================================================================
def _rand_word(a: int = 3, b: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=random.randint(a, b)))


def _b64(s) -> str:
    if isinstance(s, str):
        s = s.encode("utf-8")
    return base64.urlsafe_b64encode(s).decode("ascii")


def _b64d(s: str) -> bytes:
    return base64.urlsafe_b64decode(s.encode("ascii"))


# Grammar for a single urlsafe-base64 token payload.
grammar_b64: Grammar = clean_up(
    {
        "<start>": ["<char><chars>"],
        "<chars>": ["", "<char><chars>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_b64)


# ======================================================================
# bug_2: ``LocalCache.__setitem__`` executed ``while len(self) >= self.limit``
# unconditionally, so a cache created without a limit (``self.limit is None``)
# raised ``TypeError: '>=' not supported between instances of 'int' and
# 'NoneType'`` on the first insertion.  The fix guards the eviction loop with
# ``if self.limit is not None``.
#
# System-test format: ``<limit> <n>`` where ``<limit>`` is ``none`` or a
# positive integer and ``<n>`` is the number of ``str(i) -> i`` items inserted.
# The harness prints ``repr((len(cache), list(cache.items())))``; the oracle
# recomputes the correct (fixed) OrderedDict-eviction result.  A failing test
# uses ``none`` (buggy: TypeError; fixed: all items kept); a passing test uses
# an integer limit (identical on both builds).
# ======================================================================


def _local_cache_expected(limit: Optional[int], n: int) -> Tuple[int, list]:
    d: "OrderedDict[str, int]" = OrderedDict()
    for i in range(n):
        if limit is not None:
            while len(d) >= limit:
                d.popitem(last=False)
        d[str(i)] = i
    return len(d), list(d.items())


class Scrapy2API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            limit_arg = process.args[2]
            n = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        limit = None if limit_arg == "none" else int(limit_arg)
        expected = repr(_local_cache_expected(limit, n))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Scrapy2TestGenerator:
    @staticmethod
    def _failing_params() -> int:
        # no limit -> triggers the fault on the buggy build
        return random.randint(5, 400)

    @staticmethod
    def _passing_params() -> Tuple[int, int]:
        limit = random.randint(2, 60)
        n = random.randint(1, 400)
        return limit, n


class Scrapy2SystemtestGenerator(SystemtestGenerator, Scrapy2TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        n = self._failing_params()
        return f"none {n}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        limit, n = self._passing_params()
        return f"{limit} {n}", TestResult.PASSING


class Scrapy2UnittestGenerator(UnittestGenerator, Scrapy2TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.utils.datatypes",
                names=[ast.alias(name="LocalCache")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = self._failing_params()
        length, items = _local_cache_expected(None, n)
        last_key, last_val = items[-1]
        src = (
            "cache = LocalCache()\n"
            f"for i in range({n}):\n"
            "    cache[str(i)] = i\n"
            f"self.assertEqual({length}, len(cache))\n"
            f"self.assertEqual({last_val!r}, cache[{last_key!r}])\n"
        )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        limit, n = self._passing_params()
        length, items = _local_cache_expected(limit, n)
        last_key, last_val = items[-1]
        src = (
            f"cache = LocalCache(limit={limit})\n"
            f"for i in range({n}):\n"
            "    cache[str(i)] = i\n"
            f"self.assertEqual({length}, len(cache))\n"
            f"self.assertEqual({last_val!r}, cache[{last_key!r}])\n"
        )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_local_cache: Grammar = clean_up(
    {
        "<start>": ["<limit> <n>"],
        "<limit>": ["none", "<int>"],
        "<n>": ["<int>"],
        "<int>": ["<nonzero><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<nonzero>": srange("123456789"),
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_local_cache)


# ======================================================================
# bug_17: ``response_status_message`` looked up the reason phrase with
# ``http.RESPONSES.get(int(status))`` WITHOUT a default, so an unknown status
# code (not in twisted's ``RESPONSES``) yielded ``None`` and
# ``to_native_str(None)`` raised ``TypeError``.  The fix supplies the
# ``"Unknown Status"`` default, so an unknown code returns
# ``"<code> Unknown Status"``.
#
# System-test format: a single integer ``<status>``.  The harness prints
# ``response_status_message(status)``; the oracle recomputes the correct
# string.  A failing test uses an unknown code (buggy: TypeError; fixed:
# ``"<code> Unknown Status"``); a passing test uses a known code (identical on
# both builds).
# ======================================================================

# Exact reason phrases (twisted.web.http.RESPONSES) for known codes used as
# passing inputs.
_STATUS_REASONS = {
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    206: "Partial Content",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    307: "Temporary Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    408: "Request Time-out",
    409: "Conflict",
    410: "Gone",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Time-out",
    505: "HTTP Version not supported",
}

# Every code twisted knows about; failing (unknown) codes must avoid these.
_KNOWN_TWISTED_CODES = {
    100, 101, 200, 201, 202, 203, 204, 205, 206, 207, 300, 301, 302, 303, 304,
    305, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411,
    412, 413, 414, 415, 416, 417, 500, 501, 502, 503, 504, 505, 507, 510,
}


def _status_message_expected(code: int) -> str:
    if code in _STATUS_REASONS:
        return f"{code} {_STATUS_REASONS[code]}"
    return f"{code} Unknown Status"


class Scrapy17API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            code = int(process.args[2])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _status_message_expected(code)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy17TestGenerator:
    _KNOWN_CODES = sorted(_STATUS_REASONS)

    @staticmethod
    def _unknown_code() -> int:
        while True:
            code = random.randint(210, 599)
            if code not in _KNOWN_TWISTED_CODES:
                return code

    def _known_code(self) -> int:
        return random.choice(self._KNOWN_CODES)


class Scrapy17SystemtestGenerator(SystemtestGenerator, Scrapy17TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"{self._unknown_code()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"{self._known_code()}", TestResult.PASSING


class Scrapy17UnittestGenerator(UnittestGenerator, Scrapy17TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.utils.response",
                names=[ast.alias(name="response_status_message")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(codes: List[int]) -> List[ast.stmt]:
        src = "".join(
            f"self.assertEqual({_status_message_expected(c)!r}, "
            f"response_status_message({c}))\n"
            for c in codes
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        codes = random.sample(
            [c for c in range(210, 600) if c not in _KNOWN_TWISTED_CODES], 3
        )
        test = self.get_empty_test()
        test.body = self._assert(codes)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        codes = random.sample(self._KNOWN_CODES, 3)
        test = self.get_empty_test()
        test.body = self._assert(codes)
        return test, TestResult.PASSING


grammar_status: Grammar = clean_up(
    {
        "<start>": ["<nonzero><digit><digit>"],
        "<nonzero>": srange("123456789"),
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_status)


# ======================================================================
# bug_29: ``request_httprepr`` built the ``Host:`` line with
# ``to_bytes(parsed.hostname)``.  For a request whose URL has no authority
# (e.g. ``file:///tmp/foo.txt``) ``parsed.hostname`` is ``None`` and
# ``to_bytes(None)`` raised ``TypeError``.  The fix uses
# ``to_bytes(parsed.hostname or b'')`` so a host-less request yields an empty
# ``Host:`` value instead of crashing.
#
# System-test format: a single urlsafe-base64 token of the request URL.  The
# harness prints ``OK:<b64 httprepr>`` (or ``ERR:<type>``); the oracle
# recomputes the correct raw HTTP representation.  A failing test uses a
# host-less URL (buggy: TypeError; fixed: valid repr with empty Host); a
# passing test uses a URL with a host (identical on both builds).
# ======================================================================


def _request_httprepr_expected(url: str) -> bytes:
    from urllib.parse import urlparse, urlunparse

    parsed = urlparse(url)
    path = urlunparse(("", "", parsed.path or "/", parsed.params, parsed.query, ""))
    host = parsed.hostname or ""
    return (
        b"GET " + path.encode("utf-8") + b" HTTP/1.1\r\n"
        b"Host: " + host.encode("utf-8") + b"\r\n\r\n"
    )


class Scrapy29API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            url = _b64d(process.args[2]).decode("utf-8")
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _request_httprepr_expected(url)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out.startswith("OK:"):
            try:
                got = _b64d(out[3:])
            except Exception:
                return TestResult.FAILING, f"Malformed output: {out!r}"
            if got == expected:
                return TestResult.PASSING, f"Expected {expected!r}"
            return TestResult.FAILING, f"Expected {expected!r}, but was {got!r}"
        return TestResult.FAILING, f"request_httprepr failed: {out!r}"


class Scrapy29TestGenerator:
    _SCHEMES = ["http", "https", "ftp"]

    def _host_url(self) -> str:
        scheme = random.choice(self._SCHEMES)
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net', 'io'])}"
        path = "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
        if random.random() < 0.5:
            path += f"?{_rand_word(1, 4)}={random.randint(1, 999)}"
        return f"{scheme}://{host}{path}"

    def _hostless_url(self) -> str:
        path = "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
        if random.random() < 0.4:
            path += f".{random.choice(['txt', 'dat', 'log', 'json'])}"
        return f"file://{path}"


class Scrapy29SystemtestGenerator(SystemtestGenerator, Scrapy29TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._hostless_url()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._host_url()), TestResult.PASSING


class Scrapy29UnittestGenerator(UnittestGenerator, Scrapy29TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http", names=[ast.alias(name="Request")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.utils.request",
                names=[ast.alias(name="request_httprepr")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(url: str) -> List[ast.stmt]:
        expected = _request_httprepr_expected(url)
        src = (
            f"self.assertEqual({expected!r}, "
            f"request_httprepr(Request({url!r})))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._hostless_url())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._host_url())
        return test, TestResult.PASSING


# ======================================================================
# bug_40: ``PythonItemExporter._serialize_value`` unconditionally passed every
# scalar value through ``to_bytes``/``to_unicode``, turning non-string values
# (``int``, ``float``, ``bool``, ...) into their string representations (e.g.
# ``22 -> '22'``, ``False -> 'False'``).  The fix only encodes values that are
# already ``str``/``bytes`` and otherwise returns the value unchanged, so
# native Python types survive export.
#
# System-test format: a single urlsafe-base64 token of a Python ``dict``
# literal (values restricted to ``int``/``float``/``bool``/``str``).  The
# harness prints ``OK:<b64 repr(exported)>``; the oracle recomputes the correct
# (fixed) result -- which equals the input item, because fixed export preserves
# non-strings and returns strings unchanged.  A failing test contains at least
# one non-string value (buggy: stringified -> mismatch); a passing test uses
# only string values (identical on both builds).
# ======================================================================


def _python_exporter_expected(item: dict) -> dict:
    # Fixed PythonItemExporter preserves int/float/bool and returns str
    # unchanged, so the correct exported dict equals the input item.
    return dict(item)


class Scrapy40API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            spec = _b64d(process.args[2]).decode("utf-8")
            item = ast.literal_eval(spec)
            assert isinstance(item, dict)
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _python_exporter_expected(item)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out.startswith("OK:"):
            try:
                got = ast.literal_eval(_b64d(out[3:]).decode("utf-8"))
            except Exception:
                return TestResult.FAILING, f"Malformed output: {out!r}"
            if got == expected:
                return TestResult.PASSING, f"Expected {expected!r}"
            return TestResult.FAILING, f"Expected {expected!r}, but was {got!r}"
        return TestResult.FAILING, f"export_item failed: {out!r}"


class Scrapy40TestGenerator:
    @staticmethod
    def _scalar() -> Any:
        kind = random.choice(["int", "float", "bool"])
        if kind == "int":
            return random.randint(-999, 999)
        if kind == "float":
            return round(random.uniform(-99, 99), 3)
        return random.choice([True, False])

    def _failing_item(self) -> dict:
        n = random.randint(2, 4)
        keys = random.sample(
            ["boolean", "number", "count", "ratio", "flag", "amount", "level"], n
        )
        item = {k: self._scalar() for k in keys}
        # guarantee at least one non-string value (all scalars already are)
        return item

    def _passing_item(self) -> dict:
        n = random.randint(2, 4)
        keys = random.sample(
            ["name", "title", "label", "kind", "code", "tag", "slug"], n
        )
        return {k: _rand_word(3, 8) for k in keys}


class Scrapy40SystemtestGenerator(SystemtestGenerator, Scrapy40TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(repr(self._failing_item())), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(repr(self._passing_item())), TestResult.PASSING


class Scrapy40UnittestGenerator(UnittestGenerator, Scrapy40TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.exporters",
                names=[ast.alias(name="PythonItemExporter")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(item: dict) -> List[ast.stmt]:
        expected = _python_exporter_expected(item)
        src = (
            f"ie = PythonItemExporter(binary=False)\n"
            f"exported = ie.export_item({item!r})\n"
            f"self.assertEqual({expected!r}, exported)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._failing_item())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._passing_item())
        return test, TestResult.PASSING


# ======================================================================
# bug_18: ``ResponseTypes.from_content_disposition`` decoded the raw
# ``Content-Disposition`` bytes with ``to_native_str(content_disposition)``
# (UTF-8).  A header carrying a non-UTF-8 filename (e.g. latin-1 bytes) raised
# ``UnicodeDecodeError`` -- which is not the ``IndexError`` the method catches,
# so it propagated.  The fix decodes with ``encoding='latin-1',
# errors='replace'`` so any byte string is handled and the correct Response
# subclass is returned.
#
# System-test format: a single urlsafe-base64 token of the raw
# ``Content-Disposition`` bytes.  The harness prints ``OK:<ResponseClass>`` or
# ``ERR:<exc>``; the oracle recomputes the correct class from the filename
# extension (the fixed behaviour).  A failing test carries a non-UTF-8 filename
# (buggy: UnicodeDecodeError; fixed: correct class); a passing test carries an
# ASCII filename (identical on both builds).
# ======================================================================

# Filename extensions whose scrapy Response class is deterministic.
_CD_EXT_CLASS = {".html": "HtmlResponse", ".xml": "XmlResponse", ".txt": "TextResponse"}


def _content_disposition_expected(cd_bytes: bytes) -> str:
    # Mirror the fixed ``from_content_disposition``: latin-1/replace decode,
    # split out the filename, map its extension to the Response class.
    s = cd_bytes.decode("latin-1", "replace")
    try:
        filename = s.split(";")[1].split("=")[1].strip("\"'")
    except IndexError:
        return "Response"
    ext = os.path.splitext(filename)[1].lower()
    return _CD_EXT_CLASS.get(ext, "Response")


class Scrapy18API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            cd_bytes = _b64d(process.args[2])
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _content_disposition_expected(cd_bytes)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == f"OK:{expected}":
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected OK:{expected}, but was {out!r}"


class Scrapy18TestGenerator:
    _EXTS = [".html", ".xml", ".txt", ""]
    _NONASCII = "éñüößàµ£"

    def _failing_cd(self) -> bytes:
        ext = random.choice(self._EXTS)
        stem = _rand_word(3, 7) + random.choice(self._NONASCII) + _rand_word(0, 3)
        return ("attachment; filename=" + stem + ext).encode("latin-1")

    def _passing_cd(self) -> bytes:
        ext = random.choice(self._EXTS)
        stem = _rand_word(3, 8)
        quote = random.choice(["", '"'])
        return (f"attachment; filename={quote}{stem}{ext}{quote}").encode("ascii")


class Scrapy18SystemtestGenerator(SystemtestGenerator, Scrapy18TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._failing_cd()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._passing_cd()), TestResult.PASSING


class Scrapy18UnittestGenerator(UnittestGenerator, Scrapy18TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.responsetypes",
                names=[ast.alias(name="responsetypes")],
                level=0,
            ),
            ast.Import(names=[ast.alias(name="scrapy.http")]),
        ]

    @staticmethod
    def _assert(cd_bytes: bytes) -> List[ast.stmt]:
        expected = _content_disposition_expected(cd_bytes)
        src = (
            f"self.assertIs(scrapy.http.{expected}, "
            f"responsetypes.from_content_disposition({cd_bytes!r}))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._failing_cd())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._passing_cd())
        return test, TestResult.PASSING


# ======================================================================
# bug_15: ``_safe_ParseResult`` (used by ``canonicalize_url``) built the netloc
# with ``parts.netloc.encode('idna')``.  IDNA encoding raises ``UnicodeError``
# for a missing DNS label (e.g. ``http://.example.com``) or a label longer than
# 63 characters.  ``canonicalize_url`` only caught ``UnicodeEncodeError`` (not
# the plain ``UnicodeError`` idna raises), so such URLs crashed.  The fix wraps
# the idna encoding in ``try/except UnicodeError`` and keeps the raw netloc.
#
# System-test format: a single urlsafe-base64 token of a URL restricted to a
# lowercase-ASCII host and a non-empty lowercase-ASCII path (no query/fragment),
# so canonicalization is the identity.  The harness prints ``OK:<canonical>`` or
# ``ERR:<exc>``; the oracle expects ``OK:<url>``.  A failing test uses a URL
# with a missing/too-long DNS label (buggy: UnicodeError; fixed: url unchanged);
# a passing test uses a normal host (identical on both builds).
# ======================================================================


class Scrapy15API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            url = _b64d(process.args[2]).decode("utf-8")
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        # These URLs are already canonical, so the correct output is the URL.
        expected = f"OK:{url}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy15TestGenerator:
    def _path(self) -> str:
        return "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))

    def _passing_url(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net', 'io'])}"
        return f"http://{host}{self._path()}"

    def _failing_url(self) -> str:
        if random.random() < 0.5:
            # missing leading DNS label
            host = f".{_rand_word(3, 8)}.com"
        else:
            # single DNS label longer than 63 characters (idna limit)
            label = "".join(
                random.choices(string.ascii_lowercase, k=random.randint(64, 90))
            )
            host = f"www.{label}.com"
        return f"http://{host}{self._path()}"


class Scrapy15SystemtestGenerator(SystemtestGenerator, Scrapy15TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._failing_url()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._passing_url()), TestResult.PASSING


class Scrapy15UnittestGenerator(UnittestGenerator, Scrapy15TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.utils.url",
                names=[ast.alias(name="canonicalize_url")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(url: str) -> List[ast.stmt]:
        src = f"self.assertEqual({url!r}, canonicalize_url({url!r}))\n"
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._failing_url())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._passing_url())
        return test, TestResult.PASSING


# ======================================================================
# bug_19: ``WrappedRequest`` (adapter used by the cookie middleware) exposed the
# request via ``get_full_url()``/``get_host()``/``get_type()``/
# ``get_origin_req_host()`` methods only.  Python 3's ``http.cookiejar`` expects
# the *attributes* ``full_url``/``host``/``type``/``origin_req_host``, which the
# buggy version did not provide (accessing them raised ``AttributeError``).  The
# fix adds those four properties.
#
# System-test format: ``<attr> <b64url>`` where ``<attr>`` is one of the four
# new properties (failing) or the four always-present ``get_*`` methods
# (passing).  The harness reads the attribute (calling it if it is a method) and
# prints ``OK:<value>`` or ``ERR:<exc>``; the oracle recomputes the correct
# value from the URL.  A failing test reads a property (buggy: AttributeError;
# fixed: correct value); a passing test calls a method (identical on both).
# ======================================================================

_WRAPPED_PROPS = ["full_url", "host", "type", "origin_req_host"]
_WRAPPED_METHODS = ["get_full_url", "get_host", "get_type", "get_origin_req_host"]


def _wrapped_request_expected(attr: str, url: str) -> str:
    from urllib.parse import urlparse

    parsed = urlparse(url)
    if attr in ("full_url", "get_full_url"):
        return url
    if attr in ("host", "get_host"):
        return parsed.netloc
    if attr in ("type", "get_type"):
        return parsed.scheme
    return parsed.hostname or ""


class Scrapy19API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            attr = process.args[2]
            url = _b64d(process.args[3]).decode("utf-8")
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = f"OK:{_wrapped_request_expected(attr, url)}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy19TestGenerator:
    def _url(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net', 'io'])}"
        path = "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
        return f"http://{host}{path}"


class Scrapy19SystemtestGenerator(SystemtestGenerator, Scrapy19TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        attr = random.choice(_WRAPPED_PROPS)
        return f"{attr} {_b64(self._url())}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        attr = random.choice(_WRAPPED_METHODS)
        return f"{attr} {_b64(self._url())}", TestResult.PASSING


class Scrapy19UnittestGenerator(UnittestGenerator, Scrapy19TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http", names=[ast.alias(name="Request")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.http.cookies",
                names=[ast.alias(name="WrappedRequest")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(attr: str, url: str) -> List[ast.stmt]:
        expected = _wrapped_request_expected(attr, url)
        if attr in _WRAPPED_METHODS:
            access = f"WrappedRequest(Request({url!r})).{attr}()"
        else:
            access = f"WrappedRequest(Request({url!r})).{attr}"
        src = f"self.assertEqual({expected!r}, {access})\n"
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(random.choice(_WRAPPED_PROPS), self._url())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(random.choice(_WRAPPED_METHODS), self._url())
        return test, TestResult.PASSING


grammar_wrapped_request: Grammar = clean_up(
    {
        "<start>": ["<attr> <b64>"],
        "<attr>": _WRAPPED_PROPS + _WRAPPED_METHODS,
        "<b64>": ["<char><b64>", "<char>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_wrapped_request)


# ======================================================================
# bug_7: ``FormRequest.from_response`` resolved a form's target with
# ``_get_form_url``, which did ``urljoin(form.base_url, form.action)`` without
# trimming the ``action`` value.  An ``action`` with leading/trailing HTML5
# whitespace (e.g. ``" path "``) therefore leaked the spaces into the request
# URL.  The fix applies ``strip_html5_whitespace(action)`` before joining.
#
# System-test format: ``<b64 base-url> <b64 action>``.  The harness builds an
# ``HtmlResponse`` with a ``<form>`` carrying that action, runs
# ``FormRequest.from_response`` and prints ``OK:<req.url>``; the oracle
# recomputes ``urljoin(base, strip_html5_whitespace(action))``.  A failing test
# uses an action padded with spaces (buggy: spaces leak into the URL; fixed:
# stripped); a passing test uses a clean action (identical on both builds).
# ======================================================================

_HTML5_WS = " \t\n\r\x0c"


def _form_url_expected(base_url: str, action: str) -> str:
    from urllib.parse import urljoin

    return urljoin(base_url, action.strip(_HTML5_WS))


class Scrapy7API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            base_url = _b64d(process.args[2]).decode("utf-8")
            action = _b64d(process.args[3]).decode("utf-8")
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = f"OK:{_form_url_expected(base_url, action)}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy7TestGenerator:
    def _base_url(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net', 'io'])}"
        return f"http://{host}"

    def _core(self) -> str:
        return "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))

    def _padded(self, core: str) -> str:
        lead = " " * random.randint(1, 2)
        trail = " " * random.randint(1, 2)
        return f"{lead}{core}{trail}"


class Scrapy7SystemtestGenerator(SystemtestGenerator, Scrapy7TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        base = self._base_url()
        action = self._padded(self._core())
        return f"{_b64(base)} {_b64(action)}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        base = self._base_url()
        action = self._core()
        return f"{_b64(base)} {_b64(action)}", TestResult.PASSING


class Scrapy7UnittestGenerator(UnittestGenerator, Scrapy7TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="HtmlResponse"), ast.alias(name="FormRequest")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(base_url: str, action: str) -> List[ast.stmt]:
        expected = _form_url_expected(base_url, action)
        body = f'<html><body><form action="{action}"></form></body></html>'
        src = (
            f"response = HtmlResponse(url={base_url!r}, "
            f"body={body!r}.encode('utf-8'), encoding='utf-8')\n"
            f"request = FormRequest.from_response(response)\n"
            f"self.assertEqual({expected!r}, request.url)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._base_url(), self._padded(self._core()))
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._base_url(), self._core())
        return test, TestResult.PASSING


grammar_form_action: Grammar = clean_up(
    {
        "<start>": ["<b64> <b64>"],
        "<b64>": ["<char><b64>", "<char>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_form_action)


# ======================================================================
# bug_5: ``Response.follow`` passed ``url`` straight to ``self.urljoin(url)``.
# For ``url=None`` ``urljoin`` silently returns the base URL, so
# ``response.follow(None)`` produced a request pointing at the response's own
# URL instead of failing.  The fix raises ``ValueError("url can't be None")``
# when ``url is None``.
#
# System-test format: ``<mode> <b64 base> <b64 target>`` where ``<mode>`` is
# ``none`` (target ignored, ``follow(None)``) or ``url`` (follow an absolute
# target).  The harness prints ``OK:<req.url>`` or ``ERR:<exc>``; the oracle
# expects ``ERR:ValueError`` for ``none`` and ``OK:<joined>`` for ``url``.  A
# failing test uses ``none`` (buggy: returns a request; fixed: ValueError); a
# passing test uses ``url`` (identical on both builds).
# ======================================================================


class Scrapy5API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            base = _b64d(process.args[3]).decode("utf-8")
            if mode == "none":
                expected = "ERR:ValueError"
            else:
                from urllib.parse import urljoin

                target = _b64d(process.args[4]).decode("utf-8")
                expected = "OK:" + urljoin(base, target)
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy5TestGenerator:
    def _base(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net', 'io'])}"
        return f"http://{host}"

    def _target(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net', 'io'])}"
        path = "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
        return f"http://{host}{path}"


class Scrapy5SystemtestGenerator(SystemtestGenerator, Scrapy5TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"none {_b64(self._base())} {_b64('x')}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"url {_b64(self._base())} {_b64(self._target())}",
            TestResult.PASSING,
        )


class Scrapy5UnittestGenerator(UnittestGenerator, Scrapy5TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http", names=[ast.alias(name="Response")], level=0
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        base = self._base()
        src = (
            f"response = Response(url={base!r})\n"
            f"self.assertRaises(ValueError, response.follow, None)\n"
        )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        from urllib.parse import urljoin

        base = self._base()
        target = self._target()
        expected = urljoin(base, target)
        src = (
            f"response = Response(url={base!r})\n"
            f"self.assertEqual({expected!r}, response.follow({target!r}).url)\n"
        )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_follow: Grammar = clean_up(
    {
        "<start>": ["<mode> <b64> <b64>"],
        "<mode>": ["none", "url"],
        "<b64>": ["<char><b64>", "<char>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_follow)
