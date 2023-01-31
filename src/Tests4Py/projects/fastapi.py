import queue
import string
import subprocess
import traceback
from abc import ABC
from os import PathLike
from pathlib import Path
from typing import List, Optional, Tuple

from fuzzingbook.Grammars import Grammar, is_valid_grammar, srange
from isla.derivation_tree import DerivationTree

from Tests4Py.framework.constants import Environment, HARNESS_FILE
from Tests4Py.grammars.utils import GrammarVisitor
from Tests4Py.projects import Project, Status, TestingFramework, TestStatus
from Tests4Py.tests.generator import UnittestGenerator, SystemtestGenerator
from Tests4Py.tests.utils import API, ExpectErrAPI, TestResult


class FastAPI(Project):
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
        grammar: Grammar = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="fastapi",
            github_url="https://github.com/tiangolo/fastapi",
            status=Status.OK,
            cause="N.A.",
            python_version="3.8.3",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version="3.8.4",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar_request if grammar is None else grammar,
        )  # TODO adjust parameters


def register():
    FastAPI(
        bug_id=1,
        buggy_commit_id="766157bfb4e7dfccba09ab398e8ec444d14e947c",
        fixed_commit_id="3397d4d69a9c2d64c1219fcbf291ea5697a4abb8",
        test_file=[Path("tests", "test_jsonable_encoder.py")],
        test_cases=["tests/test_jsonable_encoder.py::test_encode_model_with_default"],
        api=FastAPI1API(
            (
                b"TypeError: jsonable_encoder() got an unexpected keyword argument 'exclude_defaults'",
                b"TypeError: jsonable_encoder() got an unexpected keyword argument 'exclude_none'",
            )
        ),
        systemtests=FastAPI1SystemtestGenerator(),
        grammar=grammar_jsonable_encoder,
    )
    FastAPI(
        bug_id=2,
        buggy_commit_id="210af1fd3dc0f612a08fa02a0cb3f5adb81e5bfb",
        fixed_commit_id="02441ff0313d5b471b662293244c53e712f1243f",
        test_file=[Path("tests", "test_ws_router.py")],
        test_cases=["tests/test_ws_router.py::test_router_ws_depends_with_override"],
        systemtests=FastAPI2SystemtestGenerator(),
        api=FastAPI2API(),
    )
    FastAPI(
        bug_id=3,
        buggy_commit_id="869c7389e22dc9ad659940fa271da76c4f3ba3b1",
        fixed_commit_id="aea04ee32ee1942e6e1a904527bb8da6ba76abd9",
        test_file=[Path("tests", "test_serialize_response_model.py")],
        test_cases=[
            "tests/test_serialize_response_model.py::test_valid",
            "tests/test_serialize_response_model.py::test_coerce",
            "tests/test_serialize_response_model.py::test_validlist",
            "tests/test_serialize_response_model.py::test_validdict",
            "tests/test_serialize_response_model.py::test_valid_exclude_unset",
            "tests/test_serialize_response_model.py::test_coerce_exclude_unset",
            "tests/test_serialize_response_model.py::test_validlist_exclude_unset",
            "tests/test_serialize_response_model.py::test_validdict_exclude_unset",
        ],
        api=FastAPI3API(),
        systemtests=FastAPI3SystemtestGenerator(),
    )
    FastAPI(
        bug_id=4,
        buggy_commit_id="7ccd81f70653857bd8f3a15ee946aa3fb0edc2cb",
        fixed_commit_id="74c4d1c1dbe6bfdb05d6e4fc767ffe062398f0a3",
        test_file=[Path("tests", "test_param_in_path_and_dependency.py")],
        test_cases=["tests/test_param_in_path_and_dependency.py::test_reused_param"],
        api=FastAPI4API(),
        systemtests=FastAPI4SystemtestGenerator(),
    )
    FastAPI(
        bug_id=5,
        buggy_commit_id="7cea84b74ca3106a7f861b774e9d215e5228728f",
        fixed_commit_id="75a07f24bf01a31225ee687f3e2b3fc1981b67ab",
        test_file=[Path("tests", "test_filter_pydantic_sub_model.py")],
        test_cases=["tests/test_filter_pydantic_sub_model.py::test_filter_sub_model"],
        api=FastAPI5API(),
        systemtests=FastAPI5SystemtestGenerator(),
    )
    FastAPI(
        bug_id=6,
        buggy_commit_id="5db99a27cf640864b4793807811848698c5ff4a2",
        fixed_commit_id="874d24181e779ebc6e1c52afb7d6598f863fd6a8",
        test_file=[Path("tests", "test_forms_from_non_typing_sequences.py")],
        test_cases=[
            "tests/test_forms_from_non_typing_sequences.py::test_python_list_param_as_form",
            "tests/test_forms_from_non_typing_sequences.py::test_python_set_param_as_form",
            "tests/test_forms_from_non_typing_sequences.py::test_python_tuple_param_as_form",
        ],
        api=FastAPI6API(),
        systemtests=FastAPI6SystemtestGenerator(),
    )
    FastAPI(
        bug_id=7,
        buggy_commit_id="cc4c13e4ae3f65fc76c23962b316df4a60e0c7e0",
        fixed_commit_id="19c77e35bdde33aeec1eb2cfa680f95016492b69",
        test_file=[Path("tests", "test_multi_body_errors.py")],
        test_cases=[
            "tests/test_multi_body_errors.py::test_jsonable_encoder_requiring_error"
        ],
        api=FastAPI7API(),
        systemtests=FastAPI7SystemtestGenerator(),
    )
    FastAPI(
        bug_id=8,
        buggy_commit_id="fdb6d43e103bcf7a7325d796e37c9435c9460e4c",
        fixed_commit_id="dd963511d699b463b416408a0ad705b3dda0d067",
        test_file=[Path("tests", "test_custom_route_class.py")],
        test_cases=["tests/test_custom_route_class.py::test_route_classes"],
        api=FastAPI8API(),
        systemtests=FastAPI8SystemtestGenerator(),
    )
    FastAPI(
        bug_id=9,
        buggy_commit_id="a7a92bc63768ccee3f3afc2b73b2c581928dfe75",
        fixed_commit_id="c5817912d2be25bb310bf9da517882f57bbe7bb5",
        test_file=[Path("tests", "test_request_body_parameters_media_type.py")],
        test_cases=[
            "tests/test_request_body_parameters_media_type.py::test_openapi_schema"
        ],
    )
    FastAPI(
        bug_id=10,
        buggy_commit_id="b77a43bcac3ec8e7edbe82543e777c60ae85c178",
        fixed_commit_id="06eb4219345a77d23484528c9d164eb8d2097fec",
        test_file=[Path("tests", "test_skip_defaults.py")],
        test_cases=["tests/test_skip_defaults.py::test_return_defaults"],
    )
    FastAPI(
        bug_id=11,
        buggy_commit_id="bf229ad5d830eb5320f966d51a55e590e8d57008",
        fixed_commit_id="38495fffa560fa57a8f0e6437d8e43c36c8e5612",
        test_file=[
            Path("tests", "test_union_body.py"),
            Path("tests", "test_union_inherited_body.py"),
        ],
        test_cases=[
            "tests/test_union_body.py::test_item_openapi_schema",
            "tests/test_union_body.py::test_post_other_item",
            "tests/test_union_body.py::test_post_item",
            "tests/test_union_inherited_body.py::test_inherited_item_openapi_schema",
            "tests/test_union_inherited_body.py::test_post_extended_item",
            "tests/test_union_inherited_body.py::test_post_item",
        ],
    )
    FastAPI(
        bug_id=12,
        buggy_commit_id="d61f5e4b555b123bf222503fc0e076cbae6a7ebc",
        fixed_commit_id="d262f6e9296993e528e2327f0a73f7bf5514e7c6",
        test_file=[Path("tests", "test_security_http_bearer_optional.py")],
        test_cases=[
            "tests/test_security_http_bearer_optional.py::test_security_http_bearer_incorrect_scheme_credentials"
        ],
    )
    FastAPI(
        bug_id=13,
        buggy_commit_id="6f7f9268f6b03f42831dcfeaa5c15ba9813333ec",
        fixed_commit_id="c8df3ae57c57e119d115dd3c1f44efa78de1022a",
        test_file=[Path("tests", "test_additional_responses_router.py")],
        test_cases=["tests/test_additional_responses_router.py::test_openapi_schema"],
    )
    FastAPI(
        bug_id=14,
        buggy_commit_id="2ddb804940bbcad4ed730b2a910c8fd3c1167127",
        fixed_commit_id="b7d184363fad5f6b55d15ec3a3a844aa81092bbd",
        test_file=[Path("tests", "test_additional_properties.py")],
        test_cases=[
            "tests/test_additional_properties.py::test_additional_properties_schema"
        ],
    )
    FastAPI(
        bug_id=15,
        buggy_commit_id="b16ca54c30644667ab9f65a712704850666a039c",
        fixed_commit_id="6d77e2ac5f2cadc63424f2d85d8d8cded2975922",
        test_file=[Path("tests", "test_ws_router.py")],
        test_cases=[
            "tests/test_ws_router.py::test_router",
            "tests/test_ws_router.py::test_prefix_router",
        ],
    )
    FastAPI(
        bug_id=16,
        buggy_commit_id="92c825be6a7362099400c9c3fe8b01ea13add3dc",
        fixed_commit_id="9745a5d1ae86a7fefacf79bdde8e5dd2d59fa2f4",
        test_file=[
            Path("tests", "test_datetime_custom_encoder.py"),
            Path("tests", "test_jsonable_encoder.py"),
        ],
        test_cases=["tests/test_jsonable_encoder.py::test_encode_model_with_config"],
    )
    # TODO implement the 16 bugs of fastapi


