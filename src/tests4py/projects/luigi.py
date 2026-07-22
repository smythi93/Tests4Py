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
        test_status_fixed=TestStatus.FAILING,
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
        test_status_fixed=TestStatus.FAILING,
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
        test_status_fixed=TestStatus.FAILING,
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
        test_status_fixed=TestStatus.FAILING,
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
        test_status_fixed=TestStatus.FAILING,
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
        test_status_fixed=TestStatus.FAILING,
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
