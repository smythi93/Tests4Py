import unittest

from parameterized import parameterized

import tests4py
from tests4py import projects
from tests4py.framework import utils
from tests4py.framework.constants import DEFAULT_WORK_DIR, INFO_FILE
from tests4py.framework.default import (
    tests4py_checkout,
    tests4py_compile,
)
from tests4py.projects import Project, load_bug_info


def _get_projects():
    utils.__setup__()
    return [
        project
        for project_name in projects.bugs.values()
        for project in project_name.values()
    ]


class BaseProjectTests:
    PROJECTS = _get_projects()


class TestGenerationTests(unittest.TestCase):
    def _assert_test_generation(self, name: str, project: Project, systemtest=True):
        report = tests4py_checkout(project.project_name, project.bug_id, version_id=0)
        if report.raised:
            raise report.raised
        work_dir = DEFAULT_WORK_DIR / name
        project_ = load_bug_info(work_dir / INFO_FILE)
        self.assertFalse(project_.compiled)
        report = tests4py_compile(work_dir)
        if report.raised:
            raise report.raised
        project_ = load_bug_info(work_dir / INFO_FILE)
        self.assertTrue(project_.compiled)
        if systemtest:
            report = tests4py.framework.systemtest.tests4py_generate(
                work_dir, n=2, p=0.5, verify=True
            )
        else:
            report = tests4py.framework.unittest.tests4py_generate(
                work_dir, n=2, p=0.5, verify=True
            )
        if report.raised:
            raise report.raised
        self.assertTrue(
            (
                work_dir / tests4py.framework.constants.DEFAULT_SUB_PATH_UNITTESTS
            ).exists()
        )
        self.assertEqual(2, report.total)
        self.assertEqual(1, report.failing)
        self.assertEqual(1, report.passing)
        self.assertEqual(1, report.verify_failing)
        self.assertEqual(1, report.verify_passing)

    @parameterized.expand(
        map(
            lambda p: (f"{p.project_name}_{p.bug_id}", p),
            filter(lambda p: p.systemtests is not None, BaseProjectTests.PROJECTS),
        )
    )
    def test_systemtest_generation(self, name: str, project: Project):
        self._assert_test_generation(name, project, systemtest=True)

    @parameterized.expand(
        map(
            lambda p: (f"{p.project_name}_{p.bug_id}", p),
            filter(lambda p: p.unittests is not None, BaseProjectTests.PROJECTS),
        )
    )
    def test_systemtest_generation(self, name: str, project: Project):
        self._assert_test_generation(name, project, systemtest=False)
