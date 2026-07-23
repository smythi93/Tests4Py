import unittest
from thefuck.rules.git_branch_exists import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git checkout -b ubogcrkgs', '', "fatal: A branch named 'ubogcrkgs' already exists.")))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git checkout -b dnjzyez', '', "fatal: A branch named 'dnjzyez' already exists.")))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git checkout -b ujzzyzu', '', "fatal: A branch named 'ujzzyzu' already exists.")))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git checkout -b lkwtcozzi', '', "fatal: A branch named 'lkwtcozzi' already exists.")))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git checkout -b zgxthrzgwi', '', "fatal: A branch named 'zgxthrzgwi' already exists.")))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git checkout -b hmbxmqhj', '', "fatal: A branch named 'hmbxmqhj' already exists.")))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git checkout -b gihzekpvb', '', "fatal: A branch named 'gihzekpvb' already exists.")))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git checkout -b dmohflhdh', '', "fatal: A branch named 'dmohflhdh' already exists.")))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git checkout -b hixjuk', '', "fatal: A branch named 'hixjuk' already exists.")))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git checkout -b yyyes', '', "fatal: A branch named 'yyyes' already exists.")))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git branch qjbzpwr', '', "fatal: A branch named 'qjbzpwr' already exists.")))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git branch mbddhpzysz', '', "fatal: A branch named 'mbddhpzysz' already exists.")))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git branch vpxgdrqm', '', "fatal: A branch named 'vpxgdrqm' already exists.")))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git branch iqzlfast', '', "fatal: A branch named 'iqzlfast' already exists.")))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git branch hjgzjchxxv', '', "fatal: A branch named 'hjgzjchxxv' already exists.")))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git branch guwwagss', '', "fatal: A branch named 'guwwagss' already exists.")))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git branch vcogxkbiu', '', "fatal: A branch named 'vcogxkbiu' already exists.")))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git branch brtbetubq', '', "fatal: A branch named 'brtbetubq' already exists.")))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git branch ydxrn', '', "fatal: A branch named 'ydxrn' already exists.")))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git branch zynnitmggx', '', "fatal: A branch named 'zynnitmggx' already exists.")))
