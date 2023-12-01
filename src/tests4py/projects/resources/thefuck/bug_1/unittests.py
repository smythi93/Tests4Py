import unittest
from thefuck.rules.pip_unknown_command import get_new_command
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('pip download cgi', get_new_command(
            Command('pip -dowNLoad cgi', 'ERROR: unknown command "-dowNLoad", maybe you meant "download"')))

    def test_diversity_2(self):
        self.assertEqual('pip uninstall warnings', get_new_command(
            Command('pip uninst4LLL warnings', 'ERROR: unknown command "uninst4LLL", maybe you meant "uninstall"')))

    def test_diversity_3(self):
        self.assertEqual('pip uninstall zipimport', get_new_command(
            Command('pip uninst4LLL zipimport', 'ERROR: unknown command "uninst4LLL", maybe you meant "uninstall"')))

    def test_diversity_4(self):
        self.assertEqual('pip check pathlib', get_new_command(
            Command('pip CHECK= pathlib', 'ERROR: unknown command "CHECK=", maybe you meant "check"')))
    def test_diversity_5(self):
        self.assertEqual('pip list ast', get_new_command(
            Command('pip l1st ast', 'ERROR: unknown command "l1st", maybe you meant "list"')))

    def test_diversity_6(self):
        self.assertEqual('pip search trace', get_new_command(
            Command('pip sEArch trace', 'ERROR: unknown command "sEArch", maybe you meant "search"')))

    def test_diversity_7(self):
        self.assertEqual('pip config pyexpat', get_new_command(
            Command('pip c0nf1g pyexpat', 'ERROR: unknown command "c0nf1g", maybe you meant "config"')))

    def test_diversity_8(self):
        self.assertEqual('pip debug pstats', get_new_command(
            Command('pip ~deBUG pstats', 'ERROR: unknown command "~deBUG", maybe you meant "debug"')))

    def test_diversity_9(self):
        self.assertEqual('pip list trace', get_new_command(
            Command('pip l1st trace', 'ERROR: unknown command "l1st", maybe you meant "list"')))

    def test_diversity_10(self):
        self.assertEqual('pip debug trace', get_new_command(
            Command('pip ~deBUG trace', 'ERROR: unknown command "~deBUG", maybe you meant "debug"')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('pip uninstall crypt', get_new_command(
            Command('pip unstal crypt', 'ERROR: unknown command "unstal", maybe you meant "uninstall"')))

    def test_diversity_2(self):
        self.assertEqual('pip show zipimport', get_new_command(
            Command('pip shw zipimport', 'ERROR: unknown command "shw", maybe you meant "show"')))

    def test_diversity_3(self):
        self.assertEqual('pip list calendar', get_new_command(
            Command('pip lst calendar', 'ERROR: unknown command "lst", maybe you meant "list"')))

    def test_diversity_4(self):
        self.assertEqual('pip search pyexpat', get_new_command(
            Command('pip serch pyexpat', 'ERROR: unknown command "serch", maybe you meant "search"')))

    def test_diversity_5(self):
        self.assertEqual('pip cache cgi', get_new_command(
            Command('pip cach cgi', 'ERROR: unknown command "cach", maybe you meant "cache"')))

    def test_diversity_6(self):
        self.assertEqual('pip show venv', get_new_command(
            Command('pip shw venv', 'ERROR: unknown command "shw", maybe you meant "show"')))

    def test_diversity_7(self):
        self.assertEqual('pip download cgi', get_new_command(
            Command('pip downld cgi', 'ERROR: unknown command "downld", maybe you meant "download"')))

    def test_diversity_8(self):
        self.assertEqual('pip config venv', get_new_command(
            Command('pip cnfig venv', 'ERROR: unknown command "cnfig", maybe you meant "config"')))

    def test_diversity_9(self):
        self.assertEqual('pip download calendar', get_new_command(
            Command('pip downld calendar', 'ERROR: unknown command "downld", maybe you meant "download"')))

    def test_diversity_10(self):
        self.assertEqual('pip download trace', get_new_command(
            Command('pip downld trace', 'ERROR: unknown command "downld", maybe you meant "download"')))
