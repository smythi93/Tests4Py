import os
import ast
import os.path
import random
import string
import subprocess
from _ast import Call, ImportFrom
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable
from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.grammars.fuzzer import srange
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
            grammar=None,
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
        api=KerasAPI1(),
        unittests=KerasUnittestGenerator1(),
        systemtests=KerasSystemtestGenerator1(),
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
        api=KerasAPI2(),
        unittests=KerasUnittestGenerator2(),
        systemtests=KerasSystemtestGenerator2(),
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
        api=KerasAPI3(),
        unittests=KerasUnittestGenerator3(),
        systemtests=KerasSystemtestGenerator3(),
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
        api=KerasAPI4(),
        unittests=KerasUnittestGenerator4(),
        systemtests=KerasSystemtestGenerator4(),
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
        api=KerasAPI5(),
        unittests=KerasUnittestGenerator5(),
        systemtests=KerasSystemtestGenerator5(),
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
        api=KerasAPI6(),
        unittests=KerasUnittestGenerator6(),
        systemtests=KerasSystemtestGenerator6(),
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
        api=KerasAPI7(),
        unittests=KerasUnittestGenerator7(),
        systemtests=KerasSystemtestGenerator7(),
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
        api=KerasAPI8(),
        unittests=KerasUnittestGenerator8(),
        systemtests=KerasSystemtestGenerator8(),
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
        api=KerasAPI9(),
        unittests=KerasUnittestGenerator9(),
        systemtests=KerasSystemtestGenerator9(),
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
        api=KerasAPI10(),
        unittests=KerasUnittestGenerator10(),
        systemtests=KerasSystemtestGenerator10(),
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
        api=KerasAPI11(),
        unittests=KerasUnittestGenerator11(),
        systemtests=KerasSystemtestGenerator11(),
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
        api=KerasAPI12(),
        unittests=KerasUnittestGenerator12(),
        systemtests=KerasSystemtestGenerator12(),
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
        api=KerasAPI13(),
        unittests=KerasUnittestGenerator13(),
        systemtests=KerasSystemtestGenerator13(),
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
        api=KerasAPI14(),
        unittests=KerasUnittestGenerator14(),
        systemtests=KerasSystemtestGenerator14(),
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
        api=KerasAPI15(),
        unittests=KerasUnittestGenerator15(),
        systemtests=KerasSystemtestGenerator15(),
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


class KerasAPI1(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI2(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI3(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI4(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[1:]
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI5(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI6(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI7(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI8(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI9(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI10(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI11(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI12(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[:-1]
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI13(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI14(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasAPI15(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("ex ", expected)
        print("res ", result)
        print(args)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class KerasTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> str:
        return producer()

    @staticmethod
    def generate_random_string():
        return "".join(random.choices(string.ascii_letters, k=random.randint(5, 15)))

    @staticmethod
    def spacy1_generate():
        initializer_id = random.choice(['orthogonal', 'uniform', 'normal', 'truncated_normal', "VarianceScaling"])
        # Ast greater, lesser or equal
        greater_or_lesser = random.choice([ast.Gt(), ast.Lt()])
        seed_value = random.randint(0, 2000)
        passing = initializer_id, seed_value, ast.Eq()
        failing = initializer_id, seed_value, greater_or_lesser
        return passing, failing

    @staticmethod
    def spacy2_generate():
        return "", ""

    @staticmethod
    def spacy3_generate():
        return "", ""

    @staticmethod
    def spacy4_generate():
        randomise = random.randint(0, 9999)
        third_argument = "param"
        passing = randomise, third_argument
        failing = randomise
        return passing, failing

    @staticmethod
    def spacy5_generate():
        randomise = KerasTestGenerator.generate_random_string()
        passing = randomise
        failing = randomise, ".keras"
        return passing, failing

    @staticmethod
    def spacy6_generate():
        value1 = random.randint(0, 999)
        value2 = random.randint(0, 999)
        passing = value1, value2, 0
        failing = value1, value2, 1
        return passing, failing

    @staticmethod
    def spacy7_generate():
        num_train = random.randint(0, 1999)
        num_test = random.randint(0, 1999)
        result = random.randint(0, 1999)
        passing = num_train, num_test
        failing = num_train, num_test, result
        return passing, failing

    @staticmethod
    def spacy8_generate():
        value1 = random.randint(0, 999)
        value2 = random.randint(0, 999)
        passing = value1, value1
        failing = value1, value2
        return passing, failing

    @staticmethod
    def spacy9_generate():
        test_doc1 = {
            'doc': """Base class for recurrent layers.

            # Arguments
                cell: A RNN cell instance. A RNN cell is a class that has:
                    - a `call(input_at_t, states_at_t)` method, returning
                        `(output_at_t, states_at_t_plus_1)`. The call method of the
                        cell can also take the optional argument `constants`, see
                        section "Note on passing external constants" below.
                    - a `state_size` attribute. This can be a single integer
                        (single state) in which case it is
                        the size of the recurrent state
                        (which should be the same as the size of the cell output).
                        This can also be a list/tuple of integers
                        (one size per state). In this case, the first entry
                        (`state_size[0]`) should be the same as
                        the size of the cell output.
                    It is also possible for `cell` to be a list of RNN cell instances,
                    in which cases the cells get stacked on after the other in the RNN,
                    implementing an efficient stacked RNN.
                return_sequences: Boolean. Whether to return the last output
                    in the output sequence, or the full sequence.
                return_state: Boolean. Whether to return the last state
                    in addition to the output.
                go_backwards: Boolean (default False).
                    If True, process the input sequence backwards and return the
                    reversed sequence.
                stateful: Boolean (default False). If True, the last state
                    for each sample at index i in a batch will be used as initial
                    state for the sample of index i in the following batch.
                unroll: Boolean (default False).
                    If True, the network will be unrolled,
                    else a symbolic loop will be used.
                    Unrolling can speed-up a RNN,
                    although it tends to be more memory-intensive.
                    Unrolling is only suitable for short sequences.
                input_dim: dimensionality of the input (integer).
                    This argument (or alternatively,
                    the keyword argument `input_shape`)
                    is required when using this layer as the first layer in a model.
                input_length: Length of input sequences, to be specified
                    when it is constant.
                    This argument is required if you are going to connect
                    `Flatten` then `Dense` layers upstream
                    (without it, the shape of the dense outputs cannot be computed).
                    Note that if the recurrent layer is not the first layer
                    in your model, you would need to specify the input length
                    at the level of the first layer
                    (e.g. via the `input_shape` argument)

            # Input shape
                3D tensor with shape `(batch_size, timesteps, input_dim)`.

            # Output shape
                - if `return_state`: a list of tensors. The first tensor is
                    the output. The remaining tensors are the last states,
                    each with shape `(batch_size, units)`.
                - if `return_sequences`: 3D tensor with shape
                    `(batch_size, timesteps, units)`.
                - else, 2D tensor with shape `(batch_size, units)`.

            # Masking
                This layer supports masking for input data with a variable number
                of timesteps. To introduce masks to your data,
                use an [Embedding](embeddings.md) layer with the `mask_zero` parameter
                set to `True`.

            # Note on using statefulness in RNNs
                You can set RNN layers to be 'stateful', which means that the states
                computed for the samples in one batch will be reused as initial states
                for the samples in the next batch. This assumes a one-to-one mapping
                between samples in different successive batches.

                To enable statefulness:
                    - specify `stateful=True` in the layer constructor.
                    - specify a fixed batch size for your model, by passing
                        if sequential model:
                          `batch_input_shape=(...)` to the first layer in your model.
                        else for functional model with 1 or more Input layers:
                          `batch_shape=(...)` to all the first layers in your model.
                        This is the expected shape of your inputs
                        *including the batch size*.
                        It should be a tuple of integers, e.g. `(32, 10, 100)`.
                    - specify `shuffle=False` when calling fit().

                To reset the states of your model, call `.reset_states()` on either
                a specific layer, or on your entire model.

            # Note on specifying the initial state of RNNs
            Note: that
                One: You can specify the initial state of RNN layers symbolically by
                    calling them with the keyword argument `initial_state`.
                Two: The value of `initial_state` should be a tensor or list of
                    tensors representing
                    the initial state of the RNN layer.
                You can specify the initial state of RNN layers numerically by:
                One: calling `reset_states`
                    - With the keyword argument `states`.
                        - The value of
                    `states` should be a numpy array or
                    list of numpy arrays representing
                the initial state of the RNN layer.

            # Note on passing external constants to RNNs
                You can pass "external" constants to the cell using the `constants`
                keyword: argument of `RNN.__call__` (as well as `RNN.call`) method.
                This: requires that the `cell.call` method accepts the same keyword argument
                `constants`. Such constants can be used to condition the cell
                transformation on additional static inputs (not changing over time),
                a.k.a. an attention mechanism.

            # Examples

            ```python
                # First, let's define a RNN Cell, as a layer subclass.

                class MinimalRNNCell(keras.layers.Layer):

                    def __init__(self, units, **kwargs):
                        self.units = units
                        self.state_size = units
                        super(MinimalRNNCell, self).__init__(**kwargs)

                    def build(self, input_shape):
                        self.kernel = self.add_weight(shape=(input_shape[-1], self.units),
                                                      initializer='uniform',
                                                      name='kernel')
                        self.recurrent_kernel = self.add_weight(
                            shape=(self.units, self.units),
                            initializer='uniform',
                            name='recurrent_kernel')
                        self.built = True

                    def call(self, inputs, states):
                        prev_output = states[0]
                        h = K.dot(inputs, self.kernel)
                        output = h + K.dot(prev_output, self.recurrent_kernel)
                        return output, [output]

                # Let's use this cell in a RNN layer:

                cell = MinimalRNNCell(32)
                x = keras.Input((None, 5))
                layer = RNN(cell)
                y = layer(x)

                # Here's how to use the cell to build a stacked RNN:

                cells = [MinimalRNNCell(32), MinimalRNNCell(64)]
                x = keras.Input((None, 5))
                layer = RNN(cells)
                y = layer(x)
            ```
            """,
            'result': '''Base class for recurrent layers.

        __Arguments__

        - __cell__: A RNN cell instance. A RNN cell is a class that has:
            - a `call(input_at_t, states_at_t)` method, returning
                `(output_at_t, states_at_t_plus_1)`. The call method of the
                cell can also take the optional argument `constants`, see
                section "Note on passing external constants" below.
            - a `state_size` attribute. This can be a single integer
                (single state) in which case it is
                the size of the recurrent state
                (which should be the same as the size of the cell output).
                This can also be a list/tuple of integers
                (one size per state). In this case, the first entry
                (`state_size[0]`) should be the same as
                the size of the cell output.

            It is also possible for `cell` to be a list of RNN cell instances,
            in which cases the cells get stacked on after the other in the RNN,
            implementing an efficient stacked RNN.

        - __return_sequences__: Boolean. Whether to return the last output
            in the output sequence, or the full sequence.
        - __return_state__: Boolean. Whether to return the last state
            in addition to the output.
        - __go_backwards__: Boolean (default False).
            If True, process the input sequence backwards and return the
            reversed sequence.
        - __stateful__: Boolean (default False). If True, the last state
            for each sample at index i in a batch will be used as initial
            state for the sample of index i in the following batch.
        - __unroll__: Boolean (default False).
            If True, the network will be unrolled,
            else a symbolic loop will be used.
            Unrolling can speed-up a RNN,
            although it tends to be more memory-intensive.
            Unrolling is only suitable for short sequences.
        - __input_dim__: dimensionality of the input (integer).
            This argument (or alternatively,
            the keyword argument `input_shape`)
            is required when using this layer as the first layer in a model.
        - __input_length__: Length of input sequences, to be specified
            when it is constant.
            This argument is required if you are going to connect
            `Flatten` then `Dense` layers upstream
            (without it, the shape of the dense outputs cannot be computed).
            Note that if the recurrent layer is not the first layer
            in your model, you would need to specify the input length
            at the level of the first layer
            (e.g. via the `input_shape` argument)

        __Input shape__

        3D tensor with shape `(batch_size, timesteps, input_dim)`.

        __Output shape__

        - if `return_state`: a list of tensors. The first tensor is
            the output. The remaining tensors are the last states,
            each with shape `(batch_size, units)`.
        - if `return_sequences`: 3D tensor with shape
            `(batch_size, timesteps, units)`.
        - else, 2D tensor with shape `(batch_size, units)`.

        __Masking__

        This layer supports masking for input data with a variable number
        of timesteps. To introduce masks to your data,
        use an [Embedding](embeddings.md) layer with the `mask_zero` parameter
        set to `True`.

        __Note on using statefulness in RNNs__

        You can set RNN layers to be 'stateful', which means that the states
        computed for the samples in one batch will be reused as initial states
        for the samples in the next batch. This assumes a one-to-one mapping
        between samples in different successive batches.

        To enable statefulness:
        - specify `stateful=True` in the layer constructor.
        - specify a fixed batch size for your model, by passing
        if sequential model:
        `batch_input_shape=(...)` to the first layer in your model.
        else for functional model with 1 or more Input layers:
        `batch_shape=(...)` to all the first layers in your model.
        This is the expected shape of your inputs
        *including the batch size*.
        It should be a tuple of integers, e.g. `(32, 10, 100)`.
        - specify `shuffle=False` when calling fit().

        To reset the states of your model, call `.reset_states()` on either
        a specific layer, or on your entire model.

        __Note on specifying the initial state of RNNs__

        Note: that
        - __One__: You can specify the initial state of RNN layers symbolically by
            calling them with the keyword argument `initial_state`.
        - __Two__: The value of `initial_state` should be a tensor or list of
            tensors representing
            the initial state of the RNN layer.

        You can specify the initial state of RNN layers numerically by:

        - __One__: calling `reset_states`
            - With the keyword argument `states`.
                - The value of

            `states` should be a numpy array or
            list of numpy arrays representing

        the initial state of the RNN layer.

        __Note on passing external constants to RNNs__

        You can pass "external" constants to the cell using the `constants`
        - __keyword__: argument of `RNN.__call__` (as well as `RNN.call`) method.
        - __This__: requires that the `cell.call` method accepts the same keyword argument

        `constants`. Such constants can be used to condition the cell
        transformation on additional static inputs (not changing over time),
        a.k.a. an attention mechanism.

        __Examples__


        ```python
        # First, let's define a RNN Cell, as a layer subclass.

        class MinimalRNNCell(keras.layers.Layer):

            def __init__(self, units, **kwargs):
                self.units = units
                self.state_size = units
                super(MinimalRNNCell, self).__init__(**kwargs)

            def build(self, input_shape):
                self.kernel = self.add_weight(shape=(input_shape[-1], self.units),
                                              initializer='uniform',
                                              name='kernel')
                self.recurrent_kernel = self.add_weight(
                    shape=(self.units, self.units),
                    initializer='uniform',
                    name='recurrent_kernel')
                self.built = True

            def call(self, inputs, states):
                prev_output = states[0]
                h = K.dot(inputs, self.kernel)
                output = h + K.dot(prev_output, self.recurrent_kernel)
                return output, [output]

        # Let's use this cell in a RNN layer:

        cell = MinimalRNNCell(32)
        x = keras.Input((None, 5))
        layer = RNN(cell)
        y = layer(x)

        # Here's how to use the cell to build a stacked RNN:

        cells = [MinimalRNNCell(32), MinimalRNNCell(64)]
        x = keras.Input((None, 5))
        layer = RNN(cells)
        y = layer(x)
        ```
        '''}
        test_doc_with_arguments_as_last_block = {
            'doc': """Base class for recurrent layers.

            # Arguments
                return_sequences: Boolean. Whether to return the last output
                    in the output sequence, or the full sequence.
                return_state: Boolean. Whether to return the last state
                    in addition to the output.
            """,
            'result': '''Base class for recurrent layers.

        __Arguments__

        - __return_sequences__: Boolean. Whether to return the last output
            in the output sequence, or the full sequence.
        - __return_state__: Boolean. Whether to return the last state
            in addition to the output.
        '''}
        passing = test_doc_with_arguments_as_last_block
        failing = test_doc1
        return passing, failing

    @staticmethod
    def spacy10_generate():
        value1 = random.randint(0, 999)
        value2 = random.randint(0, 999)
        value3 = random.randint(0, 999)
        value4 = random.randint(0, 999)
        value5 = random.randint(0, 999)
        passing = value1, value2, value3, value4, value5, [[0], [1], [2], [3], [4]]
        failing = value1, value2, value3, value4, value5, [0, 1, 0, 0, 2]
        return passing, failing

    @staticmethod
    def spacy11_generate():
        return "", ""

    @staticmethod
    def spacy12_generate():
        randomise = random.randint(1, 4999)
        passing = random.choice([((6,), randomise), ((6, 3), randomise), ((6, 3, 1), randomise)])
        failing = random.choice([((6,), float(randomise)), ((6, 3), float(randomise)), ((6, 3, 1), float(randomise))])
        return passing, failing

    @staticmethod
    def spacy13_generate():
        return "", ""

    @staticmethod
    def spacy14_generate():
        return "", ""

    @staticmethod
    def spacy15_generate():
        return "", ""


class KerasUnittestGenerator1(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy1_generate)

    @staticmethod
    def _get_assert(initializer_id: str, random_seed: int, comparison: Any
                    ) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="initializer")],
                value=ast.Attribute(
                    value=ast.Name(id="initializers"),
                    attr=initializer_id,
                    keywords=[ast.keyword(arg="seed", value=ast.Constant(value=random_seed))]
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id="init")],
                value=ast.Call(
                    func=ast.Name(id="initializer"),
                    args=[ast.keyword(arg="seed", value=ast.Constant(value=random_seed))],
                    keywords=[],
                ),
                lineno=2,
            ),
            ast.Assign(
                targets=[ast.Name(id="samples")],
                value=ast.ListComp(
                    elt=ast.Call(
                        func=ast.Name(id="init"),
                        args=[ast.Tuple(elts=[ast.Constant(value=2), ast.Constant(value=2)])],
                        keywords=[],
                    ),
                    generators=[ast.comprehension(
                        target=ast.Name(id="_"),
                        iter=ast.Call(func=ast.Name(id="range"), args=[ast.Constant(value=2)],
                                      keywords=[]),
                        ifs=[],
                        is_async=0,
                    )],
                ),
                lineno=3,
            ),
            ast.Assign(
                targets=[ast.Name(id="samples")],
                value=ast.ListComp(
                    elt=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id="backend"),
                            attr="get_value",
                        ),
                        args=[
                            ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="backend"),
                                    attr="variable",
                                ),
                                args=[ast.Name(id="x")],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                    generators=[ast.comprehension(
                        target=ast.Name(id="x"),
                        iter=ast.Name(id="samples"),
                        ifs=[],
                        is_async=0,
                    )],
                ),
                lineno=4,
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id="numpy"),
                            attr="mean",
                        ),
                        args=[
                            ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="numpy"),
                                    attr="abs",
                                ),
                                args=[
                                    ast.BinOp(
                                        left=ast.Subscript(
                                            value=ast.Name(id="samples"),
                                            slice=ast.Constant(value=0),
                                        ),
                                        op=ast.Sub(),
                                        right=ast.Subscript(
                                            value=ast.Name(id="samples"),
                                            slice=ast.Constant(value=1),
                                        ),
                                    )
                                ],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                    ops=[comparison],
                    comparators=[ast.Constant(value=0.0)],
                ),
                msg=None,
                lineno=5,
            )
        ]

    @staticmethod
    def _get_assert2(initializer_id: str, random_seed: int, compare_operator: Any
                     ) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="initializer")],
                value=ast.Attribute(
                    value=ast.Name(id="initializers"),
                    attr=initializer_id,
                    keywords=[ast.keyword(arg="seed", value=ast.Constant(value=random_seed))]
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id="init")],
                value=ast.Call(
                    func=ast.Name(id="initializer"),
                    args=[ast.keyword(arg="seed", value=ast.Constant(value=random_seed))],
                    keywords=[],
                ),
                lineno=2,
            ),
            ast.Assign(
                targets=[ast.Name(id="samples")],
                value=ast.ListComp(
                    elt=ast.Call(
                        func=ast.Name(id="init"),
                        args=[ast.Tuple(elts=[ast.Constant(value=2), ast.Constant(value=2)])],
                        keywords=[],
                    ),
                    generators=[ast.comprehension(
                        target=ast.Name(id="_"),
                        iter=ast.Call(func=ast.Name(id="range"), args=[ast.Constant(value=2)],
                                      keywords=[]),
                        ifs=[],
                        is_async=0,
                    )],
                ),
                lineno=3,
            ),
            ast.Assign(
                targets=[ast.Name(id="samples")],
                value=ast.ListComp(
                    elt=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id="backend"),
                            attr="get_value",
                        ),
                        args=[
                            ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="backend"),
                                    attr="variable",
                                ),
                                args=[ast.Name(id="x")],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                    generators=[ast.comprehension(
                        target=ast.Name(id="x"),
                        iter=ast.Name(id="samples"),
                        ifs=[],
                        is_async=0,
                    )],
                ),
                lineno=4,
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id="numpy"),
                            attr="mean",
                        ),
                        args=[
                            ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="numpy"),
                                    attr="abs",
                                ),
                                args=[
                                    ast.BinOp(
                                        left=ast.Subscript(
                                            value=ast.Name(id="samples"),
                                            slice=ast.Constant(value=0),
                                        ),
                                        op=ast.Sub(),
                                        right=ast.Subscript(
                                            value=ast.Name(id="samples"),
                                            slice=ast.Constant(value=1),
                                        ),
                                    )
                                ],
                                keywords=[],
                            )
                        ],
                        keywords=[],
                    ),
                    ops=[compare_operator],
                    comparators=[ast.Constant(value=0.0)],
                ),
                msg=None,
                lineno=5,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="backend")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="initializers")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        initializer_id, seed_value, comparison = fail_
        test = self.get_empty_test()
        test.body = self._get_assert2(initializer_id, seed_value, comparison)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        initializer_id, seed_value, comparison = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(initializer_id, seed_value, comparison)
        return test, TestResult.PASSING


