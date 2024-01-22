import ast
import os.path
import queue
import random
import shlex
import string
import subprocess
from abc import ABC
from pathlib import Path
from typing import List, Optional, Tuple, Callable, Any, Dict

from tests4py.constants import PYTHON
from tests4py.grammars.default import clean_up, CLI_GRAMMAR, get_possible_options, FLOAT
from tests4py.grammars.fuzzer import Grammar, GrammarFuzzer, srange, is_valid_grammar
from tests4py.grammars.tree import ComplexDerivationTree
from tests4py.grammars.utils import GrammarVisitor
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, ExpectErrAPI, TestResult, SpecificationError

PROJECT_MAME = "fastapi"


class FastAPI(Project):
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
        grammar: Grammar = None,
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_MAME,
            github_url="https://github.com/tiangolo/fastapi",
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
            grammar=grammar_request if grammar is None else grammar,
            loc=loc,
            setup=[
                [PYTHON, "-m", "pip", "install", "-e", "."],
                [
                    PYTHON,
                    "-c",
                    """
import shutil
import os
shutil.rmtree(os.path.join("tests", "test_modules_same_name_body"), ignore_errors=True)
shutil.rmtree(os.path.join("tests", "test_tutorial"), ignore_errors=True)
""",
                ],
            ],
            included_files=[PROJECT_MAME],
            test_base=Path("tests"),
            relevant_test_files=relevant_test_files,
        )


