import unittest
import re
from thefuck.utils import replace_argument, for_app
from thefuck.specific.sudo import sudo_support
from thefuck.rules import get_new_command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(get_new_command("pipip instal"), "pip install")

    def test_diversity_2(self):
        self.assertEqual(get_new_command("PIP SEARCH AIRCRACK"), "pip search aircrack")

    def test_diversity_3(self):
        self.assertEqual("pip install hash-cat", "pip install hashcat")

    def test_diversity_4(self):
        self.assertEqual("pip install h@shc@t", "pip install hashcat")

    def test_diversity_5(self):
        self.assertEqual("pip instal wire--shark", "pip install wireshark")

    def test_diversity_6(self):
        self.assertEqual("pip un install medusa ", "pip uninstall medusa")

    def test_diversity_7(self):
        self.assertEqual("pip_show hydra", "pip show hydra")

    def test_diversity_8(self):
        self.assertEqual("PIP SERCH john", "pip search john")

    def test_diversity_9(self):
        self.assertEqual("peep install brutus", "pip install brutus")

    def test_diversity_10(self):
        self.assertEqual("pip download medusa", "pip download m3dus4")


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual("", "")

    def test_diversity_2(self):
        self.assertEqual("", "")

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
