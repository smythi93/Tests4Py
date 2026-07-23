import ast
import os.path
import random
import string
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple, Any

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up, NUMBER
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "luigi"


class Luigi(Project):
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
            github_url="https://github.com/spotify/luigi",
            status=Status.OK,
            python_version="3.7.8",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version="3.7.8",
            python_fallback_version="3.7.8",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar,
            loc=loc,
            included_files=[PROJECT_NAME],
            source_base=Path(PROJECT_NAME),
            test_base=Path("test"),
            setup=[[PYTHON, "-m", "pip", "install", "-e", "."]],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )


def register():
    Luigi(
        bug_id=1,
        buggy_commit_id="1164eb6b85b8a70f596dbb99452bec513e72c12e",
        fixed_commit_id="aec5dc2ed8db53fc282a0bd24aabe59031b6d1ba",
        test_files=[Path("test", "server_test.py")],
        test_cases=[
            os.path.join("test", "server_test.py::MetricsHandlerTest::test_get")
        ],
        skip_tests=["_ServerTest", "UNIXServerTest", "_INETServerTest"],
        unittests=Luigi1UnittestGenerator(),
        systemtests=Luigi1SystemtestGenerator(),
        api=Luigi1API(),
        grammar=grammar_1,
        loc=15700,
    )
    Luigi(
        bug_id=2,
        buggy_commit_id="baa54c9f4f809692d62d4c3e4497161717c76550",
        fixed_commit_id="24e85945ae39e5975491527e00c3f0f64b42ea6e",
        test_files=[Path("test", "contrib", "beam_dataflow_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "contrib",
                "beam_dataflow_test.py::BeamDataflowTest::test_get_target_path",
            )
        ],
        unittests=Luigi2UnittestGenerator(),
        systemtests=Luigi2SystemtestGenerator(),
        api=Luigi2API(),
        grammar=grammar_2,
        loc=15699,
    )
    Luigi(
        bug_id=3,
        buggy_commit_id="a0f1db01ddab5b4b2bda3fbe58bad09a6d94a7b4",
        fixed_commit_id="3a0bfbff69addfb3be1107adab3d4914bcae3e4b",
        test_files=[Path("test", "parameter_test.py")],
        test_cases=[
            os.path.join(
                "test", "parameter_test.py::TestSerializeTupleParameter::testSerialize"
            )
        ],
        unittests=Luigi3UnittestGenerator(),
        systemtests=Luigi3SystemtestGenerator(),
        api=Luigi3API(),
        grammar=grammar_3,
        loc=15078,
    )
    Luigi(
        bug_id=4,
        buggy_commit_id="ffa51b50103a3adaf3c4d0569fdb037a7ba01e8e",
        fixed_commit_id="8501e5dbb8d3040453a89bb0d3562526086d51e5",
        test_files=[Path("test", "contrib", "redshift_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "contrib",
                "redshift_test.py::TestS3CopyToTable::test_s3_copy_with_nonetype_columns",
            )
        ],
        unittests=Luigi4UnittestGenerator(),
        systemtests=Luigi4SystemtestGenerator(),
        api=Luigi4API(),
        grammar=grammar_4,
        loc=13587,
    )
    Luigi(
        bug_id=5,
        buggy_commit_id="45b5711d1900184ccd66c65216d28c0d69d10d4a",
        fixed_commit_id="1fbec18ceb7c5de352e6d1df12960c61f09e67c2",
        test_files=[Path("test", "util_test.py")],
        test_cases=[
            os.path.join(
                "test", "util_test.py::BasicsTest::test_inherits_has_effect_MRO"
            ),
            os.path.join(
                "test", "util_test.py::BasicsTest::test_requires_has_effect_MRO"
            ),
        ],
        unittests=Luigi5UnittestGenerator(),
        systemtests=Luigi5SystemtestGenerator(),
        api=Luigi5API(),
        grammar=grammar_5,
        loc=13474,
    )
    Luigi(
        bug_id=6,
        buggy_commit_id="d9667b7c8ce75f17efa383e8f64e27e5852e6f89",
        fixed_commit_id="ce881b2a95743887c6147ff4ba23ce5f622b3f5e",
        test_files=[Path("test", "parameter_test.py")],
        test_cases=[
            os.path.join(
                "test", "parameter_test.py::TestParametersHashability::test_list_dict"
            ),
            os.path.join(
                "test", "parameter_test.py::TestParametersHashability::test_tuple_dict"
            ),
        ],
        unittests=Luigi6UnittestGenerator(),
        systemtests=Luigi6SystemtestGenerator(),
        api=Luigi6API(),
        grammar=grammar_6,
        loc=13248,
    )
    Luigi(
        bug_id=7,
        buggy_commit_id="dd1f2ce0061e7787166522a3c75339ba4755dd2c",
        fixed_commit_id="daf9ce99a3a7ed4227d1564570c5fce8848357e5",
        test_files=[Path("test", "scheduler_api_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "scheduler_api_test.py::SchedulerApiTest::test_status_wont_override",
            )
        ],
        unittests=Luigi7UnittestGenerator(),
        systemtests=Luigi7SystemtestGenerator(),
        api=Luigi7API(),
        grammar=grammar_7,
        loc=13176,
    )
    Luigi(
        bug_id=8,
        buggy_commit_id="61ee32e9968978c32be12a6af0affa3a5750e87e",
        fixed_commit_id="8874b93165953c4f6bbe7b747804654d13290018",
        test_files=[Path("test", "contrib", "redshift_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "contrib",
                "redshift_test.py::TestS3CopyToTable::test_s3_copy_to_table",
            ),
            os.path.join(
                "test",
                "contrib",
                "redshift_test.py::TestS3CopyToTable::test_s3_copy_to_temp_table",
            ),
            os.path.join(
                "test",
                "contrib",
                "redshift_test.py::TestS3CopyToSchemaTable::test_s3_copy_to_table",
            ),
        ],
        unittests=Luigi8UnittestGenerator(),
        systemtests=Luigi8SystemtestGenerator(),
        api=Luigi8API(),
        grammar=grammar_8,
        loc=13126,
    )
    Luigi(
        bug_id=9,
        buggy_commit_id="f7e0b7710fd8b12f27625b1efb62a8fde6e206c4",
        fixed_commit_id="b7115974c3deadf77113686248b39567cb67e38f",
        test_files=[Path("test", "execution_summary_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "execution_summary_test.py::ExecutionSummaryTest::test_status_with_task_retry",
            )
        ],
        unittests=Luigi9UnittestGenerator(),
        systemtests=Luigi9SystemtestGenerator(),
        api=Luigi9API(),
        grammar=grammar_9,
        loc=12759,
    )
    Luigi(
        bug_id=10,
        buggy_commit_id="f538d1b3d473d542a19d508e5f7e0809b1dfe5ef",
        fixed_commit_id="3c55acd2cd5cf9c6c760bec5bb3159e0bc48a614",
        test_files=[Path("test", "scheduler_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "scheduler_test.py::SchedulerWorkerTest::test_get_pending_tasks_with_many_done_tasks",
            )
        ],
        unittests=Luigi10UnittestGenerator(),
        systemtests=Luigi10SystemtestGenerator(),
        api=Luigi10API(),
        grammar=grammar_10,
        loc=12759,
    )
    Luigi(
        bug_id=11,
        buggy_commit_id="bf8b5cba573d5d6cd11f7f10a03b458aeaf955c1",
        fixed_commit_id="70d8734d60e168389f425082b41b1936d63c028e",
        test_files=[Path("test", "scheduler_api_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "scheduler_api_test.py::SchedulerApiTest::test_batch_ignore_items_not_ready",
            )
        ],
        unittests=Luigi11UnittestGenerator(),
        systemtests=Luigi11SystemtestGenerator(),
        api=Luigi11API(),
        grammar=grammar_11,
        loc=12099,
    )
    Luigi(
        bug_id=12,
        buggy_commit_id="c3119757c9ad4141fb446554109fa09cbd31173c",
        fixed_commit_id="b3e9ad57f8502a390686957b69070105fddcfd49",
        test_files=[Path("test", "hdfs_client_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "hdfs_client_test.py::HdfsClientTest::test_get_autoconfig_client_cached",
            )
        ],
        unittests=Luigi12UnittestGenerator(),
        systemtests=Luigi12SystemtestGenerator(),
        api=Luigi12API(),
        grammar=grammar_12,
        loc=11778,
    )
    Luigi(
        bug_id=13,
        buggy_commit_id="3c90bcdac63d978dbdaeae408420e22b963c9863",
        fixed_commit_id="a8e64fe7f83d69702166a44c7e8cb9470ff31040",
        test_files=[Path("test", "file_test.py")],
        test_cases=[
            os.path.join("test", "file_test.py::FileSystemTest::test_move_to_new_dir")
        ],
        skip_tests=[
            "test_rename_dont_move_on_fs",
        ],
        unittests=Luigi13UnittestGenerator(),
        systemtests=Luigi13SystemtestGenerator(),
        api=Luigi13API(),
        grammar=grammar_13,
        loc=11581,
    )
    Luigi(
        bug_id=14,
        buggy_commit_id="f7219c38121098d464011a094156d99b5b320362",
        fixed_commit_id="43f2de2646c8e1efd6e17ffabbb11accc21e70b6",
        test_files=[Path("test", "central_planner_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "central_planner_test.py::CentralPlannerTest::test_no_crash_on_only_disable_hard_timeout",
            )
        ],
        unittests=Luigi14UnittestGenerator(),
        systemtests=Luigi14SystemtestGenerator(),
        api=Luigi14API(),
        grammar=grammar_14,
        loc=11580,
    )
    Luigi(
        bug_id=15,
        buggy_commit_id="a822f55d4d7c5adf5b9e3b64f23189d8305e9bf9",
        fixed_commit_id="736c0f1352463c20ece84f2f651bcd37fd2b88ae",
        test_files=[Path("test", "central_planner_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "central_planner_test.py::CentralPlannerTest::test_assistants_dont_nurture_finished_statuses",
            )
        ],
        unittests=Luigi15UnittestGenerator(),
        systemtests=Luigi15SystemtestGenerator(),
        api=Luigi15API(),
        grammar=grammar_15,
        loc=11261,
    )
    Luigi(
        bug_id=16,
        buggy_commit_id="e38392a1381dd8daee0f180f0ac7f651edb88e0c",
        fixed_commit_id="96f2b5a97c2cc5f63bea0f422c57f93dcec0ebac",
        test_files=[Path("test", "central_planner_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "central_planner_test.py::CentralPlannerTest::test_re_enable_failed_task_assistant",
            )
        ],
        unittests=Luigi16UnittestGenerator(),
        systemtests=Luigi16SystemtestGenerator(),
        api=Luigi16API(),
        grammar=grammar_16,
        loc=10639,
    )
    Luigi(
        bug_id=17,
        buggy_commit_id="c39922350cba3a93c96c2ed223283bf8cf315a7d",
        fixed_commit_id="e38392a1381dd8daee0f180f0ac7f651edb88e0c",
        test_files=[Path("test", "scheduler_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "scheduler_test.py::SchedulerTest::test_local_scheduler_task_history_status",
            )
        ],
        unittests=Luigi17UnittestGenerator(),
        systemtests=Luigi17SystemtestGenerator(),
        api=Luigi17API(),
        grammar=grammar_17,
        loc=10639,
    )
    Luigi(
        bug_id=18,
        buggy_commit_id="6cffbf438d023441f7f42c2019a51c62eecd9018",
        fixed_commit_id="c521d59c5eacf6c19ce3c17a62f73e042fa0556e",
        test_files=[Path("test", "central_planner_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "central_planner_test.py::CentralPlannerTest::"
                "test_no_automatic_re_enable_after_auto_then_manual_disable",
            )
        ],
        unittests=Luigi18UnittestGenerator(),
        systemtests=Luigi18SystemtestGenerator(),
        api=Luigi18API(),
        grammar=grammar_18,
        loc=10061,
    )
    Luigi(
        bug_id=19,
        buggy_commit_id="3d2f75224c7649402927a5ef57558d8c3717cd94",
        fixed_commit_id="6cffbf438d023441f7f42c2019a51c62eecd9018",
        test_files=[Path("test", "central_planner_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "central_planner_test.py::CentralPlannerTest::test_automatic_re_enable_with_one_failure_allowed",
            )
        ],
        unittests=Luigi19UnittestGenerator(),
        systemtests=Luigi19SystemtestGenerator(),
        api=Luigi19API(),
        grammar=grammar_19,
        loc=10061,
    )
    Luigi(
        bug_id=20,
        buggy_commit_id="b958140c2ec838e590a5be02dbac7414d5d0bf17",
        fixed_commit_id="c3d685e2b03369aab6f4d86ed1c95169c1c2c217",
        test_files=[Path("test", "task_test.py")],
        test_cases=[
            os.path.join("test", "task_test.py::TaskTest::test_task_to_str_to_task")
        ],
        unittests=Luigi20UnittestGenerator(),
        systemtests=Luigi20SystemtestGenerator(),
        api=Luigi20API(),
        grammar=grammar_20,
        loc=9226,
    )
    Luigi(
        bug_id=21,
        buggy_commit_id="b7768da963570bd2223d97c1035f811c2eaf30b4",
        fixed_commit_id="1a6a89d8b510089392bb407d4ec660451deb1f23",
        test_files=[Path("test", "interface_test.py")],
        test_cases=[
            os.path.join(
                "test", "interface_test.py::InterfaceTest::test_just_run_main_task_cls"
            )
        ],
        unittests=Luigi21UnittestGenerator(),
        systemtests=Luigi21SystemtestGenerator(),
        api=Luigi21API(),
        grammar=grammar_21,
        loc=9174,
    )
    Luigi(
        bug_id=22,
        buggy_commit_id="9c4c47ae449593c55fb67ce51115d0be1fecb163",
        fixed_commit_id="2db9768958c9665c2bb78f040054a25534205fc4",
        test_files=[Path("test", "scheduler_test.py")],
        test_cases=[
            os.path.join(
                "test", "scheduler_test.py::SchedulerTest::test_worker_prune_after_init"
            )
        ],
        unittests=Luigi22UnittestGenerator(),
        systemtests=Luigi22SystemtestGenerator(),
        api=Luigi22API(),
        grammar=grammar_22,
        loc=9223,
    )
    Luigi(
        bug_id=23,
        buggy_commit_id="c707253572deb795a900c3e07d21eee591a55fca",
        fixed_commit_id="dc41727f4de88f86f4e77aa45be51eff4ee6b3be",
        test_files=[
            Path("test", "worker_external_task_test.py"),
            Path("test", "worker_test.py"),
        ],
        test_cases=[
            os.path.join(
                "test",
                "worker_external_task_test.py::WorkerExternalTaskTest::test_external_dependency_already_complete",
            ),
            os.path.join(
                "test",
                "worker_external_task_test.py::WorkerExternalTaskTest::test_external_dependency_completes_later",
            ),
        ],
        unittests=Luigi23UnittestGenerator(),
        systemtests=Luigi23SystemtestGenerator(),
        api=Luigi23API(),
        grammar=grammar_23,
        loc=9233,
    )
    Luigi(
        bug_id=24,
        buggy_commit_id="572fce617a3b8133983cdee2b2cc336a65af5abe",
        fixed_commit_id="8a4f73296f237fcf8182c342e62c2cb201c717df",
        test_files=[Path("test", "contrib", "spark_test.py")],
        test_cases=[
            os.path.join(
                "test", "contrib", "spark_test.py::SparkSubmitTaskTest::test_run"
            ),
            os.path.join(
                "test", "contrib", "spark_test.py::SparkSubmitTaskTest::test_defaults"
            ),
        ],
        unittests=Luigi24UnittestGenerator(),
        systemtests=Luigi24SystemtestGenerator(),
        api=Luigi24API(),
        grammar=grammar_24,
        loc=8987,
    )
    Luigi(
        bug_id=25,
        buggy_commit_id="d7ec31609c88503391d12d65b6037f397feff816",
        fixed_commit_id="040bbc9ef8d1703b64d13c60f271fded63e13601",
        test_files=[
            Path("test", "contrib", "redshift_test.py"),
        ],
        test_cases=[
            os.path.join(
                "test",
                "contrib",
                "redshift_test.py::TestS3CopyToTable::test_s3_copy_to_table",
            ),
        ],
        unittests=Luigi25UnittestGenerator(),
        systemtests=Luigi25SystemtestGenerator(),
        api=Luigi25API(),
        grammar=grammar_25,
        loc=8587,
    )
    Luigi(
        bug_id=26,
        buggy_commit_id="ed351ca3c3baf3657de584db08dfe0414fa000a3",
        fixed_commit_id="13673fd488c25325db633b1d49e664fb937fabc2",
        test_files=[Path("test", "contrib", "hadoop_jar_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "contrib",
                "hadoop_jar_test.py::HadoopJarJobTaskTest::test_missing_jar",
            )
        ],
        unittests=Luigi26UnittestGenerator(),
        systemtests=Luigi26SystemtestGenerator(),
        api=Luigi26API(),
        grammar=grammar_26,
        loc=8551,
    )
    Luigi(
        bug_id=27,
        buggy_commit_id="69dfec33dc7c34d551ddc71742fa9c847295b01f",
        fixed_commit_id="fa17292ebb54c8b83db8cf0995618a2a057103a6",
        test_files=[Path("test", "parameter_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "parameter_test.py::TestParamWithDefaultFromConfig::testCommandLineWithDefault",
            ),
            os.path.join(
                "test",
                "parameter_test.py::TestParamWithDefaultFromConfig::testCommandLineNoDefault",
            ),
        ],
        unittests=Luigi27UnittestGenerator(),
        systemtests=Luigi27SystemtestGenerator(),
        api=Luigi27API(),
        grammar=grammar_27,
        loc=8530,
    )
    Luigi(
        bug_id=28,
        buggy_commit_id="e37cb0ea1d97e6340840128a68c8d59bd05c28c3",
        fixed_commit_id="e2be971226c34a193d7029c51206e488b6a037cd",
        test_files=[Path("test", "contrib", "hive_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "contrib",
                "hive_test.py::HiveCommandClientTest::test_table_exists",
            ),
            os.path.join(
                "test",
                "contrib",
                "hive_test.py::HiveCommandClientTest::test_apacheclient_table_exists",
            ),
        ],
        unittests=Luigi28UnittestGenerator(),
        systemtests=Luigi28SystemtestGenerator(),
        api=Luigi28API(),
        grammar=grammar_28,
        loc=8316,
    )
    Luigi(
        bug_id=29,
        buggy_commit_id="07efdd9136966ffe143ea57e15b1a57b5698fd5a",
        fixed_commit_id="2898a2d2d178499435892d7a69bb1dfc90c70b29",
        test_files=[Path("test", "task_test.py")],
        test_cases=[
            os.path.join("test", "task_test.py::TaskTest::test_external_tasks_loadable")
        ],
        unittests=Luigi29UnittestGenerator(),
        systemtests=Luigi29SystemtestGenerator(),
        api=Luigi29API(),
        grammar=grammar_29,
        loc=8358,
    )
    Luigi(
        bug_id=30,
        buggy_commit_id="97fa4afea3748f0d714482d2c97990bb467bc9d1",
        fixed_commit_id="f1e3fb48fe9877e511a2d079636fd75eaaba4573",
        test_files=[Path("test", "test_event_callbacks.py")],
        test_cases=[
            os.path.join(
                "test", "test_event_callbacks.py::TestEventCallbacks::test_failure"
            ),
            os.path.join(
                "test",
                "test_event_callbacks.py::TestEventCallbacks::test_processing_time_handler_failure",
            ),
        ],
        unittests=Luigi30UnittestGenerator(),
        systemtests=Luigi30SystemtestGenerator(),
        api=Luigi30API(),
        grammar=grammar_30,
        loc=8296,
    )
    Luigi(
        bug_id=31,
        buggy_commit_id="554850f32784537796383db5ee188d0455863ca9",
        fixed_commit_id="c0857e9e06012b696017e0a353ae74f4f621d066",
        test_files=[Path("test", "central_planner_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "central_planner_test.py::CentralPlannerTest::test_assistant_get_work_external_task",
            )
        ],
        unittests=Luigi31UnittestGenerator(),
        systemtests=Luigi31SystemtestGenerator(),
        api=Luigi31API(),
        grammar=grammar_31,
        loc=8291,
    )
    Luigi(
        bug_id=32,
        buggy_commit_id="7233a0cc3e34c7c14259b1fa046f66332914f410",
        fixed_commit_id="027ac3fbcf66d5d21554c9ac6da26eee5c2e0f3d",
        test_files=[Path("test", "instance_test.py")],
        test_cases=[
            os.path.join("test", "instance_test.py::InstanceTest::test_unhashable_type")
        ],
        unittests=Luigi32UnittestGenerator(),
        systemtests=Luigi32SystemtestGenerator(),
        api=Luigi32API(),
        grammar=grammar_32,
        loc=8289,
    )
    Luigi(
        bug_id=33,
        buggy_commit_id="a7c0662eab78fd226fd7ef6b4461d7199336cbb1",
        fixed_commit_id="fccb631a14e1d52138d39f06004be14ca8f3337d",
        test_files=[Path("test", "parameter_test.py")],
        test_cases=[
            os.path.join(
                "test",
                "parameter_test.py::ParameterTest::test_insignificant_parameter",
            ),
            os.path.join(
                "test",
                "parameter_test.py::ParameterTest::test_local_insignificant_param",
            ),
            os.path.join(
                "test",
                "parameter_test.py::TestRemoveGlobalParameters::test_global_significant_param",
            ),
            os.path.join(
                "test",
                "parameter_test.py::TestRemoveGlobalParameters::test_mixed_params",
            ),
            os.path.join(
                "test",
                "parameter_test.py::TestRemoveGlobalParameters::test_mixed_params_inheritence",
            ),
        ],
        unittests=Luigi33UnittestGenerator(),
        systemtests=Luigi33SystemtestGenerator(),
        api=Luigi33API(),
        grammar=grammar_33,
        loc=7821,
    )


