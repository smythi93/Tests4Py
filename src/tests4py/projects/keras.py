from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Keras(Project):
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
            project_name="keras",
            github_url="https://github.com/keras-team/keras",
            status=Status.OK,
            cause="N.A.",
            python_version="3.7.3",
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
    Keras(
        bug_id=1,
        buggy_commit_id="331d5b0102ab0cc79cece1f03cc551d8105db3c9",
        fixed_commit_id="8e23a3ec47a2ccbf6cdd222a80886c6b9f17264f",
        test_file=[Path("tests", "keras", "initializers_test.py")],
        test_cases=["tests/keras/initializers_test.py::test_statefulness"],
    )
    Keras(
        bug_id=2,
        buggy_commit_id="2f55055a9f053b35fa721d3eb75dd07ea5a5f1e3",
        fixed_commit_id="c24d16af155e20976bdf61e468ba760408e676ff",
        test_file=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=["tests/keras/backend/backend_test.py::TestBackend::test_in_top_k"],
    )
    Keras(
        bug_id=3,
        buggy_commit_id="c0d1709cbae3d05efc6dd224230012bc120be8e5",
        fixed_commit_id="c13d2723d01212d09dfdda39b0ad439803ec9230",
        test_file=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            "tests/keras/test_sequential_model.py::test_clone_functional_model_with_multi_outputs"
        ],
    )
    Keras(
        bug_id=4,
        buggy_commit_id="b0bfd5201da2bfced84028bcc5bda05bdfd75af7",
        fixed_commit_id="4185cbb50bfcae9cc30b0fc7b67e81d67a50a8ac",
        test_file=[Path("tests", "keras", "optimizers_test.py")],
        test_cases=[
            "tests/keras/optimizers_test.py::test_tfoptimizer_pass_correct_named_params_to_native_tensorflow_optimizer"
        ],
    )
    Keras(
        bug_id=5,
        buggy_commit_id="b847b4601d608050bab6eccd049fce28b7bf1b1f",
        fixed_commit_id="e11c48d9ce3ee47bb8a966549b14cbd5b10ee70d",
        test_file=[Path("tests", "keras", "utils", "data_utils_test.py")],
        test_cases=["tests/keras/utils/data_utils_test.py::test_data_utils"],
    )
    Keras(
        bug_id=6,
        buggy_commit_id="88af7d0c97497b5c3a198ee9416b2accfbc72c36",
        fixed_commit_id="4b54657ab4806b0aaef8f8eeb973edb83c3d3483",
        test_file=[Path("tests", "test_loss_masking.py")],
        test_cases=["tests/test_loss_masking.py::test_masking_is_all_zeros"],
    )
    Keras(
        bug_id=7,
        buggy_commit_id="26b620fb37c885d60183f83abc744f43775ce75a",
        fixed_commit_id="c05ef1fd95a6024155ab59656fef8dac5a45c335",
        test_file=[Path("tests", "keras", "wrappers", "scikit_learn_test.py")],
        test_cases=[
            "tests/keras/wrappers/scikit_learn_test.py::test_regression_predict_shape_correct_num_test_1"
        ],
    )
    Keras(
        bug_id=8,
        buggy_commit_id="87540a2a2f42e00c4a2ca7ca35d19f96e62e6cb0",
        fixed_commit_id="d78c982b326adeed6ac25200dc6892ff8f518ca6",
        test_file=[Path("tests", "keras", "engine", "test_topology.py")],
        test_cases=[
            "tests/keras/engine/test_topology.py::test_layer_sharing_at_heterogeneous_depth_order"
        ],
    )
    Keras(
        bug_id=9,
        buggy_commit_id="0cd3b07eb5de1aaaad84d1ff7f7c2ed7dab4b23c",
        fixed_commit_id="0505393746d56ddacc34bb1c016dba79429c9ac9",
        test_file=[Path("tests", "test_doc_auto_generation.py")],
        test_cases=[
            "tests/test_doc_auto_generation.py::test_doc_lists[docs_descriptor1]"
        ],
    )
    Keras(
        bug_id=10,
        buggy_commit_id="8f41e41eda6e8ea96403cae5798a5a89c8bb5605",
        fixed_commit_id="c1c4afe60b1355a6c0e83577791a0423f37a3324",
        test_file=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=["tests/keras/engine/test_training.py::test_sample_weights"],
    )
    Keras(
        bug_id=11,
        buggy_commit_id="36b9e4c055f32718a036cabaf767325b010c7485",
        fixed_commit_id="d6b5c5ebb410e3366c9d7aca41977a60134bfe10",
        test_file=[Path("tests", "integration_tests", "test_image_data_tasks.py")],
        test_cases=[
            "tests/integration_tests/test_image_data_tasks.py::test_image_data_generator_training"
        ],
    )
    Keras(
        bug_id=12,
        buggy_commit_id="6dff721a3a8755356b2e89d02ef63ad8ab38ec95",
        fixed_commit_id="6dff721a3a8755356b2e89d02ef63ad8ab38ec95",
        test_file=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            "tests/keras/metrics_test.py::test_sparse_categorical_accuracy_correctness[shape1]",
            "tests/keras/metrics_test.py::test_sparse_categorical_accuracy_correctness[shape2]",
        ],
    )
    Keras(
        bug_id=13,
        buggy_commit_id="2bfd1f2c950df5fc3f40b903c1966f1b0a48bee4",
        fixed_commit_id="a07253d8269e1b750f0a64767cc9a07da8a3b7ea",
        test_file=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=["tests/keras/engine/test_training.py::test_model_methods"],
    )
    Keras(
        bug_id=14,
        buggy_commit_id="98465b85d020f1326bcef7632f1261a9a7a84e92",
        fixed_commit_id="02bc5010a04bb11c8e91835cc9775c8149dec754",
        test_file=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            "tests/keras/metrics_test.py::test_sparse_top_k_categorical_accuracy[y_pred1-y_true1]"
        ],
    )
    Keras(
        bug_id=15,
        buggy_commit_id="5b6243485acc20cc36f2db4f258512c332d691ec",
        fixed_commit_id="f60313e29657b2afb6a02f28dba5936bc0dd09e6",
        test_file=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=["tests/keras/test_callbacks.py::test_CSVLogger"],
    )
    Keras(
        bug_id=16,
        buggy_commit_id="514aca20c6f076a86819d7180f36c3b2e8bcc33b",
        fixed_commit_id="fe38f9dfc8c732a77ac03507b63c79b1d2acfba2",
        test_file=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            "tests/keras/test_sequential_model.py::test_sequential",
            "tests/keras/test_sequential_model.py::test_sequential_deferred_build",
        ],
    )
    Keras(
        bug_id=17,
        buggy_commit_id="c913b6da92f6ab9a3f4c897caa4085e782a14680",
        fixed_commit_id="5a6af4bc6d44e9adbc2a21804bfcd18c4ce849ef",
        test_file=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            "tests/keras/metrics_test.py::test_sparse_categorical_accuracy_correctness"
        ],
    )
    Keras(
        bug_id=18,
        buggy_commit_id="9400be98783135a1d42dd238f4e6c3aa048eceea",
        fixed_commit_id="244546c2fe5165b6770eb456afd5fac8878473c5",
        test_file=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            "tests/keras/backend/backend_test.py::TestBackend::test_function_tf_run_options_with_run_metadata"
        ],
    )
    Keras(
        bug_id=19,
        buggy_commit_id="f9210387088fe91b5bc8999cf0cb41a0fe9eacf6",
        fixed_commit_id="66f8cc7ac4942f7f9fe0164a2a854a6264b87735",
        test_file=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            "tests/keras/layers/recurrent_test.py::test_inconsistent_output_state_size",
            "tests/keras/layers/recurrent_test.py::test_minimal_rnn_cell_non_layer_multiple_states",
        ],
    )
    Keras(
        bug_id=20,
        buggy_commit_id="76da5f0a21ca98e4bf6706e182fb825243e76204",
        fixed_commit_id="6dd087ab73b09e449144ff17450cc14f981b9ac2",
        test_file=[Path("tests", "keras", "layers", "convolutional_test.py")],
        test_cases=[
            "tests/keras/layers/convolutional_test.py::test_conv2d_transpose_dilation"
        ],
    )
    Keras(
        bug_id=21,
        buggy_commit_id="c7b7328cc99fd5d7c298e57c6020043451d89a61",
        fixed_commit_id="1fc585adb57f20a2acf69f0cd08b731259b8d2f8",
        test_file=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            "tests/keras/test_callbacks.py::test_EarlyStopping_final_weights_when_restoring_model_weights"
        ],
    )
    Keras(
        bug_id=22,
        buggy_commit_id="54386efa549f850dff13f79fc3af67799a4e5d4f",
        fixed_commit_id="ee02d256611b17d11e37b86bd4f618d7f2a37d84",
        test_file=[Path("tests", "keras", "layers", "core_test.py")],
        test_cases=[
            "tests/keras/layers/core_test.py::test_sequential_as_downstream_of_masking_layer"
        ],
    )
    Keras(
        bug_id=23,
        buggy_commit_id="3dcd9c767ce6875fc8b69c74971ac8a552e23131",
        fixed_commit_id="69c30a150f0b2caee7961ca1c0080960ef5ad6f6",
        test_file=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            "tests/keras/test_sequential_model.py::test_nested_sequential_deferred_build"
        ],
    )
    Keras(
        bug_id=24,
        buggy_commit_id="d7884570b10951d156aa086ee29a4df9eab79cf3",
        fixed_commit_id="bcf0031b54d555179be81c088cc3df0a723d7907",
        test_file=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            "tests/keras/test_callbacks.py::test_TensorBoard_multi_input_output"
        ],
    )
    Keras(
        bug_id=25,
        buggy_commit_id="b470a595f7278acf5e7e47521edf25d3c4f479f1",
        fixed_commit_id="84e168b5fa55933e02e767ff7c86fcc0232aecc6",
        test_file=[Path("tests", "keras", "applications", "imagenet_utils_test.py")],
        test_cases=[
            "tests/keras/applications/imagenet_utils_test.py::test_preprocess_input"
        ],
    )
    Keras(
        bug_id=26,
        buggy_commit_id="87417470c8168772559be0531e297120c569a422",
        fixed_commit_id="97d5fa920e4f8248128f7c1b460fd9bb20d3478f",
        test_file=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            "tests/keras/backend/backend_test.py::TestBackend::test_rnn_additional_states"
        ],
    )
    Keras(
        bug_id=27,
        buggy_commit_id="49f5b931410bc2e56378f20a15e8ac919e0efb88",
        fixed_commit_id="b076e227da6beaf87d6c84eff1a92285e4662acf",
        test_file=[Path("tests", "keras", "layers", "wrappers_test.py")],
        test_cases=[
            "tests/keras/layers/wrappers_test.py::test_Bidirectional_updates",
            "tests/keras/layers/wrappers_test.py::test_Bidirectional_losses",
        ],
    )
    Keras(
        bug_id=28,
        buggy_commit_id="6171b3656ebd9b6038f709ba83f7475de284ba4e",
        fixed_commit_id="5422fdd38baad36730cb6aeb946e17eeae6a551c",
        test_file=[Path("tests", "keras", "preprocessing", "sequence_test.py")],
        test_cases=[
            "tests/keras/preprocessing/sequence_test.py::test_TimeSeriesGenerator_doesnt_miss_any_sample",
            "tests/keras/preprocessing/sequence_test.py::test_TimeseriesGenerator",
        ],
    )
    Keras(
        bug_id=29,
        buggy_commit_id="a341c014412cbfc86a9dd9816ae228e398dff3a2",
        fixed_commit_id="adc321b4d7a4e22f6bdb00b404dfe5e23d4887aa",
        test_file=[Path("tests", "keras", "metrics_test.py")],
        test_cases=["tests/keras/metrics_test.py::test_stateful_metrics[dict]"],
    )
    Keras(
        bug_id=30,
        buggy_commit_id="c08ef613af27da896cee168daeee5c6fad1980b6",
        fixed_commit_id="2c8d1d03599cc03243bce8f07ed9c4a3d5f384f9",
        test_file=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            "tests/keras/engine/test_training.py::test_model_with_external_loss"
        ],
    )
    Keras(
        bug_id=31,
        buggy_commit_id="ced81968b0e9d8b1389e6580721ac60d9cf3ca60",
        fixed_commit_id="e2a10a5e6e156a45e946c4d08db7133f997c1f9a",
        test_file=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=["tests/keras/backend/backend_test.py::TestBackend::test_ctc"],
    )
    Keras(
        bug_id=32,
        buggy_commit_id="a3d160b9467c99cbb27f9aa0382c759f45c8ee66",
        fixed_commit_id="709f791af201caaab4aa180bda259989087cfe47",
        test_file=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            "tests/keras/test_callbacks.py::test_ReduceLROnPlateau_patience",
            "tests/keras/test_callbacks.py::test_ReduceLROnPlateau_backwards_compatibility",
        ],
    )
    Keras(
        bug_id=33,
        buggy_commit_id="1c9a49781da2101507db23e2014e4e5d16bd2e52",
        fixed_commit_id="70ad0d6e4a569701ef106058397ad0540ec08340",
        test_file=[Path("tests", "keras", "preprocessing", "text_test.py")],
        test_cases=[
            "tests/keras/preprocessing/text_test.py::test_text_to_word_sequence_multichar_split",
            "tests/keras/preprocessing/text_test.py::test_text_to_word_sequence_unicode_multichar_split",
        ],
    )
    Keras(
        bug_id=34,
        buggy_commit_id="7ef5244a2f1f7f7b76e3c804b82cbb20cdf4d139",
        fixed_commit_id="4b74fc5418944c9f449eb88ed4b40ada280fa5ca",
        test_file=[Path("tests", "test_multiprocessing.py")],
        test_cases=["tests/test_multiprocessing.py::test_multiprocessing_training"],
    )
    Keras(
        bug_id=35,
        buggy_commit_id="06eaeebecfb73c23bfd531013ca172ee3bf5069c",
        fixed_commit_id="738819de0b7e6bc45abed8d0640f02b81c6ac4e9",
        test_file=[Path("tests", "keras", "preprocessing", "image_test.py")],
        test_cases=[
            "tests/keras/preprocessing/image_test.py::TestImage::test_directory_iterator"
        ],
    )
    Keras(
        bug_id=36,
        buggy_commit_id="85f011df5a5c0fcf1f01b39eca338eb6b7e58401",
        fixed_commit_id="fb1887d132a8ce8548ff53d868a6ba531cd63b34",
        test_file=[Path("tests", "keras", "layers", "convolutional_test.py")],
        test_cases=["tests/keras/layers/convolutional_test.py::test_separable_conv_1d"],
    )
    Keras(
        bug_id=37,
        buggy_commit_id="81f6b3aa5b2b6215a533180e848a3b4dff851d03",
        fixed_commit_id="1d2ad790dd43a2d702176c1170b2f3fd592a385a",
        test_file=[Path("tests", "keras", "layers", "wrappers_test.py")],
        test_cases=[
            "tests/keras/layers/wrappers_test.py::test_Bidirectional_state_reuse"
        ],
    )
    Keras(
        bug_id=38,
        buggy_commit_id="53ec990d54130dd0a457dd235c93d39de32d571d",
        fixed_commit_id="64f80d6077edd5f277a1181df94bf4510ea0517a",
        test_file=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            "tests/keras/layers/recurrent_test.py::test_minimal_rnn_cell_layer"
        ],
    )
    Keras(
        bug_id=39,
        buggy_commit_id="3a431ea52d090fb3ef8a1e0e5d7f796d9a42e097",
        fixed_commit_id="a5ecde595c47f35fd7293d52eba48efd687ca94e",
        test_file=[Path("tests", "keras", "utils", "generic_utils_test.py")],
        test_cases=["tests/keras/utils/generic_utils_test.py::test_progbar"],
    )
    Keras(
        bug_id=40,
        buggy_commit_id="871007dbb0e6211459b9d16244cc3c9683459df7",
        fixed_commit_id="4cad455ef4da600c96ddc69800bab39d0e52b677",
        test_file=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            "tests/keras/layers/recurrent_test.py::test_stacked_rnn_compute_output_shape"
        ],
    )
    Keras(
        bug_id=41,
        buggy_commit_id="a27b4a51f4880ad3a7669531b667c1ef44b173ef",
        fixed_commit_id="4a58b178073f0ba3b166220f7ebd7d56149bfb20",
        test_file=[Path("tests", "keras", "utils", "data_utils_test.py")],
        test_cases=[
            "tests/keras/utils/data_utils_test.py::test_generator_enqueuer_fail_threads"
        ],
    )
    Keras(
        bug_id=42,
        buggy_commit_id="67a432c273cbd65866b1d2cb1e2c62714b633b6e",
        fixed_commit_id="2f3edf96078d78450b985bdf3bfffe7e0c627169",
        test_file=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=["tests/keras/engine/test_training.py::test_model_methods"],
    )
    Keras(
        bug_id=43,
        buggy_commit_id="e3e97c401aa8251e957b73fba8ed4d108c106f12",
        fixed_commit_id="b17169ca5d6cd1c8aeb237fc2bb0555c9e1b6a02",
        test_file=[Path("tests", "keras", "utils", "np_utils_test.py")],
        test_cases=["tests/keras/utils/np_utils_test.py::test_to_categorical"],
    )
    Keras(
        bug_id=44,
        buggy_commit_id="cc08f0f01fe97a9659e3da8fa9b290a54992c74a",
        fixed_commit_id="3292aa5a30350c67627f173ceac713956f68271f",
        test_file=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=["tests/keras/layers/recurrent_test.py::test_trainability"],
    )
    Keras(
        bug_id=45,
        buggy_commit_id="d368dc870bfd8fdd4ca0ff82bd5b61aa549291c5",
        fixed_commit_id="159bb1aac17a8de0f96997d35703b8f26926a848",
        test_file=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            "tests/keras/layers/recurrent_test.py::test_implementation_mode[LSTM]"
        ],
    )


class KerasAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