class KerasUnittestGenerator2(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy2_generate)

    @staticmethod
    def _get_assert() -> list[Call]:
        return [
            ast.If(
                test=ast.Compare(
                    left=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="K"), attr="backend"),
                        args=[],
                        keywords=[],
                    ),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(value="theano")],
                ),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="WITH_NP")],
                        value=ast.List(elts=[ast.Constant(value=None), ast.Name(id="KNP")]),
                        lineno=1,
                    ),
                ],
                orelse=[
                    ast.If(
                        test=ast.Compare(
                            left=ast.Call(
                                func=ast.Attribute(value=ast.Name(id="K"), attr="backend"),
                                args=[],
                                keywords=[],
                            ),
                            ops=[ast.Eq()],
                            comparators=[ast.Constant(value="cntk")],
                        ),
                        body=[
                            ast.Assign(
                                targets=[ast.Name(id="WITH_NP")],
                                value=ast.List(elts=[ast.Constant(value=None), ast.Name(id="KNP")]),
                                lineno=1,
                            ),
                        ],
                        orelse=[
                            ast.Assign(
                                targets=[ast.Name(id="WITH_NP")],
                                value=ast.List(elts=[ast.Name(id="KTF"), ast.Name(id="KNP")]),
                                lineno=1,
                            ),

                        ],
                    )
                ],
            ),
            ast.Assign(
                targets=[ast.Name(id="batch_size")],
                value=ast.Constant(value=20),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id="num_classes")],
                value=ast.Constant(value=10),
                lineno=2,
            ),
            ast.Assign(
                targets=[ast.Name(id="predictions")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(
                                    value=ast.Name(id="np"),
                                    attr="random",
                                ),
                                attr="random",
                            ),
                            args=[
                                ast.Tuple(
                                    elts=[
                                        ast.Name(id="batch_size"),
                                        ast.Name(id="num_classes"),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                        attr="astype",
                    ),
                    args=[ast.Constant(value="float32")],
                    keywords=[],
                ),
                lineno=3,
            ),
            ast.Assign(
                targets=[ast.Name(id="targets")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                        attr="randint",
                    ),
                    args=[ast.Name(id="num_classes")],
                    keywords=[
                        ast.keyword(arg="size", value=ast.Name(id="batch_size")),
                        ast.keyword(arg="dtype", value=ast.Constant(value="int32")),
                    ],
                ),
                lineno=4,
            ),
            ast.For(
                target=ast.Name(id="k"),
                iter=ast.Call(
                    func=ast.Name(id="range"),
                    args=[
                        ast.Constant(value=1),
                        ast.BinOp(
                            left=ast.Name(id="num_classes"),
                            op=ast.Add(),
                            right=ast.Constant(value=1),
                        ),
                    ],
                    keywords=[],
                ),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="z_list")],
                        value=ast.ListComp(
                            elt=ast.Call(
                                func=ast.Attribute(value=ast.Name(id="b"), attr="eval"),
                                args=[
                                    ast.Call(
                                        func=ast.Attribute(
                                            value=ast.Name(id="b"), attr="in_top_k"
                                        ),
                                        args=[
                                            ast.Call(
                                                func=ast.Attribute(
                                                    value=ast.Name(id="b"), attr="variable"
                                                ),
                                                args=[ast.Name(id="predictions")],
                                                keywords=[
                                                    ast.keyword(
                                                        arg="dtype",
                                                        value=ast.Constant(value="float32"),
                                                    ),
                                                ],
                                            ),
                                            ast.Call(
                                                func=ast.Attribute(
                                                    value=ast.Name(id="b"), attr="variable"
                                                ),
                                                args=[ast.Name(id="targets")],
                                                keywords=[
                                                    ast.keyword(
                                                        arg="dtype",
                                                        value=ast.Constant(value="int32"),
                                                    ),
                                                ],
                                            ),
                                            ast.Name(id="k"),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            generators=[
                                ast.comprehension(
                                    target=ast.Name(id="b"),
                                    iter=ast.Name(id="WITH_NP"),
                                    ifs=[],
                                    is_async=0,
                                )
                            ],
                        ),
                        lineno=5,
                    ),
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id="assert_list_pairwise"),
                            args=[ast.Name(id="z_list")],
                            keywords=[],
                        ),
                        lineno=6,
                    ),
                ],
                orelse=[],
                lineno=7,
            ),
            ast.Assign(
                targets=[ast.Name(id="num_identical")],
                value=ast.BinOp(
                    left=ast.Name(id="num_classes"),
                    op=ast.FloorDiv(),
                    right=ast.Constant(value=2),
                ),
                lineno=8,
            ),
            ast.For(
                target=ast.Name(id="i"),
                iter=ast.Call(
                    func=ast.Name(id="range"),
                    args=[ast.Name(id="batch_size")],
                    keywords=[],
                ),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="idx_identical")],
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                                attr="choice",
                            ),
                            args=[ast.Name(id="num_classes")],
                            keywords=[
                                ast.keyword(
                                    arg="size", value=ast.Name(id="num_identical")
                                ),
                                ast.keyword(arg="replace", value=ast.Constant(value=False)),
                            ],
                        ),
                        lineno=9,
                    ),
                    ast.Assign(
                        targets=[
                            ast.Subscript(
                                value=ast.Name(id="predictions"),
                                slice=ast.Index(
                                    value=ast.Tuple(
                                        elts=[
                                            ast.Name(id="i"),
                                            ast.Name(id="idx_identical"),
                                        ]
                                    )
                                ),
                            )
                        ],
                        value=ast.Subscript(
                            value=ast.Name(id="predictions"),
                            slice=ast.Index(
                                value=ast.Tuple(
                                    elts=[
                                        ast.Name(id="i"),
                                        ast.Constant(value=0),
                                    ]
                                )
                            ),
                        ),
                        lineno=10,
                    ),
                ],
                orelse=[],
                lineno=11,
            ),
            ast.Assign(
                targets=[ast.Name(id="targets")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="np"), attr="zeros"),
                    args=[ast.Name(id="batch_size")],
                    keywords=[
                        ast.keyword(arg="dtype", value=ast.Constant(value="int32")),
                    ],
                ),
                lineno=12,
            ),
            ast.For(
                target=ast.Name(id="k"),
                iter=ast.Call(
                    func=ast.Name(id="range"),
                    args=[
                        ast.Constant(value=1),
                        ast.BinOp(
                            left=ast.Name(id="num_classes"),
                            op=ast.Add(),
                            right=ast.Constant(value=1),
                        ),
                    ],
                    keywords=[],
                ),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="z_list")],
                        value=ast.ListComp(
                            elt=ast.Call(
                                func=ast.Attribute(value=ast.Name(id="b"), attr="eval"),
                                args=[
                                    ast.Call(
                                        func=ast.Attribute(
                                            value=ast.Name(id="b"), attr="in_top_k"
                                        ),
                                        args=[
                                            ast.Call(
                                                func=ast.Attribute(
                                                    value=ast.Name(id="b"), attr="variable"
                                                ),
                                                args=[ast.Name(id="predictions")],
                                                keywords=[
                                                    ast.keyword(
                                                        arg="dtype",
                                                        value=ast.Constant(value="float32"),
                                                    ),
                                                ],
                                            ),
                                            ast.Call(
                                                func=ast.Attribute(
                                                    value=ast.Name(id="b"), attr="variable"
                                                ),
                                                args=[ast.Name(id="targets")],
                                                keywords=[
                                                    ast.keyword(
                                                        arg="dtype",
                                                        value=ast.Constant(value="int32"),
                                                    ),
                                                ],
                                            ),
                                            ast.Name(id="k"),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            generators=[
                                ast.comprehension(
                                    target=ast.Name(id="b"),
                                    iter=ast.Name(id="WITH_NP"),
                                    ifs=[],
                                    is_async=0,
                                )
                            ],
                        ),
                        lineno=5,
                    ),
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id="assert_list_pairwise"),
                            args=[ast.Name(id="z_list")],
                            keywords=[],
                        ),
                        lineno=6,
                    ),
                ],
                orelse=[],
                lineno=7,
            ),
            # ast.Assign(
            #     targets=[ast.Name(id="batch_size")],
            #     value=ast.Constant(value=20),
            #     lineno=1,
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="num_classes")],
            #     value=ast.Constant(value=10),
            #     lineno=2,
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="WITH_NP")],
            #     value=ast.List(elts=[ast.Name(id="KTF"),
            #                          ast.Name(id="KNP")]),
            #     lineno=3,
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="predictions")],
            #     value=ast.Call(
            #         func=ast.Attribute(
            #             value=ast.Call(
            #                 func=ast.Attribute(
            #                     value=ast.Attribute(value=ast.Name(id="numpy"), attr="random",
            #                                         ),
            #                     attr="random",
            #
            #                 ),
            #                 args=[
            #                     ast.Tuple(
            #                         elts=[
            #                             ast.Name(id="batch_size"),
            #                             ast.Name(id="num_classes")
            #                         ],
            #
            #                     )
            #                 ],
            #                 keywords=[]
            #             ),
            #             attr="astype",
            #
            #         ),
            #         args=[ast.Constant(value="float32")],
            #         keywords=[]
            #     ),
            #     lineno=3
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="targets")],
            #     value=ast.Call(
            #         func=ast.Attribute(
            #             value=ast.Attribute(value=ast.Name(id="numpy"), attr="random"),
            #             attr="randint",
            #
            #         ),
            #         args=[ast.Name(id="num_classes")],
            #         keywords=[
            #             ast.keyword(arg="size", value=ast.Name(id="batch_size")),
            #             ast.keyword(arg="dtype", value=ast.Constant(value="int32"))
            #         ]
            #     ),
            #     lineno=4
            # ),
            # ast.For(
            #     target=ast.Name(id="k"),
            #     iter=ast.Call(
            #         func=ast.Name(id="range"),
            #         args=[
            #             ast.Constant(value=1),
            #             ast.BinOp(left=ast.Name(id="num_classes"), op=ast.Add(),
            #                       right=ast.Constant(value=1))
            #         ],
            #         keywords=[]
            #     ),
            #     body=[
            #         ast.Assign(
            #             targets=[ast.Name(id="z_list")],
            #             value=ast.ListComp(
            #                 elt=ast.Call(
            #                     func=ast.Attribute(value=ast.Name(id="b"), attr="eval"),
            #                     args=[
            #                         ast.Call(
            #                             func=ast.Attribute(value=ast.Name(id="b"), attr="in_top_k",
            #                                                ),
            #                             args=[
            #                                 ast.Call(
            #                                     func=ast.Attribute(value=ast.Name(id="b"),
            #                                                        attr="variable"),
            #                                     args=[ast.Name(id="predictions")],
            #                                     keywords=[ast.keyword(arg="dtype", value=ast.Constant(value="float32"))]
            #                                 ),
            #                                 ast.Call(
            #                                     func=ast.Attribute(value=ast.Name(id="b"),
            #                                                        attr="variable"),
            #                                     args=[ast.Name(id="targets")],
            #                                     keywords=[ast.keyword(arg="dtype", value=ast.Constant(value="int32"))]
            #                                 ),
            #                                 ast.Name(id="k")
            #                             ],
            #                             keywords=[]
            #                         )
            #                     ],
            #                     keywords=[]
            #                 ),
            #                 generators=[
            #                     ast.comprehension(target=ast.Name(id="b"),
            #                                       iter=ast.Name(id="WITH_NP"), ifs=[], is_async=0)
            #                 ]
            #             ),
            #             lineno=5
            #         ),
            #         ast.For(
            #             target=ast.Tuple(
            #                 elts=[
            #                     ast.Name(id="z1"),
            #                     ast.Name(id="z2")
            #                 ],
            #
            #             ),
            #             iter=ast.Call(
            #                 func=ast.Name(id="zip"),
            #                 args=[
            #                     ast.Subscript(
            #                         value=ast.Name(id="z_list"),
            #                         slice=ast.Slice(lower=ast.Constant(value=1), upper=None),
            #
            #                     ),
            #                     ast.Subscript(
            #                         value=ast.Name(id="z_list"),
            #                         slice=ast.Slice(lower=None, upper=ast.Constant(value=-1)),
            #
            #                     )
            #                 ],
            #                 keywords=[]
            #             ),
            #             body=[
            #                 ast.If(
            #                     test=ast.Constant(value=True),
            #                     body=[
            #                         ast.Assert(
            #                             test=ast.Compare(
            #                                 left=ast.Attribute(value=ast.Name(id="z1"), attr="shape",
            #                                                    ),
            #                                 ops=[ast.Eq()],
            #                                 comparators=[
            #                                     ast.Attribute(value=ast.Name(id="z2"), attr="shape",
            #                                                   )]
            #                             ),
            #                             msg=None
            #                         )
            #                     ],
            #                     orelse=[]
            #                 ),
            #                 ast.If(
            #                     test=ast.Constant(value=True),
            #                     body=[
            #                         ast.Expr(
            #                             value=ast.Call(
            #                                 func=ast.Name(id="assert_allclose"),
            #                                 args=[
            #                                     ast.Name(id="z1"),
            #                                     ast.Name(id="z2")
            #                                 ],
            #                                 keywords=[ast.keyword(arg="atol", value=ast.Constant(value=1e-05))]
            #                             )
            #                         )
            #                     ],
            #                     orelse=[]
            #                 ),
            #                 ast.If(
            #                     test=ast.Constant(value=False),
            #                     body=[
            #                         ast.Assert(
            #                             test=ast.Compare(
            #                                 left=ast.Name(id="z1"),
            #                                 ops=[ast.Eq()],
            #                                 comparators=[ast.Name(id="z2")]
            #                             ),
            #                             msg=None
            #                         )
            #                     ],
            #                     orelse=[]
            #                 )
            #             ],
            #             orelse=[],
            #             lineno=13
            #         ),
            #     ],
            #     orelse=[],
            #     lineno=6
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="num_identical")],
            #     value=ast.BinOp(left=ast.Name(id="num_classes"), op=ast.FloorDiv(),
            #                     right=ast.Constant(value=2)),
            #     lineno=7
            # ),
            # ast.For(
            #     target=ast.Name(id="i"),
            #     iter=ast.Call(
            #         func=ast.Name(id="range"),
            #         args=[ast.Name(id="batch_size")],
            #         keywords=[]
            #     ),
            #     body=[
            #         ast.Assign(
            #             targets=[ast.Name(id="idx_identical")],
            #             value=ast.Call(
            #                 func=ast.Attribute(
            #                     value=ast.Attribute(value=ast.Name(id="np"), attr="random",
            #                                         ),
            #                     attr="choice",
            #
            #                 ),
            #                 args=[ast.Name(id="num_classes")],
            #                 keywords=[
            #                     ast.keyword(arg="size", value=ast.Name(id="num_identical")),
            #                     ast.keyword(arg="replace", value=ast.Constant(value=False))
            #                 ]
            #             ),
            #             lineno=8
            #         ),
            #         ast.Assign(
            #             targets=[ast.Subscript(
            #                 value=ast.Name(id="predictions"),
            #                 slice=ast.Index(value=ast.Tuple(
            #                     elts=[ast.Name(id="i"), ast.Name(id="idx_identical")],
            #                 )),
            #
            #             )],
            #             value=ast.Subscript(
            #                 value=ast.Name(id="predictions"),
            #                 slice=ast.Index(
            #                     value=ast.Tuple(elts=[ast.Name(id="i"), ast.Constant(value=0)],
            #                                     )),
            #
            #             ),
            #             lineno=9
            #         )
            #     ],
            #     orelse=[],
            #     lineno=10
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="targets")],
            #     value=ast.Call(
            #         func=ast.Attribute(value=ast.Name(id="numpy"), attr="zeros"),
            #         args=[ast.Name(id="batch_size")],
            #         keywords=[ast.keyword(arg="dtype", value=ast.Constant(value="int32"))]
            #     ),
            #     lineno=11
            # ),
            # ast.For(
            #     target=ast.Name(id="k"),
            #     iter=ast.Call(
            #         func=ast.Name(id="range"),
            #         args=[
            #             ast.Constant(value=1),
            #             ast.BinOp(left=ast.Name(id="num_classes"), op=ast.Add(),
            #                       right=ast.Constant(value=1))
            #         ],
            #         keywords=[]
            #     ),
            #     body=[
            #         ast.Assign(
            #             targets=[ast.Name(id="z_list")],
            #             value=ast.ListComp(
            #                 elt=ast.Call(
            #                     func=ast.Attribute(value=ast.Name(id="b"), attr="eval"),
            #                     args=[
            #                         ast.Call(
            #                             func=ast.Attribute(value=ast.Name(id="b"), attr="in_top_k",
            #                                                ),
            #                             args=[
            #                                 ast.Call(
            #                                     func=ast.Attribute(value=ast.Name(id="b"),
            #                                                        attr="variable"),
            #                                     args=[ast.Name(id="predictions")],
            #                                     keywords=[ast.keyword(arg="dtype", value=ast.Constant(value="float32"))]
            #                                 ),
            #                                 ast.Call(
            #                                     func=ast.Attribute(value=ast.Name(id="b"),
            #                                                        attr="variable"),
            #                                     args=[ast.Name(id="targets")],
            #                                     keywords=[ast.keyword(arg="dtype", value=ast.Constant(value="int32"))]
            #                                 ),
            #                                 ast.Name(id="k")
            #                             ],
            #                             keywords=[]
            #                         )
            #                     ],
            #                     keywords=[]
            #                 ),
            #                 generators=[
            #                     ast.comprehension(target=ast.Name(id="b"),
            #                                       iter=ast.Name(id="WITH_NP"), ifs=[], is_async=0)
            #                 ]
            #             ),
            #             lineno=12
            #         ),
            #
            #     ],
            #     orelse=[],
            #
            #     lineno=13
            # ),
            # ast.For(
            #     target=ast.Tuple(
            #         elts=[
            #             ast.Name(id="z1"),
            #             ast.Name(id="z2")
            #         ],
            #
            #     ),
            #     iter=ast.Call(
            #         func=ast.Name(id="zip"),
            #         args=[
            #             ast.Subscript(
            #                 value=ast.Name(id="z_list"),
            #                 slice=ast.Slice(lower=ast.Constant(value=1), upper=None),
            #
            #             ),
            #             ast.Subscript(
            #                 value=ast.Name(id="z_list"),
            #                 slice=ast.Slice(lower=None, upper=ast.Constant(value=-1)),
            #
            #             )
            #         ],
            #         keywords=[]
            #     ),
            #     body=[
            #         ast.If(
            #             test=ast.Constant(value=True),
            #             body=[
            #                 ast.Assert(
            #                     test=ast.Compare(
            #                         left=ast.Attribute(value=ast.Name(id="z1"), attr="shape",
            #                                            ),
            #                         ops=[ast.Eq()],
            #                         comparators=[ast.Attribute(value=ast.Name(id="z2"), attr="shape",
            #                                                    )]
            #                     ),
            #                     msg=None
            #                 )
            #             ],
            #             orelse=[]
            #         ),
            #         ast.If(
            #             test=ast.Constant(value=True),
            #             body=[
            #                 ast.Expr(
            #                     value=ast.Call(
            #                         func=ast.Name(id="assert_allclose"),
            #                         args=[
            #                             ast.Name(id="z1"),
            #                             ast.Name(id="z2")
            #                         ],
            #                         keywords=[ast.keyword(arg="atol", value=ast.Constant(value=1e-05))]
            #                     )
            #                 )
            #             ],
            #             orelse=[]
            #         ),
            #         ast.If(
            #             test=ast.Constant(value=False),
            #             body=[
            #                 ast.Assert(
            #                     test=ast.Compare(
            #                         left=ast.Name(id="z1"),
            #                         ops=[ast.Eq()],
            #                         comparators=[ast.Name(id="z2")]
            #                     ),
            #                     msg=None
            #                 )
            #             ],
            #             orelse=[]
            #         )
            #     ],
            #     orelse=[],
            #     lineno=13
            # ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="backend", asname="K")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.backend",
                names=[ast.alias(name="tensorflow_backend", asname="KTF")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.backend",
                names=[ast.alias(name="numpy_backend", asname="KNP")],
                level=0,
            ),
            ast.ImportFrom(
                module="tests.keras.backend.backend_test",
                names=[ast.alias(name="assert_list_pairwise")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class KerasUnittestGenerator3(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy3_generate)

    @staticmethod
    def _get_assert() -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="input_layer")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="keras"),
                        attr="Input",

                    ),
                    args=[],
                    keywords=[
                        ast.keyword(arg="shape", value=ast.Tuple(
                            elts=[ast.Constant(value=4)],

                        ))
                    ],
                ),
                lineno=1

            ),
            ast.Assign(
                targets=[ast.Name(id="layer1")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="keras"), attr="layers"),
                        attr="Lambda"
                    ),
                    args=[
                        ast.Lambda(
                            args=ast.arguments(
                                args=[ast.arg(arg="x", annotation=None)],
                                vararg=None,
                                kwonlyargs=[],
                                posonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[]
                            ),
                            body=ast.List(
                                elts=[
                                    ast.BinOp(left=ast.Name(id="x"), op=ast.Add(),
                                              right=ast.Constant(value=1)),
                                    ast.Name(id="x")
                                ]
                            )
                        ),
                        ast.Lambda(
                            args=ast.arguments(
                                args=[ast.arg(arg="shapes", annotation=None)],
                                vararg=None,
                                kwonlyargs=[],
                                posonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[]
                            ),
                            body=ast.List(elts=[ast.Name(id="shapes"), ast.Name(id="shapes")])
                        )
                    ],
                    keywords=[]
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[
                    ast.Tuple(
                        elts=[ast.Name(id="x_a"), ast.Name(id="x_b")],

                    )
                ],
                value=ast.Call(
                    func=ast.Name(id="layer1"),
                    args=[ast.Name(id="input_layer")],
                    keywords=[]
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[
                    ast.Tuple(
                        elts=[ast.Name(id="x_a"), ast.Name(id="x_b")],

                    )
                ],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Name(id="SwapLayer"),
                        args=[],
                        keywords=[]
                    ),
                    args=[
                        ast.List(
                            elts=[
                                ast.Name(id="x_a"),
                                ast.Name(id="x_b")
                            ],

                        )
                    ],
                    keywords=[]
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="model")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="keras"),
                        attr="Model",
                    ),
                    args=[],
                    keywords=[
                        ast.keyword(
                            arg="inputs",
                            value=ast.List(
                                elts=[ast.Name(id="input_layer")],

                            )
                        ),
                        ast.keyword(
                            arg="outputs",
                            value=ast.List(
                                elts=[ast.Name(id="x_a"), ast.Name(id="x_b")],

                            )
                        )
                    ]
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id="new_model")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="keras"), attr="models"),
                        attr="clone_model",

                    ),
                    args=[ast.Name(id="model")],
                    keywords=[]
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id="x_test")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                        attr="random",

                    ),
                    args=[ast.Tuple(elts=[ast.Constant(value=10), ast.Constant(value=4)])],
                    keywords=[]
                ),
                lineno=4
            ),
            ast.Assign(
                targets=[
                    ast.Tuple(
                        elts=[ast.Name(id="pred_a"), ast.Name(id="pred_b")],

                    )
                ],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="predict"),
                    args=[ast.Name(id="x_test")],
                    keywords=[]
                ),
                lineno=5
            ),
            ast.Assign(
                targets=[
                    ast.Tuple(
                        elts=[ast.Name(id="pred_new_a"), ast.Name(id="pred_new_b")],

                    )
                ],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="new_model"), attr="predict"),
                    args=[ast.Name(id="x_test")],
                    keywords=[]
                ),
                lineno=6
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="assert"),
                    args=[
                        ast.Compare(
                            left=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="pred_a"),
                                    attr="all",

                                ),
                                args=[],
                                keywords=[]
                            ),
                            ops=[ast.Eq()],
                            comparators=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id="pred_new_a"),
                                        attr="all",

                                    ),
                                    args=[],
                                    keywords=[]
                                )
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=7
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="assert"),
                    args=[
                        ast.Compare(
                            left=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="pred_b"),
                                    attr="all",

                                ),
                                args=[],
                                keywords=[]
                            ),
                            ops=[ast.Eq()],
                            comparators=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id="pred_new_b"),
                                        attr="all",

                                    ),
                                    args=[],
                                    keywords=[]
                                )
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=8
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.Import(
                module="keras",
                names=[ast.alias(name="keras")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="initializers")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class KerasUnittestGenerator4(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy4_generate)

    @staticmethod
    def _get_assert(randomise: int, third_argument: str) -> list[Call]:
        return [
            ast.ClassDef(
                name="MyTfOptimizer",
                bases=[ast.Attribute(value=ast.Name(id="train"), attr="Optimizer")],
                keywords=[],
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="wrapping_optimizer")],
                        value=ast.Call(
                            func=ast.Attribute(value=ast.Name(id="train"), attr="AdamOptimizer"),
                            args=[],
                            keywords=[]
                        ),
                        lineno=1
                    ),
                    ast.FunctionDef(
                        name="compute_gradients",
                        args=ast.arguments(
                            posonlyargs=[],
                            args=[
                                ast.arg(arg="self"),
                                ast.arg(arg="loss"),
                                ast.arg(arg=third_argument),
                            ],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=ast.arg(arg="kwargs"),
                            defaults=[]
                        ),
                        body=[
                            ast.Return(
                                value=ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Call(
                                            func=ast.Name(id="super"),
                                            args=[
                                                ast.Name(id="MyTfOptimizer"),
                                                ast.Name(id="self")
                                            ],
                                            keywords=[]
                                        ),
                                        attr="compute_gradients"
                                    ),
                                    args=[ast.Name(id="loss"),
                                          ast.arg(arg=third_argument)],
                                    keywords=[ast.keyword(arg=None, value=ast.Name(id="kwargs"))]
                                )
                            )
                        ],
                        decorator_list=[],
                        lineno=2
                    ),
                    ast.FunctionDef(
                        name="apply_gradients",
                        args=ast.arguments(
                            posonlyargs=[],
                            args=[
                                ast.arg(arg="self"),
                                ast.arg(arg="grads_and_vars"),
                            ],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=ast.arg(arg="kwargs"),
                            defaults=[]
                        ),
                        body=[
                            ast.Return(
                                value=ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Attribute(value=ast.Name(id="self"), attr="wrapping_optimizer"),
                                        attr="apply_gradients"
                                    ),
                                    args=[ast.Name(id="grads_and_vars")],
                                    keywords=[ast.keyword(arg=None, value=ast.Name(id="kwargs"))]
                                )
                            )
                        ],
                        decorator_list=[],
                        lineno=3
                    )
                ],
                decorator_list=[],
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id="my_tf_optimizer")],
                value=ast.Call(
                    func=ast.Name(id="MyTfOptimizer"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="use_locking", value=ast.Constant(value=False)),
                        ast.keyword(arg="name", value=ast.Constant(value="MyTfOptimizer"))
                    ]
                ),
                lineno=4
            ),
            ast.Assign(
                targets=[ast.Name(id="optimizer")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="optimizers"), attr="TFOptimizer"),
                    args=[ast.Name(id="my_tf_optimizer")],
                    keywords=[]
                ),
                lineno=5
            ),
            ast.Assign(
                targets=[ast.Name(id="model")],
                value=ast.Call(
                    func=ast.Name(id="Sequential"),
                    args=[],
                    keywords=[]
                ),
                lineno=6
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="add"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="Dense"),
                            args=[
                                ast.Constant(value=2)
                            ],
                            keywords=[
                                ast.keyword(arg="input_shape", value=ast.Tuple(elts=[ast.Constant(value=3)])),
                                ast.keyword(arg="kernel_constraint",
                                            value=ast.Call(
                                                func=ast.Attribute(value=ast.Name(id="constraints"), attr="MaxNorm"),
                                                args=[ast.Constant(value=1)],
                                                keywords=[]
                                            ))
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=7
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="compile"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="loss", value=ast.Constant(value="mean_squared_error")),
                        ast.keyword(arg="optimizer", value=ast.Name(id="optimizer"))
                    ]
                ),
                lineno=8
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="fit"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                                attr="random"
                            ),
                            args=[ast.Tuple(elts=[ast.Constant(value=randomise), ast.Constant(value=3)])],
                            keywords=[]
                        ),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                                attr="random"
                            ),
                            args=[ast.Tuple(elts=[ast.Constant(value=randomise), ast.Constant(value=2)])],
                            keywords=[]
                        ),
                    ],
                    keywords=[
                        ast.keyword(arg="epochs", value=ast.Constant(value=1)),
                        ast.keyword(arg="batch_size", value=ast.Constant(value=5)),
                        ast.keyword(arg="verbose", value=ast.Constant(value=0))
                    ]
                ),
                lineno=9
            )
        ]

    @staticmethod
    def _get_assert2(randomise: int) -> list[Call]:
        return [
            ast.ClassDef(
                name="MyTfOptimizer",
                bases=[ast.Attribute(value=ast.Name(id="train"), attr="Optimizer")],
                keywords=[],
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="wrapping_optimizer")],
                        value=ast.Call(
                            func=ast.Attribute(value=ast.Name(id="train"), attr="AdamOptimizer"),
                            args=[],
                            keywords=[]
                        ),
                        lineno=1
                    ),
                    ast.FunctionDef(
                        name="compute_gradients",
                        args=ast.arguments(
                            posonlyargs=[],
                            args=[
                                ast.arg(arg="self"),
                                ast.arg(arg="loss")],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=ast.arg(arg="kwargs"),
                            defaults=[]
                        ),
                        body=[
                            ast.Return(
                                value=ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Call(
                                            func=ast.Name(id="super"),
                                            args=[
                                                ast.Name(id="MyTfOptimizer"),
                                                ast.Name(id="self")
                                            ],
                                            keywords=[]
                                        ),
                                        attr="compute_gradients"
                                    ),
                                    args=[ast.Name(id="loss")],
                                    keywords=[ast.keyword(arg=None, value=ast.Name(id="kwargs"))]
                                )
                            )
                        ],
                        decorator_list=[],
                        lineno=2
                    ),
                    ast.FunctionDef(
                        name="apply_gradients",
                        args=ast.arguments(
                            posonlyargs=[],
                            args=[
                                ast.arg(arg="self"),
                                ast.arg(arg="grads_and_vars"),
                            ],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=ast.arg(arg="kwargs"),
                            defaults=[]
                        ),
                        body=[
                            ast.Return(
                                value=ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Attribute(value=ast.Name(id="self"), attr="wrapping_optimizer"),
                                        attr="apply_gradients"
                                    ),
                                    args=[ast.Name(id="grads_and_vars")],
                                    keywords=[ast.keyword(arg=None, value=ast.Name(id="kwargs"))]
                                )
                            )
                        ],
                        decorator_list=[],
                        lineno=3
                    )
                ],
                decorator_list=[],
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id="my_tf_optimizer")],
                value=ast.Call(
                    func=ast.Name(id="MyTfOptimizer"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="use_locking", value=ast.Constant(value=False)),
                        ast.keyword(arg="name", value=ast.Constant(value="MyTfOptimizer"))
                    ]
                ),
                lineno=4
            ),
            ast.Assign(
                targets=[ast.Name(id="optimizer")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="optimizers"), attr="TFOptimizer"),
                    args=[ast.Name(id="my_tf_optimizer")],
                    keywords=[]
                ),
                lineno=5
            ),
            ast.Assign(
                targets=[ast.Name(id="model")],
                value=ast.Call(
                    func=ast.Name(id="Sequential"),
                    args=[],
                    keywords=[]
                ),
                lineno=6
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="add"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="Dense"),
                            args=[
                                ast.Constant(value=2)
                            ],
                            keywords=[
                                ast.keyword(arg="input_shape", value=ast.Tuple(elts=[ast.Constant(value=3)])),
                                ast.keyword(arg="kernel_constraint",
                                            value=ast.Call(
                                                func=ast.Attribute(value=ast.Name(id="constraints"), attr="MaxNorm"),
                                                args=[ast.Constant(value=1)],
                                                keywords=[]
                                            ))
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=7
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="compile"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="loss", value=ast.Constant(value="mean_squared_error")),
                        ast.keyword(arg="optimizer", value=ast.Name(id="optimizer"))
                    ]
                ),
                lineno=8
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="fit"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                                attr="random"
                            ),
                            args=[ast.Tuple(elts=[ast.Constant(value=randomise), ast.Constant(value=3)])],
                            keywords=[]
                        ),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                                attr="random"
                            ),
                            args=[ast.Tuple(elts=[ast.Constant(value=randomise), ast.Constant(value=2)])],
                            keywords=[]
                        ),
                    ],
                    keywords=[
                        ast.keyword(arg="epochs", value=ast.Constant(value=1)),
                        ast.keyword(arg="batch_size", value=ast.Constant(value=5)),
                        ast.keyword(arg="verbose", value=ast.Constant(value=0))
                    ]
                ),
                lineno=9
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="constraints")],
                level=0,
            ),
            ast.ImportFrom(
                module="tensorflow",
                names=[ast.alias(name="train")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.models",
                names=[ast.alias(name="Sequential")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.layers.core",
                names=[ast.alias(name="Dense")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="optimizers")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert2(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        randomise, third_value = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(randomise, third_value)
        return test, TestResult.PASSING


class KerasUnittestGenerator5(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy5_generate)

    @staticmethod
    def _get_assert(randomise: str) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="original_keras_home")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id="os"),
                            attr="environ"
                        ),
                        attr="get"
                    ),
                    args=[ast.Constant(value="KERAS_HOME")],
                    keywords=[]
                ),
                lineno=1,
            ),
            ast.If(
                test=ast.Compare(
                    left=ast.Constant(value="KERAS_HOME"),
                    ops=[ast.In()],
                    comparators=[ast.Attribute(value=ast.Name(id="os"), attr="environ")]
                ),
                body=[
                    ast.Delete(
                        targets=[
                            ast.Subscript(
                                value=ast.Attribute(value=ast.Name(id="os"), attr="environ"),
                                slice=ast.Constant(value="KERAS_HOME")
                            )
                        ]
                    )
                ],
                orelse=[]
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="reload_module"),
                    args=[ast.Name(id="K")],
                    keywords=[]
                ),
                lineno=3,
            ),
            ast.Assign(
                targets=[ast.Name(id="dirname")],
                value=ast.Constant(value="data_utils"),
                lineno=4,
            ),
            ast.Assign(
                targets=[ast.Name(id="origin")],
                value=ast.Call(
                    func=ast.Name(id="urljoin"),
                    args=[
                        ast.Constant(value="file://"),
                        ast.Call(
                            func=ast.Name(id="pathname2url"),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                        attr="abspath"
                                    ),
                                    args=[ast.Constant(value=f"test.{randomise}.gz")],
                                    keywords=[]
                                )
                            ],
                            keywords=[]
                        ),
                    ],
                    keywords=[]
                ),
                lineno=5,
            ),
            ast.Assign(
                targets=[ast.Name(id="path")],
                value=ast.Call(
                    func=ast.Name(id="get_file"),
                    args=[
                        ast.Name(id="dirname"),
                        ast.Name(id="origin")
                    ],
                    keywords=[ast.keyword(arg="untar", value=ast.Constant(value=True))]
                ),
                lineno=6,
            ),
            ast.Assign(
                targets=[ast.Name(id="filepath")],
                value=ast.BinOp(
                    left=ast.Name(id="path"),
                    op=ast.Add(),
                    right=ast.Constant(value=".tar.gz")
                ),
                lineno=7,
            ),
            ast.Assign(
                targets=[ast.Name(id="data_keras_home")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                        attr="dirname"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                attr="dirname"
                            ),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                        attr="abspath"
                                    ),
                                    args=[ast.Name(id="filepath")],
                                    keywords=[]
                                )
                            ],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                ),
                lineno=8,
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Name(id="data_keras_home"),
                    ops=[ast.Eq()],
                    comparators=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                attr="dirname"
                            ),
                            args=[ast.Attribute(value=ast.Name(id="K"), attr="_config_path")],
                            keywords=[]
                        )
                    ]
                ),
                msg=None,
                lineno=9,
            ),
            ast.If(
                test=ast.Compare(
                    left=ast.Name(id="original_keras_home"),
                    ops=[ast.IsNot()],
                    comparators=[ast.Constant(value=None)]
                ),
                body=[
                    ast.Assign(
                        targets=[
                            ast.Subscript(
                                value=ast.Attribute(value=ast.Name(id="os"), attr="environ"),
                                slice=ast.Constant(value="KERAS_HOME")
                            )
                        ],
                        value=ast.Name(id="original_keras_home"),
                        lineno=10,
                    ),
                ],
                orelse=[
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="os"), attr="environ"),
                                               attr="pop"),
                            args=[ast.Constant(value="KERAS_HOME"), ast.Constant(value=None)],
                            keywords=[]
                        )
                    )
                ]
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="reload_module"),
                    args=[ast.Name(id="K")],
                    keywords=[]
                ),
                lineno=10,
            )
        ]

    @staticmethod
    def _get_assert2(randomise: str, keras_home: str) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="original_keras_home")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="os"), attr="environ"), attr="get"),
                    args=[ast.Constant(value="KERAS_HOME")],
                    keywords=[]
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id="_keras_home")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="os"), attr="path"), attr="join"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                               attr="abspath"),
                            args=[ast.Constant(value=".")],
                            keywords=[]
                        ),
                        ast.Constant(value=keras_home)
                    ],
                    keywords=[]
                ),
                lineno=2,
            ),
            ast.If(
                test=ast.UnaryOp(
                    op=ast.Not(),
                    operand=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="os"), attr="path.exists"),
                        args=[ast.Name(id="_keras_home")],
                        keywords=[]
                    ),
                ),
                body=[
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(value=ast.Name(id="os"), attr="makedirs"),
                            args=[ast.Name(id="_keras_home")],
                            keywords=[]
                        )
                    )
                ],
                orelse=[]
            ),
            ast.Assign(
                targets=[
                    ast.Subscript(
                        value=ast.Attribute(value=ast.Name(id="os"), attr="environ"),
                        slice=ast.Constant(value="KERAS_HOME")
                    )
                ],
                value=ast.Name(id="_keras_home"),
                lineno=3,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="reload_module"),
                    args=[ast.Name(id="K")],
                    keywords=[]
                ),
                lineno=4,
            ),
            ast.Assign(
                targets=[ast.Name(id="dirname")],
                value=ast.Constant(value="data_utils"),
                lineno=5,
            ),
            ast.Assign(
                targets=[ast.Name(id="origin")],
                value=ast.Call(
                    func=ast.Name(id="urljoin"),
                    args=[
                        ast.Constant(value="file://"),
                        ast.Call(
                            func=ast.Name(id="pathname2url"),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                        attr="abspath"
                                    ),
                                    args=[ast.Constant(value=f"test.{randomise}.gz")],
                                    keywords=[]
                                )
                            ],
                            keywords=[]
                        ),
                    ],
                    keywords=[]
                ),
                lineno=6,
            ),
            ast.Assign(
                targets=[ast.Name(id="path")],
                value=ast.Call(
                    func=ast.Name(id="get_file"),
                    args=[ast.Name(id="dirname"), ast.Name(id="origin")],
                    keywords=[ast.keyword(arg="untar", value=ast.Constant(value=True))]
                ),
                lineno=7,
            ),
            ast.Assign(
                targets=[ast.Name(id="filepath")],
                value=ast.BinOp(
                    left=ast.Name(id="path"),
                    op=ast.Add(),
                    right=ast.Constant(value=".tar.gz")
                ),
                lineno=8,
            ),
            ast.Assign(
                targets=[ast.Name(id="data_keras_home")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                        attr="dirname"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                attr="dirname"
                            ),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                        attr="abspath"
                                    ),
                                    args=[ast.Name(id="filepath")],
                                    keywords=[]
                                )
                            ],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                ),
                lineno=9,
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Name(id="data_keras_home"),
                    ops=[ast.Eq()],
                    comparators=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(value=ast.Name(id="os"), attr="path"),
                                attr="dirname"
                            ),
                            args=[ast.Attribute(value=ast.Name(id="K"), attr="_config_path")],
                            keywords=[]
                        )
                    ]
                ),
                msg=None,
                lineno=10,
            ),
            ast.If(
                test=ast.Compare(
                    left=ast.Name(id="original_keras_home"),
                    ops=[ast.IsNot()],
                    comparators=[ast.Constant(value=None)]
                ),
                body=[
                    ast.Assign(
                        targets=[
                            ast.Subscript(
                                value=ast.Attribute(value=ast.Name(id="os"), attr="environ"),
                                slice=ast.Constant(value="KERAS_HOME")
                            )
                        ],
                        value=ast.Name(id="original_keras_home"),
                        lineno=11,
                    )
                ],
                orelse=[
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="os"), attr="environ"),
                                               attr="pop"),
                            args=[ast.Constant(value="KERAS_HOME"), ast.Constant(value=None)],
                            keywords=[]
                        )
                    )
                ]
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="reload_module"),
                    args=[ast.Name(id="K")],
                    keywords=[]
                ),
                lineno=12,
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="os",
                names=[ast.alias(name="os")],
                level=0,
            ),
            ast.ImportFrom(
                module="six.moves.urllib.parse",
                names=[ast.alias(name="urljoin")],
                level=0,
            ),
            ast.ImportFrom(
                module="six.moves.urllib.request",
                names=[ast.alias(name="pathname2url")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.utils.data_utils",
                names=[ast.alias(name="get_file")],
                level=0,
            ),
            ast.ImportFrom(
                module="six.moves",
                names=[ast.alias(name="reload_module")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="backend", asname="K")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        randomise, keras_home = fail_
        test = self.get_empty_test()
        test.body = self._get_assert2(randomise, keras_home)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class KerasUnittestGenerator6(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy6_generate)

    @staticmethod
    def _get_assert(value1: int, value2: int, loss: int) -> list[Call]:
        return [
            ast.Assign(
                targets=[
                    ast.Name(id="x"),
                    ast.Name(id="y"),
                ],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="np"),
                        attr="array"
                    ),
                    args=[
                        ast.List(
                            elts=[
                                ast.List(
                                    elts=[
                                        ast.List(elts=[ast.Constant(value=value1)]),
                                        ast.List(elts=[ast.Constant(value=value2)])
                                    ]
                                )
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="model")],
                value=ast.Call(
                    func=ast.Name(id="Sequential"),
                    args=[],
                    keywords=[]
                ),
                lineno=2
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="model"),
                        attr="add"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Name(id="Masking"),
                            args=[],
                            keywords=[
                                ast.keyword(arg="mask_value", value=ast.Constant(value=0)),
                                ast.keyword(
                                    arg="input_shape",
                                    value=ast.Tuple(
                                        elts=[ast.Constant(value=None), ast.Constant(value=1)]
                                    )
                                )
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=3
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="model"),
                        attr="add"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Name(id="TimeDistributed"),
                            args=[
                                ast.Call(
                                    func=ast.Name(id="Dense"),
                                    args=[ast.Constant(value=1)],
                                    keywords=[
                                        ast.keyword(
                                            arg="kernel_initializer",
                                            value=ast.Constant(value="one")
                                        )
                                    ]
                                )
                            ],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                ),
                lineno=4
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="model"),
                        attr="compile"
                    ),
                    args=[],
                    keywords=[
                        ast.keyword(arg="loss", value=ast.Constant(value="mse")),
                        ast.keyword(arg="optimizer", value=ast.Constant(value="sgd"))
                    ]
                ),
                lineno=5
            ),
            ast.Assign(
                targets=[ast.Name(id="loss")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="model"),
                        attr="train_on_batch"
                    ),
                    args=[
                        ast.Name(id="x"),
                        ast.Name(id="y")
                    ],
                    keywords=[]
                ),
                lineno=6
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Name(id="loss"),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(value=loss)]
                ),
                msg=None,
                lineno=7
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="keras.models",
                names=[ast.alias(name="Sequential")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.layers",
                names=[ast.alias(name="TimeDistributed"),
                       ast.alias(name="Masking"),
                       ast.alias(name="Dense")],
                level=0,
            ),
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        value1, value2, loss = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(value1, value2, loss)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        value1, value2, loss = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(value1, value2, loss)
        return test, TestResult.PASSING


