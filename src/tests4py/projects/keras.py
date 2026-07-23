import ast
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
