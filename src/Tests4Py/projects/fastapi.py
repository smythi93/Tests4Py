from os import PathLike
from pathlib import Path
from typing import List, Optional

from Tests4Py.grammars import python
from Tests4Py.projects import Project, Status, TestingFramework, TestStatus
from Tests4Py.tests.generator import UnittestGenerator, SystemtestGenerator
from Tests4Py.tests.utils import API, TestResult


class FastAPI(Project):

    def __init__(self, bug_id: int, buggy_commit_id: str, fixed_commit_id: str, test_file: List[Path], test_cases: List[str],
                 test_status_fixed: TestStatus = TestStatus.PASSING,
                 test_status_buggy: TestStatus = TestStatus.FAILING,
                 unittests: Optional[UnittestGenerator] = None,
                 systemtests: Optional[SystemtestGenerator] = None,
                 api: Optional[API] = None):
        super().__init__(bug_id=bug_id, project_name='fastapi', github_url='https://github.com/tiangolo/fastapi',
                         status=Status.OK, cause='N.A.',
                         python_version='3.8.3', python_path='', buggy_commit_id=buggy_commit_id,
                         fixed_commit_id=fixed_commit_id, testing_framework=TestingFramework.PYTEST,
                         test_file=test_file, test_cases=test_cases, darwin_python_version='3.8.4',
                         test_status_fixed=test_status_fixed, test_status_buggy=test_status_buggy,
                         unittests=unittests, systemtests=systemtests, api=api, grammar=None)  # TODO adjust parameters


