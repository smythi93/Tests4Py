import unittest
from thefuck.rules.git_diff_staged import get_new_command
from thefuck.types import Command
from thefuck.types import Settings


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git diff --staged ubogcrkgs', get_new_command(Command('git diff ubogcrkgs', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('git diff --staged dnjzyez', get_new_command(Command('git diff dnjzyez', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('git diff --staged ujzzyzu', get_new_command(Command('git diff ujzzyzu', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('git diff --staged lkwtcozzi', get_new_command(Command('git diff lkwtcozzi', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('git diff --staged zgxthrzgwi', get_new_command(Command('git diff zgxthrzgwi', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('git diff --staged hmbxmqhj', get_new_command(Command('git diff hmbxmqhj', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('git diff --staged gihzekpvb', get_new_command(Command('git diff gihzekpvb', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('git diff --staged dmohflhdh', get_new_command(Command('git diff dmohflhdh', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual('git diff --staged hixjuk', get_new_command(Command('git diff hixjuk', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('git diff --staged yyyes', get_new_command(Command('git diff yyyes', '', ''), Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git qjbzpwr diff --staged', get_new_command(Command('git qjbzpwr diff', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('git mbddhpzysz diff --staged', get_new_command(Command('git mbddhpzysz diff', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('git vpxgdrqm diff --staged', get_new_command(Command('git vpxgdrqm diff', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('git iqzlfast diff --staged', get_new_command(Command('git iqzlfast diff', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('git hjgzjchxxv diff --staged', get_new_command(Command('git hjgzjchxxv diff', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('git guwwagss diff --staged', get_new_command(Command('git guwwagss diff', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('git vcogxkbiu diff --staged', get_new_command(Command('git vcogxkbiu diff', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('git brtbetubq diff --staged', get_new_command(Command('git brtbetubq diff', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual('git ydxrn diff --staged', get_new_command(Command('git ydxrn diff', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('git zynnitmggx diff --staged', get_new_command(Command('git zynnitmggx diff', '', ''), Settings()))