class KerasUnittestGenerator7(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy7_generate)

    @staticmethod
    def _get_assert(num_train: int, num_test: int) -> list[Call]:
        return [
            ast.Assign(
                targets=[
                    ast.Tuple(
                        elts=[
                            ast.Tuple(
                                elts=[
                                    ast.Name(id="X_train"),
                                    ast.Name(id="y_train"),
                                ],
                            ),
                            ast.Tuple(
                                elts=[
                                    ast.Name(id="X_test"),
                                    ast.Name(id="y_test"),
                                ],
                            ),
                        ],

                    )
                ],
                value=ast.Call(
                    func=ast.Name(id="get_test_data"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="num_train", value=ast.Constant(value=num_train)),
                        ast.keyword(arg="num_test", value=ast.Constant(value=num_test)),
                        ast.keyword(
                            arg="input_shape",
                            value=ast.Tuple(elts=[ast.Constant(value=5)]),
                        ),
                        ast.keyword(arg="classification", value=ast.Constant(value=True)),
                        ast.keyword(arg="num_classes", value=ast.Constant(value=3)),
                    ],
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="reg")],
                value=ast.Call(
                    func=ast.Name(id="KerasRegressor"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="build_fn", value=ast.Name(id="build_fn_reg")),
                        ast.keyword(arg="hidden_dims", value=ast.Name(id="hidden_dims")),
                        ast.keyword(arg="batch_size", value=ast.Name(id="batch_size")),
                        ast.keyword(arg="epochs", value=ast.Name(id="epochs"))
                    ]
                ),
                lineno=2,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="reg"),
                        attr="fit",

                    ),
                    args=[
                        ast.Name(id="X_train"),
                        ast.Name(id="y_train")
                    ],
                    keywords=[
                        ast.keyword(arg="batch_size", value=ast.Name(id="batch_size")),
                        ast.keyword(arg="epochs", value=ast.Name(id="epochs"))
                    ]
                )
            ),
            ast.Assign(
                targets=[ast.Name(id="preds")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="reg"),
                        attr="predict",

                    ),
                    args=[
                        ast.Subscript(
                            value=ast.Name(id="X_test"),
                            slice=ast.Slice(
                                lower=None,
                                upper=ast.Constant(value=1),
                                step=None
                            ),

                        )
                    ],
                    keywords=[
                        ast.keyword(arg="batch_size", value=ast.Name(id="batch_size"))
                    ]
                ),
                lineno=3

            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Attribute(
                        value=ast.Name(id="preds"),
                        attr="shape",

                    ),
                    ops=[ast.Eq()],
                    comparators=[
                        ast.Tuple(
                            elts=[],

                        )
                    ]
                ),
                msg=None
            )
        ]

    @staticmethod
    def _get_assert2(num_train: int, num_test: int, result: int) -> list[Call]:
        return [
            ast.Assign(
                targets=[
                    ast.Tuple(
                        elts=[
                            ast.Tuple(
                                elts=[
                                    ast.Name(id="X_train"),
                                    ast.Name(id="y_train"),
                                ],
                            ),
                            ast.Tuple(
                                elts=[
                                    ast.Name(id="X_test"),
                                    ast.Name(id="y_test"),
                                ],
                            ),
                        ],

                    )
                ],
                value=ast.Call(
                    func=ast.Name(id="get_test_data"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="num_train", value=ast.Constant(value=num_train)),
                        ast.keyword(arg="num_test", value=ast.Constant(value=num_test)),
                        ast.keyword(
                            arg="input_shape",
                            value=ast.Tuple(elts=[ast.Constant(value=5)]),
                        ),
                        ast.keyword(arg="classification", value=ast.Constant(value=True)),
                        ast.keyword(arg="num_classes", value=ast.Constant(value=3)),
                    ],
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="reg")],
                value=ast.Call(
                    func=ast.Name(id="KerasRegressor"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="build_fn", value=ast.Name(id="build_fn_reg")),
                        ast.keyword(arg="hidden_dims", value=ast.Name(id="hidden_dims")),
                        ast.keyword(arg="batch_size", value=ast.Name(id="batch_size")),
                        ast.keyword(arg="epochs", value=ast.Name(id="epochs"))
                    ]
                ),
                lineno=2,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="reg"),
                        attr="fit",

                    ),
                    args=[
                        ast.Name(id="X_train"),
                        ast.Name(id="y_train")
                    ],
                    keywords=[
                        ast.keyword(arg="batch_size", value=ast.Name(id="batch_size")),
                        ast.keyword(arg="epochs", value=ast.Name(id="epochs"))
                    ]
                )
            ),
            ast.Assign(
                targets=[ast.Name(id="preds")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="reg"),
                        attr="predict",

                    ),
                    args=[
                        ast.Subscript(
                            value=ast.Name(id="X_test"),
                            slice=ast.Slice(
                                lower=None,
                                upper=ast.Constant(value=1),
                                step=None
                            ),

                        )
                    ],
                    keywords=[
                        ast.keyword(arg="batch_size", value=ast.Name(id="batch_size"))
                    ]
                ),
                lineno=3

            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Attribute(
                        value=ast.Name(id="preds"),
                        attr="shape",

                    ),
                    ops=[ast.Eq()],
                    comparators=[
                        ast.Tuple(
                            elts=[ast.Constant(value=result)],

                        )
                    ]
                ),
                msg=None
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="keras.wrappers.scikit_learn",
                names=[ast.alias(name="KerasRegressor")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.utils.test_utils",
                names=[ast.alias(name="get_test_data")],
                level=0,
            ),
            ast.ImportFrom(
                module="tests.keras.wrappers.scikit_learn_test",
                names=[ast.alias(name="epochs"), ast.alias(name="batch_size"), ast.alias(name="hidden_dims"),
                       ast.alias(name="build_fn_reg")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        num_train, num_test, result = fail_
        test = self.get_empty_test()
        test.body = self._get_assert2(num_train, num_test, result)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        num_train, num_test = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(num_train, num_test)
        return test, TestResult.PASSING


class KerasUnittestGenerator8(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy8_generate)

    @staticmethod
    def _get_assert(value1: int, value2: int) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="input_shape")],
                value=ast.Tuple(elts=[ast.Constant(value=1), ast.Constant(value=value1)]),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="input_layer")],
                value=ast.Call(
                    func=ast.Name(id="Input"),
                    args=[],
                    keywords=[ast.keyword(arg="shape", value=ast.Name(id="input_shape"))],
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id="A")],
                value=ast.Call(
                    func=ast.Name(id="Dense"),
                    args=[ast.Constant(value=12)],
                    keywords=[ast.keyword(arg="name", value=ast.Constant(value="layer_a"))],
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id="r1")],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="layers"), attr="Reshape"),
                        args=[ast.Tuple(elts=[ast.Constant(value=value1)])],
                        keywords=[],
                    ),
                    args=[ast.Name(id="input_layer")],
                    keywords=[],
                ),
                lineno=4
            ),
            ast.Assign(
                targets=[ast.Name(id="Aout1")],
                value=ast.Call(func=ast.Name(id="A"), args=[ast.Name(id="r1")], keywords=[]),
                lineno=5
            ),
            ast.Assign(
                targets=[ast.Name(id="r2")],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="layers"), attr="Reshape"),
                        args=[ast.Tuple(elts=[ast.Constant(value=value2)])],
                        keywords=[],
                    ),
                    args=[ast.Name(id="input_layer")],
                    keywords=[],
                ),
                lineno=6
            ),
            ast.Assign(
                targets=[ast.Name(id="Aout2")],
                value=ast.Call(func=ast.Name(id="A"), args=[ast.Name(id="r2")], keywords=[]),
                lineno=7
            ),
            ast.Assign(
                targets=[ast.Name(id="c1")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="layers"), attr="concatenate"),
                    args=[
                        ast.List(elts=[ast.Name(id="Aout2"), ast.Name(id="Aout1")]),
                    ],
                    keywords=[],
                ),
                lineno=8
            ),
            ast.Assign(
                targets=[ast.Name(id="output")],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Name(id="Dense"),
                        args=[ast.Constant(value=2)],
                        keywords=[
                            ast.keyword(arg="name", value=ast.Constant(value="layer_b"))
                        ],
                    ),
                    args=[ast.Name(id="c1")],
                    keywords=[],
                ),
                lineno=9
            ),
            ast.Assign(
                targets=[ast.Name(id="M")],
                value=ast.Call(
                    func=ast.Name(id="Model"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="inputs", value=ast.Name(id="input_layer")),
                        ast.keyword(arg="outputs", value=ast.Name(id="output")),
                    ],
                ),
                lineno=10
            ),
            ast.Assign(
                targets=[ast.Name(id="x_val")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id="np"), attr="random"
                        ),
                        attr="random",
                    ),
                    args=[
                        ast.BinOp(
                            left=ast.Tuple(elts=[ast.Constant(value=10)]),
                            op=ast.Add(),
                            right=ast.Name(id="input_shape"),
                        )
                    ],
                    keywords=[],
                ),
                lineno=11
            ),
            ast.Assign(
                targets=[ast.Name(id="output_val")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M"), attr="predict"),
                    args=[ast.Name(id="x_val")],
                    keywords=[],
                ),
                lineno=12
            ),
            ast.Assign(
                targets=[ast.Name(id="config")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M"), attr="get_config"),
                    args=[],
                    keywords=[],
                ),
                lineno=13
            ),
            ast.Assign(
                targets=[ast.Name(id="weights")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M"), attr="get_weights"),
                    args=[],
                    keywords=[],
                ),
                lineno=14
            ),
            ast.Assign(
                targets=[ast.Name(id="M2")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="Model"), attr="from_config"),
                    args=[ast.Name(id="config")],
                    keywords=[],
                ),
                lineno=15
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M2"), attr="set_weights"),
                    args=[ast.Name(id="weights")],
                    keywords=[],
                ),
                lineno=16
            ),
            ast.Assign(
                targets=[ast.Name(id="output_val_2")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M2"), attr="predict"),
                    args=[ast.Name(id="x_val")],
                    keywords=[],
                ),
                lineno=17
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="np"), attr="testing"),
                        attr="assert_allclose",
                    ),
                    args=[ast.Name(id="output_val"), ast.Name(id="output_val_2")],
                    keywords=[
                        ast.keyword(arg="atol", value=ast.Constant(value=1e-6)),
                    ],
                ),
                lineno=18
            )
        ]

    @staticmethod
    def _get_assert2(value1: int, value2: int) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="input_shape")],
                value=ast.Tuple(elts=[ast.Constant(value=1), ast.Constant(value=value1)]),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="input_layer")],
                value=ast.Call(
                    func=ast.Name(id="Input"),
                    args=[],
                    keywords=[ast.keyword(arg="shape", value=ast.Name(id="input_shape"))],
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id="A")],
                value=ast.Call(
                    func=ast.Name(id="Dense"),
                    args=[ast.Constant(value=12)],
                    keywords=[ast.keyword(arg="name", value=ast.Constant(value="layer_a"))],
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id="r1")],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="layers"), attr="Reshape"),
                        args=[ast.Tuple(elts=[ast.Constant(value=value1)])],
                        keywords=[],
                    ),
                    args=[ast.Name(id="input_layer")],
                    keywords=[],
                ),
                lineno=4
            ),
            ast.Assign(
                targets=[ast.Name(id="Aout1")],
                value=ast.Call(func=ast.Name(id="A"), args=[ast.Name(id="r1")], keywords=[]),
                lineno=5
            ),
            ast.Assign(
                targets=[ast.Name(id="r2")],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="layers"), attr="Reshape"),
                        args=[ast.Tuple(elts=[ast.Constant(value=value2)])],
                        keywords=[],
                    ),
                    args=[
                        ast.Call(func=ast.Name(id="A"), args=[ast.Name(id="input_layer")], keywords=[], )
                    ],
                    keywords=[],
                ),
                lineno=6
            ),
            ast.Assign(
                targets=[ast.Name(id="Aout2")],
                value=ast.Call(func=ast.Name(id="A"), args=[ast.Name(id="r2")], keywords=[]),
                lineno=7
            ),
            ast.Assign(
                targets=[ast.Name(id="c1")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="layers"), attr="concatenate"),
                    args=[
                        ast.List(elts=[ast.Name(id="Aout2"), ast.Name(id="Aout1")]),
                    ],
                    keywords=[],
                ),
                lineno=8
            ),
            ast.Assign(
                targets=[ast.Name(id="output")],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Name(id="Dense"),
                        args=[ast.Constant(value=2)],
                        keywords=[
                            ast.keyword(arg="name", value=ast.Constant(value="layer_b"))
                        ],
                    ),
                    args=[ast.Name(id="c1")],
                    keywords=[],
                ),
                lineno=9
            ),
            ast.Assign(
                targets=[ast.Name(id="M")],
                value=ast.Call(
                    func=ast.Name(id="Model"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="inputs", value=ast.Name(id="input_layer")),
                        ast.keyword(arg="outputs", value=ast.Name(id="output")),
                    ],
                ),
                lineno=10
            ),
            ast.Assign(
                targets=[ast.Name(id="x_val")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id="np"), attr="random"
                        ),
                        attr="random",
                    ),
                    args=[
                        ast.BinOp(
                            left=ast.Tuple(elts=[ast.Constant(value=10)]),
                            op=ast.Add(),
                            right=ast.Name(id="input_shape"),
                        )
                    ],
                    keywords=[],
                ),
                lineno=11
            ),
            ast.Assign(
                targets=[ast.Name(id="output_val")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M"), attr="predict"),
                    args=[ast.Name(id="x_val")],
                    keywords=[],
                ),
                lineno=12
            ),
            ast.Assign(
                targets=[ast.Name(id="config")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M"), attr="get_config"),
                    args=[],
                    keywords=[],
                ),
                lineno=13
            ),
            ast.Assign(
                targets=[ast.Name(id="weights")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M"), attr="get_weights"),
                    args=[],
                    keywords=[],
                ),
                lineno=14
            ),
            ast.Assign(
                targets=[ast.Name(id="M2")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="Model"), attr="from_config"),
                    args=[ast.Name(id="config")],
                    keywords=[],
                ),
                lineno=15
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M2"), attr="set_weights"),
                    args=[ast.Name(id="weights")],
                    keywords=[],
                ),
                lineno=16
            ),
            ast.Assign(
                targets=[ast.Name(id="output_val_2")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="M2"), attr="predict"),
                    args=[ast.Name(id="x_val")],
                    keywords=[],
                ),
                lineno=17
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="np"), attr="testing"),
                        attr="assert_allclose",
                    ),
                    args=[ast.Name(id="output_val"), ast.Name(id="output_val_2")],
                    keywords=[
                        ast.keyword(arg="atol", value=ast.Constant(value=1e-6)),
                    ],
                ),
                lineno=18
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="layers")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.models",
                names=[ast.alias(name="Model")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.engine",
                names=[ast.alias(name="Input")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.layers",
                names=[ast.alias(name="Dense")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        value1, value2 = fail_
        test = self.get_empty_test()
        test.body = self._get_assert2(value1, value2)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        value1, value2 = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(value1, value2)
        return test, TestResult.PASSING


class KerasUnittestGenerator9(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy9_generate)

    @staticmethod
    def _get_assert(value: Any) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="docs_descriptor")],
                value=ast.Constant(value=value),
                lineno=2,
            ),
            ast.Assign(
                targets=[ast.Name(id="docstring")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="autogen"),
                        attr="process_docstring"),
                    args=[
                        ast.Subscript(
                            value=ast.Name(id="docs_descriptor"),
                            slice=ast.Index(value=ast.Constant(value="doc")))
                    ],
                    keywords=[],
                ),
                lineno=1
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Call(
                            func=ast.Name(id="markdown"),
                            args=[ast.Name(id="docstring")],
                            keywords=[]
                        ),
                        ast.Call(
                            func=ast.Name(id="markdown"),
                            args=[
                                ast.Subscript(
                                    value=ast.Name(id="docs_descriptor"),
                                    slice=ast.Index(value=ast.Constant(value="result")))
                            ],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                )
            ),
            # ast.Assert(
            #     test=ast.Compare(
            #         left=ast.Call(
            #             func=ast.Name(id="markdown"),
            #             args=[ast.Name(id="docstring")],
            #             keywords=[],
            #         ),
            #         ops=[ast.Eq()],
            #         comparators=[
            #             ast.Call(
            #                 func=ast.Name(id="markdown"),
            #                 args=[
            #                     ast.Subscript(
            #                         value=ast.Name(id="docs_descriptor"),
            #                         slice=ast.Index(value=ast.Constant(value="result")))
            #                 ],
            #                 keywords=[],
            #             )
            #         ],
            #     ),
            #     msg=None,
            # )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="markdown",
                names=[ast.alias(name="markdown")],
                level=0,
            ),
            ast.ImportFrom(
                module="docs",
                names=[ast.alias(name="autogen")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class KerasUnittestGenerator10(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy10_generate)

    @staticmethod
    def _get_assert(value1: int, value2: int, value3: int, value4: int, value5: int, value6: Any) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id='y')],
                value=ast.Call(
                    func=ast.Name(id='np.array'),
                    args=[ast.Constant(value=value6)],
                    keywords=[]
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id='sample_weights')],
                value=ast.Call(
                    func=ast.Name(id='np.array'),
                    args=[ast.List(
                        elts=[
                            ast.Constant(value=value1),
                            ast.Constant(value=value2),
                            ast.Constant(value=value3),
                            ast.Constant(value=value4),
                            ast.Constant(value=value5)
                        ],

                    )],
                    keywords=[]
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id='class_weights')],
                value=ast.Dict(
                    keys=[
                        ast.Constant(value=0),
                        ast.Constant(value=1),
                        ast.Constant(value=2),
                        ast.Constant(value=3),
                        ast.Constant(value=4)
                    ],
                    values=[
                        ast.Constant(value=value1),
                        ast.Constant(value=value2),
                        ast.Constant(value=value3),
                        ast.Constant(value=value4),
                        ast.Constant(value=value5)
                    ]
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id='weights')],
                value=ast.Call(
                    func=ast.Name(id='training_utils.standardize_weights'),
                    args=[
                        ast.Name(id='y'),
                        ast.Name(id='sample_weights')
                    ],
                    keywords=[]
                ),
                lineno=4
            ),
            ast.Assert(
                test=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='np'),
                        attr='allclose',

                    ),
                    args=[
                        ast.Name(id='weights'),
                        ast.Name(id='sample_weights')
                    ],
                    keywords=[]
                )
            ),
            ast.Assign(
                targets=[ast.Name(id='weights')],
                value=ast.Call(
                    func=ast.Name(id='training_utils.standardize_weights'),
                    args=[
                        ast.Name(id='y')
                    ],
                    keywords=[
                        ast.keyword(arg='class_weight', value=ast.Name(id='class_weights'))
                    ]
                ),
                lineno=5
            ),
            ast.Assert(
                test=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='np'),
                        attr='allclose',

                    ),
                    args=[
                        ast.Name(id='weights'),
                        ast.Call(
                            func=ast.Name(id='np.array'),
                            args=[ast.List(
                                elts=[
                                    ast.Constant(value=value1),
                                    ast.Constant(value=value2),
                                    ast.Constant(value=value3),
                                    ast.Constant(value=value4),
                                    ast.Constant(value=value5)
                                ],
                            )],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                )
            )
        ]

    @staticmethod
    def _get_assert2(value1: int, value2: int, value3: int, value4: int, value5: int, value6: Any) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id='y')],
                value=ast.Call(
                    func=ast.Name(id='np.array'),
                    args=[ast.Constant(value=value6)],
                    keywords=[]
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id='sample_weights')],
                value=ast.Call(
                    func=ast.Name(id='np.array'),
                    args=[ast.List(
                        elts=[
                            ast.Constant(value=value1),
                            ast.Constant(value=value2),
                            ast.Constant(value=value3),
                            ast.Constant(value=value4),
                            ast.Constant(value=value5)
                        ],

                    )],
                    keywords=[]
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id='class_weights')],
                value=ast.Dict(
                    keys=[
                        ast.Constant(value=0),
                        ast.Constant(value=1),
                        ast.Constant(value=2)
                    ],
                    values=[
                        ast.Constant(value=value1),
                        ast.Constant(value=value2),
                        ast.Constant(value=value3),
                        ast.Constant(value=value4),
                        ast.Constant(value=value5)
                    ]
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id='weights')],
                value=ast.Call(
                    func=ast.Name(id='training_utils.standardize_weights'),
                    args=[
                        ast.Name(id='y'),
                        ast.Name(id='sample_weights')
                    ],
                    keywords=[]
                ),
                lineno=4
            ),
            ast.Assert(
                test=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='np'),
                        attr='allclose',

                    ),
                    args=[
                        ast.Name(id='weights'),
                        ast.Name(id='sample_weights')
                    ],
                    keywords=[]
                )
            ),
            ast.Assign(
                targets=[ast.Name(id='weights')],
                value=ast.Call(
                    func=ast.Name(id='training_utils.standardize_weights'),
                    args=[
                        ast.Name(id='y')
                    ],
                    keywords=[
                        ast.keyword(arg='class_weight', value=ast.Name(id='class_weights'))
                    ]
                ),
                lineno=5
            ),
            ast.Assert(
                test=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='np'),
                        attr='allclose',

                    ),
                    args=[
                        ast.Name(id='weights'),
                        ast.Call(
                            func=ast.Name(id='np.array'),
                            args=[ast.List(
                                elts=[
                                    ast.Constant(value=value1),
                                    ast.Constant(value=value2),
                                    ast.Constant(value=value3),
                                    ast.Constant(value=value4),
                                    ast.Constant(value=value5)
                                ],
                            )],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                )
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.engine",
                names=[ast.alias(name="training_utils")],
                level=0,
            )

        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        value1, value2, value3, value4, value5, value6 = fail_
        test = self.get_empty_test()
        test.body = self._get_assert2(value1, value2, value3, value4, value5, value6)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        value1, value2, value3, value4, value5, value6 = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(value1, value2, value3, value4, value5, value6)
        return test, TestResult.PASSING


