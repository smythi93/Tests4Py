import unittest
from thefuck.shell.fish import Fish
from thefuck.shells.fish import _get_functions, _get_aliases


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_2(self):
        self.assertEqual("", _get_aliases())

    def test_diversity_3(self):
        self.assertEqual("", _get_functions())

    def test_diversity_4(self):
        f = Fish()
        self.assertEqual("", f.get_aliases)

    def test_diversity_5(self):
        self.assertEqual("", "")

    def test_diversity_6(self):
        self.assertEqual("", "")

    def test_diversity_7(self):
        self.assertEqual("", "")

    def test_diversity_8(self):
        self.assertEqual("", "")

    def test_diversity_9(self):
        self.assertEqual("", "")

    def test_diversity_10(self):
        self.assertEqual("", "")


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertEqual("", f._get_overridden_aliases(_get_aliases))

    def test_diversity_2(self):
        f = Fish()
        self.assertEqual("", f._get_overridden_aliases(_get_aliases))

    def test_diversity_3(self):
        self.assertEqual("", "")

    def test_diversity_4(self):
        self.assertEqual("", "")

    def test_diversity_5(self):
        self.assertEqual("", "")

    def test_diversity_6(self):
        self.assertEqual("", "")

    def test_diversity_7(self):
        self.assertEqual("", "")

    def test_diversity_8(self):
        self.assertEqual("", "")

    def test_diversity_9(self):
        self.assertEqual("", "")

    def test_diversity_10(self):
        self.assertEqual("", "")