class LuigiAPI(API):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# bug_3: ``TupleParameter.parse`` only caught ``ValueError`` and returned
# the bare ``literal_eval(x)``.  For a *flat* tuple, ``serialize`` yields a
# plain JSON list (e.g. ``"[1, 2, 3]"``); ``json.loads`` succeeds but the
# subsequent ``tuple(tuple(x) for x in ...)`` raises ``TypeError`` because
# the ints are not iterable — and the buggy ``except ValueError`` lets that
# ``TypeError`` escape.  The fix catches ``(ValueError, TypeError)`` and
# returns ``tuple(literal_eval(x))``.
#
# System-test format:  ``<mode> <int> <int> ...`` where ``<mode>`` is
#   ``flat`` (the trigger: a flat tuple that round-trips only on the fixed
#   build) or ``nested`` (pairs -> a tuple of tuples, which round-trips on
#   both builds).  The harness prints ``repr(parse(serialize(t)))``; the
#   oracle rebuilds the original tuple and compares.
# ======================================================================


def _tuple_from_args(mode: str, nums: List[int]) -> tuple:
    if mode == "flat":
        return tuple(nums)
    return tuple((nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2))


class Luigi3API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            nums = [int(a) for a in process.args[3:]]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _tuple_from_args(mode, nums)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == repr(expected):
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Luigi3TestGenerator:
    @staticmethod
    def generate_int() -> int:
        return random.randint(0, 999)

    def generate_flat(self) -> List[int]:
        return [self.generate_int() for _ in range(random.randint(1, 6))]

    def generate_pairs(self) -> List[int]:
        return [self.generate_int() for _ in range(2 * random.randint(1, 4))]


