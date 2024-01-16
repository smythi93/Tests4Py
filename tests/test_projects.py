import unittest

from parameterized import parameterized

import tests4py.api.utils
from tests4py import projects
from tests4py.cli import framework
from tests4py.constants import (
    DEFAULT_WORK_DIR,
    INFO_FILE,
    DEFAULT_SUB_PATH_SYSTEMTESTS,
    DEFAULT_SUB_PATH_UNITTESTS,
)
from tests4py.projects import Project, load_bug_info
from utils import BaseTest


def _get_projects():
    tests4py.api.utils.setup()
    return [
        project
        for project_name in projects.bugs.values()
        for project in project_name.values()
    ]


class BaseProjectTests(BaseTest):
    PROJECTS = _get_projects()


class TestGenerationTests(BaseProjectTests):
    def setUp(self):
        self.skipTest("Project tests seems to be off on github workflow")
        # pass

    def _assert_test_generation(self, name: str, project: Project, systemtest=True):
        report = framework.default.tests4py_checkout(
            project.project_name, project.bug_id, fixed=False
        )
        if report.raised:
            raise report.raised
        work_dir = DEFAULT_WORK_DIR / name
        project_ = load_bug_info(work_dir / INFO_FILE)
        self.assertFalse(project_.compiled)
        report = framework.default.tests4py_build(work_dir)
        if report.raised:
            raise report.raised
        project_ = load_bug_info(work_dir / INFO_FILE)
        self.assertTrue(project_.compiled)
        if systemtest:
            report = framework.systemtest.tests4py_generate(
                work_dir, n=2, p=0.5, verify=True
            )
        else:
            report = framework.unittest.tests4py_generate(
                work_dir, n=2, p=0.5, verify=True
            )
        if report.raised:
            raise report.raised
        self.assertTrue(
            (
                work_dir
                / (
                    DEFAULT_SUB_PATH_SYSTEMTESTS
                    if systemtest
                    else DEFAULT_SUB_PATH_UNITTESTS
                )
            ).exists()
        )
        self.assertEqual(2, report.total)
        self.assertEqual(1, report.failing)
        self.assertEqual(1, report.passing)
        self.assertEqual(1, report.verify_failing)
        self.assertEqual(1, report.verify_passing)

    @unittest.skip
    @parameterized.expand(
        map(
            lambda p: (f"{p.project_name}_{p.bug_id}", p),
            filter(lambda p: p.systemtests is not None, BaseProjectTests.PROJECTS),
        )
    )
    def test_systemtest_generation(self, name: str, project: Project):
        self._assert_test_generation(name, project, systemtest=True)

    @unittest.skip
    @parameterized.expand(
        map(
            lambda p: (f"{p.project_name}_{p.bug_id}", p),
            filter(lambda p: p.unittests is not None, BaseProjectTests.PROJECTS),
        )
    )
    def test_unittest_generation(self, name: str, project: Project):
        self._assert_test_generation(name, project, systemtest=False)
