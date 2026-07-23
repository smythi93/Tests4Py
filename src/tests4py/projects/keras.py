import ast
import json
import math
import os
import random
import string
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple, Any

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up, INTEGER, NUMBER
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "keras"


class Keras(Project):
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
            github_url="https://github.com/keras-team/keras",
            status=Status.OK,
            python_version="3.7.8",
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
            grammar=grammar,
            loc=loc,
            included_files=[PROJECT_NAME],
            source_base=Path(PROJECT_NAME),
            test_base=Path("tests"),
            setup=[[PYTHON, "-m", "pip", "install", "-e", "."]],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )

    def patch(self, location: Path):
        if self.bug_id in (14, 15, 16, 17, 18, 19, 20, 21, 22):
            with open(location / "setup.py", "r") as fp:
                content = fp.read()
            content = content.replace(
                "keras_applications==1.0.4",
                "keras_applications==1.0.6"
                if self.bug_id in (21, 22)
                else "keras_applications==1.0.8",
            )
            content = content.replace(
                "keras_preprocessing==1.0.2",
                "keras_preprocessing==1.0.5",
            )
            with open(location / "setup.py", "w") as fp:
                fp.write(content)
        if self.bug_id == 23:
            with open(location / "setup.py", "r") as fp:
                content = fp.read()
            content = content.replace(
                "keras_applications==1.0.2", "keras_applications==1.0.6"
            )
            content = content.replace(
                "keras_preprocessing==1.0.1",
                "keras_preprocessing==1.0.5",
            )
            with open(location / "setup.py", "w") as fp:
                fp.write(content)


def register():
    Keras(
        bug_id=1,
        buggy_commit_id="331d5b0102ab0cc79cece1f03cc551d8105db3c9",
        fixed_commit_id="8e23a3ec47a2ccbf6cdd222a80886c6b9f17264f",
        test_files=[Path("tests", "keras", "initializers_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "initializers_test.py::test_statefulness[uniform]"
            ),
            os.path.join(
                "tests", "keras", "initializers_test.py::test_statefulness[orthogonal]"
            ),
            os.path.join(
                "tests",
                "keras",
                "initializers_test.py::test_statefulness[truncated_normal]",
            ),
            os.path.join(
                "tests", "keras", "initializers_test.py::test_statefulness[normal]"
            ),
            os.path.join(
                "tests",
                "keras",
                "initializers_test.py::test_statefulness[variance_scaling]",
            ),
        ],
        unittests=Keras1UnittestGenerator(),
        systemtests=Keras1SystemtestGenerator(),
        api=Keras1API(),
        grammar=grammar_1,
        loc=22638,
    )
    Keras(
        bug_id=2,
        buggy_commit_id="2f55055a9f053b35fa721d3eb75dd07ea5a5f1e3",
        fixed_commit_id="c24d16af155e20976bdf61e468ba760408e676ff",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "backend",
                "backend_test.py::TestBackend::test_in_top_k",
            )
        ],
        skip_tests=[
            "test_gradient",
            "test_elementwise_operations",
            "(test_function and not test_function_tf)",
            "test_resize_images_bilinear",
        ],
        unittests=Keras2UnittestGenerator(),
        systemtests=Keras2SystemtestGenerator(),
        api=Keras2API(),
        grammar=grammar_2,
        loc=22758,
    )
    Keras(
        bug_id=3,
        buggy_commit_id="c0d1709cbae3d05efc6dd224230012bc120be8e5",
        fixed_commit_id="c13d2723d01212d09dfdda39b0ad439803ec9230",
        test_files=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_sequential_model.py::test_clone_functional_model_with_multi_outputs",
            )
        ],
        unittests=Keras3UnittestGenerator(),
        systemtests=Keras3SystemtestGenerator(),
        api=Keras3API(),
        grammar=grammar_3,
        loc=22751,
    )
    Keras(
        bug_id=4,
        buggy_commit_id="b0bfd5201da2bfced84028bcc5bda05bdfd75af7",
        fixed_commit_id="4185cbb50bfcae9cc30b0fc7b67e81d67a50a8ac",
        test_files=[Path("tests", "keras", "optimizers_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "optimizers_test.py::test_tfoptimizer_pass_correct_named_params_to_native_tensorflow_optimizer",
            )
        ],
        unittests=Keras4UnittestGenerator(),
        systemtests=Keras4SystemtestGenerator(),
        api=Keras4API(),
        grammar=grammar_4,
        loc=22459,
    )
    Keras(
        bug_id=5,
        buggy_commit_id="b847b4601d608050bab6eccd049fce28b7bf1b1f",
        fixed_commit_id="e11c48d9ce3ee47bb8a966549b14cbd5b10ee70d",
        test_files=[Path("tests", "keras", "utils", "data_utils_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "utils", "data_utils_test.py::test_data_utils"
            )
        ],
        unittests=Keras5UnittestGenerator(),
        systemtests=Keras5SystemtestGenerator(),
        api=Keras5API(),
        grammar=grammar_5,
        loc=22261,
    )
    Keras(
        bug_id=6,
        buggy_commit_id="88af7d0c97497b5c3a198ee9416b2accfbc72c36",
        fixed_commit_id="4b54657ab4806b0aaef8f8eeb973edb83c3d3483",
        test_files=[
            Path("tests", "test_loss_masking.py"),
            Path("tests", "test_loss_weighting.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_loss_masking.py::test_masking_is_all_zeros")
        ],
        unittests=Keras6UnittestGenerator(),
        systemtests=Keras6SystemtestGenerator(),
        api=Keras6API(),
        grammar=grammar_6,
        loc=22060,
    )
    Keras(
        bug_id=7,
        buggy_commit_id="26b620fb37c885d60183f83abc744f43775ce75a",
        fixed_commit_id="c05ef1fd95a6024155ab59656fef8dac5a45c335",
        test_files=[Path("tests", "keras", "wrappers", "scikit_learn_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "wrappers",
                "scikit_learn_test.py::test_regression_predict_shape_correct_num_test_1",
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        unittests=Keras7UnittestGenerator(),
        systemtests=Keras7SystemtestGenerator(),
        api=Keras7API(),
        grammar=grammar_7,
        loc=21990,
    )
    Keras(
        bug_id=8,
        buggy_commit_id="87540a2a2f42e00c4a2ca7ca35d19f96e62e6cb0",
        fixed_commit_id="d78c982b326adeed6ac25200dc6892ff8f518ca6",
        test_files=[Path("tests", "keras", "engine", "test_topology.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "engine",
                "test_topology.py::test_layer_sharing_at_heterogeneous_depth_order",
            )
        ],
        skip_tests=[
            "test_recursion",
            "test_constant_initializer_with_numpy",
        ],
        unittests=Keras8UnittestGenerator(),
        systemtests=Keras8SystemtestGenerator(),
        api=Keras8API(),
        grammar=grammar_8,
        loc=22427,
    )
    Keras(
        bug_id=9,
        buggy_commit_id="0cd3b07eb5de1aaaad84d1ff7f7c2ed7dab4b23c",
        fixed_commit_id="0505393746d56ddacc34bb1c016dba79429c9ac9",
        test_files=[
            Path("tests", "test_doc_auto_generation.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_doc_auto_generation.py::test_doc_lists[docs_descriptor1]"
            ),
        ],
        unittests=Keras9UnittestGenerator(),
        systemtests=Keras9SystemtestGenerator(),
        api=Keras9API(),
        grammar=grammar_9,
        loc=22278,
    )
    Keras(
        bug_id=10,
        buggy_commit_id="8f41e41eda6e8ea96403cae5798a5a89c8bb5605",
        fixed_commit_id="c1c4afe60b1355a6c0e83577791a0423f37a3324",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "engine", "test_training.py::test_sample_weights"
            )
        ],
        unittests=Keras10UnittestGenerator(),
        systemtests=Keras10SystemtestGenerator(),
        api=Keras10API(),
        grammar=grammar_10,
        loc=22083,
    )
    Keras(
        bug_id=11,
        buggy_commit_id="36b9e4c055f32718a036cabaf767325b010c7485",
        fixed_commit_id="d6b5c5ebb410e3366c9d7aca41977a60134bfe10",
        test_files=[
            Path("tests", "integration_tests", "test_image_data_tasks.py"),
            Path("tests", "integration_tests", "test_temporal_data_tasks.py"),
        ],
        test_cases=[
            os.path.join(
                "tests",
                "integration_tests",
                "test_image_data_tasks.py::test_image_data_generator_training",
            ),
        ],
        unittests=Keras11UnittestGenerator(),
        systemtests=Keras11SystemtestGenerator(),
        api=Keras11API(),
        grammar=grammar_11,
        loc=21230,
    )
    Keras(
        bug_id=12,
        buggy_commit_id="6dff721a3a8755356b2e89d02ef63ad8ab38ec95",
        fixed_commit_id="6dff721a3a8755356b2e89d02ef63ad8ab38ec95",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_categorical_accuracy_correctness[shape1]",
            ),
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_categorical_accuracy_correctness[shape2]",
            ),
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=21126,
    )
    Keras(
        bug_id=13,
        buggy_commit_id="2bfd1f2c950df5fc3f40b903c1966f1b0a48bee4",
        fixed_commit_id="a07253d8269e1b750f0a64767cc9a07da8a3b7ea",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "engine", "test_training.py::test_model_methods"
            )
        ],
        unittests=Keras13UnittestGenerator(),
        systemtests=Keras13SystemtestGenerator(),
        api=Keras13API(),
        grammar=grammar_13,
        loc=21127,
    )
    Keras(
        bug_id=14,
        buggy_commit_id="98465b85d020f1326bcef7632f1261a9a7a84e92",
        fixed_commit_id="02bc5010a04bb11c8e91835cc9775c8149dec754",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_top_k_categorical_accuracy[y_pred1-y_true1]",
            )
        ],
        unittests=Keras14UnittestGenerator(),
        systemtests=Keras14SystemtestGenerator(),
        api=Keras14API(),
        grammar=grammar_14,
        loc=21024,
    )
    Keras(
        bug_id=15,
        buggy_commit_id="5b6243485acc20cc36f2db4f258512c332d691ec",
        fixed_commit_id="f60313e29657b2afb6a02f28dba5936bc0dd09e6",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join("tests", "keras", "test_callbacks.py::test_CSVLogger")
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=20893,
    )
    Keras(
        bug_id=16,
        buggy_commit_id="514aca20c6f076a86819d7180f36c3b2e8bcc33b",
        fixed_commit_id="fe38f9dfc8c732a77ac03507b63c79b1d2acfba2",
        test_files=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            os.path.join("tests", "keras", "test_sequential_model.py::test_sequential"),
            os.path.join(
                "tests",
                "keras",
                "test_sequential_model.py::test_sequential_deferred_build",
            ),
        ],
        unittests=Keras16UnittestGenerator(),
        systemtests=Keras16SystemtestGenerator(),
        api=Keras16API(),
        grammar=grammar_16,
        loc=20910,
    )
    Keras(
        bug_id=17,
        buggy_commit_id="c913b6da92f6ab9a3f4c897caa4085e782a14680",
        fixed_commit_id="5a6af4bc6d44e9adbc2a21804bfcd18c4ce849ef",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_categorical_accuracy_correctness",
            )
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=20691,
    )
    Keras(
        bug_id=18,
        buggy_commit_id="9400be98783135a1d42dd238f4e6c3aa048eceea",
        fixed_commit_id="244546c2fe5165b6770eb456afd5fac8878473c5",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "backend",
                "backend_test.py::TestBackend::test_function_tf_run_options_with_run_metadata",
            )
        ],
        skip_tests=[
            "test_gradient",
            "(test_function and not test_function_tf)",
            "test_in_top_k",
            "test_resize_images_bilinear",
            "test_spatial_2d_padding",
            "test_spatial_3d_padding",
            "test_batchnorm",
            "test_sparse_dot",
            "test_sparse_concat",
            "test_ctc_decode_beam_search",
        ],
        unittests=Keras18UnittestGenerator(),
        systemtests=Keras18SystemtestGenerator(),
        api=Keras18API(),
        grammar=grammar_18,
        loc=20677,
    )
    Keras(
        bug_id=19,
        buggy_commit_id="f9210387088fe91b5bc8999cf0cb41a0fe9eacf6",
        fixed_commit_id="66f8cc7ac4942f7f9fe0164a2a854a6264b87735",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_inconsistent_output_state_size",
            ),
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_minimal_rnn_cell_non_layer_multiple_states",
            ),
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_stacked_rnn_compute_output_shape",
            ),
        ],
        unittests=Keras19UnittestGenerator(),
        systemtests=Keras19SystemtestGenerator(),
        api=Keras19API(),
        grammar=grammar_19,
        loc=20718,
    )
    Keras(
        bug_id=20,
        buggy_commit_id="76da5f0a21ca98e4bf6706e182fb825243e76204",
        fixed_commit_id="6dd087ab73b09e449144ff17450cc14f981b9ac2",
        test_files=[Path("tests", "keras", "layers", "convolutional_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "convolutional_test.py::test_conv2d_transpose_dilation",
            )
        ],
        unittests=Keras20UnittestGenerator(),
        systemtests=Keras20SystemtestGenerator(),
        api=Keras20API(),
        grammar=grammar_20,
        loc=20699,
    )
    Keras(
        bug_id=21,
        buggy_commit_id="c7b7328cc99fd5d7c298e57c6020043451d89a61",
        fixed_commit_id="1fc585adb57f20a2acf69f0cd08b731259b8d2f8",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_callbacks.py::test_EarlyStopping_final_weights_when_restoring_model_weights",
            )
        ],
        unittests=Keras21UnittestGenerator(),
        systemtests=Keras21SystemtestGenerator(),
        api=Keras21API(),
        grammar=grammar_21,
        loc=20378,
    )
    Keras(
        bug_id=22,
        buggy_commit_id="54386efa549f850dff13f79fc3af67799a4e5d4f",
        fixed_commit_id="ee02d256611b17d11e37b86bd4f618d7f2a37d84",
        test_files=[Path("tests", "keras", "layers", "core_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "core_test.py::test_sequential_as_downstream_of_masking_layer",
            )
        ],
        unittests=Keras22UnittestGenerator(),
        systemtests=Keras22SystemtestGenerator(),
        api=Keras22API(),
        grammar=grammar_22,
        loc=20447,
    )
    Keras(
        bug_id=23,
        buggy_commit_id="3dcd9c767ce6875fc8b69c74971ac8a552e23131",
        fixed_commit_id="69c30a150f0b2caee7961ca1c0080960ef5ad6f6",
        test_files=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_sequential_model.py::test_nested_sequential_deferred_build",
            )
        ],
        unittests=Keras23UnittestGenerator(),
        systemtests=Keras23SystemtestGenerator(),
        api=Keras23API(),
        grammar=grammar_23,
        loc=20647,
    )
    Keras(
        bug_id=24,
        buggy_commit_id="d7884570b10951d156aa086ee29a4df9eab79cf3",
        fixed_commit_id="bcf0031b54d555179be81c088cc3df0a723d7907",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_callbacks.py::test_TensorBoard_multi_input_output",
            )
        ],
        unittests=Keras24UnittestGenerator(),
        systemtests=Keras24SystemtestGenerator(),
        api=Keras24API(),
        grammar=grammar_24,
        loc=23663,
    )
    Keras(
        bug_id=25,
        buggy_commit_id="b470a595f7278acf5e7e47521edf25d3c4f479f1",
        fixed_commit_id="84e168b5fa55933e02e767ff7c86fcc0232aecc6",
        test_files=[
            Path("tests", "keras", "applications", "imagenet_utils_test.py"),
        ],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "applications",
                "imagenet_utils_test.py::test_preprocess_input",
            )
        ],
        unittests=Keras25UnittestGenerator(),
        systemtests=Keras25SystemtestGenerator(),
        api=Keras25API(),
        grammar=grammar_25,
        loc=23708,
    )
    Keras(
        bug_id=26,
        buggy_commit_id="87417470c8168772559be0531e297120c569a422",
        fixed_commit_id="97d5fa920e4f8248128f7c1b460fd9bb20d3478f",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "backend",
                "backend_test.py::TestBackend::test_rnn_additional_states",
            )
        ],
        skip_tests=[
            "test_linear_operations",
            "test_gradient",
            "(test_function and not test_function_tf)",
            "test_elementwise_operations",
            "test_nn_operations",
            "test_in_top_k",
            "test_ctc_decode_beam_search",
            "test_batchnorm",
            "test_sparse_dot",
            "test_sparse_concat",
            "test_arange",
            "test_in_test_phase",
            "test_in_train_phase",
        ],
        unittests=Keras26UnittestGenerator(),
        systemtests=Keras26SystemtestGenerator(),
        api=Keras26API(),
        grammar=grammar_26,
        loc=23599,
    )
    Keras(
        bug_id=27,
        buggy_commit_id="49f5b931410bc2e56378f20a15e8ac919e0efb88",
        fixed_commit_id="b076e227da6beaf87d6c84eff1a92285e4662acf",
        test_files=[Path("tests", "keras", "layers", "wrappers_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "wrappers_test.py::test_Bidirectional_updates",
            ),
            os.path.join(
                "tests",
                "keras",
                "layers",
                "wrappers_test.py::test_Bidirectional_losses",
            ),
        ],
        unittests=Keras27UnittestGenerator(),
        systemtests=Keras27SystemtestGenerator(),
        api=Keras27API(),
        grammar=grammar_27,
        loc=23414,
    )
    Keras(
        bug_id=28,
        buggy_commit_id="6171b3656ebd9b6038f709ba83f7475de284ba4e",
        fixed_commit_id="5422fdd38baad36730cb6aeb946e17eeae6a551c",
        test_files=[Path("tests", "keras", "preprocessing", "sequence_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "sequence_test.py::test_TimeSeriesGenerator_doesnt_miss_any_sample",
            ),
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "sequence_test.py::test_TimeseriesGenerator",
            ),
        ],
        unittests=Keras28UnittestGenerator(),
        systemtests=Keras28SystemtestGenerator(),
        api=Keras28API(),
        grammar=grammar_28,
        loc=23235,
    )
    Keras(
        bug_id=29,
        buggy_commit_id="a341c014412cbfc86a9dd9816ae228e398dff3a2",
        fixed_commit_id="adc321b4d7a4e22f6bdb00b404dfe5e23d4887aa",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "metrics_test.py::test_stateful_metrics[dict]"
            )
        ],
        unittests=Keras29UnittestGenerator(),
        systemtests=Keras29SystemtestGenerator(),
        api=Keras29API(),
        grammar=grammar_29,
        loc=23191,
    )
    Keras(
        bug_id=30,
        buggy_commit_id="c08ef613af27da896cee168daeee5c6fad1980b6",
        fixed_commit_id="2c8d1d03599cc03243bce8f07ed9c4a3d5f384f9",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "engine",
                "test_training.py::test_model_with_external_loss",
            )
        ],
        unittests=Keras30UnittestGenerator(),
        systemtests=Keras30SystemtestGenerator(),
        api=Keras30API(),
        grammar=grammar_30,
        loc=23177,
    )
    Keras(
        bug_id=31,
        buggy_commit_id="ced81968b0e9d8b1389e6580721ac60d9cf3ca60",
        fixed_commit_id="e2a10a5e6e156a45e946c4d08db7133f997c1f9a",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "backend", "backend_test.py::TestBackend::test_ctc"
            )
        ],
        skip_tests=[
            "test_linear_operations",
            "test_gradient",
            "(test_function and not test_function_tf)",
            "test_elementwise_operations",
            "test_nn_operations",
            "test_in_top_k",
            "test_batchnorm",
            "test_ctc_decode_beam_search",
            "test_sparse_dot",
            "test_sparse_concat",
            "test_arange",
            "test_in_train_phase",
        ],
        unittests=Keras31UnittestGenerator(),
        systemtests=Keras31SystemtestGenerator(),
        api=Keras31API(),
        grammar=grammar_31,
        loc=23134,
    )
    Keras(
        bug_id=32,
        buggy_commit_id="a3d160b9467c99cbb27f9aa0382c759f45c8ee66",
        fixed_commit_id="709f791af201caaab4aa180bda259989087cfe47",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "test_callbacks.py::test_ReduceLROnPlateau_patience"
            ),
            os.path.join(
                "tests",
                "keras",
                "test_callbacks.py::test_ReduceLROnPlateau_backwards_compatibility",
            ),
        ],
        skip_tests=["tests_RemoteMonitor"],
        unittests=Keras32UnittestGenerator(),
        systemtests=Keras32SystemtestGenerator(),
        api=Keras32API(),
        grammar=grammar_32,
        loc=23124,
    )
    Keras(
        bug_id=33,
        buggy_commit_id="1c9a49781da2101507db23e2014e4e5d16bd2e52",
        fixed_commit_id="70ad0d6e4a569701ef106058397ad0540ec08340",
        test_files=[Path("tests", "keras", "preprocessing", "text_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "text_test.py::test_text_to_word_sequence_multichar_split",
            ),
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "text_test.py::test_text_to_word_sequence_unicode_multichar_split",
            ),
        ],
        unittests=Keras33UnittestGenerator(),
        systemtests=Keras33SystemtestGenerator(),
        api=Keras33API(),
        grammar=grammar_33,
        loc=23085,
    )
    Keras(
        bug_id=34,
        buggy_commit_id="7ef5244a2f1f7f7b76e3c804b82cbb20cdf4d139",
        fixed_commit_id="4b74fc5418944c9f449eb88ed4b40ada280fa5ca",
        test_files=[Path("tests", "test_multiprocessing.py")],
        test_cases=[
            os.path.join(
                "tests", "test_multiprocessing.py::test_multiprocessing_training"
            )
        ],
        unittests=Keras34UnittestGenerator(),
        systemtests=Keras34SystemtestGenerator(),
        api=Keras34API(),
        grammar=grammar_34,
        loc=23036,
    )
    Keras(
        bug_id=35,
        buggy_commit_id="06eaeebecfb73c23bfd531013ca172ee3bf5069c",
        fixed_commit_id="738819de0b7e6bc45abed8d0640f02b81c6ac4e9",
        test_files=[Path("tests", "keras", "preprocessing", "image_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "image_test.py::TestImage::test_directory_iterator",
            )
        ],
        unittests=Keras35UnittestGenerator(),
        systemtests=Keras35SystemtestGenerator(),
        api=Keras35API(),
        grammar=grammar_35,
        loc=22563,
    )
    Keras(
        bug_id=36,
        buggy_commit_id="85f011df5a5c0fcf1f01b39eca338eb6b7e58401",
        fixed_commit_id="fb1887d132a8ce8548ff53d868a6ba531cd63b34",
        test_files=[Path("tests", "keras", "layers", "convolutional_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "convolutional_test.py::test_separable_conv_1d",
            )
        ],
        unittests=Keras36UnittestGenerator(),
        systemtests=Keras36SystemtestGenerator(),
        api=Keras36API(),
        grammar=grammar_36,
        loc=22278,
    )
    Keras(
        bug_id=37,
        buggy_commit_id="81f6b3aa5b2b6215a533180e848a3b4dff851d03",
        fixed_commit_id="1d2ad790dd43a2d702176c1170b2f3fd592a385a",
        test_files=[Path("tests", "keras", "layers", "wrappers_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "wrappers_test.py::test_Bidirectional_state_reuse",
            )
        ],
        unittests=Keras37UnittestGenerator(),
        systemtests=Keras37SystemtestGenerator(),
        api=Keras37API(),
        grammar=grammar_37,
        loc=22237,
    )
    Keras(
        bug_id=38,
        buggy_commit_id="53ec990d54130dd0a457dd235c93d39de32d571d",
        fixed_commit_id="64f80d6077edd5f277a1181df94bf4510ea0517a",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_minimal_rnn_cell_layer",
            )
        ],
        unittests=Keras38UnittestGenerator(),
        systemtests=Keras38SystemtestGenerator(),
        api=Keras38API(),
        grammar=grammar_38,
        loc=22146,
    )
    Keras(
        bug_id=39,
        buggy_commit_id="3a431ea52d090fb3ef8a1e0e5d7f796d9a42e097",
        fixed_commit_id="a5ecde595c47f35fd7293d52eba48efd687ca94e",
        test_files=[Path("tests", "keras", "utils", "generic_utils_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "utils", "generic_utils_test.py::test_progbar"
            )
        ],
        unittests=Keras39UnittestGenerator(),
        systemtests=Keras39SystemtestGenerator(),
        api=Keras39API(),
        grammar=grammar_39,
        loc=22117,
    )
    Keras(
        bug_id=40,
        buggy_commit_id="871007dbb0e6211459b9d16244cc3c9683459df7",
        fixed_commit_id="4cad455ef4da600c96ddc69800bab39d0e52b677",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_stacked_rnn_compute_output_shape",
            )
        ],
        unittests=Keras40UnittestGenerator(),
        systemtests=Keras40SystemtestGenerator(),
        api=Keras40API(),
        grammar=grammar_40,
        loc=21482,
    )
    Keras(
        bug_id=41,
        buggy_commit_id="a27b4a51f4880ad3a7669531b667c1ef44b173ef",
        fixed_commit_id="4a58b178073f0ba3b166220f7ebd7d56149bfb20",
        test_files=[Path("tests", "keras", "utils", "data_utils_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "utils",
                "data_utils_test.py::test_generator_enqueuer_fail_threads",
            ),
            os.path.join(
                "tests",
                "keras",
                "utils",
                "data_utils_test.py::test_generator_enqueuer_fail_processes",
            ),
        ],
        skip_tests=[
            "test_ordered_enqueuer_fail_threads",
            "test_ordered_enqueuer_fail_processes",
            "test_finite_generator_enqueuer_threads",
            "test_finite_generator_enqueuer_processes",
        ],
        unittests=Keras41UnittestGenerator(),
        systemtests=Keras41SystemtestGenerator(),
        api=Keras41API(),
        grammar=grammar_41,
        loc=20988,
    )
    Keras(
        bug_id=42,
        buggy_commit_id="67a432c273cbd65866b1d2cb1e2c62714b633b6e",
        fixed_commit_id="2f3edf96078d78450b985bdf3bfffe7e0c627169",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "engine", "test_training.py::test_model_methods"
            )
        ],
        unittests=Keras42UnittestGenerator(),
        systemtests=Keras42SystemtestGenerator(),
        api=Keras42API(),
        grammar=grammar_42,
        loc=20868,
    )
    Keras(
        bug_id=43,
        buggy_commit_id="e3e97c401aa8251e957b73fba8ed4d108c106f12",
        fixed_commit_id="b17169ca5d6cd1c8aeb237fc2bb0555c9e1b6a02",
        test_files=[
            Path("tests", "keras", "utils", "generic_utils_test.py"),
            Path("tests", "keras", "utils", "io_utils_test.py"),
            Path("tests", "keras", "utils", "layer_utils_test.py"),
            Path("tests", "keras", "utils", "multi_gpu_test.py"),
            Path("tests", "keras", "utils", "np_utils_test.py"),
            Path("tests", "keras", "utils", "vis_utils_test.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "keras", "utils", "np_utils_test.py::test_to_categorical"
            )
        ],
        unittests=Keras43UnittestGenerator(),
        systemtests=Keras43SystemtestGenerator(),
        api=Keras43API(),
        grammar=grammar_43,
        loc=20859,
    )
    Keras(
        bug_id=44,
        buggy_commit_id="cc08f0f01fe97a9659e3da8fa9b290a54992c74a",
        fixed_commit_id="3292aa5a30350c67627f173ceac713956f68271f",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_trainability[SimpleRNN]",
            ),
            os.path.join(
                "tests", "keras", "layers", "recurrent_test.py::test_trainability[GRU]"
            ),
            os.path.join(
                "tests", "keras", "layers", "recurrent_test.py::test_trainability[LSTM]"
            ),
        ],
        unittests=Keras44UnittestGenerator(),
        systemtests=Keras44SystemtestGenerator(),
        api=Keras44API(),
        grammar=grammar_44,
        loc=20825,
    )
    Keras(
        bug_id=45,
        buggy_commit_id="d368dc870bfd8fdd4ca0ff82bd5b61aa549291c5",
        fixed_commit_id="159bb1aac17a8de0f96997d35703b8f26926a848",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_implementation_mode[LSTM]",
            )
        ],
        unittests=Keras45UnittestGenerator(),
        systemtests=Keras45SystemtestGenerator(),
        api=Keras45API(),
        grammar=grammar_45,
        loc=20761,
    )


