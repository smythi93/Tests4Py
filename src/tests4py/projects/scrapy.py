from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Scrapy(Project):
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
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="scrapy",
            github_url="https://github.com/scrapy/scrapy",
            status=Status.OK,
            cause="N.A.",
            python_version="3.8.3",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.UNITTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version="3.8.4",
            python_fallback_version="3.8.4",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


def register():
    Scrapy(
        bug_id=1,
        buggy_commit_id="c57512fa669e6f6b1b766a7639206a380f0d10ce",
        fixed_commit_id="9d9dea0d69709ef0f7aef67ddba1bd7bda25d273",
        test_file=[Path("tests", "test_spidermiddleware_offsite.py")],
        test_cases=[
            "tests.test_spidermiddleware_offsite.TestOffsiteMiddleware4._get_spiderargs",
            "tests.test_spidermiddleware_offsite.TestOffsiteMiddleware4.test_process_spider_output",
        ],
    )
    Scrapy(
        bug_id=2,
        buggy_commit_id="f02c3d1dcf3e4880388d19e961e7911be5dc54ff",
        fixed_commit_id="439a3e59b8e858441f8d97dbc32f398db392330d",
        test_file=[Path("tests", "test_utils_datatypes.py")],
        test_cases=[
            "tests.test_utils_datatypes.LocalCacheTest.test_cache_without_limit"
        ],
    )
    Scrapy(
        bug_id=3,
        buggy_commit_id="be2e910dd06ba4904e7b10eb5a7e3251e8dab099",
        fixed_commit_id="66cbceeb0a9104fc0fa238898e38d0d9ce9cbcf6",
        test_file=[Path("tests", "test_downloadermiddleware_redirect.py")],
        test_cases=[
            "tests.test_downloadermiddleware_redirect.RedirectMiddlewareTest.test_redirect_302_relative"
        ],
    )
    Scrapy(
        bug_id=4,
        buggy_commit_id="c8f3d07e86dd41074971b5423fb932c2eda6db1e",
        fixed_commit_id="16dad81715d3970149c0cf7a318e73a0d84be1ff",
        test_file=[Path("tests", "test_contracts.py")],
        test_cases=["tests.test_contracts.ContractsManagerTest.test_errback"],
    )
    Scrapy(
        bug_id=5,
        buggy_commit_id="426da0ed07637e7efbcfb0fe49546e187d5d7f67",
        fixed_commit_id="acd2b8d43b5ebec7ffd364b6f335427041a0b98d",
        test_file=[Path("tests", "test_http_response.py")],
        test_cases=["tests.test_http_response.BaseResponseTest.test_follow_None_url"],
    )
    Scrapy(
        bug_id=6,
        buggy_commit_id="8aa2e4f9976d31bbe3a0014b4f1f96ace1b87043",
        fixed_commit_id="25f609e2a3c27ca7d7d98dbfddb2c049735935bb",
        test_file=[Path("tests", "test_pipeline_images.py")],
        test_cases=[
            "tests.test_pipeline_images.ImagesPipelineTestCase.test_convert_image"
        ],
    )
    Scrapy(
        bug_id=7,
        buggy_commit_id="e1ceaf3b5fa29326f032c4ed3f50943384b9e63d",
        fixed_commit_id="074caf434e255bc96f106e57e3e288028f372485",
        test_file=[Path("tests", "test_http_request.py")],
        test_cases=["tests.test_http_request.FormRequestTest.test_spaces_in_action"],
    )
    Scrapy(
        bug_id=8,
        buggy_commit_id="f2f9350c47db73bdfb60773601b59b0633e1595a",
        fixed_commit_id="4e765acaed7a914630ee5320fa6f6523890a2b9d",
        test_file=[Path("tests", "test_item.py")],
        test_cases=[
            "tests.test_item.ItemMetaTest.test_new_method_propagates_classcell",
            "tests.test_item.ItemMetaClassCellRegression.test_item_meta_classcell_regression",
        ],
    )
    Scrapy(
        bug_id=9,
        buggy_commit_id="a9c69458ff1667cc4d20ba25bb6a0dd9a5a08ce6",
        fixed_commit_id="ff3aec661355a82a6f77355a95e1f391fa586c2b",
        test_file=[Path("tests", "test_mail.py")],
        test_cases=["tests.test_mail.MailSenderTest.test_send_single_values_to_and_cc"],
    )
    Scrapy(
        bug_id=10,
        buggy_commit_id="6cc83c041eac36e7688dbd9c4c55487a43b622e0",
        fixed_commit_id="db408528928b2d15043593032913fe40d6eb6783",
        test_file=[Path("tests", "test_downloadermiddleware_redirect.py")],
        test_cases=[
            "tests.test_downloadermiddleware_redirect.RedirectMiddlewareTest.test_latin1_location",
            "tests.test_downloadermiddleware_redirect.RedirectMiddlewareTest.test_utf8_location",
        ],
    )
    Scrapy(
        bug_id=11,
        buggy_commit_id="241bd00e76df142a24699819f8496bdec8f5c83a",
        fixed_commit_id="9de6f1ca757b7f200d15e94840c9d431cf202276",
        test_file=[Path("tests", "test_utils_gz.py")],
        test_cases=["tests.test_utils_gz.GunzipTest.test_gunzip_illegal_eof"],
    )
    Scrapy(
        bug_id=12,
        buggy_commit_id="34e7dadf38ba1796094c0c76e92ea8d9837681cc",
        fixed_commit_id="2c9a38d1f54a12c33d7c9a19e021c840c4a32dee",
        test_file=[Path("tests", "test_selector.py")],
        test_cases=["tests.test_selector.SelectorTestCase.test_selector_bad_args"],
    )
    Scrapy(
        bug_id=13,
        buggy_commit_id="fa78849e335994a1617ed63221a70940c21cca20",
        fixed_commit_id="414857a593ad5b82fa21d6344928f43f93dc9f14",
        test_file=[Path("tests", "test_pipeline_images.py")],
        test_cases=["tests.test_pipeline_images.ImagesPipelineTestCaseCustomSettings"],
    )
    Scrapy(
        bug_id=14,
        buggy_commit_id="b7553d921afe356ec858bb1d2e5b1702df05ea24",
        fixed_commit_id="d43a35735a062a4260b002cfbcd3236c77ef9399",
        test_file=[Path("tests", "test_utils_gz.py")],
        test_cases=[
            "tests.test_utils_gz.GunzipTest.test_is_gzipped_case_insensitive",
            "tests.test_utils_gz.GunzipTest.test_is_gzipped_with_charset",
        ],
    )
    Scrapy(
        bug_id=15,
        buggy_commit_id="b7925e42202d79d2ba9d00b6aded3a451c92fe81",
        fixed_commit_id="1aec5200bc81493623f2a4e077b4e80e104e47d5",
        test_file=[Path("tests", "test_utils_url.py")],
        test_cases=[
            "tests.test_utils_url.CanonicalizeUrlTest.test_canonicalize_url_idna_exceptions"
        ],
    )
    Scrapy(
        bug_id=16,
        buggy_commit_id="73a5571c6044d5aea47b4f973e325c2f3d4e25dc",
        fixed_commit_id="68dedf54cb27847f6d035099b61aa06226549fad",
        test_file=[Path("tests", "test_utils_url.py")],
        test_cases=[
            "tests.test_utils_url.CanonicalizeUrlTest.test_canonicalize_url_unicode_query_string",
            "tests.test_utils_url.CanonicalizeUrlTest.test_normalize_percent_encoding_in_paths",
            "tests.test_utils_url.CanonicalizeUrlTest.test_normalize_percent_encoding_in_query_arguments",
            "tests.test_utils_url.CanonicalizeUrlTest.test_canonicalize_idns",
            "tests.test_utils_url.CanonicalizeUrlTest.test_canonicalize_urlparsed",
            "tests.test_utils_url.CanonicalizeUrlTest.test_canonicalize_parse_url",
        ],
    )
    Scrapy(
        bug_id=17,
        buggy_commit_id="ebef6d7c6dd8922210db8a4a44f48fe27ee0cd16",
        fixed_commit_id="65c7c05060fd2d1fc161d4904243d5e0b31e202b",
        test_file=[Path("tests", "test_utils_response.py")],
        test_cases=[
            "tests.test_utils_response.ResponseUtilsTest.test_response_status_message"
        ],
    )
    Scrapy(
        bug_id=18,
        buggy_commit_id="41588397c04356f2b0c393b61ed68271a08d6ccd",
        fixed_commit_id="cabed6f183cfb2ab778c57be8c75802fec5e54d4",
        test_file=[Path("tests", "test_responsetypes.py")],
        test_cases=[
            "tests.test_responsetypes.ResponseTypesTest.test_from_content_disposition"
        ],
    )
    Scrapy(
        bug_id=19,
        buggy_commit_id="e328a9b9dfa4fbc79c59ed4f45f757e998301c31",
        fixed_commit_id="1f743996ff00a7b728d59b93d0967e1eb50072f0",
        test_file=[Path("tests", "test_http_cookies.py")],
        test_cases=[
            "tests.test_http_cookies.WrappedRequestTest.test_get_full_url",
            "tests.test_http_cookies.WrappedRequestTest.test_get_host",
            "tests.test_http_cookies.WrappedRequestTest.test_get_type",
            "tests.test_http_cookies.WrappedRequestTest.test_get_origin_req_host",
        ],
    )
    Scrapy(
        bug_id=20,
        buggy_commit_id="e328a9b9dfa4fbc79c59ed4f45f757e998301c31",
        fixed_commit_id="25c56159b86288311630cc0cf6db9d755aeeff1e",
        test_file=[Path("tests", "test_spider.py")],
        test_cases=[
            "tests.test_spider.SitemapSpiderTest.test_get_sitemap_urls_from_robotstxt"
        ],
    )
    Scrapy(
        bug_id=21,
        buggy_commit_id="43a53aca1207a82b663fe7a90c375546ce340a8e",
        fixed_commit_id="a8a6f050e71fbb7881076a8d6e2867e868d26016",
        test_file=[Path("tests", "test_downloadermiddleware_robotstxt.py")],
        test_cases=[
            "tests.test_downloadermiddleware_robotstxt.RobotsTxtMiddlewareTest.test_robotstxt_immediate_error"
        ],
    )
    Scrapy(
        bug_id=22,
        buggy_commit_id="a35aec71e96b0c0288c370afa425e8e700dca8b3",
        fixed_commit_id="bb2cf7c0d7199fffe0aa100e5c8a51c6b4b82fc2",
        test_file=[Path("tests", "test_exporters.py")],
        test_cases=[
            "tests.test_exporters.XmlItemExporterTest.test_nonstring_types_item"
        ],
    )
    Scrapy(
        bug_id=23,
        buggy_commit_id="c9e046d11dc63fbdc40effce4e6d15bcecd44593",
        fixed_commit_id="f042ad0f39594d59a1a2032e6294ff1890638138",
        test_file=[Path("tests", "test_downloadermiddleware_httpproxy.py")],
        test_cases=[
            "tests.test_downloadermiddleware_httpproxy.TestDefaultHeadersMiddleware.test_proxy_auth",
            "tests.test_downloadermiddleware_httpproxy.TestDefaultHeadersMiddleware.test_proxy_auth_empty_passwd",
        ],
    )
    Scrapy(
        bug_id=24,
        buggy_commit_id="98c060d0b2cc76934e16abc03a033f21850fd565",
        fixed_commit_id="0f527849f2e8eddaf5d756b061699f2eca522a18",
        test_file=[Path("tests", "test_downloader_handlers.py")],
        test_cases=[
            "tests.test_downloader_handlers.HttpProxyTestCase.test_download_with_proxy_https_timeout"
        ],
    )
    Scrapy(
        bug_id=25,
        buggy_commit_id="57f87b95d4d705f8afdd8fb9f7551033a7d88ee2",
        fixed_commit_id="9548691fdd47077a53f85daace091ef4af599cb9",
        test_file=[Path("tests", "test_http_request.py")],
        test_cases=[
            "tests.test_http_request.FormRequestTest.test_html_base_form_action"
        ],
    )
    Scrapy(
        bug_id=26,
        buggy_commit_id="f249b309ab779b5ab518f54f309d7a4ac6661ec7",
        fixed_commit_id="03f1720afb4a437314659a306286f440df664a0b",
        test_file=[Path("tests", "test_settings", "__init__.py")],
        test_cases=["tests.test_settings.__init__.BaseSettingsTest.test_getcomposite"],
    )
    Scrapy(
        bug_id=27,
        buggy_commit_id="280eab241680c93a763a3ef3a9ccd0c257259ca0",
        fixed_commit_id="d164398a27736f75286cc435eca69b06ff7c1c06",
        test_file=[Path("tests", "test_downloadermiddleware_redirect.py")],
        test_cases=[
            "tests.test_downloadermiddleware_redirect.RedirectMiddlewareTest.test_request_meta_handling"
        ],
    )
    Scrapy(
        bug_id=28,
        buggy_commit_id="e2f31f3018c0037f65982209c22f93b80a5d6e7b",
        fixed_commit_id="457b97c13ccf9a84f3dc7800c180cf059822c09a",
        test_file=[Path("tests", "test_dupefilters.py")],
        test_cases=["tests.test_dupefilters.RFPDupeFilterTest.test_dupefilter_path"],
    )
    Scrapy(
        bug_id=29,
        buggy_commit_id="5c4666a3d489bd3efa2e188de58721a125a5bfad",
        fixed_commit_id="8d45b3c4810cb5304ba1193b45697a0df1157326",
        test_file=[Path("tests", "test_utils_request.py")],
        test_cases=[
            "tests.test_utils_request.UtilsRequestTest.test_request_httprepr_for_non_http_request"
        ],
    )
    Scrapy(
        bug_id=30,
        buggy_commit_id="4d41cc0dc4821da07d467b368528c61ce48a0df2",
        fixed_commit_id="3e6d6c43ac0763adf2cd92efdb4a1dc2ba165440",
        test_file=[Path("tests", "test_command_version.py")],
        test_cases=["tests.test_command_version.VersionTest.test_output"],
    )
    Scrapy(
        bug_id=31,
        buggy_commit_id="5f02ef82e8560242eb34b336f385addfdef3211d",
        fixed_commit_id="dba7e39f61cbe2c22d3c9064f32f6e36d74f14b2",
        test_file=[Path("tests", "test_downloadermiddleware_cookies.py")],
        test_cases=[
            "tests.test_downloadermiddleware_cookies.CookiesMiddlewareTest.test_do_not_break_on_non_utf8_header"
        ],
    )
    Scrapy(
        bug_id=32,
        buggy_commit_id="342cb622f1ea93268477da557099010bbd72529a",
        fixed_commit_id="aa6a72707daabfb6217f52e4774f2ff038f83dcc",
        test_file=[Path("tests", "test_crawler.py")],
        test_cases=[
            "tests.test_crawler.CrawlerProcessTest.test_crawler_process_accepts_dict"
        ],
    )
    Scrapy(
        bug_id=33,
        buggy_commit_id="2d216771976cd7aedfb88ae97418c2d4dcc84917",
        fixed_commit_id="6dccb3a9b320a8d0808764ac8e6e88e663e2d52c",
        test_file=[
            Path("tests", "test_pipeline_media.py"),
            Path("tests", "test_utils_log.py"),
        ],
        test_cases=[
            "tests.test_pipeline_media.BaseMediaPipelineTestCase.test_default_item_completed",
            "tests.test_utils_log.FailureToExcInfoTest.test_failure",
            "tests.test_utils_log.FailureToExcInfoTest.test_non_failure",
        ],
    )
    Scrapy(
        bug_id=34,
        buggy_commit_id="e521740b3951bacc80d3c9c1db8652ed5e914b89",
        fixed_commit_id="773ea5a5ef76426dd91a8669542d2602082a5746",
        test_file=[Path("tests", "test_item.py")],
        test_cases=[
            "tests.test_item.ItemTest.test_metaclass_with_fields_attribute",
            "tests.test_item.ItemTest.test_metaclass_multiple_inheritance_simple",
            "tests.test_item.ItemTest.test_metaclass_multiple_inheritance_diamond",
        ],
    )
    Scrapy(
        bug_id=35,
        buggy_commit_id="0a5bbbaed3e182d2151b6b34357667901ece353f",
        fixed_commit_id="c3d3a9491412d2a91b0927a05908593dcd329e4a",
        test_file=[Path("tests", "test_crawler.py")],
        test_cases=[
            "tests.test_crawler.CrawlerRunnerTestCase.test_spidermanager_deprecation"
        ],
    )
    Scrapy(
        bug_id=36,
        buggy_commit_id="cb8140a42a27ede87b0880372024f2f1804618b8",
        fixed_commit_id="cf9be5344a89dd8e14f8241ec69de9c984ec1e05",
        test_file=[Path("tests", "test_utils_misc", "__init__.py")],
        test_cases=[
            "tests.test_utils_misc.__init__.UtilsMiscTestCase.test_create_instance"
        ],
    )
    Scrapy(
        bug_id=37,
        buggy_commit_id="1d5c270ce8caf954ce83c8db262e2a35707e0c5e",
        fixed_commit_id="f701f5b0db10faef08e4ed9a21b98fd72f9cfc9a",
        test_file=[Path("tests", "test_http_request.py")],
        test_cases=["tests.test_http_request.RequestTest.test_url_no_scheme"],
    )
    Scrapy(
        bug_id=38,
        buggy_commit_id="6cc6bbb5fc5c102271829a554772effb0444023c",
        fixed_commit_id="6c3970e6722191b642fd99c6c1bfed0d93010cab",
        test_file=[Path("tests", "test_http_request.py")],
        test_cases=[
            "tests.test_http_request.FormRequestTest.test_from_response_clickdata_does_not_ignore_image"
        ],
    )
    Scrapy(
        bug_id=39,
        buggy_commit_id="692975acb40c6394424dfb728b1ffa46b3b3c55d",
        fixed_commit_id="a1e8a8525d2312842c7e1cca8ba6e4e1a83084b7",
        test_file=[Path("tests", "test_spider.py")],
        test_cases=[
            "tests.test_spider.DeprecationTest.test_make_requests_from_url_deprecated"
        ],
    )
    Scrapy(
        bug_id=40,
        buggy_commit_id="7d24df37380cd5a5b7394cd2534e240bd2eff0ca",
        fixed_commit_id="f1d971a5c0cdfe0f4fe5619146cd6818324fc98e",
        test_file=[Path("tests", "test_exporters.py")],
        test_cases=[
            "tests.test_exporters.PythonItemExporterTest.test_other_python_types_item"
        ],
    )


class ScrapyAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