class KerasUnittestGenerator11(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy11_generate)

    @staticmethod
    def _get_assert() -> list[Call]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="np"), attr="random"), attr="seed"),
                    args=[ast.Constant(value=1337)],
                    keywords=[]
                ),
                lineno=1,
            ),
            ast.Assign(
                targets=[ast.Name(id="img_gen")],
                value=ast.Call(
                    func=ast.Name(id="ImageDataGenerator"),
                    args=[],
                    keywords=[ast.keyword(arg="rescale", value=ast.Constant(value=1.0))],
                ),
                lineno=2,
            ),
            ast.Assign(
                targets=[ast.Name(id="input_shape")],
                value=ast.Tuple(elts=[ast.Constant(value=16), ast.Constant(value=16), ast.Constant(value=3)],
                                ),
                lineno=3,
            ),
            ast.Assign(
                targets=[
                    ast.Tuple(elts=[ast.Name(id="x_train"), ast.Name(id="y_train")],
                              ),
                    ast.Tuple(elts=[ast.Name(id="x_test"), ast.Name(id="y_test")],
                              )
                ],
                value=ast.Call(
                    func=ast.Name(id="get_test_data"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="num_train", value=ast.Constant(value=500)),
                        ast.keyword(arg="num_test", value=ast.Constant(value=200)),
                        ast.keyword(arg="input_shape", value=ast.Name(id="input_shape")),
                        ast.keyword(arg="classification", value=ast.Constant(value=True)),
                        ast.keyword(arg="num_classes", value=ast.Constant(value=4))
                    ]
                ),
                lineno=4,
            ),
            ast.Assign(
                targets=[ast.Name(id="y_train")],
                value=ast.Call(
                    func=ast.Name(id="to_categorical"),
                    args=[ast.Name(id="y_train")],
                    keywords=[]
                ),
                lineno=5,
            ),
            ast.Assign(
                targets=[ast.Name(id="y_test")],
                value=ast.Call(
                    func=ast.Name(id="to_categorical"),
                    args=[ast.Name(id="y_test")],
                    keywords=[]
                ),
                lineno=6,
            ),
            ast.Assign(
                targets=[ast.Name(id="model")],
                value=ast.Call(
                    func=ast.Name(id="Sequential"),
                    args=[
                        ast.List(elts=[
                            ast.Call(
                                func=ast.Attribute(value=ast.Name(id="layers"), attr="Conv2D"),
                                args=[],
                                keywords=[
                                    ast.keyword(arg="filters", value=ast.Constant(value=8)),
                                    ast.keyword(arg="kernel_size", value=ast.Constant(value=3)),
                                    ast.keyword(arg="activation", value=ast.Constant(value="relu")),
                                    ast.keyword(arg="input_shape", value=ast.Name(id="input_shape"))
                                ]
                            ),
                            ast.Call(
                                func=ast.Attribute(value=ast.Name(id="layers"), attr="MaxPooling2D"),
                                args=[],
                                keywords=[
                                    ast.keyword(arg="pool_size", value=ast.Constant(value=2))
                                ]
                            ),
                            ast.Call(
                                func=ast.Attribute(value=ast.Name(id="layers"), attr="Conv2D"),
                                args=[],
                                keywords=[
                                    ast.keyword(arg="filters", value=ast.Constant(value=4)),
                                    ast.keyword(arg="kernel_size",
                                                value=ast.Tuple(elts=[ast.Constant(value=3), ast.Constant(value=3)],
                                                                )),
                                    ast.keyword(arg="activation", value=ast.Constant(value="relu")),
                                    ast.keyword(arg="padding", value=ast.Constant(value="same"))
                                ]
                            ),
                            ast.Call(
                                func=ast.Attribute(value=ast.Name(id="layers"),
                                                   attr="GlobalAveragePooling2D"),
                                args=[],
                                keywords=[]
                            ),
                            ast.Call(
                                func=ast.Attribute(value=ast.Name(id="layers"), attr="Dense"),
                                args=[],
                                keywords=[
                                    ast.keyword(arg="units", value=ast.Subscript(
                                        value=ast.Attribute(value=ast.Name(id="y_test"), attr="shape"),
                                        slice=ast.Index(
                                            value=ast.UnaryOp(op=ast.USub(), operand=ast.Constant(value=1))),

                                    )),
                                    ast.keyword(arg="activation", value=ast.Constant(value="softmax"))
                                ]
                            )
                        ])
                    ],
                    keywords=[]
                ),
                lineno=7,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="compile"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="loss", value=ast.Constant(value="categorical_crossentropy")),
                        ast.keyword(arg="optimizer", value=ast.Constant(value="rmsprop")),
                        ast.keyword(arg="metrics",
                                    value=ast.List(elts=[ast.Constant(value="accuracy")]))
                    ]
                ),
                lineno=8,
            ),
            ast.Assign(
                targets=[ast.Name(id="history")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="fit_generator"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(value=ast.Name(id="img_gen"), attr="flow"),
                            args=[
                                ast.Name(id="x_train"),
                                ast.Name(id="y_train")
                            ],
                            keywords=[
                                ast.keyword(arg="batch_size", value=ast.Constant(value=16))
                            ]
                        )
                    ],
                    keywords=[
                        ast.keyword(arg="epochs", value=ast.Constant(value=10)),
                        ast.keyword(arg="validation_data", value=ast.Call(
                            func=ast.Attribute(value=ast.Name(id="img_gen"), attr="flow"),
                            args=[
                                ast.Name(id="x_test"),
                                ast.Name(id="y_test")
                            ],
                            keywords=[
                                ast.keyword(arg="batch_size", value=ast.Constant(value=16))
                            ]
                        )),
                        ast.keyword(arg="verbose", value=ast.Constant(value=0))
                    ]
                ),
                lineno=9,
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Subscript(
                        value=ast.Attribute(value=ast.Name(id="history"), attr="history"),
                        slice=ast.Index(value=ast.Constant(value="val_acc")),

                    ),
                    ops=[ast.Gt()],
                    comparators=[ast.Constant(value=0.75)]
                ),
                msg=None,
                lineno=10,
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="model"), attr="evaluate_generator"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(value=ast.Name(id="img_gen"), attr="flow"),
                            args=[
                                ast.Name(id="x_train"),
                                ast.Name(id="y_train")
                            ],
                            keywords=[
                                ast.keyword(arg="batch_size", value=ast.Constant(value=16))
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=11,
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.models",
                names=[ast.alias(name="Sequential")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.utils.np_utils",
                names=[ast.alias(name="to_categorical")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="layers")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.preprocessing.image",
                names=[ast.alias(name="ImageDataGenerator")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.utils.test_utils",
                names=[ast.alias(name="get_test_data")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class KerasUnittestGenerator12(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy12_generate)

    @staticmethod
    def _get_assert(value: Any, randomise: int) -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="y_a")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="K"),
                        attr="variable"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(
                                    value=ast.Name(id="np"),
                                    attr="random"
                                ),
                                attr="randint"
                            ),
                            args=[
                                ast.Constant(value=0),
                                ast.Constant(value=randomise),
                                ast.Constant(value=value)
                                # (6,)
                                # (6, 3)
                                # (6, 3, 1)
                            ],
                            keywords=[]
                        )
                    ],
                    keywords=[
                        ast.keyword(
                            arg="dtype",
                            value=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="K"),
                                    attr="floatx"
                                ),
                                args=[],
                                keywords=[]
                            )
                        )
                    ]
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="y_b_shape")],
                value=ast.BinOp(
                    left=ast.Constant(value=value),
                    # (6,)
                    # (6, 3)
                    # (6, 3, 1)
                    op=ast.Add(),
                    right=ast.Tuple(
                        elts=[ast.Constant(value=randomise)],

                    )
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id="y_b")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="K"),
                        attr="variable"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(
                                    value=ast.Name(id="np"),
                                    attr="random"
                                ),
                                attr="random"
                            ),
                            args=[ast.Name(id="y_b_shape")],
                            keywords=[]
                        )
                    ],
                    keywords=[
                        ast.keyword(
                            arg="dtype",
                            value=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="K"),
                                    attr="floatx"
                                ),
                                args=[],
                                keywords=[]
                            )
                        )
                    ]
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id="y_a_dense_labels")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="K"),
                        attr="cast"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="K"),
                                attr="one_hot"
                            ),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id="K"),
                                        attr="cast"
                                    ),
                                    args=[
                                        ast.Name(id="y_a")
                                    ],
                                    keywords=[
                                        ast.keyword(arg="dtype", value=ast.Constant(value="int32"))
                                    ]
                                ),
                                ast.Constant(value=7)
                            ],
                            keywords=[]
                        )
                    ],
                    keywords=[
                        ast.keyword(arg="dtype", value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="K"),
                                attr="floatx"
                            ),
                            args=[],
                            keywords=[]
                        ))
                    ]
                ),
                lineno=4
            ),
            ast.Assign(
                targets=[ast.Name(id="sparse_categorical_acc")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="metrics"),
                        attr="sparse_categorical_accuracy"
                    ),
                    args=[
                        ast.Name(id="y_a"),
                        ast.Name(id="y_b")
                    ],
                    keywords=[]
                ),
                lineno=5
            ),
            ast.Assign(
                targets=[ast.Name(id="categorical_acc")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="metrics"),
                        attr="categorical_accuracy"
                    ),
                    args=[
                        ast.Name(id="y_a_dense_labels"),
                        ast.Name(id="y_b")
                    ],
                    keywords=[]
                ),
                lineno=6
            ),
            ast.Assert(
                test=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="np"),
                        attr="allclose"
                    ),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="K"),
                                attr="eval"
                            ),
                            args=[ast.Name(id="sparse_categorical_acc")],
                            keywords=[]
                        ),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="K"),
                                attr="eval"
                            ),
                            args=[ast.Name(id="categorical_acc")],
                            keywords=[]
                        )
                    ],
                    keywords=[]
                ),
                msg=None,
                lineno=7
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="backend", asname="K"), ast.alias(name="metrics")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        value, randomise = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(value, randomise)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        value, randomise = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(value, randomise)
        return test, TestResult.PASSING