class KerasAPI(API):
    def __init__(self, default_timeout: int = 30):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# NOTE on importing keras on this platform:
# The pinned TensorFlow 1.15 wheel is x86_64 compiled with AVX and aborts
# on import under Rosetta (no AVX).  Every helper therefore loads the
# *pure-numpy* target module directly from its source file (bypassing
# ``keras/__init__`` and the TF backend) with importlib.  This works for
# modules that only depend on numpy / six / stdlib.
# ======================================================================


# ======================================================================
# bug_43: keras.utils.np_utils.to_categorical did not squeeze a trailing
# singleton dimension.  For an input of shape ``(n, 1)`` the buggy version
# returned shape ``(n, 1, num_classes)`` instead of ``(n, num_classes)``.
#
# System-test format:  ``<mode> <num_classes> <v1> <v2> ...`` where
#   ``<mode>`` is ``col`` (y reshaped to ``(n, 1)`` — the trigger) or
#   ``flat`` (y kept 1-D).  The harness prints ``tuple(out.shape)``; the
#   oracle compares against the correct (fixed) shape ``(n, num_classes)``.
# ======================================================================


class Keras43API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            num_classes = int(process.args[3])
            vals = [int(x) for x in process.args[4:]]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if not vals:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = (len(vals), num_classes)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras43TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, List[int]]:
        num_classes = random.randint(2, 12)
        n = random.randint(2, 8)
        vals = [random.randint(0, num_classes - 1) for _ in range(n)]
        return num_classes, vals


