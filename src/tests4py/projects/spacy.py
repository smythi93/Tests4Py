from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class SpaCy(Project):
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
            project_name="spacy",
            github_url="https://github.com/explosion/spaCy",
            status=Status.OK,
            cause="N.A.",
            python_version="3.7.7",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version="3.7.8",
            python_fallback_version="3.7.8",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


def register():
    SpaCy(
        bug_id=1,
        buggy_commit_id="9ce059dd067ecc3f097d04023e3cfa0d70d35bb8",
        fixed_commit_id="a987e9e45d4084f30964a4cec9914ae6ed25a73c",
        test_file=[Path("spacy", "tests", "test_errors.py")],
        test_cases=["py.testspacy/tests/test_errors.py::test_add_codes"],
    )
    SpaCy(
        bug_id=2,
        buggy_commit_id="efec28ce70a0ff69471cc379867deebe7eb881e0",
        fixed_commit_id="cfdaf99b8029d6762730c5d5bd2b6f6c173c1241",
        test_file=[Path("spacy", "tests", "regression", "test_issue5137.py")],
        test_cases=["py.testspacy/tests/regression/test_issue5137.py::test_issue5137"],
    )
    SpaCy(
        bug_id=3,
        buggy_commit_id="dac70f29eb3b1f21ae9e2c6346666bf6a46307b6",
        fixed_commit_id="663333c3b2bad90915d1a48a626ca1275b7ef077",
        test_file=[Path("spacy", "tests", "regression", "test_issue5314.py")],
        test_cases=["py.testspacy/tests/regression/test_issue5314.py::test_issue5314"],
    )
    SpaCy(
        bug_id=4,
        buggy_commit_id="abd5c06374eab5db0cf897b73543b1f3eb007e12",
        fixed_commit_id="9fa9d7f2cb52ce6a70c264d4e57c7f190d7686bf",
        test_file=[Path("spacy", "tests", "regression", "test_issue4665.py")],
        test_cases=["py.testspacy/tests/regression/test_issue4665.py::test_issue4665"],
    )
    SpaCy(
        bug_id=5,
        buggy_commit_id="bdfb696677a7591ced018e7597c00929e97c6837",
        fixed_commit_id="3bd15055ce74b04dcaf3b9abe2adeb01fb595776",
        test_file=[Path("spacy", "tests", "test_language.py")],
        test_cases=["py.testspacy/tests/test_language.py::test_evaluate_no_pipe"],
    )
    SpaCy(
        bug_id=6,
        buggy_commit_id="6b874ef09611ac32ad038203423d44087cbeb3ae",
        fixed_commit_id="afe4a428f78abe45d6104d74ef42a066570fa43d",
        test_file=[Path("spacy", "tests", "pipeline", "test_analysis.py")],
        test_cases=[
            "py.testspacy/tests/pipeline/test_analysis.py::test_analysis_validate_attrs_remove_pipe"
        ],
    )
    SpaCy(
        bug_id=7,
        buggy_commit_id="da6e0de34f4947fdebc839df3969c641014cfa97",
        fixed_commit_id="6f54e59fe7ccb3bacce896ed33d36b39f11cbfaf",
        test_file=[Path("spacy", "tests", "doc", "test_span.py")],
        test_cases=["py.testspacy/tests/doc/test_span.py::test_filter_spans"],
    )
    SpaCy(
        bug_id=8,
        buggy_commit_id="fa95c030a511337935d1a2e930cb954c7a4cd376",
        fixed_commit_id="5efae495f18f37316bd641a05ca26e62cb78e242",
        test_file=[Path("spacy", "tests", "matcher", "test_matcher_logic.py")],
        test_cases=[
            "py.testspacy/tests/matcher/test_matcher_logic.py::test_matcher_remove"
        ],
    )
    SpaCy(
        bug_id=9,
        buggy_commit_id="bc7e7db208d351fae2982afbcdff7633f9636779",
        fixed_commit_id="3297a19545027c8d8550b1ae793ce290567eff32",
        test_file=[Path("spacy", "tests", "pipeline", "test_tagger.py")],
        test_cases=[
            "py.testspacy/tests/pipeline/test_tagger.py::test_tagger_warns_no_lemma_lookups"
        ],
    )
    SpaCy(
        bug_id=10,
        buggy_commit_id="38de08c7a99d5d8c490223126071afe7dd4f4b67",
        fixed_commit_id="52904b72700a3f301a26563d3f94493bad96a446",
        test_file=[Path("spacy", "tests", "matcher", "test_matcher_api.py")],
        test_cases=[
            "py.testspacy/tests/matcher/test_matcher_api.py::test_matcher_valid_callback"
        ],
    )


class SpaCyAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
