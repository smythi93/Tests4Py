import os.path

from sflkit.analysis.suggestion import Location

import tests4py.api as t4p
from tests4py.constants import DEFAULT_WORK_DIR
from tests4py.projects import Project
from tests4py.tests.utils import TestResult
from utils import BaseTest


class CommandTests(BaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        t4p.setup()

    def test_faulty_lines_3(self):
        faulty_lines = t4p.get_faulty_lines(t4p.get_projects("pysnooper", 3)[0])
        expected_lines = [
            Location(file=os.path.join("pysnooper", "pysnooper.py"), line=26)
        ]
        for line in expected_lines:
            self.assertIn(
                line,
                faulty_lines,
                f"Expected line {line} not in faulty lines {faulty_lines}.",
            )
        for line in faulty_lines:
            self.assertIn(
                line,
                expected_lines,
                f"Faulty line {line} not in expected lines {expected_lines}.",
            )

    def test_faulty_lines_2(self):
        faulty_lines = t4p.get_faulty_lines(t4p.get_projects("pysnooper", 2)[0])
        expected_lines = [
            Location(file=os.path.join("pysnooper", "tracer.py"), line=7),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=16),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=22),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=26),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=87),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=133),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=139),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=179),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=189),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=207),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=210),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=245),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=250),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=255),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=310),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=383),
        ]
        for line in expected_lines:
            self.assertIn(
                line,
                faulty_lines,
                f"Expected line {line} not in faulty lines {faulty_lines}.",
            )
        for line in faulty_lines:
            self.assertIn(
                line,
                expected_lines,
                f"Faulty line {line} not in expected lines {expected_lines}.",
            )

    def test_faulty_lines_1(self):
        faulty_lines = t4p.get_faulty_lines(t4p.get_projects("pysnooper", 1)[0])
        expected_lines = [
            Location(file=os.path.join("pysnooper", "pycompat.py"), line=10),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=16),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=87),
            Location(file=os.path.join("pysnooper", "tracer.py"), line=133),
        ]
        for line in expected_lines:
            self.assertIn(
                line,
                faulty_lines,
                f"Expected line {line} not in faulty lines {faulty_lines}.",
            )
        for line in faulty_lines:
            self.assertIn(
                line,
                expected_lines,
                f"Faulty line {line} not in expected lines {expected_lines}.",
            )

    def test_get_system_tests(self):
        project: Project = t4p.middle_1
        report = t4p.get_tests(project)
        self.assertEqual(10, len(report.passing_tests))
        self.assertEqual(10, len(report.failing_tests))
        work_dir = DEFAULT_WORK_DIR / project.get_identifier()
        r = t4p.checkout(project, DEFAULT_WORK_DIR)
        if r.raised:
            raise r.raised
        r = t4p.build(work_dir)
        if r.raised:
            raise r.raised
        for tests, expected in (
            (report.passing_tests, TestResult.PASSING),
            (report.failing_tests, TestResult.FAILING),
        ):
            for test in tests:
                r = t4p.run(work_dir, test, invoke_oracle=True)
                self.assertTrue(r.successful)
                self.assertEqual(expected, r.test_result)