class Luigi3SystemtestGenerator(SystemtestGenerator, Luigi3TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        nums = self.generate_flat()
        return "flat " + " ".join(map(str, nums)), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        nums = self.generate_pairs()
        return "nested " + " ".join(map(str, nums)), TestResult.PASSING


class Luigi3UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi3TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="luigi",
                names=[ast.alias(name="TupleParameter")],
                level=0,
            )
        ]

    @staticmethod
    def _assert(the_tuple: tuple) -> List[ast.stmt]:
        return ast.parse(
            "tp = TupleParameter()\n"
            f"self.assertEqual(tp.parse(tp.serialize({the_tuple!r})), {the_tuple!r})"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        the_tuple = tuple(self.generate_flat())
        test = self.get_empty_test()
        test.body = self._assert(the_tuple)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        nums = self.generate_pairs()
        the_tuple = tuple((nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2))
        test = self.get_empty_test()
        test.body = self._assert(the_tuple)
        return test, TestResult.PASSING


grammar_3: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <numbers>"],
            "<mode>": ["flat", "nested"],
            "<numbers>": ["<number>", "<number> <numbers>"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_3)


# ======================================================================
# bug_32: ``Register.__call__`` in ``task_register.py`` caught the
# ``TypeError`` raised when a task's parameter values are unhashable and
# tried to ``logger.debug(...)`` — but the module never defined ``logger``,
# so a ``NameError`` escaped and instantiating a task with an unhashable
# parameter value (e.g. a ``dict``) crashed.  The fix adds
# ``logger = logging.getLogger('luigi-interface')``.
#
# System-test format:  ``<kind> <word> <word>`` where ``<kind>`` is
#   ``dict`` (the trigger: an unhashable value -> NameError on the buggy
#   build, but fine on the fixed build) or ``str``/``tuple``/``list``/
#   ``set`` (all normalize to hashable values, so they succeed on both).
#   The harness instantiates the task and prints ``HARNESS_OK``; the
#   oracle -- knowing the CORRECT behaviour is that instantiation always
#   succeeds -- returns PASSING iff ``HARNESS_OK`` was printed.
# ======================================================================


class Luigi32API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi32TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    def generate_words(self) -> Tuple[str, str]:
        return self.generate_word(), self.generate_word()


class Luigi32SystemtestGenerator(SystemtestGenerator, Luigi32TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        w1, w2 = self.generate_words()
        return f"dict {w1} {w2}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        w1, w2 = self.generate_words()
        kind = random.choice(("str", "tuple", "list", "set"))
        return f"{kind} {w1} {w2}", TestResult.PASSING


class Luigi32UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi32TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="luigi")])]

    @staticmethod
    def _value_literal(kind: str, w1: str, w2: str) -> str:
        if kind == "dict":
            return f"{{{w1!r}: {w2!r}}}"
        if kind == "tuple":
            return f"({w1!r}, {w2!r})"
        if kind == "list":
            return f"[{w1!r}, {w2!r}]"
        if kind == "set":
            return f"{{{w1!r}, {w2!r}}}"
        return f"{w1!r}"

    def _body(self, kind: str, w1: str, w2: str) -> List[ast.stmt]:
        cls_name = f"Task_{kind}_{w1}_{w2}"
        return ast.parse(
            f"class {cls_name}(luigi.Task):\n"
            f"    x = luigi.Parameter()\n"
            f"t = {cls_name}(x={self._value_literal(kind, w1, w2)})\n"
            f"self.assertIsNotNone(t)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w1, w2 = self.generate_words()
        test = self.get_empty_test()
        test.body = self._body("dict", w1, w2)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w1, w2 = self.generate_words()
        kind = random.choice(("str", "tuple", "list", "set"))
        test = self.get_empty_test()
        test.body = self._body(kind, w1, w2)
        return test, TestResult.PASSING


grammar_32: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <word> <word>"],
            "<kind>": ["dict", "str", "tuple", "list", "set"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_32)


# ======================================================================
# bug_6: ``_recursively_freeze`` handled ``list`` but not ``tuple``, and
# ``List``/``TupleParameter.serialize`` used a plain ``json.dumps`` that
# could not serialize the ``_FrozenOrderedDict`` produced by freezing a
# nested dict.  Consequences: a ``ListParameter`` whose value is a list of
# dicts failed to *serialize* during task instantiation, and a
# ``TupleParameter`` whose value is a tuple of dicts produced an
# *unhashable* normalized value.  The fix adds tuple handling to
# ``_recursively_freeze`` and a ``_DictParamEncoder`` for serialization.
#
# System-test format:  ``<ptype> <shape> <word> <word>`` where ``<ptype>``
#   is ``list`` or ``tuple`` and ``<shape>`` is ``dicts`` (the trigger: a
#   list/tuple of dicts) or ``flat``/``nested`` (no dicts, fine on both).
#   The harness instantiates a task with that parameter value and hashes
#   ``.args``; the oracle -- knowing the CORRECT behaviour is that this
#   always succeeds -- returns PASSING iff ``HARNESS_OK`` was printed.
# ======================================================================


class Luigi6API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi6TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    def generate_words(self) -> Tuple[str, str]:
        return self.generate_word(), self.generate_word()


class Luigi6SystemtestGenerator(SystemtestGenerator, Luigi6TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        w1, w2 = self.generate_words()
        ptype = random.choice(("list", "tuple"))
        return f"{ptype} dicts {w1} {w2}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        w1, w2 = self.generate_words()
        ptype = random.choice(("list", "tuple"))
        shape = random.choice(("flat", "nested"))
        return f"{ptype} {shape} {w1} {w2}", TestResult.PASSING


class Luigi6UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi6TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="luigi")])]

    @staticmethod
    def _value_literal(ptype: str, shape: str, w1: str, w2: str) -> str:
        if shape == "dicts":
            body = f"{{{w1!r}: {w2!r}}}, {{{w2!r}: {w1!r}}}"
        elif shape == "nested":
            body = f"[{w1!r}, {w2!r}], [{w2!r}, {w1!r}]"
        else:
            body = f"{w1!r}, {w2!r}"
        if ptype == "tuple":
            if shape == "nested":
                body = f"({w1!r}, {w2!r}), ({w2!r}, {w1!r})"
            return f"({body})"
        return f"[{body}]"

    def _body(self, ptype: str, shape: str, w1: str, w2: str) -> List[ast.stmt]:
        cls_name = f"Task_{ptype}_{shape}_{w1}_{w2}"
        param = "ListParameter" if ptype == "list" else "TupleParameter"
        return ast.parse(
            f"class {cls_name}(luigi.Task):\n"
            f"    args = luigi.{param}()\n"
            f"inst = {cls_name}(args={self._value_literal(ptype, shape, w1, w2)})\n"
            f"self.assertIsInstance(hash(inst.args), int)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w1, w2 = self.generate_words()
        ptype = random.choice(("list", "tuple"))
        test = self.get_empty_test()
        test.body = self._body(ptype, "dicts", w1, w2)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w1, w2 = self.generate_words()
        ptype = random.choice(("list", "tuple"))
        shape = random.choice(("flat", "nested"))
        test = self.get_empty_test()
        test.body = self._body(ptype, shape, w1, w2)
        return test, TestResult.PASSING


grammar_6: Grammar = clean_up(
    dict(
        {
            "<start>": ["<ptype> <shape> <word> <word>"],
            "<ptype>": ["list", "tuple"],
            "<shape>": ["dicts", "flat", "nested"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_6)


# ======================================================================
# bug_33: ``Task.get_param_values`` chose the positional-parameter slots by
# filtering on ``p.significant`` instead of ``not p.is_global``.  As a
# result a task with an *insignificant* (but non-global) parameter could
# not receive that parameter positionally -- instantiating it with a
# positional argument for the insignificant parameter raised
# ``UnknownParameterException`` ("takes at most N parameters").  The fix
# filters on ``not p.is_global`` so every local parameter is positional.
#
# System-test format:  ``<mode> <word> <word>`` where ``<mode>`` is
#   ``pos`` (the trigger: both values passed positionally, one of them for
#   the insignificant parameter) or ``kw``/``allkw`` (the insignificant
#   parameter passed by keyword, fine on both builds).  The harness
#   instantiates the task and prints ``HARNESS_OK``; the oracle -- knowing
#   the CORRECT behaviour is that instantiation always succeeds -- returns
#   PASSING iff ``HARNESS_OK`` was printed.
# ======================================================================


class Luigi33API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi33TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    def generate_words(self) -> Tuple[str, str]:
        return self.generate_word(), self.generate_word()


class Luigi33SystemtestGenerator(SystemtestGenerator, Luigi33TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        w1, w2 = self.generate_words()
        return f"pos {w1} {w2}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        w1, w2 = self.generate_words()
        mode = random.choice(("kw", "allkw"))
        return f"{mode} {w1} {w2}", TestResult.PASSING


class Luigi33UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi33TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="luigi")])]

    def _body(self, mode: str, w1: str, w2: str) -> List[ast.stmt]:
        cls_name = f"Task_{mode}_{w1}_{w2}"
        if mode == "pos":
            call = f"{cls_name}({w1!r}, {w2!r})"
        elif mode == "kw":
            call = f"{cls_name}({w1!r}, y={w2!r})"
        else:
            call = f"{cls_name}(x={w1!r}, y={w2!r})"
        return ast.parse(
            f"class {cls_name}(luigi.Task):\n"
            f"    x = luigi.Parameter()\n"
            f"    y = luigi.Parameter(significant=False)\n"
            f"t = {call}\n"
            f"self.assertIsNotNone(t)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w1, w2 = self.generate_words()
        test = self.get_empty_test()
        test.body = self._body("pos", w1, w2)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w1, w2 = self.generate_words()
        mode = random.choice(("kw", "allkw"))
        test = self.get_empty_test()
        test.body = self._body(mode, w1, w2)
        return test, TestResult.PASSING


grammar_33: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word> <word>"],
            "<mode>": ["pos", "kw", "allkw"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_33)


# ======================================================================
# bug_29: ``Register.__get_reg`` skipped every class whose ``run`` was
# still ``NotImplemented`` (``if cls.run == NotImplemented: continue``),
# which excludes *external* tasks from the name registry -- so an
# ``ExternalTask`` could not be looked up / loaded by name
# (``get_task_cls`` raised ``TaskClassException``).  The fix drops the
# skip so external tasks are registered too.
#
# System-test format:  ``<kind> <name>`` where ``<kind>`` is ``ext`` (the
#   trigger: an ExternalTask, unloadable on the buggy build) or ``normal``
#   (a regular task with a ``run`` method, loadable on both).  The harness
#   defines a uniquely-named task of that kind, looks it up by name and
#   prints ``HARNESS_OK``; the oracle -- knowing the CORRECT behaviour is
#   that the lookup always succeeds -- returns PASSING iff ``HARNESS_OK``.
# ======================================================================


class Luigi29API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi29TestGenerator:
    @staticmethod
    def generate_name() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi29SystemtestGenerator(SystemtestGenerator, Luigi29TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"ext {self.generate_name()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"normal {self.generate_name()}", TestResult.PASSING


class Luigi29UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi29TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.ImportFrom(
                module="luigi.task_register",
                names=[ast.alias(name="Register")],
                level=0,
            ),
        ]

    def _body(self, kind: str, name: str) -> List[ast.stmt]:
        var = f"Task_{kind}_{name}"
        if kind == "ext":
            create = f"{var} = type({name!r}, (luigi.ExternalTask,), {{}})"
        else:
            create = (
                f"{var} = type({name!r}, (luigi.Task,), "
                f"{{'run': lambda self: None}})"
            )
        return ast.parse(
            f"{create}\n"
            f"found = Register.get_task_cls({name!r})\n"
            f"self.assertIs(found, {var})\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("ext", self.generate_name())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("normal", self.generate_name())
        return test, TestResult.PASSING


grammar_29: Grammar = clean_up(
    dict(
        {
            "<start>": ["<kind> <name>"],
            "<kind>": ["ext", "normal"],
            "<name>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_29)


# ======================================================================
# bug_5: the ``inherits``/``requires`` decorators in ``util.py`` returned a
# *new* subclass ``Wrapped(task_that_inherits)`` (decorated with
# ``_task_wraps`` so it copied the original ``__name__``/``__module__``).
# Consequently the decorated class had an extra MRO level whose string
# representation was identical to the original class, i.e.
# ``str(Child.__mro__[0]) == str(Child.__mro__[1])``.  The fix mutates the
# class in place and returns it unchanged, so the first two MRO entries are
# genuinely distinct (Child vs its real parent).
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``requires``
#   or ``inherits`` (the trigger: the decorator, which on the buggy build
#   makes the first two MRO entries string-equal) or ``plain`` (no
#   decorator, so the entries always differ).  The harness prints
#   ``repr(str(mro[0]) != str(mro[1]))``; the oracle -- knowing the CORRECT
#   behaviour is that those two entries differ -- returns PASSING iff the
#   printed value is ``True``.
# ======================================================================


class Luigi5API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "True":
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi5TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))


class Luigi5SystemtestGenerator(SystemtestGenerator, Luigi5TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(("requires", "inherits"))
        return f"{mode} {self.generate_word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"plain {self.generate_word()}", TestResult.PASSING


class Luigi5UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi5TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.ImportFrom(
                module="luigi.util",
                names=[ast.alias(name="requires"), ast.alias(name="inherits")],
                level=0,
            ),
        ]

    def _body(self, mode: str, w: str) -> List[ast.stmt]:
        lines = [
            f"Required = type('Req_{w}', (luigi.Task,), {{}})",
            f"Parent = type('Par_{w}', (luigi.Task,), {{}})",
            f"Child = type('Child_{w}', (Parent,), {{}})",
        ]
        if mode == "requires":
            lines.append("Child = requires(Required)(Child)")
        elif mode == "inherits":
            lines.append("Child = inherits(Required)(Child)")
        lines.append(
            "self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))"
        )
        return ast.parse("\n".join(lines)).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        mode = random.choice(("requires", "inherits"))
        test = self.get_empty_test()
        test.body = self._body(mode, self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("plain", self.generate_word())
        return test, TestResult.PASSING


grammar_5: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word>"],
            "<mode>": ["requires", "inherits", "plain"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_5)


# ======================================================================
# bug_13: ``LocalFileSystem.move`` created the destination directory with
# ``self.fs.mkdir(d)`` -- but ``LocalFileSystem`` has no ``fs`` attribute,
# so moving a file into a not-yet-existing directory raised
# ``AttributeError``.  The fix calls ``self.mkdir(d)``.
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``newdir``
#   (the trigger: destination in a non-existent sub-directory, which forces
#   the ``mkdir`` path) or ``samedir`` (destination in the existing base
#   directory, so the ``mkdir`` path is skipped).  The harness performs the
#   move and prints ``HARNESS_OK`` if the destination exists afterwards;
#   the oracle -- knowing the CORRECT behaviour is that the move always
#   succeeds -- returns PASSING iff ``HARNESS_OK`` was printed.
# ======================================================================


class Luigi13API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi13TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi13SystemtestGenerator(SystemtestGenerator, Luigi13TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"newdir {self.generate_word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"samedir {self.generate_word()}", TestResult.PASSING


class Luigi13UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi13TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="os")]),
            ast.Import(names=[ast.alias(name="tempfile")]),
            ast.ImportFrom(
                module="luigi.file",
                names=[ast.alias(name="LocalFileSystem")],
                level=0,
            ),
        ]

    def _body(self, mode: str, w: str) -> List[ast.stmt]:
        if mode == "newdir":
            dest = f"os.path.join(base, 'newdir_{w}', 'dest.txt')"
        else:
            dest = "os.path.join(base, 'dest.txt')"
        return ast.parse(
            f"base = tempfile.mkdtemp(prefix='t4p_{w}_')\n"
            f"src = os.path.join(base, 'src.txt')\n"
            f"open(src, 'w').close()\n"
            f"dest = {dest}\n"
            f"LocalFileSystem().move(src, dest)\n"
            f"self.assertTrue(os.path.exists(dest))\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("newdir", self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("samedir", self.generate_word())
        return test, TestResult.PASSING


grammar_13: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word>"],
            "<mode>": ["newdir", "samedir"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_13)


# ======================================================================
# bug_27: ``Parameter.parse_from_input`` resolved an empty command-line
# value through the *global* ``self.value`` (config_path/default) and had
# no ``task_name`` argument, so a value configured under the task's own
# section (``[TaskName] param = ...``) was ignored when building tasks from
# the command line.  The fix adds a ``task_name`` argument and resolves via
# ``has_task_value``/``task_value`` (task-scoped config).
#
# System-test format:  ``<mode> <section> <name> <value>`` where ``<mode>``
#   is ``cfg`` (the trigger: an empty input resolved via the task-scoped
#   config, which the buggy ``parse_from_input`` cannot even accept a
#   ``task_name`` for) or ``explicit`` (a non-empty input value, parsed
#   directly on both builds).  In both cases the CORRECT result equals
#   ``<value>``; the harness prints the resolved value and the oracle
#   returns PASSING iff it equals ``<value>``.
# ======================================================================


class Luigi27API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            expected = process.args[5]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Luigi27TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    def generate_triple(self) -> Tuple[str, str, str]:
        return self.generate_word(), self.generate_word(), self.generate_word()


class Luigi27SystemtestGenerator(SystemtestGenerator, Luigi27TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        s, n, v = self.generate_triple()
        return f"cfg {s} {n} {v}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        s, n, v = self.generate_triple()
        return f"explicit {s} {n} {v}", TestResult.PASSING


class Luigi27UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi27TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.Import(names=[ast.alias(name="luigi.configuration")]),
        ]

    def _body(self, mode: str, s: str, n: str, v: str) -> List[ast.stmt]:
        if mode == "cfg":
            call = f"p.parse_from_input({n!r}, '', task_name={s!r})"
        else:
            call = f"p.parse_from_input({n!r}, {v!r})"
        return ast.parse(
            f"conf = luigi.configuration.get_config()\n"
            f"if not conf.has_section({s!r}):\n"
            f"    conf.add_section({s!r})\n"
            f"conf.set({s!r}, {n!r}, {v!r})\n"
            f"p = luigi.Parameter(default='defval')\n"
            f"self.assertEqual({call}, {v!r})\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        s, n, v = self.generate_triple()
        test = self.get_empty_test()
        test.body = self._body("cfg", s, n, v)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        s, n, v = self.generate_triple()
        test = self.get_empty_test()
        test.body = self._body("explicit", s, n, v)
        return test, TestResult.PASSING


grammar_27: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word> <word> <word>"],
            "<mode>": ["cfg", "explicit"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_27)


# ======================================================================
# bug_22: ``scheduler.Worker.__init__`` used ``last_active=None`` as the
# default, so a ``Worker`` created without an explicit ``last_active`` had
# ``last_active is None``.  ``Worker.prune`` then evaluates
# ``self.last_active + config.worker_disconnect_delay`` which raises
# ``TypeError`` (``None + int``) — i.e. pruning a freshly-created worker
# crashes.  The fix defaults ``last_active`` to a timestamp so pruning
# always works.
#
# System-test format:  ``<mode> <id> <delay> [<last_active>]`` where
#   ``<mode>`` is ``default`` (the trigger: no ``last_active`` given, so it
#   defaults to ``None`` on the buggy build and pruning crashes) or
#   ``explicit`` (a numeric ``last_active`` is supplied, so pruning works on
#   both builds).  The harness creates the worker, calls ``prune`` and
#   prints ``HARNESS_OK``; the oracle -- knowing the CORRECT behaviour is
#   that pruning always succeeds -- returns PASSING iff ``HARNESS_OK``.
# ======================================================================


class Luigi22API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi22TestGenerator:
    @staticmethod
    def generate_int(lo: int = 1, hi: int = 99999) -> int:
        return random.randint(lo, hi)


class Luigi22SystemtestGenerator(SystemtestGenerator, Luigi22TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"default {self.generate_int()} {self.generate_int()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"explicit {self.generate_int()} {self.generate_int()} "
            f"{self.generate_int()}",
            TestResult.PASSING,
        )


class Luigi22UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi22TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="types")]),
            ast.Import(names=[ast.alias(name="luigi.scheduler")]),
        ]

    def _body(self, mode: str, wid: int, delay: int, la: int) -> List[ast.stmt]:
        if mode == "explicit":
            create = f"w = luigi.scheduler.Worker({wid}, last_active={la})"
        else:
            create = f"w = luigi.scheduler.Worker({wid})"
        return ast.parse(
            f"{create}\n"
            f"cfg = types.SimpleNamespace(worker_disconnect_delay={delay})\n"
            f"w.prune(cfg)\n"
            f"self.assertIsNotNone(w.last_active)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(
            "default", self.generate_int(), self.generate_int(), 0
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(
            "explicit", self.generate_int(), self.generate_int(), self.generate_int()
        )
        return test, TestResult.PASSING


grammar_22: Grammar = clean_up(
    dict(
        {
            "<start>": ["default <int> <int>", "explicit <int> <int> <int>"],
            "<int>": ["<digit>", "<digit><int>"],
            "<digit>": srange(string.digits),
        }
    )
)

assert is_valid_grammar(grammar_22)


# ======================================================================
# bug_26: ``HadoopJarJobRunner.run_job`` guarded a missing jar with
# ``if not job.jar() or not os.path.exists(job.jar()):`` and then logged
# ``os.path.abspath(job.jar())``.  When ``job.jar()`` is ``None`` the
# ``os.path.abspath(None)`` call raises ``TypeError`` instead of the
# intended ``HadoopJarJobError`` -- i.e. a task with an undefined jar
# crashes with the wrong exception.  The fix raises
# ``HadoopJarJobError("Jar not defined")`` up-front when the jar is falsy.
#
# System-test format:  ``<mode> <name>`` where ``<mode>`` is ``none`` (the
#   trigger: ``jar()`` returns ``None`` -> ``TypeError`` on the buggy build,
#   ``HadoopJarJobError`` on the fixed one) or ``missing`` (``jar()`` returns
#   a non-existent path -> ``HadoopJarJobError`` on both builds).  The
#   correct behaviour is that running a job with no usable jar raises
#   ``HadoopJarJobError``; the harness runs it, prints ``HARNESS_OK`` iff
#   that exception was raised, and the oracle returns PASSING iff so.
# ======================================================================


class Luigi26API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi26TestGenerator:
    @staticmethod
    def generate_name() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi26SystemtestGenerator(SystemtestGenerator, Luigi26TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"none {self.generate_name()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"missing {self.generate_name()}", TestResult.PASSING


class Luigi26UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi26TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="luigi.contrib.hadoop_jar",
                names=[
                    ast.alias(name="HadoopJarJobRunner"),
                    ast.alias(name="HadoopJarJobError"),
                ],
                level=0,
            )
        ]

    def _body(self, mode: str, name: str) -> List[ast.stmt]:
        if mode == "none":
            jar_return = "None"
        else:
            jar_return = repr(f"/no/such/dir_{name}/{name}.jar")
        return ast.parse(
            f"class FakeJob_{name}:\n"
            f"    def ssh(self):\n        return None\n"
            f"    def jar(self):\n        return {jar_return}\n"
            f"runner = HadoopJarJobRunner()\n"
            f"self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_{name}())\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("none", self.generate_name())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("missing", self.generate_name())
        return test, TestResult.PASSING


grammar_26: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <name>"],
            "<mode>": ["none", "missing"],
            "<name>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_26)


# ======================================================================
# bug_12: ``luigi.contrib.hdfs.get_autoconfig_client`` rebuilt the HDFS
# client on every call, so two consecutive calls returned *different*
# client objects.  The fix caches the client in a per-thread
# ``threading.local`` (``client_cache`` argument), so within one thread the
# same object is returned each time.
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``same`` (the
#   trigger: two calls must return the identical object -- true on the fixed
#   build, false on the buggy one) or ``instance`` (a single call returns a
#   non-None client -- true on both builds).  ``<word>`` only makes the
#   inputs distinct.  The correct behaviour is that repeated calls are
#   cached; the harness prints ``HARNESS_OK`` iff the checked property holds
#   and the oracle returns PASSING iff so.
# ======================================================================


class Luigi12API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi12TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi12SystemtestGenerator(SystemtestGenerator, Luigi12TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"same {self.generate_word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"instance {self.generate_word()}", TestResult.PASSING


class Luigi12UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi12TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="luigi.contrib.hdfs",
                names=[ast.alias(name="get_autoconfig_client")],
                level=0,
            )
        ]

    def _body(self, mode: str, word: str) -> List[ast.stmt]:
        if mode == "same":
            check = (
                "self.assertIs(get_autoconfig_client(), get_autoconfig_client())"
            )
        else:
            check = "self.assertIsNotNone(get_autoconfig_client())"
        return ast.parse(f"note = {word!r}\n{check}\n").body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("same", self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("instance", self.generate_word())
        return test, TestResult.PASSING


grammar_12: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word>"],
            "<mode>": ["same", "instance"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_12)


# ======================================================================
# bug_28: ``HiveCommandClient.table_exists`` compared the table name
# case-sensitively (``table in stdout``), so a table queried with different
# casing than Hive reports (Hive lower-cases table names) was reported as
# missing.  The fix compares ``table.lower() in stdout``.
#
# System-test format:  ``<mode> <name>`` where ``<mode>`` is ``mixed`` (the
#   trigger: a mixed-case table name whose lower-cased form is what Hive
#   returns -> found only on the fixed build) or ``plain`` (an all-lowercase
#   name that matches exactly -> found on both builds).  ``run_hive_cmd`` is
#   stubbed to return the lower-cased name.  The correct behaviour is that
#   the table is found; the harness prints ``HARNESS_OK`` iff
#   ``table_exists`` is truthy and the oracle returns PASSING iff so.
# ======================================================================


class Luigi28API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi28TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi28SystemtestGenerator(SystemtestGenerator, Luigi28TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"mixed {self.generate_word().capitalize()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"plain {self.generate_word()}", TestResult.PASSING


class Luigi28UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi28TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(
                names=[ast.alias(name="luigi.contrib.hive", asname="hive")]
            )
        ]

    def _body(self, table: str) -> List[ast.stmt]:
        lower = table.lower()
        return ast.parse(
            f"hive.run_hive_cmd = lambda *a, **k: 'OK\\n{lower}'\n"
            f"client = hive.HiveCommandClient()\n"
            f"self.assertTrue(client.table_exists({table!r}))\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_word().capitalize())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_word())
        return test, TestResult.PASSING


grammar_28: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <name>"],
            "<mode>": ["mixed", "plain"],
            "<name>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_letters),
        }
    )
)