class Keras43SystemtestGenerator(SystemtestGenerator, Keras43TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        num_classes, vals = self.generate_case()
        return (
            f"col {num_classes} " + " ".join(map(str, vals)),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        num_classes, vals = self.generate_case()
        return (
            f"flat {num_classes} " + " ".join(map(str, vals)),
            TestResult.PASSING,
        )


_KERAS43_UTILS = '''
def _t4p_to_categorical_shape(mode, num_classes, vals):
    import os
    import importlib.util
    import numpy as np
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'np_utils.py')
    spec = importlib.util.spec_from_file_location('t4p_np_utils', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if mode == 'col':
        y = np.array(vals).reshape(-1, 1)
    else:
        y = np.array(vals)
    return tuple(module.to_categorical(y, num_classes).shape)
'''


class Keras43UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras43TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS43_UTILS).body

    @staticmethod
    def _assert(mode: str, num_classes: int, vals: List[int]) -> List[ast.stmt]:
        expected = (len(vals), num_classes)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Tuple(elts=[ast.Constant(value=v) for v in expected]),
                        ast.Call(
                            func=ast.Name(id="_t4p_to_categorical_shape"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=num_classes),
                                ast.List(
                                    elts=[ast.Constant(value=v) for v in vals]
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        num_classes, vals = self.generate_case()
        test = self.get_empty_test()
        test.body = self._assert("col", num_classes, vals)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        num_classes, vals = self.generate_case()
        test = self.get_empty_test()
        test.body = self._assert("flat", num_classes, vals)
        return test, TestResult.PASSING


grammar_43: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number><values>"],
            "<mode>": ["col", "flat"],
            "<values>": [" <number>", " <number><values>"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_43)


# ======================================================================
# bug_1: seeded initializers (RandomUniform / RandomNormal / TruncatedNormal /
# VarianceScaling) did NOT advance their ``seed`` between calls, so calling the
# same *seeded* initializer twice returned identical draws.  The fix increments
# ``self.seed`` after every ``__call__`` so consecutive calls differ.
#
# System-test format:  ``<mode> <init> <seed> <rows> <cols>`` where
#   ``<mode>`` is ``diff`` (the trigger: harness prints ``1`` iff two
#   consecutive calls differ) or ``shape`` (harness prints the output shape).
#   ``<init>`` is one of uniform/normal/truncated/varscale.  The oracle expects
#   ``1`` for a ``diff`` test (the fixed behaviour) and ``(rows, cols)`` for a
#   ``shape`` test (true on both builds).
# ======================================================================


class Keras1API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            rows = int(process.args[5])
            cols = int(process.args[6])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if mode == "diff":
            expected = "1"
        else:
            expected = str((rows, cols))
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


_KERAS1_INITS = ["uniform", "normal", "truncated", "varscale"]


class Keras1TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[str, int, int, int]:
        init = random.choice(_KERAS1_INITS)
        seed = random.randint(1, 10000)
        rows = random.randint(2, 8)
        cols = random.randint(2, 8)
        return init, seed, rows, cols


class Keras1SystemtestGenerator(SystemtestGenerator, Keras1TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        init, seed, rows, cols = self.generate_case()
        return f"diff {init} {seed} {rows} {cols}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        init, seed, rows, cols = self.generate_case()
        return f"shape {init} {seed} {rows} {cols}", TestResult.PASSING


_KERAS1_UTILS = '''
def _t4p_init(name, seed, rows, cols):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras.backend as K
    from keras import initializers
    mapping = {"uniform": "RandomUniform", "normal": "RandomNormal",
               "truncated": "TruncatedNormal", "varscale": "VarianceScaling"}
    init = getattr(initializers, mapping[name])(seed=seed)
    a = np.asarray(K.eval(init((rows, cols))))
    b = np.asarray(K.eval(init((rows, cols))))
    return a, b


def _t4p_init_diff(name, seed, rows, cols):
    import numpy as np
    a, b = _t4p_init(name, seed, rows, cols)
    return not np.allclose(a, b)


def _t4p_init_shape(name, seed, rows, cols):
    a, _ = _t4p_init(name, seed, rows, cols)
    return tuple(a.shape)
'''


class Keras1UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras1TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS1_UTILS).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        init, seed, rows, cols = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_init_diff"),
                            args=[
                                ast.Constant(value=init),
                                ast.Constant(value=seed),
                                ast.Constant(value=rows),
                                ast.Constant(value=cols),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        init, seed, rows, cols = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Tuple(elts=[ast.Constant(value=rows), ast.Constant(value=cols)]),
                        ast.Call(
                            func=ast.Name(id="_t4p_init_shape"),
                            args=[
                                ast.Constant(value=init),
                                ast.Constant(value=seed),
                                ast.Constant(value=rows),
                                ast.Constant(value=cols),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.PASSING


grammar_1: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <init> <number> <number> <number>"],
            "<mode>": ["diff", "shape"],
            "<init>": ["uniform", "normal", "truncated", "varscale"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_1)


# ======================================================================
# bug_40: RNN.compute_output_shape with return_state=True built the returned
# state shapes as ``[(batch, output_dim) for _ in self.states]`` -- i.e. every
# state was reported with the FIRST state's dimension.  For a cell whose states
# have DIFFERENT sizes (e.g. a stack of LSTMCells with different units) this is
# wrong.  The fix builds ``[(batch, dim) for dim in state_size]``.
#
# System-test format:  ``<u1> <u2> <timesteps> <emb> <rs>`` -- two stacked
#   LSTMCells with units u1 and u2, RNN(return_state=True), ``<rs>`` is ``seq``
#   (return_sequences=True) or ``last``.  The harness prints
#   compute_output_shape.  The stack state_size is ``(u2, u2, u1, u1)`` (reverse
#   order in this keras version); the oracle recomputes the correct list.
#   ``u1 != u2`` triggers the fault (failing); ``u1 == u2`` makes buggy and
#   fixed agree (passing).
# ======================================================================


def _keras40_expected(u1: int, u2: int, ts: int, emb: int, rs: str) -> str:
    output_shape = (None, ts, u2) if rs == "seq" else (None, u2)
    state = [(None, u2), (None, u2), (None, u1), (None, u1)]
    return str([output_shape] + state)


class Keras40API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            u1 = int(process.args[2])
            u2 = int(process.args[3])
            ts = int(process.args[4])
            emb = int(process.args[5])
            rs = process.args[6]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _keras40_expected(u1, u2, ts, emb, rs)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras40TestGenerator:
    @staticmethod
    def generate_failing_case() -> Tuple[int, int, int, int, str]:
        u1 = random.randint(2, 8)
        u2 = random.choice([u for u in range(2, 9) if u != u1])
        ts = random.randint(2, 8)
        emb = random.randint(2, 8)
        rs = random.choice(["seq", "last"])
        return u1, u2, ts, emb, rs

    @staticmethod
    def generate_passing_case() -> Tuple[int, int, int, int, str]:
        u = random.randint(2, 8)
        ts = random.randint(2, 8)
        emb = random.randint(2, 8)
        rs = random.choice(["seq", "last"])
        return u, u, ts, emb, rs


class Keras40SystemtestGenerator(SystemtestGenerator, Keras40TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        u1, u2, ts, emb, rs = self.generate_failing_case()
        return f"{u1} {u2} {ts} {emb} {rs}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        u1, u2, ts, emb, rs = self.generate_passing_case()
        return f"{u1} {u2} {ts} {emb} {rs}", TestResult.PASSING


_KERAS40_UTILS = '''
def _t4p_stacked_output_shape(u1, u2, ts, emb, rs):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.layers import recurrent
    cells = [recurrent.LSTMCell(u1), recurrent.LSTMCell(u2)]
    layer = recurrent.RNN(cells, return_state=True, return_sequences=(rs == "seq"))
    return str(layer.compute_output_shape((None, ts, emb)))
'''


class Keras40UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras40TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS40_UTILS).body

    @staticmethod
    def _assert(u1: int, u2: int, ts: int, emb: int, rs: str) -> List[ast.stmt]:
        expected = _keras40_expected(u1, u2, ts, emb, rs)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_stacked_output_shape"),
                            args=[
                                ast.Constant(value=u1),
                                ast.Constant(value=u2),
                                ast.Constant(value=ts),
                                ast.Constant(value=emb),
                                ast.Constant(value=rs),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_passing_case())
        return test, TestResult.PASSING


grammar_40: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <number> <number> <number> <rs>"],
            "<rs>": ["seq", "last"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_40)


# ======================================================================
# bug_44: RNN.trainable_weights ignored the layer's ``trainable`` flag -- it
# returned the wrapped cell's trainable weights even after ``layer.trainable =
# False`` (and non_trainable_weights stayed empty).  The fix returns ``[]`` for
# trainable_weights and the cell's weights for non_trainable_weights once the
# layer is frozen.
#
# System-test format:  ``<layer> <units> <emb> <mode>`` where ``<layer>`` is
#   simple/gru/lstm, ``<mode>`` is ``frozen`` (the trigger: harness freezes the
#   layer and prints ``len(trainable_weights)`` -- oracle expects 0) or
#   ``trainable`` (harness prints ``1`` iff all weights are trainable -- true on
#   both builds).
# ======================================================================


class Keras44API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[5]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "0" if mode == "frozen" else "1"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


_KERAS44_LAYERS = ["simple", "gru", "lstm"]


class Keras44TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[str, int, int]:
        layer = random.choice(_KERAS44_LAYERS)
        units = random.randint(2, 8)
        emb = random.randint(2, 8)
        return layer, units, emb


class Keras44SystemtestGenerator(SystemtestGenerator, Keras44TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        layer, units, emb = self.generate_case()
        return f"{layer} {units} {emb} frozen", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        layer, units, emb = self.generate_case()
        return f"{layer} {units} {emb} trainable", TestResult.PASSING


_KERAS44_UTILS = '''
_LAYERS = {"simple": "SimpleRNN", "gru": "GRU", "lstm": "LSTM"}


def _t4p_rnn_layer(layer_name, units, emb):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.layers import recurrent
    layer = getattr(recurrent, _LAYERS[layer_name])(units)
    layer.build((None, None, emb))
    return layer


def _t4p_frozen_trainable_count(layer_name, units, emb):
    layer = _t4p_rnn_layer(layer_name, units, emb)
    layer.trainable = False
    return len(layer.trainable_weights)


def _t4p_all_trainable(layer_name, units, emb):
    layer = _t4p_rnn_layer(layer_name, units, emb)
    return len(layer.trainable_weights) == len(layer.weights) and len(layer.weights) > 0
'''


class Keras44UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras44TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS44_UTILS).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        layer, units, emb = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=0),
                        ast.Call(
                            func=ast.Name(id="_t4p_frozen_trainable_count"),
                            args=[
                                ast.Constant(value=layer),
                                ast.Constant(value=units),
                                ast.Constant(value=emb),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        layer, units, emb = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_all_trainable"),
                            args=[
                                ast.Constant(value=layer),
                                ast.Constant(value=units),
                                ast.Constant(value=emb),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.PASSING


grammar_44: Grammar = clean_up(
    dict(
        {
            "<start>": ["<layer> <number> <number> <mode>"],
            "<layer>": ["simple", "gru", "lstm"],
            "<mode>": ["frozen", "trainable"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_44)


# ======================================================================
# bug_45: LSTMCell (implementation=1) added the gate biases unconditionally
# (``K.dot(...) + self.bias_i``).  When ``use_bias=False`` the bias tensors are
# None, so building/running the layer raised ``ValueError: None values not
# supported``.  The fix only adds bias via ``K.bias_add`` when ``use_bias``.
#
# System-test format:  ``<units> <ts> <emb> <batch> <mode>`` where ``<mode>`` is
#   ``nobias`` (the trigger: build an LSTM(implementation=1, use_bias=False) and
#   run predict) or ``bias``.  The harness prints ``OK`` on success / ``ERR`` on
#   exception; the oracle expects ``OK`` (true on fixed for both modes, false on
#   buggy for ``nobias``).
# ======================================================================


class Keras45API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Model ran"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras45TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int, int]:
        units = random.randint(2, 8)
        ts = random.randint(3, 8)
        emb = random.randint(2, 8)
        batch = random.randint(2, 3)
        return units, ts, emb, batch


class Keras45SystemtestGenerator(SystemtestGenerator, Keras45TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        units, ts, emb, batch = self.generate_case()
        return f"{units} {ts} {emb} {batch} nobias", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        units, ts, emb, batch = self.generate_case()
        return f"{units} {ts} {emb} {batch} bias", TestResult.PASSING


_KERAS45_UTILS = '''
def _t4p_lstm_runs(units, ts, emb, batch, use_bias):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras import backend as K
    from keras.layers import LSTM, Input
    from keras.models import Model
    K.clear_session()
    try:
        inp = Input((ts, emb))
        out = LSTM(units, implementation=1, use_bias=use_bias)(inp)
        model = Model(inp, out)
        y = model.predict(np.random.random((batch, ts, emb)))
        return tuple(y.shape) == (batch, units)
    except Exception:
        return False
'''


class Keras45UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras45TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS45_UTILS).body

    def _make(self, use_bias: bool) -> ast.FunctionDef:
        units, ts, emb, batch = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_lstm_runs"),
                            args=[
                                ast.Constant(value=units),
                                ast.Constant(value=ts),
                                ast.Constant(value=emb),
                                ast.Constant(value=batch),
                                ast.Constant(value=use_bias),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(False), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(True), TestResult.PASSING


grammar_45: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <number> <number> <number> <mode>"],
            "<mode>": ["nobias", "bias"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_45)


# ======================================================================
# bug_38: StackedRNNCells.build passed a 3-tuple ``(batch, features,
# output_dim)`` as the input shape to each inner cell instead of the correct
# 2-tuple ``(batch, output_dim)`` (RNN cells never see a time axis).  A custom
# cell that asserts ``len(input_shape) == 2`` therefore raised when stacked.
#
# System-test format:  ``<mode> <u1> <u2> <emb> <batch> <ts>`` where ``<mode>``
#   is ``stack`` (the trigger: two stacked custom cells) or ``single`` (one
#   cell).  The harness prints ``OK`` on success / ``ERR`` on exception; the
#   oracle expects ``OK`` (true on fixed for both, false on buggy for ``stack``).
# ======================================================================


class Keras38API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Model built"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras38TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int, int, int]:
        u1 = random.randint(2, 8)
        u2 = random.randint(2, 12)
        emb = random.randint(2, 8)
        batch = random.randint(2, 4)
        ts = random.randint(3, 7)
        return u1, u2, emb, batch, ts


class Keras38SystemtestGenerator(SystemtestGenerator, Keras38TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        u1, u2, emb, batch, ts = self.generate_case()
        return f"stack {u1} {u2} {emb} {batch} {ts}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        u1, u2, emb, batch, ts = self.generate_case()
        return f"single {u1} {u2} {emb} {batch} {ts}", TestResult.PASSING


_KERAS38_UTILS = '''
def _t4p_make_cell():
    import keras

    class MinimalRNNCell(keras.layers.Layer):
        def __init__(self, units, **kwargs):
            self.units = units
            self.state_size = units
            super(MinimalRNNCell, self).__init__(**kwargs)

        def build(self, input_shape):
            assert len(input_shape) == 2
            self.kernel = self.add_weight(
                shape=(input_shape[-1], self.units),
                initializer="uniform", name="kernel")
            self.recurrent_kernel = self.add_weight(
                shape=(self.units, self.units),
                initializer="uniform", name="recurrent_kernel")
            self.built = True

        def call(self, inputs, states):
            prev_output = states[0]
            h = keras.backend.dot(inputs, self.kernel)
            output = h + keras.backend.dot(prev_output, self.recurrent_kernel)
            return output, [output]

    return MinimalRNNCell


def _t4p_stack_runs(mode, u1, u2, emb, batch, ts):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    from keras.layers import RNN, Input
    keras.backend.clear_session()
    Cell = _t4p_make_cell()
    try:
        x = Input((None, emb))
        if mode == "stack":
            layer = RNN([Cell(u1), Cell(u2)])
        else:
            layer = RNN(Cell(u1))
        y = layer(x)
        model = keras.models.Model(x, y)
        model.predict(np.random.random((batch, ts, emb)))
        return True
    except Exception:
        return False
'''


class Keras38UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras38TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS38_UTILS).body

    def _make(self, mode: str) -> ast.FunctionDef:
        u1, u2, emb, batch, ts = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_stack_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=u1),
                                ast.Constant(value=u2),
                                ast.Constant(value=emb),
                                ast.Constant(value=batch),
                                ast.Constant(value=ts),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("stack"), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("single"), TestResult.PASSING


grammar_38: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number> <number>"],
            "<mode>": ["stack", "single"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_38)


# ======================================================================
# bug_19: StackedRNNCells.state_size listed the inner cells' states in REVERSE
# cell order (e.g. a stack of LSTMCell(u1), LSTMCell(u2) reported
# ``(u2, u2, u1, u1)``).  The fix reports them in natural order
# ``(u1, u1, u2, u2)`` (reverse only when the new ``reverse_state_order`` flag
# is set).
#
# System-test format:  ``<u1> <u2>`` -- a two-LSTMCell stack.  The harness
#   prints ``tuple(layer.cell.state_size)``; the oracle expects the natural
#   order ``(u1, u1, u2, u2)``.  ``u1 != u2`` triggers the fault (failing);
#   ``u1 == u2`` makes both builds agree (passing).
# ======================================================================


class Keras19API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            u1 = int(process.args[2])
            u2 = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str((u1, u1, u2, u2))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras19TestGenerator:
    @staticmethod
    def generate_failing_case() -> Tuple[int, int]:
        u1 = random.randint(2, 12)
        u2 = random.choice([u for u in range(2, 13) if u != u1])
        return u1, u2

    @staticmethod
    def generate_passing_case() -> Tuple[int, int]:
        u = random.randint(2, 12)
        return u, u


class Keras19SystemtestGenerator(SystemtestGenerator, Keras19TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        u1, u2 = self.generate_failing_case()
        return f"{u1} {u2}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        u1, u2 = self.generate_passing_case()
        return f"{u1} {u2}", TestResult.PASSING


_KERAS19_UTILS = '''
def _t4p_stack_state_size(u1, u2):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.layers import recurrent
    layer = recurrent.RNN([recurrent.LSTMCell(u1), recurrent.LSTMCell(u2)])
    return str(tuple(layer.cell.state_size))
'''


class Keras19UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras19TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS19_UTILS).body

    @staticmethod
    def _assert(u1: int, u2: int) -> List[ast.stmt]:
        expected = str((u1, u1, u2, u2))
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_stack_state_size"),
                            args=[ast.Constant(value=u1), ast.Constant(value=u2)],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_passing_case())
        return test, TestResult.PASSING


grammar_19: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <number>"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_19)


# ======================================================================
# bug_36: backend.separable_conv1d built an UNEQUAL (H, W) stride tuple for the
# internal depthwise_conv2d -- ``(1, 1) + strides + (1,)`` (NHWC) instead of
# ``(1,) + strides * 2 + (1,)``.  TF's depthwise_conv2d requires equal spatial
# strides, so a stride > 1 raised ``InvalidArgumentError``.
#
# System-test format:  ``<strides> <filters> <numstep> <stacksize> <batch>
#   <df>`` where ``<df>`` is last/first.  ``<strides> > 1`` triggers the fault
#   (failing); ``<strides> == 1`` works on both (passing).  The harness prints
#   ``OK`` / ``ERR``; the oracle expects ``OK``.
# ======================================================================


class Keras36API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Ran"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras36TestGenerator:
    @staticmethod
    def generate_case(strides: int) -> Tuple[int, int, int, int, int, str]:
        filters = random.randint(3, 8)
        numstep = random.randint(7, 12)
        stacksize = random.randint(2, 4)
        batch = random.randint(2, 3)
        df = random.choice(["last", "first"])
        return strides, filters, numstep, stacksize, batch, df


class Keras36SystemtestGenerator(SystemtestGenerator, Keras36TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        s, f, n, ss, b, df = self.generate_case(random.choice([2, 3]))
        return f"{s} {f} {n} {ss} {b} {df}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        s, f, n, ss, b, df = self.generate_case(1)
        return f"{s} {f} {n} {ss} {b} {df}", TestResult.PASSING


_KERAS36_UTILS = '''
def _t4p_sepconv1d_runs(strides, filters, numstep, stacksize, batch, df):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    from keras.layers import SeparableConv1D, Input
    from keras.models import Model
    data_format = "channels_last" if df == "last" else "channels_first"
    keras.backend.clear_session()
    try:
        if df == "last":
            inp = Input((numstep, stacksize))
            x = np.random.random((batch, numstep, stacksize))
        else:
            inp = Input((stacksize, numstep))
            x = np.random.random((batch, stacksize, numstep))
        layer = SeparableConv1D(filters, 3, strides=strides, padding="valid",
                                data_format=data_format)
        model = Model(inp, layer(inp))
        model.predict(x)
        return True
    except Exception:
        return False
'''


class Keras36UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras36TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS36_UTILS).body

    def _make(self, strides: int) -> ast.FunctionDef:
        s, f, n, ss, b, df = self.generate_case(strides)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_sepconv1d_runs"),
                            args=[
                                ast.Constant(value=s),
                                ast.Constant(value=f),
                                ast.Constant(value=n),
                                ast.Constant(value=ss),
                                ast.Constant(value=b),
                                ast.Constant(value=df),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(random.choice([2, 3])), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(1), TestResult.PASSING


grammar_36: Grammar = clean_up(
    dict(
        {
            "<start>": [
                "<number> <number> <number> <number> <number> <df>"
            ],
            "<df>": ["last", "first"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_36)


# ======================================================================
# bug_31: backend.ctc_batch_cost squeezed ``label_length`` / ``input_length``
# without specifying ``axis=-1``.  Those tensors have shape (batch, 1), so for a
# SINGLE-sample batch the squeeze collapsed them to a scalar and downstream code
# raised.  The fix squeezes only the last axis.
#
# System-test format:  ``<batch> <T> <L> <num_classes> <seed>``.  ``batch == 1``
#   triggers the fault (failing); ``batch >= 2`` works on both (passing).  The
#   harness prints ``OK`` on a finite (batch, 1) cost / ``ERR`` on exception;
#   the oracle expects ``OK``.
# ======================================================================


class Keras31API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Ran"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras31TestGenerator:
    @staticmethod
    def generate_case(batch: int) -> Tuple[int, int, int, int, int]:
        num_classes = random.randint(4, 7)
        L = random.randint(2, min(4, num_classes - 1))
        T = random.randint(L + 3, L + 8)
        seed = random.randint(0, 100000)
        return batch, T, L, num_classes, seed


class Keras31SystemtestGenerator(SystemtestGenerator, Keras31TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        b, T, L, nc, seed = self.generate_case(1)
        return f"{b} {T} {L} {nc} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        b, T, L, nc, seed = self.generate_case(random.randint(2, 5))
        return f"{b} {T} {L} {nc} {seed}", TestResult.PASSING


_KERAS31_UTILS = '''
def _t4p_ctc_runs(batch, T, L, num_classes, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras.backend as K
    K.clear_session()
    try:
        rng = np.random.RandomState(seed)
        y_pred = rng.random_sample((batch, T, num_classes)).astype("float32")
        y_pred = y_pred / y_pred.sum(axis=-1, keepdims=True)
        y_true = rng.randint(0, num_classes - 1, size=(batch, L)).astype("float32")
        input_length = np.full((batch, 1), T, dtype="float32")
        label_length = np.full((batch, 1), L, dtype="float32")
        cost = K.ctc_batch_cost(K.variable(y_true), K.variable(y_pred),
                                K.variable(input_length), K.variable(label_length))
        c = np.asarray(K.eval(cost))
        return c.shape == (batch, 1) and bool(np.all(np.isfinite(c)))
    except Exception:
        return False
'''


class Keras31UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras31TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS31_UTILS).body

    def _make(self, batch: int) -> ast.FunctionDef:
        b, T, L, nc, seed = self.generate_case(batch)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_ctc_runs"),
                            args=[
                                ast.Constant(value=b),
                                ast.Constant(value=T),
                                ast.Constant(value=L),
                                ast.Constant(value=nc),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(1), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make(random.randint(2, 5)), TestResult.PASSING


grammar_31: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <number> <number> <number> <number>"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_31)


# ======================================================================
# bug_26: backend.rnn tiled the step mask to the OUTPUT width and reused it for
# every state (``tf.where(tiled_mask_t, new_states[i], states[i])``).  When a
# cell keeps a state WIDER than its output, the wider state failed the
# ``tf.where`` shape check.  The fix tiles the mask per-state.
#
# System-test format:  ``<mode> <ns> <input_dim> <output_dim> <timesteps>
#   <seed>`` where ``<mode>`` is ``mask`` (the trigger: a masked rnn whose 2nd
#   state is 2x the output width) or ``nomask``.  The harness prints ``OK`` /
#   ``ERR``; the oracle expects ``OK`` (fixed for both, buggy fails ``mask``).
# ======================================================================


class Keras26API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Ran"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras26TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int, int, int]:
        ns = random.randint(2, 6)
        idim = random.randint(3, 7)
        odim = random.randint(2, 5)
        ts = random.randint(4, 8)
        seed = random.randint(seed_lo, seed_hi)
        return ns, idim, odim, ts, seed


class Keras26SystemtestGenerator(SystemtestGenerator, Keras26TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        ns, idim, odim, ts, seed = self.generate_case(0, 5000)
        return f"mask {ns} {idim} {odim} {ts} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        ns, idim, odim, ts, seed = self.generate_case(5001, 10000)
        return f"nomask {ns} {idim} {odim} {ts} {seed}", TestResult.PASSING


_KERAS26_UTILS = '''
def _t4p_rnn_states(mode, ns, idim, odim, ts, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras.backend as K
    K.clear_session()
    try:
        rng = np.random.RandomState(seed)
        x = rng.random_sample((ns, ts, idim)).astype("float32")
        h0 = rng.random_sample((ns, odim)).astype("float32")
        wi = rng.random_sample((idim, odim)).astype("float32")
        wh = rng.random_sample((odim, odim)).astype("float32")
        x_k = K.variable(x)
        h0_k = [K.variable(h0), K.variable(np.concatenate([h0, h0], axis=-1))]
        wi_k = K.variable(wi)
        wh_k = K.variable(wh)

        def rnn_fn(x_k, h_k):
            y_k = K.dot(x_k, wi_k) + K.dot(h_k[0], wh_k)
            return y_k, [y_k, K.concatenate([y_k, y_k], axis=-1)]

        kwargs = {}
        if mode == "mask":
            m = rng.randint(2, size=(ns, ts))
            kwargs["mask"] = K.variable(m)
        last, outs, states = K.rnn(rnn_fn, x_k, h0_k, **kwargs)
        o = np.asarray(K.eval(outs))
        s1 = np.asarray(K.eval(states[1]))
        return o.shape == (ns, ts, odim) and s1.shape == (ns, 2 * odim)
    except Exception:
        return False
'''


class Keras26UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras26TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS26_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        ns, idim, odim, ts, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_rnn_states"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=ns),
                                ast.Constant(value=idim),
                                ast.Constant(value=odim),
                                ast.Constant(value=ts),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("mask", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("nomask", 5001, 10000), TestResult.PASSING


grammar_26: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number> <number>"],
            "<mode>": ["mask", "nomask"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_26)


# ======================================================================
# bug_18: backend.Function stored ``options`` / ``run_metadata`` in
# ``session_kwargs`` and then rejected them ("Some keys in session_kwargs are
# not supported").  The fix pops them out into ``run_options`` / ``run_metadata``
# and wires them into the callable.
#
# System-test format:  ``<mode> <a> <b>`` where ``<mode>`` is ``withmeta`` (the
#   trigger: build a K.function with options+run_metadata) or ``plain``.  The
#   harness computes ``x + y`` and prints ``OK`` / ``ERR``; the oracle expects
#   ``OK`` (fixed for both, buggy fails ``withmeta``).
# ======================================================================


class Keras18API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Ran"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras18TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int]:
        return random.randint(1, 100), random.randint(1, 100)


class Keras18SystemtestGenerator(SystemtestGenerator, Keras18TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        a, b = self.generate_case()
        return f"withmeta {a} {b}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        a, b = self.generate_case()
        return f"plain {a} {b}", TestResult.PASSING


_KERAS18_UTILS = '''
def _t4p_function_runs(mode, a, b):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K
    K.clear_session()
    try:
        from tensorflow.core.protobuf import config_pb2
        x = K.placeholder(shape=())
        y = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        kwargs = {}
        if mode == "withmeta":
            kwargs["options"] = config_pb2.RunOptions(output_partition_graphs=True)
            kwargs["run_metadata"] = run_metadata
        f = K.function(inputs=[x, y], outputs=[x + y], **kwargs)
        out = f([float(a), float(b)])
        ok = abs(float(out[0]) - (a + b)) < 1e-4
        if mode == "withmeta":
            ok = ok and len(run_metadata.partition_graphs) > 0
        return ok
    except Exception:
        return False
'''


class Keras18UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras18TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS18_UTILS).body

    def _make(self, mode: str) -> ast.FunctionDef:
        a, b = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_function_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=a),
                                ast.Constant(value=b),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("withmeta"), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("plain"), TestResult.PASSING


grammar_18: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number>"],
            "<mode>": ["withmeta", "plain"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_18)


# ======================================================================
# bug_27: Bidirectional did not override ``get_updates_for`` / ``get_losses_for``
# so it only reported its FORWARD sub-layer's conditional updates/losses,
# ignoring the backward layer.  The fix sums forward + backward (+ its own).
#
# System-test format:  ``<check> <nf_none> <nf_x> <nb_none> <nb_x>`` -- add that
#   many updates to the forward/backward layers with ``inputs=None`` / ``x``.
#   ``<check>`` is ``getnone`` (report get_updates_for(None), expect
#   nf_none+nb_none), ``getx`` (get_updates_for(x), expect nf_x+nb_x) or
#   ``total`` (report len(updates), expect the sum).  getnone/getx trigger the
#   fault when the backward count is > 0 (failing); ``total`` agrees on both
#   (passing).
# ======================================================================


class Keras27API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            check = process.args[2]
            nf_none = int(process.args[3])
            nf_x = int(process.args[4])
            nb_none = int(process.args[5])
            nb_x = int(process.args[6])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if check == "getnone":
            expected = nf_none + nb_none
        elif check == "getx":
            expected = nf_x + nb_x
        else:
            expected = nf_none + nf_x + nb_none + nb_x
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras27TestGenerator:
    @staticmethod
    def generate_failing_case() -> Tuple[str, int, int, int, int]:
        check = random.choice(["getnone", "getx"])
        nf_none = random.randint(0, 3)
        nf_x = random.randint(0, 3)
        nb_none = random.randint(0, 3)
        nb_x = random.randint(0, 3)
        # Guarantee the relevant backward count is non-zero so buggy differs.
        if check == "getnone":
            nb_none = random.randint(1, 3)
        else:
            nb_x = random.randint(1, 3)
        return check, nf_none, nf_x, nb_none, nb_x

    @staticmethod
    def generate_passing_case() -> Tuple[str, int, int, int, int]:
        nf_none = random.randint(0, 3)
        nf_x = random.randint(0, 3)
        nb_none = random.randint(0, 3)
        nb_x = random.randint(0, 3)
        if nf_none + nf_x + nb_none + nb_x == 0:
            nf_none = 1
        return "total", nf_none, nf_x, nb_none, nb_x


class Keras27SystemtestGenerator(SystemtestGenerator, Keras27TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        check, a, b, c, d = self.generate_failing_case()
        return f"{check} {a} {b} {c} {d}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        check, a, b, c, d = self.generate_passing_case()
        return f"{check} {a} {b} {c} {d}", TestResult.PASSING


_KERAS27_UTILS = '''
def _t4p_bidir_count(check, nf_none, nf_x, nb_none, nb_x):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K
    from keras.layers import Input, SimpleRNN
    from keras.layers import wrappers
    K.clear_session()
    x = Input(shape=(3, 2))
    layer = wrappers.Bidirectional(SimpleRNN(3))
    _ = layer(x)
    counter = [0]

    def add(target_layer, n, inputs):
        for _ in range(n):
            target_layer.add_update(counter[0], inputs=inputs)
            counter[0] += 1

    add(layer.forward_layer, nf_none, None)
    add(layer.forward_layer, nf_x, x)
    add(layer.backward_layer, nb_none, None)
    add(layer.backward_layer, nb_x, x)
    if check == "getnone":
        return len(layer.get_updates_for(None))
    elif check == "getx":
        return len(layer.get_updates_for(x))
    return len(layer.updates)
'''


class Keras27UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras27TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS27_UTILS).body

    @staticmethod
    def _assert(check: str, a: int, b: int, c: int, d: int) -> List[ast.stmt]:
        if check == "getnone":
            expected = a + c
        elif check == "getx":
            expected = b + d
        else:
            expected = a + b + c + d
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_bidir_count"),
                            args=[
                                ast.Constant(value=check),
                                ast.Constant(value=a),
                                ast.Constant(value=b),
                                ast.Constant(value=c),
                                ast.Constant(value=d),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_passing_case())
        return test, TestResult.PASSING


grammar_27: Grammar = clean_up(
    dict(
        {
            "<start>": ["<check> <number> <number> <number> <number>"],
            "<check>": ["getnone", "getx", "total"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_27)


# ======================================================================
# bug_37: Bidirectional had no ``__call__`` override, so an ``initial_state``
# passed to a Bidirectional RNN was silently dropped -- the states never became
# model inputs.  The fix adds a __call__ that standardizes and wires the
# initial_state list.
#
# System-test format:  ``<mode> <dim> <timesteps> <units>`` where ``<mode>`` is
#   ``withstate`` (the trigger: pass a proper initial_state list to a second
#   Bidirectional) or ``plain``.  The harness prints ``len(model.layers)``; the
#   oracle expects 4 for ``withstate`` (buggy drops the state -> 2) and 2 for
#   ``plain`` (both builds agree).
# ======================================================================


class Keras37API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = 4 if mode == "withstate" else 2
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras37TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int]:
        dim = random.randint(3, 8)
        timesteps = random.randint(2, 5)
        units = random.randint(2, 6)
        return dim, timesteps, units


class Keras37SystemtestGenerator(SystemtestGenerator, Keras37TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        dim, ts, units = self.generate_case()
        return f"withstate {dim} {ts} {units}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        dim, ts, units = self.generate_case()
        return f"plain {dim} {ts} {units}", TestResult.PASSING


_KERAS37_UTILS = '''
def _t4p_bidir_layers(mode, dim, timesteps, units):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K
    from keras.layers import Input, LSTM
    from keras.layers import wrappers
    from keras.models import Model
    K.clear_session()
    input1 = Input((timesteps, dim))
    layer = wrappers.Bidirectional(LSTM(units, return_state=True, return_sequences=True))
    state = layer(input1)[1:]
    input2 = Input((timesteps, dim))
    if mode == "withstate":
        output = wrappers.Bidirectional(LSTM(units))(input2, initial_state=state)
    else:
        output = wrappers.Bidirectional(LSTM(units))(input2)
    model = Model([input1, input2], output)
    return len(model.layers)
'''


class Keras37UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras37TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS37_UTILS).body

    def _make(self, mode: str) -> ast.FunctionDef:
        dim, ts, units = self.generate_case()
        expected = 4 if mode == "withstate" else 2
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_bidir_layers"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=dim),
                                ast.Constant(value=ts),
                                ast.Constant(value=units),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("withstate"), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("plain"), TestResult.PASSING


grammar_37: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["withstate", "plain"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_37)


# ======================================================================
# bug_22: InputLayer did not set ``supports_masking = True``.  Feeding a masked
# tensor into a nested model (e.g. a Sequential wrapped in TimeDistributed) then
# raised "Layer ..._input does not support masking".  The fix sets the flag.
#
# System-test format:  ``<mode> <units> <dim> <ts>`` where ``<mode>`` is
#   ``masked`` (the trigger: a Masking layer feeds a TimeDistributed Sequential)
#   or ``nomask``.  The harness prints ``OK`` / ``ERR``; the oracle expects
#   ``OK`` (fixed for both, buggy fails ``masked``).
# ======================================================================


class Keras22API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Built"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras22TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int]:
        units = random.randint(3, 8)
        dim = random.randint(2, 6)
        ts = random.randint(2, 6)
        return units, dim, ts


class Keras22SystemtestGenerator(SystemtestGenerator, Keras22TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        units, dim, ts = self.generate_case()
        return f"masked {units} {dim} {ts}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        units, dim, ts = self.generate_case()
        return f"nomask {units} {dim} {ts}", TestResult.PASSING


_KERAS22_UTILS = '''
def _t4p_masked_seq_builds(mode, units, dim, ts):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K
    from keras import layers
    from keras.models import Model, Sequential
    K.clear_session()
    try:
        inputs = layers.Input(shape=(ts, dim))
        if mode == "masked":
            x = layers.Masking(mask_value=0.0)(inputs)
        else:
            x = inputs
        s = Sequential()
        s.add(layers.Dense(units, input_shape=(dim,)))
        s.add(layers.Activation("relu"))
        x = layers.wrappers.TimeDistributed(s)(x)
        model = Model(inputs=inputs, outputs=x)
        model.compile(optimizer="rmsprop", loss="mse")
        return True
    except Exception:
        return False
'''


class Keras22UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras22TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS22_UTILS).body

    def _make(self, mode: str) -> ast.FunctionDef:
        units, dim, ts = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_masked_seq_builds"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=units),
                                ast.Constant(value=dim),
                                ast.Constant(value=ts),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("masked"), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("nomask"), TestResult.PASSING


grammar_22: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["masked", "nomask"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_22)


# ======================================================================
# bug_4: TFOptimizer.get_updates called ``self.optimizer.compute_gradients(loss,
# params)`` -- passing ``params`` POSITIONALLY.  A native TF optimizer whose
# ``compute_gradients`` only accepts keyword args then raised a TypeError.  The
# fix passes ``var_list=params``.
#
# System-test format:  ``<mode> <num_classes> <samples> <indim> <seed>`` where
#   ``<mode>`` is ``strict`` (the trigger: a keyword-only compute_gradients) or
#   ``lenient``.  The harness compiles + fits a model and prints ``OK`` / ``ERR``;
#   the oracle expects ``OK`` (fixed for both, buggy fails ``strict``).
# ======================================================================


class Keras4API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Fitted"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras4TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int, int]:
        num_classes = random.randint(2, 5)
        samples = random.randint(4, 8)
        indim = random.randint(2, 5)
        seed = random.randint(seed_lo, seed_hi)
        return num_classes, samples, indim, seed


class Keras4SystemtestGenerator(SystemtestGenerator, Keras4TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        nc, s, d, seed = self.generate_case(0, 5000)
        return f"strict {nc} {s} {d} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        nc, s, d, seed = self.generate_case(5001, 10000)
        return f"lenient {nc} {s} {d} {seed}", TestResult.PASSING


_KERAS4_UTILS = '''
def _t4p_tfoptimizer_fits(mode, num_classes, samples, indim, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from tensorflow import train
    from keras import optimizers
    from keras.models import Sequential
    from keras.layers import Dense
    import keras.backend as K
    K.clear_session()

    class StrictOpt(train.Optimizer):
        wrapping_optimizer = train.AdamOptimizer()
        def compute_gradients(self, loss, **kwargs):
            return super(StrictOpt, self).compute_gradients(loss, **kwargs)
        def apply_gradients(self, gv, **kwargs):
            return self.wrapping_optimizer.apply_gradients(gv, **kwargs)

    class LenientOpt(train.Optimizer):
        wrapping_optimizer = train.AdamOptimizer()
        def compute_gradients(self, loss, var_list=None, **kwargs):
            return super(LenientOpt, self).compute_gradients(loss, var_list=var_list, **kwargs)
        def apply_gradients(self, gv, **kwargs):
            return self.wrapping_optimizer.apply_gradients(gv, **kwargs)

    try:
        Opt = StrictOpt if mode == "strict" else LenientOpt
        tf_opt = Opt(use_locking=False, name="T4POpt%d" % seed)
        optimizer = optimizers.TFOptimizer(tf_opt)
        model = Sequential()
        model.add(Dense(num_classes, input_shape=(indim,)))
        model.compile(loss="mean_squared_error", optimizer=optimizer)
        rng = np.random.RandomState(seed)
        model.fit(rng.random_sample((samples, indim)),
                  rng.random_sample((samples, num_classes)),
                  epochs=1, batch_size=samples, verbose=0)
        return True
    except Exception:
        return False
'''


class Keras4UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras4TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS4_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        nc, s, d, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_tfoptimizer_fits"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=nc),
                                ast.Constant(value=s),
                                ast.Constant(value=d),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("strict", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("lenient", 5001, 10000), TestResult.PASSING


grammar_4: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number>"],
            "<mode>": ["strict", "lenient"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_4)


# ======================================================================
# bug_24: TensorBoard's histogram summaries did not handle layers whose
# ``.output`` is a LIST of tensors -- it passed the list straight to
# ``tf.summary.histogram`` and failed.  The fix iterates list outputs.
#
# System-test format:  ``<mode> <D> <num_classes> <num_hidden> <seed>`` where
#   ``<mode>`` is ``hist`` (the trigger: fit with TensorBoard(histogram_freq=1)
#   on a model containing a list-output Lambda) or ``nohist``
#   (histogram_freq=0).  The harness prints ``OK`` / ``ERR``; the oracle expects
#   ``OK`` (fixed for both, buggy fails ``hist``).
# ======================================================================


class Keras24API(KerasAPI):
    def __init__(self, default_timeout: int = 240):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Fitted"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras24TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int, int]:
        D = random.randint(3, 6)
        nc = random.randint(2, 3)
        nh = random.randint(4, 8)
        seed = random.randint(seed_lo, seed_hi)
        return D, nc, nh, seed


class Keras24SystemtestGenerator(SystemtestGenerator, Keras24TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        D, nc, nh, seed = self.generate_case(0, 5000)
        return f"hist {D} {nc} {nh} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        D, nc, nh, seed = self.generate_case(5001, 10000)
        return f"nohist {D} {nc} {nh} {seed}", TestResult.PASSING


_KERAS24_UTILS = '''
def _t4p_tensorboard_fits(mode, D, nc, nh, seed):
    import os
    import tempfile
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    from keras.layers import Input, Dense, Lambda, GlobalAveragePooling1D, add, dot
    from keras.models import Model
    from keras import callbacks
    import keras.backend as K
    K.clear_session()
    try:
        rng = np.random.RandomState(seed)
        logs = tempfile.mkdtemp()
        inp1 = Input((D, D))
        inp2 = Input((D, D))
        inp_3d = add([inp1, inp2])
        inp_2d = GlobalAveragePooling1D()(inp_3d)
        inp_pair = Lambda(lambda x: x)([inp_3d, inp_2d])
        hidden = dot(inp_pair, axes=-1)
        hidden = Dense(nh, activation="relu")(hidden)
        output = Dense(nc, activation="softmax")(hidden)
        model = Model(inputs=[inp1, inp2], outputs=output)
        model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
        n = 10
        X = [rng.random_sample((n, D, D)), rng.random_sample((n, D, D))]
        Y = keras.utils.to_categorical(rng.randint(0, nc, size=(n,)), nc)
        hist = 1 if mode == "hist" else 0
        cb = [callbacks.TensorBoard(log_dir=logs, histogram_freq=hist, batch_size=5)]
        model.fit(X, Y, batch_size=5, validation_data=(X, Y), callbacks=cb, epochs=1, verbose=0)
        return True
    except Exception:
        return False
'''


class Keras24UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras24TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS24_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        D, nc, nh, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_tensorboard_fits"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=D),
                                ast.Constant(value=nc),
                                ast.Constant(value=nh),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("hist", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("nohist", 5001, 10000), TestResult.PASSING


grammar_24: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number>"],
            "<mode>": ["hist", "nohist"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_24)


# ======================================================================
# bug_42: Model.fit_generator required ``steps_per_epoch`` as a positional
# argument.  The fix makes it optional and, for a keras ``Sequence``, defaults
# to ``len(generator)``.  Calling ``fit_generator(seq)`` on the buggy build
# raises a TypeError for the missing argument.
#
# System-test format:  ``<mode> <indim> <num_classes> <seed>`` where ``<mode>``
#   is ``nostep`` (the trigger: fit_generator on a Sequence with no
#   steps_per_epoch) or ``withstep``.  The harness prints ``OK`` / ``ERR``; the
#   oracle expects ``OK`` (fixed for both, buggy fails ``nostep``).
# ======================================================================


class Keras42API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Fitted"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras42TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int]:
        indim = random.randint(2, 6)
        nc = random.randint(2, 5)
        seed = random.randint(seed_lo, seed_hi)
        return indim, nc, seed


class Keras42SystemtestGenerator(SystemtestGenerator, Keras42TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(0, 5000)
        return f"nostep {indim} {nc} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(5001, 10000)
        return f"withstep {indim} {nc} {seed}", TestResult.PASSING


_KERAS42_UTILS = '''
def _t4p_fitgen_runs(mode, indim, nc, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence
    import keras.backend as K
    K.clear_session()

    class MySeq(Sequence):
        def __init__(self, n, bs, indim, nc, seed):
            self.n = n
            self.bs = bs
            self.indim = indim
            self.nc = nc
            self.rng = np.random.RandomState(seed)

        def __len__(self):
            return self.n

        def __getitem__(self, i):
            return (self.rng.random_sample((self.bs, self.indim)),
                    self.rng.random_sample((self.bs, self.nc)))

    try:
        model = Sequential()
        model.add(Dense(nc, input_shape=(indim,)))
        model.compile("sgd", "mse")
        seq = MySeq(4, 5, indim, nc, seed)
        if mode == "nostep":
            model.fit_generator(seq, epochs=1, verbose=0)
        else:
            model.fit_generator(seq, steps_per_epoch=len(seq), epochs=1, verbose=0)
        return True
    except Exception:
        return False
'''


class Keras42UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras42TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS42_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        indim, nc, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_fitgen_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=indim),
                                ast.Constant(value=nc),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("nostep", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("withstep", 5001, 10000), TestResult.PASSING


grammar_42: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["nostep", "withstep"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_42)


# ======================================================================
# bug_16: Sequential.get_config returned a bare LIST of layer configs instead of
# a dict (``{'name', 'layers', 'build_input_shape'}``).  The fix returns the
# dict form (and stops mutating the first layer's batch_input_shape).
#
# System-test format:  ``<mode> <nlayers> <units> <indim>`` where ``<mode>`` is
#   ``cfgtype`` (the trigger: harness prints ``type(get_config()).__name__`` --
#   oracle expects ``dict``) or ``nlayers`` (harness prints ``len(model.layers)``
#   -- oracle expects nlayers, true on both builds).
# ======================================================================


class Keras16API(KerasAPI):
    def __init__(self, default_timeout: int = 120):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            nlayers = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "dict" if mode == "cfgtype" else str(nlayers)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras16TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int]:
        nlayers = random.randint(1, 3)
        units = random.randint(3, 8)
        indim = random.randint(2, 6)
        return nlayers, units, indim


class Keras16SystemtestGenerator(SystemtestGenerator, Keras16TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        nlayers, units, indim = self.generate_case()
        return f"cfgtype {nlayers} {units} {indim}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        nlayers, units, indim = self.generate_case()
        return f"nlayers {nlayers} {units} {indim}", TestResult.PASSING


_KERAS16_UTILS = '''
def _t4p_seq_build(nlayers, units, indim):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.models import Sequential
    from keras.layers import Dense
    import keras.backend as K
    K.clear_session()
    model = Sequential()
    model.add(Dense(units, input_shape=(indim,)))
    for _ in range(nlayers - 1):
        model.add(Dense(units))
    return model


def _t4p_seq_config_type(nlayers, units, indim):
    return isinstance(_t4p_seq_build(nlayers, units, indim).get_config(), dict)


def _t4p_seq_nlayers(nlayers, units, indim):
    return len(_t4p_seq_build(nlayers, units, indim).layers)
'''


class Keras16UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras16TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS16_UTILS).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nlayers, units, indim = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_seq_config_type"),
                            args=[
                                ast.Constant(value=nlayers),
                                ast.Constant(value=units),
                                ast.Constant(value=indim),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nlayers, units, indim = self.generate_case()
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Constant(value=nlayers),
                        ast.Call(
                            func=ast.Name(id="_t4p_seq_nlayers"),
                            args=[
                                ast.Constant(value=nlayers),
                                ast.Constant(value=units),
                                ast.Constant(value=indim),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]
        return test, TestResult.PASSING


grammar_16: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["cfgtype", "nlayers"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_16)


# ======================================================================
# bug_3: _clone_functional_model called ``layer.compute_mask`` even for layers
# that do not support masking.  Cloning a multi-output functional model (a
# multi-output Lambda + a multi-in/out layer) then failed.  The fix skips
# compute_mask for layers without ``supports_masking``.
#
# System-test format:  ``<mode> <dim> <seed>`` where ``<mode>`` is ``multi`` (the
#   trigger: clone a multi-output model) or ``single``.  The harness prints
#   ``OK`` / ``ERR``; the oracle expects ``OK`` (fixed for both, buggy fails
#   ``multi``).
# ======================================================================


class Keras3API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Cloned"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras3TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int]:
        dim = random.randint(3, 8)
        seed = random.randint(seed_lo, seed_hi)
        return dim, seed


class Keras3SystemtestGenerator(SystemtestGenerator, Keras3TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        dim, seed = self.generate_case(0, 5000)
        return f"multi {dim} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        dim, seed = self.generate_case(5001, 10000)
        return f"single {dim} {seed}", TestResult.PASSING


_KERAS3_UTILS = '''
def _t4p_clone_runs(mode, dim, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    import keras.backend as K
    K.clear_session()
    try:
        input_layer = keras.Input(shape=(dim,))
        if mode == "multi":
            layer1 = keras.layers.Lambda(lambda x: [x + 1, x], lambda s: [s, s])
            x_a, x_b = layer1(input_layer)

            class SwapLayer(keras.layers.Layer):
                def call(self, inputs, **kwargs):
                    return [inputs[1], inputs[0]]

                def compute_output_shape(self, s):
                    return [s[1], s[0]]

            x_a, x_b = SwapLayer()([x_a, x_b])
            model = keras.Model(inputs=[input_layer], outputs=[x_a, x_b])
        else:
            out = keras.layers.Dense(dim)(input_layer)
            model = keras.Model(inputs=[input_layer], outputs=[out])
        new_model = keras.models.clone_model(model)
        x = np.random.RandomState(seed).random_sample((6, dim))
        new_model.predict(x)
        return True
    except Exception:
        return False
'''


class Keras3UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras3TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS3_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        dim, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_clone_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=dim),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("multi", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("single", 5001, 10000), TestResult.PASSING


grammar_3: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number>"],
            "<mode>": ["multi", "single"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_3)


# ======================================================================
# bug_23: Sequential's build read the (possibly nested) first layer's
# ``batch_input_shape`` / ``dtype`` unconditionally.  A nested, deferred-build
# Sequential (inner model with no input_shape) then raised AttributeError.  The
# fix only reads those attributes when present.
#
# System-test format:  ``<mode> <inner_units> <out_units> <indim> <seed>`` where
#   ``<mode>`` is ``deferred`` (the trigger: nested Sequential with no
#   input_shape) or ``explicit``.  The harness prints ``OK`` / ``ERR``; the
#   oracle expects ``OK`` (fixed for both, buggy fails ``deferred``).
# ======================================================================


class Keras23API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Trained"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras23TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int, int]:
        inner_units = random.randint(2, 6)
        out_units = random.randint(2, 7)
        indim = random.randint(2, 6)
        seed = random.randint(seed_lo, seed_hi)
        return inner_units, out_units, indim, seed


class Keras23SystemtestGenerator(SystemtestGenerator, Keras23TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        iu, ou, d, seed = self.generate_case(0, 5000)
        return f"deferred {iu} {ou} {d} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        iu, ou, d, seed = self.generate_case(5001, 10000)
        return f"explicit {iu} {ou} {d} {seed}", TestResult.PASSING


_KERAS23_UTILS = '''
def _t4p_nested_seq_runs(mode, inner_units, out_units, indim, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    import keras.backend as K
    K.clear_session()
    try:
        inner = keras.models.Sequential()
        if mode == "deferred":
            inner.add(keras.layers.Dense(inner_units))
        else:
            inner.add(keras.layers.Dense(inner_units, input_shape=(indim,)))
        inner.add(keras.layers.Dense(inner_units))
        model = keras.models.Sequential()
        model.add(inner)
        model.add(keras.layers.Dense(out_units))
        model.compile("sgd", "mse")
        rng = np.random.RandomState(seed)
        model.train_on_batch(rng.random_sample((2, indim)), rng.random_sample((2, out_units)))
        return True
    except Exception:
        return False
'''


class Keras23UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras23TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS23_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        iu, ou, d, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_nested_seq_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=iu),
                                ast.Constant(value=ou),
                                ast.Constant(value=d),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("deferred", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("explicit", 5001, 10000), TestResult.PASSING


grammar_23: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number>"],
            "<mode>": ["deferred", "explicit"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_23)


# ======================================================================
# bug_8: Network reconstruction (Model.from_config) processed layer nodes in
# config order and raised when a shared layer was applied at heterogeneous depth
# (a node referenced an inbound node not yet created).  The fix re-queues such
# unprocessed nodes.  The buggy from_config mis-wires the graph.
#
# System-test format:  ``<mode> <D> <out> <seed>`` where ``<mode>`` is ``shared``
#   (the trigger: a shared Dense at heterogeneous depth, round-tripped through
#   from_config) or ``simple``.  The harness prints ``OK`` / ``ERR``; the oracle
#   expects ``OK`` (fixed for both, buggy fails ``shared``).
# ======================================================================


class Keras8API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Round-tripped"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras8TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int]:
        D = random.randint(6, 16)
        out = random.randint(2, 5)
        seed = random.randint(seed_lo, seed_hi)
        return D, out, seed


class Keras8SystemtestGenerator(SystemtestGenerator, Keras8TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        D, out, seed = self.generate_case(0, 5000)
        return f"shared {D} {out} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        D, out, seed = self.generate_case(5001, 10000)
        return f"simple {D} {out} {seed}", TestResult.PASSING


_KERAS8_UTILS = '''
def _t4p_from_config_runs(mode, D, out, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.layers import Input, Dense, Reshape, concatenate
    from keras.models import Model
    import keras.backend as K
    K.clear_session()
    try:
        input_shape = (1, D)
        inp = Input(shape=input_shape)
        if mode == "shared":
            A = Dense(D, name="layer_a")
            r1 = Reshape((D,))(inp)
            Aout1 = A(r1)
            r2 = Reshape((D,))(A(inp))
            Aout2 = A(r2)
            c1 = concatenate([Aout2, Aout1])
            output = Dense(out, name="layer_b")(c1)
        else:
            r1 = Reshape((D,))(inp)
            h = Dense(D)(r1)
            output = Dense(out)(h)
        model = Model(inputs=inp, outputs=output)
        x = np.random.RandomState(seed).random_sample((5,) + input_shape)
        model.predict(x)
        config = model.get_config()
        weights = model.get_weights()
        model2 = Model.from_config(config)
        model2.set_weights(weights)
        model2.predict(x)
        return True
    except Exception:
        return False
'''


class Keras8UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras8TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS8_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        D, out, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_from_config_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=D),
                                ast.Constant(value=out),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("shared", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("simple", 5001, 10000), TestResult.PASSING


grammar_8: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["shared", "simple"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_8)


# ======================================================================
# bug_30: evaluate_generator / predict_generator computed the batch size from
# ``x`` without handling framework-native data tensors, where the generator
# yields ``x = None``.  ``None.shape`` then raised.  The fix uses batch_size = 1
# when x is None/empty.
#
# System-test format:  ``<mode> <D> <units> <n> <seed>`` where ``<mode>`` is
#   ``datatensor`` (the trigger: an Input(tensor=...) model driven by a
#   None-yielding generator) or ``normal``.  The harness prints ``OK`` / ``ERR``;
#   the oracle expects ``OK`` (fixed for both, buggy fails ``datatensor``).
# ======================================================================


class Keras30API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Ran"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras30TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int, int]:
        D = random.randint(2, 6)
        units = random.randint(3, 6)
        n = random.randint(6, 12)
        seed = random.randint(seed_lo, seed_hi)
        return D, units, n, seed


class Keras30SystemtestGenerator(SystemtestGenerator, Keras30TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        D, u, n, seed = self.generate_case(0, 5000)
        return f"datatensor {D} {u} {n} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        D, u, n, seed = self.generate_case(5001, 10000)
        return f"normal {D} {u} {n} {seed}", TestResult.PASSING


_KERAS30_UTILS = '''
def _t4p_datatensor_eval_runs(mode, D, units, n, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import tensorflow as tf
    from keras.layers import Input, Dense, Dropout
    from keras.models import Model
    import keras.backend as K
    K.clear_session()
    rng = np.random.RandomState(seed)
    try:
        if mode == "datatensor":
            data = rng.random_sample((n, D)).astype("float32")
            a = Input(tensor=tf.Variable(data, dtype=tf.float32))
            a2 = Dense(units, name="d1")(a)
            a2 = Dropout(0.5)(a2)
            model = Model(a, a2)
            model.add_loss(K.mean(a2))
            model.compile(optimizer="rmsprop", loss=None, metrics=["mse"])

            def gen():
                while True:
                    yield (None, None)

            model.evaluate_generator(gen(), steps=3)
            model.predict_generator(gen(), steps=3)
        else:
            a = Input(shape=(D,))
            out = Dense(units)(a)
            model = Model(a, out)
            model.compile("rmsprop", "mse", metrics=["mse"])

            def gen():
                while True:
                    yield (rng.random_sample((5, D)), rng.random_sample((5, units)))

            model.evaluate_generator(gen(), steps=3)
        return True
    except Exception:
        return False
'''


class Keras30UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras30TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS30_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        D, u, n, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_datatensor_eval_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=D),
                                ast.Constant(value=u),
                                ast.Constant(value=n),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("datatensor", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("normal", 5001, 10000), TestResult.PASSING


grammar_30: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number>"],
            "<mode>": ["datatensor", "normal"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_30)


# ======================================================================
# bug_29: stateful metrics were not reliably reset between fit/evaluate because
# the reset loop iterated ``self.metrics`` (which, in DICT metrics mode, does not
# expose the metric layer).  The fix tracks ``stateful_metric_functions`` and
# resets those.  In dict mode the buggy metric therefore ACCUMULATES.
#
# System-test format:  ``<mode> <samples> <seed>`` where ``<mode>`` is ``dict``
#   (the trigger) or ``list``.  The harness fits + evaluates a stateful
#   true-positives metric and prints ``MATCH`` iff it equals the numpy-recomputed
#   count; the oracle expects ``MATCH`` (fixed for both, buggy fails ``dict``).
# ======================================================================


class Keras29API(KerasAPI):
    def __init__(self, default_timeout: int = 240):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "MATCH":
            return TestResult.PASSING, "Metric reset correctly"
        return TestResult.FAILING, f"Expected 'MATCH', but was {out!r}"


class Keras29TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int]:
        samples = random.randint(150, 300)
        seed = random.randint(seed_lo, seed_hi)
        return samples, seed


class Keras29SystemtestGenerator(SystemtestGenerator, Keras29TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        samples, seed = self.generate_case(0, 5000)
        return f"dict {samples} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        samples, seed = self.generate_case(5001, 10000)
        return f"list {samples} {seed}", TestResult.PASSING


_KERAS29_UTILS = '''
def _t4p_stateful_metric_matches(mode, samples, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    import keras.backend as K
    K.clear_session()

    class BinaryTruePositives(keras.layers.Layer):
        def __init__(self, name="true_positives", **kwargs):
            super(BinaryTruePositives, self).__init__(name=name, **kwargs)
            self.stateful = True
            self.true_positives = K.variable(value=0, dtype="int32")

        def reset_states(self):
            K.set_value(self.true_positives, 0)

        def __call__(self, y_true, y_pred):
            y_true = K.cast(y_true, "int32")
            y_pred = K.cast(K.round(y_pred), "int32")
            correct_preds = K.cast(K.equal(y_pred, y_true), "int32")
            true_pos = K.cast(K.sum(correct_preds * y_true), "int32")
            current_true_pos = self.true_positives * 1
            self.add_update(K.update_add(self.true_positives, true_pos), inputs=[y_true, y_pred])
            return current_true_pos + true_pos

    try:
        np.random.seed(seed)
        metric_fn = BinaryTruePositives()
        inputs = keras.Input(shape=(2,))
        outputs = keras.layers.Dense(1, activation="sigmoid", name="out",
                                     bias_initializer=keras.initializers.Constant(5.0))(inputs)
        model = keras.Model(inputs, outputs)
        if mode == "dict":
            model.compile("sgd", "binary_crossentropy", metrics={"out": ["acc", metric_fn]})
        else:
            model.compile("sgd", "binary_crossentropy", metrics=["acc", metric_fn])
        x = np.random.random((samples, 2))
        y = np.random.randint(2, size=(samples, 1))
        model.fit(x, y, epochs=1, batch_size=10, verbose=0)
        idx = [i for i, n in enumerate(model.metrics_names) if "true_positives" in n][0]
        outs = model.evaluate(x, y, batch_size=10, verbose=0)
        preds = model.predict(x)
        ref = np.sum(np.logical_and(preds[:, 0] > 0.5, y[:, 0] == 1))
        return bool(np.isclose(outs[idx], ref, atol=1e-4))
    except Exception:
        return False
'''


class Keras29UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras29TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS29_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        samples, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_stateful_metric_matches"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=samples),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("dict", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("list", 5001, 10000), TestResult.PASSING


grammar_29: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number>"],
            "<mode>": ["dict", "list"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_29)


# ======================================================================
# bug_34: the generator training loops assigned ``output_generator = generator``
# for the no-worker (workers=0) path.  A keras ``Sequence`` is NOT an iterator,
# so ``next(output_generator)`` raised ``TypeError``.  The fix wraps a Sequence
# with ``iter(...)``.
#
# System-test format:  ``<mode> <indim> <num_classes> <seed>`` where ``<mode>``
#   is ``workers0`` (the trigger: fit_generator on a Sequence with workers=0) or
#   ``workers1``.  The harness prints ``OK`` / ``ERR``; the oracle expects ``OK``
#   (fixed for both, buggy fails ``workers0``).
# ======================================================================


class Keras34API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Fitted"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras34TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int]:
        indim = random.randint(2, 6)
        nc = random.randint(2, 5)
        seed = random.randint(seed_lo, seed_hi)
        return indim, nc, seed


class Keras34SystemtestGenerator(SystemtestGenerator, Keras34TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(0, 5000)
        return f"workers0 {indim} {nc} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(5001, 10000)
        return f"workers1 {indim} {nc} {seed}", TestResult.PASSING


_KERAS34_UTILS = '''
def _t4p_fitgen_workers_runs(mode, indim, nc, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence
    import keras.backend as K
    K.clear_session()

    class MySeq(Sequence):
        def __init__(self, n, bs, indim, nc, seed):
            self.n = n
            self.bs = bs
            self.indim = indim
            self.nc = nc
            self.rng = np.random.RandomState(seed)

        def __len__(self):
            return self.n

        def __getitem__(self, i):
            return (self.rng.random_sample((self.bs, self.indim)),
                    self.rng.random_sample((self.bs, self.nc)))

    try:
        model = Sequential()
        model.add(Dense(nc, input_shape=(indim,)))
        model.compile("sgd", "mse")
        seq = MySeq(4, 5, indim, nc, seed)
        workers = 0 if mode == "workers0" else 1
        model.fit_generator(seq, steps_per_epoch=len(seq), epochs=1, workers=workers, verbose=0)
        return True
    except Exception:
        return False
'''


class Keras34UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras34TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS34_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        indim, nc, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_fitgen_workers_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=indim),
                                ast.Constant(value=nc),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("workers0", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("workers1", 5001, 10000), TestResult.PASSING


grammar_34: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["workers0", "workers1"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_34)


# ======================================================================
# bug_11: fit_generator detected a ``Sequence`` with a strict
# ``isinstance(generator, Sequence)`` check.  A duck-typed Sequence (``__len__``
# + ``__getitem__`` but not a subclass) was therefore treated as a plain
# generator, so ``steps_per_epoch=None`` raised.  The fix uses duck-typed
# ``is_sequence``.
#
# System-test format:  ``<mode> <indim> <num_classes> <seed>`` where ``<mode>``
#   is ``duck`` (the trigger: a duck-typed Sequence with no steps_per_epoch) or
#   ``real`` (a real Sequence subclass).  The harness prints ``OK`` / ``ERR``;
#   the oracle expects ``OK`` (fixed for both, buggy fails ``duck``).
# ======================================================================


class Keras11API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Fitted"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Keras11TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int]:
        indim = random.randint(2, 6)
        nc = random.randint(2, 5)
        seed = random.randint(seed_lo, seed_hi)
        return indim, nc, seed


class Keras11SystemtestGenerator(SystemtestGenerator, Keras11TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(0, 5000)
        return f"duck {indim} {nc} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(5001, 10000)
        return f"real {indim} {nc} {seed}", TestResult.PASSING


_KERAS11_UTILS = '''
def _t4p_ducktyped_fitgen_runs(mode, indim, nc, seed):
    import os
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence
    import keras.backend as K
    K.clear_session()

    class DuckSeq(object):
        use_sequence_api = True

        def __init__(self, n, bs, indim, nc, seed):
            self.n = n
            self.bs = bs
            self.indim = indim
            self.nc = nc
            self.rng = np.random.RandomState(seed)

        def __len__(self):
            return self.n

        def __getitem__(self, i):
            return (self.rng.random_sample((self.bs, self.indim)),
                    self.rng.random_sample((self.bs, self.nc)))

    class RealSeq(Sequence):
        def __init__(self, n, bs, indim, nc, seed):
            self.n = n
            self.bs = bs
            self.indim = indim
            self.nc = nc
            self.rng = np.random.RandomState(seed)

        def __len__(self):
            return self.n

        def __getitem__(self, i):
            return (self.rng.random_sample((self.bs, self.indim)),
                    self.rng.random_sample((self.bs, self.nc)))

    try:
        model = Sequential()
        model.add(Dense(nc, input_shape=(indim,)))
        model.compile("sgd", "mse")
        seq = DuckSeq(4, 5, indim, nc, seed) if mode == "duck" else RealSeq(4, 5, indim, nc, seed)
        model.fit_generator(seq, epochs=1, verbose=0)
        return True
    except Exception:
        return False
'''


class Keras11UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras11TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS11_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        indim, nc, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_ducktyped_fitgen_runs"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=indim),
                                ast.Constant(value=nc),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("duck", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("real", 5001, 10000), TestResult.PASSING


grammar_11: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["duck", "real"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_11)


# ======================================================================
# bug_13: fit_generator's Sequence-based validation used the TRAINING generator
# (``iter_sequence_infinite(generator)``) instead of the validation data, so the
# validation Sequence was never read.  The fix iterates ``val_data`` (and
# defaults validation_steps to len(val_data)).
#
# System-test format:  ``<mode> <indim> <num_classes> <seed>``.  A tracked
#   validation Sequence records each ``__getitem__``.  ``<mode>`` is ``val`` (the
#   trigger: report whether the VALIDATION Sequence was read) or ``train``
#   (whether the TRAINING Sequence was read).  The harness prints ``ACCESSED`` /
#   ``NOTACCESSED``; the oracle expects ``ACCESSED`` -- true on both for
#   ``train``, but only on the fixed build for ``val``.
# ======================================================================


class Keras13API(KerasAPI):
    def __init__(self, default_timeout: int = 180):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "ACCESSED":
            return TestResult.PASSING, "Data accessed"
        return TestResult.FAILING, f"Expected 'ACCESSED', but was {out!r}"


class Keras13TestGenerator:
    @staticmethod
    def generate_case(seed_lo: int, seed_hi: int) -> Tuple[int, int, int]:
        indim = random.randint(2, 6)
        nc = random.randint(2, 5)
        seed = random.randint(seed_lo, seed_hi)
        return indim, nc, seed


class Keras13SystemtestGenerator(SystemtestGenerator, Keras13TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(0, 5000)
        return f"val {indim} {nc} {seed}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        indim, nc, seed = self.generate_case(5001, 10000)
        return f"train {indim} {nc} {seed}", TestResult.PASSING


_KERAS13_UTILS = '''
def _t4p_val_data_accessed(mode, indim, nc, seed):
    import os
    import tempfile
    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence
    import keras.backend as K
    K.clear_session()

    class TrackSeq(Sequence):
        def __init__(self, n, bs, indim, nc, seed, path):
            self.n = n
            self.bs = bs
            self.indim = indim
            self.nc = nc
            self.rng = np.random.RandomState(seed)
            self.path = path

        def __len__(self):
            return self.n

        def __getitem__(self, i):
            with open(self.path, "a") as f:
                f.write("x")
            return (self.rng.random_sample((self.bs, self.indim)),
                    self.rng.random_sample((self.bs, self.nc)))

    try:
        model = Sequential()
        model.add(Dense(nc, input_shape=(indim,)))
        model.compile("sgd", "mse")
        tpath = tempfile.mktemp(); open(tpath, "w").close()
        vpath = tempfile.mktemp(); open(vpath, "w").close()
        train = TrackSeq(4, 5, indim, nc, seed, tpath)
        val = TrackSeq(3, 5, indim, nc, seed + 1, vpath)
        model.fit_generator(train, steps_per_epoch=len(train), validation_data=val,
                            validation_steps=len(val), epochs=1, workers=0, verbose=0)
        count = len(open(vpath).read()) if mode == "val" else len(open(tpath).read())
        return count > 0
    except Exception:
        return False
'''


class Keras13UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras13TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS13_UTILS).body

    def _make(self, mode: str, seed_lo: int, seed_hi: int) -> ast.FunctionDef:
        indim, nc, seed = self.generate_case(seed_lo, seed_hi)
        test = self.get_empty_test()
        test.body = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="_t4p_val_data_accessed"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=indim),
                                ast.Constant(value=nc),
                                ast.Constant(value=seed),
                            ],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                )
            )
        ]
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("val", 0, 5000), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._make("train", 5001, 10000), TestResult.PASSING


grammar_13: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["val", "train"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_13)


# ======================================================================
# bug_33: keras.preprocessing.text.text_to_word_sequence built its
# translation map with ``maketrans(filters, split * len(filters))``, which
# requires the two arguments to have equal length.  A MULTI-CHARACTER
# ``split`` therefore raised ``ValueError`` ("arguments must have equal
# length").  The fix builds the map from a ``{char: split}`` dict.
#
# System-test format:  ``<split> <word1> <word2> ...`` where ``<split>`` is
#   a digit string (digits survive ``lower()`` and are not filter chars).
#   The harness builds ``text = split.join(words)``, calls
#   text_to_word_sequence(text, split=split) and prints the result list.
#   A multi-digit split triggers the fault; a single-digit split does not.
#   The oracle expects the list of input words.
# ======================================================================


class Keras33API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        words = list(process.args[3:])
        if not words:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(words)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras33TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 7)))

    def generate_words(self) -> List[str]:
        return [self.generate_word() for _ in range(random.randint(2, 5))]

    @staticmethod
    def generate_multichar_split() -> str:
        return "".join(random.choices(string.digits, k=random.randint(2, 3)))

    @staticmethod
    def generate_single_split() -> str:
        return random.choice(string.digits)


class Keras33SystemtestGenerator(SystemtestGenerator, Keras33TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{self.generate_multichar_split()} " + " ".join(self.generate_words()),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{self.generate_single_split()} " + " ".join(self.generate_words()),
            TestResult.PASSING,
        )


_KERAS33_UTILS = '''
def _t4p_text_to_word_sequence(split, words):
    import os
    import importlib.util
    path = os.path.join(os.getcwd(), 'keras', 'preprocessing', 'text.py')
    spec = importlib.util.spec_from_file_location('t4p_text', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    text = split.join(words)
    return module.text_to_word_sequence(text, split=split)
'''


class Keras33UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras33TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS33_UTILS).body

    @staticmethod
    def _assert(split: str, words: List[str]) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.List(elts=[ast.Constant(value=w) for w in words]),
                        ast.Call(
                            func=ast.Name(id="_t4p_text_to_word_sequence"),
                            args=[
                                ast.Constant(value=split),
                                ast.List(
                                    elts=[ast.Constant(value=w) for w in words]
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        split = self.generate_multichar_split()
        words = self.generate_words()
        test = self.get_empty_test()
        test.body = self._assert(split, words)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        split = self.generate_single_split()
        words = self.generate_words()
        test = self.get_empty_test()
        test.body = self._assert(split, words)
        return test, TestResult.PASSING


grammar_33: Grammar = clean_up(
    {
        "<start>": ["<split><words>"],
        "<split>": ["<digit>", "<digit><split>"],
        "<digit>": srange(string.digits),
        "<words>": [" <word>", " <word><words>"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_33)


# ======================================================================
# bug_39: keras.utils.generic_utils.Progbar.update early-return guard read
# ``current < self.target`` unconditionally.  With ``target=None`` (progress
# bar of unknown length) this evaluates ``current < None``, which raises
# ``TypeError`` on Python 3.  The fix guards it with
# ``self.target is not None and current < self.target``.
#
# generic_utils.py only depends on numpy/six/stdlib, so the harness loads the
# module source directly (bypassing keras/__init__ and the TF backend).  A
# large ``interval`` makes the timing-gated early-return branch fire
# deterministically on the first ``update`` call (independent of wall-clock
# jitter on a loaded machine).
#
# System-test format:  ``<mode> <v1> <v2> ...`` where ``<mode>`` is ``none``
#   (target=None -> the trigger) or a positive integer (used as target).  The
#   ``<vi>`` are the ``current`` indices passed to ``update``.  The harness
#   prints ``RESULT:OK`` iff every update succeeds; the oracle treats OK
#   (fixed behaviour) as PASSING.
# ======================================================================


class Keras39API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if process.returncode == 0 and marker == "OK":
            return TestResult.PASSING, "progbar update succeeded"
        return TestResult.FAILING, f"expected OK, got {marker!r}"


class Keras39TestGenerator:
    @staticmethod
    def generate_vals() -> List[int]:
        return [random.randint(0, 20) for _ in range(random.randint(1, 4))]

    @staticmethod
    def generate_target() -> int:
        return random.randint(2, 20)


class Keras39SystemtestGenerator(SystemtestGenerator, Keras39TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            "none " + " ".join(map(str, self.generate_vals())),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{self.generate_target()} " + " ".join(map(str, self.generate_vals())),
            TestResult.PASSING,
        )


_KERAS39_UTILS = '''
def _t4p_progbar_update(mode, vals):
    import os
    import io
    import contextlib
    import importlib.util
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'generic_utils.py')
    spec = importlib.util.spec_from_file_location('t4p_generic_utils', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    target = None if mode == 'none' else int(mode)
    p = module.Progbar(target, width=30, verbose=1, interval=1e12)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        for v in vals:
            p.update(v)
    return 'OK'
'''


class Keras39UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras39TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS39_UTILS).body

    @staticmethod
    def _assert(mode: str, vals: List[int]) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value="OK"),
                        ast.Call(
                            func=ast.Name(id="_t4p_progbar_update"),
                            args=[
                                ast.Constant(value=mode),
                                ast.List(
                                    elts=[ast.Constant(value=v) for v in vals]
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("none", self.generate_vals())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(str(self.generate_target()), self.generate_vals())
        return test, TestResult.PASSING


grammar_39: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number><values>"],
            "<mode>": ["none", "<number>"],
            "<values>": ["", " <number><values>"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_39)


# ======================================================================
# bug_28: keras.preprocessing.sequence.TimeseriesGenerator had an off-by-one
# in ``__len__`` (and ``__getitem__``): it computed the number of batches as
# ``ceil((end_index - start_index) / (batch_size * stride))`` where
# ``end_index`` is the INCLUSIVE last usable index.  The correct count is
# ``ceil((end_index - start_index + 1) / (batch_size * stride))`` -- the buggy
# version misses the final sample whenever ``(end_index - start_index)`` is an
# exact multiple of ``batch_size * stride``.
#
# sequence.py imports ``Sequence`` from ``keras.utils.data_utils`` (a relative
# import) but uses it only as an abstract base class, so the harness injects a
# tiny stub ``keras.utils.data_utils.Sequence`` into ``sys.modules`` and loads
# the module source directly (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<n> <length> <batch_size> <stride>`` describing a
#   generator over ``n`` consecutive timesteps.  The harness prints ``len(g)``;
#   the oracle recomputes the correct (fixed) batch count
#   ``ceil((n - length) / (batch_size * stride))``.  ``batch_size*stride == 1``
#   always triggers the off-by-one (failing); a larger, non-dividing span
#   leaves ``len`` unchanged (passing).
# ======================================================================


class Keras28API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            n = int(process.args[2])
            length = int(process.args[3])
            batch_size = int(process.args[4])
            stride = int(process.args[5])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = int(math.ceil((n - length) / (batch_size * stride)))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras28TestGenerator:
    @staticmethod
    def generate_failing_case() -> Tuple[int, int, int, int]:
        # batch_size * stride == 1 => the off-by-one always drops one batch.
        length = random.randint(2, 6)
        n = random.randint(length + 2, length + 12)
        return n, length, 1, 1

    @staticmethod
    def generate_passing_case() -> Tuple[int, int, int, int]:
        # batch_size * stride > 1 and the span not a multiple of it => the
        # ceil() is unchanged by the +1, so buggy and fixed agree.
        while True:
            length = random.randint(2, 6)
            batch_size = random.randint(2, 4)
            stride = random.randint(1, 3)
            m = batch_size * stride
            if m == 1:
                continue
            n = random.randint(length + 2, length + 14)
            d = n - 1 - length
            if d >= 1 and d % m != 0:
                return n, length, batch_size, stride


class Keras28SystemtestGenerator(SystemtestGenerator, Keras28TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        n, length, batch_size, stride = self.generate_failing_case()
        return f"{n} {length} {batch_size} {stride}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        n, length, batch_size, stride = self.generate_passing_case()
        return f"{n} {length} {batch_size} {stride}", TestResult.PASSING


_KERAS28_UTILS = '''
def _t4p_timeseries_len(n, length, batch_size, stride):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    prep = types.ModuleType('keras.preprocessing'); prep.__path__ = []
    data_utils = types.ModuleType('keras.utils.data_utils')
    class Sequence(object):
        def __iter__(self):
            for i in range(len(self)):
                yield self[i]
    data_utils.Sequence = Sequence
    sys.modules['keras'] = keras
    sys.modules['keras.utils'] = utils
    sys.modules['keras.preprocessing'] = prep
    sys.modules['keras.utils.data_utils'] = data_utils
    path = os.path.join(os.getcwd(), 'keras', 'preprocessing', 'sequence.py')
    spec = importlib.util.spec_from_file_location('keras.preprocessing.sequence', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.preprocessing.sequence'] = module
    spec.loader.exec_module(module)
    data = np.arange(n).reshape(-1, 1)
    g = module.TimeseriesGenerator(data, data, length=length,
                                   batch_size=batch_size, stride=stride)
    return len(g)
'''


class Keras28UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras28TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS28_UTILS).body

    @staticmethod
    def _assert(n: int, length: int, batch_size: int, stride: int) -> List[ast.stmt]:
        expected = int(math.ceil((n - length) / (batch_size * stride)))
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_timeseries_len"),
                            args=[
                                ast.Constant(value=n),
                                ast.Constant(value=length),
                                ast.Constant(value=batch_size),
                                ast.Constant(value=stride),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_passing_case())
        return test, TestResult.PASSING


grammar_28: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <number> <number> <number>"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_28)


# ======================================================================
# bug_25: keras.applications.imagenet_utils._preprocess_numpy_input applied the
# scaling / mean-subtraction in place (``x /= 127.5``, ``x[..., 0] -= mean``,
# ...) WITHOUT first casting to float.  For an INTEGER input array the in-place
# float operations raise ``TypeError`` / ``UFuncTypeError`` (numpy refuses the
# ``same_kind`` cast).  The fix casts up front: ``x = x.astype(K.floatx())``.
#
# imagenet_utils.py has relative imports (``from ..utils.data_utils import
# get_file`` and ``from .. import backend as K``); the numpy code path only
# touches ``K.image_data_format`` / ``K.floatx``, so the harness injects tiny
# stubs into ``sys.modules`` and loads the module source directly (bypassing
# keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <dtype> <h> <w>`` where ``<mode>`` is ``tf`` /
#   ``caffe`` / ``torch``, ``<dtype>`` is ``int`` (the trigger) or ``float``,
#   and ``<h> <w>`` size the ``(h, w, 3)`` pixel array.  The harness prints
#   ``RESULT:OK`` iff ``preprocess_input`` succeeds; the oracle treats OK
#   (fixed behaviour) as PASSING.
# ======================================================================


class Keras25API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if process.returncode == 0 and marker == "OK":
            return TestResult.PASSING, "preprocess_input succeeded"
        return TestResult.FAILING, f"expected OK, got {marker!r}"


class Keras25TestGenerator:
    MODES = ["tf", "caffe", "torch"]

    def generate_dims(self) -> Tuple[int, int]:
        return random.randint(2, 6), random.randint(2, 6)

    def generate_failing_case(self) -> Tuple[str, str, int, int]:
        h, w = self.generate_dims()
        return random.choice(self.MODES), "int", h, w

    def generate_passing_case(self) -> Tuple[str, str, int, int]:
        h, w = self.generate_dims()
        return random.choice(self.MODES), "float", h, w


class Keras25SystemtestGenerator(SystemtestGenerator, Keras25TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        mode, dtype, h, w = self.generate_failing_case()
        return f"{mode} {dtype} {h} {w}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode, dtype, h, w = self.generate_passing_case()
        return f"{mode} {dtype} {h} {w}", TestResult.PASSING


_KERAS25_UTILS = '''
def _t4p_preprocess_input(mode, dtype, h, w):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    apps = types.ModuleType('keras.applications'); apps.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    data_utils = types.ModuleType('keras.utils.data_utils')
    data_utils.get_file = lambda *a, **k: None
    backend = types.ModuleType('keras.backend')
    backend.image_data_format = lambda: 'channels_last'
    backend.floatx = lambda: 'float32'
    for name, module in [('keras', keras), ('keras.applications', apps),
                         ('keras.utils', utils),
                         ('keras.utils.data_utils', data_utils),
                         ('keras.backend', backend)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'applications', 'imagenet_utils.py')
    spec = importlib.util.spec_from_file_location(
        'keras.applications.imagenet_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.applications.imagenet_utils'] = module
    spec.loader.exec_module(module)
    base = (np.arange(h * w * 3) % 256).reshape(h, w, 3)
    arr = base.astype('int32') if dtype == 'int' else base.astype('float64')
    module.preprocess_input(arr, 'channels_last', mode)
    return 'OK'
'''


class Keras25UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras25TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS25_UTILS).body

    @staticmethod
    def _assert(mode: str, dtype: str, h: int, w: int) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value="OK"),
                        ast.Call(
                            func=ast.Name(id="_t4p_preprocess_input"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=dtype),
                                ast.Constant(value=h),
                                ast.Constant(value=w),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_passing_case())
        return test, TestResult.PASSING


grammar_25: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <dtype> <number> <number>"],
            "<mode>": ["tf", "caffe", "torch"],
            "<dtype>": ["int", "float"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_25)


# ======================================================================
# bug_20: keras.utils.conv_utils.deconv_length (used by Conv2DTranspose to
# infer the transposed-convolution output length) did not support dilation.
# Its signature was ``deconv_length(dim_size, stride_size, kernel_size,
# padding, output_padding)`` -- 5 parameters.  The fix adds a ``dilation=1``
# parameter and inflates the effective kernel size
# (``kernel + (kernel - 1) * (dilation - 1)``) so dilated transposed convs
# compute the right shape.  On the buggy build, calling ``deconv_length`` with
# a dilation argument raises ``TypeError`` (too many arguments).
#
# conv_utils.py's only keras dependency is ``from .. import backend as K``,
# which ``deconv_length`` never touches, so the harness injects an empty
# ``keras.backend`` stub into ``sys.modules`` and loads the module source
# directly (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <dim> <stride> <kernel> <padding> <outpad>
#   <dilation>`` where ``<mode>`` is ``dil`` (pass the dilation arg -> the
#   trigger) or ``nodil`` (5-arg call), ``<padding>`` is same/valid/full and
#   ``<outpad>`` is ``none`` or an integer.  The harness prints the returned
#   length; the oracle recomputes the correct (fixed) length.
# ======================================================================


def _fixed_deconv_length(dim_size, stride_size, kernel_size, padding,
                         output_padding, dilation):
    if dim_size is None:
        return None
    kernel_size = kernel_size + (kernel_size - 1) * (dilation - 1)
    if output_padding is None:
        if padding == "valid":
            dim_size = dim_size * stride_size + max(kernel_size - stride_size, 0)
        elif padding == "full":
            dim_size = dim_size * stride_size - (stride_size + kernel_size - 2)
        elif padding == "same":
            dim_size = dim_size * stride_size
    else:
        if padding == "same":
            pad = kernel_size // 2
        elif padding == "valid":
            pad = 0
        elif padding == "full":
            pad = kernel_size - 1
        dim_size = (dim_size - 1) * stride_size + kernel_size - 2 * pad + output_padding
    return dim_size


class Keras20API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            dim = int(process.args[3])
            stride = int(process.args[4])
            kernel = int(process.args[5])
            padding = process.args[6]
            op = process.args[7]
            out_pad = None if op == "none" else int(op)
            dilation = int(process.args[8]) if mode == "dil" else 1
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _fixed_deconv_length(dim, stride, kernel, padding, out_pad, dilation)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras20TestGenerator:
    PADDINGS = ["same", "valid", "full"]

    def generate_params(self) -> Tuple[int, int, int, str, str]:
        dim = random.randint(2, 12)
        stride = random.randint(1, 3)
        kernel = random.randint(1, 5)
        padding = random.choice(self.PADDINGS)
        out_pad = "none" if random.random() < 0.5 else str(random.randint(0, stride - 1))
        return dim, stride, kernel, padding, out_pad

    def generate_failing_case(self) -> Tuple[str, int, int, int, str, str, int]:
        dim, stride, kernel, padding, out_pad = self.generate_params()
        return "dil", dim, stride, kernel, padding, out_pad, random.randint(2, 4)

    def generate_passing_case(self) -> Tuple[str, int, int, int, str, str, int]:
        dim, stride, kernel, padding, out_pad = self.generate_params()
        return "nodil", dim, stride, kernel, padding, out_pad, 1


class Keras20SystemtestGenerator(SystemtestGenerator, Keras20TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        mode, dim, stride, kernel, padding, out_pad, dilation = (
            self.generate_failing_case()
        )
        return (
            f"{mode} {dim} {stride} {kernel} {padding} {out_pad} {dilation}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode, dim, stride, kernel, padding, out_pad, dilation = (
            self.generate_passing_case()
        )
        return (
            f"{mode} {dim} {stride} {kernel} {padding} {out_pad} {dilation}",
            TestResult.PASSING,
        )


_KERAS20_UTILS = '''
def _t4p_deconv_length(mode, dim, stride, kernel, padding, out_pad, dilation):
    import os
    import sys
    import types
    import importlib.util
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    backend = types.ModuleType('keras.backend')
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.backend', backend)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'conv_utils.py')
    spec = importlib.util.spec_from_file_location('keras.utils.conv_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.utils.conv_utils'] = module
    spec.loader.exec_module(module)
    op = None if out_pad == 'none' else int(out_pad)
    if mode == 'dil':
        return module.deconv_length(dim, stride, kernel, padding, op, dilation)
    return module.deconv_length(dim, stride, kernel, padding, op)
'''


class Keras20UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras20TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS20_UTILS).body

    @staticmethod
    def _assert(
        mode: str, dim: int, stride: int, kernel: int, padding: str,
        out_pad: str, dilation: int,
    ) -> List[ast.stmt]:
        eff_dilation = dilation if mode == "dil" else 1
        op = None if out_pad == "none" else int(out_pad)
        expected = _fixed_deconv_length(dim, stride, kernel, padding, op, eff_dilation)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_deconv_length"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=dim),
                                ast.Constant(value=stride),
                                ast.Constant(value=kernel),
                                ast.Constant(value=padding),
                                ast.Constant(value=out_pad),
                                ast.Constant(value=dilation),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(*self.generate_passing_case())
        return test, TestResult.PASSING


grammar_20: Grammar = clean_up(
    dict(
        {
            "<start>": [
                "<mode> <number> <number> <number> <padding> <outpad> <number>"
            ],
            "<mode>": ["dil", "nodil"],
            "<padding>": ["same", "valid", "full"],
            "<outpad>": ["none", "<number>"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_20)


# ======================================================================
# bug_5: keras.utils.data_utils.get_file, when called with ``cache_dir=None``,
# hard-coded the cache directory to ``~/.keras`` and ignored the ``KERAS_HOME``
# environment variable.  The fix honours ``KERAS_HOME`` when it is set.  So a
# file that has been pre-cached under ``$KERAS_HOME/datasets`` is FOUND (no
# download) on the fixed build but MISSED on the buggy build (which looks under
# ``~/.keras`` and then tries to download).
#
# data_utils.py's only keras dependency is ``from ..utils.generic_utils import
# Progbar`` (used only for the download progress bar), so the harness injects a
# tiny ``keras.utils.generic_utils.Progbar`` stub into ``sys.modules`` and
# loads the module source directly (bypassing keras/__init__ and the TF
# backend).  No real network is used: the pre-cached file makes ``get_file``
# return without downloading, and the (unreachable) origin only matters on the
# buggy path, which fails fast with connection-refused.
#
# System-test format:  ``<mode> <fname>`` where ``<mode>`` is ``none``
#   (``cache_dir=None`` with ``KERAS_HOME`` set -> the trigger) or ``explicit``
#   (an explicit ``cache_dir``, which both builds honour).  The harness
#   pre-caches ``<fname>`` under ``$KERAS_HOME/datasets`` and prints
#   ``RESULT:OK`` iff ``get_file`` returns without error.
# ======================================================================


class Keras5API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if process.returncode == 0 and marker == "OK":
            return TestResult.PASSING, "get_file honoured the cache directory"
        return TestResult.FAILING, f"expected OK, got {marker!r}"


class Keras5TestGenerator:
    @staticmethod
    def generate_fname() -> str:
        return "t4p_" + "".join(
            random.choices(
                string.ascii_lowercase + string.digits, k=random.randint(6, 12)
            )
        )


class Keras5SystemtestGenerator(SystemtestGenerator, Keras5TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"none {self.generate_fname()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"explicit {self.generate_fname()}", TestResult.PASSING


_KERAS5_UTILS = '''
def _t4p_get_file(mode, fname):
    import os
    import sys
    import types
    import hashlib
    import tempfile
    import importlib.util
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    gu = types.ModuleType('keras.utils.generic_utils')
    class Progbar(object):
        def __init__(self, *a, **k):
            pass
        def update(self, *a, **k):
            pass
    gu.Progbar = Progbar
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'data_utils.py')
    spec = importlib.util.spec_from_file_location('keras.utils.data_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.utils.data_utils'] = module
    spec.loader.exec_module(module)
    tmp = tempfile.mkdtemp()
    os.environ['KERAS_HOME'] = tmp
    content = ('data-' + fname).encode()
    file_hash = hashlib.sha256(content).hexdigest()
    datadir = os.path.join(tmp, 'datasets')
    os.makedirs(datadir, exist_ok=True)
    with open(os.path.join(datadir, fname), 'wb') as fp:
        fp.write(content)
    origin = 'http://127.0.0.1:1/' + fname
    if mode == 'none':
        module.get_file(fname, origin=origin, cache_dir=None, file_hash=file_hash)
    else:
        module.get_file(fname, origin=origin, cache_dir=tmp, file_hash=file_hash)
    return 'OK'
'''


class Keras5UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras5TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS5_UTILS).body

    @staticmethod
    def _assert(mode: str, fname: str) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value="OK"),
                        ast.Call(
                            func=ast.Name(id="_t4p_get_file"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=fname),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("none", self.generate_fname())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("explicit", self.generate_fname())
        return test, TestResult.PASSING


grammar_5: Grammar = {
    "<start>": ["<mode> <fname>"],
    "<mode>": ["none", "explicit"],
    "<fname>": ["<char><chars>"],
    "<chars>": ["", "<char><chars>"],
    "<char>": srange(string.ascii_lowercase + string.digits + "_"),
}

assert is_valid_grammar(grammar_5)


# ======================================================================
# bug_7: keras.wrappers.scikit_learn.KerasRegressor.predict squeezed the
# model output with ``np.squeeze(self.model.predict(x))`` (no axis).  For a
# single test sample the regressor output has shape ``(1, 1)`` and the
# unrestricted squeeze collapsed it to a 0-d scalar of shape ``()`` instead
# of the expected ``(1,)``.  The fix passes ``axis=-1`` so only the trailing
# singleton is removed.  (The canonical pytest is marked FAILING because it
# needs the TensorFlow backend, which aborts on import under Rosetta; the
# code fix itself IS present on the fixed checkout, so the diversity tests
# below still distinguish buggy from fixed.)
#
# System-test format:  ``<n> <feat> <tag>`` where ``<n>`` is the number of
# test samples (the fault triggers only for ``n == 1``), ``<feat>`` the
# number of input features and ``<tag>`` an arbitrary distinctness token.
# The harness builds a KerasRegressor with a fake model returning a
# ``(n, 1)`` array (mirroring a single-output regressor) and prints
# ``RESULT:<shape>``; the oracle compares against the correct shape
# ``(n,)``.
# ======================================================================


class Keras7API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            n = int(process.args[2])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr((n,))
        marker = None
        for line in process.stdout.decode("utf8").splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if process.returncode == 0 and marker == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {marker!r}"


class Keras7TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(
            random.choices(
                string.ascii_lowercase + string.digits, k=random.randint(4, 8)
            )
        )

    @staticmethod
    def generate_feat() -> int:
        return random.randint(2, 12)


class Keras7SystemtestGenerator(SystemtestGenerator, Keras7TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"1 {self.generate_feat()} {self.generate_tag()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"{random.randint(2, 12)} {self.generate_feat()} {self.generate_tag()}",
            TestResult.PASSING,
        )


_KERAS7_UTILS = '''
def _t4p_regressor_predict_shape(n, feat):
    import importlib.util
    import inspect
    import os
    import sys
    import types
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    np_utils = types.ModuleType('keras.utils.np_utils')
    np_utils.to_categorical = lambda *a, **k: None
    gu = types.ModuleType('keras.utils.generic_utils')
    def has_arg(fn, name, accept_all=False):
        try:
            sig = inspect.signature(fn)
        except (TypeError, ValueError):
            return False
        if accept_all:
            for param in sig.parameters.values():
                if param.kind == inspect.Parameter.VAR_KEYWORD:
                    return True
        return name in sig.parameters
    gu.has_arg = has_arg
    gu.to_list = lambda x: x if isinstance(x, list) else [x]
    models = types.ModuleType('keras.models')
    class Sequential(object):
        def fit(self, x, y, **kwargs): pass
        def predict(self, x, **kwargs): pass
        def predict_classes(self, x, **kwargs): pass
        def evaluate(self, x, y, **kwargs): pass
    models.Sequential = Sequential
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.np_utils', np_utils),
                         ('keras.utils.generic_utils', gu),
                         ('keras.models', models)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'wrappers', 'scikit_learn.py')
    spec = importlib.util.spec_from_file_location('keras.wrappers.scikit_learn', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.wrappers.scikit_learn'] = module
    spec.loader.exec_module(module)
    class _FakeModel(object):
        def predict(self, x, **kwargs):
            return np.zeros((n, 1))
    reg = module.KerasRegressor(build_fn=lambda: None)
    reg.model = _FakeModel()
    x = np.zeros((n, feat))
    return tuple(reg.predict(x).shape)
'''


class Keras7UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras7TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS7_UTILS).body

    @staticmethod
    def _assert(n: int, feat: int) -> List[ast.stmt]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Tuple(elts=[ast.Constant(value=n)]),
                        ast.Call(
                            func=ast.Name(id="_t4p_regressor_predict_shape"),
                            args=[
                                ast.Constant(value=n),
                                ast.Constant(value=feat),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(1, self.generate_feat())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(random.randint(2, 12), self.generate_feat())
        return test, TestResult.PASSING


grammar_7: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <number> <tag>"],
            "<tag>": ["<char>", "<char><tag>"],
            "<char>": srange(string.ascii_lowercase + string.digits),
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_7)


# ======================================================================
# bug_9: docs/autogen.py::process_list_block sliced the current list block
# with ``docstring[starting_point:(None if ending_point == -1 else
# ending_point - 1)]``.  When the "# Arguments" list is the LAST block of the
# docstring there is no terminating ``\n\n`` (``ending_point == -1``), so the
# buggy slice runs to the END of the docstring instead of stopping at
# ``section_end``.  It therefore swallows trailing text and, because the
# over-long block no longer matches ``docstring[starting_point:section_end]``,
# the reinjection marker is never placed.  The fix uses
# ``ending_point - 1 if ending_point > -1 else section_end``.
#
# autogen.py imports keras / keras.backend / docs.structure at module level
# (which would drag in the TF backend), but ``process_list_block`` only needs
# ``re``; the harness injects tiny stubs into ``sys.modules`` and loads the
# module source directly (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <name1> <name2> ...`` where ``<mode>`` is
#   ``last`` (Arguments is the last block, no blank line -> the trigger) or
#   ``sep`` (a blank line follows -> both builds agree).  The harness builds a
#   synthetic docstring from the argument names, calls process_list_block and
#   prints ``json.dumps([docstring, block])``; the oracle recomputes the
#   correct (fixed) result and compares.
# ======================================================================


def _fixed_process_list_block(docstring, starting_point, section_end,
                              leading_spaces, marker):
    import re
    ending_point = docstring.find("\n\n", starting_point)
    block = docstring[starting_point:(ending_point - 1 if ending_point > -1
                                      else section_end)]
    docstring_slice = docstring[starting_point:section_end].replace(block, marker)
    docstring = (docstring[:starting_point]
                 + docstring_slice
                 + docstring[section_end:])
    lines = block.split("\n")
    lines = [re.sub("^" + " " * leading_spaces, "", line) for line in lines]
    top_level_regex = r"^    ([^\s\\\(]+):(.*)"
    top_level_replacement = r"- __\1__:\2"
    lines = [re.sub(top_level_regex, top_level_replacement, line) for line in lines]
    lines = [re.sub(r"^    ", "", line) for line in lines]
    indent = 0
    text_block = False
    for i in range(len(lines)):
        line = lines[i]
        spaces = re.search(r"\S", line)
        if spaces:
            if line[spaces.start()] == "-":
                indent = spaces.start() + 1
                if text_block:
                    text_block = False
                    lines[i] = "\n" + line
            elif spaces.start() < indent:
                text_block = True
                indent = spaces.start()
                lines[i] = "\n" + line
        else:
            text_block = False
            indent = 0
    block = "\n".join(lines)
    return docstring, block


def _keras9_docstring(mode, names):
    block_body = "\n".join(
        "    %s: description of %s follows" % (n, n) for n in names
    )
    section_end = len(block_body)
    if mode == "last":
        docstring = block_body + "\n    trailing text without blank line"
    else:
        docstring = block_body + "\n\n    trailing text after blank line"
    return docstring, 0, section_end, 4, "@@MARKER@@"


class Keras9API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        mode = process.args[2] if len(process.args) > 2 else None
        names = list(process.args[3:])
        if mode not in ("last", "sep") or not names:
            return TestResult.UNDEFINED, "Malformed test input"
        docstring, sp, se, ls, marker = _keras9_docstring(mode, names)
        expected = json.dumps(
            list(_fixed_process_list_block(docstring, sp, se, ls, marker))
        )
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, "process_list_block matched fixed output"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Keras9TestGenerator:
    @staticmethod
    def generate_name() -> str:
        return "".join(
            random.choices(string.ascii_lowercase, k=random.randint(3, 8))
        )

    def generate_names(self) -> List[str]:
        return [self.generate_name() for _ in range(random.randint(2, 5))]


class Keras9SystemtestGenerator(SystemtestGenerator, Keras9TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return "last " + " ".join(self.generate_names()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return "sep " + " ".join(self.generate_names()), TestResult.PASSING


_KERAS9_UTILS = '''
def _t4p_process_list_block(mode, names):
    import os
    import sys
    import types
    import json
    import importlib.util
    for name in ['keras', 'keras.backend', 'keras.backend.numpy_backend',
                 'docs', 'docs.structure']:
        m = types.ModuleType(name)
        if name in ('keras', 'docs'):
            m.__path__ = []
        sys.modules[name] = m
    ds = sys.modules['docs.structure']
    for a in ['EXCLUDE', 'PAGES', 'ROOT', 'template_np_implementation',
              'template_hidden_np_implementation']:
        setattr(ds, a, None)
    sys.modules['keras.backend'].numpy_backend = sys.modules['keras.backend.numpy_backend']
    path = os.path.join(os.getcwd(), 'docs', 'autogen.py')
    spec = importlib.util.spec_from_file_location('docs.autogen', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['docs.autogen'] = module
    spec.loader.exec_module(module)
    block_body = "\\n".join("    %s: description of %s follows" % (n, n) for n in names)
    section_end = len(block_body)
    if mode == 'last':
        docstring = block_body + "\\n    trailing text without blank line"
    else:
        docstring = block_body + "\\n\\n    trailing text after blank line"
    result = module.process_list_block(docstring, 0, section_end, 4, '@@MARKER@@')
    return json.dumps(list(result))
'''


class Keras9UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras9TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS9_UTILS).body

    @staticmethod
    def _assert(mode: str, names: List[str]) -> List[ast.stmt]:
        docstring, sp, se, ls, marker = _keras9_docstring(mode, names)
        expected = json.dumps(
            list(_fixed_process_list_block(docstring, sp, se, ls, marker))
        )
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_process_list_block"),
                            args=[
                                ast.Constant(value=mode),
                                ast.List(
                                    elts=[ast.Constant(value=n) for n in names]
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("last", self.generate_names())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("sep", self.generate_names())
        return test, TestResult.PASSING


grammar_9: Grammar = clean_up(
    {
        "<start>": ["<mode> <names>"],
        "<mode>": ["last", "sep"],
        "<names>": ["<name>", "<name> <names>"],
        "<name>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_9)


# ======================================================================
# bug_2: keras.backend.numpy_backend was missing the ``in_top_k`` reference
# implementation entirely.  The fix ADDS
#   def in_top_k(predictions, targets, k):
#       top_k = np.argsort(-predictions)[:, :k]
#       targets = targets.reshape(-1, 1)
#       return np.any(targets == top_k, axis=-1)
# On the buggy build ``numpy_backend.in_top_k`` does not exist, so calling it
# raises ``AttributeError``.
#
# numpy_backend.py depends on numpy / scipy (both in the build venv) plus a few
# keras helpers (``.common.floatx``, ``keras.utils.to_categorical``,
# ``keras.utils.generic_utils.transpose_shape``) that ``in_top_k`` never uses;
# the harness injects tiny stubs into ``sys.modules`` and loads the module
# source directly (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <seed> <n> <c> <k>`` where ``<mode>`` is
#   ``topk`` (call in_top_k -> the trigger) or ``greater`` (call the existing
#   elementwise ``greater``, which both builds have).  Arrays are built
#   deterministically from ``<seed>`` with numpy's legacy ``RandomState`` (which
#   is stable across numpy versions), so the oracle recomputes the correct
#   (fixed) boolean result and compares.  All outputs are 0/1 strings (exact,
#   no float fragility).
# ======================================================================


def _keras2_topk_build(seed, n, c):
    import numpy as np
    rng = np.random.RandomState(seed)
    preds = np.stack([rng.permutation(c) for _ in range(n)]).astype("float32")
    targets = rng.randint(0, c, size=n)
    return preds, targets


def _keras2_expected_topk(seed, n, c, k):
    import numpy as np
    preds, targets = _keras2_topk_build(seed, n, c)
    top_k = np.argsort(-preds)[:, :k]
    r = np.any(targets.reshape(-1, 1) == top_k, axis=-1)
    return "".join("1" if b else "0" for b in r.astype(bool).ravel())


def _keras2_greater_build(seed, n):
    import numpy as np
    rng = np.random.RandomState(seed)
    a = rng.randint(0, 100, size=n)
    b = rng.randint(0, 100, size=n)
    return a, b


def _keras2_expected_greater(seed, n):
    import numpy as np
    a, b = _keras2_greater_build(seed, n)
    r = a > b
    return "".join("1" if x else "0" for x in r.astype(bool).ravel())


class Keras2API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            seed = int(process.args[3])
            n = int(process.args[4])
            c = int(process.args[5])
            k = int(process.args[6])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "topk":
            expected = _keras2_expected_topk(seed, n, c, k)
        elif mode == "greater":
            expected = _keras2_expected_greater(seed, n)
        else:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras2TestGenerator:
    @staticmethod
    def generate_failing_case() -> Tuple[int, int, int, int]:
        seed = random.randint(0, 9999)
        n = random.randint(3, 8)
        c = random.randint(3, 8)
        k = random.randint(1, c - 1)
        return seed, n, c, k

    @staticmethod
    def generate_passing_case() -> Tuple[int, int, int, int]:
        seed = random.randint(0, 9999)
        n = random.randint(3, 8)
        c = random.randint(3, 8)
        k = random.randint(1, c - 1)
        return seed, n, c, k


class Keras2SystemtestGenerator(SystemtestGenerator, Keras2TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        seed, n, c, k = self.generate_failing_case()
        return f"topk {seed} {n} {c} {k}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        seed, n, c, k = self.generate_passing_case()
        return f"greater {seed} {n} {c} {k}", TestResult.PASSING


_KERAS2_UTILS = '''
def _t4p_numpy_backend(mode, seed, n, c, k):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend'); backend.__path__ = []
    common = types.ModuleType('keras.backend.common')
    common.floatx = lambda: 'float32'
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    utils.to_categorical = lambda *a, **k: None
    gu = types.ModuleType('keras.utils.generic_utils')
    gu.transpose_shape = lambda *a, **k: None
    for name, module in [('keras', keras), ('keras.backend', backend),
                         ('keras.backend.common', common), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'backend', 'numpy_backend.py')
    spec = importlib.util.spec_from_file_location('keras.backend.numpy_backend', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.backend.numpy_backend'] = module
    spec.loader.exec_module(module)
    if mode == 'topk':
        rng = np.random.RandomState(seed)
        preds = np.stack([rng.permutation(c) for _ in range(n)]).astype('float32')
        targets = rng.randint(0, c, size=n)
        r = np.asarray(module.in_top_k(preds, targets, k))
    else:
        rng = np.random.RandomState(seed)
        a = rng.randint(0, 100, size=n)
        b = rng.randint(0, 100, size=n)
        r = np.asarray(module.greater(a, b))
    return "".join('1' if x else '0' for x in r.astype(bool).ravel())
'''


class Keras2UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras2TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS2_UTILS).body

    @staticmethod
    def _assert(mode: str, seed: int, n: int, c: int, k: int) -> List[ast.stmt]:
        if mode == "topk":
            expected = _keras2_expected_topk(seed, n, c, k)
        else:
            expected = _keras2_expected_greater(seed, n)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_numpy_backend"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=seed),
                                ast.Constant(value=n),
                                ast.Constant(value=c),
                                ast.Constant(value=k),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("topk", *self.generate_failing_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("greater", *self.generate_passing_case())
        return test, TestResult.PASSING


grammar_2: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number>"],
            "<mode>": ["topk", "greater"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_2)


# ======================================================================
# bug_10: keras.engine.training_utils.standardize_weights ignored
# ``class_weight`` whenever ``sample_weight`` was also provided -- it emitted a
# warning and returned ``sample_weight`` alone.  The fix combines them
# (``return sample_weight * class_sample_weight``) so both contributions are
# applied.
#
# training_utils.py imports the TF backend / losses at module level, but
# ``standardize_weights`` only uses numpy + warnings; the harness injects tiny
# stubs (keras.backend, keras.losses, keras.utils.Sequence,
# keras.utils.generic_utils.to_list) into ``sys.modules`` and loads the module
# source directly (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <seed> <n> <C>`` where ``<mode>`` is ``both``
#   (pass both sample_weight and class_weight -> the trigger) or ``onlysw``
#   (only sample_weight, which both builds treat identically).  Arrays are
#   built deterministically from ``<seed>`` (numpy legacy RandomState); the
#   oracle recomputes the correct (fixed) integer weight vector and compares.
# ======================================================================


def _keras10_build(seed, n, C):
    import numpy as np
    rng = np.random.RandomState(seed)
    y = rng.randint(0, C, size=n)
    sw = rng.randint(1, 6, size=n)
    cw = {c: int(rng.randint(2, 6)) for c in range(C)}
    return y, sw, cw


def _keras10_expected(mode, seed, n, C):
    import numpy as np
    y, sw, cw = _keras10_build(seed, n, C)
    if mode == "both":
        r = sw * np.asarray([cw[c] for c in y])
    else:
        r = sw
    return ",".join(str(int(v)) for v in np.asarray(r).ravel())


class Keras10API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            seed = int(process.args[3])
            n = int(process.args[4])
            C = int(process.args[5])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode not in ("both", "onlysw"):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _keras10_expected(mode, seed, n, C)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras10TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int]:
        return random.randint(0, 9999), random.randint(3, 8), random.randint(2, 5)


class Keras10SystemtestGenerator(SystemtestGenerator, Keras10TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        seed, n, C = self.generate_case()
        return f"both {seed} {n} {C}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        seed, n, C = self.generate_case()
        return f"onlysw {seed} {n} {C}", TestResult.PASSING


_KERAS10_UTILS = '''
def _t4p_standardize_weights(mode, seed, n, C):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend')
    for a in ['is_tensor', 'int_shape', 'floatx']:
        setattr(backend, a, lambda *x, **k: None)
    losses = types.ModuleType('keras.losses')
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    class Sequence(object):
        pass
    utils.Sequence = Sequence
    gu = types.ModuleType('keras.utils.generic_utils')
    gu.to_list = lambda x: x if isinstance(x, list) else [x]
    for name, module in [('keras', keras), ('keras.backend', backend),
                         ('keras.losses', losses), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'engine', 'training_utils.py')
    spec = importlib.util.spec_from_file_location('keras.engine.training_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.engine.training_utils'] = module
    spec.loader.exec_module(module)
    rng = np.random.RandomState(seed)
    y = rng.randint(0, C, size=n)
    sw = rng.randint(1, 6, size=n)
    cw = {c: int(rng.randint(2, 6)) for c in range(C)}
    if mode == 'both':
        r = module.standardize_weights(y, sample_weight=sw, class_weight=cw)
    else:
        r = module.standardize_weights(y, sample_weight=sw, class_weight=None)
    return ",".join(str(int(v)) for v in np.asarray(r).ravel())
'''


class Keras10UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras10TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS10_UTILS).body

    @staticmethod
    def _assert(mode: str, seed: int, n: int, C: int) -> List[ast.stmt]:
        expected = _keras10_expected(mode, seed, n, C)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_standardize_weights"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=seed),
                                ast.Constant(value=n),
                                ast.Constant(value=C),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("both", *self.generate_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("onlysw", *self.generate_case())
        return test, TestResult.PASSING


grammar_10: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["both", "onlysw"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_10)


# ======================================================================
# bug_35: keras.preprocessing.image.ImageDataGenerator.standardize applied the
# user ``preprocessing_function`` at the START of standardization (before
# rescale / centering).  The fix REMOVES that call from ``standardize`` (the
# preprocessing function is instead applied by the iterators, before the random
# transform).  So on the buggy build ``standardize`` runs the preprocessing
# function, on the fixed build it does not.
#
# image.py imports the TF backend / scipy / PIL at module level, but the
# ``standardize`` path (with only ``preprocessing_function`` + ``rescale`` set)
# needs numpy only; the harness injects tiny stubs (keras.backend,
# keras.utils.data_utils.Sequence) into ``sys.modules`` and loads the module
# source directly (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <seed> <n> <mult> <rescale>`` where ``<mode>``
#   is ``pf`` (a preprocessing_function that multiplies by ``mult`` is set ->
#   the trigger) or ``nopf`` (no preprocessing_function).  The oracle recomputes
#   the correct (fixed) result ``x * rescale`` (integer, exact) and compares.
# ======================================================================


def _keras35_expected(seed, n, mult, rescale):
    import numpy as np
    rng = np.random.RandomState(seed)
    x = rng.randint(0, 10, size=(n, 2, 2, 3)).astype("int64")
    r = x * rescale
    return ",".join(str(int(v)) for v in r.ravel())


class Keras35API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            seed = int(process.args[3])
            n = int(process.args[4])
            mult = int(process.args[5])
            rescale = int(process.args[6])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode not in ("pf", "nopf"):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _keras35_expected(seed, n, mult, rescale)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras35TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int, int]:
        seed = random.randint(0, 9999)
        n = random.randint(1, 3)
        mult = random.randint(2, 5)
        rescale = random.randint(2, 4)
        return seed, n, mult, rescale


class Keras35SystemtestGenerator(SystemtestGenerator, Keras35TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        seed, n, mult, rescale = self.generate_case()
        return f"pf {seed} {n} {mult} {rescale}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        seed, n, mult, rescale = self.generate_case()
        return f"nopf {seed} {n} {mult} {rescale}", TestResult.PASSING


_KERAS35_UTILS = '''
def _t4p_standardize(mode, seed, n, mult, rescale):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend')
    backend.image_data_format = lambda: 'channels_last'
    backend.floatx = lambda: 'float32'
    backend.epsilon = lambda: 1e-7
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    du = types.ModuleType('keras.utils.data_utils')
    class Sequence(object):
        pass
    du.Sequence = Sequence
    for name, module in [('keras', keras), ('keras.backend', backend),
                         ('keras.utils', utils), ('keras.utils.data_utils', du)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'preprocessing', 'image.py')
    spec = importlib.util.spec_from_file_location('keras.preprocessing.image', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.preprocessing.image'] = module
    spec.loader.exec_module(module)
    rng = np.random.RandomState(seed)
    x = rng.randint(0, 10, size=(n, 2, 2, 3)).astype('int64')
    if mode == 'pf':
        idg = module.ImageDataGenerator(
            preprocessing_function=lambda a: a * mult, rescale=rescale,
            data_format='channels_last')
    else:
        idg = module.ImageDataGenerator(
            preprocessing_function=None, rescale=rescale,
            data_format='channels_last')
    out = np.asarray(idg.standardize(x))
    return ",".join(str(int(v)) for v in out.ravel())
'''


class Keras35UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras35TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS35_UTILS).body

    @staticmethod
    def _assert(mode: str, seed: int, n: int, mult: int, rescale: int) -> List[ast.stmt]:
        expected = _keras35_expected(seed, n, mult, rescale)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_standardize"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=seed),
                                ast.Constant(value=n),
                                ast.Constant(value=mult),
                                ast.Constant(value=rescale),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("pf", *self.generate_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("nopf", *self.generate_case())
        return test, TestResult.PASSING


grammar_35: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number> <number>"],
            "<mode>": ["pf", "nopf"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_35)


# ======================================================================
# bug_32: keras.callbacks.ReduceLROnPlateau.on_epoch_end incremented
# ``self.wait`` AFTER the ``if self.wait >= self.patience`` check, so it took
# ``patience + 1`` non-improving epochs to reduce the learning rate instead of
# ``patience``.  The fix moves ``self.wait += 1`` before the check.
#
# callbacks.py imports the TF backend / Progbar / engine.topology at module
# level, but ReduceLROnPlateau only needs numpy + a couple of ``K.get_value`` /
# ``K.set_value`` hooks on the optimizer's lr; the harness injects tiny stubs
# into ``sys.modules`` (with a plain-dict lr variable) and loads the module
# source directly (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <lr0_pow> <patience>`` where ``<mode>`` is
#   ``reduce`` (run ``patience + 1`` epochs of a constant, non-improving metric
#   -> fixed reduces the lr, buggy does not: the trigger) or ``noreduce`` (run
#   ``patience`` epochs -> neither reduces).  ``lr0 = 2 ** lr0_pow``,
#   ``factor = 0.5``.  The oracle recomputes the correct (fixed) final lr and
#   compares (values are exact powers of two).
# ======================================================================


def _keras32_fixed_final_lr(lr0, factor, patience, epochs, V):
    epsilon = 1e-4
    best = float("inf")
    wait = 0
    cooldown_counter = 0
    cooldown = 0
    min_lr = 0.0
    lr = float(lr0)
    for _ in range(epochs):
        current = V
        if cooldown_counter > 0:
            cooldown_counter -= 1
            wait = 0
        if current < best - epsilon:
            best = current
            wait = 0
        elif not (cooldown_counter > 0):
            wait += 1
            if wait >= patience:
                if lr > min_lr:
                    lr = float(max(lr * factor, min_lr))
                cooldown_counter = cooldown
                wait = 0
    return lr


class Keras32API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            lr0_pow = int(process.args[3])
            patience = int(process.args[4])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode not in ("reduce", "noreduce"):
            return TestResult.UNDEFINED, "Malformed test input"
        lr0 = 2.0 ** lr0_pow
        epochs = patience + 1 if mode == "reduce" else patience
        expected = repr(_keras32_fixed_final_lr(lr0, 0.5, patience, epochs, 0.5))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras32TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int]:
        return random.randint(1, 6), random.randint(1, 6)


class Keras32SystemtestGenerator(SystemtestGenerator, Keras32TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        lr0_pow, patience = self.generate_case()
        return f"reduce {lr0_pow} {patience}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        lr0_pow, patience = self.generate_case()
        return f"noreduce {lr0_pow} {patience}", TestResult.PASSING


_KERAS32_UTILS = '''
def _t4p_reduce_lr(mode, lr0_pow, patience):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    gu = types.ModuleType('keras.utils.generic_utils')
    class Progbar(object):
        def __init__(self, *a, **k):
            pass
        def update(self, *a, **k):
            pass
    gu.Progbar = Progbar
    backend = types.ModuleType('keras.backend')
    backend.get_value = lambda var: var['v']
    backend.set_value = lambda var, val: var.__setitem__('v', val)
    backend.epsilon = lambda: 1e-7
    engine = types.ModuleType('keras.engine'); engine.__path__ = []
    topo = types.ModuleType('keras.engine.topology')
    class Layer(object):
        pass
    topo.Layer = Layer
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu), ('keras.backend', backend),
                         ('keras.engine', engine), ('keras.engine.topology', topo)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'callbacks.py')
    spec = importlib.util.spec_from_file_location('keras.callbacks', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.callbacks'] = module
    spec.loader.exec_module(module)
    lr0 = 2.0 ** lr0_pow
    epochs = patience + 1 if mode == 'reduce' else patience

    class Opt(object):
        def __init__(self, lr):
            self.lr = {'v': lr}

    class Model(object):
        def __init__(self, lr):
            self.optimizer = Opt(lr)

    model = Model(lr0)
    cb = module.ReduceLROnPlateau(monitor='loss', factor=0.5, patience=patience,
                                  cooldown=0, min_lr=0)
    cb.model = model
    cb.on_train_begin()
    for e in range(epochs):
        cb.on_epoch_end(e, {'loss': 0.5})
    return repr(float(model.optimizer.lr['v']))
'''


class Keras32UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras32TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS32_UTILS).body

    @staticmethod
    def _assert(mode: str, lr0_pow: int, patience: int) -> List[ast.stmt]:
        lr0 = 2.0 ** lr0_pow
        epochs = patience + 1 if mode == "reduce" else patience
        expected = repr(_keras32_fixed_final_lr(lr0, 0.5, patience, epochs, 0.5))
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_reduce_lr"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=lr0_pow),
                                ast.Constant(value=patience),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("reduce", *self.generate_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("noreduce", *self.generate_case())
        return test, TestResult.PASSING


grammar_32: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number>"],
            "<mode>": ["reduce", "noreduce"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_32)


# ======================================================================
# bug_21: keras.callbacks.EarlyStopping had no ``restore_best_weights`` option.
# The fix adds the ``restore_best_weights`` constructor argument, snapshots the
# best weights on each improvement, and restores them when training stops.  On
# the buggy build ``EarlyStopping(restore_best_weights=True)`` raises
# ``TypeError`` (unexpected keyword argument); even setting it aside, the buggy
# callback never restores the best weights.
#
# callbacks.py imports the TF backend / Progbar / engine.topology at module
# level, but EarlyStopping only needs numpy + ``model.get_weights`` /
# ``model.set_weights`` / ``model.stop_training``; the harness injects tiny
# stubs into ``sys.modules`` and loads the module source directly (bypassing
# keras/__init__ and the TF backend), driving a fake model whose single
# "weight" is an integer we control per epoch.
#
# System-test format:  ``<mode> <base> <patience>`` where ``<mode>`` is
#   ``restore`` (construct with restore_best_weights=True -> the trigger) or
#   ``default`` (no restore kwarg).  The metric improves (epoch 1 is best) then
#   plateaus for ``patience`` epochs to trigger early stopping; the fake model's
#   weight at epoch e is ``base + e``.  The oracle expects the fixed final
#   weight: ``base + 1`` (best, restored) for ``restore`` and
#   ``base + patience + 1`` (last) for ``default``.
# ======================================================================


class Keras21API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            base = int(process.args[3])
            patience = int(process.args[4])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "restore":
            expected = str(base + 1)
        elif mode == "default":
            expected = str(base + patience + 1)
        else:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras21TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int]:
        return random.randint(100, 900), random.randint(1, 5)


class Keras21SystemtestGenerator(SystemtestGenerator, Keras21TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        base, patience = self.generate_case()
        return f"restore {base} {patience}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        base, patience = self.generate_case()
        return f"default {base} {patience}", TestResult.PASSING


_KERAS21_UTILS = '''
def _t4p_early_stopping(mode, base, patience):
    import os
    import sys
    import types
    import importlib.util
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    gu = types.ModuleType('keras.utils.generic_utils')
    class Progbar(object):
        def __init__(self, *a, **k):
            pass
        def update(self, *a, **k):
            pass
    gu.Progbar = Progbar
    backend = types.ModuleType('keras.backend')
    backend.epsilon = lambda: 1e-7
    engine = types.ModuleType('keras.engine'); engine.__path__ = []
    tu = types.ModuleType('keras.engine.training_utils')
    tu.standardize_input_data = lambda *a, **k: None
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu), ('keras.backend', backend),
                         ('keras.engine', engine),
                         ('keras.engine.training_utils', tu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'callbacks.py')
    spec = importlib.util.spec_from_file_location('keras.callbacks', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.callbacks'] = module
    spec.loader.exec_module(module)

    class Model(object):
        def __init__(self):
            self.w = None
            self.stop_training = False
        def get_weights(self):
            return [self.w]
        def set_weights(self, ws):
            self.w = ws[0]

    model = Model()
    if mode == 'restore':
        cb = module.EarlyStopping(monitor='loss', patience=patience,
                                  restore_best_weights=True)
    else:
        cb = module.EarlyStopping(monitor='loss', patience=patience)
    cb.model = model
    cb.on_train_begin()
    losses = [10.0, 5.0] + [8.0] * patience
    for e, loss in enumerate(losses):
        model.w = base + e
        cb.on_epoch_end(e, {'loss': loss})
        if model.stop_training:
            break
    return str(model.w)
'''


class Keras21UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras21TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS21_UTILS).body

    @staticmethod
    def _assert(mode: str, base: int, patience: int) -> List[ast.stmt]:
        if mode == "restore":
            expected = str(base + 1)
        else:
            expected = str(base + patience + 1)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_early_stopping"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=base),
                                ast.Constant(value=patience),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("restore", *self.generate_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("default", *self.generate_case())
        return test, TestResult.PASSING


grammar_21: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number>"],
            "<mode>": ["restore", "default"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_21)


# ======================================================================
# bug_6: keras.engine.training_utils.weighted_masked_objective divided the
# masked score array by ``K.mean(mask)`` without guarding against an all-zero
# mask.  When every timestep/sample is masked out, ``K.mean(mask) == 0`` so the
# division yields NaN.  The fix divides by ``K.mean(mask) + K.epsilon()``.
#
# training_utils.py imports the TF backend / losses at module level, but the
# ``weighted`` closure only needs a handful of backend ops (cast/floatx/mean/
# ndim/not_equal/epsilon) that are trivially backed by numpy; the harness
# injects tiny stubs into ``sys.modules`` and loads the module source directly
# (bypassing keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <seed> <n> <m>`` where ``<mode>`` is ``mask0``
#   (an all-zero mask -> the trigger: buggy returns NaN, fixed returns 0.0) or
#   ``nomask`` (mask=None, so the masking branch is skipped and both builds
#   agree).  ``y_true`` / ``y_pred`` are float arrays built from ``<seed>``; the
#   oracle recomputes the correct (fixed) scalar and compares.
# ======================================================================


def _keras6_expected(mode, seed, n, m):
    import numpy as np
    if mode == "mask0":
        return "0.0"
    rng = np.random.RandomState(seed)
    yt = rng.randint(0, 10, size=(n, m)).astype("float64")
    yp = rng.randint(0, 10, size=(n, m)).astype("float64")
    return repr(float(np.mean((yp - yt) ** 2)))


class Keras6API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            seed = int(process.args[3])
            n = int(process.args[4])
            m = int(process.args[5])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode not in ("mask0", "nomask"):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _keras6_expected(mode, seed, n, m)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras6TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int, int]:
        return random.randint(0, 9999), random.randint(2, 5), random.randint(2, 5)


class Keras6SystemtestGenerator(SystemtestGenerator, Keras6TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        seed, n, m = self.generate_case()
        return f"mask0 {seed} {n} {m}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        seed, n, m = self.generate_case()
        return f"nomask {seed} {n} {m}", TestResult.PASSING


_KERAS6_UTILS = '''
def _t4p_weighted_masked(mode, seed, n, m):
    import os
    import sys
    import types
    import warnings
    import importlib.util
    import numpy as np
    warnings.filterwarnings('ignore')
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend')
    backend.floatx = lambda: 'float32'
    backend.epsilon = lambda: 1e-7
    backend.cast = lambda x, dtype: np.asarray(x).astype(dtype)
    backend.mean = lambda x, axis=None: np.mean(x, axis=axis)
    backend.ndim = lambda x: np.asarray(x).ndim
    backend.not_equal = lambda x, y: np.asarray(x) != y
    backend.is_tensor = lambda x: False
    backend.int_shape = lambda x: None
    losses = types.ModuleType('keras.losses')
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    class Sequence(object):
        pass
    utils.Sequence = Sequence
    gu = types.ModuleType('keras.utils.generic_utils')
    gu.to_list = lambda x: x if isinstance(x, list) else [x]
    for name, module in [('keras', keras), ('keras.backend', backend),
                         ('keras.losses', losses), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'engine', 'training_utils.py')
    spec = importlib.util.spec_from_file_location('keras.engine.training_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.engine.training_utils'] = module
    spec.loader.exec_module(module)
    fn = lambda yt, yp: (yp - yt) ** 2
    weighted = module.weighted_masked_objective(fn)
    rng = np.random.RandomState(seed)
    yt = rng.randint(0, 10, size=(n, m)).astype('float64')
    yp = rng.randint(0, 10, size=(n, m)).astype('float64')
    if mode == 'mask0':
        mask = np.zeros((n, m))
        res = weighted(yt, yp, None, mask)
    else:
        res = weighted(yt, yp, None, None)
    return repr(float(res))
'''


class Keras6UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras6TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS6_UTILS).body

    @staticmethod
    def _assert(mode: str, seed: int, n: int, m: int) -> List[ast.stmt]:
        expected = _keras6_expected(mode, seed, n, m)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_weighted_masked"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=seed),
                                ast.Constant(value=n),
                                ast.Constant(value=m),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("mask0", *self.generate_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("nomask", *self.generate_case())
        return test, TestResult.PASSING


grammar_6: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["mask0", "nomask"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_6)


# ======================================================================
# bug_14: keras.metrics.sparse_top_k_categorical_accuracy collapsed the true
# labels with ``K.max(y_true, axis=-1)`` before the top-k check.  For a 1-D
# ``y_true`` of shape ``(num_samples,)`` this reduces every label to the single
# GLOBAL maximum, so every sample is scored against the same class.  The fix
# uses ``K.flatten(y_true)`` to keep the per-sample labels.
#
# metrics.py imports the TF backend / losses / utils at module level, but
# ``sparse_top_k_categorical_accuracy`` only needs a handful of numpy-backed
# backend ops (mean/cast/max/flatten/in_top_k); the harness injects tiny stubs
# into ``sys.modules`` and loads the module source directly (bypassing
# keras/__init__ and the TF backend).
#
# System-test format:  ``<mode> <seed> <N>`` where ``<mode>`` is ``flat``
#   (1-D y_true -> the trigger: buggy scores every sample against the global max
#   class, giving accuracy 1/N; fixed gives 1.0) or ``col`` (2-D y_true of shape
#   (N, 1) -> ``K.max(axis=-1)`` equals the per-sample label, so both agree).
#   ``y_pred[i]`` is a one-hot whose argmax is the i-th label, so the correct
#   (fixed) top-1 accuracy is always 1.0.
# ======================================================================


class Keras14API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            int(process.args[3])
            n = int(process.args[4])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode not in ("flat", "col") or n < 2:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = repr(1.0)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Keras14TestGenerator:
    @staticmethod
    def generate_case() -> Tuple[int, int]:
        return random.randint(0, 9999), random.randint(2, 8)


class Keras14SystemtestGenerator(SystemtestGenerator, Keras14TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        seed, n = self.generate_case()
        return f"flat {seed} {n}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        seed, n = self.generate_case()
        return f"col {seed} {n}", TestResult.PASSING


_KERAS14_UTILS = '''
def _t4p_sparse_top_k(mode, seed, n):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    K = types.ModuleType('keras.backend')
    K.mean = lambda x, axis=None: np.mean(x, axis=axis)
    K.cast = lambda x, dtype: np.asarray(x).astype('int32' if dtype == 'int32' else dtype)
    K.max = lambda x, axis=None: np.max(x, axis=axis)
    K.flatten = lambda x: np.asarray(x).flatten()
    def in_top_k(preds, targets, k):
        top_k = np.argsort(-np.asarray(preds))[:, :k]
        t = np.asarray(targets).reshape(-1, 1)
        return np.any(t == top_k, axis=-1)
    K.in_top_k = in_top_k
    losses = types.ModuleType('keras.losses')
    losses.__getattr__ = lambda name: (lambda *a, **k: None)
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    gu = types.ModuleType('keras.utils.generic_utils')
    gu.__getattr__ = lambda name: (lambda *a, **k: None)
    for name, module in [('keras', keras), ('keras.backend', K),
                         ('keras.losses', losses), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'metrics.py')
    spec = importlib.util.spec_from_file_location('keras.metrics', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.metrics'] = module
    spec.loader.exec_module(module)
    perm = np.random.RandomState(seed).permutation(n)
    ypred = np.eye(n)[perm]
    if mode == 'flat':
        y_true = perm
    else:
        y_true = perm.reshape(-1, 1)
    res = module.sparse_top_k_categorical_accuracy(y_true, ypred, 1)
    return repr(float(np.asarray(res)))
'''


class Keras14UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras14TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS14_UTILS).body

    @staticmethod
    def _assert(mode: str, seed: int, n: int) -> List[ast.stmt]:
        expected = repr(1.0)
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_sparse_top_k"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=seed),
                                ast.Constant(value=n),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("flat", *self.generate_case())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("col", *self.generate_case())
        return test, TestResult.PASSING


grammar_14: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number>"],
            "<mode>": ["flat", "col"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_14)


# ======================================================================
# bug_41: keras.utils.data_utils.GeneratorEnqueuer swallowed exceptions raised
# by the wrapped generator.  When the generator raised (e.g. IndexError), the
# buggy worker only re-raised inside its own thread and set the stop event, so
# the consumer side (``get()``) simply ran dry and the caller saw a
# ``StopIteration`` instead of the real error.  The fix pushes ``(False, exc)``
# onto the queue and re-raises the exception in the consumer.
#
# data_utils.py's only keras dependency is ``from ..utils.generic_utils import
# Progbar`` (used only for download progress), so the harness injects a tiny
# Progbar stub into ``sys.modules`` and loads the module source directly
# (bypassing keras/__init__ and the TF backend), then drives a thread-based
# GeneratorEnqueuer.
#
# System-test format:  ``<mode> <val>`` where ``<mode>`` is ``fault`` (the
#   wrapped generator raises IndexError -> the trigger: buggy yields
#   StopIteration, fixed re-raises IndexError) or ``good`` (the generator yields
#   ``val``).  The harness prints ``RESULT:IndexError`` / ``RESULT:<other>`` /
#   ``RESULT:OK``; the oracle expects the correct (fixed) behaviour:
#   ``IndexError`` for ``fault`` and ``OK`` for ``good``.
# ======================================================================


class Keras41API(KerasAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "fault":
            expected = "IndexError"
        elif mode == "good":
            expected = "OK"
        else:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8")
        marker = None
        for line in out.splitlines():
            if line.startswith("RESULT:"):
                marker = line[len("RESULT:"):].strip()
        if process.returncode == 0 and marker == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {marker!r}"


class Keras41TestGenerator:
    @staticmethod
    def generate_val() -> int:
        return random.randint(1, 99999)


class Keras41SystemtestGenerator(SystemtestGenerator, Keras41TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"fault {self.generate_val()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"good {self.generate_val()}", TestResult.PASSING


_KERAS41_UTILS = '''
def _t4p_generator_enqueuer(mode, val):
    import os
    import sys
    import types
    import signal
    import importlib.util
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    gu = types.ModuleType('keras.utils.generic_utils')
    class Progbar(object):
        def __init__(self, *a, **k):
            pass
        def update(self, *a, **k):
            pass
    gu.Progbar = Progbar
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'data_utils.py')
    spec = importlib.util.spec_from_file_location('keras.utils.data_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.utils.data_utils'] = module
    spec.loader.exec_module(module)

    def faulty():
        raise IndexError('t4p fault %d' % val)
        yield val

    def good():
        while True:
            yield val

    try:
        signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
        signal.alarm(15)
    except Exception:
        pass
    gen = faulty() if mode == 'fault' else good()
    enq = module.GeneratorEnqueuer(gen, use_multiprocessing=False)
    enq.start(1, 10)
    out = enq.get()
    try:
        next(out)
        result = 'OK'
    except IndexError:
        result = 'IndexError'
    except BaseException as e:
        result = type(e).__name__
    try:
        enq.stop()
    except Exception:
        pass
    try:
        signal.alarm(0)
    except Exception:
        pass
    return result
'''


class Keras41UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Keras41TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(_KERAS41_UTILS).body

    @staticmethod
    def _assert(mode: str, val: int) -> List[ast.stmt]:
        expected = "IndexError" if mode == "fault" else "OK"
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self"), attr="assertEqual"
                    ),
                    args=[
                        ast.Constant(value=expected),
                        ast.Call(
                            func=ast.Name(id="_t4p_generator_enqueuer"),
                            args=[
                                ast.Constant(value=mode),
                                ast.Constant(value=val),
                            ],
                            keywords=[],
                        ),
                    ],
                    keywords=[],
                )
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("fault", self.generate_val())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("good", self.generate_val())
        return test, TestResult.PASSING


grammar_41: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number>"],
            "<mode>": ["fault", "good"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_41)