def register():
    FastAPI(
        bug_id=1,
        buggy_commit_id="766157bfb4e7dfccba09ab398e8ec444d14e947c",
        fixed_commit_id="3397d4d69a9c2d64c1219fcbf291ea5697a4abb8",
        test_files=[Path("tests", "test_jsonable_encoder.py")],
        test_cases=[
            os.path.join(
                "tests", "test_jsonable_encoder.py::test_encode_model_with_default"
            )
        ],
        api=FastAPI1API(
            (
                b"TypeError: jsonable_encoder() got an unexpected keyword argument 'exclude_defaults'",
                b"TypeError: jsonable_encoder() got an unexpected keyword argument 'exclude_none'",
            )
        ),
        systemtests=FastAPI1SystemtestGenerator(),
        unittests=FastAPI1UnittestGenerator(),
        grammar=grammar_jsonable_encoder,
        loc=4274,
    )
    FastAPI(
        bug_id=2,
        buggy_commit_id="210af1fd3dc0f612a08fa02a0cb3f5adb81e5bfb",
        fixed_commit_id="02441ff0313d5b471b662293244c53e712f1243f",
        test_files=[Path("tests", "test_ws_router.py")],
        test_cases=[
            os.path.join(
                "tests", "test_ws_router.py::test_router_ws_depends_with_override"
            )
        ],
        relevant_test_files=[
            Path("tests", "test_additional_responses_router.py"),
            Path("tests", "test_custom_route_class.py"),
            Path("tests", "test_default_response_class_router.py"),
            Path("tests", "test_empty_router.py"),
            Path("tests", "test_router_events.py"),
            Path("tests", "test_router_prefix_with_template.py"),
            Path("tests", "test_ws_router.py"),
        ],
        systemtests=FastAPI2SystemtestGenerator(),
        unittests=FastAPI2UnittestGenerator(),
        api=FastAPI2API(),
        loc=4266,
    )
    FastAPI(
        bug_id=3,
        buggy_commit_id="869c7389e22dc9ad659940fa271da76c4f3ba3b1",
        fixed_commit_id="aea04ee32ee1942e6e1a904527bb8da6ba76abd9",
        test_files=[Path("tests", "test_serialize_response_model.py")],
        test_cases=[
            os.path.join("tests", "test_serialize_response_model.py::test_valid"),
            os.path.join("tests", "test_serialize_response_model.py::test_coerce"),
            os.path.join("tests", "test_serialize_response_model.py::test_validlist"),
            os.path.join("tests", "test_serialize_response_model.py::test_validdict"),
            os.path.join(
                "tests", "test_serialize_response_model.py::test_valid_exclude_unset"
            ),
            os.path.join(
                "tests", "test_serialize_response_model.py::test_coerce_exclude_unset"
            ),
            os.path.join(
                "tests",
                "test_serialize_response_model.py::test_validlist_exclude_unset",
            ),
            os.path.join(
                "tests",
                "test_serialize_response_model.py::test_validdict_exclude_unset",
            ),
        ],
        relevant_test_files=[
            Path("tests", "test_serialize_response.py"),
            Path("tests", "test_serialize_response_dataclass.py"),
            Path("tests", "test_serialize_response_model.py"),
        ],
        api=FastAPI3API(),
        systemtests=FastAPI3SystemtestGenerator(),
        unittests=FastAPI3UnittestGenerator(),
        loc=4238,
    )
    FastAPI(
        bug_id=4,
        buggy_commit_id="7ccd81f70653857bd8f3a15ee946aa3fb0edc2cb",
        fixed_commit_id="74c4d1c1dbe6bfdb05d6e4fc767ffe062398f0a3",
        test_files=[Path("tests", "test_param_in_path_and_dependency.py")],
        test_cases=[
            os.path.join(
                "tests", "test_param_in_path_and_dependency.py::test_reused_param"
            )
        ],
        relevant_test_files=[
            Path("tests", "test_param_class.py"),
            Path("tests", "test_param_in_path_and_dependency.py"),
        ],
        api=FastAPI4API(),
        systemtests=FastAPI4SystemtestGenerator(),
        unittests=FastAPI4UnittestGenerator(),
        loc=4231,
    )
    FastAPI(
        bug_id=5,
        buggy_commit_id="7cea84b74ca3106a7f861b774e9d215e5228728f",
        fixed_commit_id="75a07f24bf01a31225ee687f3e2b3fc1981b67ab",
        test_files=[Path("tests", "test_filter_pydantic_sub_model.py")],
        test_cases=[
            os.path.join(
                "tests", "test_filter_pydantic_sub_model.py::test_filter_sub_model"
            )
        ],
        relevant_test_files=[
            Path("tests", "test_application.py"),
            Path("tests", "test_duplicate_models_openapi.py"),
            Path("tests", "test_filter_pydantic_sub_model.py"),
            Path("tests", "test_union_body.py"),
            Path("tests", "test_union_inherited_body.py"),
        ],
        api=FastAPI5API(),
        systemtests=FastAPI5SystemtestGenerator(),
        unittests=FastAPI5UnittestGenerator(),
        loc=4227,
    )
    FastAPI(
        bug_id=6,
        buggy_commit_id="5db99a27cf640864b4793807811848698c5ff4a2",
        fixed_commit_id="874d24181e779ebc6e1c52afb7d6598f863fd6a8",
        test_files=[Path("tests", "test_forms_from_non_typing_sequences.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_forms_from_non_typing_sequences.py::test_python_list_param_as_form",
            ),
            os.path.join(
                "tests",
                "test_forms_from_non_typing_sequences.py::test_python_set_param_as_form",
            ),
            os.path.join(
                "tests",
                "test_forms_from_non_typing_sequences.py::test_python_tuple_param_as_form",
            ),
        ],
        relevant_test_files=[
            Path("tests", "test_application.py"),
            Path("tests", "test_forms_from_non_typing_sequences.py"),
            Path("tests", "test_union_body.py"),
            Path("tests", "test_union_inherited_body.py"),
        ],
        api=FastAPI6API(),
        systemtests=FastAPI6SystemtestGenerator(),
        unittests=FastAPI6UnittestGenerator(),
        loc=4220,
    )
    FastAPI(
        bug_id=7,
        buggy_commit_id="cc4c13e4ae3f65fc76c23962b316df4a60e0c7e0",
        fixed_commit_id="19c77e35bdde33aeec1eb2cfa680f95016492b69",
        test_files=[Path("tests", "test_multi_body_errors.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_multi_body_errors.py::test_jsonable_encoder_requiring_error",
            )
        ],
        relevant_test_files=[
            Path("tests", "test_jsonable_encoder.py"),
            Path("tests", "test_multi_body_errors.py"),
        ],
        api=FastAPI7API(),
        systemtests=FastAPI7SystemtestGenerator(),
        unittests=FastAPI7UnittestGenerator(),
        loc=4113,
    )
    FastAPI(
        bug_id=8,
        buggy_commit_id="fdb6d43e103bcf7a7325d796e37c9435c9460e4c",
        fixed_commit_id="dd963511d699b463b416408a0ad705b3dda0d067",
        test_files=[Path("tests", "test_custom_route_class.py")],
        test_cases=[
            os.path.join("tests", "test_custom_route_class.py::test_route_classes")
        ],
        relevant_test_files=[
            Path("tests", "test_additional_responses_router.py"),
            Path("tests", "test_custom_route_class.py"),
            Path("tests", "test_default_response_class_router.py"),
            Path("tests", "test_empty_router.py"),
            Path("tests", "test_router_prefix_with_template.py"),
            Path("tests", "test_ws_router.py"),
        ],
        api=FastAPI8API(),
        systemtests=FastAPI8SystemtestGenerator(),
        unittests=FastAPI8UnittestGenerator(),
        loc=3694,
    )
    FastAPI(
        bug_id=9,
        buggy_commit_id="a7a92bc63768ccee3f3afc2b73b2c581928dfe75",
        fixed_commit_id="c5817912d2be25bb310bf9da517882f57bbe7bb5",
        test_files=[Path("tests", "test_request_body_parameters_media_type.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_request_body_parameters_media_type.py::test_openapi_schema",
            )
        ],
        relevant_test_files=[
            Path("tests", "test_application.py"),
            Path("tests", "test_duplicate_models_openapi.py"),
            Path("tests", "test_request_body_parameters_media_type.py"),
            Path("tests", "test_union_body.py"),
            Path("tests", "test_union_inherited_body.py"),
        ],
        api=FastAPI9API(),
        # systemtests=FastAPI9SystemtestGenerator(),
        # unittests=FastAPI9UnittestGenerator(),
        loc=3625,
    )
    FastAPI(
        bug_id=10,
        buggy_commit_id="b77a43bcac3ec8e7edbe82543e777c60ae85c178",
        fixed_commit_id="38495fffa560fa57a8f0e6437d8e43c36c8e5612",
        test_files=[Path("tests", "test_skip_defaults.py")],
        test_cases=[
            os.path.join("tests", "test_skip_defaults.py::test_return_defaults")
        ],
        relevant_test_files=[
            Path("tests", "test_dependency_overrides.py"),
            Path("tests", "test_skip_defaults.py"),
        ],
        loc=3613,
    )
    FastAPI(
        bug_id=11,
        buggy_commit_id="bf229ad5d830eb5320f966d51a55e590e8d57008",
        fixed_commit_id="06eb4219345a77d23484528c9d164eb8d2097fec",
        test_files=[
            Path("tests", "test_union_body.py"),
            Path("tests", "test_union_inherited_body.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_union_body.py::test_item_openapi_schema"),
            os.path.join("tests", "test_union_body.py::test_post_other_item"),
            os.path.join("tests", "test_union_body.py::test_post_item"),
            os.path.join(
                "tests",
                "test_union_inherited_body.py::test_inherited_item_openapi_schema",
            ),
            os.path.join(
                "tests", "test_union_inherited_body.py::test_post_extended_item"
            ),
            os.path.join("tests", "test_union_inherited_body.py::test_post_item"),
        ],
        relevant_test_files=[
            Path("tests", "test_application.py"),
            Path("tests", "test_union_body.py"),
            Path("tests", "test_union_inherited_body.py"),
        ],
        loc=3591,
    )
    FastAPI(
        bug_id=12,
        buggy_commit_id="d61f5e4b555b123bf222503fc0e076cbae6a7ebc",
        fixed_commit_id="d262f6e9296993e528e2327f0a73f7bf5514e7c6",
        test_files=[Path("tests", "test_security_http_bearer_optional.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_security_http_bearer_optional.py::test_security_http_bearer_incorrect_scheme_credentials",
            )
        ],
        relevant_test_files=[
            Path("tests", "test_security_http_base.py"),
            Path("tests", "test_security_http_base_optional.py"),
            Path("tests", "test_security_http_basic_optional.py"),
            Path("tests", "test_security_http_basic_realm.py"),
            Path("tests", "test_security_http_bearer.py"),
            Path("tests", "test_security_http_bearer_optional.py"),
            Path("tests", "test_security_http_digest.py"),
            Path("tests", "test_security_http_digest_optional.py"),
        ],
        loc=3396,
    )
    FastAPI(
        bug_id=13,
        buggy_commit_id="6f7f9268f6b03f42831dcfeaa5c15ba9813333ec",
        fixed_commit_id="c8df3ae57c57e119d115dd3c1f44efa78de1022a",
        test_files=[Path("tests", "test_additional_responses_router.py")],
        test_cases=[
            os.path.join(
                "tests", "test_additional_responses_router.py::test_openapi_schema"
            )
        ],
        relevant_test_files=[
            Path("tests", "test_additional_properties.py"),
            Path("tests", "test_additional_response_extra.py"),
            Path("tests", "test_additional_responses_router.py"),
            Path("tests", "test_include_route.py"),
            Path("tests", "test_ws_router.py"),
        ],
        loc=2703,
    )
    FastAPI(
        bug_id=14,
        buggy_commit_id="2ddb804940bbcad4ed730b2a910c8fd3c1167127",
        fixed_commit_id="b7d184363fad5f6b55d15ec3a3a844aa81092bbd",
        test_files=[Path("tests", "test_additional_properties.py")],
        test_cases=[
            os.path.join(
                "tests",
                "test_additional_properties.py::test_additional_properties_schema",
            )
        ],
        relevant_test_files=[
            Path("tests", "test_additional_properties.py"),
            Path("tests", "test_application.py"),
            Path("tests", "test_extra_routes.py"),
            Path("tests", "test_multi_body_errors.py"),
            Path("tests", "test_put_no_body.py"),
        ],
        loc=2533,
    )
    FastAPI(
        bug_id=15,
        buggy_commit_id="b16ca54c30644667ab9f65a712704850666a039c",
        fixed_commit_id="6d77e2ac5f2cadc63424f2d85d8d8cded2975922",
        test_files=[Path("tests", "test_ws_router.py")],
        test_cases=[
            os.path.join("tests", "test_ws_router.py::test_router"),
            os.path.join("tests", "test_ws_router.py::test_prefix_router"),
        ],
        relevant_test_files=[
            Path("tests", "test_extra_routes.py"),
            Path("tests", "test_include_route.py"),
            Path("tests", "test_ws_router.py"),
        ],
        loc=2495,
    )
    FastAPI(
        bug_id=16,
        buggy_commit_id="92c825be6a7362099400c9c3fe8b01ea13add3dc",
        fixed_commit_id="9745a5d1ae86a7fefacf79bdde8e5dd2d59fa2f4",
        test_files=[
            Path("tests", "test_datetime_custom_encoder.py"),
            Path("tests", "test_jsonable_encoder.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_jsonable_encoder.py::test_encode_model_with_config"
            )
        ],
        relevant_test_files=[
            Path("tests", "test_datetime.py"),
            Path("tests", "test_datetime_custom_encoder.py"),
            Path("tests", "test_jsonable_encoder.py"),
        ],
        loc=2427,
    )


