from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Luigi(Project):
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
            project_name="luigi",
            github_url="https://github.com/spotify/luigi",
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
            python_fallback_version="3.8.4",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


def register():
    Luigi(
        bug_id=1,
        buggy_commit_id="1164eb6b85b8a70f596dbb99452bec513e72c12e",
        fixed_commit_id="aec5dc2ed8db53fc282a0bd24aabe59031b6d1ba",
        test_file=[Path("test", "server_test.py")],
        test_cases=["test/server_test.py::MetricsHandlerTest::test_get"],
    )
    Luigi(
        bug_id=2,
        buggy_commit_id="baa54c9f4f809692d62d4c3e4497161717c76550",
        fixed_commit_id="24e85945ae39e5975491527e00c3f0f64b42ea6e",
        test_file=[Path("test", "contrib", "beam_dataflow_test.py")],
        test_cases=[
            "test/contrib/beam_dataflow_test.py::BeamDataflowTest::test_get_target_path"
        ],
    )
    Luigi(
        bug_id=3,
        buggy_commit_id="a0f1db01ddab5b4b2bda3fbe58bad09a6d94a7b4",
        fixed_commit_id="3a0bfbff69addfb3be1107adab3d4914bcae3e4b",
        test_file=[Path("test", "parameter_test.py")],
        test_cases=[
            "test/parameter_test.py::TestSerializeTupleParameter::testSerialize"
        ],
    )
    Luigi(
        bug_id=4,
        buggy_commit_id="ffa51b50103a3adaf3c4d0569fdb037a7ba01e8e",
        fixed_commit_id="8501e5dbb8d3040453a89bb0d3562526086d51e5",
        test_file=[Path("test", "contrib", "redshift_test.py")],
        test_cases=[
            "test/contrib/redshift_test.py::TestS3CopyToTable::test_s3_copy_with_nonetype_columns"
        ],
    )
    Luigi(
        bug_id=5,
        buggy_commit_id="45b5711d1900184ccd66c65216d28c0d69d10d4a",
        fixed_commit_id="1fbec18ceb7c5de352e6d1df12960c61f09e67c2",
        test_file=[Path("test", "util_test.py")],
        test_cases=[
            "test/util_test.py::BasicsTest::test_inherits_has_effect_MRO",
            "test/util_test.py::BasicsTest::test_requires_has_effect_MRO",
        ],
    )
    Luigi(
        bug_id=6,
        buggy_commit_id="d9667b7c8ce75f17efa383e8f64e27e5852e6f89",
        fixed_commit_id="ce881b2a95743887c6147ff4ba23ce5f622b3f5e",
        test_file=[Path("test", "parameter_test.py")],
        test_cases=[
            "test/parameter_test.py::TestParametersHashability::test_list_dict",
            "test/parameter_test.py::TestParametersHashability::test_tuple_dict",
        ],
    )
    Luigi(
        bug_id=7,
        buggy_commit_id="dd1f2ce0061e7787166522a3c75339ba4755dd2c",
        fixed_commit_id="daf9ce99a3a7ed4227d1564570c5fce8848357e5",
        test_file=[Path("test", "scheduler_api_test.py")],
        test_cases=[
            "test/scheduler_api_test.py::SchedulerApiTest::test_status_wont_override"
        ],
    )
    Luigi(
        bug_id=8,
        buggy_commit_id="61ee32e9968978c32be12a6af0affa3a5750e87e",
        fixed_commit_id="8874b93165953c4f6bbe7b747804654d13290018",
        test_file=[Path("test", "contrib", "redshift_test.py")],
        test_cases=[
            "test/contrib/redshift_test.py::TestS3CopyToSchemaTable::test_s3_copy_to_table"
        ],
    )
    Luigi(
        bug_id=9,
        buggy_commit_id="f7e0b7710fd8b12f27625b1efb62a8fde6e206c4",
        fixed_commit_id="b7115974c3deadf77113686248b39567cb67e38f",
        test_file=[Path("test", "execution_summary_test.py")],
        test_cases=[
            "test/execution_summary_test.py::ExecutionSummaryTest::test_status_with_task_retry"
        ],
    )
    Luigi(
        bug_id=10,
        buggy_commit_id="f538d1b3d473d542a19d508e5f7e0809b1dfe5ef",
        fixed_commit_id="3c55acd2cd5cf9c6c760bec5bb3159e0bc48a614",
        test_file=[Path("test", "scheduler_test.py")],
        test_cases=[
            "test/scheduler_test.py::SchedulerWorkerTest::test_get_pending_tasks_with_many_done_tasks"
        ],
    )
    Luigi(
        bug_id=11,
        buggy_commit_id="bf8b5cba573d5d6cd11f7f10a03b458aeaf955c1",
        fixed_commit_id="70d8734d60e168389f425082b41b1936d63c028e",
        test_file=[Path("test", "scheduler_api_test.py")],
        test_cases=[
            "test/scheduler_api_test.py::SchedulerApiTest::test_batch_ignore_items_not_ready"
        ],
    )
    Luigi(
        bug_id=12,
        buggy_commit_id="c3119757c9ad4141fb446554109fa09cbd31173c",
        fixed_commit_id="b3e9ad57f8502a390686957b69070105fddcfd49",
        test_file=[Path("test", "hdfs_client_test.py")],
        test_cases=[
            "test/hdfs_client_test.py::HdfsClientTest::test_get_autoconfig_client_cached"
        ],
    )
    Luigi(
        bug_id=13,
        buggy_commit_id="3c90bcdac63d978dbdaeae408420e22b963c9863",
        fixed_commit_id="a8e64fe7f83d69702166a44c7e8cb9470ff31040",
        test_file=[Path("test", "file_test.py")],
        test_cases=["test/file_test.py::FileSystemTest::test_move_to_new_dir"],
    )
    Luigi(
        bug_id=14,
        buggy_commit_id="f7219c38121098d464011a094156d99b5b320362",
        fixed_commit_id="43f2de2646c8e1efd6e17ffabbb11accc21e70b6",
        test_file=[Path("test", "central_planner_test.py")],
        test_cases=[
            "test/central_planner_test.py::CentralPlannerTest::test_no_crash_on_only_disable_hard_timeout"
        ],
    )
    Luigi(
        bug_id=15,
        buggy_commit_id="a822f55d4d7c5adf5b9e3b64f23189d8305e9bf9",
        fixed_commit_id="736c0f1352463c20ece84f2f651bcd37fd2b88ae",
        test_file=[Path("test", "central_planner_test.py")],
        test_cases=[
            "test/central_planner_test.py::CentralPlannerTest::test_assistants_dont_nurture_finished_statuses"
        ],
    )
    Luigi(
        bug_id=16,
        buggy_commit_id="e38392a1381dd8daee0f180f0ac7f651edb88e0c",
        fixed_commit_id="96f2b5a97c2cc5f63bea0f422c57f93dcec0ebac",
        test_file=[Path("test", "central_planner_test.py")],
        test_cases=[
            "test/central_planner_test.py::CentralPlannerTest::test_re_enable_failed_task_assistant"
        ],
    )
    Luigi(
        bug_id=17,
        buggy_commit_id="c39922350cba3a93c96c2ed223283bf8cf315a7d",
        fixed_commit_id="e38392a1381dd8daee0f180f0ac7f651edb88e0c",
        test_file=[Path("test", "scheduler_test.py")],
        test_cases=[
            "test/scheduler_test.py::SchedulerTest::test_local_scheduler_task_history_status"
        ],
    )
    Luigi(
        bug_id=18,
        buggy_commit_id="6cffbf438d023441f7f42c2019a51c62eecd9018",
        fixed_commit_id="c521d59c5eacf6c19ce3c17a62f73e042fa0556e",
        test_file=[Path("test", "central_planner_test.py")],
        test_cases=[
            "test/central_planner_test.py::CentralPlannerTest::test_no_automatic_re_enable_after_auto_then_manual_disable"
        ],
    )
    Luigi(
        bug_id=19,
        buggy_commit_id="3d2f75224c7649402927a5ef57558d8c3717cd94",
        fixed_commit_id="6cffbf438d023441f7f42c2019a51c62eecd9018",
        test_file=[Path("test", "central_planner_test.py")],
        test_cases=[
            "test/central_planner_test.py::CentralPlannerTest::test_automatic_re_enable_with_one_failure_allowed"
        ],
    )
    Luigi(
        bug_id=20,
        buggy_commit_id="b958140c2ec838e590a5be02dbac7414d5d0bf17",
        fixed_commit_id="c3d685e2b03369aab6f4d86ed1c95169c1c2c217",
        test_file=[Path("test", "task_test.py")],
        test_cases=["test/task_test.py::TaskTest::test_task_to_str_to_task"],
    )
    Luigi(
        bug_id=21,
        buggy_commit_id="b7768da963570bd2223d97c1035f811c2eaf30b4",
        fixed_commit_id="1a6a89d8b510089392bb407d4ec660451deb1f23",
        test_file=[Path("test", "interface_test.py")],
        test_cases=[
            "test/interface_test.py::InterfaceTest::test_just_run_main_task_cls"
        ],
    )
    Luigi(
        bug_id=22,
        buggy_commit_id="9c4c47ae449593c55fb67ce51115d0be1fecb163",
        fixed_commit_id="2db9768958c9665c2bb78f040054a25534205fc4",
        test_file=[Path("test", "scheduler_test.py")],
        test_cases=[
            "test/scheduler_test.py::SchedulerTest::test_worker_prune_after_init"
        ],
    )
    Luigi(
        bug_id=24,
        buggy_commit_id="572fce617a3b8133983cdee2b2cc336a65af5abe",
        fixed_commit_id="8a4f73296f237fcf8182c342e62c2cb201c717df",
        test_file=[Path("test", "contrib", "spark_test.py")],
        test_cases=[
            "test/contrib/spark_test.py::SparkSubmitTaskTest::test_run",
            "test/contrib/spark_test.py::SparkSubmitTaskTest::test_defaults",
        ],
    )
    Luigi(
        bug_id=25,
        buggy_commit_id="d7ec31609c88503391d12d65b6037f397feff816",
        fixed_commit_id="040bbc9ef8d1703b64d13c60f271fded63e13601",
        test_file=[Path("test", "contrib", "redshift_test.py")],
        test_cases=[
            "test/contrib/redshift_test.py::TestS3CopyToTable::test_s3_copy_to_table"
        ],
    )
    Luigi(
        bug_id=26,
        buggy_commit_id="ed351ca3c3baf3657de584db08dfe0414fa000a3",
        fixed_commit_id="13673fd488c25325db633b1d49e664fb937fabc2",
        test_file=[Path("test", "contrib", "hadoop_jar_test.py")],
        test_cases=[
            "test/contrib/hadoop_jar_test.py::HadoopJarJobTaskTest::test_missing_jar"
        ],
    )
    Luigi(
        bug_id=27,
        buggy_commit_id="69dfec33dc7c34d551ddc71742fa9c847295b01f",
        fixed_commit_id="fa17292ebb54c8b83db8cf0995618a2a057103a6",
        test_file=[Path("test", "parameter_test.py")],
        test_cases=[
            "test/parameter_test.py::TestParamWithDefaultFromConfig::testCommandLineWithDefault",
            "test/parameter_test.py::TestParamWithDefaultFromConfig::testCommandLineNoDefault",
        ],
    )
    Luigi(
        bug_id=28,
        buggy_commit_id="e37cb0ea1d97e6340840128a68c8d59bd05c28c3",
        fixed_commit_id="e2be971226c34a193d7029c51206e488b6a037cd",
        test_file=[Path("test", "contrib", "hive_test.py")],
        test_cases=[
            "test/contrib/hive_test.py::HiveCommandClientTest::test_table_exists",
            "test/contrib/hive_test.py::HiveCommandClientTest::test_apacheclient_table_exists",
        ],
    )
    Luigi(
        bug_id=29,
        buggy_commit_id="07efdd9136966ffe143ea57e15b1a57b5698fd5a",
        fixed_commit_id="2898a2d2d178499435892d7a69bb1dfc90c70b29",
        test_file=[Path("test", "task_test.py")],
        test_cases=["test/task_test.py::TaskTest::test_external_tasks_loadable"],
    )
    Luigi(
        bug_id=30,
        buggy_commit_id="97fa4afea3748f0d714482d2c97990bb467bc9d1",
        fixed_commit_id="f1e3fb48fe9877e511a2d079636fd75eaaba4573",
        test_file=[Path("test", "test_event_callbacks.py")],
        test_cases=[
            "test/test_event_callbacks.py::TestEventCallbacks::test_failure",
            "test/test_event_callbacks.py::TestEventCallbacks::test_processing_time_handler_failure",
        ],
    )
    Luigi(
        bug_id=31,
        buggy_commit_id="554850f32784537796383db5ee188d0455863ca9",
        fixed_commit_id="c0857e9e06012b696017e0a353ae74f4f621d066",
        test_file=[Path("test", "central_planner_test.py")],
        test_cases=[
            "test/central_planner_test.py::CentralPlannerTest::test_assistant_get_work_external_task"
        ],
    )
    Luigi(
        bug_id=32,
        buggy_commit_id="7233a0cc3e34c7c14259b1fa046f66332914f410",
        fixed_commit_id="027ac3fbcf66d5d21554c9ac6da26eee5c2e0f3d",
        test_file=[Path("test", "instance_test.py")],
        test_cases=["test/instance_test.py::InstanceTest::test_unhashable_type"],
    )
    Luigi(
        bug_id=33,
        buggy_commit_id="a7c0662eab78fd226fd7ef6b4461d7199336cbb1",
        fixed_commit_id="fccb631a14e1d52138d39f06004be14ca8f3337d",
        test_file=[Path("test", "parameter_test.py")],
        test_cases=[
            "test/parameter_test.py::ParameterTest::test_local_insignificant_param",
            "test/parameter_test.py::TestRemoveGlobalParameters::test_global_significant_param",
            "test/parameter_test.py::TestRemoveGlobalParameters::test_mixed_params",
            "test/parameter_test.py::TestRemoveGlobalParameters::test_mixed_params_inheritence",
        ],
    )


class LuigiAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