def register():
    FastAPI(
        bug_id=1,
        buggy_commit_id='766157bfb4e7dfccba09ab398e8ec444d14e947c',
        fixed_commit_id='3397d4d69a9c2d64c1219fcbf291ea5697a4abb8',
        test_file=[Path('tests', 'test_jsonable_encoder.py')],
        test_cases=['tests/test_jsonable_encoder.py::test_encode_model_with_default'],
    )
    FastAPI(
        bug_id=2,
        buggy_commit_id='210af1fd3dc0f612a08fa02a0cb3f5adb81e5bfb',
        fixed_commit_id='02441ff0313d5b471b662293244c53e712f1243f',
        test_file=[Path('tests', 'test_ws_router.py')],
        test_cases=['tests/test_ws_router.py::test_router_ws_depends_with_override'],
    )
    FastAPI(
        bug_id=3,
        buggy_commit_id='869c7389e22dc9ad659940fa271da76c4f3ba3b1',
        fixed_commit_id='aea04ee32ee1942e6e1a904527bb8da6ba76abd9',
        test_file=[Path('tests', 'test_serialize_response_model.py')],
        test_cases=[
            'tests/test_serialize_response_model.py::test_valid',
            'tests/test_serialize_response_model.py::test_coerce',
            'tests/test_serialize_response_model.py::test_validlist',
            'tests/test_serialize_response_model.py::test_validdict',
            'tests/test_serialize_response_model.py::test_valid_exclude_unset',
            'tests/test_serialize_response_model.py::test_coerce_exclude_unset',
            'tests/test_serialize_response_model.py::test_validlist_exclude_unset',
            'tests/test_serialize_response_model.py::test_validdict_exclude_unset',
        ],
    )
    FastAPI(
        bug_id=4,
        buggy_commit_id='7ccd81f70653857bd8f3a15ee946aa3fb0edc2cb',
        fixed_commit_id='74c4d1c1dbe6bfdb05d6e4fc767ffe062398f0a3',
        test_file=[Path('tests', 'test_param_in_path_and_dependency.py')],
        test_cases=['tests/test_param_in_path_and_dependency.py::test_reused_param'],
    )
    FastAPI(
        bug_id=5,
        buggy_commit_id='7cea84b74ca3106a7f861b774e9d215e5228728f',
        fixed_commit_id='75a07f24bf01a31225ee687f3e2b3fc1981b67ab',
        test_file=[Path('tests', 'test_filter_pydantic_sub_model.py')],
        test_cases=['tests/test_filter_pydantic_sub_model.py::test_filter_sub_model'],
    )
    FastAPI(
        bug_id=6,
        buggy_commit_id='5db99a27cf640864b4793807811848698c5ff4a2',
        fixed_commit_id='874d24181e779ebc6e1c52afb7d6598f863fd6a8',
        test_file=[Path('tests', 'test_forms_from_non_typing_sequences.py')],
        test_cases=[
            'tests/test_forms_from_non_typing_sequences.py::test_python_list_param_as_form',
            'tests/test_forms_from_non_typing_sequences.py::test_python_set_param_as_form',
            'tests/test_forms_from_non_typing_sequences.py::test_python_tuple_param_as_form',
        ],
    )
    FastAPI(
        bug_id=7,
        buggy_commit_id='cc4c13e4ae3f65fc76c23962b316df4a60e0c7e0',
        fixed_commit_id='19c77e35bdde33aeec1eb2cfa680f95016492b69',
        test_file=[Path('tests', 'test_multi_body_errors.py')],
        test_cases=['tests/test_multi_body_errors.py::test_jsonable_encoder_requiring_error'],
    )
    FastAPI(
        bug_id=8,
        buggy_commit_id='fdb6d43e103bcf7a7325d796e37c9435c9460e4c',
        fixed_commit_id='dd963511d699b463b416408a0ad705b3dda0d067',
        test_file=[Path('tests', 'test_custom_route_class.py')],
        test_cases=['tests/test_custom_route_class.py::test_route_classes'],
    )
    FastAPI(
        bug_id=9,
        buggy_commit_id='a7a92bc63768ccee3f3afc2b73b2c581928dfe75',
        fixed_commit_id='c5817912d2be25bb310bf9da517882f57bbe7bb5',
        test_file=[Path('tests', 'test_request_body_parameters_media_type.py')],
        test_cases=['tests/test_request_body_parameters_media_type.py::test_openapi_schema'],
    )
    FastAPI(
        bug_id=10,
        buggy_commit_id='b77a43bcac3ec8e7edbe82543e777c60ae85c178',
        fixed_commit_id='06eb4219345a77d23484528c9d164eb8d2097fec',
        test_file=[Path('tests', 'test_skip_defaults.py')],
        test_cases=['tests/test_skip_defaults.py::test_return_defaults'],
    )
    FastAPI(
        bug_id=11,
        buggy_commit_id='bf229ad5d830eb5320f966d51a55e590e8d57008',
        fixed_commit_id='38495fffa560fa57a8f0e6437d8e43c36c8e5612',
        test_file=[Path('tests', 'test_union_body.py'), Path('tests', 'test_union_inherited_body.py')],
        test_cases=[
            'tests/test_union_body.py::test_item_openapi_schema',
            'tests/test_union_body.py::test_post_other_item',
            'tests/test_union_body.py::test_post_item',
            'tests/test_union_inherited_body.py::test_inherited_item_openapi_schema',
            'tests/test_union_inherited_body.py::test_post_extended_item',
            'tests/test_union_inherited_body.py::test_post_item',
        ],
    )
    FastAPI(
        bug_id=12,
        buggy_commit_id='d61f5e4b555b123bf222503fc0e076cbae6a7ebc',
        fixed_commit_id='d262f6e9296993e528e2327f0a73f7bf5514e7c6',
        test_file=[Path('tests', 'test_security_http_bearer_optional.py')],
        test_cases=[
            'tests/test_security_http_bearer_optional.py::test_security_http_bearer_incorrect_scheme_credentials'
        ],
    )
    FastAPI(
        bug_id=13,
        buggy_commit_id='6f7f9268f6b03f42831dcfeaa5c15ba9813333ec',
        fixed_commit_id='c8df3ae57c57e119d115dd3c1f44efa78de1022a',
        test_file=[Path('tests', 'test_additional_responses_router.py')],
        test_cases=['tests/test_additional_responses_router.py::test_openapi_schema'],
    )
    FastAPI(
        bug_id=14,
        buggy_commit_id='2ddb804940bbcad4ed730b2a910c8fd3c1167127',
        fixed_commit_id='b7d184363fad5f6b55d15ec3a3a844aa81092bbd',
        test_file=[Path('tests', 'test_additional_properties.py')],
        test_cases=['tests/test_additional_properties.py::test_additional_properties_schema'],
    )
    FastAPI(
        bug_id=15,
        buggy_commit_id='b16ca54c30644667ab9f65a712704850666a039c',
        fixed_commit_id='6d77e2ac5f2cadc63424f2d85d8d8cded2975922',
        test_file=[Path('tests', 'test_ws_router.py')],
        test_cases=[
            'tests/test_ws_router.py::test_router',
            'tests/test_ws_router.py::test_prefix_router'
        ],
    )
    FastAPI(
        bug_id=16,
        buggy_commit_id='92c825be6a7362099400c9c3fe8b01ea13add3dc',
        fixed_commit_id='9745a5d1ae86a7fefacf79bdde8e5dd2d59fa2f4',
        test_file=[Path('tests', 'test_datetime_custom_encoder.py'), Path('tests', 'test_jsonable_encoder.py')],
        test_cases=['tests/test_jsonable_encoder.py::test_encode_model_with_config'],
    )
    # TODO implement the 16 bugs of fastapi


class FastAPIAPI(API):

    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike) -> TestResult:
        return TestResult.UNKNOWN