class FastAPI1API(ExpectErrAPI):
    pass


class FastAPIDefaultAPI(API, GrammarVisitor):
    """ """

    def __init__(self, default_timeout: int = 5):
        API.__init__(self, default_timeout=default_timeout)
        GrammarVisitor.__init__(self, grammar_request)
        self.path = None
        self.mode = None
        self.alias = False
        self.override = False

    def visit_options(self, node: DerivationTree):
        self.path = None
        self.mode = None
        self.alias = False
        self.override = False
        self.generic_visit(node)

    def visit_alias(self, node: DerivationTree):
        self.alias = True

    def visit_override(self, node: DerivationTree):
        self.override = True

    def visit_url(self, node: DerivationTree):
        self.path = node.children[1].to_string()

    def visit_mode(self, node: DerivationTree):
        self.mode = node.children[1].to_string()

    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return False

    def fallback_condition(self, process: subprocess.CompletedProcess) -> bool:
        return False

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return False

    def fallback_contains(self, process: subprocess.CompletedProcess) -> bool:
        return False

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        try:
            with open(system_test_path, "r") as fp:
                test = fp.read()
            if test:
                self.visit_source(test)
                test = test.split("\n")
            else:
                test = []
            process = subprocess.run(
                ["python", HARNESS_FILE] + test,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.default_timeout,
                env=environ,
            )
            if self.condition(process) and self.contains(process):
                return TestResult.FAILING
            else:
                if self.fallback_condition(process) and self.fallback_contains(process):
                    return TestResult.FAILING
                elif self.error_handling(process):
                    print(process)
                    return TestResult.UNDEFINED
                else:
                    return TestResult.PASSING
        except subprocess.TimeoutExpired:
            return TestResult.UNDEFINED
        except Exception as e:
            traceback.print_exception(e)
            return TestResult.UNDEFINED

    def error_handling(self, process) -> bool:
        return process.returncode != 0 and process.returncode != 200


