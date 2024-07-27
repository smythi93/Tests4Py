import os
from pathlib import Path
from typing import List, Optional, Tuple

from tests4py.constants import PYTHON
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "tqdm"


class TQDM(Project):
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
            github_url="https://github.com/tqdm/tqdm",
            status=Status.OK,
            python_version="3.6.15",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version="3.6.15",
            python_fallback_version="3.6.15",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
            loc=loc,
            source_base=Path(PROJECT_NAME),
            test_base=Path(PROJECT_NAME, "tests"),
            included_files=[PROJECT_NAME],
            excluded_files=[os.path.join(PROJECT_NAME, "tests")],
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
            ],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )


def register():
    TQDM(
        bug_id=1,
        buggy_commit_id="8cc777fe8401a05d07f2c97e65d15e4460feab88",
        fixed_commit_id="c0dcf39b046d1b4ff6de14ac99ad9a1b10487512",
        test_files=[Path("tqdm", "tests", "tests_contrib.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_contrib.py::test_enumerate")],
        loc=1910,
    )
    TQDM(
        bug_id=2,
        buggy_commit_id="bef86db56654d271838b145ad77f7040a73a7b4d",
        fixed_commit_id="127af5caf19e7d29c346f5ca8a9c7ef3004b664b",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_format_meter"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_si_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_all_defaults"),
            os.path.join(
                "tqdm", "tests", "tests_tqdm.py::test_native_string_io_for_default_file"
            ),
            os.path.join(
                "tqdm",
                "tests",
                "tests_tqdm.py::test_unicode_string_io_for_specified_file",
            ),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_write_bytes"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_file_output"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_leave_option"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_trange"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_min_interval"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_max_interval"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_min_iters"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_dynamic_min_iters"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_big_min_interval"),
            os.path.join(
                "tqdm", "tests", "tests_tqdm.py::test_smoothed_dynamic_min_iters"
            ),
            os.path.join(
                "tqdm",
                "tests",
                "tests_tqdm.py::test_smoothed_dynamic_min_iters_with_min_interval",
            ),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_nototal"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_unit"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_ascii"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_update"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_close"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_smoothing"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_bar_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_custom_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_unpause"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_reset"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_position"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_set_description"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_deprecated_gui"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_cmp"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_repr"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_autodisable_enable"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_file_redirection"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_external_write"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_unit_scale"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_bool"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_auto"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_float_progress"),
        ],
        skip_tests=["test_ansi_escape_codes"],
        loc=1759,
    )
    TQDM(
        bug_id=3,
        buggy_commit_id="c2599e3cd6087429f48bae34347ec5d2473c8392",
        fixed_commit_id="73962a47026dd980ac0758820efc9c41cbf938e0",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_bool")],
        loc=1567,
    )
    TQDM(
        bug_id=4,
        buggy_commit_id="03b347646492131d889871939b40457d29147216",
        fixed_commit_id="964dee631d0ed30e2f799b42fc58ba5e73795a08",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_nototal")],
        loc=1534,
    )
    TQDM(
        bug_id=5,
        buggy_commit_id="19b08ab34fdbfa0275bc5cb2430436c724c7e759",
        fixed_commit_id="4f340697af69b71850aad496387c9c5aa1904136",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_bool")],
        loc=1485,
    )
    TQDM(
        bug_id=6,
        buggy_commit_id="a4b9c86db548b2d0dbb5af7a6bbdc26ab47e1eec",
        fixed_commit_id="6dad2e89019317e875c46d5a3a82a811ad6de2f9",
        test_files=[Path("tqdm", "tests", "tests_synchronisation.py")],
        test_cases=[
            os.path.join("tqdm", "tests", "tests_synchronisation.py::test_imap")
        ],
        skip_tests=["test_monitoring_multi"],
        loc=1438,
    )
    TQDM(
        bug_id=7,
        buggy_commit_id="caefe02fd6f3165e5634460ab20caf4c60400120",
        fixed_commit_id="4efd35246c924236f34d8130b1055a3c3ba78605",
        test_files=[
            Path("tqdm", "tests", "tests_main.py"),
            Path("tqdm", "tests", "tests_tqdm.py"),
        ],
        test_cases=[os.path.join("tqdm", "tests", "tests_main.py::test_main")],
        loc=1389,
    )
    TQDM(
        bug_id=8,
        buggy_commit_id="08b8ad1ff3bd003ef8309faaa0cc108ffa40317d",
        fixed_commit_id="cae9d139c6df5614be3bf6e25ccbd600ee3286dc",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[os.path.join("tqdm", "tests", "tests_tqdm.py::test_format_meter")],
        loc=870,
    )
    TQDM(
        bug_id=9,
        buggy_commit_id="9da1d5d116aec7a23d8f6dc22d5e23ecb1c40a7c",
        fixed_commit_id="d877c1dfb4739852105f7b967a8fceb869ac5042",
        test_files=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_si_format"),
            os.path.join("tqdm", "tests", "tests_tqdm.py::test_update"),
        ],
        loc=385,
    )


class TQDMAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""
