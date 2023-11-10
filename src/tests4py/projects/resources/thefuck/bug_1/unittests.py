import unittest
import re
from thefuck.rules.pip_unknown_command import get_new_command
from thefuck.utils import replace_argument, for_app
from thefuck.specific.sudo import sudo_support


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual("pip install", get_new_command("pipip instal"))

    def test_diversity_2(self):
        self.assertEqual("pip search aircrack", get_new_command("PIP SEARCH AIRCRACK"))

    def test_diversity_3(self):
        self.assertEqual("pip install hashcat", get_new_command("pip install hash-cat"))

    def test_diversity_4(self):
        self.assertEqual("pip install hashcat", get_new_command("pip install h@shc@t"))

    def test_diversity_5(self):
        self.assertEqual("pip install wireshark", get_new_command("pip instal wire--shark"))

    def test_diversity_6(self):
        self.assertEqual("pip uninstall medusa", get_new_command("pip un install medusa"))

    def test_diversity_7(self):
        self.assertEqual("pip show hydra", get_new_command("pip_show hydra"))

    def test_diversity_8(self):
        self.assertEqual("pip search john", get_new_command("PIP SERCH john"))

    def test_diversity_9(self):
        self.assertEqual("pip install brutus", get_new_command("peep install brutus"))

    def test_diversity_10(self):
        self.assertEqual("pip download medusa", get_new_command("pip download m3dus4"))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual("pip search python", get_new_command("pip src python"))

    def test_diversity_2(self):
        self.assertEqual(('ERROR: unknown command "instl", maybe you meant "install"', "pip instl python"), get_new_command("pip install python"))

    def test_diversity_3(self):
        self.assertEqual("ERROR: unknown command", get_new_command("pip cnfg"))

    def test_diversity_4(self):
        self.assertEqual("pip list", get_new_command("pip lst"))

    def test_diversity_5(self):
        self.assertEqual("pip install", get_new_command("pip instl"))

    def test_diversity_6(self):
        self.assertEqual("pip uninstall", get_new_command("pip unstal"))

    def test_diversity_7(self):
        self.assertEqual("pip show", get_new_command("pip shw"))

    def test_diversity_8(self):
        self.assertEqual("pip wheel", get_new_command("pip whel"))

    def test_diversity_9(self):
        self.assertEqual("pip inspect", get_new_command("pip spct"))

    def test_diversity_10(self):
        self.assertEqual("pip cache", get_new_command("pip cac"))


'''

class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual("pip src, ERROR: unknown command src, maybe you meant search", get_new_command("pip src"))

    def test_diversity_2(self):
        self.assertEqual("pip dwnld, ERROR: unknown command dwnld, maybe you meant download", get_new_command("pip dwnld"))

    def test_diversity_3(self):
        self.assertEqual("pip cnfg, ERROR: unknown command cnfg, maybe you meant config", get_new_command("pip cnfg"))

    def test_diversity_4(self):
        self.assertEqual("pip lst, ERROR: unknown command lst, maybe you meant list", get_new_command("pip lst"))

    def test_diversity_5(self):
        self.assertEqual("pip instl, ERROR: unknown command instl, maybe you meant install", get_new_command("pip instl"))

    def test_diversity_6(self):
        self.assertEqual("pip unstal, ERROR: unknown command unstal, maybe you meant uninstall", get_new_command("pip unstal"))

    def test_diversity_7(self):
        self.assertEqual("pip shw, ERROR: unknown command shw, maybe you meant show", get_new_command("pip shw"))

    def test_diversity_8(self):
        self.assertEqual("pip whel, ERROR: unknown command whel, maybe you meant wheel", get_new_command("pip whel"))

    def test_diversity_9(self):
        self.assertEqual("pip spct, ERROR: unknown command spct, maybe you meant inspect", get_new_command("pip spct"))

    def test_diversity_10(self):
        self.assertEqual("pip cac, ERROR: unknown command cac, maybe you meant cache", get_new_command("pip cac"))

'''
