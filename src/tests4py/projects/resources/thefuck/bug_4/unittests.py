import unittest
from thefuck.shell.fish import Fish
from thefuck.shells.fish import _get_aliases


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertDictEqual("", _get_aliases(f._get_overridden_aliases()))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertIn("", _get_aliases(f._get_overridden_aliases()))