assert is_valid_grammar(grammar_28)


# ======================================================================
# bug_4: ``S3CopyToTable.copy`` computed ``if len(self.columns) > 0`` -- but
# ``columns`` may legitimately be ``None`` (no explicit column list), and
# ``len(None)`` raises ``TypeError``, crashing the COPY.  The fix guards
# with ``if self.columns and len(self.columns) > 0``.
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``none`` (the
#   trigger: ``columns=None`` -> ``TypeError`` on the buggy build, clean
#   COPY on the fixed one) or ``cols`` (a non-empty column list -> works on
#   both builds).  ``<word>`` is the table name (distinctness).  The correct
#   behaviour is that ``copy`` runs without error; the harness prints
#   ``HARNESS_OK`` iff it does and the oracle returns PASSING iff so.
# ======================================================================


class Luigi4API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi4TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi4SystemtestGenerator(SystemtestGenerator, Luigi4TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"none {self.generate_word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"cols {self.generate_word()}", TestResult.PASSING


class Luigi4UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi4TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.Import(names=[ast.alias(name="luigi.contrib.redshift")]),
            ast.ImportFrom(
                module="unittest", names=[ast.alias(name="mock")], level=0
            ),
        ]

    def _body(self, mode: str, word: str) -> List[ast.stmt]:
        cls_name = f"Dummy_{mode}_{word}"
        cols = "None" if mode == "none" else "(('a', 'int'), ('b', 'varchar'))"
        return ast.parse(
            f"class {cls_name}(luigi.contrib.redshift.S3CopyToTable):\n"
            f"    host = 'h'\n"
            f"    database = 'd'\n"
            f"    user = 'u'\n"
            f"    password = 'p'\n"
            f"    aws_access_key_id = 'key'\n"
            f"    aws_secret_access_key = 'secret'\n"
            f"    copy_options = ''\n"
            f"    table = luigi.Parameter(default={word!r})\n"
            f"    columns = {cols}\n"
            f"    def s3_load_path(self):\n"
            f"        return 's3://bucket/key'\n"
            f"task = {cls_name}()\n"
            f"luigi.contrib.redshift.S3CopyToTable.copy("
            f"task, mock.Mock(), 's3://bucket/key')\n"
            f"self.assertTrue(True)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("none", self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("cols", self.generate_word())
        return test, TestResult.PASSING


grammar_4: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word>"],
            "<mode>": ["none", "cols"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_4)


# ======================================================================
# bug_10: ``scheduler.Worker.get_pending_tasks`` -- when the worker has at
# least as many tasks as there are pending tasks in the whole state -- fell
# into an ``else`` branch that returned ``state.get_pending_tasks()``, i.e.
# *every* pending task in the scheduler, not just the ones belonging to this
# worker.  The fix filters that result by ``self.id in task.workers``.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``trigger`` (the
#   target worker owns 1 pending + 1 done task while another worker owns a
#   pending task, forcing the buggy ``else`` branch that leaks the other
#   worker's task) or ``safe`` (the target owns just 1 pending task while
#   many other pending tasks exist, forcing the correct ``if`` branch on
#   both builds).  ``<tag>`` makes ids distinct.  The correct behaviour is
#   that the worker's pending set is exactly its own pending task; the
#   harness prints ``HARNESS_OK`` iff so and the oracle returns PASSING iff.
# ======================================================================


class Luigi10API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi10TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi10SystemtestGenerator(SystemtestGenerator, Luigi10TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"trigger {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"safe {self.generate_tag()}", TestResult.PASSING


class Luigi10UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi10TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="luigi.scheduler")])]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        tw, ow, tp, op = f"TW_{tag}", f"OW_{tag}", f"TP_{tag}", f"OP_{tag}"
        extra = ""
        if mode == "trigger":
            extra = (
                f"sch.add_task(worker={tw!r}, task_id='DN_{tag}', status='DONE')\n"
            )
        else:
            extra = (
                f"sch.add_task(worker={ow!r}, task_id='EP1_{tag}', status='PENDING')\n"
                f"sch.add_task(worker={ow!r}, task_id='EP2_{tag}', status='PENDING')\n"
            )
        return ast.parse(
            f"sch = luigi.scheduler.Scheduler()\n"
            f"sch.add_task(worker={tw!r}, task_id={tp!r}, status='PENDING')\n"
            f"sch.add_task(worker={ow!r}, task_id={op!r}, status='PENDING')\n"
            f"{extra}"
            f"st = sch._state\n"
            f"target = st.get_worker({tw!r})\n"
            f"got = {{t.id for t in target.get_pending_tasks(st)}}\n"
            f"self.assertEqual(got, {{{tp!r}}})\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("trigger", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("safe", self.generate_tag())
        return test, TestResult.PASSING


grammar_10: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["trigger", "safe"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_10)


# ======================================================================
# bug_11: ``Scheduler.get_work`` batched together *all* same-family
# batchable tasks without checking that each was actually schedulable, so a
# batch could include tasks whose dependencies were not yet done.  The fix
# adds ``and self._schedulable(task)`` to the batching condition, excluding
# not-ready tasks from the batch.
#
# System-test format:  ``<mode> <tag> <pattern>`` where ``<pattern>`` is a
#   string of ``r`` (ready: dep already DONE) / ``n`` (not-ready: dep on an
#   unfinished task) characters.  ``<mode>`` is ``mix`` (the trigger: the
#   pattern contains at least one ``n``, so the buggy build wrongly batches
#   the not-ready tasks) or ``allready`` (all ``r`` -> both builds batch
#   everything).  ``<tag>`` makes ids distinct.  The correct batch contains
#   exactly the ready tasks' params; the harness prints ``HARNESS_OK`` iff
#   the batch equals that and the oracle returns PASSING iff so.
# ======================================================================


class Luigi11API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi11TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))

    def generate_mix_pattern(self) -> str:
        length = random.randint(3, 6)
        # first task ready; ensure at least one 'n'
        chars = ["r"] + [random.choice("rn") for _ in range(length - 1)]
        if "n" not in chars:
            chars[random.randint(1, length - 1)] = "n"
        return "".join(chars)

    @staticmethod
    def generate_allready_pattern() -> str:
        return "r" * random.randint(2, 6)


