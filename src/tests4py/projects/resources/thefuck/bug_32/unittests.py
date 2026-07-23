import unittest
from thefuck.rules.ls_lah import match
from thefuck.types import Command
from thefuck.types import Settings


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(Command('als ubogcrkgs', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('mls dnjzyez', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('pls ujzzyzu', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('bls lkwtcozzi', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('xls zgxthrzgwi', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('pls hmbxmqhj', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('zls gihzekpvb', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('xls dmohflhdh', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('kls hixjuk', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('zls yyyes', '', ''), Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('ls wymqjmv', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('ls jfahvdoiq', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('ls iheiuhjg', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('ls jchxxvmt', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('ls agsspmwbtp', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('ls biuowvw', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('ls etubqcsexf', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('ls zynnitmggx', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('ls xeptudhdh', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('ls yftbvuydd', '', ''), Settings()))
