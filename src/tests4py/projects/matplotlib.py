import ast
import bisect
import os
import random
import string
import subprocess
from pathlib import Path
from typing import Any, List, Optional, Tuple

from tests4py.grammars import python
from tests4py.grammars.default import clean_up, INTEGER, FLOAT, NUMBER
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "matplotlib"

# On an Apple-Silicon host the pyenv CPython 3.8.4 runs as x86_64 (Rosetta), but
# clang defaults to the native arm64 target which the ancient numpy 1.15 headers
# bundled with these matplotlib versions cannot classify ("Unknown CPU").  Force
# the C/C++ extensions to build for x86_64 so they match the interpreter.  The
# ft2font patch works around a hard C++ type error (char* vs unsigned char*) that
# modern system FreeType headers trigger; the replace is a no-op when absent.
_FT2FONT_PATCH = (
    "import io\n"
    "p = 'src/ft2font.cpp'\n"
    "try:\n"
    "    s = io.open(p, encoding='utf8').read()\n"
    "except OSError:\n"
    "    raise SystemExit(0)\n"
    "s = s.replace('tags = outline.tags + first;', "
    "'tags = (char *)(outline.tags + first);')\n"
    "io.open(p, 'w', encoding='utf8').write(s)\n"
)

# Older matplotlib commits download and build a local FreeType 2.6.1 whose
# bundled zlib no longer compiles against modern macOS headers ("unknown type
# name 'Byte'" in ftgzip.c).  Newer commits already link the system FreeType.
# Force *system* FreeType for every build so the extensions link the brew
# freetype2 (found via pkg-config) instead of the broken local build.  configparser
# is used so an existing setup.cfg is preserved rather than clobbered.
_SYSTEM_FREETYPE_PATCH = (
    "import configparser, os\n"
    "c = configparser.ConfigParser()\n"
    "if os.path.exists('setup.cfg'):\n"
    "    c.read('setup.cfg')\n"
    "if not c.has_section('libs'):\n"
    "    c.add_section('libs')\n"
    "c.set('libs', 'system_freetype', 'True')\n"
    "with open('setup.cfg', 'w') as f:\n"
    "    c.write(f)\n"
)


class Matplotlib(Project):
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
        python_version: Optional[str] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/matplotlib/matplotlib",
            status=Status.OK,
            python_version=python_version or "3.8.4",
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
            test_base=Path("lib", PROJECT_NAME, "tests"),
            source_base=Path("lib", PROJECT_NAME),
            setup=[
                ["python", "-c", _SYSTEM_FREETYPE_PATCH],
                ["python", "-c", _FT2FONT_PATCH],
                ["python", "-m", "pip", "install", "-e", "."],
            ],
            setup_env={"ARCHFLAGS": "-arch x86_64"},
            included_files=[os.path.join("lib", PROJECT_NAME)],
            excluded_files=[os.path.join("lib", PROJECT_NAME, "tests")],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )


def register():
    Matplotlib(
        bug_id=1,
        buggy_commit_id="c404d1f716e8aaefd4d7371ff49673e9c1f7f07c",
        fixed_commit_id="5324adaec6a7fd3d78dea7b28451d5f6e95392a6",
        test_files=[
            Path("lib", "matplotlib", "tests", "test_bbox_tight.py"),
        ],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_bbox_tight.py::test_noop_tight_bbox"
            )
        ],
        unittests=Matplotlib1UnittestGenerator(),
        systemtests=Matplotlib1SystemtestGenerator(),
        api=Matplotlib1API(),
        grammar=grammar_1,
        loc=63544,
    )
    Matplotlib(
        bug_id=2,
        buggy_commit_id="2a3707d9c3472b1a010492322b6946388d4989ae",
        fixed_commit_id="d86cc2bab8183fd3288ed474e4dfd33e0f018908",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::TestScatter::test_scatter_unfilled",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::TestScatter",
            )
        ],
        unittests=Matplotlib2UnittestGenerator(),
        systemtests=Matplotlib2SystemtestGenerator(),
        api=Matplotlib2API(),
        grammar=grammar_2,
        loc=63506,
    )
    Matplotlib(
        bug_id=3,
        buggy_commit_id="5e046f72ae82788788c7e9b9354b87b131891cd8",
        fixed_commit_id="2a3707d9c3472b1a010492322b6946388d4989ae",
        test_files=[Path("lib", "matplotlib", "tests", "test_marker.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_marker.py::test_marker_fillstyle"
            )
        ],
        unittests=Matplotlib3UnittestGenerator(),
        systemtests=Matplotlib3SystemtestGenerator(),
        api=Matplotlib3API(),
        grammar=grammar_3,
        loc=63506,
    )
    Matplotlib(
        bug_id=4,
        buggy_commit_id="793c6b05381231371267b44b107726f3878e14f2",
        fixed_commit_id="fafa132484872141431a5be3727eab1d8b3c7b82",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_vlines_default"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hlines_default"
            ),
        ],
        relevant_test_files=[
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_vlines"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_vlines_default"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_vline_limit"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_hlines"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hlines_default"
            ),
        ],
        unittests=Matplotlib4UnittestGenerator(),
        systemtests=Matplotlib4SystemtestGenerator(),
        api=Matplotlib4API(),
        grammar=grammar_4,
        loc=63462,
    )
    Matplotlib(
        bug_id=5,
        buggy_commit_id="49593b73854e10ace8f3c05343220328def6a328",
        fixed_commit_id="66289c4f1895b8c65ca92a03d92f6b1cfa552267",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::TestScatter::test_scatter_linewidths",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::TestScatter",
            )
        ],
        unittests=Matplotlib5UnittestGenerator(),
        systemtests=Matplotlib5SystemtestGenerator(),
        api=Matplotlib5API(),
        grammar=grammar_5,
        loc=63378,
    )
    Matplotlib(
        bug_id=6,
        buggy_commit_id="fb9e72309aeefb51d1a56ecbdb1e7399d105ff06",
        fixed_commit_id="d84f4a7ac8d43d1288cb8ce11ab60ae557306b7e",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::TestScatter::test_scatter_single_color_c[png]",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::TestScatter",
            )
        ],
        unittests=Matplotlib6UnittestGenerator(),
        systemtests=Matplotlib6SystemtestGenerator(),
        api=Matplotlib6API(),
        grammar=grammar_6,
        loc=63369,
    )
    Matplotlib(
        bug_id=7,
        buggy_commit_id="969513e2a5227331a2eb9e4bc4ba8448a0f9831d",
        fixed_commit_id="ac400b51bb31b91920ee9aae02a0606a67983a8f",
        test_files=[Path("lib", "matplotlib", "tests", "test_colors.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_light_source_shading_empty_mask",
            )
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=63292,
    )
    Matplotlib(
        bug_id=8,
        buggy_commit_id="54bd6f19b23dc940a4d572583c449613b6b1ae3c",
        fixed_commit_id="2f41868de465b86d2fc357f7ed58ff323d58030f",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_unautoscaley[True]"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_unautoscalex[True]"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_unautoscaley[None]"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_unautoscalex[None]"
            ),
        ],
        unittests=Matplotlib8UnittestGenerator(),
        systemtests=Matplotlib8SystemtestGenerator(),
        api=Matplotlib8API(),
        grammar=grammar_8,
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_unautoscaley"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_unautoscalex"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_shared_axes_autoscale"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_twinx_axis_scales"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_twin_inherit_autoscale_setting",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_autoscale_tiny_range"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_autoscale_tight"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_autoscale_log_shared"
            ),
        ],
        loc=63243,
    )
    Matplotlib(
        bug_id=9,
        buggy_commit_id="8673167d4c44dc2ede02fedd718dadf7f88e102d",
        fixed_commit_id="c01f9d3eff9b6239446c1bb2d205eccd69054aeb",
        test_files=[Path("lib", "matplotlib", "tests", "test_polar.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_polar.py::test_polar_invertedylim_rorigin[png]",
            )
        ],
        unittests=Matplotlib9UnittestGenerator(),
        systemtests=Matplotlib9SystemtestGenerator(),
        api=Matplotlib9API(),
        grammar=grammar_9,
        loc=63277,
    )
    Matplotlib(
        bug_id=10,
        buggy_commit_id="b31d64ce3910e8d297d8300690e459587f77181f",
        fixed_commit_id="1986da3968ee76c6bce8f4c04aed80e23bd4ecfa",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_offset_text_visible"
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_offset_text_visible"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_offset_label_color"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_text_labelsize"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_large_offset"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_errorbar_offsets"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_offset"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_move_offsetlabel"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_dash_offset"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_relim_visible_only"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_retain_tick_visibility",
            ),
        ],
        unittests=Matplotlib10UnittestGenerator(),
        systemtests=Matplotlib10SystemtestGenerator(),
        api=Matplotlib10API(),
        grammar=grammar_10,
        loc=62823,
    )
    Matplotlib(
        bug_id=11,
        buggy_commit_id="f8459a513c3f67447ceb1a07c29760d504517ff2",
        fixed_commit_id="af745264376a10782bd0d8b96d255f958c2950f3",
        test_files=[Path("lib", "matplotlib", "tests", "test_text.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_text.py::test_non_default_dpi[empty]",
            )
        ],
        skip_tests=["test_text_repr"],
        unittests=Matplotlib11UnittestGenerator(),
        systemtests=Matplotlib11SystemtestGenerator(),
        api=Matplotlib11API(),
        grammar=grammar_11,
        loc=62827,
    )
    Matplotlib(
        bug_id=12,
        buggy_commit_id="e92685a26442bfced06067934f34c104487583a8",
        fixed_commit_id="382be60aec3e6ebbf92f3d5792ba059bf3cfe6cf",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_lines_with_colors[png-data0]",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_lines_with_colors[png-data1]",
            ),
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_lines_with_colors"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_step_linestyle"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_markevery_line"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_eb_line_zorder"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_pie_linewidth_0"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_pie_linewidth_2"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_zero_linewidth"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_vlines"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_vline_limit"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_hlines"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_eventplot_colors"
            ),
        ],
        unittests=Matplotlib12UnittestGenerator(),
        systemtests=Matplotlib12SystemtestGenerator(),
        api=Matplotlib12API(),
        grammar=grammar_12,
        loc=62948,
    )
    Matplotlib(
        bug_id=13,
        buggy_commit_id="2c845db9d961ddea6e072c3e6dbb0bec823ac25e",
        fixed_commit_id="eb4b15b47a4d019f0e9edb2fb0587aebc2dbd8e8",
        test_files=[Path("lib", "matplotlib", "tests", "test_path.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_path.py::test_make_compound_path_stops",
            )
        ],
        unittests=Matplotlib13UnittestGenerator(),
        systemtests=Matplotlib13SystemtestGenerator(),
        api=Matplotlib13API(),
        grammar=grammar_13,
        loc=62951,
    )
    Matplotlib(
        bug_id=14,
        buggy_commit_id="dbc35a9d625e162445f864b9f463c9961888e901",
        fixed_commit_id="c986a12b6d0d0d44f5a87f7cd4408f38040e2537",
        test_files=[Path("lib", "matplotlib", "tests", "test_text.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_text.py::test_fontproperties_kwarg_precedence",
            )
        ],
        skip_tests=["test_text_repr"],
        unittests=Matplotlib14UnittestGenerator(),
        systemtests=Matplotlib14SystemtestGenerator(),
        api=Matplotlib14API(),
        grammar=grammar_14,
        loc=64078,
    )
    Matplotlib(
        bug_id=15,
        buggy_commit_id="6a8e39f4eba28e99d7b1dd454b001b987dd0bbca",
        fixed_commit_id="c7df5d2770030fe4588a0fc1ab4449a689554dfc",
        test_files=[Path("lib", "matplotlib", "tests", "test_colors.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_SymLogNorm"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_SymLogNorm_colorbar",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_SymLogNorm_single_zero",
            ),
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_BoundaryNorm"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_lognorm_invalid"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_colors.py::test_LogNorm"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_PowerNorm"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_PowerNorm_translation_invariance",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_autoscale",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_autoscale_None_vmin",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_autoscale_None_vmax",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_TwoSlopeNorm_scale"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_scaleout_center",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_scaleout_center_max",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_TwoSlopeNorm_Even"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_TwoSlopeNorm_Odd"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_VminEqualsVcenter",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_VmaxEqualsVcenter",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_VminGTVcenter",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_TwoSlopeNorm_VminGTVmax",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_TwoSlopeNorm_VcenterGTVmax",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_SymLogNorm"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_SymLogNorm_colorbar"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_SymLogNorm_single_zero",
            ),
        ],
        unittests=Matplotlib15UnittestGenerator(),
        systemtests=Matplotlib15SystemtestGenerator(),
        api=Matplotlib15API(),
        grammar=grammar_15,
        loc=64152,
    )
    Matplotlib(
        bug_id=16,
        buggy_commit_id="89ff308306bafac22647c050a42141f040210216",
        fixed_commit_id="5d99e151be80bcb0b3b6d081fd3038330f573d94",
        test_files=[Path("lib", "matplotlib", "tests", "test_colorbar.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colorbar.py::test_colorbar_int[clim0]",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colorbar.py::test_colorbar_int[clim1]",
            ),
        ],
        skip_tests=["test_colorbar_positioning[png]"],
        unittests=Matplotlib16UnittestGenerator(),
        systemtests=Matplotlib16SystemtestGenerator(),
        api=Matplotlib16API(),
        grammar=grammar_16,
        loc=65317,
    )
    Matplotlib(
        bug_id=17,
        buggy_commit_id="58c66982d98851c56b045137ced803fd62c6c5e8",
        fixed_commit_id="05a5db0fec2eced55076736f0b9520641b279ad6",
        test_files=[Path("lib", "matplotlib", "tests", "test_colorbar.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colorbar.py::test_colorbar_int[clim0]",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colorbar.py::test_colorbar_int[clim1]",
            ),
        ],
        skip_tests=["test_colorbar_positioning[png]"],
        unittests=Matplotlib17UnittestGenerator(),
        systemtests=Matplotlib17SystemtestGenerator(),
        api=Matplotlib17API(),
        grammar=grammar_17,
        loc=64261,
    )
    Matplotlib(
        bug_id=18,
        buggy_commit_id="7d958c63f4fbcd8a28df666d738400b251f89af7",
        fixed_commit_id="47479b04b6718a65ebaac094db106d44b40da509",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_no_data"
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_twice"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_polar_wrap"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_units_1"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_units_2"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_polar_rlim"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_rlim_bottom"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_rlim_zero"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_no_data"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_polar_not_datalim_adjustable",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_gridlines"
            ),
        ],
        unittests=Matplotlib18UnittestGenerator(),
        systemtests=Matplotlib18SystemtestGenerator(),
        api=Matplotlib18API(),
        grammar=grammar_18,
        loc=65299,
    )
    Matplotlib(
        bug_id=19,
        buggy_commit_id="47cfa35fc01af26498f493affcd8cb42b8fb2fc8",
        fixed_commit_id="670d5614e884be8013cf5dbb2160b4d33314d771",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_no_data"
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_twice"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_polar_wrap"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_units_1"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_units_2"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_polar_rlim"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_rlim_bottom"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_rlim_zero"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_no_data"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_polar_not_datalim_adjustable",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_polar_gridlines"
            ),
        ],
        unittests=Matplotlib19UnittestGenerator(),
        systemtests=Matplotlib19SystemtestGenerator(),
        api=Matplotlib19API(),
        grammar=grammar_19,
        loc=64410,
    )
    Matplotlib(
        bug_id=20,
        buggy_commit_id="805f451b7122d1ef595c7a01592bb2f500aed41f",
        fixed_commit_id="5375487ab28c877c8008c5a178e0b81a6e267957",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_invisible_axes"
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_invisible_axes"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_annotate_across_transforms",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_twin_spines",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_relim_visible_only",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_axisbelow",
            ),
        ],
        unittests=Matplotlib20UnittestGenerator(),
        systemtests=Matplotlib20SystemtestGenerator(),
        api=Matplotlib20API(),
        grammar=grammar_20,
        loc=65299,
    )
    Matplotlib(
        bug_id=21,
        buggy_commit_id="e240493a899ac05cb992cdb88f5487386586090e",
        fixed_commit_id="6fceb054369445d0b20d2864957e8bcfd8d2cb87",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_boxplot_marker_behavior",
            ),
        ],
        unittests=Matplotlib21UnittestGenerator(),
        systemtests=Matplotlib21SystemtestGenerator(),
        api=Matplotlib21API(),
        grammar=grammar_21,
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_dates_pandas"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_boxplot"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_sym2"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_sym"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_boxplot_autorange_whiskers",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_rc_parameters"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_with_CIarray"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_boxplot_no_weird_whisker",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_bad_medians_1"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_bad_medians_2"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_bad_ci_1"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_zorder"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_bad_ci_2"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_boxplot_marker_behavior",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_boxplot_mod_artist_after_plotting",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_boxplot_not_single"
            ),
        ],
        loc=65200,
    )
    Matplotlib(
        bug_id=22,
        buggy_commit_id="a87cd8a4c43688137155accdc57ed64fb95e2d40",
        fixed_commit_id="2349d826a170a10510d1ee8be02eaff51f7ee89f",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_hist_datetime_datasets_bins[datetime.datetime]",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_hist_datetime_datasets_bins[np.datetime64]",
            ),
        ],
        relevant_test_files=[
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_hist_log_2"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_bar_empty"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_step_empty"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_step_filled"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_hist_unequal_bins_density",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_hist_datetime_datasets",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_hist_datetime_datasets_bins",
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_with_empty_input"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist2d_density_normed"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_hist_step"),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_step_bottom"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_emptydata"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_labels"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_auto_bins"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_hist_nan_data"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_hist_range_and_density",
            ),
        ],
        unittests=Matplotlib22UnittestGenerator(),
        systemtests=Matplotlib22SystemtestGenerator(),
        api=Matplotlib22API(),
        grammar=grammar_22,
        loc=65308,
    )
    Matplotlib(
        bug_id=23,
        buggy_commit_id="bb6a4af984778dbac55c8391ae29fa2b5b201361",
        fixed_commit_id="418a1adf597b4d7759dcd64b864bd64cc1b507f4",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_aspect_nonlinear_adjustable_datalim",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_aspect_nonlinear_adjustable_datalim",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_aspect_nonlinear_adjustable_box",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_shared_with_aspect_2",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_shared_with_aspect_3",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_inset",
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_zoom_inset",
            ),
        ],
        unittests=Matplotlib23UnittestGenerator(),
        systemtests=Matplotlib23SystemtestGenerator(),
        api=Matplotlib23API(),
        grammar=grammar_23,
        loc=65354,
    )
    Matplotlib(
        bug_id=24,
        buggy_commit_id="9a5473dbac05f3d6773b42c8e16d58a7dc3159b8",
        fixed_commit_id="407a9fe71a4c0a8ba4914b8f54f21d32d6dd2d74",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_set_ticks_inverted"
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_set_ticks_inverted"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_inverted_limits"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_tick_label_update"
            ),
        ],
        unittests=Matplotlib24UnittestGenerator(),
        systemtests=Matplotlib24SystemtestGenerator(),
        api=Matplotlib24API(),
        grammar=grammar_24,
        loc=66180,
    )
    Matplotlib(
        bug_id=25,
        buggy_commit_id="9a5473dbac05f3d6773b42c8e16d58a7dc3159b8",
        fixed_commit_id="184225bc5639fbd2f29c1253602806a8b6462d9f",
        test_files=[Path("lib", "matplotlib", "tests", "test_collections.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_collections.py::test_EventCollection_nosort",
            )
        ],
        skip_tests=[
            "test__EventCollection__get_segments",
            "test__EventCollection__set_positions",
            "test__EventCollection__add_positions",
            "test__EventCollection__append_positions",
            "test__EventCollection__extend_positions",
            "test__EventCollection__switch_orientation",
            "test__EventCollection__switch_orientation_2x",
            "test__EventCollection__set_orientation",
            "test__EventCollection__set_linelength",
            "test__EventCollection__set_lineoffset",
            "test__EventCollection__set_linestyle",
            "test__EventCollection__set_linestyle_single_dash",
            "test__EventCollection__set_linewidth",
            "test__EventCollection__set_color",
            "test_cap_and_joinstyle_image",
        ],
        unittests=Matplotlib25UnittestGenerator(),
        systemtests=Matplotlib25SystemtestGenerator(),
        api=Matplotlib25API(),
        grammar=grammar_25,
        loc=66180,
    )
    Matplotlib(
        bug_id=26,
        buggy_commit_id="04d9d28b820af0b4df230a3c67314ed5b0af8fdd",
        fixed_commit_id="557375ff91f64c1b827f6014da2d369513a69316",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_set_ticks_inverted"
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_set_ticks_inverted"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_inverted_limits"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_tick_label_update"
            ),
        ],
        unittests=Matplotlib26UnittestGenerator(),
        systemtests=Matplotlib26SystemtestGenerator(),
        api=Matplotlib26API(),
        grammar=grammar_26,
        loc=65354,
    )
    Matplotlib(
        bug_id=27,
        buggy_commit_id="11269123d516cda369764a081ddfb8c1a10ddc53",
        fixed_commit_id="02f25d60139b160fd9b321802b4a2f6c6f3f8672",
        test_files=[Path("lib", "matplotlib", "tests", "test_colorbar.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_colorbar.py::test_colorbar_label"
            )
        ],
        skip_tests=[
            "test_colorbar_positioning",
            "test_colorbar_closed_patch",
        ],
        unittests=Matplotlib27UnittestGenerator(),
        systemtests=Matplotlib27SystemtestGenerator(),
        api=Matplotlib27API(),
        grammar=grammar_27,
        loc=65356,
    )
    Matplotlib(
        bug_id=28,
        buggy_commit_id="896fb8140a600341ebb5eaa4191584f23df2d2a0",
        fixed_commit_id="94ac78a47cfaed9a09e5fd8295b88e8248b67f55",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_log_scales_invalid"
            )
        ],
        unittests=Matplotlib28UnittestGenerator(),
        systemtests=Matplotlib28SystemtestGenerator(),
        api=Matplotlib28API(),
        grammar=grammar_28,
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_log_scales_invalid"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_shared_scale"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_minorticks_on"
            ),
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_secondary_minorloc"
            ),
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_axes.py::test_boxplot_no_weird_whisker",
            ),
        ],
        loc=65357,
    )
    Matplotlib(
        bug_id=29,
        buggy_commit_id="cdf9e30e4f3fb7747b178ee9c3849dfdebee7bd0",
        fixed_commit_id="fc51b411ba5d0984544ecff97e0a28ea4b6a6d03",
        test_files=[Path("lib", "matplotlib", "tests", "test_axes.py")],
        test_cases=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_inverted_cla"
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_axes.py::test_inverted_cla"
            ),
            os.path.join("lib", "matplotlib", "tests", "test_axes.py::test_twinx_cla"),
        ],
        unittests=Matplotlib29UnittestGenerator(),
        systemtests=Matplotlib29SystemtestGenerator(),
        api=Matplotlib29API(),
        grammar=grammar_29,
        loc=66175,
    )
    Matplotlib(
        bug_id=30,
        buggy_commit_id="3b26ee6f6b31bc0cca4be0407dbb40f44756030d",
        fixed_commit_id="d4de838fe7b38abb02f061540fd93962cc063fc4",
        test_files=[Path("lib", "matplotlib", "tests", "test_colors.py")],
        test_cases=[
            os.path.join(
                "lib",
                "matplotlib",
                "tests",
                "test_colors.py::test_makeMappingArray[1-result2]",
            )
        ],
        relevant_test_files=[
            os.path.join(
                "lib", "matplotlib", "tests", "test_colors.py::test_makeMappingArray"
            )
        ],
        unittests=Matplotlib30UnittestGenerator(),
        systemtests=Matplotlib30SystemtestGenerator(),
        api=Matplotlib30API(),
        grammar=grammar_30,
        loc=66111,
    )


class MatplotlibAPI(API):
    # Generous timeout: the first rendering call in a fresh environment builds
    # matplotlib's font cache, which under parallel CPU load can take well over
    # the default 10s and would otherwise spuriously time out a passing test.
    def __init__(self, default_timeout: int = 90):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# bug_30: ``matplotlib.colors.makeMappingArray`` produced a 2-element
# lookup table for ``N == 1`` (concatenating ``[y1[0]]`` and ``[y0[-1]]``)
# instead of the documented single ``y0[-1]`` value.  The fix special-cases
# ``N == 1`` to return ``np.array(y0[-1])``.
#
# System-test format:  ``<N> <gamma> <x,y0,y1> <x,y0,y1> ...``
#   The harness calls ``makeMappingArray(N, data, gamma)`` and prints the
#   rounded lookup table.  ``N == 1`` triggers the fault; ``N >= 2`` does
#   not.  The oracle recomputes the correct (fixed) table in pure Python.
# ======================================================================


def _correct_make_mapping_array(
    n: int, data: List[Tuple[float, float, float]], gamma: float
) -> List[float]:
    xs = [d[0] for d in data]
    y0 = [d[1] for d in data]
    y1 = [d[2] for d in data]
    if n == 1:
        return [min(max(y0[-1], 0.0), 1.0)]
    x = [xi * (n - 1) for xi in xs]
    xind = [(n - 1) * ((i / (n - 1)) ** gamma) for i in range(n)]
    inner = xind[1:-1]
    ind = [bisect.bisect_left(x, v) for v in inner]
    lut = [y1[0]]
    for k, i in enumerate(ind):
        distance = (inner[k] - x[i - 1]) / (x[i] - x[i - 1])
        lut.append(distance * (y0[i] - y1[i - 1]) + y1[i - 1])
    lut.append(y0[-1])
    return [min(max(v, 0.0), 1.0) for v in lut]


def _parse_mapping_data(
    tokens: List[str],
) -> Tuple[int, float, List[Tuple[float, float, float]]]:
    n = int(tokens[0])
    gamma = float(tokens[1])
    data = []
    for tok in tokens[2:]:
        a, b, c = tok.split(",")
        data.append((float(a), float(b), float(c)))
    return n, gamma, data


def _round_list(values: List[float], ndigits: int = 6) -> str:
    return str([round(float(v), ndigits) for v in values])