class Luigi11SystemtestGenerator(SystemtestGenerator, Luigi11TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"mix {self.generate_tag()} {self.generate_mix_pattern()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"allready {self.generate_tag()} {self.generate_allready_pattern()}",
            TestResult.PASSING,
        )


_LUIGI11_CONF = (
    "{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, "
    "'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, "
    "'disable_hard_timeout': 3600}"
)


class Luigi11UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi11TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[ast.alias(name="Scheduler"), ast.alias(name="DONE")],
                level=0,
            )
        ]

    def _body(self, tag: str, pattern: str) -> List[ast.stmt]:
        fam = f"A{tag}"
        ready = [str(i) for i, ch in enumerate(pattern, 1) if ch == "r"]
        lines = [
            f"sch = Scheduler(**{_LUIGI11_CONF})",
            f"sch.add_task_batcher(worker='myworker', task_family={fam!r}, "
            f"batched_args=['a'])",
        ]
        for i, ch in enumerate(pattern, 1):
            dep = f"NOTDONE_{tag}" if ch == "n" else f"DONE_{tag}"
            lines.append(
                f"sch.add_task(worker='myworker', task_id='{fam}_a_{i}', "
                f"family={fam!r}, params={{'a': {str(i)!r}}}, batchable=True, "
                f"deps=[{dep!r}])"
            )
        lines.append(
            f"sch.add_task(worker='myworker', task_id='NOTDONE_{tag}', runnable=False)"
        )
        lines.append(
            f"sch.add_task(worker='myworker', task_id='DONE_{tag}', status=DONE)"
        )
        lines.append(
            "got = sch.get_work(worker='myworker')['task_params'].get('a', [])"
        )
        lines.append(f"self.assertEqual(got, {ready!r})")
        return ast.parse("\n".join(lines)).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_tag(), self.generate_mix_pattern())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.generate_tag(), self.generate_allready_pattern())
        return test, TestResult.PASSING


grammar_11: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag> <pattern>"],
            "<mode>": ["mix", "allready"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
            "<pattern>": ["<rn>", "<rn><pattern>"],
            "<rn>": ["r", "n"],
        }
    )
)

assert is_valid_grammar(grammar_11)


# ======================================================================
# bug_31: ``CentralPlannerScheduler.get_work`` computed
# ``in_workers = assistant or worker in task.workers``.  For an *assistant*
# this was always true, so an assistant could be handed an external
# (``runnable=False``) task belonging to another worker.  The fix uses
# ``(assistant and task.workers) or worker in task.workers`` so a bare
# external task is not offered to an assistant.
#
# System-test format:  ``<mode> <owner> <task> <assistant>`` where
#   ``<mode>`` is ``external`` (the trigger: an external task owned by
#   another worker is wrongly returned to the assistant on the buggy build)
#   or ``done`` (a DONE task -> no work returned on both builds).  The
#   correct behaviour is that the assistant gets ``task_id is None``; the
#   harness prints ``HARNESS_OK`` iff so and the oracle returns PASSING iff.
# ======================================================================


class Luigi31API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi31TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))

    def generate_triple(self) -> Tuple[str, str, str]:
        return self.generate_word(), self.generate_word(), self.generate_word()


class Luigi31SystemtestGenerator(SystemtestGenerator, Luigi31TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        o, t, a = self.generate_triple()
        return f"external {o} {t} {a}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        o, t, a = self.generate_triple()
        return f"done {o} {t} {a}", TestResult.PASSING


_LUIGI31_CONF = (
    "{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, "
    "'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3}"
)


class Luigi31UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi31TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[
                    ast.alias(name="CentralPlannerScheduler"),
                    ast.alias(name="DONE"),
                ],
                level=0,
            )
        ]

    def _body(self, mode: str, owner: str, task: str, asst: str) -> List[ast.stmt]:
        if mode == "external":
            add = f"sch.add_task({owner!r}, task_id={task!r}, runnable=False)"
        else:
            add = f"sch.add_task({owner!r}, task_id={task!r}, status=DONE)"
        return ast.parse(
            f"sch = CentralPlannerScheduler(**{_LUIGI31_CONF})\n"
            f"{add}\n"
            f"r = sch.get_work({asst!r}, assistant=True)\n"
            f"self.assertIsNone(r['task_id'])\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        o, t, a = self.generate_triple()
        test = self.get_empty_test()
        test.body = self._body("external", o, t, a)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        o, t, a = self.generate_triple()
        test = self.get_empty_test()
        test.body = self._body("done", o, t, a)
        return test, TestResult.PASSING


grammar_31: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word> <word> <word>"],
            "<mode>": ["external", "done"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_31)


# ======================================================================
# bug_23: like bug_22, ``scheduler.Worker.__init__`` stored
# ``self.last_active = last_active`` with a ``None`` default, so a freshly
# created worker had ``last_active is None`` and ``prune`` crashed with
# ``TypeError`` (``None + int``).  The fix stores ``last_active or
# time.time()`` (this commit also adds ``prune_on_get_work``).
#
# System-test format:  ``<mode> <id> <delay> [<last_active>]`` -- ``default``
#   (trigger: no ``last_active`` -> crash on the buggy build) or ``explicit``
#   (a numeric ``last_active`` -> works on both).  The correct behaviour is
#   that pruning a new worker succeeds; the harness prints ``HARNESS_OK`` iff
#   it does and the oracle returns PASSING iff so.
# ======================================================================


class Luigi23API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi23TestGenerator:
    @staticmethod
    def generate_int(lo: int = 1, hi: int = 99999) -> int:
        return random.randint(lo, hi)


class Luigi23SystemtestGenerator(SystemtestGenerator, Luigi23TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"default {self.generate_int()} {self.generate_int()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"explicit {self.generate_int()} {self.generate_int()} "
            f"{self.generate_int()}",
            TestResult.PASSING,
        )


class Luigi23UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi23TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="types")]),
            ast.Import(names=[ast.alias(name="luigi.scheduler")]),
        ]

    def _body(self, mode: str, wid: int, delay: int, la: int) -> List[ast.stmt]:
        if mode == "explicit":
            create = f"w = luigi.scheduler.Worker({wid}, last_active={la})"
        else:
            create = f"w = luigi.scheduler.Worker({wid})"
        return ast.parse(
            f"{create}\n"
            f"cfg = types.SimpleNamespace(worker_disconnect_delay={delay})\n"
            f"w.prune(cfg)\n"
            f"self.assertIsNotNone(w.last_active)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("default", self.generate_int(), self.generate_int(), 0)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(
            "explicit", self.generate_int(), self.generate_int(), self.generate_int()
        )
        return test, TestResult.PASSING


grammar_23: Grammar = clean_up(
    dict(
        {
            "<start>": ["default <int> <int>", "explicit <int> <int> <int>"],
            "<int>": ["<digit>", "<digit><int>"],
            "<digit>": srange(string.digits),
        }
    )
)

assert is_valid_grammar(grammar_23)


# ======================================================================
# bug_16: ``CentralPlannerScheduler.prune`` used
# ``if task.id not in necessary_tasks and self._state.prune(task, cfg)``.
# Because ``and`` short-circuits, ``self._state.prune`` (which also resets
# FAILED tasks to PENDING after the retry delay and re-enables disabled
# tasks) was skipped for *necessary* tasks -- so a still-needed FAILED task
# was never retried when an assistant kept it necessary.  The fix computes
# ``removed = self._state.prune(...)`` unconditionally, then decides removal.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``assistant``
#   (the trigger: an assistant keeps the FAILED task necessary, so the buggy
#   build never resets it to PENDING) or ``plain`` (no assistant, so the
#   task is not necessary and gets reset on both builds).  After the retry
#   delay the correct status is PENDING; the harness prints ``HARNESS_OK``
#   iff the task became PENDING and the oracle returns PASSING iff so.
# ======================================================================