class KerasUnittestGenerator13(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy13_generate)

    @staticmethod
    def _get_assert() -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="a")],
                value=ast.Call(
                    func=ast.Name(id="Input"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="shape", value=ast.Tuple(elts=[ast.Constant(value=3)])),
                        ast.keyword(arg="name", value=ast.Constant(value="input_a"))
                    ]
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="b")],
                value=ast.Call(
                    func=ast.Name(id="Input"),
                    args=[],
                    keywords=[
                        ast.keyword(arg="shape", value=ast.Tuple(elts=[ast.Constant(value=3)])),
                        ast.keyword(arg="name", value=ast.Constant(value="input_b"))
                    ]
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id="a_2")],
                value=ast.Call(
                    func=ast.Call(
                        func=ast.Name(id="Dense"),
                        args=[],
                        keywords=[
                            ast.keyword(arg="units", value=ast.Constant(value=4)),
                            ast.keyword(arg="name", value=ast.Constant(value="dense_1"))
                        ]
                    ),
                    args=[ast.Name(id="a")],
                    keywords=[]
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id="dp")],
                value=ast.Call(
                    func=ast.Name(id="Dropout"),
                    args=[ast.Constant(value=0.5)],
                    keywords=[
                        ast.keyword(arg="name", value=ast.Constant(value="dropout"))
                    ]
                ),
                lineno=4
            ),
            ast.Assign(
                targets=[ast.Name(id="b_2")],
                value=ast.Call(
                    func=ast.Name(id="dp"),
                    args=[ast.Name(id="b")],
                    keywords=[]
                ),
                lineno=5
            ),
            ast.Assign(
                targets=[ast.Name(id="model")],
                value=ast.Call(
                    func=ast.Name(id="Model"),
                    args=[
                        ast.List(elts=[ast.Name(id="a"), ast.Name(id="b")],
                                 ),
                        ast.List(elts=[ast.Name(id="a_2"), ast.Name(id="b_2")],
                                 )
                    ],
                    keywords=[]
                ),
                lineno=6
            ),
            ast.Assign(
                targets=[ast.Name(id="optimizer")],
                value=ast.Constant(value="rmsprop"),
                lineno=7
            ),
            ast.Assign(
                targets=[ast.Name(id="loss")],
                value=ast.Constant(value="mse"),
                lineno=8
            ),
            ast.Assign(
                targets=[ast.Name(id="loss_weights")],
                value=ast.List(elts=[ast.Constant(value=1.0), ast.Constant(value=0.5)]),
                lineno=9
            ),
            ast.Assign(
                targets=[ast.Name(id="input_a_np")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id="np"),
                            attr="random"
                        ),
                        attr="random"
                    ),
                    args=[
                        ast.Tuple(elts=[ast.Constant(value=10), ast.Constant(value=3)])
                    ],
                    keywords=[]
                ),
                lineno=10
            ),
            ast.Assign(
                targets=[ast.Name(id="input_b_np")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id="np"),
                            attr="random"
                        ),
                        attr="random"
                    ),
                    args=[
                        ast.Tuple(elts=[ast.Constant(value=10), ast.Constant(value=3)])
                    ],
                    keywords=[]
                ),
                lineno=11
            ),
            ast.Assign(
                targets=[ast.Name(id="output_a_np")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id="np"),
                            attr="random"
                        ),
                        attr="random"
                    ),
                    args=[
                        ast.Tuple(elts=[ast.Constant(value=10), ast.Constant(value=4)])
                    ],
                    keywords=[]
                ),
                lineno=12
            ),
            ast.Assign(
                targets=[ast.Name(id="output_b_np")],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id="np"),
                            attr="random"
                        ),
                        attr="random"
                    ),
                    args=[
                        ast.Tuple(elts=[ast.Constant(value=10), ast.Constant(value=3)])
                    ],
                    keywords=[]
                ),
                lineno=13
            ),
            ast.With(
                items=[
                    ast.withitem(
                        context_expr=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="pytest"),
                                attr="raises"
                            ),
                            args=[ast.Name(id="RuntimeError")],
                            keywords=[]
                        ),
                        optional_vars=None
                    )
                ],
                body=[
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="model"),
                                attr="train_on_batch"
                            ),
                            args=[
                                ast.List(elts=[
                                    ast.Name(id="input_a_np"),
                                    ast.Name(id="input_b_np")
                                ]),
                                ast.List(elts=[
                                    ast.Name(id="output_a_np"),
                                    ast.Name(id="output_b_np")
                                ])
                            ],
                            keywords=[]
                        ),
                        lineno=14
                    )
                ],
                lineno=14
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="backend")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="initializers")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class KerasUnittestGenerator14(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy14_generate)

    @staticmethod
    def _get_assert() -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="y_pred")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="K"), attr="variable"),
                    args=[ast.Name(id="y_pred")],
                    keywords=[]
                ),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="y_true")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="K"), attr="variable"),
                    args=[ast.Name(id="y_true")],
                    keywords=[]
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Name(id="success_result")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="K"), attr="eval"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="metrics"),
                                                                   attr="sparse_top_k_categorical_accuracy"),
                                               attr="__call__"),
                            args=[
                                ast.Name(id="y_true"),
                                ast.Name(id="y_pred")
                            ],
                            keywords=[
                                ast.keyword(arg="k", value=ast.Constant(value=3))
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=3
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Name(id="success_result"),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(value=1)]
                ),
                msg=None,
                lineno=4
            ),
            ast.Assign(
                targets=[ast.Name(id="partial_result")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="K"), attr="eval"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="metrics"),
                                                                   attr="sparse_top_k_categorical_accuracy"),
                                               attr="__call__"),
                            args=[
                                ast.Name(id="y_true"),
                                ast.Name(id="y_pred")
                            ],
                            keywords=[
                                ast.keyword(arg="k", value=ast.Constant(value=2))
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=5
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Name(id="partial_result"),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(value=0.5)]
                ),
                msg=None,
                lineno=6
            ),
            ast.Assign(
                targets=[ast.Name(id="failure_result")],
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="K"), attr="eval"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(value=ast.Attribute(value=ast.Name(id="metrics"),
                                                                   attr="sparse_top_k_categorical_accuracy"),
                                               attr="__call__"),
                            args=[
                                ast.Name(id="y_true"),
                                ast.Name(id="y_pred")
                            ],
                            keywords=[
                                ast.keyword(arg="k", value=ast.Constant(value=1))
                            ]
                        )
                    ],
                    keywords=[]
                ),
                lineno=7
            ),
            ast.Assert(
                test=ast.Compare(
                    left=ast.Name(id="failure_result"),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(value=0)]
                ),
                msg=None,
                lineno=8
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="backend")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="initializers")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class KerasUnittestGenerator15(
    python.PythonGenerator, UnittestGenerator, KerasTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy15_generate)

    @staticmethod
    def _get_assert() -> list[Call]:
        return [
            ast.Assign(
                targets=[ast.Name(id="num_classes")],
                value=ast.Constant(value=2),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="input_dim")],
                value=ast.Constant(value=2),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="train_samples")],
                value=ast.Constant(value=20),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id="test_samples")],
                value=ast.Constant(value=20),
                lineno=1
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
                        attr="seed"
                    ),
                    args=[ast.Constant(value=1337)],
                    keywords=[]
                ),
                lineno=1
            ),
            ast.With(
                items=[
                    ast.withitem(
                        context_expr=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="tempfile", ctx=ast.Load()),
                                attr="TemporaryDirectory",
                                ctx=ast.Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        optional_vars=ast.Name(id="tempdir", ctx=ast.Store()),
                    )
                ],
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="filepath", ctx=ast.Store())],
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(
                                    value=ast.Name(id="os", ctx=ast.Load()),
                                    attr="path",
                                    ctx=ast.Load()
                                ),
                                attr="join",
                                ctx=ast.Load()
                            ),
                            args=[
                                ast.Name(id="tempdir", ctx=ast.Load()),
                                ast.Constant(value="log.tsv")
                            ],
                            keywords=[]
                        ),
                        lineno=1
                    ),
                    ast.Assign(
                        targets=[ast.Name(id="sep", ctx=ast.Store())],
                        value=ast.Constant(value="\t"),
                        lineno=1

                    ),
                    ast.Assign(
                        targets=[
                            ast.Tuple(
                                elts=[
                                    ast.Tuple(
                                        elts=[
                                            ast.Name(id="X_train", ctx=ast.Store()),
                                            ast.Name(id="y_train", ctx=ast.Store()),
                                        ],
                                        ctx=ast.Store(),
                                    ),
                                    ast.Tuple(
                                        elts=[
                                            ast.Name(id="X_test", ctx=ast.Store()),
                                            ast.Name(id="y_test", ctx=ast.Store()),
                                        ],
                                        ctx=ast.Store(),
                                    ),
                                ],
                                ctx=ast.Store(),
                            )
                        ],
                        value=ast.Call(
                            func=ast.Name(id="get_test_data", ctx=ast.Load()),
                            args=[],
                            keywords=[
                                ast.keyword(arg="num_train", value=ast.Name(id="train_samples", ctx=ast.Load())),
                                ast.keyword(arg="num_test", value=ast.Name(id="test_samples", ctx=ast.Load())),
                                ast.keyword(
                                    arg="input_shape",
                                    value=ast.Tuple(elts=[ast.Name(id="input_dim", ctx=ast.Load())], ctx=ast.Load()),
                                ),
                                ast.keyword(arg="classification", value=ast.Constant(value=True)),
                                ast.keyword(arg="num_classes", value=ast.Name(id="num_classes", ctx=ast.Load())),
                            ],
                        ),
                        lineno=1

                    ),
                    ast.Assign(
                        targets=[ast.Name(id="y_test", ctx=ast.Store())],
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="np_utils", ctx=ast.Load()), attr="to_categorical", ctx=ast.Load()
                            ),
                            args=[ast.Name(id="y_test", ctx=ast.Load())],
                            keywords=[],
                        ),
                        lineno=1

                    ),
                    ast.Assign(
                        targets=[ast.Name(id="y_train", ctx=ast.Store())],
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="np_utils", ctx=ast.Load()), attr="to_categorical", ctx=ast.Load()
                            ),
                            args=[ast.Name(id="y_train", ctx=ast.Load())],
                            keywords=[],
                        ),
                        lineno=1

                    ),

                ],
                lineno=1

            )
            # ast.Assign(
            #     targets=[ast.Name(id="num_classes")],
            #     value=ast.Constant(value=2),
            #     lineno=1
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="input_dim")],
            #     value=ast.Constant(value=2),
            #     lineno=1
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="train_samples")],
            #     value=ast.Constant(value=20),
            #     lineno=1
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="test_samples")],
            #     value=ast.Constant(value=20),
            #     lineno=1
            # ),
            # ast.Expr(
            #     value=ast.Call(
            #         func=ast.Attribute(
            #             value=ast.Attribute(value=ast.Name(id="np"), attr="random"),
            #             attr="seed"
            #         ),
            #         args=[ast.Constant(value=1337)],
            #         keywords=[]
            #     ),
            #     lineno=1
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="filepath")],
            #     value=ast.Call(
            #         func=ast.Name(id="str"),
            #         args=[
            #             ast.BinOp(
            #                 left=ast.Name(id="tmpdir"),
            #                 op=ast.Div(),
            #                 right=ast.Constant(value="log.tsv")
            #             )
            #         ],
            #         keywords=[]
            #     ),
            #     lineno=2
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="sep")],
            #     value=ast.Constant(value="\t"),
            #     lineno=3
            # ),
            # ast.Assign(
            #     targets=[
            #         ast.Tuple(
            #             elts=[
            #                 ast.Tuple(
            #                     elts=[ast.Name(id="X_train"), ast.Name(id="y_train")],
            #                     ),
            #                 ast.Tuple(
            #                     elts=[ast.Name(id="X_test"), ast.Name(id="y_test")],
            #                     )
            #             ],
