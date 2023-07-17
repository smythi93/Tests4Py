import json
import os

from fuzzingbook import Grammars

import tests4py.constants
import tests4py.framework.default
from tests4py import framework
from tests4py.projects import load_bug_info
from utils import BaseTest


class CommandTests(BaseTest):
    def test_checkout_pysnooper_1(self):
        report = tests4py.framework.default.tests4py_checkout("pysnooper", 1)
        if report.raised:
            raise report.raised
        self.assertTrue((tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_1").exists())
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_1"
                / tests4py.constants.INFO_FILE
            ).exists()
        )
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_1"
                / tests4py.constants.REQUIREMENTS_FILE
            ).exists()
        )

    def test_checkout_pysnooper_2(self):
        report = tests4py.framework.default.tests4py_checkout("pysnooper", 2)
        if report.raised:
            raise report.raised
        self.assertTrue((tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_2").exists())
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / tests4py.constants.INFO_FILE
            ).exists()
        )
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / tests4py.constants.REQUIREMENTS_FILE
            ).exists()
        )
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / tests4py.constants.DEFAULT_UNITTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / tests4py.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertEqual(
            20,
            len(
                os.listdir(
                    tests4py.constants.DEFAULT_WORK_DIR
                    / "pysnooper_2"
                    / tests4py.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
                )
            ),
        )

    def test_checkout_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout("pysnooper", 3)
        if report.raised:
            raise report.raised
        self.assertTrue((tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3").exists())
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / tests4py.constants.INFO_FILE
            ).exists()
        )
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / tests4py.constants.REQUIREMENTS_FILE
            ).exists()
        )
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / tests4py.constants.DEFAULT_UNITTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertTrue(
            (
                tests4py.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / tests4py.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertEqual(
            20,
            len(
                os.listdir(
                    tests4py.constants.DEFAULT_WORK_DIR
                    / "pysnooper_3"
                    / tests4py.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
                )
            ),
        )

    def test_compile_pysnooper_1(self):
        report = tests4py.framework.default.tests4py_checkout("pysnooper", 1)
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_1"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)

    def test_test_pysnooper_3(self):
        tests4py.framework.default.tests4py_checkout("pysnooper", 3, fixed=False)
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        tests4py.framework.default.tests4py_compile(work_dir)
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = tests4py.framework.default.tests4py_test(work_dir)
        if report.raised:
            raise report.raised
        self.assertEqual(1, report.total)
        self.assertEqual(1, report.failing)
        self.assertEqual(0, report.passing)

    def test_unittest_test_buggy_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=False
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(10, report.failing)
        self.assertEqual(10, report.passing)

    def test_unittest_test_fixed_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=True
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(20, report.passing)

    def test_systemtest_test_buggy_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=False
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(10, report.failing)
        self.assertEqual(10, report.passing)

    def test_systemtest_test_fixed_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=True
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(20, report.passing)

    def test_unittest_generate_buggy_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=False
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_generate(work_dir, n=6, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue(
            (work_dir / tests4py.constants.DEFAULT_SUB_PATH_UNITTESTS).exists()
        )
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)
        report = framework.unittest.tests4py_test(
            work_dir,
            path=work_dir / tests4py.constants.DEFAULT_SUB_PATH_UNITTESTS,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)

    def test_unittest_generate_fixed_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=True
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_generate(work_dir, n=6, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue(
            (work_dir / tests4py.constants.DEFAULT_SUB_PATH_UNITTESTS).exists()
        )
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)
        report = framework.unittest.tests4py_test(
            work_dir,
            path=work_dir / tests4py.constants.DEFAULT_SUB_PATH_UNITTESTS,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(6, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(6, report.passing)

    def test_systemtest_generate_buggy_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=False
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_generate(work_dir, n=6, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue(
            (work_dir / tests4py.constants.DEFAULT_SUB_PATH_SYSTEMTESTS).exists()
        )
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)
        report = framework.systemtest.tests4py_test(
            work_dir,
            path=work_dir / tests4py.constants.DEFAULT_SUB_PATH_SYSTEMTESTS,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)

    def test_systemtest_generate_fixed_pysnooper_3(self):
        report = tests4py.framework.default.tests4py_checkout(
            "pysnooper", 3, fixed=True
        )
        if report.raised:
            raise report.raised
        work_dir = tests4py.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = tests4py.framework.default.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / tests4py.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_generate(work_dir, n=6, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue(
            (work_dir / tests4py.constants.DEFAULT_SUB_PATH_SYSTEMTESTS).exists()
        )
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)
        report = framework.systemtest.tests4py_test(
            work_dir,
            path=work_dir / tests4py.constants.DEFAULT_SUB_PATH_SYSTEMTESTS,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(6, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(6, report.passing)

    def test_grammar_python(self):
        file = "grammar.py"
        tests4py.framework.grammar.tests4py_grammar(
            "pysnooper", 2, grammar_format="python", output=file
        )
        with open(file, "r") as fp:
            exec(fp.read())
        self.assertTrue(Grammars.is_valid_grammar(locals()["grammar"]))
        if os.path.exists(file):
            os.remove(file)

    def test_grammar_json(self):
        file = "grammar.json"
        tests4py.framework.grammar.tests4py_grammar(
            "pysnooper", 2, grammar_format="json", output=file
        )
        with open(file, "r") as fp:
            grammar = json.load(fp)
        self.assertTrue(Grammars.is_valid_grammar(grammar))
        if os.path.exists(file):
            os.remove(file)

    def test_grammar_antlr(self):
        file = "grammar.g4"
        # target = "test_antlr"
        tests4py.framework.grammar.tests4py_grammar(
            "pysnooper", 2, grammar_format="antlr", output=file
        )
        self.assertTrue(os.path.exists(file))
        if os.path.exists(file):
            os.remove(file)