class Matplotlib30API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            n, gamma, data = _parse_mapping_data(list(process.args[2:]))
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _round_list(_correct_make_mapping_array(n, data, gamma))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib30TestGenerator:
    @staticmethod
    def generate_data() -> List[Tuple[float, float, float]]:
        nseg = random.randint(2, 4)
        interior = sorted(
            round(random.uniform(0.15, 0.85), 3) for _ in range(nseg - 2)
        )
        xs = [0.0] + interior + [1.0]
        return [
            (xi, round(random.uniform(0, 1), 3), round(random.uniform(0, 1), 3))
            for xi in xs
        ]

    @staticmethod
    def format_data(data: List[Tuple[float, float, float]]) -> str:
        return " ".join(f"{a},{b},{c}" for a, b, c in data)

    def make_failing(self) -> str:
        return f"1 1.0 {self.format_data(self.generate_data())}"

    def make_passing(self) -> str:
        n = random.randint(2, 8)
        return f"{n} 1.0 {self.format_data(self.generate_data())}"


class Matplotlib30SystemtestGenerator(
    SystemtestGenerator, Matplotlib30TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib30UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib30TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "import matplotlib.colors as mcolors\n"
        ).body

    @staticmethod
    def _assert(
        n: int, data: List[Tuple[float, float, float]], gamma: float
    ) -> List[ast.stmt]:
        # Inline the call so the assertion works as a self-contained test-method
        # body (the framework places all statements inside the TestCase class, so
        # a class-body helper could not be referenced by bare name).
        expected = [round(v, 6) for v in _correct_make_mapping_array(n, data, gamma)]
        src = (
            f"self.assertEqual({expected!r}, "
            "[round(float(v), 6) for v in np.atleast_1d(np.asarray("
            f"mcolors.makeMappingArray({n}, {list(data)!r}, {gamma})))])"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        data = self.generate_data()
        test = self.get_empty_test()
        test.body = self._assert(1, data, 1.0)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        data = self.generate_data()
        n = random.randint(2, 8)
        test = self.get_empty_test()
        test.body = self._assert(n, data, 1.0)
        return test, TestResult.PASSING


grammar_30: Grammar = clean_up(
    dict(
        {
            "<start>": ["<n> <gamma> <segments>"],
            "<n>": ["<number>"],
            "<gamma>": ["1.0"],
            "<segments>": ["<segment>", "<segment> <segments>"],
            "<segment>": ["<float>,<float>,<float>"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_30)


# ======================================================================
# bug_3: ``matplotlib.markers.MarkerStyle`` initialised ``_filled`` to
# ``True`` unconditionally, so a *filled* marker created with
# ``fillstyle='none'`` still reported ``is_filled() == True``.  The fix
# initialises ``_filled = self._fillstyle != 'none'`` before the marker
# function runs, so an explicitly unfilled marker reports ``False``.
#
# System-test format:  ``<marker> <fillstyle>``
#   The harness builds ``MarkerStyle(marker, fillstyle)`` and prints
#   ``is_filled()``.  For a *filled* marker the correct (fixed) answer is
#   ``fillstyle != 'none'``; ``fillstyle='none'`` triggers the fault
#   (buggy prints ``True``, fixed prints ``False``).
# ======================================================================

_FILLED_MARKERS = ["o", "v", "^", "8", "s", "p", "*", "h", "H", "D", "d"]


def _correct_is_filled(fillstyle: str) -> bool:
    # Only ever evaluated for *filled* markers, whose fixed ``is_filled``
    # value is simply ``fillstyle != 'none'``.
    return fillstyle != "none"


class Matplotlib3API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            fillstyle = process.args[3]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(_correct_is_filled(fillstyle))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib3TestGenerator:
    def make_failing(self) -> str:
        return f"{random.choice(_FILLED_MARKERS)} none"

    def make_passing(self) -> str:
        return f"{random.choice(_FILLED_MARKERS)} full"


class Matplotlib3SystemtestGenerator(
    SystemtestGenerator, Matplotlib3TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib3UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib3TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "from matplotlib.markers import MarkerStyle\n"
        ).body

    @staticmethod
    def _assert(marker: str, fillstyle: str) -> List[ast.stmt]:
        # Inline the call (the framework places every statement inside the
        # TestCase class, so a class-body helper cannot be referenced by name).
        expected = _correct_is_filled(fillstyle)
        src = (
            f"self.assertEqual({expected!r}, "
            f"bool(MarkerStyle({marker!r}, {fillstyle!r}).is_filled()))"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(random.choice(_FILLED_MARKERS), "none")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(random.choice(_FILLED_MARKERS), "full")
        return test, TestResult.PASSING


grammar_3: Grammar = clean_up(
    {
        "<start>": ["<marker> <fillstyle>"],
        "<marker>": ["o", "v", "^", "8", "s", "p", "*", "h", "H", "D", "d"],
        "<fillstyle>": ["full", "none", "left", "right", "top", "bottom"],
    }
)

assert is_valid_grammar(grammar_3)


# ======================================================================
# bug_16: ``matplotlib.transforms.nonsingular`` did not cast integer
# endpoints to float, so ``abs(np.int8(-128))`` wrapped to ``-128`` and
# ``vmax - vmin`` could overflow, yielding a wrong expanded interval.  The
# fix inserts ``vmin, vmax = map(float, [vmin, vmax])`` before the
# arithmetic.
#
# System-test format:  ``<dtype> <vmin> <vmax>``  (dtype one of
# int8/int16/int32/int64/float64).  The harness calls ``nonsingular`` on the
# typed endpoints and prints the rounded ``[vmin, vmax]``.  A signed-integer
# dtype whose *vmin* is the most-negative value triggers the fault (``abs``
# overflow); ``float64`` never does.  The oracle recomputes the correct
# (float) result in pure Python.
# ======================================================================

_TINY_FLOAT = 2.2250738585072014e-308  # == np.finfo(float).tiny

_INT_RANGES = {
    "int8": (-128, 127),
    "int16": (-32768, 32767),
    "int32": (-2147483648, 2147483647),
    "int64": (-9223372036854775808, 9223372036854775807),
}


def _correct_nonsingular(vmin, vmax, expander=0.001, tiny=1e-15, increasing=True):
    import math

    vmin = float(vmin)
    vmax = float(vmax)
    if (not math.isfinite(vmin)) or (not math.isfinite(vmax)):
        return -expander, expander
    swapped = False
    if vmax < vmin:
        vmin, vmax = vmax, vmin
        swapped = True
    maxabsvalue = max(abs(vmin), abs(vmax))
    if maxabsvalue < (1e6 / tiny) * _TINY_FLOAT:
        vmin = -expander
        vmax = expander
    elif vmax - vmin <= maxabsvalue * tiny:
        if vmax == 0 and vmin == 0:
            vmin = -expander
            vmax = expander
        else:
            vmin -= expander * abs(vmin)
            vmax += expander * abs(vmax)
    if swapped and not increasing:
        vmin, vmax = vmax, vmin
    return vmin, vmax


class Matplotlib16API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            vmin = float(process.args[3])
            vmax = float(process.args[4])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str([round(v, 9) for v in _correct_nonsingular(vmin, vmax)])
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib16TestGenerator:
    def make_failing(self) -> str:
        dtype = random.choice(list(_INT_RANGES))
        negmost, _ = _INT_RANGES[dtype]
        vmax = random.choice([negmost, 0])
        return f"{dtype} {negmost} {vmax}"

    def make_passing(self) -> str:
        lo = round(random.uniform(-100, 50), 3)
        hi = round(lo + random.uniform(1, 50), 3)
        return f"float64 {lo} {hi}"


class Matplotlib16SystemtestGenerator(
    SystemtestGenerator, Matplotlib16TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib16UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib16TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "import matplotlib.transforms as mtransforms\n"
        ).body

    @staticmethod
    def _assert(dtype: str, vmin, vmax) -> List[ast.stmt]:
        expected = [
            round(v, 9) for v in _correct_nonsingular(float(vmin), float(vmax))
        ]
        cast = "float" if dtype == "float64" else "int"
        src = (
            f"self.assertEqual({expected!r}, "
            f"[round(float(v), 9) for v in mtransforms.nonsingular("
            f"np.{dtype}({cast}({vmin})), np.{dtype}({cast}({vmax})))])"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        dtype = random.choice(list(_INT_RANGES))
        negmost, _ = _INT_RANGES[dtype]
        vmax = random.choice([negmost, 0])
        test = self.get_empty_test()
        test.body = self._assert(dtype, negmost, vmax)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lo = round(random.uniform(-100, 50), 3)
        hi = round(lo + random.uniform(1, 50), 3)
        test = self.get_empty_test()
        test.body = self._assert("float64", lo, hi)
        return test, TestResult.PASSING


grammar_16: Grammar = clean_up(
    dict(
        {
            "<start>": ["<dtype> <float> <float>"],
            "<dtype>": ["int8", "int16", "int32", "int64", "float64"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_16)


# bug_17 is the identical ``transforms.nonsingular`` integer-overflow fault as
# bug_16 (a different buggy/fixed commit pair), so it reuses the same oracle,
# generators and grammar.
Matplotlib17API = Matplotlib16API
Matplotlib17SystemtestGenerator = Matplotlib16SystemtestGenerator
Matplotlib17UnittestGenerator = Matplotlib16UnittestGenerator
grammar_17 = grammar_16


# ======================================================================
# bug_13: ``matplotlib.path.Path.make_compound_path`` concatenated the code
# arrays of its inputs verbatim, leaving *internal* ``STOP`` codes in the
# middle of the compound path.  The fix strips every ``STOP`` code and only
# re-appends a single trailing ``STOP`` if the concatenation originally ended
# with one.
#
# System-test format:  ``<path> <path> ...`` where each path is a comma-
# separated list of integer path codes (0=STOP, 1=MOVETO, 2=LINETO) and every
# path starts with MOVETO.  The harness builds the paths, calls
# ``make_compound_path`` and prints the resulting code list.  An *internal*
# STOP triggers the fault; paths without STOPs never do.  The oracle recomputes
# the correct (STOP-stripped) code list in pure Python.
# ======================================================================

_STOP_CODE = 0


def _correct_compound_codes_from_lists(code_lists: List[List[int]]) -> List[int]:
    all_codes = [c for cs in code_lists for c in cs]
    fixed = [c for c in all_codes if c != _STOP_CODE]
    if all_codes and all_codes[-1] == _STOP_CODE:
        fixed.append(_STOP_CODE)
    return fixed


def _correct_compound_codes(tokens: List[str]) -> List[int]:
    return _correct_compound_codes_from_lists(
        [[int(c) for c in t.split(",")] for t in tokens]
    )


class Matplotlib13API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            tokens = list(process.args[2:])
            expected = str(_correct_compound_codes(tokens))
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib13TestGenerator:
    @staticmethod
    def _rand_codes() -> List[int]:
        # A valid sub-path: starts with MOVETO, then 1-3 MOVETO/LINETO, no STOP.
        return [1] + [random.choice([1, 2]) for _ in range(random.randint(1, 3))]

    def _failing_lists(self) -> List[List[int]]:
        lists = [self._rand_codes() + [_STOP_CODE], self._rand_codes()]
        if random.random() < 0.5:
            lists.append(self._rand_codes())
        return lists

    def _passing_lists(self) -> List[List[int]]:
        return [self._rand_codes() for _ in range(random.randint(2, 3))]

    @staticmethod
    def _format(code_lists: List[List[int]]) -> str:
        return " ".join(",".join(str(c) for c in cs) for cs in code_lists)

    def make_failing(self) -> str:
        return self._format(self._failing_lists())

    def make_passing(self) -> str:
        return self._format(self._passing_lists())


class Matplotlib13SystemtestGenerator(
    SystemtestGenerator, Matplotlib13TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib13UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib13TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "from matplotlib.path import Path\n"
        ).body

    @staticmethod
    def _assert(code_lists: List[List[int]]) -> List[ast.stmt]:
        expected = _correct_compound_codes_from_lists(code_lists)
        src = (
            "paths = [Path(np.array([[float(k), float(k)] for k in range(len(cs))], "
            f"dtype=float), cs) for cs in {code_lists!r}]\n"
            f"self.assertEqual({expected!r}, "
            "[int(c) for c in Path.make_compound_path(*paths).codes])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._failing_lists())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._passing_lists())
        return test, TestResult.PASSING


grammar_13: Grammar = clean_up(
    {
        "<start>": ["<paths>"],
        "<paths>": ["<path>", "<path> <paths>"],
        "<path>": ["<codes>"],
        "<codes>": ["<code>", "<code>,<codes>"],
        "<code>": ["0", "1", "2"],
    }
)

assert is_valid_grammar(grammar_13)


# ======================================================================
# bug_24: the setter generated by ``matplotlib.axis._make_getset_interval``
# mixed up ``oldmin``/``oldmax`` when *growing* an already **inverted** data
# interval, so growing an inverted interval with values inside it wrongly
# shrank (and re-oriented) it.  The fix uses
# ``max(vmin, vmax, oldmin), min(vmin, vmax, oldmax)`` in the inverted branch.
#
# System-test format:  ``<old_min> <old_max> <new_min> <new_max>``.  The harness
# seeds the axis data interval with (old_min, old_max) (possibly inverted) then
# grows it with (new_min, new_max) and prints the resulting interval.  An
# inverted seed grown with interior values triggers the fault; a normal
# (increasing) seed never does.  The oracle recomputes the correct interval.
# ======================================================================


def _correct_interval(old_min, old_max, new_min, new_max) -> List[float]:
    vmin, vmax = new_min, new_max
    oldmin, oldmax = old_min, old_max
    if oldmin < oldmax:
        r = (min(vmin, vmax, oldmin), max(vmin, vmax, oldmax))
    else:
        r = (max(vmin, vmax, oldmin), min(vmin, vmax, oldmax))
    return [round(float(r[0]), 9), round(float(r[1]), 9)]


class Matplotlib24API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            vals = [float(x) for x in process.args[2:6]]
            expected = str(_correct_interval(*vals))
        except (IndexError, ValueError, TypeError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib24TestGenerator:
    @staticmethod
    def _seed_and_inner() -> Tuple[float, float, float, float]:
        lo = round(random.uniform(-50, 40), 3)
        hi = round(lo + random.uniform(2, 40), 3)
        mid = (lo + hi) / 2
        nlo = round(random.uniform(lo + 0.1, mid), 3)
        nhi = round(random.uniform(mid, hi - 0.1), 3)
        return lo, hi, nlo, nhi

    def make_failing(self) -> str:
        lo, hi, nlo, nhi = self._seed_and_inner()
        # inverted seed (old_min > old_max)
        return f"{hi} {lo} {nlo} {nhi}"

    def make_passing(self) -> str:
        lo, hi, nlo, nhi = self._seed_and_inner()
        # increasing seed (old_min < old_max)
        return f"{lo} {hi} {nlo} {nhi}"


class Matplotlib24SystemtestGenerator(
    SystemtestGenerator, Matplotlib24TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib24UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib24TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(old_min, old_max, new_min, new_max) -> List[ast.stmt]:
        expected = _correct_interval(old_min, old_max, new_min, new_max)
        src = (
            "fig, ax = plt.subplots()\n"
            "axis = ax.xaxis\n"
            f"axis.set_data_interval({old_min}, {old_max}, ignore=True)\n"
            f"axis.set_data_interval({new_min}, {new_max}, ignore=False)\n"
            f"self.assertEqual({expected!r}, "
            "[round(float(v), 9) for v in axis.get_data_interval()])\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lo, hi, nlo, nhi = self._seed_and_inner()
        test = self.get_empty_test()
        test.body = self._assert(hi, lo, nlo, nhi)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lo, hi, nlo, nhi = self._seed_and_inner()
        test = self.get_empty_test()
        test.body = self._assert(lo, hi, nlo, nhi)
        return test, TestResult.PASSING


grammar_24: Grammar = clean_up(
    dict(
        {"<start>": ["<float> <float> <float> <float>"]},
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_24)


# bug_26 is the identical ``_make_getset_interval`` inverted-interval fault as
# bug_24 (a different buggy/fixed commit pair), so it reuses the same oracle,
# generators and grammar.
Matplotlib26API = Matplotlib24API
Matplotlib26SystemtestGenerator = Matplotlib24SystemtestGenerator
Matplotlib26UnittestGenerator = Matplotlib24UnittestGenerator
grammar_26 = grammar_24


# ======================================================================
# bug_25: ``matplotlib.collections.EventCollection.__init__`` sorted the
# *positions* argument **in place** instead of taking a copy, so building an
# ``EventCollection`` from an unsorted array silently reordered the caller's
# array.  The fix copies the positions (``np.array(positions, copy=True)``)
# before sorting, leaving the input untouched.
#
# System-test format:  ``<number> <number> ...`` (the positions).  The harness
# builds an ``EventCollection`` from the array and prints the array *afterwards*.
# The correct (fixed) behaviour is that the input array is unchanged; an
# unsorted input therefore triggers the fault (buggy prints it sorted), while an
# already-sorted input never does.  The oracle recomputes the correct output
# (the input, unchanged).
# ======================================================================


def _round_num_list(values: List[float], ndigits: int = 6) -> str:
    return str([round(float(v), ndigits) for v in values])


class Matplotlib25API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            values = [float(x) for x in process.args[2:]]
            if not values:
                raise ValueError("no positions")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _round_num_list(values)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib25TestGenerator:
    @staticmethod
    def _distinct_values(k: int) -> List[float]:
        vals = set()
        while len(vals) < k:
            vals.add(round(random.uniform(-50, 50), 3))
        return list(vals)

    def _sorted(self) -> List[float]:
        return sorted(self._distinct_values(random.randint(3, 6)))

    def _unsorted(self) -> List[float]:
        vals = self._sorted()
        # Guarantee the list is *not* already in ascending order.
        while True:
            shuffled = vals[:]
            random.shuffle(shuffled)
            if shuffled != sorted(shuffled):
                return shuffled

    @staticmethod
    def _format(values: List[float]) -> str:
        return " ".join(str(v) for v in values)

    def make_failing(self) -> str:
        return self._format(self._unsorted())

    def make_passing(self) -> str:
        return self._format(self._sorted())


class Matplotlib25SystemtestGenerator(
    SystemtestGenerator, Matplotlib25TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib25UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib25TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "from matplotlib.collections import EventCollection\n"
        ).body

    @staticmethod
    def _assert(values: List[float]) -> List[ast.stmt]:
        expected = [round(float(v), 6) for v in values]
        src = (
            f"arr = np.array({list(values)!r}, dtype=float)\n"
            "EventCollection(arr)\n"
            f"self.assertEqual({expected!r}, "
            "[round(float(v), 6) for v in arr])\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._unsorted())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._sorted())
        return test, TestResult.PASSING


grammar_25: Grammar = clean_up(
    dict(
        {
            "<start>": ["<numbers>"],
            "<numbers>": ["<float>", "<float> <numbers>"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_25)


# ======================================================================
# bug_20: ``FigureCanvasBase.inaxes`` returned the topmost axes whose patch
# contained the point *without* checking whether that axes was visible, so an
# invisible axes still "captured" events.  The fix adds ``and a.get_visible()``
# to the filter.
#
# System-test format:  ``<visible> <x> <y>`` where ``<visible>`` is ``true`` or
# ``false`` and ``(x, y)`` is a pixel point *inside* the default single-subplot
# axes.  The harness builds the figure, applies the visibility, and prints
# ``inaxes((x, y)) is None``.  The correct (fixed) answer is ``True`` exactly
# when the axes is invisible; an invisible axes therefore triggers the fault
# (buggy still returns the axes), a visible one never does.
# ======================================================================


class Matplotlib20API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            visible = process.args[2]
            if visible not in ("true", "false"):
                raise ValueError("bad visible flag")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(visible == "false")
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib20TestGenerator:
    @staticmethod
    def _point() -> Tuple[float, float]:
        # Well inside the default single-subplot axes (x in [80, 576],
        # y in [52.8, 422.4] at 640x480).
        return (
            round(random.uniform(100, 560), 1),
            round(random.uniform(70, 410), 1),
        )

    def make_failing(self) -> str:
        x, y = self._point()
        return f"false {x} {y}"

    def make_passing(self) -> str:
        x, y = self._point()
        return f"true {x} {y}"


class Matplotlib20SystemtestGenerator(
    SystemtestGenerator, Matplotlib20TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib20UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib20TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(visible: bool, x: float, y: float) -> List[ast.stmt]:
        expected = not visible
        vis_line = "" if visible else "ax.set_visible(False)\n"
        src = (
            "fig, ax = plt.subplots()\n"
            f"{vis_line}"
            f"self.assertEqual({expected!r}, "
            f"fig.canvas.inaxes(({x}, {y})) is None)\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        x, y = self._point()
        test = self.get_empty_test()
        test.body = self._assert(False, x, y)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        x, y = self._point()
        test = self.get_empty_test()
        test.body = self._assert(True, x, y)
        return test, TestResult.PASSING


grammar_20: Grammar = clean_up(
    dict(
        {
            "<start>": ["<visible> <float> <float>"],
            "<visible>": ["true", "false"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_20)


# ======================================================================
# bug_10: turning a tick's labels on/off with ``Axis.set_tick_params`` did not
# propagate to the axis *offset text* (the ``1e9`` exponent label), so hiding
# every tick label still left the offset text visible.  The fix updates
# ``offsetText`` visibility from ``label1On``/``label2On`` whenever they change.
#
# System-test format:  ``<axis> <label1On> <label2On> <exp> <npts>`` where
# ``<axis>`` is ``x``/``y``, the two label flags are ``true``/``false``, ``exp``
# is the data's power-of-ten magnitude and ``npts`` the point count.  The
# harness plots large data, applies the tick params and prints the offset text's
# visibility.  The correct (fixed) visibility is ``label1On or label2On``;
# hiding both labels triggers the fault (buggy keeps the offset visible).
# ======================================================================


class Matplotlib10API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            b1 = process.args[3]
            b2 = process.args[4]
            if b1 not in ("true", "false") or b2 not in ("true", "false"):
                raise ValueError("bad flags")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(b1 == "true" or b2 == "true")
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib10TestGenerator:
    @staticmethod
    def _axis() -> str:
        return random.choice(["x", "y"])

    @staticmethod
    def _exp() -> int:
        return random.randint(7, 15)

    @staticmethod
    def _npts() -> int:
        return random.randint(3, 6)

    def make_failing(self) -> str:
        return f"{self._axis()} false false {self._exp()} {self._npts()}"

    def make_passing(self) -> str:
        b1, b2 = random.choice([("true", "false"), ("false", "true"),
                                ("true", "true")])
        return f"{self._axis()} {b1} {b2} {self._exp()} {self._npts()}"


class Matplotlib10SystemtestGenerator(
    SystemtestGenerator, Matplotlib10TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib10UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib10TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(axis: str, b1: bool, b2: bool, exp: int, npts: int) -> List[ast.stmt]:
        expected = b1 or b2
        plot = (
            "ax.plot(data, [0] * len(data))\n" if axis == "x" else "ax.plot(data)\n"
        )
        which = "ax.xaxis" if axis == "x" else "ax.yaxis"
        src = (
            "fig = plt.figure()\n"
            "ax = fig.add_subplot(1, 1, 1)\n"
            f"data = [(1.01 + 0.01 * i) * 10 ** {exp} for i in range({npts})]\n"
            f"{plot}"
            f"axis = {which}\n"
            f"axis.set_tick_params(label1On={b1!r}, label2On={b2!r})\n"
            f"self.assertEqual({expected!r}, axis.get_offset_text().get_visible())\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), False, False, self._exp(), self._npts())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        b1, b2 = random.choice([(True, False), (False, True), (True, True)])
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), b1, b2, self._exp(), self._npts())
        return test, TestResult.PASSING


grammar_10: Grammar = clean_up(
    dict(
        {
            "<start>": ["<axis> <flag> <flag> <number> <number>"],
            "<axis>": ["x", "y"],
            "<flag>": ["true", "false"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_10)


# ======================================================================
# bug_11: ``Text.get_window_extent(dpi=...)`` temporarily set ``figure.dpi`` to
# the requested value but, for *empty* text, returned early without restoring
# it, permanently corrupting the figure's dpi.  The fix uses a
# ``cbook._setattr_cm`` context manager so the dpi is always restored.
#
# System-test format:  ``<mult> <textkind>`` where ``<mult>`` is the dpi
# multiplier and ``<textkind>`` is the literal ``EMPTY`` (empty label) or a
# word (non-empty label).  The harness draws the label, calls
# ``get_window_extent(dpi=dpi*mult)`` and prints whether ``figure.dpi`` is
# unchanged.  The correct (fixed) answer is always ``True``; an *empty* label
# triggers the fault (buggy leaves dpi corrupted -> ``False``).
# ======================================================================


class Matplotlib11API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            float(process.args[2])
            _ = process.args[3]
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "True"  # fixed always leaves figure.dpi unchanged
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib11TestGenerator:
    @staticmethod
    def _mult() -> float:
        return round(random.uniform(2.0, 12.0), 3)

    @staticmethod
    def _word() -> str:
        return "".join(
            random.choice(string.ascii_lowercase)
            for _ in range(random.randint(3, 8))
        )

    def make_failing(self) -> str:
        return f"{self._mult()} EMPTY"

    def make_passing(self) -> str:
        return f"{self._mult()} {self._word()}"


class Matplotlib11SystemtestGenerator(
    SystemtestGenerator, Matplotlib11TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib11UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib11TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(mult: float, text: str) -> List[ast.stmt]:
        src = (
            "fig, ax = plt.subplots()\n"
            f"t1 = ax.text(0.5, 0.5, {text!r}, ha='left', va='bottom')\n"
            "fig.canvas.draw()\n"
            "dpi = fig.dpi\n"
            "t1.get_window_extent()\n"
            f"t1.get_window_extent(dpi=dpi * {mult})\n"
            "self.assertEqual(True, fig.dpi == dpi)\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._mult(), "")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._mult(), self._word())
        return test, TestResult.PASSING


grammar_11: Grammar = clean_up(
    dict(
        {
            "<start>": ["<float> <textkind>"],
            "<textkind>": ["EMPTY", "<letters>"],
            "<letters>": ["<letter>", "<letter><letters>"],
            "<letter>": srange(string.ascii_lowercase),
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_11)


# ======================================================================
# bug_14: ``Text.update`` applied the ``fontproperties`` kwarg *after* the
# other kwargs, so an explicit ``size=`` (or other font kwarg) passed *before*
# ``fontproperties`` in the call was overwritten by the fontproperties'
# defaults.  The fix pops and applies ``fontproperties`` *first* so explicit
# kwargs always win.
#
# System-test format:  ``<order> <size> <family>`` where ``<order>`` is ``sf``
# (``size`` kwarg before ``fontproperties``) or ``fs`` (after) and ``<family>``
# is a font family.  The harness sets an axis label with that kwarg order and
# prints the resulting font size.  The correct (fixed) size is always the
# explicit ``size``; the ``sf`` order triggers the fault (buggy resets the size
# to the fontproperties' default of 10).
# ======================================================================

# Single-word families only: a hyphenated string such as ``sans-serif`` is
# (mis)parsed as a fontconfig pattern by ``FontProperties`` and raises.
_FONT_FAMILIES = ["serif", "monospace", "cursive", "fantasy"]


class Matplotlib14API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            order = process.args[2]
            size = float(process.args[3])
            if order not in ("sf", "fs"):
                raise ValueError("bad order")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(float(size))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib14TestGenerator:
    @staticmethod
    def _size() -> float:
        # Any size != 10.0 (the fontproperties default the buggy code falls to).
        return round(random.uniform(15.0, 60.0), 1)

    @staticmethod
    def _family() -> str:
        return random.choice(_FONT_FAMILIES)

    def make_failing(self) -> str:
        return f"sf {self._size()} {self._family()}"

    def make_passing(self) -> str:
        return f"fs {self._size()} {self._family()}"


class Matplotlib14SystemtestGenerator(
    SystemtestGenerator, Matplotlib14TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib14UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib14TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(order: str, size: float, family: str) -> List[ast.stmt]:
        if order == "sf":
            call = (
                f"ax.set_xlabel('value', size={size}, fontproperties={family!r})"
            )
        else:
            call = (
                f"ax.set_xlabel('value', fontproperties={family!r}, size={size})"
            )
        src = (
            "fig, ax = plt.subplots()\n"
            f"t = {call}\n"
            f"self.assertEqual({float(size)!r}, t.get_size())\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("sf", self._size(), self._family())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("fs", self._size(), self._family())
        return test, TestResult.PASSING


grammar_14: Grammar = clean_up(
    dict(
        {
            "<start>": ["<order> <float> <family>"],
            "<order>": ["sf", "fs"],
            "<family>": ["serif", "monospace", "cursive", "fantasy"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_14)


# ======================================================================
# bug_2: ``Axes.scatter`` with an *unfilled* marker forced ``edgecolors='face'``
# and still passed the colors as ``facecolors``, so the points were drawn
# filled.  The fix sets ``facecolors='none'`` and routes the colors to
# ``edgecolors`` for unfilled markers, leaving them hollow.
#
# System-test format:  ``<fillstyle> <n>`` where ``<fillstyle>`` is ``none``
# (unfilled 'o') or ``full`` (filled) and ``n`` is the number of points.  The
# harness scatters ``n`` points with ``n`` distinct colors and prints the number
# of facecolor rows.  The correct (fixed) count is ``0`` for an unfilled marker
# and ``n`` for a filled one; ``fillstyle='none'`` triggers the fault (buggy
# still stores ``n`` facecolors).
# ======================================================================


class Matplotlib2API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            fillstyle = process.args[2]
            n = int(process.args[3])
            if fillstyle not in ("none", "full"):
                raise ValueError("bad fillstyle")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(0 if fillstyle == "none" else n)
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib2TestGenerator:
    @staticmethod
    def _n() -> int:
        return random.randint(2, 16)

    def make_failing(self) -> str:
        return f"none {self._n()}"

    def make_passing(self) -> str:
        return f"full {self._n()}"


class Matplotlib2SystemtestGenerator(
    SystemtestGenerator, Matplotlib2TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib2UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib2TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
            "from matplotlib.markers import MarkerStyle\n"
        ).body

    @staticmethod
    def _assert(fillstyle: str, n: int) -> List[ast.stmt]:
        expected = 0 if fillstyle == "none" else n
        src = (
            f"grays = [round((i + 1) / ({n} + 1), 3) for i in range({n})]\n"
            f"coll = plt.scatter(range({n}), range({n}), "
            "c=[str(g) for g in grays], "
            f"marker=MarkerStyle('o', fillstyle={fillstyle!r}), "
            f"linewidths=[1.0] * {n})\n"
            f"self.assertEqual({expected!r}, coll.get_facecolors().shape[0])\n"
            "plt.close('all')\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("none", self._n())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("full", self._n())
        return test, TestResult.PASSING


grammar_2: Grammar = clean_up(
    dict(
        {
            "<start>": ["<fillstyle> <number>"],
            "<fillstyle>": ["none", "full"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_2)


# ======================================================================
# bug_5: ``Axes.scatter`` with an *unfilled* marker overwrote the caller's
# ``linewidths`` with ``rcParams['lines.linewidth']`` unconditionally, so an
# explicit ``linewidths=`` was ignored.  The fix only falls back to the rcParam
# when ``linewidths`` is ``None``.
#
# System-test format:  ``<marker> <lw>`` where ``<marker>`` is an *unfilled*
# marker (e.g. ``x``, ``+``) or a *filled* one (e.g. ``o``, ``s``) and ``<lw>``
# is the requested line width (never the ``1.5`` default).  The harness scatters
# points with that marker and ``linewidths=lw`` and prints the resulting line
# width.  The correct (fixed) width is always ``lw``; an unfilled marker
# triggers the fault (buggy reports ``1.5``).
# ======================================================================

_UNFILLED_MARKERS = ["x", "+", "1", "2", "3", "4"]
_FILLED_MARKERS2 = ["o", "s", "^", "D", "v", "p"]


class Matplotlib5API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            _ = process.args[2]
            lw = float(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(float(lw))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib5TestGenerator:
    @staticmethod
    def _lw() -> float:
        # Any width other than the 1.5 rcParams default.
        return round(random.uniform(2.0, 9.0), 1)

    def make_failing(self) -> str:
        return f"{random.choice(_UNFILLED_MARKERS)} {self._lw()}"

    def make_passing(self) -> str:
        return f"{random.choice(_FILLED_MARKERS2)} {self._lw()}"


class Matplotlib5SystemtestGenerator(
    SystemtestGenerator, Matplotlib5TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib5UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib5TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(marker: str, lw: float) -> List[ast.stmt]:
        src = (
            "fig, ax = plt.subplots()\n"
            f"pc = ax.scatter(range(5), [0] * 5, c='C0', marker={marker!r}, "
            f"s=100, linewidths={lw})\n"
            f"self.assertEqual({float(lw)!r}, float(pc.get_linewidths()[0]))\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(random.choice(_UNFILLED_MARKERS), self._lw())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(random.choice(_FILLED_MARKERS2), self._lw())
        return test, TestResult.PASSING


grammar_5: Grammar = clean_up(
    dict(
        {
            "<start>": ["<marker> <float>"],
            "<marker>": ["x", "+", "1", "2", "3", "4", "o", "s", "^", "D", "v", "p"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_5)


# ======================================================================
# bug_4: ``Axes.vlines``/``Axes.hlines`` hard-coded their default ``colors='k'``
# instead of honouring ``rcParams['lines.color']``.  The fix changes the default
# to ``None`` (which resolves to the rcParam).
#
# System-test format:  ``<func> <color> <pos> <lo> <hi>`` where ``<func>`` is
# ``vlines``/``hlines`` and ``<color>`` is the ``lines.color`` rc value.  The
# harness draws the line under that rc context (no explicit color) and prints
# whether the drawn colour matches the rc colour.  The correct (fixed) answer is
# always ``True``; a *non-black* rc colour triggers the fault (buggy draws
# black), a black one never does.
# ======================================================================

_NONBLACK_COLORS = [
    "red", "green", "blue", "cyan", "magenta", "yellow", "orange",
    "purple", "brown", "pink", "olive", "teal",
]
_BLACK_COLORS = ["black", "k", "#000000"]


class Matplotlib4API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            func = process.args[2]
            if func not in ("vlines", "hlines"):
                raise ValueError("bad func")
            float(process.args[4])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "True"  # fixed: line colour always equals the rc lines.color
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib4TestGenerator:
    @staticmethod
    def _pos_lo_hi() -> Tuple[float, float, float]:
        pos = round(random.uniform(-5, 5), 2)
        lo = round(random.uniform(-5, 0), 2)
        hi = round(lo + random.uniform(1, 6), 2)
        return pos, lo, hi

    @staticmethod
    def _func() -> str:
        return random.choice(["vlines", "hlines"])

    def make_failing(self) -> str:
        pos, lo, hi = self._pos_lo_hi()
        return f"{self._func()} {random.choice(_NONBLACK_COLORS)} {pos} {lo} {hi}"

    def make_passing(self) -> str:
        pos, lo, hi = self._pos_lo_hi()
        return f"{self._func()} {random.choice(_BLACK_COLORS)} {pos} {lo} {hi}"


class Matplotlib4SystemtestGenerator(
    SystemtestGenerator, Matplotlib4TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib4UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib4TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib as mpl\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(func: str, color: str, pos: float, lo: float, hi: float) -> List[ast.stmt]:
        src = (
            "fig, ax = plt.subplots()\n"
            f"with mpl.rc_context({{'lines.color': {color!r}}}):\n"
            f"    lines = ax.{func}({pos}, {lo}, {hi})\n"
            f"    self.assertEqual(True, "
            f"mpl.colors.same_color(lines.get_color(), {color!r}))\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pos, lo, hi = self._pos_lo_hi()
        test = self.get_empty_test()
        test.body = self._assert(self._func(), random.choice(_NONBLACK_COLORS), pos, lo, hi)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pos, lo, hi = self._pos_lo_hi()
        test = self.get_empty_test()
        test.body = self._assert(self._func(), random.choice(_BLACK_COLORS), pos, lo, hi)
        return test, TestResult.PASSING


grammar_4: Grammar = clean_up(
    dict(
        {
            "<start>": ["<func> <color> <float> <float> <float>"],
            "<func>": ["vlines", "hlines"],
            "<color>": _NONBLACK_COLORS + _BLACK_COLORS,
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_4)


# ======================================================================
# bug_21: ``Axes.boxplot`` built the box/whisker/cap/median line properties from
# the general ``rcParams`` (including ``lines.marker``), so a non-default
# ``lines.marker`` wrongly put markers on those lines.  The fix forces
# ``marker=''`` for those four artist groups (fliers/means keep their markers).
#
# System-test format:  ``<mode> <group> <marker>``.  For ``mode=box`` the harness
# sets ``rcParams['lines.marker']=marker`` and prints the marker of a
# box/whisker/cap/median line (correct fixed value: ``''``).  For ``mode=flier``
# it sets the flier/mean marker rcParam and prints that artist's marker (value:
# ``marker``).  ``mode=box`` triggers the fault (buggy leaks the rc marker).
# ======================================================================

_BOX_GROUPS = ["whiskers", "caps", "boxes", "medians"]
_FLIER_GROUPS = ["fliers", "means"]
_BOX_MARKERS = ["s", "o", "^", "x", "+", "D", "v", "p", "*", "h"]


class Matplotlib21API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            marker = process.args[4]
            if mode not in ("box", "flier"):
                raise ValueError("bad mode")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "" if mode == "box" else marker
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Matplotlib21TestGenerator:
    def make_failing(self) -> str:
        return (
            f"box {random.choice(_BOX_GROUPS)} {random.choice(_BOX_MARKERS)}"
        )

    def make_passing(self) -> str:
        return (
            f"flier {random.choice(_FLIER_GROUPS)} {random.choice(_BOX_MARKERS)}"
        )


class Matplotlib21SystemtestGenerator(
    SystemtestGenerator, Matplotlib21TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib21UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib21TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(mode: str, group: str, marker: str) -> List[ast.stmt]:
        expected = "" if mode == "box" else marker
        if mode == "box":
            setrc = f"plt.rcParams['lines.marker'] = {marker!r}\n"
        elif group == "fliers":
            setrc = f"plt.rcParams['boxplot.flierprops.marker'] = {marker!r}\n"
        else:
            setrc = f"plt.rcParams['boxplot.meanprops.marker'] = {marker!r}\n"
        src = (
            "plt.rcdefaults()\n"
            f"{setrc}"
            "fig, ax = plt.subplots()\n"
            "d = np.arange(100)\n"
            "d[-1] = 150\n"
            "bxp = ax.boxplot(d, showmeans=True)\n"
            f"self.assertEqual({expected!r}, bxp[{group!r}][0].get_marker())\n"
            "plt.close(fig)\n"
            "plt.rcdefaults()\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(
            "box", random.choice(_BOX_GROUPS), random.choice(_BOX_MARKERS)
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(
            "flier", random.choice(_FLIER_GROUPS), random.choice(_BOX_MARKERS)
        )
        return test, TestResult.PASSING


grammar_21: Grammar = clean_up(
    {
        "<start>": ["<mode> <group> <marker>"],
        "<mode>": ["box", "flier"],
        "<group>": _BOX_GROUPS + _FLIER_GROUPS,
        "<marker>": _BOX_MARKERS,
    }
)

assert is_valid_grammar(grammar_21)


# ======================================================================
# bug_27: ``Colorbar.set_label`` coerced its argument with ``str(label)``, so
# ``set_label(None)`` produced the literal label ``"None"`` instead of clearing
# it.  The fix stores ``label`` unchanged (``None`` -> empty label).
#
# System-test format:  ``<orientation> <initial> <label>`` where
# ``<orientation>`` is ``v``/``h``, ``<initial>`` the constructor label and
# ``<label>`` is either the literal ``NONE`` (``set_label(None)``) or a word.
# The harness builds the colorbar, calls ``set_label`` and prints the long-axis
# label.  The correct (fixed) label is ``''`` for ``NONE`` and the word
# otherwise; ``NONE`` triggers the fault (buggy yields ``"None"``).
# ======================================================================


class Matplotlib27API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            orientation = process.args[2]
            label = process.args[4]
            if orientation not in ("v", "h"):
                raise ValueError("bad orientation")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "" if label == "NONE" else label
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Matplotlib27TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(
            random.choice(string.ascii_lowercase)
            for _ in range(random.randint(3, 8))
        )

    @staticmethod
    def _orient() -> str:
        return random.choice(["v", "h"])

    def make_failing(self) -> str:
        return f"{self._orient()} {self._word()} NONE"

    def make_passing(self) -> str:
        return f"{self._orient()} {self._word()} {self._word()}"


class Matplotlib27SystemtestGenerator(
    SystemtestGenerator, Matplotlib27TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib27UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib27TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(orient: str, initial: str, label: str) -> List[ast.stmt]:
        expected = "" if label == "NONE" else label
        orientation = "vertical" if orient == "v" else "horizontal"
        getlabel = "get_xlabel" if orient == "h" else "get_ylabel"
        label_expr = "None" if label == "NONE" else repr(label)
        src = (
            "fig, ax = plt.subplots()\n"
            "im = ax.imshow([[1, 2], [3, 4]])\n"
            f"cbar = fig.colorbar(im, orientation={orientation!r}, "
            f"label={initial!r})\n"
            f"cbar.set_label({label_expr})\n"
            f"self.assertEqual({expected!r}, cbar.ax.{getlabel}())\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._orient(), self._word(), "NONE")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert(self._orient(), self._word(), self._word())
        return test, TestResult.PASSING


grammar_27: Grammar = clean_up(
    {
        "<start>": ["<orientation> <word> <label>"],
        "<orientation>": ["v", "h"],
        "<label>": ["NONE", "<word>"],
        "<word>": ["<letter>", "<letter><word>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_27)


# ======================================================================
# bug_15: ``matplotlib.colors.SymLogNorm`` had no ``base`` parameter (the log
# base was hard-wired to ``np.e``).  The fix adds a ``base`` kwarg and divides
# the logarithm by ``log(base)``.  A ``SymLogNorm(..., base=10)`` call therefore
# raises ``TypeError`` on the buggy build and normalises correctly on the fixed
# one.
#
# System-test format:  ``<mode> <linthresh> <linscale> <vmin> <vmax> <base>
# <value>`` where ``<mode>`` is ``basekw`` (pass ``base=``) or ``nobase`` (omit
# it, both builds use ``np.e``).  The harness prints ``norm(value)``.  The
# correct (fixed) value is recomputed in pure Python; ``basekw`` triggers the
# fault (buggy raises ``TypeError`` -> no output).
# ======================================================================


def _symlognorm_value(
    linthresh: float,
    linscale: float,
    vmin: float,
    vmax: float,
    base: float,
    value: float,
) -> float:
    import math

    adj = linscale / (1.0 - base ** -1)
    log_base = math.log(base)

    def tr(a: float) -> float:
        if abs(a) > linthresh:
            s = 1.0 if a > 0 else (-1.0 if a < 0 else 0.0)
            return (adj + math.log(abs(a) / linthresh) / log_base) * s * linthresh
        return a * adj

    upper = tr(vmax)
    lower = tr(vmin)
    return (tr(value) - lower) / (upper - lower)


def _parse_base(token: str) -> float:
    import math

    if token == "e":
        return math.e
    return float(token)


class Matplotlib15API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            import math

            mode = process.args[2]
            linthresh = float(process.args[3])
            linscale = float(process.args[4])
            vmin = float(process.args[5])
            vmax = float(process.args[6])
            base = math.e if mode == "nobase" else _parse_base(process.args[7])
            value = float(process.args[8])
            if mode not in ("basekw", "nobase"):
                raise ValueError("bad mode")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = _symlognorm_value(linthresh, linscale, vmin, vmax, base, value)
        out = process.stdout.decode("utf8").strip()
        try:
            got = float(out)
        except ValueError:
            return TestResult.FAILING, f"Expected {expected}, but was {out!r}"
        if process.returncode == 0 and abs(got - expected) < 1e-4:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {got}"


class Matplotlib15TestGenerator:
    @staticmethod
    def _params() -> Tuple[float, float, float, float, float]:
        linthresh = round(random.uniform(0.5, 3.0), 3)
        linscale = round(random.uniform(0.5, 2.0), 3)
        vmin = round(random.uniform(-30, -5), 3)
        vmax = round(random.uniform(5, 30), 3)
        value = round(random.uniform(vmin + 0.5, vmax - 0.5), 3)
        return linthresh, linscale, vmin, vmax, value

    def make_failing(self) -> str:
        lt, ls, vmin, vmax, val = self._params()
        base = random.choice(["2", "e", "10"])
        return f"basekw {lt} {ls} {vmin} {vmax} {base} {val}"

    def make_passing(self) -> str:
        lt, ls, vmin, vmax, val = self._params()
        return f"nobase {lt} {ls} {vmin} {vmax} e {val}"


class Matplotlib15SystemtestGenerator(
    SystemtestGenerator, Matplotlib15TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib15UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib15TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import math\n"
            "import warnings\n"
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.colors as mcolors\n"
        ).body

    @staticmethod
    def _assert(mode: str, lt: float, ls: float, vmin: float, vmax: float,
                base_token: str, value: float) -> List[ast.stmt]:
        import math

        base = math.e if mode == "nobase" else _parse_base(base_token)
        expected = _symlognorm_value(lt, ls, vmin, vmax, base, value)
        if mode == "basekw":
            base_expr = "math.e" if base_token == "e" else base_token
            ctor = (
                f"mcolors.SymLogNorm({lt}, {ls}, vmin={vmin}, vmax={vmax}, "
                f"base={base_expr})"
            )
        else:
            ctor = f"mcolors.SymLogNorm({lt}, {ls}, vmin={vmin}, vmax={vmax})"
        src = (
            "with warnings.catch_warnings():\n"
            "    warnings.simplefilter('ignore')\n"
            f"    norm = {ctor}\n"
            f"    self.assertAlmostEqual({expected!r}, float(norm({value})), places=4)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lt, ls, vmin, vmax, val = self._params()
        base = random.choice(["2", "e", "10"])
        test = self.get_empty_test()
        test.body = self._assert("basekw", lt, ls, vmin, vmax, base, val)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lt, ls, vmin, vmax, val = self._params()
        test = self.get_empty_test()
        test.body = self._assert("nobase", lt, ls, vmin, vmax, "e", val)
        return test, TestResult.PASSING


grammar_15: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <float> <float> <float> <float> <base> <float>"],
            "<mode>": ["basekw", "nobase"],
            "<base>": ["2", "e", "10"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_15)


# ======================================================================
# bug_29: ``Axis.set_inverted`` used ``set_view_interval`` directly, which does
# not propagate to *shared* axes.  The fix reimplements ``set_inverted`` in the
# ``XAxis``/``YAxis`` subclasses via ``set_xlim``/``set_ylim`` so shared
# siblings get inverted too.
#
# System-test format:  ``<axis> <inverted> <lo> <hi>`` where ``<axis>`` is
# ``x``/``y``, ``<inverted>`` is ``true``/``false`` and ``(lo, hi)`` seed the
# primary axes' data.  The harness makes two axes sharing that axis, inverts the
# primary and prints whether the *sibling* is inverted.  The correct (fixed)
# answer is the ``inverted`` flag; inverting (``true``) triggers the fault
# (buggy leaves the sibling un-inverted).
# ======================================================================


class Matplotlib29API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            axis = process.args[2]
            inverted = process.args[3]
            if axis not in ("x", "y") or inverted not in ("true", "false"):
                raise ValueError("bad args")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(inverted == "true")
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib29TestGenerator:
    @staticmethod
    def _lo_hi() -> Tuple[float, float]:
        lo = round(random.uniform(-20, 10), 2)
        hi = round(lo + random.uniform(1, 20), 2)
        return lo, hi

    @staticmethod
    def _axis() -> str:
        return random.choice(["x", "y"])

    def make_failing(self) -> str:
        lo, hi = self._lo_hi()
        return f"{self._axis()} true {lo} {hi}"

    def make_passing(self) -> str:
        lo, hi = self._lo_hi()
        return f"{self._axis()} false {lo} {hi}"


class Matplotlib29SystemtestGenerator(
    SystemtestGenerator, Matplotlib29TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib29UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib29TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(axis: str, inverted: bool, lo: float, hi: float) -> List[ast.stmt]:
        share = "sharey" if axis == "y" else "sharex"
        src = (
            "fig = plt.figure()\n"
            "ax0 = plt.subplot(211)\n"
            f"ax1 = plt.subplot(212, {share}=ax0)\n"
            f"ax0.plot([{lo}, {hi}], [{lo}, {hi}])\n"
            f"ax0.{axis}axis.set_inverted({inverted!r})\n"
            f"self.assertEqual({inverted!r}, ax1.{axis}axis_inverted())\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lo, hi = self._lo_hi()
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), True, lo, hi)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lo, hi = self._lo_hi()
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), False, lo, hi)
        return test, TestResult.PASSING


grammar_29: Grammar = clean_up(
    dict(
        {
            "<start>": ["<axis> <inverted> <float> <float>"],
            "<axis>": ["x", "y"],
            "<inverted>": ["true", "false"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_29)


# ======================================================================
# bug_28: on a *log*-scaled x-axis, ``set_xlim`` with a non-positive endpoint
# tried to fall back to ``old_left``/``old_right`` which were only assigned in a
# different branch, raising ``UnboundLocalError``.  The fix fetches the old
# limits inside the log branch before using them.  (Only ``set_xlim`` is fixed
# by this commit, so the subject uses the x-axis exclusively.)
#
# System-test format:  ``<axis> <left> <right>`` (axis is always ``x``).  The
# harness log-scales the axis, calls ``set_xlim(left, right)`` and prints ``OK``
# on success.  A non-positive endpoint triggers the fault (buggy crashes -> no
# output); two positive endpoints never do.  The correct (fixed) result is
# always ``OK`` (the invalid limit is warned about and ignored).
# ======================================================================


class Matplotlib28API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            axis = process.args[2]
            float(process.args[3])
            float(process.args[4])
            if axis != "x":
                raise ValueError("bad axis")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "OK"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib28TestGenerator:
    @staticmethod
    def _axis() -> str:
        return "x"

    def make_failing(self) -> str:
        # A non-positive endpoint on a log axis.
        left = round(random.uniform(-10, -0.1), 2)
        right = round(random.uniform(1, 100), 2)
        return f"{self._axis()} {left} {right}"

    def make_passing(self) -> str:
        left = round(random.uniform(0.1, 5), 2)
        right = round(left + random.uniform(1, 50), 2)
        return f"{self._axis()} {left} {right}"


class Matplotlib28SystemtestGenerator(
    SystemtestGenerator, Matplotlib28TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib28UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib28TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import warnings\n"
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(axis: str, left: float, right: float) -> List[ast.stmt]:
        src = (
            "fig, ax = plt.subplots()\n"
            f"ax.set_{axis}scale('log')\n"
            "ok = 'FAIL'\n"
            "with warnings.catch_warnings():\n"
            "    warnings.simplefilter('ignore')\n"
            f"    ax.set_{axis}lim({left}, {right})\n"
            "    ok = 'OK'\n"
            "self.assertEqual('OK', ok)\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        left = round(random.uniform(-10, -0.1), 2)
        right = round(random.uniform(1, 100), 2)
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), left, right)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        left = round(random.uniform(0.1, 5), 2)
        right = round(left + random.uniform(1, 50), 2)
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), left, right)
        return test, TestResult.PASSING


grammar_28: Grammar = clean_up(
    dict(
        {
            "<start>": ["<axis> <float> <float>"],
            "<axis>": ["x"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_28)


# ======================================================================
# bug_8: ``set_xlim``/``set_ylim`` set the view interval but did not clear the
# ``_stale_viewlim`` flag, so the next ``draw`` re-autoscaled and *reverted* the
# freshly-set limits (unless autoscaling had been turned off).  The fix clears
# the stale-viewlim flag for the axes and its shared siblings.
#
# System-test format:  ``<axis> <auto> <lo> <hi>`` where ``<axis>`` is ``x``/``y``
# and ``<auto>`` is ``true``/``false``/``none``.  The harness scatters data whose
# range differs from ``(lo, hi)``, sets the limit with that ``auto`` value,
# draws, and prints the resulting limit.  The correct (fixed) limit is always
# ``(lo, hi)``; ``auto`` ``true``/``none`` triggers the fault (buggy re-autoscales
# back to the data range).
# ======================================================================

_AUTO_MAP = {"true": True, "false": False, "none": None}


class Matplotlib8API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            axis = process.args[2]
            auto = process.args[3]
            lo = round(float(process.args[4]), 3)
            hi = round(float(process.args[5]), 3)
            if axis not in ("x", "y") or auto not in _AUTO_MAP:
                raise ValueError("bad args")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str([lo, hi])
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib8TestGenerator:
    @staticmethod
    def _axis() -> str:
        return random.choice(["x", "y"])

    @staticmethod
    def _lo_hi() -> Tuple[float, float]:
        # Clearly wider than the data range (~+-0.11) so a buggy re-autoscale
        # produces a visibly different limit.
        lo = round(random.uniform(-2.0, -0.3), 3)
        hi = round(random.uniform(0.3, 2.0), 3)
        return lo, hi

    def make_failing(self) -> str:
        lo, hi = self._lo_hi()
        return f"{self._axis()} {random.choice(['true', 'none'])} {lo} {hi}"

    def make_passing(self) -> str:
        lo, hi = self._lo_hi()
        return f"{self._axis()} false {lo} {hi}"


class Matplotlib8SystemtestGenerator(
    SystemtestGenerator, Matplotlib8TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib8UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib8TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(axis: str, auto: str, lo: float, hi: float) -> List[ast.stmt]:
        expected = [round(lo, 3), round(hi, 3)]
        auto_val = _AUTO_MAP[auto]
        if axis == "y":
            scatter = "ax.scatter(np.arange(100), np.linspace(-.1, .1, 100))"
        else:
            scatter = "ax.scatter(np.linspace(-.1, .1, 100), np.arange(100))"
        src = (
            "fig, ax = plt.subplots()\n"
            f"{scatter}\n"
            f"ax.set_{axis}lim(({lo}, {hi}), auto={auto_val!r})\n"
            "fig.canvas.draw()\n"
            f"self.assertEqual({expected!r}, "
            f"[round(float(v), 3) for v in ax.get_{axis}lim()])\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lo, hi = self._lo_hi()
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), random.choice(["true", "none"]), lo, hi)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        lo, hi = self._lo_hi()
        test = self.get_empty_test()
        test.body = self._assert(self._axis(), "false", lo, hi)
        return test, TestResult.PASSING


grammar_8: Grammar = clean_up(
    dict(
        {
            "<start>": ["<axis> <auto> <float> <float>"],
            "<axis>": ["x", "y"],
            "<auto>": ["true", "false", "none"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_8)


# ======================================================================
# bug_18/bug_19: a polar axes with *no data* autoscaled its radial axis from the
# initial ``(-inf, inf)`` limits and expanded them to a tiny ``(-0.055, 0.055)``
# instead of the documented ``(0, 1)``.  The fix adds ``RadialLocator.nonsingular``
# which returns ``(0, 1)`` for the initial limits.
#
# System-test format:  ``<trigger> <w> <h>`` where ``<trigger>`` selects how the
# empty polar axes is exercised (``autoscale``/``relim``/``polar`` force the
# faulty autoscale; ``none``/``draw`` do not) and ``(w, h)`` is the figure size.
# The harness prints the resulting ``[rmin, rmax]``.  The correct (fixed) value
# is ``[0.0, 1.0]`` for the ``none``/``draw`` triggers and ``[0.0, 1.05]`` for the
# autoscaling triggers (the 5% radial margin on the ``(0, 1)`` default); the
# buggy build instead collapses the autoscaling triggers to ``[-0.055, 0.055]``.
# ======================================================================

_POLAR_FAULT_TRIGGERS = ("autoscale", "relim", "polar")


def _polar_expected(trigger: str) -> List[float]:
    return [0.0, 1.05] if trigger in _POLAR_FAULT_TRIGGERS else [0.0, 1.0]


class Matplotlib18API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            trigger = process.args[2]
            float(process.args[3])
            float(process.args[4])
            if trigger not in ("autoscale", "relim", "polar", "none", "draw"):
                raise ValueError("bad trigger")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(_polar_expected(trigger))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib18TestGenerator:
    @staticmethod
    def _wh() -> Tuple[float, float]:
        return round(random.uniform(3.0, 8.0), 2), round(random.uniform(3.0, 8.0), 2)

    def make_failing(self) -> str:
        w, h = self._wh()
        return f"{random.choice(['autoscale', 'relim', 'polar'])} {w} {h}"

    def make_passing(self) -> str:
        w, h = self._wh()
        return f"{random.choice(['none', 'draw'])} {w} {h}"


class Matplotlib18SystemtestGenerator(
    SystemtestGenerator, Matplotlib18TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib18UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib18TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(trigger: str, w: float, h: float) -> List[ast.stmt]:
        if trigger == "polar":
            setup = (
                f"plt.figure(figsize=({w}, {h}))\n"
                "plt.polar()\n"
                "ax = plt.gca()\n"
            )
        else:
            setup = (
                f"fig = plt.figure(figsize=({w}, {h}))\n"
                "ax = fig.add_subplot(projection='polar')\n"
            )
            if trigger == "draw":
                setup += "fig.canvas.draw()\n"
            elif trigger == "autoscale":
                setup += "ax.autoscale()\nfig.canvas.draw()\n"
            elif trigger == "relim":
                setup += "ax.relim()\nax.autoscale_view()\nfig.canvas.draw()\n"
        expected = _polar_expected(trigger)
        src = (
            f"{setup}"
            f"self.assertEqual({expected!r}, "
            "[round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])\n"
            "plt.close('all')\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w, h = self._wh()
        test = self.get_empty_test()
        test.body = self._assert(random.choice(["autoscale", "relim", "polar"]), w, h)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        w, h = self._wh()
        test = self.get_empty_test()
        test.body = self._assert(random.choice(["none", "draw"]), w, h)
        return test, TestResult.PASSING


grammar_18: Grammar = clean_up(
    dict(
        {
            "<start>": ["<trigger> <float> <float>"],
            "<trigger>": ["autoscale", "relim", "polar", "none", "draw"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_18)


# bug_19 is the identical polar no-data ``RadialLocator.nonsingular`` fault as
# bug_18 (a different buggy/fixed commit pair), so it reuses everything.
Matplotlib19API = Matplotlib18API
Matplotlib19SystemtestGenerator = Matplotlib18SystemtestGenerator
Matplotlib19UnittestGenerator = Matplotlib18UnittestGenerator
grammar_19 = grammar_18


# ======================================================================
# bug_12: ``Axes.vlines``/``hlines`` used ``cbook.delete_masked_points`` which
# *removed* masked/NaN entries, shifting every following line's colour by one
# (and shrinking the collection).  The fix uses ``_combine_masks`` to build a
# masked vertex array, so masked entries become *empty* segments that keep the
# per-line colour alignment.
#
# System-test format:  ``<func> <data>`` where ``<func>`` is ``vlines``/``hlines``
# and ``<data>`` is a comma-separated list of numbers with optional ``nan``
# entries.  The harness draws the lines and prints the number of segments.  The
# correct (fixed) count equals the number of data points (masked -> empty
# segment); a ``nan`` entry triggers the fault (buggy drops the segment).
# ======================================================================


class Matplotlib12API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            func = process.args[2]
            tokens = process.args[3].split(",")
            if func not in ("vlines", "hlines") or not tokens:
                raise ValueError("bad args")
            for t in tokens:
                if t != "nan":
                    float(t)
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(len(tokens))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib12TestGenerator:
    @staticmethod
    def _func() -> str:
        return random.choice(["vlines", "hlines"])

    @staticmethod
    def _values(n: int) -> List[float]:
        return [round(random.uniform(-10, 10), 2) for _ in range(n)]

    def make_failing(self) -> str:
        n = random.randint(4, 7)
        vals = [str(v) for v in self._values(n)]
        # Replace 1-2 interior entries with nan (keep >=2 real points).
        k = random.randint(1, 2)
        idxs = random.sample(range(n), k)
        for i in idxs:
            vals[i] = "nan"
        return f"{self._func()} {','.join(vals)}"

    def make_passing(self) -> str:
        n = random.randint(2, 7)
        vals = [str(v) for v in self._values(n)]
        return f"{self._func()} {','.join(vals)}"


class Matplotlib12SystemtestGenerator(
    SystemtestGenerator, Matplotlib12TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib12UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib12TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(func: str, tokens: List[str]) -> List[ast.stmt]:
        expected = len(tokens)
        data = "[" + ", ".join(
            "float('nan')" if t == "nan" else t for t in tokens
        ) + "]"
        src = (
            "fig, ax = plt.subplots()\n"
            f"coll = ax.{func}({data}, 0, 1)\n"
            f"self.assertEqual({expected!r}, len(coll.get_segments()))\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = random.randint(4, 7)
        vals = [str(v) for v in self._values(n)]
        k = random.randint(1, 2)
        for i in random.sample(range(n), k):
            vals[i] = "nan"
        test = self.get_empty_test()
        test.body = self._assert(self._func(), vals)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        n = random.randint(2, 7)
        vals = [str(v) for v in self._values(n)]
        test = self.get_empty_test()
        test.body = self._assert(self._func(), vals)
        return test, TestResult.PASSING


grammar_12: Grammar = clean_up(
    dict(
        {
            "<start>": ["<func> <data>"],
            "<func>": ["vlines", "hlines"],
            "<data>": ["<item>", "<item>,<data>"],
            "<item>": ["<float>", "nan"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_12)


# ======================================================================
# bug_6: ``Axes.scatter`` misclassified a single-row RGB(A) ``c`` (shape
# ``(1, 3)`` / ``(1, 4)``) as *mapped values* whenever its size happened to equal
# the number of points, instead of broadcasting it as one colour.  The fix
# special-cases the ``(1, 3)``/``(1, 4)`` shape as a single colour.
#
# System-test format:  ``<n> <color>`` where ``<n>`` is the number of points and
# ``<color>`` is a comma-separated RGB or RGBA colour.  The harness scatters with
# ``c=[color]`` and prints whether the collection has *no* mapped array (i.e. the
# colour was taken as a single colour).  The correct (fixed) answer is always
# ``True``; a colour whose component count equals ``n`` triggers the fault (buggy
# maps it through the colormap instead).
# ======================================================================


class Matplotlib6API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            int(process.args[2])
            comps = process.args[3].split(",")
            if len(comps) not in (3, 4):
                raise ValueError("bad color")
            for x in comps:
                float(x)
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "True"  # fixed always treats a single RGB(A) row as one colour
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib6TestGenerator:
    @staticmethod
    def _color(size: int) -> str:
        return ",".join(str(round(random.uniform(0.05, 0.95), 3)) for _ in range(size))

    def make_failing(self) -> str:
        size = random.choice([3, 4])
        # n equal to the colour's component count triggers the misclassification.
        return f"{size} {self._color(size)}"

    def make_passing(self) -> str:
        size = random.choice([3, 4])
        n = random.choice([x for x in range(2, 9) if x != size])
        return f"{n} {self._color(size)}"


class Matplotlib6SystemtestGenerator(
    SystemtestGenerator, Matplotlib6TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib6UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib6TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(n: int, comps: List[float]) -> List[ast.stmt]:
        src = (
            "fig, ax = plt.subplots()\n"
            f"coll = ax.scatter(np.ones({n}), range({n}), c=[{list(comps)!r}])\n"
            "self.assertEqual(True, coll.get_array() is None)\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        size = random.choice([3, 4])
        comps = [round(random.uniform(0.05, 0.95), 3) for _ in range(size)]
        test = self.get_empty_test()
        test.body = self._assert(size, comps)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        size = random.choice([3, 4])
        n = random.choice([x for x in range(2, 9) if x != size])
        comps = [round(random.uniform(0.05, 0.95), 3) for _ in range(size)]
        test = self.get_empty_test()
        test.body = self._assert(n, comps)
        return test, TestResult.PASSING


grammar_6: Grammar = clean_up(
    dict(
        {
            "<start>": ["<number> <color>"],
            "<color>": ["<c>,<c>,<c>", "<c>,<c>,<c>,<c>"],
            "<c>": ["<float>"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_6)


# ======================================================================
# bug_22: ``Axes.hist`` did not run the *bins* through unit conversion, so
# passing ``datetime`` bin edges raised ``TypeError`` (comparing float to
# datetime).  The fix converts non-scalar ``bins`` with ``convert_xunits``.
#
# System-test format:  ``<kind> <edges>`` where ``<kind>`` is ``datetime`` or
# ``numeric`` and ``<edges>`` is a comma-separated list of ``YYYY-MM-DD`` dates.
# The harness histograms a fixed datetime dataset with those edges (as raw
# datetimes or as ``date2num`` numbers) and prints the number of returned bins.
# The correct (fixed) count equals the number of edges; ``datetime`` bins trigger
# the fault (buggy raises -> no output).
# ======================================================================


class Matplotlib22API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            kind = process.args[2]
            edges = process.args[3].split(",")
            if kind not in ("datetime", "numeric") or len(edges) < 2:
                raise ValueError("bad args")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(len(edges))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib22TestGenerator:
    @staticmethod
    def _edges() -> List[str]:
        # 2-4 distinct sorted dates within 2019.
        import datetime as _dt

        n = random.randint(2, 4)
        days = sorted(random.sample(range(1, 360), n))
        base = _dt.date(2019, 1, 1)
        return [(base + _dt.timedelta(days=d)).strftime("%Y-%m-%d") for d in days]

    def make_failing(self) -> str:
        return f"datetime {','.join(self._edges())}"

    def make_passing(self) -> str:
        return f"numeric {','.join(self._edges())}"


class Matplotlib22SystemtestGenerator(
    SystemtestGenerator, Matplotlib22TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


_HIST_DATA = (
    "[[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), "
    "datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], "
    "[datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), "
    "datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]"
)


class Matplotlib22UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib22TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import datetime\n"
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib as mpl\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(kind: str, edges: List[str]) -> List[ast.stmt]:
        expected = len(edges)
        edge_exprs = ", ".join(
            f"datetime.datetime.strptime({e!r}, '%Y-%m-%d')" for e in edges
        )
        bins = (
            f"[{edge_exprs}]"
            if kind == "datetime"
            else f"mpl.dates.date2num([{edge_exprs}])"
        )
        src = (
            "fig, ax = plt.subplots()\n"
            f"data = {_HIST_DATA}\n"
            f"_, bins, _ = ax.hist(data, bins={bins}, stacked=True)\n"
            f"self.assertEqual({expected!r}, len(bins))\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("datetime", self._edges())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("numeric", self._edges())
        return test, TestResult.PASSING


grammar_22: Grammar = clean_up(
    {
        "<start>": ["<kind> <edges>"],
        "<kind>": ["datetime", "numeric"],
        "<edges>": [
            "<date>,<date>",
            "<date>,<date>,<date>",
            "<date>,<date>,<date>,<date>",
        ],
        "<date>": ["2019-<two>-<two>"],
        "<two>": ["<d><d>"],
        "<d>": [str(i) for i in range(10)],
    }
)

assert is_valid_grammar(grammar_22)


# ======================================================================
# bug_23: ``_AxesBase.apply_aspect`` with ``adjustable='datalim'`` on a
# *nonlinear* scale forwarded the data limits through ``trf.inverted().transform``
# instead of ``trf.transform``, so the aspect-driven limit adjustment silently did
# nothing.  The fix uses the forward transform.
#
# System-test format:  ``<mode> <xlo> <xhi>`` where ``<mode>`` is ``datalim`` or
# ``box`` and ``(xlo, xhi)`` is the log x-range.  The harness builds a square
# log-x / logit-y axes with ``aspect=1``, applies the aspect and prints whether
# the x-limits stayed unchanged.  With ``datalim`` the limits should change (the
# correct answer is ``False``); the buggy build leaves them unchanged.  ``box``
# never changes the data limits (answer ``True``).
# ======================================================================


class Matplotlib23API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            float(process.args[3])
            float(process.args[4])
            if mode not in ("datalim", "box"):
                raise ValueError("bad mode")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = str(mode == "box")  # box leaves data limits unchanged
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib23TestGenerator:
    @staticmethod
    def _xrange() -> Tuple[float, float]:
        # A *wide* range (>2 decades) so the aspect requires the limits to be
        # *shrunk*: that is the direction the buggy inverted-transform fails to
        # apply (a too-narrow range would be expanded even by the buggy code).
        xlo = round(random.uniform(0.5, 2.0), 3)
        xhi = round(xlo * random.uniform(150.0, 400.0), 3)
        return xlo, xhi

    def make_failing(self) -> str:
        xlo, xhi = self._xrange()
        return f"datalim {xlo} {xhi}"

    def make_passing(self) -> str:
        xlo, xhi = self._xrange()
        return f"box {xlo} {xhi}"


class Matplotlib23SystemtestGenerator(
    SystemtestGenerator, Matplotlib23TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib23UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib23TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(mode: str, xlo: float, xhi: float) -> List[ast.stmt]:
        expected = mode == "box"
        src = (
            "fig = plt.figure(figsize=(10, 10))\n"
            "ax = fig.add_axes([.1, .1, .8, .8])\n"
            "ax.plot([.4, .6], [.4, .6])\n"
            f"ax.set(xscale='log', xlim=({xlo}, {xhi}), yscale='logit', "
            f"ylim=(1 / 101, 1 / 11), aspect=1, adjustable={mode!r})\n"
            "ax.margins(0)\n"
            "ax.apply_aspect()\n"
            "cur = ax.get_xlim()\n"
            f"unchanged = abs(cur[0] - {xlo}) < 1e-06 and abs(cur[1] - {xhi}) < 1e-06\n"
            f"self.assertEqual({expected!r}, unchanged)\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        xlo, xhi = self._xrange()
        test = self.get_empty_test()
        test.body = self._assert("datalim", xlo, xhi)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        xlo, xhi = self._xrange()
        test = self.get_empty_test()
        test.body = self._assert("box", xlo, xhi)
        return test, TestResult.PASSING


grammar_23: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <float> <float>"],
            "<mode>": ["datalim", "box"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_23)


# ======================================================================
# bug_9: ``PolarAxes.draw`` did not call ``self._unstale_viewLim()`` before
# rendering, so setting the r-limits *indirectly* (e.g. via
# ``yaxis.set_inverted`` + ``set_rorigin``) left the view limits stale and the
# figure was drawn with the wrong radial transform.  The fix unstales the view
# limits at the top of ``draw``.
#
# Because the fault only shows up in the *rendered* transform (the reported
# limits are already correct), the harness renders the scene twice -- once with a
# plain ``draw`` and once after an explicit ``_unstale_viewLim()`` -- and reports
# whether the two Agg buffers are identical.  On the fixed build ``draw`` already
# unstales, so the explicit call is a no-op and the buffers match (``True``); on
# the buggy build the stale-limit scene renders differently (``False``).
#
# System-test format:  ``<scenario> <rorigin> <rmax>`` where ``<scenario>`` is
# ``stale`` (the inverted-ylim + rorigin fault) or ``normal`` (a plain polar
# plot whose limits are never stale).  ``stale`` triggers the fault.
# ======================================================================


class Matplotlib9API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            scenario = process.args[2]
            float(process.args[3])
            float(process.args[4])
            if scenario not in ("stale", "normal"):
                raise ValueError("bad scenario")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "True"  # a redundant pre-unstale must not change the render
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib9TestGenerator:
    def make_failing(self) -> str:
        rmax = round(random.uniform(1.5, 3.0), 3)
        rorigin = round(rmax + random.uniform(0.5, 3.0), 3)
        return f"stale {rorigin} {rmax}"

    def make_passing(self) -> str:
        rmax = round(random.uniform(2.0, 4.0), 3)
        rorigin = round(random.uniform(-3.0, -0.5), 3)
        return f"normal {rorigin} {rmax}"


class Matplotlib9SystemtestGenerator(
    SystemtestGenerator, Matplotlib9TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib9UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib9TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "import hashlib\n"
            "import warnings\n"
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "import matplotlib.pyplot as plt\n"
        ).body

    @staticmethod
    def _assert(scenario: str, rorigin: float, rmax: float) -> List[ast.stmt]:
        if scenario == "stale":
            build = (
                "ax.yaxis.set_inverted(True)\n"
                f"    ax.plot([0, 0], [0, {rmax}], c='none')\n"
                "    ax.margins(0)\n"
                f"    ax.set_rorigin({rorigin})\n"
            )
        else:
            build = (
                "theta = np.linspace(0, 2 * np.pi, 50)\n"
                f"    ax.plot(theta, np.ones(50) * {rmax} * 0.8)\n"
                f"    ax.set_rlim(0, {rmax})\n"
                f"    ax.set_rorigin({rorigin})\n"
            )
        src = (
            "def _render(unstale):\n"
            "    fig = plt.figure()\n"
            "    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)\n"
            f"    {build}"
            "    if unstale:\n"
            "        ax._unstale_viewLim()\n"
            "    fig.canvas.draw()\n"
            "    buf = np.asarray(fig.canvas.buffer_rgba()).copy()\n"
            "    plt.close(fig)\n"
            "    return hashlib.md5(buf.tobytes()).hexdigest()\n"
            "with warnings.catch_warnings():\n"
            "    warnings.simplefilter('ignore')\n"
            "    self.assertEqual(True, _render(False) == _render(True))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        rmax = round(random.uniform(1.5, 3.0), 3)
        rorigin = round(rmax + random.uniform(0.5, 3.0), 3)
        test = self.get_empty_test()
        test.body = self._assert("stale", rorigin, rmax)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        rmax = round(random.uniform(2.0, 4.0), 3)
        rorigin = round(random.uniform(-3.0, -0.5), 3)
        test = self.get_empty_test()
        test.body = self._assert("normal", rorigin, rmax)
        return test, TestResult.PASSING


grammar_9: Grammar = clean_up(
    dict(
        {
            "<start>": ["<scenario> <float> <float>"],
            "<scenario>": ["stale", "normal"],
        },
        **FLOAT,
    )
)

assert is_valid_grammar(grammar_9)


# ======================================================================
# bug_1: the tight-bbox save path patched the renderer's ``draw_*`` methods to
# no-ops *permanently* (via ``_get_renderer(draw_disabled=True)``) and then drew
# the figure with them, so a ``savefig(bbox_inches='tight')`` produced a blank
# (all-white, fully-transparent) image.  The fix restores the draw methods with a
# ``cbook._setattr_cm`` context manager so the real content is rendered.
#
# System-test format:  ``<mode> <x_size> <y_size> <dpi>`` where ``<mode>`` is
# ``tight`` (save with ``bbox_inches='tight'``) or ``normal`` (plain save).  The
# harness draws an ``imshow`` filling the axes and prints whether the saved image
# is fully opaque *and* not entirely white.  The correct (fixed) answer is always
# ``True``; ``tight`` triggers the fault (buggy saves a blank image).
# ======================================================================


class Matplotlib1API(MatplotlibAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            int(process.args[3])
            int(process.args[4])
            int(process.args[5])
            if mode not in ("tight", "normal"):
                raise ValueError("bad mode")
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "True"  # the content is always rendered on the fixed build
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Matplotlib1TestGenerator:
    # Whether ``savefig(bbox_inches='tight')`` renders a blank image on the buggy
    # build is sensitive to the tight-bbox pixel rounding, so the failing tests
    # use the test's own aspect (y=7, dpi=100) with x-sizes empirically verified
    # to reproduce the blank output on the buggy build (and which render
    # correctly on the fixed build).
    _BLANK_X = [
        8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 27, 28, 29, 30,
    ]

    @staticmethod
    def _pass_dims() -> Tuple[int, int, int]:
        return (
            random.randint(6, 30),
            random.randint(5, 20),
            random.choice([80, 100, 120, 150]),
        )

    def make_failing(self) -> str:
        return f"tight {random.choice(self._BLANK_X)} 7 100"

    def make_passing(self) -> str:
        x, y, dpi = self._pass_dims()
        return f"normal {x} {y} {dpi}"


class Matplotlib1SystemtestGenerator(
    SystemtestGenerator, Matplotlib1TestGenerator
):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Matplotlib1UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Matplotlib1TestGenerator
):
    def get_imports(self) -> List[ast.stmt]:
        return ast.parse(
            "from io import BytesIO\n"
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
            "import numpy as np\n"
            "import matplotlib.pyplot as plt\n"
            "from PIL import Image\n"
        ).body

    @staticmethod
    def _assert(mode: str, x_size: int, y_size: int, dpi: int) -> List[ast.stmt]:
        save = (
            "fig.savefig(out, bbox_inches='tight', pad_inches=0)"
            if mode == "tight"
            else "fig.savefig(out)"
        )
        src = (
            f"fig = plt.figure(frameon=False, dpi={dpi}, "
            f"figsize=({x_size} / {dpi}, {y_size} / {dpi}))\n"
            "ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])\n"
            "fig.add_axes(ax)\n"
            "ax.set_axis_off()\n"
            "ax.get_xaxis().set_visible(False)\n"
            "ax.get_yaxis().set_visible(False)\n"
            f"data = np.arange({x_size} * {y_size}).reshape({y_size}, {x_size})\n"
            "ax.imshow(data)\n"
            "out = BytesIO()\n"
            f"{save}\n"
            "out.seek(0)\n"
            "im = np.asarray(Image.open(out))\n"
            "ok = bool((im[:, :, 3] == 255).all() and not (im[:, :, :3] == 255).all())\n"
            "self.assertEqual(True, ok)\n"
            "plt.close(fig)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._assert("tight", random.choice(self._BLANK_X), 7, 100)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        x, y, dpi = self._pass_dims()
        test = self.get_empty_test()
        test.body = self._assert("normal", x, y, dpi)
        return test, TestResult.PASSING


grammar_1: Grammar = clean_up(
    dict(
        {
            "<start>": ["<mode> <number> <number> <number>"],
            "<mode>": ["tight", "normal"],
        },
        **NUMBER,
    )
)

assert is_valid_grammar(grammar_1)