#
            #         )
            #     ],
            #     value=ast.Call(
            #         func=ast.Name(id="get_test_data"),
            #         args=[],
            #         keywords=[
            #             ast.keyword(arg="num_train", value=ast.Name(id="train_samples")),
            #             ast.keyword(arg="num_test", value=ast.Name(id="test_samples")),
            #             ast.keyword(arg="input_shape",
            #                         value=ast.Tuple(elts=[ast.Name(id="input_dim")])),
            #             ast.keyword(arg="classification", value=ast.Constant(value=True)),
            #             ast.keyword(arg="num_classes", value=ast.Name(id="num_classes"))
            #         ]
            #     ),
            #     lineno=4
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="y_test")],
            #     value=ast.Call(
            #         func=ast.Attribute(value=ast.Name(id="np_utils"), attr="to_categorical"),
            #         args=[ast.Name(id="y_test")],
            #         keywords=[]
            #     ),
            #     lineno=5
            # ),
            # ast.Assign(
            #     targets=[ast.Name(id="y_train")],
            #     value=ast.Call(
            #         func=ast.Attribute(value=ast.Name(id="np_utils"), attr="to_categorical"),
            #         args=[ast.Name(id="y_train")],
            #         keywords=[]
            #     ),
            #     lineno=6
            # )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.Import(
                module="numpy",
                names=[ast.alias(name="numpy", asname="np")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.utils.test_utils",
                names=[ast.alias(name="get_test_data")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras",
                names=[ast.alias(name="initializers")],
                level=0,
            ),
            ast.ImportFrom(
                module="keras.utils",
                names=[ast.alias(name="np_utils")],
                level=0,
            ),
            ast.Import(
                module="tempfile",
                names=[ast.alias(name="tempfile")],
                level=0,
            ),
            ast.Import(
                module="os",
                names=[ast.alias(name="os")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class KerasSystemtestGenerator1(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy1_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy1_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator2(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy2_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy2_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator3(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy3_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy3_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator4(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy4_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy4_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator5(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy5_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy5_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator6(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy6_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy6_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator7(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy7_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy7_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator8(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy8_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy8_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator9(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy9_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy9_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator10(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy10_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy10_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator11(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy11_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy11_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator12(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy12_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy12_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator13(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy13_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy13_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator14(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy14_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy14_generate)
        return f"{pass_}", TestResult.PASSING


class KerasSystemtestGenerator15(SystemtestGenerator, KerasTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy15_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy15_generate)
        return f"{pass_}", TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<structure_>"],
    "<structure_>": ["<str_int_sym_><structure_>"],
    "<str_int_sym_>": [
        "<string_><str_int_sym_>",
        "<integer_><str_int_sym_>",
        "<symbols_><str_int_sym_>",
        " ",
    ],
    "<string_>": ["<char_><string_>", "<char_>", ""],
    "<integer_>": ["<digit_><integer_>", "<digit_>", ""],
    "<symbols_>": ["<symbol_><symbols_>", "<symbol_>", ""],
    "<symbol_>": srange(string.punctuation),
    "<digit_>": srange(string.digits),
    "<char_>": srange(string.ascii_letters),
}
assert is_valid_grammar(grammar)