class FastAPI2API(FastAPIDefaultAPI):
    def condition(self, process: subprocess.CompletedProcess) -> bool:
        return self.mode == "websocket" and self.path == "/router/" and self.override

    def contains(self, process: subprocess.CompletedProcess) -> bool:
        return b"Overridden" not in process.stdout

    def fallback_condition(self, process: subprocess.CompletedProcess) -> bool:
        return (
            self.mode == "websocket" and self.path == "/router/" and not self.override
        )

    def fallback_contains(self, process: subprocess.CompletedProcess) -> bool:
        return b"Dependency" not in process.stdout


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
            and b"aliased_name" in process.stderr
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


class FastAPISystemtestGenerator(SystemtestGenerator, ABC):
    pass


class FastAPI1SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


class FastAPI2SystemtestGenerator(FastAPISystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pass

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass


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


grammar_jsonable_encoder: Grammar = {
    "<start>": ["<options>"],
    "<options>": ["", "<option_list>"],
    "<option_list>": ["<option>", "<option_list>\n<option>"],
    "<option>": [
        "<obj>",
        "<include>",
        "<exclude>",
        "<by_alias>",
        "<skip_defaults>",
        "<exclude_unset>",
        "<exclude_defaults>",
        "<include_none>",
        "<exclude_none>",
        "<custom_encoder>",
        "<sqlalchemy_safe>",
    ],
    # OPTIONS
    "<obj>": ["-o<object>"],
    "<include>": ["-i<key_list>"],
    "<exclude>": ["-e<key_list>"],
    "<by_alias>": ["-a"],
    "<skip_defaults>": ["-s"],
    "<exclude_unset>": ["-u"],
    "<exclude_defaults>": ["-d"],
    "<include_none>": ["-ni"],
    "<exclude_none>": ["-ne"],
    "<custom_encoder>": ["-c<custom_encoders>"],
    "<sqlalchemy_safe>": ["-q"],
    # MODEL
    "<object>": ["<dict>", "<model>"],
    "<dict>": ["{}", "{<dict_entries>}"],
    "<dict_entries>": ["<dict_entry>", "<dict_entries>,<dict_entry>"],
    "<dict_entry>": ["'<key>':<str>"],
    "<model>": ["Model()", "Model(<parameters>)"],
    "<parameters>": ["<parameter>", "<parameters>,<parameter>"],
    "<parameter>": ["<key>=<str>"],
    # LISTS
    "<key_list>": ["<key>", "<key_list>,<key>"],
    # ENCODERS
    "<custom_encoders>": ["{str:repr}"],
    # UTILS
    "<key>": ["foo", "bar", "bla", "da"],
    "<str>": ["''", "'<chars>'"],
    "<chars>": ["<char>", "<chars><char>"],
    "<char>": srange(string.ascii_letters + string.digits + "_ "),
}

assert is_valid_grammar(grammar_jsonable_encoder)

grammar_request: Grammar = {
    "<start>": ["<options>"],
    "<options>": ["", "<option_list>"],
    "<option_list>": ["<option>", "<option_list>\n<option>"],
    "<option>": [
        "<url>",
        "<mode>",
        "<data>",
        "<alias>",
        "<override>",
        "<users>",
    ],
    # OPTIONS
    "<url>": ["-p<path>"],
    "<mode>": ["-m<r_mode>"],
    "<data>": ["-d<json>"],
    "<alias>": ["-a"],
    "<override>": ["-o"],
    "<users>": ["-u"],
    # UTILS
    "<path>": ["/<chars>", "/<chars>/", "/<chars><path>"],
    "<r_mode>": ["get", "post", "websocket"],
    "<json>": ["<json_object>", "<json_list>", "<json_value>"],
    "<json_object>": ["{}", "{<pairs>}"],
    "<pairs>": ["<pair>", "<pairs>,<pair>"],
    "<pair>": ["<key>:<json_value>"],
    "<json_list>": ["[]", "[<json_values>]"],
    "<json_values>": ["<json_value>", "<json_values>,<json_value>"],
    "<json_value>": ["<number>", "<str>", "<json_object>", "<json_list>"],
    "<key>": ["<str>"],
    "<str>": ['""', '"<chars>"'],
    "<chars>": ["<char>", "<chars><char>"],
    "<char>": srange(string.ascii_letters + string.digits + "_-. "),
    "<number>": ["<int>", "<float>"],
    "<int>": ["<nonzero><digits>", "-<nonzero><digits>", "0", "-0"],
    "<digit>": srange(string.digits),
    "<digits>": ["", "<digits><digit>"],
    "<nonzero>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<float>": ["<int>.<digit><digits>"],
}

assert is_valid_grammar(grammar_request)
