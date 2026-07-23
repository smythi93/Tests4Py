import ast
import base64
import os.path
import random
import re
import string
import subprocess
from collections import OrderedDict
from pathlib import Path
from typing import Any, List, Optional, Tuple
from urllib.parse import urljoin

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
        api=Scrapy1API(),
        unittests=Scrapy1UnittestGenerator(),
        systemtests=Scrapy1SystemtestGenerator(),
        grammar=grammar_offsite,
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
        api=Scrapy3API(),
        unittests=Scrapy3UnittestGenerator(),
        systemtests=Scrapy3SystemtestGenerator(),
        grammar=grammar_redirect_location,
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
        api=Scrapy4API(),
        unittests=Scrapy4UnittestGenerator(),
        systemtests=Scrapy4SystemtestGenerator(),
        grammar=grammar_contracts,
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
        api=Scrapy6API(),
        unittests=Scrapy6UnittestGenerator(),
        systemtests=Scrapy6SystemtestGenerator(),
        grammar=grammar_printable,
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
        api=Scrapy8API(),
        unittests=Scrapy8UnittestGenerator(),
        systemtests=Scrapy8SystemtestGenerator(),
        grammar=grammar_classcell,
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
        api=Scrapy9API(),
        unittests=Scrapy9UnittestGenerator(),
        systemtests=Scrapy9SystemtestGenerator(),
        grammar=grammar_mail,
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
        api=Scrapy10API(),
        unittests=Scrapy10UnittestGenerator(),
        systemtests=Scrapy10SystemtestGenerator(),
        grammar=grammar_b64,
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
        api=Scrapy12API(),
        unittests=Scrapy12UnittestGenerator(),
        systemtests=Scrapy12SystemtestGenerator(),
        grammar=grammar_selector,
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
        api=Scrapy13API(),
        unittests=Scrapy13UnittestGenerator(),
        systemtests=Scrapy13SystemtestGenerator(),
        grammar=grammar_images_expires,
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
        api=Scrapy14API(),
        unittests=Scrapy14UnittestGenerator(),
        systemtests=Scrapy14SystemtestGenerator(),
        grammar=grammar_gzip,
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
        api=Scrapy16API(),
        unittests=Scrapy16UnittestGenerator(),
        systemtests=Scrapy16SystemtestGenerator(),
        grammar=grammar_canonicalize,
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
        api=Scrapy20API(),
        unittests=Scrapy20UnittestGenerator(),
        systemtests=Scrapy20SystemtestGenerator(),
        grammar=grammar_sitemap,
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
        api=Scrapy21API(),
        unittests=Scrapy21UnittestGenerator(),
        systemtests=Scrapy21SystemtestGenerator(),
        grammar=grammar_robotstxt,
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
        api=Scrapy22API(),
        unittests=Scrapy22UnittestGenerator(),
        systemtests=Scrapy22SystemtestGenerator(),
        grammar=grammar_b64,
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
        api=Scrapy23API(),
        unittests=Scrapy23UnittestGenerator(),
        systemtests=Scrapy23SystemtestGenerator(),
        grammar=grammar_b64,
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
        api=Scrapy24API(),
        unittests=Scrapy24UnittestGenerator(),
        systemtests=Scrapy24SystemtestGenerator(),
        grammar=grammar_tunneling,
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
        api=Scrapy25API(),
        unittests=Scrapy25UnittestGenerator(),
        systemtests=Scrapy25SystemtestGenerator(),
        grammar=grammar_printable,
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
        api=Scrapy26API(),
        unittests=Scrapy26UnittestGenerator(),
        systemtests=Scrapy26SystemtestGenerator(),
        grammar=grammar_composite,
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
        api=Scrapy27API(),
        unittests=Scrapy27UnittestGenerator(),
        systemtests=Scrapy27SystemtestGenerator(),
        grammar=grammar_redirect_meta,
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
        api=Scrapy28API(),
        unittests=Scrapy28UnittestGenerator(),
        systemtests=Scrapy28SystemtestGenerator(),
        grammar=grammar_dupefilter,
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
        api=Scrapy30API(),
        unittests=Scrapy30UnittestGenerator(),
        systemtests=Scrapy30SystemtestGenerator(),
        grammar=grammar_version,
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
        api=Scrapy31API(),
        unittests=Scrapy31UnittestGenerator(),
        systemtests=Scrapy31SystemtestGenerator(),
        grammar=grammar_b64,
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
        api=Scrapy32API(),
        unittests=Scrapy32UnittestGenerator(),
        systemtests=Scrapy32SystemtestGenerator(),
        grammar=grammar_crawler_dict,
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
        api=Scrapy33API(),
        unittests=Scrapy33UnittestGenerator(),
        systemtests=Scrapy33SystemtestGenerator(),
        grammar=grammar_media_log,
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
        api=Scrapy34API(),
        unittests=Scrapy34UnittestGenerator(),
        systemtests=Scrapy34SystemtestGenerator(),
        grammar=grammar_item_fields,
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
        api=Scrapy35API(),
        unittests=Scrapy35UnittestGenerator(),
        systemtests=Scrapy35SystemtestGenerator(),
        grammar=grammar_spider_loader,
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
        api=Scrapy36API(),
        unittests=Scrapy36UnittestGenerator(),
        systemtests=Scrapy36SystemtestGenerator(),
        grammar=grammar_create_instance,
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
        api=Scrapy37API(),
        unittests=Scrapy37UnittestGenerator(),
        systemtests=Scrapy37SystemtestGenerator(),
        grammar=grammar_request_scheme,
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
        api=Scrapy38API(),
        unittests=Scrapy38UnittestGenerator(),
        systemtests=Scrapy38SystemtestGenerator(),
        grammar=grammar_printable,
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
        api=Scrapy39API(),
        unittests=Scrapy39UnittestGenerator(),
        systemtests=Scrapy39SystemtestGenerator(),
        grammar=grammar_deprecation,
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
# bug_3: ``RedirectMiddleware.process_response`` resolved the ``Location`` header
# with ``urljoin(request.url, safe_url_string(location))``.  For a scheme-
# relative ``Location`` with extra leading slashes (e.g. ``///host/path``)
# ``urljoin`` produced a broken URL (empty/duplicated host).  The fix detects a
# ``//``-prefixed Location and rebuilds it as ``<request-scheme>://<location
# without leading slashes>``.
#
# System-test format: ``<mode> <b64 request-url> <b64 location>`` with ``<mode>``
# ``rel`` (a ``///host/path`` Location) or ``abs`` (an absolute ``http://``
# Location).  The harness runs the middleware and prints ``OK:<redirect url>`` or
# ``ERR:<exc>``; the oracle recomputes the correct redirect URL.  A failing test
# uses ``rel`` (buggy: broken URL; fixed: ``http://host/path``); a passing test
# uses ``abs`` (identical on both builds).
# ======================================================================


