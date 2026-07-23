import unittest
from thefuck.rules.git_fix_stash import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash ubogcrkgs')))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash dnjzyez')))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash ujzzyzu')))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash lkwtcozzi')))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash zgxthrzgwi')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash hmbxmqhj')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash gihzekpvb')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash dmohflhdh')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash hixjuk')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('git', '', 'usage: git stash yyyes')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(Command('git qjbzpwr', '', 'usage: git something')))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('git mbddhpzysz', '', 'usage: git something')))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('git vpxgdrqm', '', 'usage: git something')))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('git iqzlfast', '', 'usage: git something')))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('git hjgzjchxxv', '', 'usage: git something')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('git guwwagss', '', 'usage: git something')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('git vcogxkbiu', '', 'usage: git something')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git brtbetubq', '', 'usage: git something')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git ydxrn', '', 'usage: git something')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('git zynnitmggx', '', 'usage: git something')))
