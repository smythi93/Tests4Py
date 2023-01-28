import os
import unittest

import Tests4Py.framework.constants
from Tests4Py import framework
from Tests4Py.projects import load_bug_info


class CheckOutTests(unittest.TestCase):
    def test_checkout_pysnooper_1(self):
        report = framework.tests4py_checkout("pysnooper", 1)
        if report.raised:
            raise report.raised
        self.assertTrue(
            (Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_1").exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_1"
                / Tests4Py.framework.constants.INFO_FILE
            ).exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_1"
                / Tests4Py.framework.constants.REQUIREMENTS_FILE
            ).exists()
        )

    def test_checkout_pysnooper_2(self):
        report = framework.tests4py_checkout("pysnooper", 2)
        if report.raised:
            raise report.raised
        self.assertTrue(
            (Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_2").exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / Tests4Py.framework.constants.INFO_FILE
            ).exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / Tests4Py.framework.constants.REQUIREMENTS_FILE
            ).exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / Tests4Py.framework.constants.DEFAULT_UNITTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_2"
                / Tests4Py.framework.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertEqual(
            20,
            len(
                os.listdir(
                    Tests4Py.framework.constants.DEFAULT_WORK_DIR
                    / "pysnooper_2"
                    / Tests4Py.framework.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
                )
            ),
        )

    def test_checkout_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3)
        if report.raised:
            raise report.raised
        self.assertTrue(
            (Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3").exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / Tests4Py.framework.constants.INFO_FILE
            ).exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / Tests4Py.framework.constants.REQUIREMENTS_FILE
            ).exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / Tests4Py.framework.constants.DEFAULT_UNITTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertTrue(
            (
                Tests4Py.framework.constants.DEFAULT_WORK_DIR
                / "pysnooper_3"
                / Tests4Py.framework.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
            ).exists()
        )
        self.assertEqual(
            20,
            len(
                os.listdir(
                    Tests4Py.framework.constants.DEFAULT_WORK_DIR
                    / "pysnooper_3"
                    / Tests4Py.framework.constants.DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
                )
            ),
        )

    def test_compile_pysnooper_1(self):
        report = framework.tests4py_checkout("pysnooper", 1)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_1"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)

    def test_test_pysnooper_3(self):
        framework.tests4py_checkout("pysnooper", 3, version_id=0)
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        framework.tests4py_compile(work_dir)
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.tests4py_test(work_dir)
        if report.raised:
            raise report.raised
        self.assertEqual(1, report.total)
        self.assertEqual(1, report.failing)
        self.assertEqual(0, report.passing)

    def test_unittest_test_buggy_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=0)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(10, report.failing)
        self.assertEqual(10, report.passing)

    def test_unittest_test_fixed_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=1)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(20, report.passing)

    def test_systemtest_test_buggy_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=0)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(10, report.failing)
        self.assertEqual(10, report.passing)

    def test_systemtest_test_fixed_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=1)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(20, report.passing)

    def test_unittest_generate_buggy_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=0)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_generate(work_dir, n=10, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue((work_dir / framework.unittest.DEFAULT_SUB_PATH).exists())
        self.assertEqual(10, report.total)
        self.assertEqual(5, report.failing)
        self.assertEqual(5, report.passing)
        report = framework.unittest.tests4py_test(
            work_dir,
            path=work_dir / framework.unittest.DEFAULT_SUB_PATH,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(10, report.total)
        self.assertEqual(5, report.failing)
        self.assertEqual(5, report.passing)

    def test_unittest_generate_fixed_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=1)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.unittest.tests4py_generate(work_dir, n=10, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue((work_dir / framework.unittest.DEFAULT_SUB_PATH).exists())
        self.assertEqual(10, report.total)
        self.assertEqual(5, report.failing)
        self.assertEqual(5, report.passing)
        report = framework.unittest.tests4py_test(
            work_dir,
            path=work_dir / framework.unittest.DEFAULT_SUB_PATH,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(10, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(10, report.passing)

    def test_systemtest_generate_buggy_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=0)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_generate(work_dir, n=10, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue((work_dir / framework.systemtest.DEFAULT_SUB_PATH).exists())
        self.assertEqual(10, report.total)
        self.assertEqual(5, report.failing)
        self.assertEqual(5, report.passing)
        report = framework.systemtest.tests4py_test(
            work_dir,
            path=work_dir / framework.systemtest.DEFAULT_SUB_PATH,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(10, report.total)
        self.assertEqual(5, report.failing)
        self.assertEqual(5, report.passing)

    def test_systemtest_generate_fixed_pysnooper_3(self):
        report = framework.tests4py_checkout("pysnooper", 3, version_id=1)
        if report.raised:
            raise report.raised
        work_dir = Tests4Py.framework.constants.DEFAULT_WORK_DIR / "pysnooper_3"
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / Tests4Py.framework.constants.INFO_FILE)
        self.assertTrue(project.compiled)
        report = framework.systemtest.tests4py_generate(work_dir, n=10, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue((work_dir / framework.systemtest.DEFAULT_SUB_PATH).exists())
        self.assertEqual(10, report.total)
        self.assertEqual(5, report.failing)
        self.assertEqual(5, report.passing)
        report = framework.systemtest.tests4py_test(
            work_dir,
            path=work_dir / framework.systemtest.DEFAULT_SUB_PATH,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(10, report.total)
        self.assertEqual(0, report.failing)
        self.assertEqual(10, report.passing)