class Luigi16API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi16TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi16SystemtestGenerator(SystemtestGenerator, Luigi16TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"assistant {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"plain {self.generate_tag()}", TestResult.PASSING


_LUIGI16_CONF = (
    "{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, "
    "'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, "
    "'disable_hard_timeout': 3600}"
)


class Luigi16UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi16TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="time")]),
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[
                    ast.alias(name="CentralPlannerScheduler"),
                    ast.alias(name="FAILED"),
                ],
                level=0,
            ),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        w, tid = f"W_{tag}", f"A_{tag}"
        if mode == "assistant":
            setup = (
                f"    sch.add_worker({w!r}, [('assistant', True)])\n"
                f"    sch.add_task(worker={w!r}, task_id={tid!r}, "
                f"status=FAILED, assistant=True)\n"
            )
        else:
            setup = (
                f"    sch.add_task(worker={w!r}, task_id={tid!r}, status=FAILED)\n"
            )
        return ast.parse(
            f"_orig = time.time\n"
            f"try:\n"
            f"    time.time = lambda: 0\n"
            f"    sch = CentralPlannerScheduler(**{_LUIGI16_CONF})\n"
            f"{setup}"
            f"    time.time = lambda: 101\n"
            f"    sch.ping(worker={w!r})\n"
            f"    status = sch.task_list('', '')[{tid!r}]['status']\n"
            f"finally:\n"
            f"    time.time = _orig\n"
            f"self.assertEqual(status, 'PENDING')\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("assistant", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("plain", self.generate_tag())
        return test, TestResult.PASSING


grammar_16: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["assistant", "plain"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_16)


# ======================================================================
# bug_15: ``SimpleTaskState.get_necessary_tasks`` treated only ``DONE`` and
# ``DISABLED`` as finished, so an ``UNKNOWN`` task was kept "necessary" by an
# assistant and therefore never pruned/removed.  The fix adds ``UNKNOWN`` to
# the finished set so such tasks are not nurtured.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``unknown`` (the
#   trigger: an UNKNOWN task is wrongly kept alive on the buggy build) or
#   ``done``/``disabled`` (finished statuses that are removed on both
#   builds).  After pruning with an assistant present the correct behaviour
#   is that the task is removed; the harness prints ``HARNESS_OK`` iff the
#   task no longer exists and the oracle returns PASSING iff so.
# ======================================================================


class Luigi15API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi15TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi15SystemtestGenerator(SystemtestGenerator, Luigi15TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"unknown {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        mode = random.choice(("done", "disabled"))
        return f"{mode} {self.generate_tag()}", TestResult.PASSING


class Luigi15UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi15TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="time")]),
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[ast.alias(name="CentralPlannerScheduler")],
                level=0,
            ),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        w, up, tid = f"AS_{tag}", f"UP_{tag}", f"T_{tag}"
        status = mode.upper()
        return ast.parse(
            f"_orig = time.time\n"
            f"try:\n"
            f"    time.time = lambda: 1\n"
            f"    sch = CentralPlannerScheduler(retry_delay=100000000000)\n"
            f"    sch.add_worker({w!r}, [('assistant', True)])\n"
            f"    sch.ping(worker={w!r})\n"
            f"    sch.add_task(worker={up!r}, task_id={tid!r}, status={status!r})\n"
            f"    time.time = lambda: 100000\n"
            f"    sch.ping(worker={w!r})\n"
            f"    sch.prune()\n"
            f"    time.time = lambda: 200000\n"
            f"    sch.ping(worker={w!r})\n"
            f"    sch.prune()\n"
            f"    exists = {tid!r} in sch.task_list(None, '')\n"
            f"finally:\n"
            f"    time.time = _orig\n"
            f"self.assertFalse(exists)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("unknown", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        mode = random.choice(("done", "disabled"))
        test = self.get_empty_test()
        test.body = self._body(mode, self.generate_tag())
        return test, TestResult.PASSING


grammar_15: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["unknown", "done", "disabled"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_15)


# ======================================================================
# bug_19: ``SimpleTaskState.set_status`` ran the FAILED-handling block
# (``if new_status == FAILED and task.can_disable():`` -> add_failure /
# re-disable) even for tasks that were *already* DISABLED.  That bumped the
# ``scheduler_disable_time`` on every failure, so a disabled task could
# never be automatically re-enabled after ``disable_persist`` elapsed.  The
# fix adds ``and task.status != DISABLED``.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``reenable`` (the
#   trigger: ``disable_failures=1`` disables the task, which must re-enable
#   to FAILED after ``disable_persist`` -- but stays DISABLED on the buggy
#   build) or ``stayfailed`` (a high ``disable_failures`` so the task is
#   never disabled and stays FAILED on both builds).  The correct status
#   after the persist window is FAILED; the harness prints ``HARNESS_OK``
#   iff so and the oracle returns PASSING iff so.
# ======================================================================


class Luigi19API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi19TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi19SystemtestGenerator(SystemtestGenerator, Luigi19TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"reenable {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"stayfailed {self.generate_tag()}", TestResult.PASSING


class Luigi19UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi19TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="time")]),
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[
                    ast.alias(name="CentralPlannerScheduler"),
                    ast.alias(name="FAILED"),
                ],
                level=0,
            ),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        w, tid = f"w_{tag}", f"T_{tag}"
        df = 1 if mode == "reenable" else 1000
        return ast.parse(
            f"_orig = time.time\n"
            f"try:\n"
            f"    time.time = lambda: 0\n"
            f"    sch = CentralPlannerScheduler(disable_failures={df}, "
            f"disable_persist=100)\n"
            f"    sch.add_task(worker={w!r}, task_id={tid!r}, status=FAILED)\n"
            f"    time.time = lambda: 101\n"
            f"    status = sch.task_list('', '')[{tid!r}]['status']\n"
            f"finally:\n"
            f"    time.time = _orig\n"
            f"self.assertEqual(status, 'FAILED')\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("reenable", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("stayfailed", self.generate_tag())
        return test, TestResult.PASSING


grammar_19: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["reenable", "stayfailed"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_19)


# ======================================================================
# bug_18: ``SimpleTaskState.set_status`` had ``elif
# task.scheduler_disable_time is not None: return`` -- so once a task had
# been *auto*-disabled (scheduler_disable_time set), a subsequent *manual*
# ``DISABLED`` was ignored (early return), leaving scheduler_disable_time in
# place; the task then auto-re-enabled after ``disable_persist``.  The fix
# adds ``and new_status != DISABLED`` so a manual disable is applied,
# clearing the auto-disable timer and making the disable permanent.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``automanual``
#   (the trigger: auto-disable via 2 failures, then a manual disable -- must
#   stay DISABLED, but re-enables to FAILED on the buggy build) or
#   ``manualonly`` (a plain manual disable that stays DISABLED on both).
#   The correct status after the persist window is DISABLED; the harness
#   prints ``HARNESS_OK`` iff so and the oracle returns PASSING iff so.
# ======================================================================


class Luigi18API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi18TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi18SystemtestGenerator(SystemtestGenerator, Luigi18TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"automanual {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"manualonly {self.generate_tag()}", TestResult.PASSING


class Luigi18UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi18TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="time")]),
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[
                    ast.alias(name="CentralPlannerScheduler"),
                    ast.alias(name="FAILED"),
                    ast.alias(name="DISABLED"),
                ],
                level=0,
            ),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        w, tid = f"w_{tag}", f"T_{tag}"
        if mode == "automanual":
            setup = (
                f"    sch.add_task(worker={w!r}, task_id={tid!r}, status=FAILED)\n"
                f"    sch.add_task(worker={w!r}, task_id={tid!r}, status=FAILED)\n"
                f"    sch.add_task(worker={w!r}, task_id={tid!r}, status=DISABLED)\n"
            )
        else:
            setup = (
                f"    sch.add_task(worker={w!r}, task_id={tid!r}, status=DISABLED)\n"
            )
        return ast.parse(
            f"_orig = time.time\n"
            f"try:\n"
            f"    time.time = lambda: 0\n"
            f"    sch = CentralPlannerScheduler(disable_failures=2, "
            f"disable_persist=100)\n"
            f"{setup}"
            f"    time.time = lambda: 101\n"
            f"    status = sch.task_list('', '')[{tid!r}]['status']\n"
            f"finally:\n"
            f"    time.time = _orig\n"
            f"self.assertEqual(status, 'DISABLED')\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("automanual", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("manualonly", self.generate_tag())
        return test, TestResult.PASSING


grammar_18: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["automanual", "manualonly"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_18)


# ======================================================================
# bug_14: the ``scheduler`` config defaulted ``disable_failures`` and
# ``disable_hard_timeout`` to ``None``.  With only ``disable_hard_timeout``
# configured, ``Task.has_excessive_failures`` still evaluated
# ``num_failures() >= self.disable_failures`` where ``disable_failures`` is
# ``None`` -> ``TypeError`` (int >= NoneType), crashing the scheduler when a
# task failed.  The fix defaults both to ``999999999`` (and drops the now
# unnecessary ``can_disable`` guard).
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``hardonly`` (the
#   trigger: only ``disable_hard_timeout`` set, so failing a task crashes on
#   the buggy build) or ``bothset`` (both limits set, so no crash on either
#   build).  The correct behaviour is that failing a task never crashes the
#   scheduler; the harness prints ``HARNESS_OK`` iff it completes and the
#   oracle returns PASSING iff so.
# ======================================================================


class Luigi14API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi14TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi14SystemtestGenerator(SystemtestGenerator, Luigi14TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"hardonly {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"bothset {self.generate_tag()}", TestResult.PASSING


class Luigi14UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi14TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="time")]),
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[
                    ast.alias(name="CentralPlannerScheduler"),
                    ast.alias(name="FAILED"),
                ],
                level=0,
            ),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        w, a, b = f"w_{tag}", f"A_{tag}", f"B_{tag}"
        if mode == "hardonly":
            create = "CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)"
        else:
            create = (
                "CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, "
                "disable_failures=100)"
            )
        return ast.parse(
            f"_orig = time.time\n"
            f"try:\n"
            f"    time.time = lambda: 1\n"
            f"    sch = {create}\n"
            f"    sch.add_worker({w!r}, [])\n"
            f"    sch.ping(worker={w!r})\n"
            f"    time.time = lambda: 2\n"
            f"    sch.add_task(worker={w!r}, task_id={a!r})\n"
            f"    sch.add_task(worker={w!r}, task_id={b!r}, deps=[{a!r}])\n"
            f"    sch.get_work(worker={w!r})\n"
            f"    sch.add_task(worker={w!r}, task_id={a!r}, status=FAILED)\n"
            f"    time.time = lambda: 10\n"
            f"    sch.prune()\n"
            f"    sch.get_work(worker={w!r})\n"
            f"finally:\n"
            f"    time.time = _orig\n"
            f"self.assertTrue(True)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("hardonly", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("bothset", self.generate_tag())
        return test, TestResult.PASSING


grammar_14: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["hardonly", "bothset"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_14)


# ======================================================================
# bug_7: ``Scheduler.add_task`` only refused to re-schedule a RUNNING task
# when the incoming status was ``PENDING`` (``not (task.status in (RUNNING,
# BATCH_RUNNING) and status == PENDING)``).  So another worker could
# override the status of a task actively RUNNING on a different worker (e.g.
# to UNKNOWN), losing the RUNNING state.  The fix blocks any non-terminal
# override from a worker that is not the one running the task.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``override`` (the
#   trigger: a second worker sets the RUNNING task to UNKNOWN -- accepted on
#   the buggy build, blocked on the fixed one) or ``blocked`` (the second
#   worker sets PENDING, which is blocked on both builds).  The correct
#   behaviour is that the task stays RUNNING; the harness prints
#   ``HARNESS_OK`` iff the task is still RUNNING and the oracle returns
#   PASSING iff so.
# ======================================================================


class Luigi7API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi7TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi7SystemtestGenerator(SystemtestGenerator, Luigi7TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"override {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"blocked {self.generate_tag()}", TestResult.PASSING


_LUIGI7_CONF = (
    "{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, "
    "'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, "
    "'disable_hard_timeout': 3600}"
)


class Luigi7UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi7TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="luigi.scheduler",
                names=[ast.alias(name="Scheduler")],
                level=0,
            )
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        x, y, a = f"X_{tag}", f"Y_{tag}", f"A_{tag}"
        newstatus = "UNKNOWN" if mode == "override" else "PENDING"
        return ast.parse(
            f"sch = Scheduler(**{_LUIGI7_CONF})\n"
            f"sch.add_task(worker={x!r}, task_id={a!r})\n"
            f"sch.get_work(worker={x!r})\n"
            f"sch.add_task(worker={y!r}, task_id={a!r}, status={newstatus!r})\n"
            f"status = sch.task_list('', '')[{a!r}]['status']\n"
            f"self.assertEqual(status, 'RUNNING')\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("override", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("blocked", self.generate_tag())
        return test, TestResult.PASSING


grammar_7: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["override", "blocked"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_7)


# ======================================================================
# bug_9: ``execution_summary`` classified any task that ever emitted a
# FAILED event as ``failed`` -- even if it later succeeded on a retry.  So
# the run summary reported ``:( ... there were failed tasks`` for a task
# that actually completed.  The fix tracks ``ever_failed`` separately and
# defines ``failed = ever_failed - completed``, reporting ``:) ... they all
# suceeded in a retry`` when every failure eventually completed.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``retry`` (the
#   trigger: a task fails once then completes -- the buggy summary still
#   shows a sad ``:(``) or ``clean`` (a task that succeeds first try -- happy
#   on both builds).  The correct behaviour is that the summary contains no
#   ``:(``; the harness prints ``HARNESS_OK`` iff the summary has no ``:(``
#   and the oracle returns PASSING iff so.
# ======================================================================


class Luigi9API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi9TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi9SystemtestGenerator(SystemtestGenerator, Luigi9TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"retry {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"clean {self.generate_tag()}", TestResult.PASSING


class Luigi9UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi9TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.Import(names=[ast.alias(name="luigi.worker")]),
            ast.Import(names=[ast.alias(name="luigi.scheduler")]),
            ast.Import(names=[ast.alias(name="luigi.execution_summary")]),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        if mode == "retry":
            run_def = (
                "def _run(t):\n"
                "    t.run_count += 1\n"
                "    if t.run_count == 1:\n"
                "        raise ValueError()\n"
            )
        else:
            run_def = "def _run(t):\n    t.run_count += 1\n"
        return ast.parse(
            f"{run_def}"
            f"def _complete(t):\n"
            f"    return t.run_count > 0\n"
            f"Foo = type('Foo_{tag}', (luigi.Task,), "
            f"{{'run_count': 0, 'run': _run, 'complete': _complete}})\n"
            f"sch = luigi.scheduler.Scheduler(prune_on_get_work=False)\n"
            f"w = luigi.worker.Worker(scheduler=sch)\n"
            f"w.add(Foo())\n"
            f"w.run()\n"
            f"w.add(Foo())\n"
            f"w.run()\n"
            f"s = luigi.execution_summary.summary(w)\n"
            f"self.assertNotIn(':(', s)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("retry", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("clean", self.generate_tag())
        return test, TestResult.PASSING


grammar_9: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["retry", "clean"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_9)


# ======================================================================
# bug_30: ``worker.TaskProcess.run`` wrapped the task execution in a
# ``try/finally`` whose ``finally`` block fired ``Event.PROCESSING_TIME`` and
# ``Event.SUCCESS`` (and called ``on_success``) whenever ``status`` was not
# SUSPENDED -- even when the task actually *failed*.  So a failing task
# wrongly triggered a SUCCESS event in addition to FAILURE.  The fix only
# fires the success events when the task truly produced no new deps and did
# not error.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``fail`` (the
#   trigger: a failing task, which fires *both* SUCCESS and FAILURE on the
#   buggy build) or ``succeed`` (a succeeding task, which fires only
#   SUCCESS on both builds).  The correct behaviour is that exactly one
#   terminal event fires per run; the harness prints ``HARNESS_OK`` iff the
#   total number of SUCCESS+FAILURE events is 1 and the oracle returns
#   PASSING iff so.
# ======================================================================


class Luigi30API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi30TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi30SystemtestGenerator(SystemtestGenerator, Luigi30TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"fail {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"succeed {self.generate_tag()}", TestResult.PASSING


class Luigi30UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi30TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.ImportFrom(
                module="luigi",
                names=[
                    ast.alias(name="Event"),
                    ast.alias(name="Task"),
                    ast.alias(name="build"),
                ],
                level=0,
            ),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        fail_bool = "True" if mode == "fail" else "False"
        return ast.parse(
            f"class DummyException_{tag}(Exception):\n"
            f"    pass\n"
            f"def _run(self):\n"
            f"    if self.fail:\n"
            f"        raise DummyException_{tag}()\n"
            f"T = type('ET_{tag}', (Task,), "
            f"{{'fail': luigi.BoolParameter(), 'run': _run}})\n"
            f"successes = []\n"
            f"failures = []\n"
            f"def _s(task):\n"
            f"    successes.append(task)\n"
            f"def _f(task, exc):\n"
            f"    failures.append(task)\n"
            f"T.event_handler(Event.SUCCESS)(_s)\n"
            f"T.event_handler(Event.FAILURE)(_f)\n"
            f"t = T({fail_bool})\n"
            f"build([t], local_scheduler=True)\n"
            f"self.assertEqual(len(successes) + len(failures), 1)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("fail", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("succeed", self.generate_tag())
        return test, TestResult.PASSING


grammar_30: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["fail", "succeed"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_30)


# ======================================================================
# bug_1: ``server.MetricsHandler.get`` obtained ``metrics =
# collector.generate_latest()`` and then, when metrics were present, called
# ``metrics.configure_http_handler(self)`` -- invoking the method on the
# *metrics payload* instead of on the *metrics collector*.  The fix calls
# ``metrics_collector.configure_http_handler(self)``.
#
# System-test format:  ``<mode> <tag>`` where ``<mode>`` is ``metrics`` (the
#   trigger: ``generate_latest`` returns a payload, so the collector's
#   ``configure_http_handler`` must be called -- it is not on the buggy
#   build) or ``nometrics`` (``generate_latest`` returns ``None`` so the
#   collector method is not called on either build).  The correct behaviour
#   is that the collector's ``configure_http_handler`` is called iff metrics
#   are present; the harness prints ``HARNESS_OK`` iff observed == expected
#   and the oracle returns PASSING iff so.
# ======================================================================


class Luigi1API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi1TestGenerator:
    @staticmethod
    def generate_tag() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi1SystemtestGenerator(SystemtestGenerator, Luigi1TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"metrics {self.generate_tag()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"nometrics {self.generate_tag()}", TestResult.PASSING


class Luigi1UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi1TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="unittest", names=[ast.alias(name="mock")], level=0
            ),
            ast.Import(names=[ast.alias(name="tornado.web")]),
            ast.Import(names=[ast.alias(name="luigi.server")]),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        has_metrics = mode == "metrics"
        payload = "mock.MagicMock()" if has_metrics else "None"
        return ast.parse(
            f"note = {tag!r}\n"
            f"sched = mock.MagicMock()\n"
            f"handler = luigi.server.MetricsHandler("
            f"tornado.web.Application(), mock.MagicMock(), scheduler=sched)\n"
            f"coll = sched._state._metrics_collector\n"
            f"coll.generate_latest.return_value = {payload}\n"
            f"with mock.patch.object(handler, 'write'):\n"
            f"    handler.get()\n"
            f"self.assertEqual(coll.configure_http_handler.called, {has_metrics})\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("metrics", self.generate_tag())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("nometrics", self.generate_tag())
        return test, TestResult.PASSING


grammar_1: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <tag>"],
            "<mode>": ["metrics", "nometrics"],
            "<tag>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_1)


# ======================================================================
# bug_8: ``S3CopyToTable.does_table_exist`` built its existence-check SQL
# comparing the table name case-sensitively (``where tablename = %s`` /
# ``where table_schema = %s and table_name = %s``).  Because Redshift stores
# identifiers lower-cased, a table queried with different casing was
# reported missing.  The fix wraps the bound params in ``lower(%s)``.
#
# System-test format:  ``<mode> <tag> <table>`` where ``<mode>`` is ``lower``
#   (the trigger: the generated query must use ``lower(`` -- it does not on
#   the buggy build) or ``exists`` (an invariant -- the query always
#   contains ``table_exists`` on both builds).  The correct behaviour is a
#   case-insensitive existence query; the harness prints ``HARNESS_OK`` iff
#   the checked substring is present and the oracle returns PASSING iff so.
# ======================================================================


class Luigi8API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi8TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi8SystemtestGenerator(SystemtestGenerator, Luigi8TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return (
            f"lower {self.generate_word()} {self.generate_word()}",
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return (
            f"exists {self.generate_word()} {self.generate_word()}",
            TestResult.PASSING,
        )


class Luigi8UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi8TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="unittest", names=[ast.alias(name="mock")], level=0
            ),
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.Import(names=[ast.alias(name="luigi.contrib.redshift")]),
        ]

    def _body(self, mode: str, tag: str, table: str) -> List[ast.stmt]:
        cls_name = f"Dummy_{tag}"
        substr = "lower(" if mode == "lower" else "table_exists"
        return ast.parse(
            f"class {cls_name}(luigi.contrib.redshift.S3CopyToTable):\n"
            f"    host = 'h'\n"
            f"    database = 'd'\n"
            f"    user = 'u'\n"
            f"    password = 'p'\n"
            f"    aws_access_key_id = 'key'\n"
            f"    aws_secret_access_key = 'secret'\n"
            f"    copy_options = ''\n"
            f"    table = luigi.Parameter(default={table!r})\n"
            f"    columns = None\n"
            f"    def s3_load_path(self):\n"
            f"        return 's3://bucket/key'\n"
            f"task = {cls_name}()\n"
            f"conn = mock.MagicMock()\n"
            f"cursor = conn.cursor.return_value\n"
            f"luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)\n"
            f"query = cursor.execute.call_args[0][0]\n"
            f"self.assertIn({substr!r}, query)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("lower", self.generate_word(), self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("exists", self.generate_word(), self.generate_word())
        return test, TestResult.PASSING


grammar_8: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word> <word>"],
            "<mode>": ["lower", "exists"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_8)


# ======================================================================
# bug_20: ``Task.to_str_params`` serialized only *significant* parameters
# (``if params[param_name].significant``).  ``from_str_params`` however
# reads ``params_str[param_name]`` for *every* declared parameter, so a
# task that has an *insignificant* parameter could not be round-tripped:
# ``to_str_params`` dropped the insignificant key and ``from_str_params``
# raised ``KeyError``.  The fix serializes *all* parameters.
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``insig`` (the
#   trigger: the task carries an insignificant parameter, so the round-trip
#   raises ``KeyError`` on the buggy build) or ``sig`` (only significant
#   parameters, so the round-trip succeeds on both builds).  The harness
#   round-trips the task through ``to_str_params``/``from_str_params`` and
#   prints ``HARNESS_OK`` iff the reconstructed task equals the original;
#   the oracle -- knowing the CORRECT behaviour is that the round-trip
#   always succeeds -- returns PASSING iff ``HARNESS_OK`` was printed.
# ======================================================================


class Luigi20API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi20TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi20SystemtestGenerator(SystemtestGenerator, Luigi20TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"insig {self.generate_word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"sig {self.generate_word()}", TestResult.PASSING


class Luigi20UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi20TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [ast.Import(names=[ast.alias(name="luigi")])]

    def _body(self, mode: str, w: str) -> List[ast.stmt]:
        cls_name = f"Task_{mode}_{w}"
        if mode == "insig":
            attrs = (
                "    x = luigi.Parameter()\n"
                "    y = luigi.Parameter(significant=False)\n"
            )
            create = f"original = {cls_name}(x={('vx' + w)!r}, y={('vy' + w)!r})"
        else:
            attrs = (
                "    x = luigi.Parameter()\n"
                "    z = luigi.Parameter()\n"
            )
            create = f"original = {cls_name}(x={('vx' + w)!r}, z={('vz' + w)!r})"
        return ast.parse(
            f"class {cls_name}(luigi.Task):\n"
            f"{attrs}"
            f"{create}\n"
            f"other = {cls_name}.from_str_params(original.to_str_params())\n"
            f"self.assertEqual(original, other)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("insig", self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("sig", self.generate_word())
        return test, TestResult.PASSING


grammar_20: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word>"],
            "<mode>": ["insig", "sig"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_20)


# ======================================================================
# bug_24: ``SparkSubmitTask._dict_arg`` wrapped every ``prop=value`` in an
# extra pair of double quotes -- ``'"{0}={1}"'.format(prop, value)`` --
# which leaked the literal quotes into the ``spark-submit`` command line
# (e.g. ``['--conf', '"Prop=Value"']`` instead of ``['--conf',
# 'Prop=Value']``).  The fix drops the quotes: ``'{0}={1}'.format(...)``.
#
# System-test format:  ``<mode> <name> <prop> <val>`` where ``<mode>`` is
#   ``dict`` (the trigger: a non-empty dict, so the buggy build emits the
#   quoted form) or ``empty`` (an empty dict, so ``_dict_arg`` returns
#   ``[]`` on both builds).  The harness prints ``repr(_dict_arg(name,
#   value))``; the oracle -- knowing the CORRECT behaviour is the
#   quote-free ``["<name>", "<prop>=<val>"]`` (or ``[]``) -- returns
#   PASSING iff the printed value equals that.
# ======================================================================


class Luigi24API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            name = process.args[3]
            prop = process.args[4]
            val = process.args[5]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "dict":
            expected = [name, "{0}={1}".format(prop, val)]
        else:
            expected = []
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == repr(expected):
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Luigi24TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))

    def generate_triple(self) -> Tuple[str, str, str]:
        return self.generate_word(), self.generate_word(), self.generate_word()


class Luigi24SystemtestGenerator(SystemtestGenerator, Luigi24TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        name, prop, val = self.generate_triple()
        return f"dict --{name} {prop} {val}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        name, prop, val = self.generate_triple()
        return f"empty --{name} {prop} {val}", TestResult.PASSING


class Luigi24UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi24TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.ImportFrom(
                module="luigi.contrib.spark",
                names=[ast.alias(name="SparkSubmitTask")],
                level=0,
            )
        ]

    def _body(self, mode: str, name: str, prop: str, val: str) -> List[ast.stmt]:
        if mode == "dict":
            value = f"{{{prop!r}: {val!r}}}"
            expected = [f"--{name}", f"{prop}={val}"]
        else:
            value = "{}"
            expected = []
        return ast.parse(
            f"self.assertEqual(\n"
            f"    SparkSubmitTask._dict_arg(None, {('--' + name)!r}, {value}),\n"
            f"    {expected!r},\n"
            f")\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        name, prop, val = self.generate_triple()
        test = self.get_empty_test()
        test.body = self._body("dict", name, prop, val)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        name, prop, val = self.generate_triple()
        test = self.get_empty_test()
        test.body = self._body("empty", name, prop, val)
        return test, TestResult.PASSING


grammar_24: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> --<word> <word> <word>"],
            "<mode>": ["dict", "empty"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_24)


# ======================================================================
# bug_2: ``BeamDataflowJobTask.get_target_path`` had a broken branch for
# ``BigQueryTarget``: it built the ``"{}:{}.{}"`` string but never
# ``return``-ed it (and referenced non-existent ``target.project_id``
# attributes), so passing a ``BigQueryTarget`` produced ``None`` /
# ``AttributeError`` instead of ``"project:dataset.table"``.  The fix
# returns ``"{}:{}.{}".format(target.table.project_id,
# target.table.dataset_id, target.table.table_id)``.
#
# System-test format:  ``<kind> ...`` where ``<kind>`` is ``bq <p> <d> <t>``
#   (the trigger: a BigQueryTarget, mishandled on the buggy build) or
#   ``local <path>`` / ``gcs gs://<path>`` (a LocalTarget/GCSTarget, whose
#   ``return target.path`` branch works on both builds).  The harness prints
#   ``repr(get_target_path(target))``; the oracle -- knowing the CORRECT
#   result (``"<p>:<d>.<t>"`` for bq, the path otherwise) -- returns PASSING
#   iff the printed value equals it.
# ======================================================================


class Luigi2API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            kind = process.args[2]
            if kind == "bq":
                expected = "{}:{}.{}".format(
                    process.args[3], process.args[4], process.args[5]
                )
            else:
                expected = process.args[3]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == repr(expected):
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Luigi2TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))


class Luigi2SystemtestGenerator(SystemtestGenerator, Luigi2TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        p, d, t = self.generate_word(), self.generate_word(), self.generate_word()
        return f"bq {p} {d} {t}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        if random.random() < 0.5:
            return f"local out_{self.generate_word()}", TestResult.PASSING
        return (
            f"gcs gs://{self.generate_word()}/{self.generate_word()}",
            TestResult.PASSING,
        )


class Luigi2UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi2TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi")]),
            ast.ImportFrom(
                module="luigi.contrib",
                names=[ast.alias(name="bigquery"), ast.alias(name="gcs")],
                level=0,
            ),
            ast.ImportFrom(
                module="luigi.contrib.beam_dataflow",
                names=[ast.alias(name="BeamDataflowJobTask")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        p, d, t = self.generate_word(), self.generate_word(), self.generate_word()
        test = self.get_empty_test()
        test.body = ast.parse(
            f"target = bigquery.BigQueryTarget({p!r}, {d!r}, {t!r}, client='fake_client')\n"
            f"self.assertEqual(BeamDataflowJobTask.get_target_path(target), {f'{p}:{d}.{t}'!r})\n"
        ).body
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        if random.random() < 0.5:
            path = f"out_{self.generate_word()}"
            test.body = ast.parse(
                f"target = luigi.LocalTarget({path!r})\n"
                f"self.assertEqual(BeamDataflowJobTask.get_target_path(target), {path!r})\n"
            ).body
        else:
            path = f"gs://{self.generate_word()}/{self.generate_word()}"
            test.body = ast.parse(
                f"target = gcs.GCSTarget({path!r}, client='fake_client')\n"
                f"self.assertEqual(BeamDataflowJobTask.get_target_path(target), {path!r})\n"
            ).body
        return test, TestResult.PASSING


grammar_2: Grammar = clean_up(
    dict(
        {
            "<start>": ["bq <word> <word> <word>", "local out_<word>", "gcs gs://<word>/<word>"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_2)


# ======================================================================
# bug_17: ``_WorkerSchedulerFactory.create_local_scheduler`` created a
# ``CentralPlannerScheduler(prune_on_get_work=True)`` without forcing
# ``record_task_history=False``.  A *local* (in-process) scheduler has no
# task-history database, yet if the user's config set
# ``[scheduler] record_task_history=True`` the local scheduler would honour
# it and try to build a ``DbTaskHistory`` -- so ``_config.record_task_history``
# came back ``True`` (and construction could even fail).  The fix passes
# ``record_task_history=False`` so a local scheduler never records history.
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``on`` (the
#   trigger: config sets ``record_task_history=True``, which the buggy local
#   scheduler wrongly honours) or ``off`` (config leaves it False).  The
#   harness sets the config accordingly, builds a local scheduler and prints
#   ``_config.record_task_history``; the oracle -- knowing the CORRECT
#   behaviour is that a local scheduler is ALWAYS ``False`` -- returns
#   PASSING iff the printed value is ``False``.
# ======================================================================


class Luigi17API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "False":
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi17TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi17SystemtestGenerator(SystemtestGenerator, Luigi17TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"on {self.generate_word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"off {self.generate_word()}", TestResult.PASSING


class Luigi17UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi17TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi.configuration")]),
            ast.ImportFrom(
                module="luigi.interface",
                names=[ast.alias(name="_WorkerSchedulerFactory")],
                level=0,
            ),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        value = "True" if mode == "on" else "False"
        return ast.parse(
            f"_tag = {tag!r}\n"
            "config = luigi.configuration.get_config()\n"
            "if not config.has_section('scheduler'):\n"
            "    config.add_section('scheduler')\n"
            f"config.set('scheduler', 'record_task_history', {value!r})\n"
            "ls = _WorkerSchedulerFactory().create_local_scheduler()\n"
            "self.assertEqual(False, ls._config.record_task_history)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("on", self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("off", self.generate_word())
        return test, TestResult.PASSING


grammar_17: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word>"],
            "<mode>": ["on", "off"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_17)


# ======================================================================
# bug_25: ``S3CopyToTable.run`` referenced the load path as ``self.
# s3_load_path()`` -- but ``s3_load_path`` is an (abstract) *property* that
# subclasses override with a plain string attribute, so calling it raised
# ``TypeError: 'str' object is not callable``.  The fix reads it as an
# attribute: ``path = self.s3_load_path``.
#
# System-test format:  ``<mode> <bucket> <key>`` where ``<mode>`` is
#   ``attr`` (the trigger: ``s3_load_path`` is a string attribute -- the
#   documented usage -- so the buggy build crashes when calling it) or
#   ``method`` (``s3_load_path`` is a callable, which the buggy build can
#   still call and the fixed build simply doesn't call, so both succeed).
#   The harness mocks the Redshift target + copy, runs the task and prints
#   ``HARNESS_OK``; the oracle -- knowing the CORRECT behaviour is that the
#   task runs to completion -- returns PASSING iff ``HARNESS_OK`` printed.
# ======================================================================


class Luigi25API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi25TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))

    def generate_pair(self) -> Tuple[str, str]:
        return self.generate_word(), self.generate_word()


class Luigi25SystemtestGenerator(SystemtestGenerator, Luigi25TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        bucket, key = self.generate_pair()
        return f"attr {bucket} {key}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        bucket, key = self.generate_pair()
        return f"method {bucket} {key}", TestResult.PASSING


class Luigi25UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi25TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="luigi.contrib.redshift")]),
            ast.ImportFrom(
                module="unittest", names=[ast.alias(name="mock")], level=0
            ),
        ]

    def _body(self, mode: str, bucket: str, key: str) -> List[ast.stmt]:
        cls_name = f"DummyS3CopyToTable_{mode}_{bucket}_{key}"
        load_path = f"s3://{bucket}/{key}"
        if mode == "attr":
            load_line = f"    s3_load_path = {load_path!r}\n"
        else:
            load_line = (
                "    def s3_load_path(self):\n"
                f"        return {load_path!r}\n"
            )
        return ast.parse(
            f"class {cls_name}(luigi.contrib.redshift.S3CopyToTable):\n"
            f"    host = 'h'\n"
            f"    database = 'd'\n"
            f"    user = 'u'\n"
            f"    password = 'p'\n"
            f"    table = 't'\n"
            f"    columns = (('c', 'text'),)\n"
            f"    aws_access_key_id = 'k'\n"
            f"    aws_secret_access_key = 's'\n"
            f"{load_line}"
            f"    copy_options = ''\n"
            f"with mock.patch('luigi.contrib.redshift.RedshiftTarget'), "
            f"mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):\n"
            f"    task = {cls_name}()\n"
            f"    task.run()\n"
            f"self.assertTrue(True)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        bucket, key = self.generate_pair()
        test = self.get_empty_test()
        test.body = self._body("attr", bucket, key)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        bucket, key = self.generate_pair()
        test = self.get_empty_test()
        test.body = self._body("method", bucket, key)
        return test, TestResult.PASSING


grammar_25: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word> <word>"],
            "<mode>": ["attr", "method"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_25)


# ======================================================================
# bug_21: ``interface.run`` did not default ``cmdline_args`` to
# ``sys.argv[1:]`` when it was ``None``.  So calling ``luigi.run(
# main_task_cls=SomeTask)`` (the documented no-args entry point) hit
# ``cmdline_args.insert(0, main_task_cls.task_family)`` with
# ``cmdline_args is None`` and raised ``AttributeError: 'NoneType' object
# has no attribute 'insert'``.  The fix adds ``if cmdline_args is None:
# cmdline_args = sys.argv[1:]`` at the top of ``run``.
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``none`` (the
#   trigger: ``cmdline_args`` left as ``None`` while a ``main_task_cls`` is
#   given, which crashes on the buggy build) or ``explicit`` (an explicit
#   ``cmdline_args`` list, which both builds accept).  The harness invokes
#   ``luigi.run`` accordingly on a trivially-complete task and prints
#   ``HARNESS_OK``; the oracle -- knowing the CORRECT behaviour is that the
#   call returns without error -- returns PASSING iff ``HARNESS_OK`` printed.
# ======================================================================


class Luigi21API(LuigiAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and "HARNESS_OK" in out:
            return TestResult.PASSING, out
        return TestResult.FAILING, out or process.stderr.decode("utf8").strip()


class Luigi21TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9)))


class Luigi21SystemtestGenerator(SystemtestGenerator, Luigi21TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return f"none {self.generate_word()}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return f"explicit {self.generate_word()}", TestResult.PASSING


class Luigi21UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Luigi21TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="sys")]),
            ast.Import(names=[ast.alias(name="luigi")]),
        ]

    def _body(self, mode: str, tag: str) -> List[ast.stmt]:
        cls_name = f"MyTask_{mode}_{tag}"
        cls_def = (
            f"class {cls_name}(luigi.Task):\n"
            f"    def complete(self):\n"
            f"        return True\n"
        )
        if mode == "none":
            return ast.parse(
                cls_def
                + "_saved = sys.argv\n"
                + "sys.argv = ['harness', '--no-lock', '--local-scheduler']\n"
                + "try:\n"
                + f"    luigi.run(main_task_cls={cls_name})\n"
                + "finally:\n"
                + "    sys.argv = _saved\n"
                + "self.assertTrue(True)\n"
            ).body
        return ast.parse(
            cls_def
            + f"luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], "
            f"main_task_cls={cls_name})\n"
            + "self.assertTrue(True)\n"
        ).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("none", self.generate_word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("explicit", self.generate_word())
        return test, TestResult.PASSING


grammar_21: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <word>"],
            "<mode>": ["none", "explicit"],
            "<word>": ["<letter><letters>"],
            "<letters>": ["", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        }
    )
)

assert is_valid_grammar(grammar_21)