class Scrapy3API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            location = _b64d(process.args[4]).decode("utf-8")
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "rel":
            expected = "OK:http://" + location.lstrip("/")
        else:
            expected = "OK:" + location
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy3TestGenerator:
    def _request_url(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net'])}"
        return f"http://{host}/{_rand_word(2, 6)}"

    def _target(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net'])}"
        return f"{host}/{_rand_word(2, 6)}"

    def _rel_location(self) -> str:
        return "///" + self._target()

    def _abs_location(self) -> str:
        return "http://" + self._target()


class Scrapy3SystemtestGenerator(SystemtestGenerator, Scrapy3TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"rel {_b64(self._request_url())} {_b64(self._rel_location())}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"abs {_b64(self._request_url())} {_b64(self._abs_location())}",
            TestResult.PASSING,
        )


class Scrapy3UnittestGenerator(UnittestGenerator, Scrapy3TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.downloadermiddlewares.redirect",
                names=[ast.alias(name="RedirectMiddleware")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.spiders", names=[ast.alias(name="Spider")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="Request"), ast.alias(name="Response")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.utils.test",
                names=[ast.alias(name="get_crawler")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(request_url: str, location: str, expected: str) -> List[ast.stmt]:
        src = (
            f"crawler = get_crawler(Spider)\n"
            f"spider = crawler._create_spider('foo')\n"
            f"mw = RedirectMiddleware.from_crawler(crawler)\n"
            f"req = Request({request_url!r})\n"
            f"rsp = Response({request_url!r}, headers={{'Location': {location!r}}}, "
            f"status=302)\n"
            f"result = mw.process_response(req, rsp, spider)\n"
            f"self.assertEqual({expected!r}, result.url)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        request_url = self._request_url()
        location = self._rel_location()
        expected = "http://" + location.lstrip("/")
        test = self.get_empty_test()
        test.body = self._assert(request_url, location, expected)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        request_url = self._request_url()
        location = self._abs_location()
        test = self.get_empty_test()
        test.body = self._assert(request_url, location, location)
        return test, TestResult.PASSING


grammar_redirect_location: Grammar = clean_up(
    {
        "<start>": ["<mode> <b64> <b64>"],
        "<mode>": ["rel", "abs"],
        "<b64>": ["<char><b64>", "<char>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_redirect_location)


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


# ======================================================================
# bug_36: ``create_instance`` returned whatever ``from_crawler``/
# ``from_settings``/``objcls`` produced, even ``None`` (e.g. a misimplemented
# component whose factory forgot to ``return``).  Callers then failed later with
# a confusing error.  The fix raises ``TypeError("<cls>.<method> returned
# None")`` when the built instance is ``None``.
#
# System-test format: ``<mode> <method> <tag>`` where ``<mode>`` is ``none``
# (factory returns ``None``) or ``ok`` (factory returns an instance),
# ``<method>`` is ``from_settings`` or ``from_crawler`` and ``<tag>`` is an
# integer only used to keep tests distinct.  The harness prints
# ``OK:instance``/``OK:None`` or ``ERR:<exc>``; the oracle expects
# ``ERR:TypeError`` for ``none`` and ``OK:instance`` for ``ok``.  A failing test
# uses ``none`` (buggy: returns None; fixed: TypeError); a passing test uses
# ``ok`` (identical on both builds).
# ======================================================================


class Scrapy36API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "ERR:TypeError" if mode == "none" else "OK:instance"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy36TestGenerator:
    _METHODS = ["from_settings", "from_crawler"]

    def _tag(self) -> int:
        return random.randint(1, 100000)


class Scrapy36SystemtestGenerator(SystemtestGenerator, Scrapy36TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"none {random.choice(self._METHODS)} {self._tag()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"ok {random.choice(self._METHODS)} {self._tag()}",
            TestResult.PASSING,
        )


class Scrapy36UnittestGenerator(UnittestGenerator, Scrapy36TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.utils.misc",
                names=[ast.alias(name="create_instance")],
                level=0,
            )
        ]

    @staticmethod
    def _factory_src(method: str, returns_none: bool, tag: int) -> str:
        ret = "None" if returns_none else "cls()"
        if method == "from_crawler":
            return (
                f"class Obj{tag}(object):\n"
                f"    @classmethod\n"
                f"    def from_crawler(cls, crawler, *a, **k):\n"
                f"        return {ret}\n"
                f"settings = object()\n"
                f"crawler = type('C{tag}', (object,), {{'settings': settings}})()\n"
                f"call = lambda: create_instance(Obj{tag}, settings, crawler)\n"
            )
        return (
            f"class Obj{tag}(object):\n"
            f"    @classmethod\n"
            f"    def from_settings(cls, settings, *a, **k):\n"
            f"        return {ret}\n"
            f"settings = object()\n"
            f"call = lambda: create_instance(Obj{tag}, settings, None)\n"
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        method = random.choice(self._METHODS)
        tag = self._tag()
        src = self._factory_src(method, True, tag) + "self.assertRaises(TypeError, call)\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        method = random.choice(self._METHODS)
        tag = self._tag()
        src = self._factory_src(method, False, tag) + "self.assertIsNotNone(call())\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_create_instance: Grammar = clean_up(
    {
        "<start>": ["<mode> <method> <tag>"],
        "<mode>": ["none", "ok"],
        "<method>": ["from_settings", "from_crawler"],
        "<tag>": ["<nonzero><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<nonzero>": srange("123456789"),
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_create_instance)


# ======================================================================
# bug_34: ``ItemMeta.__new__`` started the field collection with ``fields = {}``,
# so a class that declared its fields via an explicit ``fields = {...}`` class
# attribute (instead of individual ``Field()`` attributes) had that mapping
# discarded -- constructing such an item with one of those keys raised
# ``KeyError``.  The fix seeds it with ``fields = getattr(_class, 'fields', {})``
# so an explicit ``fields`` mapping is honoured.
#
# System-test format: ``<mode> <field> <default> <value>`` (three lowercase
# words after the mode).  ``explicit`` builds ``class T(Item): fields =
# {field: Field(default=default)}`` then ``T(field=value)``; ``normal`` builds a
# class with a plain ``Field`` attribute.  The harness prints ``OK:<item[field]>``
# or ``ERR:<exc>``; the oracle expects ``OK:<value>``.  A failing test uses
# ``explicit`` (buggy: KeyError; fixed: OK); a passing test uses ``normal``
# (identical on both builds).
# ======================================================================


class Scrapy34API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode, _field, _default, value = process.args[2:6]
        except ValueError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = f"OK:{value}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy34TestGenerator:
    def _params(self) -> Tuple[str, str, str]:
        field = _rand_word(3, 7)
        while field == "fields":
            field = _rand_word(3, 7)
        return field, _rand_word(3, 7), _rand_word(3, 7)


class Scrapy34SystemtestGenerator(SystemtestGenerator, Scrapy34TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        field, default, value = self._params()
        return f"explicit {field} {default} {value}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        field, default, value = self._params()
        return f"normal {field} {default} {value}", TestResult.PASSING


class Scrapy34UnittestGenerator(UnittestGenerator, Scrapy34TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.item",
                names=[ast.alias(name="Item"), ast.alias(name="Field")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        field, default, value = self._params()
        src = (
            f"class T(Item):\n"
            f"    fields = {{{field!r}: Field(default={default!r})}}\n"
            f"item = T(**{{{field!r}: {value!r}}})\n"
            f"self.assertEqual({value!r}, item[{field!r}])\n"
        )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        field, default, value = self._params()
        src = (
            f"T = type('T', (Item,), {{{field!r}: Field(default={default!r})}})\n"
            f"item = T(**{{{field!r}: {value!r}}})\n"
            f"self.assertEqual({value!r}, item[{field!r}])\n"
        )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_item_fields: Grammar = clean_up(
    {
        "<start>": ["<mode> <w> <w> <w>"],
        "<mode>": ["explicit", "normal"],
        "<w>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_item_fields)


# ======================================================================
# bug_37: ``Request._set_url`` rejected a URL only when it contained no colon
# (``if ':' not in self._url``).  A URL such as ``foo:bar`` -- which has a colon
# but no real scheme (no ``://`` and not a ``data:`` URI) -- was therefore
# accepted, producing a request with an invalid scheme.  The fix rejects a URL
# unless it contains ``://`` or starts with ``data:``.
#
# System-test format: ``<mode> <b64url>`` with ``<mode>`` ``noscheme`` (a
# ``word:word`` URL) or ``scheme`` (a proper ``http://`` URL).  The harness
# prints ``OK:<req.url>`` or ``ERR:<exc>``; the oracle expects
# ``ERR:ValueError`` for ``noscheme`` and ``OK:<url>`` for ``scheme``.  A
# failing test uses ``noscheme`` (buggy: accepts; fixed: ValueError); a passing
# test uses ``scheme`` (identical on both builds).
# ======================================================================


class Scrapy37API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            url = _b64d(process.args[3]).decode("utf-8")
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "ERR:ValueError" if mode == "noscheme" else f"OK:{url}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy37TestGenerator:
    def _noscheme_url(self) -> str:
        head = _rand_word(3, 8)
        while head == "data":
            head = _rand_word(3, 8)
        return f"{head}:{_rand_word(3, 8)}"

    def _scheme_url(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net', 'io'])}"
        path = "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
        return f"http://{host}{path}"


class Scrapy37SystemtestGenerator(SystemtestGenerator, Scrapy37TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"noscheme {_b64(self._noscheme_url())}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"scheme {_b64(self._scheme_url())}", TestResult.PASSING


class Scrapy37UnittestGenerator(UnittestGenerator, Scrapy37TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http", names=[ast.alias(name="Request")], level=0
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        url = self._noscheme_url()
        src = f"self.assertRaises(ValueError, Request, {url!r})\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        url = self._scheme_url()
        src = f"self.assertEqual({url!r}, Request({url!r}).url)\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_request_scheme: Grammar = clean_up(
    {
        "<start>": ["<mode> <b64>"],
        "<mode>": ["noscheme", "scheme"],
        "<b64>": ["<char><b64>", "<char>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_request_scheme)


# ======================================================================
# bug_31: ``WrappedRequest.get_header`` decoded header values with
# ``to_native_str(value)`` (UTF-8, strict).  A header carrying non-UTF-8 bytes
# therefore raised ``UnicodeDecodeError`` while the cookie middleware processed
# the request.  The fix passes ``errors='replace'`` so undecodable bytes become
# the replacement character instead of crashing.
#
# System-test format: a single urlsafe-base64 token of the raw header-value
# bytes.  The harness builds a ``Request`` with that ``X-Test`` header, wraps it
# and prints ``OK:<get_header>`` or ``ERR:<exc>``; the oracle recomputes
# ``value.decode('utf-8', 'replace')``.  A failing test uses non-UTF-8 bytes
# (buggy: UnicodeDecodeError; fixed: replaced string); a passing test uses ASCII
# bytes (identical on both builds).
# ======================================================================


class Scrapy31API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            value = _b64d(process.args[2])
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:" + value.decode("utf-8", "replace")
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy31TestGenerator:
    def _failing_value(self) -> bytes:
        # contains 0xff, which is never valid UTF-8
        return _rand_word(2, 5).encode("ascii") + b"\xff" + _rand_word(2, 5).encode(
            "ascii"
        )

    def _passing_value(self) -> bytes:
        return _rand_word(3, 10).encode("ascii")


class Scrapy31SystemtestGenerator(SystemtestGenerator, Scrapy31TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._failing_value()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._passing_value()), TestResult.PASSING


class Scrapy31UnittestGenerator(UnittestGenerator, Scrapy31TestGenerator):
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
    def _assert(value: bytes) -> List[ast.stmt]:
        expected = value.decode("utf-8", "replace")
        src = (
            f"request = Request('http://example.com', "
            f"headers={{b'X-Test': {value!r}}})\n"
            f"wrapped = WrappedRequest(request)\n"
            f"self.assertEqual({expected!r}, wrapped.get_header('X-Test'))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._failing_value())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._passing_value())
        return test, TestResult.PASSING


# ======================================================================
# bug_23: ``HttpProxyMiddleware._get_proxy`` built the basic-auth credentials
# with ``base64.b64encode('%s:%s' % (user, password))`` -- passing a ``str`` to
# ``b64encode``, which on Python 3 raises ``TypeError`` for any proxy URL that
# carries a username/password.  The fix wraps the credentials with
# ``to_bytes(...)`` first.
#
# System-test format: a single urlsafe-base64 token of the proxy URL.  The
# harness calls ``_get_proxy(url, 'http')`` and prints ``OK:<creds>`` /
# ``OK:None`` or ``ERR:<exc>``; the oracle recomputes the correct credentials.
# A failing test uses a proxy URL with auth (buggy: TypeError; fixed: base64
# credentials); a passing test uses a URL without auth (identical on both
# builds).
# ======================================================================


def _proxy_creds_expected(url: str) -> str:
    import base64
    from urllib.parse import unquote
    from urllib.request import _parse_proxy

    _type, user, password, _hostport = _parse_proxy(url)
    if user:
        user_pass = "%s:%s" % (unquote(user), unquote(password))
        creds = base64.b64encode(user_pass.encode("utf-8")).strip().decode("ascii")
        return "OK:" + creds
    return "OK:None"


class Scrapy23API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            url = _b64d(process.args[2]).decode("utf-8")
            expected = _proxy_creds_expected(url)
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy23TestGenerator:
    def _host(self) -> str:
        return f"{_rand_word(3, 8)}.{random.choice(['com', 'net', 'io'])}:{random.randint(1024, 9999)}"

    def _auth_url(self) -> str:
        return f"http://{_rand_word(3, 8)}:{_rand_word(3, 8)}@{self._host()}"

    def _noauth_url(self) -> str:
        return f"http://{self._host()}"


class Scrapy23SystemtestGenerator(SystemtestGenerator, Scrapy23TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._auth_url()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._noauth_url()), TestResult.PASSING


class Scrapy23UnittestGenerator(UnittestGenerator, Scrapy23TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.downloadermiddlewares.httpproxy",
                names=[ast.alias(name="HttpProxyMiddleware")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(url: str) -> List[ast.stmt]:
        expected = _proxy_creds_expected(url)[3:]  # strip "OK:"
        creds_expr = "None" if expected == "None" else f"b{expected!r}"
        src = (
            f"mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)\n"
            f"creds, proxy = mw._get_proxy({url!r}, 'http')\n"
            f"self.assertEqual({creds_expr}, creds)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._auth_url())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._noauth_url())
        return test, TestResult.PASSING


# ======================================================================
# bug_20: ``SitemapSpider._parse_sitemap`` fed the raw ``response.body`` (bytes)
# to ``sitemap_urls_from_robots``, which does ``line.lstrip().startswith(
# 'Sitemap:')``.  On Python 3 ``bytes.startswith(str)`` raises ``TypeError`` for
# any non-empty robots.txt.  The fix passes ``response.text`` (a native str).
#
# System-test format: ``<mode> <b64 robots-url> <b64 body>`` with ``<mode>``
# ``content`` (a robots.txt containing ``Sitemap:`` lines) or ``empty`` (empty
# body).  The harness runs ``_parse_sitemap`` and prints ``OK:<comma-joined
# sitemap urls>`` or ``ERR:<exc>``; the oracle recomputes the sitemap urls.  A
# failing test uses ``content`` (buggy: TypeError; fixed: urls); a passing test
# uses ``empty`` (identical on both builds).
# ======================================================================


def _sitemap_urls_expected(body: bytes) -> List[str]:
    text = body.decode("utf-8")
    return [
        line.split(":", 1)[1].strip()
        for line in text.splitlines()
        if line.lstrip().startswith("Sitemap:")
    ]


class Scrapy20API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            body = b"" if mode == "empty" else _b64d(process.args[4])
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:" + ",".join(_sitemap_urls_expected(body))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy20TestGenerator:
    def _robots_url(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net'])}"
        return f"http://{host}/robots.txt"

    def _sitemap_url(self) -> str:
        host = f"{_rand_word(3, 8)}.{random.choice(['com', 'org', 'net'])}"
        return f"http://{host}/{_rand_word(3, 7)}.xml"

    def _content_body(self) -> bytes:
        lines = ["User-agent: *", f"Disallow: /{_rand_word(2, 5)}"]
        for _ in range(random.randint(1, 3)):
            lines.append(f"Sitemap: {self._sitemap_url()}")
        random.shuffle(lines)
        return ("\n".join(lines) + "\n").encode("utf-8")


class Scrapy20SystemtestGenerator(SystemtestGenerator, Scrapy20TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"content {_b64(self._robots_url())} {_b64(self._content_body())}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"empty {_b64(self._robots_url())} {_b64('x')}",
            TestResult.PASSING,
        )


class Scrapy20UnittestGenerator(UnittestGenerator, Scrapy20TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.spiders",
                names=[ast.alias(name="SitemapSpider")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="TextResponse")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(robots_url: str, body: bytes) -> List[ast.stmt]:
        expected = _sitemap_urls_expected(body)
        src = (
            f"spider = SitemapSpider.__new__(SitemapSpider)\n"
            f"response = TextResponse(url={robots_url!r}, body={body!r}, "
            f"encoding='utf-8')\n"
            f"urls = [r.url for r in spider._parse_sitemap(response)]\n"
            f"self.assertEqual({expected!r}, urls)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._robots_url(), self._content_body())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._robots_url(), b"")
        return test, TestResult.PASSING


grammar_sitemap: Grammar = clean_up(
    {
        "<start>": ["<mode> <b64> <b64>"],
        "<mode>": ["content", "empty"],
        "<b64>": ["<char><b64>", "<char>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_sitemap)


# ======================================================================
# bug_22: ``XmlItemExporter._xg_characters`` assumed every non-``str`` field
# value was ``bytes`` and called ``value.decode(...)`` on it.  Exporting an item
# with a non-string value (``int``/``float``/``bool``) therefore raised
# ``AttributeError`` (e.g. ``'int' object has no attribute 'decode'``).  The fix
# converts such values with ``str(serialized_value)`` before writing them.
#
# System-test format: a single urlsafe-base64 token of a one-field Python dict
# literal.  The harness exports it with ``XmlItemExporter`` to a buffer and
# prints ``OK:<b64 xml>`` or ``ERR:<exc>``; the oracle recomputes the correct
# XML.  A failing test uses a non-string value (buggy: AttributeError; fixed:
# ``str(value)`` in the XML); a passing test uses a string value (identical on
# both builds).
# ======================================================================


def _xml_export_expected(item: dict) -> bytes:
    (key, value), = item.items()
    body = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        "<items><item><%s>%s</%s></item></items>" % (key, str(value), key)
    )
    return body.encode("utf-8")


class Scrapy22API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            item = ast.literal_eval(_b64d(process.args[2]).decode("utf-8"))
            assert isinstance(item, dict) and len(item) == 1
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:" + _b64(_xml_export_expected(item))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, "Expected XML matched"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy22TestGenerator:
    def _failing_item(self) -> dict:
        value = random.choice(
            [random.randint(-999, 999), round(random.uniform(-99, 99), 2),
             random.choice([True, False])]
        )
        return {_rand_word(3, 8): value}

    def _passing_item(self) -> dict:
        return {_rand_word(3, 8): _rand_word(3, 8)}


class Scrapy22SystemtestGenerator(SystemtestGenerator, Scrapy22TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(repr(self._failing_item())), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(repr(self._passing_item())), TestResult.PASSING


class Scrapy22UnittestGenerator(UnittestGenerator, Scrapy22TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(module="io", names=[ast.alias(name="BytesIO")], level=0),
            ast.ImportFrom(
                module="scrapy.exporters",
                names=[ast.alias(name="XmlItemExporter")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(item: dict) -> List[ast.stmt]:
        expected = _xml_export_expected(item)
        src = (
            f"fp = BytesIO()\n"
            f"ie = XmlItemExporter(fp)\n"
            f"ie.start_exporting()\n"
            f"ie.export_item({item!r})\n"
            f"ie.finish_exporting()\n"
            f"self.assertEqual({expected!r}, fp.getvalue())\n"
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
# bug_27: ``RedirectMiddleware.process_response`` only skipped redirection when
# ``dont_redirect`` was set in the request meta or the response status was in the
# spider's ``handle_httpstatus_list``.  It ignored the per-request meta keys
# ``handle_httpstatus_list`` and ``handle_httpstatus_all``, so a request that
# explicitly asked to handle a redirect status itself was still redirected
# (here it even raises because the raw bytes ``Location`` header cannot be
# ``urljoin``-ed).  The fix also returns the response unchanged when the status
# is in ``request.meta['handle_httpstatus_list']`` or
# ``request.meta['handle_httpstatus_all']`` is truthy.
#
# System-test format: ``<mode> <status> <word>`` where ``<mode>`` selects how the
# response status is declared as "handle it myself" -- ``list``/``all`` set it
# via the *request meta* (the buggy path, so FAILING) and ``dont``/``spiderlist``
# set it via ``dont_redirect``/the spider attribute (honoured on both builds, so
# PASSING).  ``<status>`` is a redirect status and ``<word>`` only varies the
# host.  The harness prints ``SAME`` (response returned unchanged), ``REDIRECT``
# or ``ERR:<exc>``; the correct (fixed) behaviour is always ``SAME``.
# ======================================================================


class Scrapy27API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "SAME"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy27TestGenerator:
    _STATUS = ["301", "302", "303", "307"]
    _FAIL_MODES = ["list", "all"]
    _PASS_MODES = ["dont", "spiderlist"]

    def _word(self) -> str:
        return _rand_word(3, 8)


class Scrapy27SystemtestGenerator(SystemtestGenerator, Scrapy27TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(self._FAIL_MODES)} {random.choice(self._STATUS)} "
            f"{self._word()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.choice(self._PASS_MODES)} {random.choice(self._STATUS)} "
            f"{self._word()}",
            TestResult.PASSING,
        )


class Scrapy27UnittestGenerator(UnittestGenerator, Scrapy27TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.downloadermiddlewares.redirect",
                names=[ast.alias(name="RedirectMiddleware")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.spiders", names=[ast.alias(name="Spider")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="Request"), ast.alias(name="Response")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.utils.test",
                names=[ast.alias(name="get_crawler")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(mode: str, status: str, word: str) -> List[ast.stmt]:
        url = f"http://{word}.example.com/{status}"
        url2 = f"http://{word}.example.com/redirected"
        if mode == "list":
            meta = f"{{'handle_httpstatus_list': [{status}]}}"
            spider_setup = ""
        elif mode == "all":
            meta = "{'handle_httpstatus_all': True}"
            spider_setup = ""
        elif mode == "dont":
            meta = "{'dont_redirect': True}"
            spider_setup = ""
        else:  # spiderlist
            meta = "{}"
            spider_setup = f"spider.handle_httpstatus_list = [{status}]\n"
        src = (
            "crawler = get_crawler(Spider)\n"
            "spider = crawler._create_spider('foo')\n"
            f"{spider_setup}"
            "mw = RedirectMiddleware.from_crawler(crawler)\n"
            f"req = Request({url!r}, meta={meta})\n"
            f"rsp = Response({url!r}, headers={{'Location': {url2!r}}}, "
            f"status={status}, request=req)\n"
            "self.assertIs(rsp, mw.process_response(req, rsp, spider))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(
            random.choice(self._FAIL_MODES), random.choice(self._STATUS), self._word()
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(
            random.choice(self._PASS_MODES), random.choice(self._STATUS), self._word()
        )
        return test, TestResult.PASSING


grammar_redirect_meta: Grammar = clean_up(
    {
        "<start>": ["<mode> <status> <word>"],
        "<mode>": ["list", "all", "dont", "spiderlist"],
        "<status>": ["301", "302", "303", "307"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_redirect_meta)


# ======================================================================
# bug_10: ``RedirectMiddleware.process_response`` resolved the redirect target
# with ``to_native_str(response.headers['location'].decode('latin1'))``.  A
# ``Location`` header carrying percent-encodable bytes (a non-ASCII path, in
# either latin-1 or UTF-8) was therefore left un-encoded / mis-encoded in the
# redirected URL.  The fix computes the target with
# ``safe_url_string(response.headers['location'])`` so the bytes are correctly
# percent-encoded.
#
# System-test format: a single urlsafe-base64 token of the raw ``Location``
# bytes.  The harness runs the middleware, compares the resulting url against the
# reference ``urljoin(request.url, safe_url_string(location))`` (the fixed
# behaviour -- ``safe_url_string`` lives in w3lib and is identical on both
# builds) and prints ``MATCH`` / ``NOMATCH:<url>`` / ``ERR:<exc>``; the oracle
# expects ``MATCH``.  A failing test uses a non-ASCII location (buggy: mis-
# encoded -> NOMATCH; fixed: MATCH); a passing test uses an ASCII location
# (identical on both builds).
# ======================================================================


class Scrapy10API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _b64d(process.args[2])
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "MATCH"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy10TestGenerator:
    _NONASCII = "éñüàçßµ"

    def _failing_location(self) -> bytes:
        stem = "/" + _rand_word(2, 6) + random.choice(self._NONASCII) + _rand_word(0, 4)
        return stem.encode(random.choice(["latin-1", "utf-8"]))

    def _passing_location(self) -> bytes:
        path = "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
        return path.encode("ascii")


class Scrapy10SystemtestGenerator(SystemtestGenerator, Scrapy10TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._failing_location()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return _b64(self._passing_location()), TestResult.PASSING


class Scrapy10UnittestGenerator(UnittestGenerator, Scrapy10TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.downloadermiddlewares.redirect",
                names=[ast.alias(name="RedirectMiddleware")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.spiders", names=[ast.alias(name="Spider")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="Request"), ast.alias(name="Response")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.utils.test",
                names=[ast.alias(name="get_crawler")],
                level=0,
            ),
            ast.ImportFrom(
                module="w3lib.url", names=[ast.alias(name="safe_url_string")], level=0
            ),
            ast.ImportFrom(
                module="six.moves.urllib.parse",
                names=[ast.alias(name="urljoin")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(location: bytes) -> List[ast.stmt]:
        url = "http://scrapytest.org/first"
        src = (
            "crawler = get_crawler(Spider)\n"
            "spider = crawler._create_spider('foo')\n"
            "mw = RedirectMiddleware.from_crawler(crawler)\n"
            f"loc = {location!r}\n"
            f"rsp = Response({url!r}, headers={{'Location': loc}}, status=302)\n"
            f"result = mw.process_response(Request({url!r}), rsp, spider)\n"
            f"self.assertEqual(urljoin({url!r}, safe_url_string(loc)), result.url)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._failing_location())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._passing_location())
        return test, TestResult.PASSING


# ======================================================================
# bug_39: ``Spider.start_requests`` decided whether to emit the
# ``make_requests_from_url`` deprecation warning with
# ``self.make_requests_from_url is not Spider.make_requests_from_url``.  A *bound*
# method is never identical to the underlying function, so this comparison was
# always true and *every* spider -- even one that did not override the method --
# got the deprecation warning.  The fix compares the class attribute
# ``cls.make_requests_from_url is not Spider.make_requests_from_url`` so only
# spiders that actually override the method are warned.
#
# System-test format: ``<mode> <word>`` where ``<mode>`` is ``plain`` (a spider
# that does NOT override ``make_requests_from_url``) or ``override`` (a spider
# that does), and ``<word>`` only varies the spider name/host.  The harness runs
# ``start_requests`` under ``catch_warnings`` and prints
# ``OK:<n_requests>:<n_deprecation_warnings>``; the correct (fixed) warning count
# is 0 for ``plain`` and 1 for ``override``.  A failing test uses ``plain``
# (buggy: 1 warning; fixed: 0); a passing test uses ``override`` (identical on
# both builds).
# ======================================================================


class Scrapy39API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        warn_count = 0 if mode == "plain" else 1
        expected = f"OK:1:{warn_count}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy39TestGenerator:
    def _word(self) -> str:
        return _rand_word(3, 8)


class Scrapy39SystemtestGenerator(SystemtestGenerator, Scrapy39TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"plain {self._word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"override {self._word()}", TestResult.PASSING


class Scrapy39UnittestGenerator(UnittestGenerator, Scrapy39TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="warnings")]),
            ast.ImportFrom(
                module="scrapy.spiders", names=[ast.alias(name="Spider")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.http", names=[ast.alias(name="Request")], level=0
            ),
        ]

    @staticmethod
    def _assert(mode: str, word: str) -> List[ast.stmt]:
        url = f"http://{word}.example.com"
        warn_count = 0 if mode == "plain" else 1
        if mode == "override":
            body = (
                f"class S(Spider):\n"
                f"    name = {word!r}\n"
                f"    start_urls = [{url!r}]\n"
                f"    def make_requests_from_url(self, u):\n"
                f"        return Request(u + '/foo', dont_filter=True)\n"
            )
        else:
            body = (
                f"class S(Spider):\n"
                f"    name = {word!r}\n"
                f"    start_urls = [{url!r}]\n"
            )
        src = (
            f"{body}"
            f"with warnings.catch_warnings(record=True) as w:\n"
            f"    warnings.simplefilter('always')\n"
            f"    reqs = list(S().start_requests())\n"
            f"count = sum(1 for x in w "
            f"if 'make_requests_from_url' in str(x.message))\n"
            f"self.assertEqual(1, len(reqs))\n"
            f"self.assertEqual({warn_count}, count)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("plain", self._word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("override", self._word())
        return test, TestResult.PASSING


grammar_deprecation: Grammar = clean_up(
    {
        "<start>": ["<mode> <word>"],
        "<mode>": ["plain", "override"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_deprecation)


# ======================================================================
# bug_1: ``OffsiteMiddleware.get_host_regex`` warned about URL entries in
# ``allowed_domains`` by iterating and calling ``url_pattern.match(domain)`` on
# every entry *before* filtering out ``None``.  A spider whose ``allowed_domains``
# contained a ``None`` entry therefore raised ``TypeError`` (``re.match`` on
# ``None``).  The fix skips ``None`` entries (and only escapes real domains).
#
# System-test format: ``<mode> <domain>`` where ``<mode>`` is ``none``
# (``allowed_domains=[domain, None]``) or ``plain`` (``allowed_domains=[domain]``)
# and ``<domain>`` is a normal ``word.tld`` host.  The harness builds the regex
# and prints ``OK:<matches domain><matches sub.domain><matches evil.com>`` or
# ``ERR:<exc>``; the correct (fixed) result is always ``OK:110``.  A failing test
# uses ``none`` (buggy: TypeError; fixed: OK:110); a passing test uses ``plain``
# (identical on both builds).
# ======================================================================


class Scrapy1API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            _domain = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:110"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy1TestGenerator:
    _TLDS = ["com", "org", "net", "io"]

    def _domain(self) -> str:
        return f"{_rand_word(3, 8)}.{random.choice(self._TLDS)}"


class Scrapy1SystemtestGenerator(SystemtestGenerator, Scrapy1TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"none {self._domain()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"plain {self._domain()}", TestResult.PASSING


class Scrapy1UnittestGenerator(UnittestGenerator, Scrapy1TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.spidermiddlewares.offsite",
                names=[ast.alias(name="OffsiteMiddleware")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.spiders", names=[ast.alias(name="Spider")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.utils.test",
                names=[ast.alias(name="get_crawler")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(mode: str, domain: str) -> List[ast.stmt]:
        allowed = f"[{domain!r}, None]" if mode == "none" else f"[{domain!r}]"
        src = (
            "crawler = get_crawler(Spider)\n"
            "mw = OffsiteMiddleware.from_crawler(crawler)\n"
            "spider = crawler._create_spider('foo')\n"
            f"spider.allowed_domains = {allowed}\n"
            "regex = mw.get_host_regex(spider)\n"
            f"self.assertTrue(regex.search({domain!r}))\n"
            f"self.assertTrue(regex.search('sub.' + {domain!r}))\n"
            "self.assertFalse(regex.search('evil.com'))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("none", self._domain())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("plain", self._domain())
        return test, TestResult.PASSING


grammar_offsite: Grammar = clean_up(
    {
        "<start>": ["<mode> <domain>"],
        "<mode>": ["none", "plain"],
        "<domain>": ["<word>.<tld>"],
        "<tld>": ["com", "org", "net", "io"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_offsite)


# ======================================================================
# bug_30: ``scrapy/cmdline.py._iter_command_classes`` enumerated command classes
# with ``vars(module).itervalues()`` -- a Python-2 dict method that does not
# exist on Python 3.  Command discovery therefore raised ``AttributeError`` and
# every ``scrapy`` sub-command (including ``scrapy version``) crashed.  The fix
# uses ``vars(module).values()``.
#
# System-test format: ``<mode> <tag>`` where ``<mode>`` is ``cli`` (run
# ``scrapy version`` through ``scrapy.cmdline`` -- the buggy path) or ``import``
# (read the version by importing scrapy, which never touches ``cmdline``), and
# ``<tag>`` only keeps tests distinct.  The harness runs the chosen command in a
# subprocess and prints ``OK`` when it exits 0 with a ``Scrapy <version>`` line,
# else ``ERR``; the correct behaviour is always ``OK``.  A failing test uses
# ``cli`` (buggy: AttributeError -> ERR; fixed: OK); a passing test uses
# ``import`` (identical on both builds).
# ======================================================================


class Scrapy30API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy30TestGenerator:
    def _tag(self) -> int:
        return random.randint(1, 1000000)


class Scrapy30SystemtestGenerator(SystemtestGenerator, Scrapy30TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"cli {self._tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"import {self._tag()}", TestResult.PASSING


class Scrapy30UnittestGenerator(UnittestGenerator, Scrapy30TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="sys")]),
            ast.Import(names=[ast.alias(name="subprocess")]),
        ]

    @staticmethod
    def _assert(mode: str, tag: int) -> List[ast.stmt]:
        if mode == "cli":
            cmd = "[sys.executable, '-m', 'scrapy.cmdline', 'version']"
        else:
            cmd = (
                "[sys.executable, '-c', "
                "\"import scrapy; print('Scrapy ' + scrapy.__version__)\"]"
            )
        src = (
            f"tag = {tag}\n"
            f"proc = subprocess.run({cmd}, "
            f"stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n"
            f"out = proc.stdout.decode('utf-8', 'replace').strip()\n"
            f"self.assertEqual(0, proc.returncode)\n"
            f"self.assertTrue(out.startswith('Scrapy '))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("cli", self._tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("import", self._tag())
        return test, TestResult.PASSING


grammar_version: Grammar = clean_up(
    {
        "<start>": ["<mode> <tag>"],
        "<mode>": ["cli", "import"],
        "<tag>": ["<nonzero><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<nonzero>": srange("123456789"),
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_version)


# ======================================================================
# bug_8: ``ItemMeta.__new__`` rebuilt the class through
# ``super().__new__(mcs, 'x_' + class_name, ...)`` and then a second
# ``super().__new__`` without ever preserving the compiler-provided
# ``__classcell__`` entry.  Any ``Item`` subclass that used a zero-argument
# ``super()`` (or referenced ``__class__``) in one of its methods therefore
# failed at class-creation time with ``TypeError: __class__ set to ... defining
# ...``.  The fix pops ``__classcell__`` off ``attrs`` and re-injects it into the
# final class namespace.
#
# System-test format: ``<mode> <word>`` where ``<mode>`` is ``classcell`` (define
# an ``Item`` subclass whose method uses ``super()`` -- the buggy path) or
# ``plain`` (a subclass with just a ``Field``), and ``<word>`` names the class /
# keeps tests distinct.  The harness defines and instantiates the class and
# prints ``OK`` or ``ERR:<exc>``; the correct behaviour is always ``OK``.  A
# failing test uses ``classcell`` (buggy: TypeError; fixed: OK); a passing test
# uses ``plain`` (identical on both builds).
# ======================================================================


class Scrapy8API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            _word = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy8TestGenerator:
    def _word(self) -> str:
        return _rand_word(3, 8)


class Scrapy8SystemtestGenerator(SystemtestGenerator, Scrapy8TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"classcell {self._word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"plain {self._word()}", TestResult.PASSING


class Scrapy8UnittestGenerator(UnittestGenerator, Scrapy8TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.item",
                names=[ast.alias(name="Item"), ast.alias(name="Field")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(mode: str, word: str) -> List[ast.stmt]:
        if mode == "classcell":
            src = (
                f"class Item_{word}(Item):\n"
                f"    def method(self):\n"
                f"        return super().__init__\n"
                f"item = Item_{word}()\n"
                f"self.assertIsNotNone(item)\n"
            )
        else:
            src = (
                f"class Item_{word}(Item):\n"
                f"    name = Field()\n"
                f"item = Item_{word}(name='x')\n"
                f"self.assertEqual('x', item['name'])\n"
            )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("classcell", self._word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("plain", self._word())
        return test, TestResult.PASSING


grammar_classcell: Grammar = clean_up(
    {
        "<start>": ["<mode> <word>"],
        "<mode>": ["classcell", "plain"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_classcell)


# ======================================================================
# bug_26: ``BaseSettings._getcomposite`` merged a ``<NAME>_BASE`` mapping with
# the current ``<NAME>`` settings by ``compsett.update(self[name])`` -- copying
# *every* entry of ``self[name]``, including ones that still carry the
# ``'default'`` priority.  Once the Scrapy defaults were moved into the plain
# ``<NAME>`` setting, this made a user's ``_BASE`` values get overridden by those
# defaults.  The fix only copies ``self[name]`` entries whose priority is
# strictly higher than ``'default'``.
#
# System-test format: ``<mode> <b1> <b2> <v3> <x1>`` (four ints).  A settings
# object is built with ``TEST_BASE = {1: b1, 2: b2}`` and a ``TEST`` sub-setting;
# in ``override`` mode ``TEST`` also holds ``{1: x1}`` at ``'default'`` priority
# (the buggy path -- that default entry must be dropped), in ``clean`` mode it
# does not.  Both modes add ``3 -> v3`` at ``'project'`` priority.  The harness
# prints ``OK:<sorted (key,value) items of _getcomposite('TEST')>``; the correct
# (fixed) composite is always ``[(1, b1), (2, b2), (3, v3)]``.  A failing test
# uses ``override`` with ``x1 != b1`` (buggy: cs[1]==x1; fixed: cs[1]==b1); a
# passing test uses ``clean`` (identical on both builds).
# ======================================================================


def _composite_expected(b1: int, b2: int, v3: int) -> list:
    return [(1, b1), (2, b2), (3, v3)]


class Scrapy26API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            b1 = int(process.args[3])
            b2 = int(process.args[4])
            v3 = int(process.args[5])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:" + repr(_composite_expected(b1, b2, v3))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy26TestGenerator:
    def _vals(self) -> Tuple[int, int, int, int]:
        b1 = random.randint(1, 9)
        b2 = random.randint(1, 999)
        v3 = random.randint(1, 999)
        x1 = random.randint(1, 999)
        while x1 == b1:
            x1 = random.randint(1, 999)
        return b1, b2, v3, x1


class Scrapy26SystemtestGenerator(SystemtestGenerator, Scrapy26TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        b1, b2, v3, x1 = self._vals()
        return f"override {b1} {b2} {v3} {x1}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        b1, b2, v3, x1 = self._vals()
        return f"clean {b1} {b2} {v3} {x1}", TestResult.PASSING


class Scrapy26UnittestGenerator(UnittestGenerator, Scrapy26TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.settings",
                names=[ast.alias(name="BaseSettings")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(mode: str, b1: int, b2: int, v3: int, x1: int) -> List[ast.stmt]:
        if mode == "override":
            test_sub = f"BaseSettings({{1: {x1}}}, 'default')"
        else:
            test_sub = "BaseSettings()"
        expected = _composite_expected(b1, b2, v3)
        src = (
            f"s = BaseSettings({{'TEST_BASE': {{1: {b1}, 2: {b2}}}, "
            f"'TEST': {test_sub}}})\n"
            f"s['TEST'].set(3, {v3}, priority='project')\n"
            f"cs = s._getcomposite('TEST')\n"
            f"self.assertEqual({expected!r}, "
            f"sorted((int(k), int(cs[k])) for k in cs))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        b1, b2, v3, x1 = self._vals()
        test = self.get_empty_test()
        test.body = self._assert("override", b1, b2, v3, x1)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        b1, b2, v3, x1 = self._vals()
        test = self.get_empty_test()
        test.body = self._assert("clean", b1, b2, v3, x1)
        return test, TestResult.PASSING


grammar_composite: Grammar = clean_up(
    {
        "<start>": ["<mode> <int> <int> <int> <int>"],
        "<mode>": ["override", "clean"],
        "<int>": ["<nonzero><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<nonzero>": srange("123456789"),
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_composite)


# ======================================================================
# bug_4: ``ContractsManager._clean_req.eb_wrapper`` built the error triple as
# ``exc_info = failure.value, failure.type, failure.getTracebackObject()`` -- the
# ``value`` and ``type`` are swapped.  ``TestResult.addError`` expects
# ``(exctype, value, tb)``; with the swap it received an exception *instance*
# where the *class* was expected and raised ``AttributeError`` while formatting
# the traceback, so a contract errback crashed instead of recording an error.
# The fix uses ``failure.type, failure.value, ...``.
#
# System-test format: ``<mode> <word>`` where ``<mode>`` is ``errback`` (drive a
# contract request's ``errback`` with a Twisted ``Failure`` -- the buggy path) or
# ``callback`` (drive a contract request's ``callback`` whose spider method
# raises, which records the error via ``sys.exc_info()`` and works on both), and
# ``<word>`` keeps tests distinct.  The harness prints ``OK:1`` when an error was
# recorded without raising, ``OK:0`` or ``ERR:<exc>`` otherwise; the correct
# behaviour is always ``OK:1``.  A failing test uses ``errback`` (buggy:
# AttributeError; fixed: OK:1); a passing test uses ``callback`` (identical on
# both builds).
# ======================================================================


_SCRAPY4_RUN_SRC = '''
def _run(self, mode, word):
    url = 'http://%s.scrapy.org' % word

    class ResponseMock(object):
        pass

    resp = ResponseMock()
    resp.url = url

    class TestSpider(Spider):
        name = 'demo_%s' % word

        def returns_request(self, response):
            """method which returns request
            @url http://scrapy.org
            @returns requests 1
            """
            return Request('http://scrapy.org')

        def raises_cb(self, response):
            """method whose callback raises
            @url http://scrapy.org
            """
            raise ValueError('boom')

    conman = ContractsManager([UrlContract, ReturnsContract, ScrapesContract])
    results = TextTestResult(stream=None, descriptions=False, verbosity=0)
    spider = TestSpider()
    if mode == 'errback':
        try:
            raise HttpError(resp, 'Ignoring non-200 response')
        except HttpError:
            fm = failure.Failure()
        request = conman.from_method(spider.returns_request, results)
        request.errback(fm)
    else:
        request = conman.from_method(spider.raises_cb, results)
        request.callback(resp)
    return 'OK:%d' % (1 if results.errors else 0)
'''


class Scrapy4API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            _word = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:1"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy4TestGenerator:
    def _word(self) -> str:
        return _rand_word(3, 8)


class Scrapy4SystemtestGenerator(SystemtestGenerator, Scrapy4TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"errback {self._word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"callback {self._word()}", TestResult.PASSING


class Scrapy4UnittestGenerator(UnittestGenerator, Scrapy4TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="unittest", names=[ast.alias(name="TextTestResult")], level=0
            ),
            ast.ImportFrom(
                module="twisted.python", names=[ast.alias(name="failure")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.spidermiddlewares.httperror",
                names=[ast.alias(name="HttpError")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.spiders", names=[ast.alias(name="Spider")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.http", names=[ast.alias(name="Request")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.contracts",
                names=[ast.alias(name="ContractsManager")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.contracts.default",
                names=[
                    ast.alias(name="UrlContract"),
                    ast.alias(name="ReturnsContract"),
                    ast.alias(name="ScrapesContract"),
                ],
                level=0,
            ),
        ]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_SCRAPY4_RUN_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self._word()
        src = f"self.assertEqual('OK:1', self._run('errback', {word!r}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self._word()
        src = f"self.assertEqual('OK:1', self._run('callback', {word!r}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_contracts: Grammar = clean_up(
    {
        "<start>": ["<mode> <word>"],
        "<mode>": ["errback", "callback"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_contracts)


# ======================================================================
# bug_16: ``canonicalize_url`` (via ``_unquotepath`` / ``parse_qsl``) decoded
# percent-encoded path and query bytes with the strict UTF-8 ``unquote``.  A
# non-UTF-8 percent sequence (e.g. a lone latin-1 byte ``%a3``) was therefore
# turned into the Unicode replacement character and re-encoded as ``%EF%BF%BD``,
# corrupting the URL.  The fix decodes with ``unquote_to_bytes`` /
# ``parse_qsl_to_bytes`` so the raw byte is preserved and merely re-percent-
# encoded (which also normalises the hex to upper-case).
#
# System-test format: ``<mode> <b64url>`` where ``<mode>`` is ``hex`` (a URL
# containing a lone non-UTF-8 percent byte in ``0x80..0xBF`` -- the buggy path)
# or ``plain`` (a plain ASCII URL with no percent-encoding).  The harness prints
# ``OK:<canonicalize_url(url)>`` or ``ERR:<exc>``; the correct (fixed) result is
# the url with every ``%xx`` upper-cased (an identity for a plain URL).  A
# failing test uses ``hex`` (buggy: byte mangled to %EF%BF%BD; fixed: byte kept,
# hex upper-cased); a passing test uses ``plain`` (identical on both builds).
# ======================================================================

import re as _re


def _norm_pct(url: str) -> str:
    return _re.sub(r"%([0-9a-fA-F]{2})", lambda m: "%" + m.group(1).upper(), url)


class Scrapy16API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            url = _b64d(process.args[3]).decode("utf-8")
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:" + _norm_pct(url)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy16TestGenerator:
    _TLDS = ["com", "org", "net", "io"]

    def _host(self) -> str:
        return f"{_rand_word(3, 8)}.example.{random.choice(self._TLDS)}"

    def _hex_url(self) -> str:
        # a lone non-UTF-8 byte in 0x80..0xBF is always invalid UTF-8, so the
        # buggy decoder mangles it while the fixed one keeps it (upper-cased).
        hh = "%02x" % random.randint(0x80, 0xBF)
        return f"http://{self._host()}/{_rand_word(2, 5)}%{hh}{_rand_word(2, 5)}"

    def _plain_url(self) -> str:
        path = "/" + "/".join(_rand_word(2, 6) for _ in range(random.randint(1, 3)))
        return f"http://{self._host()}{path}"


class Scrapy16SystemtestGenerator(SystemtestGenerator, Scrapy16TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"hex {_b64(self._hex_url())}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"plain {_b64(self._plain_url())}", TestResult.PASSING


class Scrapy16UnittestGenerator(UnittestGenerator, Scrapy16TestGenerator):
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
        expected = _norm_pct(url)
        src = f"self.assertEqual({expected!r}, canonicalize_url({url!r}))\n"
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._hex_url())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._plain_url())
        return test, TestResult.PASSING


grammar_canonicalize: Grammar = clean_up(
    {
        "<start>": ["<mode> <b64>"],
        "<mode>": ["hex", "plain"],
        "<b64>": ["<char><b64>", "<char>"],
        "<char>": srange(string.ascii_letters + string.digits + "-_="),
    }
)

assert is_valid_grammar(grammar_canonicalize)


# ======================================================================
# bug_32: ``CrawlerProcess.__init__`` passed the *raw* ``settings`` argument to
# ``configure_logging`` / ``log_scrapy_info`` instead of the normalised
# ``self.settings``.  ``CrawlerRunner.__init__`` wraps a plain ``dict`` into a
# ``Settings`` object as ``self.settings``, so constructing
# ``CrawlerProcess({...})`` with a dict made ``configure_logging`` receive a dict
# and crash with ``KeyError`` (a dict has no ``getbool`` etc.).  The fix uses
# ``self.settings``.
#
# System-test format: ``<mode> <key> <val>`` where ``<mode>`` is ``dict`` (build
# ``CrawlerProcess`` from a plain dict -- the buggy path) or ``settings`` (build
# it from a ``Settings`` object, which works on both), and ``<key>``/``<val>``
# are arbitrary lowercase words.  The harness prints ``OK`` when the process is
# built and its settings expose the value plus the default ``RETRY_ENABLED``,
# else ``BAD``/``ERR:<exc>``; the correct behaviour is always ``OK``.  A failing
# test uses ``dict`` (buggy: KeyError; fixed: OK); a passing test uses
# ``settings`` (identical on both builds).
# ======================================================================


class Scrapy32API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            _key = process.args[3]
            _val = process.args[4]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy32TestGenerator:
    def _kv(self) -> Tuple[str, str]:
        return _rand_word(3, 8), _rand_word(3, 8)


class Scrapy32SystemtestGenerator(SystemtestGenerator, Scrapy32TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        key, val = self._kv()
        return f"dict {key} {val}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        key, val = self._kv()
        return f"settings {key} {val}", TestResult.PASSING


class Scrapy32UnittestGenerator(UnittestGenerator, Scrapy32TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.crawler",
                names=[ast.alias(name="CrawlerProcess")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.settings",
                names=[
                    ast.alias(name="Settings"),
                    ast.alias(name="default_settings"),
                ],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(mode: str, key: str, val: str) -> List[ast.stmt]:
        arg = f"{{{key!r}: {val!r}}}" if mode == "dict" else f"Settings({{{key!r}: {val!r}}})"
        src = (
            f"rp = CrawlerProcess({arg})\n"
            f"self.assertEqual({val!r}, rp.settings[{key!r}])\n"
            f"self.assertEqual(default_settings.RETRY_ENABLED, "
            f"rp.settings['RETRY_ENABLED'])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key, val = self._kv()
        test = self.get_empty_test()
        test.body = self._assert("dict", key, val)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        key, val = self._kv()
        test = self.get_empty_test()
        test.body = self._assert("settings", key, val)
        return test, TestResult.PASSING


grammar_crawler_dict: Grammar = clean_up(
    {
        "<start>": ["<mode> <word> <word>"],
        "<mode>": ["dict", "settings"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_crawler_dict)


# ======================================================================
# bug_35: ``_get_spider_loader`` resolved the loader class with
# ``settings.get('SPIDER_LOADER_CLASS', settings.get('SPIDER_MANAGER_CLASS'))``.
# Because ``SPIDER_LOADER_CLASS`` always has a default value, a user who set the
# (deprecated) ``SPIDER_MANAGER_CLASS`` had it silently ignored -- the default
# loader was used instead.  The fix looks up ``SPIDER_MANAGER_CLASS`` first,
# falling back to ``SPIDER_LOADER_CLASS``, so the deprecated option keeps working.
#
# System-test format: ``<mode> <word>`` where ``<mode>`` is ``manager`` (point a
# custom loader at the deprecated ``SPIDER_MANAGER_CLASS`` -- the buggy path) or
# ``loader`` (point it at ``SPIDER_LOADER_CLASS``, honoured on both), and
# ``<word>`` names a throw-away module holding the custom loader (kept distinct
# per test).  The harness prints ``OK:1`` when the built ``spider_loader`` is the
# custom class, ``OK:0`` otherwise, or ``ERR:<exc>``; the correct behaviour is
# always ``OK:1``.  A failing test uses ``manager`` (buggy: default loader used
# -> OK:0; fixed: custom -> OK:1); a passing test uses ``loader`` (identical on
# both builds).
# ======================================================================


class Scrapy35API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            _word = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:1"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy35TestGenerator:
    def _word(self) -> str:
        return _rand_word(4, 9)


class Scrapy35SystemtestGenerator(SystemtestGenerator, Scrapy35TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"manager {self._word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"loader {self._word()}", TestResult.PASSING


class Scrapy35UnittestGenerator(UnittestGenerator, Scrapy35TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="sys")]),
            ast.Import(names=[ast.alias(name="types")]),
            ast.Import(names=[ast.alias(name="warnings")]),
            ast.ImportFrom(
                module="scrapy.crawler",
                names=[ast.alias(name="CrawlerRunner")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.spiderloader",
                names=[ast.alias(name="SpiderLoader")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(mode: str, word: str) -> List[ast.stmt]:
        setting = "SPIDER_MANAGER_CLASS" if mode == "manager" else "SPIDER_LOADER_CLASS"
        src = (
            f"modname = 'customloader_{word}'\n"
            f"mod = types.ModuleType(modname)\n"
            f"class CustomSpiderLoader(SpiderLoader):\n"
            f"    pass\n"
            f"mod.CustomSpiderLoader = CustomSpiderLoader\n"
            f"sys.modules[modname] = mod\n"
            f"with warnings.catch_warnings():\n"
            f"    warnings.simplefilter('ignore')\n"
            f"    runner = CrawlerRunner("
            f"{{{setting!r}: modname + '.CustomSpiderLoader'}})\n"
            f"    loader = runner.spider_loader\n"
            f"self.assertIsInstance(loader, CustomSpiderLoader)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("manager", self._word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("loader", self._word())
        return test, TestResult.PASSING


grammar_spider_loader: Grammar = clean_up(
    {
        "<start>": ["<mode> <word>"],
        "<mode>": ["manager", "loader"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_spider_loader)


# ======================================================================
# bug_21: ``RobotsTxtMiddleware._robots_error`` did
# ``self._parsers.pop(netloc).callback(None)``.  When the robots.txt download
# failed *synchronously* (e.g. an immediate ``DNSLookupError``), this errback ran
# in the middle of ``robot_parser`` -- before it re-read ``self._parsers[netloc]``
# -- so the key was already gone and ``robot_parser`` crashed with ``KeyError``.
# The fix keeps the key (``self._parsers[netloc] = None``) instead of popping it.
#
# System-test format: ``<mode> <word>`` where ``<mode>`` is ``immediate`` (the
# mocked ``engine.download`` errbacks synchronously -- the buggy path) or
# ``pending`` (it returns a deferred that never fires), and ``<word>`` varies the
# netloc.  The harness calls ``robot_parser`` and prints ``OK`` when it returns
# without raising, else ``ERR:<exc>``; the correct behaviour is always ``OK``.  A
# failing test uses ``immediate`` (buggy: KeyError; fixed: OK); a passing test
# uses ``pending`` (identical on both builds).
# ======================================================================


_SCRAPY21_RUN_SRC = '''
def _run(self, mode, word):
    crawler = mock.MagicMock()
    crawler.settings = Settings()
    crawler.settings.set('ROBOTSTXT_OBEY', True)
    crawler.engine.download = mock.MagicMock()
    if mode == 'immediate':
        err = error.DNSLookupError('Robotstxt address not found')

        def side(request, spider):
            d = Deferred()
            d.errback(failure.Failure(err))
            return d
    else:

        def side(request, spider):
            return Deferred()

    crawler.engine.download.side_effect = side
    mw = RobotsTxtMiddleware(crawler)
    spider = mock.MagicMock()
    try:
        mw.robot_parser(Request('http://%s.local' % word), spider)
    except Exception as exc:
        return 'ERR:' + type(exc).__name__
    return 'OK'
'''


class Scrapy21API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            _word = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy21TestGenerator:
    def _word(self) -> str:
        return _rand_word(3, 8)


class Scrapy21SystemtestGenerator(SystemtestGenerator, Scrapy21TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"immediate {self._word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"pending {self._word()}", TestResult.PASSING


class Scrapy21UnittestGenerator(UnittestGenerator, Scrapy21TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="unittest", names=[ast.alias(name="mock")], level=0
            ),
            ast.ImportFrom(
                module="twisted.internet", names=[ast.alias(name="error")], level=0
            ),
            ast.ImportFrom(
                module="twisted.internet.defer",
                names=[ast.alias(name="Deferred")],
                level=0,
            ),
            ast.ImportFrom(
                module="twisted.python", names=[ast.alias(name="failure")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.downloadermiddlewares.robotstxt",
                names=[ast.alias(name="RobotsTxtMiddleware")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.http", names=[ast.alias(name="Request")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.settings", names=[ast.alias(name="Settings")], level=0
            ),
        ]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_SCRAPY21_RUN_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self._word()
        src = f"self.assertEqual('OK', self._run('immediate', {word!r}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self._word()
        src = f"self.assertEqual('OK', self._run('pending', {word!r}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_robotstxt: Grammar = clean_up(
    {
        "<start>": ["<mode> <word>"],
        "<mode>": ["immediate", "pending"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_robotstxt)


# ======================================================================
# bug_33: ``MediaPipeline.item_completed`` logged a failed media result with
# ``logger.error(..., extra={'spider': info.spider, 'failure': value})`` -- it
# stuffed the Twisted ``Failure`` into ``extra`` and never set ``exc_info``, so
# the emitted log record carried ``exc_info=None`` and the traceback was lost.
# The fix logs with ``exc_info=failure_to_exc_info(value)`` (and drops the
# ``failure`` extra).
#
# System-test format: ``<mode> <word>`` where ``<mode>`` is ``fail`` (call
# ``item_completed`` with a failed result -- the buggy path) or ``success`` (all
# results succeed).  The harness captures the ``scrapy.pipelines.media`` log and
# prints ``OK`` when the log matches the correct behaviour -- for ``fail`` exactly
# one ERROR record whose ``exc_info`` equals ``failure_to_exc_info(value)`` (the
# reference lives in ``scrapy.utils.log`` on both builds); for ``success`` no
# records -- else ``BAD``; the correct behaviour is always ``OK``.  A failing test
# uses ``fail`` (buggy: exc_info is None -> BAD; fixed: OK); a passing test uses
# ``success`` (identical on both builds).
# ======================================================================


_SCRAPY33_RUN_SRC = '''
def _run(self, mode, word):
    def _mocked_download_func(request, info):
        return None

    class _Capture(logging.Handler):
        def __init__(self):
            super().__init__()
            self.records = []

        def emit(self, record):
            self.records.append(record)

    pipe = MediaPipeline(download_func=_mocked_download_func)
    spider = Spider('%s.com' % word)
    pipe.open_spider(spider)
    info = pipe.spiderinfo
    item = dict(name=word)
    handler = _Capture()
    logger = logging.getLogger('scrapy.pipelines.media')
    logger.addHandler(handler)
    old_level = logger.level
    logger.setLevel(logging.DEBUG)
    try:
        if mode == 'fail':
            fail = Failure(Exception('boom %s' % word))
            pipe.item_completed([(True, 1), (False, fail)], item, info)
            ok = (len(handler.records) == 1
                  and handler.records[0].levelname == 'ERROR'
                  and handler.records[0].exc_info == failure_to_exc_info(fail))
        else:
            pipe.item_completed([(True, 1), (True, 2)], item, info)
            ok = len(handler.records) == 0
    finally:
        logger.removeHandler(handler)
        logger.setLevel(old_level)
    return 'OK' if ok else 'BAD'
'''


class Scrapy33API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _mode = process.args[2]
            _word = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy33TestGenerator:
    def _word(self) -> str:
        return _rand_word(3, 8)


class Scrapy33SystemtestGenerator(SystemtestGenerator, Scrapy33TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"fail {self._word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"success {self._word()}", TestResult.PASSING


class Scrapy33UnittestGenerator(UnittestGenerator, Scrapy33TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="logging")]),
            ast.ImportFrom(
                module="twisted.python.failure",
                names=[ast.alias(name="Failure")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.spiders", names=[ast.alias(name="Spider")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.pipelines.media",
                names=[ast.alias(name="MediaPipeline")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.utils.log",
                names=[ast.alias(name="failure_to_exc_info")],
                level=0,
            ),
        ]

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(_SCRAPY33_RUN_SRC).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self._word()
        src = f"self.assertEqual('OK', self._run('fail', {word!r}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        word = self._word()
        src = f"self.assertEqual('OK', self._run('success', {word!r}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_media_log: Grammar = clean_up(
    {
        "<start>": ["<mode> <word>"],
        "<mode>": ["fail", "success"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_media_log)


# ======================================================================
# bug_13: ``ImagesPipeline`` declared the default expiration as the class
# attribute ``EXPIRES = 0``.  A pipeline built with default settings therefore
# never expired downloaded images (``expires == 0`` instead of the intended 90
# days).  The fix sets ``EXPIRES = 90``.
#
# System-test format: ``<mode> <n>`` where ``<mode>`` is ``default`` (build an
# ``ImagesPipeline`` from empty settings -- the buggy path, ``expires`` comes from
# the class attribute) or ``custom`` (build it ``from_settings`` with
# ``IMAGES_EXPIRES=<n>``, which overrides the class attribute on both builds).
# The harness prints ``OK:<pipe.expires>`` or ``ERR:<exc>``; the correct
# behaviour is ``OK:90`` for ``default`` and ``OK:<n>`` for ``custom``.  A failing
# test uses ``default`` (buggy: expires 0; fixed: 90); a passing test uses
# ``custom`` (identical on both builds).
# ======================================================================


class Scrapy13API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            n = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK:90" if mode == "default" else f"OK:{n}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Scrapy13TestGenerator:
    def _n(self) -> int:
        # any value other than the fixed default (90)
        return random.randint(100, 99999)


class Scrapy13SystemtestGenerator(SystemtestGenerator, Scrapy13TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"default {self._n()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"custom {self._n()}", TestResult.PASSING


class Scrapy13UnittestGenerator(UnittestGenerator, Scrapy13TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="tempfile")]),
            ast.ImportFrom(
                module="scrapy.settings", names=[ast.alias(name="Settings")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.pipelines.images",
                names=[ast.alias(name="ImagesPipeline")],
                level=0,
            ),
        ]

    @staticmethod
    def _assert(mode: str, n: int) -> List[ast.stmt]:
        if mode == "default":
            src = (
                f"tmp = tempfile.mkdtemp(prefix='img{n}_')\n"
                "pipe = ImagesPipeline(tmp, settings=Settings())\n"
                "self.assertEqual(90, pipe.expires)\n"
            )
        else:
            src = (
                "tmp = tempfile.mkdtemp()\n"
                f"pipe = ImagesPipeline.from_settings("
                f"Settings({{'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': {n}}}))\n"
                f"self.assertEqual({n}, pipe.expires)\n"
            )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("default", self._n())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("custom", self._n())
        return test, TestResult.PASSING


grammar_images_expires: Grammar = clean_up(
    {
        "<start>": ["<mode> <int>"],
        "<mode>": ["default", "custom"],
        "<int>": ["<nonzero><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<nonzero>": srange("123456789"),
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_images_expires)


# ======================================================================
# bug_24: scrapy.core.downloader.handlers.http11.TunnelingTCP4ClientEndpoint
# (used for HTTPS downloads through an HTTP proxy) was written for Python 2
# and mishandled bytes on Python 3.  ``requestTunnel`` built the CONNECT
# request as a ``str`` (``'CONNECT %s:%s HTTP/1.1\r\n'``) and wrote that str
# to the transport, and ``_responseMatcher`` was a ``str`` regex matched
# against the proxy's ``bytes`` response (raising ``TypeError``).  The fix
# builds the request as ``bytes`` and compiles ``_responseMatcher`` as a
# ``bytes`` pattern.  (The canonical pytest is marked FAILING because it
# spins up a live Twisted HTTPS-proxy fixture that is environment specific;
# the code fix itself IS present on the fixed checkout, so the diversity
# tests below still distinguish buggy from fixed.)
#
# System-test format:  ``<mode> <host> <port>``.  ``mode == "request"`` (the
# fault trigger) builds the CONNECT request and prints the *type* written to
# the transport; the oracle expects ``bytes`` (buggy prints ``str``).
# ``mode == "port"`` prints the stored tunneled port, an invariant that holds
# on both builds.
# ======================================================================


class Scrapy24API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            port = process.args[4]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "request":
            expected = "bytes"
        elif mode == "port":
            expected = port
        else:
            return TestResult.UNDEFINED, "Malformed test input"
        marker = None
        for line in process.stdout.decode("utf8").splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if process.returncode == 0 and marker == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {marker!r}"


class Scrapy24TestGenerator:
    @staticmethod
    def _host() -> str:
        labels = [_rand_word(3, 7) for _ in range(random.randint(2, 3))]
        return ".".join(labels)

    @staticmethod
    def _port() -> int:
        return random.randint(1, 65535)


class Scrapy24SystemtestGenerator(SystemtestGenerator, Scrapy24TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"request {self._host()} {self._port()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"port {self._host()} {self._port()}", TestResult.PASSING


_SCRAPY24_UTILS = '''
def _t4p_tunnel_request_type(host, port):
    from scrapy.core.downloader.handlers.http11 import TunnelingTCP4ClientEndpoint
    from twisted.internet import reactor
    class _FT(object):
        def __init__(self):
            self.written = None
        def write(self, data):
            self.written = data
    class _FP(object):
        def __init__(self):
            self.transport = _FT()
            self.dataReceived = None
    endpoint = TunnelingTCP4ClientEndpoint(
        reactor, host.encode('ascii'), port, ('proxy.example', 8080, None), None)
    protocol = _FP()
    endpoint.requestTunnel(protocol)
    return type(protocol.transport.written).__name__


def _t4p_tunnel_port(host, port):
    from scrapy.core.downloader.handlers.http11 import TunnelingTCP4ClientEndpoint
    from twisted.internet import reactor
    endpoint = TunnelingTCP4ClientEndpoint(
        reactor, host.encode('ascii'), port, ('proxy.example', 8080, None), None)
    return endpoint._tunneledPort
'''


class Scrapy24UnittestGenerator(UnittestGenerator, Scrapy24TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_SCRAPY24_UTILS).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        host, port = self._host(), self._port()
        src = f"self.assertEqual('bytes', _t4p_tunnel_request_type({host!r}, {port}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        host, port = self._host(), self._port()
        src = f"self.assertEqual({port}, _t4p_tunnel_port({host!r}, {port}))\n"
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


grammar_tunneling: Grammar = clean_up(
    {
        "<start>": ["<mode> <host> <port>"],
        "<mode>": ["request", "port"],
        "<host>": ["<label>", "<label>.<host>"],
        "<label>": ["<char><chars>"],
        "<chars>": ["", "<char><chars>"],
        "<char>": srange(string.ascii_lowercase + string.digits),
        "<port>": ["<nonzero><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<nonzero>": srange("123456789"),
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_tunneling)


# ======================================================================
# bug_28: ``RFPDupeFilter.__init__`` opened ``requests.seen`` in ``'a+'`` mode
# and immediately iterated over it to load previously-seen fingerprints.  In
# append mode the file offset starts at EOF, so the iteration read nothing and
# a freshly-constructed filter pointed at an existing job dir "forgot" every
# persisted request.  The fix inserts ``self.file.seek(0)`` before loading.
#
# System-test format: ``<mode> <url>`` where ``<mode>`` is ``persist`` or
# ``same``.  ``persist`` writes the url with one filter, then reloads a second
# filter from the same dir and reports whether the reloaded filter recognises
# the url (buggy: False; fixed: True).  ``same`` reports the second lookup
# within a single filter instance (True on both builds).  Every scenario is
# expected to end up seen (True), so ``persist`` distinguishes the fault.
# ======================================================================


grammar_dupefilter: Grammar = clean_up(
    {
        "<start>": ["<mode> <url>"],
        "<mode>": ["persist", "same"],
        "<url>": ["http://scrapytest.org/<path>"],
        "<path>": ["<c>", "<c><path>"],
        "<c>": srange(string.ascii_letters + string.digits + "/-_."),
    }
)

assert is_valid_grammar(grammar_dupefilter)


class Scrapy28API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        # In both modes a duplicate of the recorded request must be recognised.
        expected = "True"
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Scrapy28TestGenerator:
    @staticmethod
    def _url() -> str:
        return (
            "http://scrapytest.org/"
            + _rand_word(4, 10)
            + "/"
            + str(random.randint(1, 1000000))
        )


class Scrapy28SystemtestGenerator(SystemtestGenerator, Scrapy28TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"persist {self._url()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"same {self._url()}", TestResult.PASSING


class Scrapy28UnittestGenerator(UnittestGenerator, Scrapy28TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="tempfile")]),
            ast.Import(names=[ast.alias(name="shutil")]),
            ast.ImportFrom(
                module="scrapy.dupefilters",
                names=[ast.alias(name="RFPDupeFilter")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="Request")],
                level=0,
            ),
        ]

    def _failing_src(self, url: str) -> str:
        return (
            "path = tempfile.mkdtemp()\n"
            "try:\n"
            "    df = RFPDupeFilter(path)\n"
            "    df.open()\n"
            f"    df.request_seen(Request({url!r}))\n"
            "    df.close('finished')\n"
            "    df2 = RFPDupeFilter(path)\n"
            "    df2.open()\n"
            f"    seen = df2.request_seen(Request({url!r}))\n"
            "    df2.close('finished')\n"
            "    self.assertTrue(seen)\n"
            "finally:\n"
            "    shutil.rmtree(path)\n"
        )

    def _passing_src(self, url: str) -> str:
        return (
            "path = tempfile.mkdtemp()\n"
            "try:\n"
            "    df = RFPDupeFilter(path)\n"
            "    df.open()\n"
            f"    df.request_seen(Request({url!r}))\n"
            f"    seen = df.request_seen(Request({url!r}))\n"
            "    df.close('finished')\n"
            "    self.assertTrue(seen)\n"
            "finally:\n"
            "    shutil.rmtree(path)\n"
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._failing_src(self._url())).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._passing_src(self._url())).body
        return test, TestResult.PASSING


# ======================================================================
# bug_14: ``is_gzipped`` compared the raw ``Content-Type`` header against the
# exact byte strings ``b'application/x-gzip'``/``b'application/gzip'``.  A
# header carrying a charset parameter (``application/x-gzip;charset=utf-8``) or
# different casing (``application/X-Gzip``) therefore was NOT recognised as
# gzip.  The fix matches with the case-insensitive regex
# ``^application/(x-)?gzip\b`` instead.
#
# System-test format: the ``Content-Type`` value (a single token, no spaces).
# The harness prints ``is_gzipped(Response(...))``; the oracle recomputes the
# correct (fixed) answer with the same regex.  Failing tests use charset/case
# variants (buggy False, fixed True); passing tests use exact gzip types or
# clearly non-gzip types (identical on both builds).
# ======================================================================


_GZIP_RE = re.compile(br"^application/(x-)?gzip\b", re.I)


def _gzip_expected(ctype: str) -> bool:
    return _GZIP_RE.search(ctype.encode("utf-8")) is not None


grammar_gzip: Grammar = clean_up(
    {
        "<start>": ["<chars>"],
        "<chars>": ["<char>", "<char><chars>"],
        "<char>": srange(string.ascii_letters + string.digits + "/-;=+._"),
    }
)

assert is_valid_grammar(grammar_gzip)


class Scrapy14API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            ctype = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(_gzip_expected(ctype))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Scrapy14TestGenerator:
    @staticmethod
    def _failing() -> str:
        return random.choice(
            [
                f"application/x-gzip;charset={_rand_word()}",
                f"application/gzip;charset={_rand_word()}",
                f"application/X-GZIP;charset={_rand_word()}",
                "application/X-Gzip",
                "APPLICATION/GZIP",
                "Application/GZip",
            ]
        )

    @staticmethod
    def _passing() -> str:
        return random.choice(
            [
                "application/x-gzip",
                "application/gzip",
                f"text/{_rand_word()}",
                f"image/{_rand_word()}",
                f"application/gzip{_rand_word()}",
            ]
        )


class Scrapy14SystemtestGenerator(SystemtestGenerator, Scrapy14TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self._failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self._passing(), TestResult.PASSING


class Scrapy14UnittestGenerator(UnittestGenerator, Scrapy14TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="Response")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.utils.gz",
                names=[ast.alias(name="is_gzipped")],
                level=0,
            ),
        ]

    @staticmethod
    def _src(ctype: str) -> str:
        expected = _gzip_expected(ctype)
        return (
            f"response = Response('http://www.example.com', "
            f"headers={{'Content-Type': {ctype!r}}})\n"
            f"self.assertEqual({expected!r}, is_gzipped(response))\n"
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(self._failing())).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(self._passing())).body
        return test, TestResult.PASSING


# ======================================================================
# bug_12: ``Selector.__init__`` silently accepted BOTH a ``response`` and a
# ``text`` argument (``text`` won, ``response`` was ignored), masking a caller
# mistake.  The fix raises ``ValueError('... received both response and text')``
# when both are provided.
#
# System-test format: ``<mode> <html>`` with ``<mode>`` in ``both``/``text``/
# ``response`` (``type='html'`` is always supplied so the base Selector builds
# on this version).  The harness reports ``VALUEERROR``/``NOERROR``; the oracle
# expects ``VALUEERROR`` only for ``both``.  Failing tests use ``both`` (buggy:
# no error; fixed: ValueError); passing tests use a single argument.
# ======================================================================


grammar_selector: Grammar = clean_up(
    {
        "<start>": ["<mode> <html>"],
        "<mode>": ["both", "text", "response"],
        "<html>": ["<chars>"],
        "<chars>": ["<char>", "<char><chars>"],
        "<char>": srange(string.ascii_letters + string.digits + "<>/"),
    }
)

assert is_valid_grammar(grammar_selector)


class Scrapy12API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "VALUEERROR" if mode == "both" else "NOERROR"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Scrapy12TestGenerator:
    @staticmethod
    def _html() -> str:
        return f"<html><body><p>{_rand_word(3, 9)}</p></body></html>"


class Scrapy12SystemtestGenerator(SystemtestGenerator, Scrapy12TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"both {self._html()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(["text", "response"])
        return f"{mode} {self._html()}", TestResult.PASSING


class Scrapy12UnittestGenerator(UnittestGenerator, Scrapy12TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.selector",
                names=[ast.alias(name="Selector")],
                level=0,
            ),
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="TextResponse")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        html = self._html()
        src = (
            "resp = TextResponse(url='http://example.com', "
            f"body={html.encode('utf-8')!r}, encoding='utf-8')\n"
            "with self.assertRaises(ValueError):\n"
            f"    Selector(response=resp, text={html!r}, type='html')\n"
        )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        html = self._html()
        if random.random() < 0.5:
            src = (
                f"sel = Selector(text={html!r}, type='html')\n"
                "self.assertIsNotNone(sel)\n"
            )
        else:
            src = (
                "resp = TextResponse(url='http://example.com', "
                f"body={html.encode('utf-8')!r}, encoding='utf-8')\n"
                "sel = Selector(response=resp, type='html')\n"
                "self.assertIsNotNone(sel)\n"
            )
        test = self.get_empty_test()
        test.body = ast.parse(src).body
        return test, TestResult.PASSING


# ======================================================================
# bug_9: ``MailSender.send`` joined the recipient list with
# ``COMMASPACE.join(to)`` without first normalising a bare string into a list.
# Passing a single address string therefore produced a ``To`` header made of
# the address' individual characters (``t, e, s, t, ...``).  The fix runs
# ``to``/``cc`` through ``arg_to_iter`` before joining.
#
# System-test format: ``<mode> <email>`` with ``<mode>`` in ``single``/``list``.
# The harness sends with ``debug=True`` and a ``_callback`` capturing the built
# message, then prints ``msg['To']``; the oracle expects it to equal the
# address.  ``single`` distinguishes (buggy garbles it); ``list`` agrees on
# both builds.
# ======================================================================


grammar_mail: Grammar = clean_up(
    {
        "<start>": ["<mode> <email>"],
        "<mode>": ["single", "list"],
        "<email>": ["<chars>@<chars>.<tld>"],
        "<chars>": ["<char>", "<char><chars>"],
        "<char>": srange(string.ascii_lowercase + string.digits),
        "<tld>": ["org", "com", "net", "io"],
    }
)

assert is_valid_grammar(grammar_mail)


class Scrapy9API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            email = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == email:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {email}, but was {out!r}"


class Scrapy9TestGenerator:
    @staticmethod
    def _email() -> str:
        return (
            f"{_rand_word(3, 8)}@{_rand_word(3, 8)}."
            + random.choice(["org", "com", "net", "io"])
        )


class Scrapy9SystemtestGenerator(SystemtestGenerator, Scrapy9TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"single {self._email()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"list {self._email()}", TestResult.PASSING


class Scrapy9UnittestGenerator(UnittestGenerator, Scrapy9TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.mail",
                names=[ast.alias(name="MailSender")],
                level=0,
            )
        ]

    @staticmethod
    def _src(to_expr: str, email: str) -> str:
        return (
            "captured = {}\n"
            "def cb(**kw):\n"
            "    captured['msg'] = kw['msg']\n"
            "ms = MailSender(debug=True)\n"
            f"ms.send(to={to_expr}, subject='subject', body='body', _callback=cb)\n"
            f"self.assertEqual({email!r}, captured['msg']['To'])\n"
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        email = self._email()
        test = self.get_empty_test()
        test.body = ast.parse(self._src(repr(email), email)).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        email = self._email()
        test = self.get_empty_test()
        test.body = ast.parse(self._src(repr([email]), email)).body
        return test, TestResult.PASSING


# Permissive line grammar (parses any printable input, spaces included) used by
# multi-token subjects whose precise structure is impractical to encode.
grammar_printable: Grammar = clean_up(
    {
        "<start>": ["<chars>"],
        "<chars>": ["", "<char><chars>"],
        "<char>": srange(string.printable),
    }
)

assert is_valid_grammar(grammar_printable)


# ======================================================================
# bug_25: ``_get_form_url`` returned ``form.action or form.base_url`` and
# ``_get_form`` rooted the parsed tree at ``response.url``, so a ``<base href>``
# in the document was ignored and relative form actions were resolved against
# the wrong base.  The fix roots at ``get_base_url(response)`` and returns
# ``urljoin(form.base_url, form.action)``.
#
# System-test format: ``<expected> <response_url> <base_href> <action>`` where
# ``<base_href>`` may be ``none``.  The harness builds an HTML page with the
# given base tag + form action and prints ``FormRequest.from_response(...).url``;
# the oracle compares it to ``<expected>`` (the fixed result).  Failing tests
# use a ``<base>`` + relative action (buggy resolves against response.url);
# passing tests use an absolute action with no base (identical on both builds).
# ======================================================================


class Scrapy25API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            expected = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Scrapy25TestGenerator:
    @staticmethod
    def _failing() -> Tuple[str, str, str, str]:
        response_url = f"http://{_rand_word()}.com/"
        base_href = f"http://{_rand_word()}.org/"
        action = _rand_word() + random.choice(["", ".html", "/sub"])
        expected = urljoin(base_href, action)
        return expected, response_url, base_href, action

    @staticmethod
    def _passing() -> Tuple[str, str, str, str]:
        response_url = f"http://{_rand_word()}.com/"
        action = f"http://{_rand_word()}.net/{_rand_word()}"
        expected = action  # absolute action, no base -> same on both builds
        return expected, response_url, "none", action


class Scrapy25SystemtestGenerator(SystemtestGenerator, Scrapy25TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self._failing()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self._passing()), TestResult.PASSING


class Scrapy25UnittestGenerator(UnittestGenerator, Scrapy25TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="HtmlResponse"), ast.alias(name="FormRequest")],
                level=0,
            )
        ]

    @staticmethod
    def _src(expected: str, response_url: str, base_href: str, action: str) -> str:
        base_tag = "" if base_href == "none" else f'<base href="{base_href}">'
        body = (
            f"<html><head>{base_tag}</head><body>"
            f'<form action="{action}"></form></body></html>'
        )
        return (
            f"response = HtmlResponse(url={response_url!r}, "
            f"body={body.encode('utf-8')!r}, encoding='utf-8')\n"
            "req = FormRequest.from_response(response)\n"
            f"self.assertEqual({expected!r}, req.url)\n"
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(*self._failing())).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(*self._passing())).body
        return test, TestResult.PASSING


# ======================================================================
# bug_38: ``_get_clickable`` used an XPath that only matched
# ``input``/``button`` elements with ``type="submit"`` (or type-less buttons),
# so an image submit control (``<input type="image">``) was never treated as a
# clickable and its ``name=value`` pair was dropped from the submitted form.
# The fix extends the XPath to ``input[type in (submit, image)]``.
#
# System-test format:
# ``<expected> <clicktype> <t_name> <t_val> <c_name> <c_val>`` with
# ``<clicktype>`` in ``image``/``submit``.  The harness builds a form with a
# text field plus one clickable of the given type, submits it, and prints the
# canonical (sorted) query string; the oracle compares to ``<expected>``.
# Failing tests use ``image`` (buggy drops the control); passing tests use
# ``submit`` (matched on both builds).
# ======================================================================


class Scrapy38API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            expected = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Scrapy38TestGenerator:
    @staticmethod
    def _spec(clicktype: str) -> Tuple[str, str, str, str, str, str]:
        names = set()

        def uw():
            while True:
                w = _rand_word(3, 7)
                if w not in names:
                    names.add(w)
                    return w

        t_name, t_val, c_name, c_val = uw(), _rand_word(3, 7), uw(), _rand_word(3, 7)
        params = {t_name: t_val, c_name: c_val}
        expected = "&".join(f"{k}={params[k]}" for k in sorted(params))
        return expected, clicktype, t_name, t_val, c_name, c_val


class Scrapy38SystemtestGenerator(SystemtestGenerator, Scrapy38TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self._spec("image")), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self._spec("submit")), TestResult.PASSING


class Scrapy38UnittestGenerator(UnittestGenerator, Scrapy38TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="scrapy.http",
                names=[ast.alias(name="HtmlResponse"), ast.alias(name="FormRequest")],
                level=0,
            ),
            ast.ImportFrom(
                module="urllib.parse",
                names=[ast.alias(name="urlparse"), ast.alias(name="parse_qs")],
                level=0,
            ),
        ]

    @staticmethod
    def _src(
        expected: str,
        clicktype: str,
        t_name: str,
        t_val: str,
        c_name: str,
        c_val: str,
    ) -> str:
        body = (
            f'<form><input type="text" name="{t_name}" value="{t_val}">'
            f'<input type="{clicktype}" name="{c_name}" value="{c_val}"></form>'
        )
        return (
            "response = HtmlResponse(url='http://example.com', "
            f"body={body.encode('utf-8')!r}, encoding='utf-8')\n"
            "req = FormRequest.from_response(response)\n"
            "params = parse_qs(urlparse(req.url).query)\n"
            "canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) "
            "for v in params[k])\n"
            f"self.assertEqual({expected!r}, canon)\n"
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(*self._spec("image"))).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(*self._spec("submit"))).body
        return test, TestResult.PASSING


# ======================================================================
# bug_6: ``ImagesPipeline.convert_image`` handled ``PNG``/``RGBA`` images by
# compositing them onto a white background, but a palette-mode (``P``) image
# with transparency fell through to a plain ``convert('RGB')`` that discarded
# the alpha channel, so transparent regions kept their raw palette colour
# instead of being blended onto white.  The fix adds a dedicated ``P`` branch
# that composites like the ``RGBA`` case.
#
# System-test format: ``<mode> <r> <g> <b> <a>`` with ``<mode>`` in
# ``palette``/``rgba``.  The harness builds a solid ``RGBA`` image (optionally
# converted to ``P``), runs ``convert_image`` and prints the resulting ``R,G,B``
# colour; the oracle recomputes the correct alpha-over-white blend.  ``palette``
# distinguishes the fault (buggy keeps the raw colour); ``rgba`` agrees on both
# builds.
# ======================================================================


def _blend_over_white(r: int, g: int, b: int, a: int) -> Tuple[int, int, int]:
    # Matches PIL's integer alpha compositing onto a white background.
    return tuple(round((c * a + 255 * (255 - a)) / 255) for c in (r, g, b))


class Scrapy6API(ScrapyAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            r, g, b, a = (int(process.args[i]) for i in range(3, 7))
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = ",".join(map(str, _blend_over_white(r, g, b, a)))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, ""
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Scrapy6TestGenerator:
    @staticmethod
    def _failing() -> Tuple[str, int, int, int, int]:
        r, g, b = (random.randint(0, 200) for _ in range(3))
        a = random.randint(30, 200)
        return "palette", r, g, b, a

    @staticmethod
    def _passing() -> Tuple[str, int, int, int, int]:
        r, g, b = (random.randint(0, 255) for _ in range(3))
        a = random.randint(30, 255)
        return "rgba", r, g, b, a


class Scrapy6SystemtestGenerator(SystemtestGenerator, Scrapy6TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return " ".join(map(str, self._failing())), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return " ".join(map(str, self._passing())), TestResult.PASSING


class Scrapy6UnittestGenerator(UnittestGenerator, Scrapy6TestGenerator):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="io", names=[ast.alias(name="BytesIO")], level=0
            ),
            ast.ImportFrom(
                module="tempfile", names=[ast.alias(name="mkdtemp")], level=0
            ),
            ast.ImportFrom(
                module="PIL", names=[ast.alias(name="Image")], level=0
            ),
            ast.ImportFrom(
                module="scrapy.pipelines.images",
                names=[ast.alias(name="ImagesPipeline")],
                level=0,
            ),
        ]

    @staticmethod
    def _src(mode: str, r: int, g: int, b: int, a: int) -> str:
        expected = _blend_over_white(r, g, b, a)
        convert = "im = im.convert('P')\n" if mode == "palette" else ""
        return (
            "buf = BytesIO()\n"
            f"Image.new('RGBA', (50, 50), ({r}, {g}, {b}, {a})).save(buf, 'PNG')\n"
            "buf.seek(0)\n"
            "im = Image.open(buf)\n"
            f"{convert}"
            "pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)\n"
            "conv, _ = pipeline.convert_image(im)\n"
            "self.assertEqual('RGB', conv.mode)\n"
            f"self.assertEqual([(2500, {expected!r})], conv.getcolors())\n"
        )

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(*self._failing())).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = ast.parse(self._src(*self._passing())).body
        return test, TestResult.PASSING