class FastAPI1API(ExpectErrAPI):
    pass


class FastAPIDefaultAPI(API, GrammarVisitor):
    """ """

    def __init__(self, default_timeout: int = 5):
        API.__init__(self, default_timeout=default_timeout)
        GrammarVisitor.__init__(self, grammar_request_generic)
        self.websockets = dict()
        self.gets = dict()
        self.posts = dict()
        self.dependencies = []
        self.overrides = dict()
        self.url = None
        self.mode = None
        self.data = None
        self.aliased = False

    def visit_options(self, node: ComplexDerivationTree):
        self.websockets = dict()
        self.gets = dict()
        self.posts = dict()
        self.websockets = dict()
        self.dependencies = []
        self.overrides = dict()
        self.url = None
        self.mode = None
        self.data = None
        self.aliased = None
        self.generic_visit(node)

    def prepare_args(self, args: List[str], work_dir: Path) -> List[str]:
        try:
            self.visit_source(shlex.join(args))
        except SyntaxError as e:
            raise SpecificationError(f"Cannot parse contents of {args}: {e}")
        return args

    def visit_arg(self, node: ComplexDerivationTree):
        return self.visit(node.children[0])

    @staticmethod
    def visit_unescaped(node: ComplexDerivationTree):
        return node.to_string()

    @staticmethod
    def visit_escaped(node: ComplexDerivationTree):
        return node.children[1].to_string()

    @staticmethod
    def _filter(node: ComplexDerivationTree):
        return list(
            filter(
                lambda n: n.value not in ("<sep>", " ", "\n", "\t", "\r"), node.children
            )
        )

    # noinspection PyUnusedLocal
    def visit_websocket(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.websockets[self.visit(filtered[1])] = self.visit(filtered[2])

    def visit_get(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.gets[self.visit(filtered[1])] = self.visit(filtered[2])

    def visit_post(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.posts[self.visit(filtered[1])] = self.visit(filtered[2])

    # noinspection PyUnusedLocal
    def visit_dependency(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.dependencies.append(self.visit(filtered[1]))

    # noinspection PyUnusedLocal
    def visit_override(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.overrides[self.visit(filtered[1])] = self.visit(filtered[2])

    def visit_url(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.url = self.visit(filtered[1])

    def visit_mode(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.mode = self.visit(filtered[1])

    def visit_alias(self, node: ComplexDerivationTree):
        filtered = self._filter(node)
        self.aliased = self.visit(filtered[1])

    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return False

    def fallback_condition(self, process: subprocess.CompletedProcess) -> bool:
        return False

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return False

    def fallback_contains(self, process: subprocess.CompletedProcess) -> bool:
        return False

    def get_failing_feedback(self):
        return ""

    def get_failing_fallback_feedback(self):
        return ""

    def get_error_feedback(self):
        return "Encountered an error that cannot be interpreted"

    def oracle(self, args) -> Tuple[TestResult, str]:
        process = args
        if not self.parsed:
            return TestResult.UNDEFINED, "Cannot parse argument"
        if self.condition(process) and self.contains(process):
            return TestResult.FAILING, self.get_failing_feedback()
        else:
            if self.fallback_condition(process) and self.fallback_contains(process):
                return TestResult.FAILING, self.get_failing_fallback_feedback()
            elif self.error_handling(process):
                return TestResult.UNDEFINED, self.get_error_feedback()
            else:
                return TestResult.PASSING, ""

    def error_handling(self, process) -> bool:
        return process.returncode != 0 and process.returncode != 200


class FastAPI2API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return (
            self.mode == "websocket"
            and self.url in self.websockets
            and self.websockets[self.url] in self.overrides
        )

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            self.overrides[self.websockets[self.url]].encode("utf8")
            not in process.stdout
        )

    def fallback_condition(self, process: subprocess.CompletedProcess) -> bool:
        return (
            self.mode == "websocket"
            and self.url in self.websockets
            and not self.websockets[self.url] in self.overrides
        )

    def fallback_contains(self, process: subprocess.CompletedProcess) -> bool:
        return self.websockets[self.url].encode("utf8") not in process.stdout


class FastAPI3API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return process.returncode != 0 and process.returncode != 200

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"pydantic.error_wrappers.ValidationError:" in process.stderr
            and (
                b"validation errors for Item" in process.stderr
                or b"validation error for Item" in process.stderr
                or b"validation error for OtherItem" in process.stderr
                or b"validation errors for OtherItem" in process.stderr
            )
            and b"field required (type=value_error.missing)" in process.stderr
        )


class FastAPI4API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return process.returncode in (0, 200) and self.path == "/openapi.json"

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        response = eval(process.stdout.decode("utf-8"))
        if not isinstance(response, dict):
            return False
        key_queue = queue.Queue()
        for key in response:
            key_queue.put((key, response[key]))
        while not key_queue.empty():
            key, value = key_queue.get()
            if key == "parameters":
                if isinstance(value, list):
                    result = sorted(list(map(str, value)))
                    expected = [*set(result)]
                    if result != expected:
                        return True
            elif isinstance(value, dict):
                for k in value:
                    key_queue.put((k, value[k]))
        return False


class FastAPI5API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return process.returncode == 0 or process.returncode == 200

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b'"password"' in process.stdout
            or b'"test-password"' in process.stdout
            or b"'password'" in process.stdout
            or b"'test-password'" in process.stdout
        )


class FastAPI6API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return process.returncode == 166

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return b"value_error.missing" in process.stdout


class FastAPI7API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return process.returncode != 0 and process.returncode != 200

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"TypeError: Object of type Decimal is not JSON serializable"
            in process.stderr
        )

    def error_handling(self, process: subprocess.CompletedProcess) -> bool:
        return (
            process.returncode != 0
            and process.returncode != 200
            and (
                process.returncode != 166
                or b"value_error.number.not_gt" not in process.stdout
            )
        )


class FastAPI8API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return (
            self.path == "/routes/"
            and process.returncode != 0
            and process.returncode != 200
        )

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return (
            b"AttributeError: 'APIRoute' object has no attribute 'x_type'"
            in process.stderr
        )


class FastAPI9API(FastAPIDefaultAPI):
    pass


class FastAPI10API(FastAPIDefaultAPI):
    pass


class FastAPISystemtestGenerator(SystemtestGenerator, ABC):
    pass


class FastAPI1TestGenerator(ABC):
    def __init__(self):
        self.string_fuzzer = GrammarFuzzer(
            grammar_jsonable_encoder, start_symbol="<json_str>"
        )

    @staticmethod
    def _get_keys(m: int = 0, n: int = 4):
        m = max(m, 0)
        n = min(n, len(grammar_jsonable_encoder["<key>"]))
        return list(
            random.sample(grammar_jsonable_encoder["<key>"], k=random.randint(m, n))
        )

    def _generate_default_object(self, set_self=False):
        if random.getrandbits(1):
            entries = [
                f"'{key}':{self.string_fuzzer.fuzz()}" for key in self._get_keys()
            ]
            if entries:
                return f"\"{{{','.join(entries)}}}\""
            else:
                return "{}"
        else:
            keys = self._get_keys()
            if "foo" not in keys:
                keys.append("foo")
                random.shuffle(keys)
            entries = [f"{key}={self.string_fuzzer.fuzz()}" for key in keys]
            if entries:
                return f"\"{'self.' if set_self else ''}Model({','.join(entries)})\""
            else:
                return f"{'self.' if set_self else ''}Model()"

    def _generate_key_list(self):
        return ",".join(self._get_keys(m=1))


class FastAPI1SystemtestGenerator(FastAPISystemtestGenerator, FastAPI1TestGenerator):
    def __init__(self):
        FastAPISystemtestGenerator.__init__(self)
        FastAPI1TestGenerator.__init__(self)

    def _generate_object(self):
        return "-o" + self._generate_default_object()

    def _generate_test(self, failing=False):
        args = [self._generate_object()]
        if random.getrandbits(1):
            args.append(f"-i{self._generate_key_list()}")
        if random.getrandbits(1):
            args.append(f"-e{self._generate_key_list()}")
        if random.getrandbits(1):
            args.append("-a")
        if random.getrandbits(1):
            args.append("-s")
        if random.getrandbits(1):
            args.append("-u")
        if random.getrandbits(1):
            args.append("-c{str:repr}")
        if random.getrandbits(1):
            args.append("-q")
        if failing:
            if random.getrandbits(1):
                args.append("-d")
                if random.getrandbits(1):
                    args.append("-ne")
            else:
                args.append("-ne")
                if random.getrandbits(1):
                    args.append("-d")
        random.shuffle(args)
        return "\n".join(args)

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self._generate_test(failing=True), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self._generate_test(failing=False), TestResult.PASSING


class FastAPIDefaultSystemtestGenerator(FastAPISystemtestGenerator, ABC):
    WEBSOCKET = "websocket"
    GET = "get"
    POST = "post"

    def __init__(self, max_others: int = 10):
        super().__init__()
        self.string_fuzzer = GrammarFuzzer(grammar_request, start_symbol="<chars>")
        self.json_fuzzer = GrammarFuzzer(grammar_request, start_symbol="<json>")
        self.paths: Dict[str, str] = dict()
        self.dependencies: List[str] = list()
        self.overrides: List[str] = list()
        self.data: Optional[str] = None
        self.max_others = max_others
        self.responders: List[
            Tuple[Callable[[Any], Tuple[List[str], str]], List[Callable]]
        ] = [
            (self.generate_websocket, [self.random_bool]),
        ]
        self.others: List[
            Tuple[Callable[[Any], Tuple[List[str], str]], List[Callable]]
        ] = [
            (self.generate_dependency, [self.random_bool]),
        ]

    def reset(self):
        self.paths = dict()
        self.dependencies = list()
        self.overrides = list()
        self.data = None

    def _generate_path(self) -> str:
        prefix = "" if random.random() < 0.5 else self._generate_path()
        return prefix + "/" + self.string_fuzzer.fuzz()

    def generate_new_path(self) -> str:
        path = self._generate_path()
        while path in self.paths:
            path = self._generate_path()
        return path

    def generate_dependency(self, override: bool = False) -> Tuple[List[str], str]:
        dependency = self.string_fuzzer.fuzz()
        while dependency in self.dependencies:
            dependency = self.string_fuzzer.fuzz()
        if override:
            override = dependency
            while override == dependency:
                override = self.string_fuzzer.fuzz()
            self.overrides.append(dependency)
            return ["-os", dependency, override], None
        else:
            self.dependencies.append(dependency)
            return ["-ds", dependency], None

    def generate_websocket(self, override: bool = False) -> Tuple[List[str], str]:
        path = self.generate_new_path()
        self.paths[path] = self.WEBSOCKET
        args = []
        if override:
            if not self.overrides:
                args, _ = self.generate_dependency(override=True)
            dependency = random.choice(self.overrides)
        else:
            if not self.dependencies:
                args, _ = self.generate_dependency(override=False)
            dependency = random.choice(self.dependencies)
        return args + ["-ws", path, dependency], path

    @staticmethod
    def random_bool() -> bool:
        return bool(random.getrandbits(1))

    @staticmethod
    def select_and_generate(
        choices: List[Tuple[Callable[[Any], Tuple[List[str], str]], List[Callable]]]
    ):
        producer, args_producer = random.choice(choices)
        return producer(*list(map(lambda f: f(), args_producer)))

    def generate_others(self) -> List[str]:
        args = []
        for i in range(random.randint(0, self.max_others)):
            arg, _ = self.select_and_generate(self.responders + self.others)
            args += arg
        return args

    def generate_data(self) -> List[str]:
        if self.data is not None:
            return ["-d", f'"self.data"']
        else:
            if random.getrandbits(1):
                return []
            return ["-d", f'"{self.json_fuzzer.fuzz()}"']

    def generate_target(
        self, excluded: Optional[List[Callable]] = None
    ) -> Tuple[List[str], str]:
        excluded = excluded or list()
        return self.select_and_generate(
            list(filter(lambda f: f[0] not in excluded, self.responders))
        )

    def generate_request(
        self,
        target_arguments: List[str],
        target_path: str,
    ):
        arguments = self.generate_others()
        data_arguments = self.generate_data()
        return " ".join(
            arguments
            + target_arguments
            + data_arguments
            + ["-u", target_path, "-m", self.paths[target_path]]
        )


class FastAPI2SystemtestGenerator(FastAPIDefaultSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        self.reset()
        return (
            self.generate_request(*self.generate_websocket(override=True)),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        self.reset()
        if True or random.getrandbits(1):  # TODO remove when alternatives exist
            return (
                self.generate_request(*self.generate_websocket(override=False)),
                TestResult.PASSING,
            )
        else:
            return (
                self.generate_request(
                    *self.generate_target(excluded=[self.generate_websocket])
                ),
                TestResult.PASSING,
            )


class FastAPI3SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI4SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI5SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI6SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI7SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI8SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI9SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI10SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI1UnittestGenerator(UnittestGenerator, FastAPI1TestGenerator):
    def __init__(self):
        UnittestGenerator.__init__(self)
        FastAPI1TestGenerator.__init__(self)

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(
            """
@staticmethod
def run_test(obj=None, include=None, exclude=None, by_alias=None, skip_defaults=None, exclude_unset=None, 
    exclude_defaults=None, include_none=None, exclude_none=None, custom_encoder=None, sqlalchemy_safe=None): 
    parameters = dict()
    if obj is not None:
        parameters["obj"] = obj
    if include is not None:
        parameters["include"] = include
    if exclude is not None:
        parameters["exclude"] = exclude
    if by_alias is not None:
        parameters["by_alias"] = False
    if skip_defaults is not None:
        parameters["skip_defaults"] = True
    if exclude_unset is not None:
        parameters["exclude_unset"] = True
    if exclude_defaults is not None:
        parameters["exclude_defaults"] = True
    if include_none is not None:
        parameters["include_none"] = False
    if exclude_none is not None:
        parameters["exclude_none"] = True
    if custom_encoder is not None:
        parameters["custom_encoder"] = custom_encoder
    if sqlalchemy_safe is not None:
        parameters["sqlalchemy_safe"] = False
    jsonable_encoder(**parameters)

class Model(BaseModel):
    foo: str = Field(..., alias="foo")
    bar: str = "bar"
    bla: str = "bla"

    class Config:
        use_enum_values = True
"""
        ).body

    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            """
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
try:
    from pydantic import Field
except ImportError:
    from pydantic import Schema as Field
"""
        ).body

    def _generate_test(self, failing=False):
        args = [f"obj={self._generate_default_object(set_self=True)}"]
        if random.getrandbits(1):
            args.append(
                f"include=[{', '.join([repr(x) for x in self._get_keys(m=1)])}]"
            )
        if random.getrandbits(1):
            args.append(
                f"exclude=[{', '.join([repr(x) for x in self._get_keys(m=1)])}]"
            )
        if random.getrandbits(1):
            args.append("by_alias=True")
        if random.getrandbits(1):
            args.append("skip_defaults=True")
        if random.getrandbits(1):
            args.append("exclude_unset=True")
        if random.getrandbits(1):
            args.append("custom_encoder={str: repr}")
        if random.getrandbits(1):
            args.append("sqlalchemy_safe=True")
        if failing:
            if random.getrandbits(1):
                args.append("exclude_defaults=True")
                if random.getrandbits(1):
                    args.append("exclude_none=True")
            else:
                args.append("exclude_none=True")
                if random.getrandbits(1):
                    args.append("exclude_defaults=True")

        test = self.get_empty_test()
        test.body = ast.parse(f"self.run_test({', '.join(args)})").body
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._generate_test(failing=True), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._generate_test(failing=False), TestResult.PASSING


class FastAPI2UnittestGenerator(UnittestGenerator):
    def __init__(self):
        super().__init__()
        self.string_fuzzer = GrammarFuzzer(grammar_request, start_symbol="<json_str>")
        self.json_fuzzer = GrammarFuzzer(grammar_request, start_symbol="<json>")

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(
            """
@staticmethod
def run_test(mode="get", url="/", data=None, depend=None, override=None):
    app = FastAPI()
    router = APIRouter()

    depend = "Dependency" if depend is None else depend

    async def dependency():
        return depend

    @app.get("/get", response_model=str)
    def get_valid():
        return f"get_{depend}"

    @app.post("/post", response_model=str)
    def get_valid():
        return f"post_{depend}"

    @router.websocket("/")
    async def router_ws_decorator_depends(
        websocket_: WebSocket, data_=Depends(dependency)
    ):
        await websocket_.accept()
        await websocket_.send_text(data_)
        await websocket_.close()

    if override is not None:
        app.dependency_overrides[dependency] = lambda: override

    app.include_router(router, prefix="/router")

    client = TestClient(app)

    if mode == "websocket":
        with client.websocket_connect(url) as websocket:
            return websocket.receive_text(), 200
    elif data is not None:
        response = getattr(client, mode)(url, json=data)
        return response.json(), response.status_code
    else:
        response = getattr(client, mode)(url)
        return response.json(), response.status_code"""
        ).body

    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            """
from fastapi import APIRouter, Depends, FastAPI
try:
    from fastapi import WebSocket
except ImportError:
    from starlette.websockets import WebSocket
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient
    """
        ).body

    def _get_test(
        self, arguments: List[str], expected_response: str, expected_status: int = 200
    ):
        test = self.get_empty_test()
        test.body = ast.parse(
            f"""
response, status = self.run_test({', '.join(arguments)})
self.assertEqual({expected_response}, response)
self.assertEqual({expected_status}, status)
            """
        ).body
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        expected = self.string_fuzzer.fuzz()
        arguments = ['"websocket"', '"/router/"', f"override={expected}"]
        if random.getrandbits(1):
            arguments.append(f"data={self.json_fuzzer.fuzz()}")
        return self._get_test(arguments, expected), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        value = self.string_fuzzer.fuzz()
        status = 200
        if random.getrandbits(1):
            expected = value
            arguments = ["websocket", "/router/", f"depend={value}"]
        else:
            p = random.random()
            e = value.replace('"', "")
            if p <= 0.45:
                expected = f'"get_{e}"'
                arguments = ['"get"', '"/get"', f"depend={value}"]
            elif p <= 0.9:
                expected = f'"post_{e}"'
                arguments = ['"post"', '"/post"', f"depend={value}"]
            else:
                expected = '{"detail": "Method Not Allowed"}'
                if p <= 0.95:
                    arguments = ['"get"', '"/post"', f"depend={value}"]
                    status = 405
                else:
                    arguments = ['"post"', '"/get"', f"depend={value}"]
                    status = 405

        if random.random() < 0.1:
            arguments.append(f"override={value}")
        if random.getrandbits(1):
            arguments.append(f"data={self.json_fuzzer.fuzz()}")
        return (
            self._get_test(arguments, expected, expected_status=status),
            TestResult.PASSING,
        )


class FastAPI3UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


class FastAPI4UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


class FastAPI5UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


class FastAPI6UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


class FastAPI7UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


class FastAPI8UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


class FastAPI9UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


class FastAPI10UnittestGenerator(UnittestGenerator):
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass


grammar_jsonable_encoder: Grammar = clean_up(
    dict(
        CLI_GRAMMAR,
        **{
            "<start>": ["<options>"],
            "<flag>": [
                "-<by_alias>",
                "-<skip_defaults>",
                "-<exclude_unset>",
                "-<exclude_defaults>",
                "-<include_none>",
                "-<exclude_none>",
                "-<sqlalchemy_safe>",
            ],
            "<op>": [
                "-<obj>",
                "-<include>",
                "-<exclude>",
                "-<custom_encoder>",
            ],
            # OPTIONS
            "<obj>": get_possible_options("o", "<object>"),
            "<include>": get_possible_options("i", "<key_list>"),
            "<exclude>": get_possible_options("e", "<key_list>"),
            "<custom_encoder>": get_possible_options("c", "<custom_encoders>"),
            "<by_alias>": ["a"],
            "<skip_defaults>": ["s"],
            "<exclude_unset>": ["u"],
            "<exclude_defaults>": ["d"],
            "<include_none>": ["ni"],
            "<exclude_none>": ["ne"],
            "<sqlalchemy_safe>": ["q"],
            # MODEL
            "<object>": ["<dict>", "<model>"],
            "<dict>": ["{}", '"{}"', '"{<dict_entries>}"'],
            "<dict_entries>": ["<dict_entry>", "<dict_entries>,<dict_entry>"],
            "<dict_entry>": ["'<key>':<json_str>"],
            "<model>": ["Model()", '"Model()"', '"Model(<parameters>)"'],
            "<parameters>": ["<parameter>", "<parameters>,<parameter>"],
            "<parameter>": ["<key>=<json_str>"],
            # LISTS
            "<key_list>": ["<key>", "<key_list>,<key>"],
            # ENCODERS
            "<custom_encoders>": ["{str:repr}"],
            # UTILS
            "<key>": ["foo", "bar", "bla", "da"],
            "<json_str>": ["''", "'<chars>'"],
            "<chars>": ["<char>", "<chars><char>"],
            "<char>": srange(string.ascii_letters + string.digits + "_ "),
        },
    )
)

assert is_valid_grammar(grammar_jsonable_encoder)

grammar_request: Grammar = clean_up(
    dict(
        CLI_GRAMMAR,
        **{
            "<start>": ["<options>"],
            "<op>": [
                "-<websocket>",
                "-<dependency>",
                "-<override>",
                "-<url>",
                "-<data>",
                "-<mode>",
                "-<item>",
                "-<model_a>",
                "-<model_b>",
                "-<get>",
                "-<post>",
                "-<alias>",
            ],
            # OPTIONS
            "<websocket>": get_possible_options("ws", "<arg><sep><arg>"),
            "<dependency>": get_possible_options("ds", "<arg>"),
            "<override>": get_possible_options("os", "<arg><sep><arg>"),
            "<url>": get_possible_options("u", "<arg>"),
            "<data>": get_possible_options("d", "<json>"),
            "<mode>": get_possible_options("m", "<r_mode>"),
            "<item>": get_possible_options("item", "<arg><sep><float><sep><integer>"),
            "<model_a>": get_possible_options("ma", "<arg><sep><arg>"),
            "<model_b>": get_possible_options("mb", "<arg>"),
            "<get>": get_possible_options("gs", "<arg><sep><model>"),
            "<post>": get_possible_options("ps", "<arg><sep><model>"),
            "<alias>": get_possible_options("a", "<arg>"),
            # UTILS
            "<r_mode>": ["get", "post", "websocket"],
            "<json>": ["<json_>", '"<json_>"', "'<json_>'"],
            "<json_>": ["<json_object>", "<json_list>", "<json_value>"],
            "<json_object>": ["{}", "{<pairs>}"],
            "<pairs>": ["<pair>", "<pairs>,<pair>"],
            "<pair>": ["<key>:<json_value>"],
            "<json_list>": ["[]", "[<json_values>]"],
            "<json_values>": ["<json_value>", "<json_values>,<json_value>"],
            "<json_value>": ["<float>", "<json_str>", "<json_object>", "<json_list>"],
            "<key>": ["<json_str>"],
            "<json_str>": ['\\"\\"', '\\"<chars>\\"', '""', '"<chars>"'],
            "<chars>": ["<char>", "<chars><char>"],
            "<char>": srange(string.ascii_letters + string.digits + "_"),
            "<model>": [
                "ModelA",
                "ModelB",
                "ModelCA",
                "ModelCB",
                "Item",
                "OtherItem",
                "List[Item]",
                "List[OtherItem]",
            ],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_request)

grammar_request_generic: Grammar = clean_up(
    dict(
        CLI_GRAMMAR,
        **{
            "<start>": ["<options>"],
            "<option>": ["<op>"],
            "<op>": [
                "-<websocket>",
                "-<dependency>",
                "-<override>",
                "-<get>",
                "-<post>",
                "-<url>",
                "-<data>",
                "-<mode>",
                "-<item>",
                "-<model_a>",
                "-<model_b>",
                "-<get>",
                "-<post>",
                "-<alias>",
            ],
            # OPTIONS
            "<websocket>": get_possible_options("ws", "<arg><sep><arg>"),
            "<dependency>": get_possible_options("ds", "<arg>"),
            "<override>": get_possible_options("os", "<arg><sep><arg>"),
            "<url>": get_possible_options("u", "<arg>"),
            "<data>": get_possible_options("d", "<arg>"),
            "<mode>": get_possible_options("m", "<arg>"),
            "<item>": get_possible_options("item", "<arg><sep><arg><sep><arg>"),
            "<model_a>": get_possible_options("ma", "<arg><sep><arg>"),
            "<model_b>": get_possible_options("mb", "<arg>"),
            "<get>": get_possible_options("gs", "<arg><sep><arg>"),
            "<post>": get_possible_options("ps", "<arg><sep><arg>"),
            "<alias>": get_possible_options("a", "<arg>"),
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_request_generic)
