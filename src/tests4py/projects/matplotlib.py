from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Matplotlib(Project):
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
            project_name="matplotlib",
            github_url="=https://github.com/matplotlib/matplotlib",
            status=Status.OK,
            cause="N.A.",
            python_version="3.8.1",
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
    Matplotlib(
        bug_id=1,
        buggy_commit_id="c404d1f716e8aaefd4d7371ff49673e9c1f7f07c",
        fixed_commit_id="5324adaec6a7fd3d78dea7b28451d5f6e95392a6",
        test_file=[Path("lib", "matplotlib", "tests", "test_bbox_tight.py")],
        test_cases=["lib/matplotlib/tests/test_bbox_tight.py::test_noop_tight_bbox"],
    )
    Matplotlib(
        bug_id=2,
        buggy_commit_id="2a3707d9c3472b1a010492322b6946388d4989ae",
        fixed_commit_id="d86cc2bab8183fd3288ed474e4dfd33e0f018908",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            "lib/matplotlib/tests/test_axes.py::TestScatter::test_scatter_unfilled"
        ],
    )
    Matplotlib(
        bug_id=3,
        buggy_commit_id="5e046f72ae82788788c7e9b9354b87b131891cd8",
        fixed_commit_id="2a3707d9c3472b1a010492322b6946388d4989ae",
        test_file=[Path("lib", "matplotlib", "tests", "test_marker.py")],
        test_cases=["lib/matplotlib/tests/test_marker.py::test_marker_fillstyle"],
    )
    Matplotlib(
        bug_id=4,
        buggy_commit_id="793c6b05381231371267b44b107726f3878e14f2",
        fixed_commit_id="fafa132484872141431a5be3727eab1d8b3c7b82",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_vlines_default"],
    )
    Matplotlib(
        bug_id=5,
        buggy_commit_id="49593b73854e10ace8f3c05343220328def6a328",
        fixed_commit_id="66289c4f1895b8c65ca92a03d92f6b1cfa552267",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            "lib/matplotlib/tests/test_axes.py::TestScatter::test_scatter_linewidths"
        ],
    )
    Matplotlib(
        bug_id=6,
        buggy_commit_id="fb9e72309aeefb51d1a56ecbdb1e7399d105ff06",
        fixed_commit_id="d84f4a7ac8d43d1288cb8ce11ab60ae557306b7e",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            "lib/matplotlib/tests/test_axes.py::TestScatter::test_scatter_single_color_c"
        ],
    )
    Matplotlib(
        bug_id=7,
        buggy_commit_id="969513e2a5227331a2eb9e4bc4ba8448a0f9831d",
        fixed_commit_id="ac400b51bb31b91920ee9aae02a0606a67983a8f",
        test_file=[Path("lib", "matplotlib", "tests", "test_colors.py")],
        test_cases=[
            "lib/matplotlib/tests/test_colors.py::test_light_source_shading_empty_mask"
        ],
    )
    Matplotlib(
        bug_id=8,
        buggy_commit_id="54bd6f19b23dc940a4d572583c449613b6b1ae3c",
        fixed_commit_id="2f41868de465b86d2fc357f7ed58ff323d58030f",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            "lib/matplotlib/tests/test_axes.py::test_unautoscaley;lib/matplotlib/tests/test_axes.py::test_unautoscalex"
        ],
    )
    Matplotlib(
        bug_id=9,
        buggy_commit_id="8673167d4c44dc2ede02fedd718dadf7f88e102d",
        fixed_commit_id="c01f9d3eff9b6239446c1bb2d205eccd69054aeb",
        test_file=[Path("lib", "matplotlib", "tests", "test_polar.py")],
        test_cases=[
            "lib/matplotlib/tests/test_polar.py::test_polar_invertedylim_rorigin"
        ],
    )
    Matplotlib(
        bug_id=10,
        buggy_commit_id="b31d64ce3910e8d297d8300690e459587f77181f",
        fixed_commit_id="1986da3968ee76c6bce8f4c04aed80e23bd4ecfa",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_offset_text_visible"],
    )
    Matplotlib(
        bug_id=11,
        buggy_commit_id="f8459a513c3f67447ceb1a07c29760d504517ff2",
        fixed_commit_id="af745264376a10782bd0d8b96d255f958c2950f3",
        test_file=[Path("lib", "matplotlib", "tests", "test_text.py")],
        test_cases=["lib/matplotlib/tests/test_text.py::test_non_default_dpi"],
    )
    Matplotlib(
        bug_id=12,
        buggy_commit_id="e92685a26442bfced06067934f34c104487583a8",
        fixed_commit_id="382be60aec3e6ebbf92f3d5792ba059bf3cfe6cf",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_lines_with_colors"],
    )
    Matplotlib(
        bug_id=13,
        buggy_commit_id="2c845db9d961ddea6e072c3e6dbb0bec823ac25e",
        fixed_commit_id="eb4b15b47a4d019f0e9edb2fb0587aebc2dbd8e8",
        test_file=[Path("lib", "matplotlib", "tests", "test_path.py")],
        test_cases=["lib/matplotlib/tests/test_path.py::test_make_compound_path_stops"],
    )
    Matplotlib(
        bug_id=14,
        buggy_commit_id="dbc35a9d625e162445f864b9f463c9961888e901",
        fixed_commit_id="c986a12b6d0d0d44f5a87f7cd4408f38040e2537",
        test_file=[Path("lib", "matplotlib", "tests", "test_text.py")],
        test_cases=[
            "lib/matplotlib/tests/test_text.py::test_fontproperties_kwarg_precedence"
        ],
    )
    Matplotlib(
        bug_id=15,
        buggy_commit_id="6a8e39f4eba28e99d7b1dd454b001b987dd0bbca",
        fixed_commit_id="c7df5d2770030fe4588a0fc1ab4449a689554dfc",
        test_file=[Path("lib", "matplotlib", "tests", "test_colors.py")],
        test_cases=["lib/matplotlib/tests/test_colors.py::test_SymLogNorm"],
    )
    Matplotlib(
        bug_id=16,
        buggy_commit_id="89ff308306bafac22647c050a42141f040210216",
        fixed_commit_id="5d99e151be80bcb0b3b6d081fd3038330f573d94",
        test_file=[Path("lib", "matplotlib", "tests", "test_colorbar.py")],
        test_cases=["lib/matplotlib/tests/test_colorbar.py::test_colorbar_int"],
    )
    Matplotlib(
        bug_id=17,
        buggy_commit_id="58c66982d98851c56b045137ced803fd62c6c5e8",
        fixed_commit_id="05a5db0fec2eced55076736f0b9520641b279ad6",
        test_file=[Path("lib", "matplotlib", "tests", "test_colorbar.py")],
        test_cases=["lib/matplotlib/tests/test_colorbar.py::test_colorbar_int"],
    )
    Matplotlib(
        bug_id=18,
        buggy_commit_id="7d958c63f4fbcd8a28df666d738400b251f89af7",
        fixed_commit_id="47479b04b6718a65ebaac094db106d44b40da509",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_polar_no_data"],
    )
    Matplotlib(
        bug_id=19,
        buggy_commit_id="47cfa35fc01af26498f493affcd8cb42b8fb2fc8",
        fixed_commit_id="670d5614e884be8013cf5dbb2160b4d33314d771",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_polar_no_data"],
    )
    Matplotlib(
        bug_id=20,
        buggy_commit_id="805f451b7122d1ef595c7a01592bb2f500aed41f",
        fixed_commit_id="5375487ab28c877c8008c5a178e0b81a6e267957",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_invisible_axes"],
    )
    Matplotlib(
        bug_id=21,
        buggy_commit_id="e240493a899ac05cb992cdb88f5487386586090e",
        fixed_commit_id="6fceb054369445d0b20d2864957e8bcfd8d2cb87",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_boxplot_marker_behavior"],
    )
    Matplotlib(
        bug_id=22,
        buggy_commit_id="a87cd8a4c43688137155accdc57ed64fb95e2d40",
        fixed_commit_id="2349d826a170a10510d1ee8be02eaff51f7ee89f",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            "lib/matplotlib/tests/test_axes.py::test_hist_datetime_datasets_bins"
        ],
    )
    Matplotlib(
        bug_id=23,
        buggy_commit_id="bb6a4af984778dbac55c8391ae29fa2b5b201361",
        fixed_commit_id="418a1adf597b4d7759dcd64b864bd64cc1b507f4",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            "lib/matplotlib/tests/test_axes.py::test_aspect_nonlinear_adjustable_datalim"
        ],
    )
    Matplotlib(
        bug_id=24,
        buggy_commit_id="9a5473dbac05f3d6773b42c8e16d58a7dc3159b8",
        fixed_commit_id="407a9fe71a4c0a8ba4914b8f54f21d32d6dd2d74",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_set_ticks_inverted"],
    )
    Matplotlib(
        bug_id=25,
        buggy_commit_id="9a5473dbac05f3d6773b42c8e16d58a7dc3159b8",
        fixed_commit_id="184225bc5639fbd2f29c1253602806a8b6462d9f",
        test_file=[Path("lib", "matplotlib", "tests", "test_collections.py")],
        test_cases=[
            "lib/matplotlib/tests/test_collections.py::test_EventCollection_nosort"
        ],
    )
    Matplotlib(
        bug_id=26,
        buggy_commit_id="04d9d28b820af0b4df230a3c67314ed5b0af8fdd",
        fixed_commit_id="557375ff91f64c1b827f6014da2d369513a69316",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_set_ticks_inverted"],
    )
    Matplotlib(
        bug_id=27,
        buggy_commit_id="11269123d516cda369764a081ddfb8c1a10ddc53",
        fixed_commit_id="02f25d60139b160fd9b321802b4a2f6c6f3f8672",
        test_file=[Path("lib", "matplotlib", "tests", "test_colorbar.py")],
        test_cases=["lib/matplotlib/tests/test_colorbar.py::test_colorbar_label"],
    )
    Matplotlib(
        bug_id=28,
        buggy_commit_id="896fb8140a600341ebb5eaa4191584f23df2d2a0",
        fixed_commit_id="94ac78a47cfaed9a09e5fd8295b88e8248b67f55",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_log_scales_invalid"],
    )
    Matplotlib(
        bug_id=29,
        buggy_commit_id="cdf9e30e4f3fb7747b178ee9c3849dfdebee7bd0",
        fixed_commit_id="fc51b411ba5d0984544ecff97e0a28ea4b6a6d03",
        test_file=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=["lib/matplotlib/tests/test_axes.py::test_inverted_cla"],
    )
    Matplotlib(
        bug_id=30,
        buggy_commit_id="3b26ee6f6b31bc0cca4be0407dbb40f44756030d",
        fixed_commit_id="d4de838fe7b38abb02f061540fd93962cc063fc4",
        test_file=[Path("lib", "matplotlib", "tests", "test_colors.py")],
        test_cases=["lib/matplotlib/tests/test_colors.py::test_makeMappingArray"],
    )


class MatplotlibAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass
