import unittest
from thefuck.rules.no_command import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(Command('git ubogcrkgs', '', 'git: not found')))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('ls dnjzyez', '', 'ls: not found')))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('cat ujzzyzu', '', 'cat: not found')))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('echo lkwtcozzi', '', 'echo: not found')))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('cp zgxthrzgwi', '', 'cp: not found')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('mv hmbxmqhj', '', 'mv: not found')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('rm gihzekpvb', '', 'rm: not found')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('date dmohflhdh', '', 'date: not found')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('grep hixjuk', '', 'grep: not found')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('sort yyyes', '', 'sort: not found')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('gitt xeptudhdh', '', 'gitt: not found')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('lss yftbvuydd', '', 'lss: not found')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('catt vrvzfbe', '', 'catt: not found')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('echoo gpsfujk', '', 'echoo: not found')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('rmm gjundkdo', '', 'rmm: not found')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('datee dkkbw', '', 'datee: not found')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('grepp vzynonqnv', '', 'grepp: not found')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('sortt nbgosppu', '', 'sortt: not found')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('headd euhutgtge', '', 'headd: not found')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('taill mjsnwcsuc', '', 'taill: not found')))
