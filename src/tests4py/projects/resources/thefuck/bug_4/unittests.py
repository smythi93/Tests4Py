import unittest
from thefuck.shell.fish import Fish
from thefuck.shells.fish import _get_functions, _get_aliases


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_2(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_3(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_4(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_5(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_6(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_7(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_8(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_9(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_10(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_2(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_3(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_4(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_5(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_6(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_7(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_8(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_9(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))

    def test_diversity_10(self):
        f = Fish()
        self.assertIn("", _get_functions(f._get_overridden_aliases()))
