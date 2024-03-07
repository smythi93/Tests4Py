import os.path
from pathlib import Path

from sflkit.analysis.analysis_type import AnalysisType
from sflkit.analysis.spectra import Spectrum
from sflkit.analysis.suggestion import Location

from tests4py.cli import framework
from tests4py.constants import DEFAULT_WORK_DIR
from utils import BaseTest


class TestSFL(BaseTest):
    def test_middle(self):
        project_name = "middle"
        bug_id = 2
        report = framework.default.tests4py_checkout(project_name, bug_id)
        if report.raised:
            raise report.raised
        src = Path(report.location)
        dst = DEFAULT_WORK_DIR / "sfl"
        report = framework.sfl.tests4py_sfl_instrument(src, dst)
        if report.raised:
            raise report.raised

        dst_src = dst / "src"
        dst_src_middle = dst_src / "middle"
        dst_src_middle___init___py = dst_src_middle / "__init__.py"
        dst_tests = dst / "tests"
        dst_tests_test_middle_py = dst_tests / "test_middle.py"
        dst_gitignore = dst / ".gitignore"
        dst_license = dst / "LICENSE"
        dst_readme_md = dst / "README.md"
        dst_setup_cfg = dst / "setup.cfg"
        dst_setup_py = dst / "setup.py"

        src_src = src / "src"
        src_src_middle = src_src / "middle"
        src_src_middle___init___py = src_src_middle / "__init__.py"
        src_tests = src / "tests"
        src_tests_test_middle_py = src_tests / "test_middle.py"
        src_gitignore = src / ".gitignore"
        src_license = src / "LICENSE"
        src_readme_md = src / "README.md"
        src_setup_cfg = src / "setup.cfg"
        src_setup_py = src / "setup.py"

        exist_files = [
            dst_src_middle___init___py,
            dst_tests_test_middle_py,
            dst_gitignore,
            dst_license,
            dst_readme_md,
            dst_setup_cfg,
            dst_setup_py,
        ]
        exist_dirs = [dst_src, dst_src_middle, dst_tests]

        for d in exist_dirs:
            self.assertTrue(d.exists())
            self.assertTrue(d.is_dir())

        for f in exist_files:
            self.assertTrue(f.exists())
            self.assertTrue(f.is_file())

        for d, s in [
            (dst_tests_test_middle_py, src_tests_test_middle_py),
            (dst_gitignore, src_gitignore),
            (dst_license, src_license),
            (dst_readme_md, src_readme_md),
            (dst_setup_cfg, src_setup_cfg),
            (dst_setup_py, src_setup_py),
        ]:
            with open(d, "r") as fp:
                d_content = fp.read()
            with open(s, "r") as fp:
                s_content = fp.read()
            self.assertEqual(s_content, d_content, f"{d} has other content then {s}")

        for d, s in [
            (dst_src_middle___init___py, src_src_middle___init___py),
        ]:
            with open(d, "r") as fp:
                d_content = fp.read()
            with open(s, "r") as fp:
                s_content = fp.read()
            self.assertNotEqual(
                s_content, d_content, f"{d} has the same content then {s}"
            )

        report = framework.sfl.tests4py_sfl_events(dst)
        if report.raised:
            raise report.raised

        report = framework.sfl.tests4py_sfl_analyze(dst, src, predicates="line")
        if report.raised:
            raise report.raised

        suggestions = report.analyzer.get_sorted_suggestions(
            base_dir=src,
            type_=AnalysisType.LINE,
            metric=Spectrum.Ochiai,
        )
        self.assertAlmostEqual(
            0.7071067811865475, suggestions[0].suspiciousness, delta=0.0000001
        )
        self.assertEqual(1, len(suggestions[0].lines))
        self.assertIn(
            Location(os.path.join("src", "middle", "__init__.py"), 6),
            suggestions[0].lines,
        )
