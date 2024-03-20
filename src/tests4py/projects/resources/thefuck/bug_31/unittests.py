import unittest
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.git_diff_staged import get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(23, '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(454, '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(33, '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(3, '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(1000, '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(54, '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(1232, '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(643, '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(324, '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('Integer value cannot be used', get_new_command(Command(435, '', ''), Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git diff KsdjkdRCgjxG --staged',
                         get_new_command(Command('git diff KsdjkdRCgjxG', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('git diff giOaYVEyyitgY --staged',
                         get_new_command(Command('git diff giOaYVEyyitgY', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('git diff wVuXSWPVCqndbGN --staged',
                         get_new_command(Command('git diff wVuXSWPVCqndbGN', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('git diff hhWptFQBXUUaVUW --staged',
                         get_new_command(Command('git diff hhWptFQBXUUaVUW', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('git diff TQMMY --staged', get_new_command(Command('git diff TQMMY', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('git diff KoulNMKoa --staged',
                         get_new_command(Command('git diff KoulNMKoa', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('git diff GtCxg --staged', get_new_command(Command('git diff GtCxg', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('git diff CWsXwuetYHWisC --staged',
                         get_new_command(Command('git diff CWsXwuetYHWisC', '', ''), Settings()))
    def test_diversity_9(self):
        self.assertEqual('git diff JgDXrLPVlI --staged',
                         get_new_command(Command('git diff JgDXrLPVlI', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('git diff FwbyMcFwjaPUpd --staged',
                         get_new_command(Command('git diff FwbyMcFwjaPUpd', '', ''), Settings()))

