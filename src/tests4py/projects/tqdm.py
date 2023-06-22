from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class TQDM(Project):
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
            project_name="tqdm",
            github_url="https://github.com/tqdm/tqdm",
            status=Status.OK,
            cause="N.A.",
            python_version="3.6.9",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version="3.6.15",
            python_fallback_version="3.6.15",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


def register():
    TQDM(
        bug_id=1,
        buggy_commit_id="8cc777fe8401a05d07f2c97e65d15e4460feab88",
        fixed_commit_id="c0dcf39b046d1b4ff6de14ac99ad9a1b10487512",
        test_file=[Path("tqdm", "tests", "tests_contrib.py")],
        test_cases=["python3-mtqdm/tests/tests_contrib.py::test_enumerate"],
    )
    TQDM(
        bug_id=2,
        buggy_commit_id="bef86db56654d271838b145ad77f7040a73a7b4d",
        fixed_commit_id="127af5caf19e7d29c346f5ca8a9c7ef3004b664b",
        test_file=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=["python3-mtqdm/tests/tests_tqdm.py::test_format_meter"],
    )
    TQDM(
        bug_id=3,
        buggy_commit_id="c2599e3cd6087429f48bae34347ec5d2473c8392",
        fixed_commit_id="73962a47026dd980ac0758820efc9c41cbf938e0",
        test_file=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=["python3-mtqdm/tests/tests_tqdm.py::test_bool"],
    )
    TQDM(
        bug_id=4,
        buggy_commit_id="03b347646492131d889871939b40457d29147216",
        fixed_commit_id="964dee631d0ed30e2f799b42fc58ba5e73795a08",
        test_file=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=["python3-mtqdm/tests/tests_tqdm.py::test_nototal"],
    )
    TQDM(
        bug_id=5,
        buggy_commit_id="19b08ab34fdbfa0275bc5cb2430436c724c7e759",
        fixed_commit_id="4f340697af69b71850aad496387c9c5aa1904136",
        test_file=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=["python3-mtqdm/tests/tests_tqdm.py::test_bool"],
    )
    TQDM(
        bug_id=6,
        buggy_commit_id="a4b9c86db548b2d0dbb5af7a6bbdc26ab47e1eec",
        fixed_commit_id="6dad2e89019317e875c46d5a3a82a811ad6de2f9",
        test_file=[Path("tqdm", "tests", "tests_synchronisation.py")],
        test_cases=["python3-mtqdm/tests/tests_synchronisation.py::test_imap"],
    )
    TQDM(
        bug_id=7,
        buggy_commit_id="caefe02fd6f3165e5634460ab20caf4c60400120",
        fixed_commit_id="4efd35246c924236f34d8130b1055a3c3ba78605",
        test_file=[Path("tqdm", "tests", "tests_main.py")],
        test_cases=["python3-mtqdm/tests/tests_main.py::test_main"],
    )
    TQDM(
        bug_id=8,
        buggy_commit_id="08b8ad1ff3bd003ef8309faaa0cc108ffa40317d",
        fixed_commit_id="cae9d139c6df5614be3bf6e25ccbd600ee3286dc",
        test_file=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=["python3-mtqdm/tests/tests_tqdm.py::test_format_meter"],
    )
    TQDM(
        bug_id=9,
        buggy_commit_id="9da1d5d116aec7a23d8f6dc22d5e23ecb1c40a7c",
        fixed_commit_id="d877c1dfb4739852105f7b967a8fceb869ac5042",
        test_file=[Path("tqdm", "tests", "tests_tqdm.py")],
        test_cases=[
            "python3-mtqdm/tests/tests_tqdm.py::test_si_format",
            "python3-mtqdm/tests/tests_tqdm.py::test_update",
        ],
    )


class TQDMAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
