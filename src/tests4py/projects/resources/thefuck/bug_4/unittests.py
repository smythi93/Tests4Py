import unittest
from thefuck.shell.fish import Fish
from thefuck.shells.fish import _get_aliases


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_2(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_3(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_4(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_5(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_6(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_7(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_8(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_9(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_10(self):
        f = Fish()
        self.assertIn("Error Retrieving Fish Shell Overridden", _get_aliases(f._get_overridden_aliases()))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertIn("cd", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_2(self):
        f = Fish()
        self.assertIn("greet", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_3(self):
        f = Fish()
        self.assertIn("gs", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_4(self):
        f = Fish()
        self.assertIn("dc", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_5(self):
        f = Fish()
        self.assertIn("gc", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_6(self):
        f = Fish()
        self.assertIn("dl", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_7(self):
        f = Fish()
        self.assertIn("dt", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_8(self):
        f = Fish()
        self.assertIn("gp", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_9(self):
        f = Fish()
        self.assertIn("rmi", _get_aliases(f._get_overridden_aliases()))

    def test_diversity_10(self):
        f = Fish()
        self.assertIn("dps", _get_aliases(f._get_overridden_aliases()))
