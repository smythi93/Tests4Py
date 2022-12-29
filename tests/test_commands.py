import os.path
import unittest

from BugsTest import framework
from BugsTest.projects import load_bug_info


class CheckOutTests(unittest.TestCase):

    def test_checkout_pysnooper_1(self):
        framework.bugstest_checkout('pysnooper', 1)
        self.assertTrue(os.path.exists(os.path.join(framework.DEFAULT_WORK_DIR, 'pysnooper_1')))
        self.assertTrue(os.path.exists(os.path.join(framework.DEFAULT_WORK_DIR, 'pysnooper_1', 'bugstest_info.ini')))
        self.assertTrue(
            os.path.exists(os.path.join(framework.DEFAULT_WORK_DIR, 'pysnooper_1', 'bugstest_requirements.txt')))

    def test_compile_pysnooper_1(self):
        framework.bugstest_checkout('pysnooper', 1)
        work_dir = framework.DEFAULT_WORK_DIR / 'pysnooper_1'
        project = load_bug_info(work_dir / 'bugstest_info.ini')
        self.assertFalse(project.compiled)
        framework.bugstest_compile(work_dir)
        project = load_bug_info(work_dir / 'bugstest_info.ini')
        self.assertTrue(project.compiled)
