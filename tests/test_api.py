import os.path

from sflkit.analysis.suggestion import Location

from tests4py.api import get_faulty_lines, get_projects
from tests4py.framework.utils import __setup__
from utils import BaseTest


class CommandTests(BaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        __setup__()

    def test_faulty_lines(self):
        faulty_lines = get_faulty_lines(get_projects("pysnooper", 3)[0])
        expected_lines = [
            Location(file=os.path.join("pysnooper", "pysnooper.py"), line=line)
            for line in range(23, 30)
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
                faulty_lines,
                f"Faulty line {line} not in expected lines {expected_lines}.",
            )
