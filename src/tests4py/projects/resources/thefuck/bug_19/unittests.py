import unittest
from thefuck.rules.git_push_force import get_new_command, match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git push --force-with-lease origin ubogcrkgs', get_new_command(Command('git push origin ubogcrkgs', '', '')))

    def test_diversity_2(self):
        self.assertEqual('git push --force-with-lease origin dnjzyez', get_new_command(Command('git push origin dnjzyez', '', '')))

    def test_diversity_3(self):
        self.assertEqual('git push --force-with-lease origin ujzzyzu', get_new_command(Command('git push origin ujzzyzu', '', '')))

    def test_diversity_4(self):
        self.assertEqual('git push --force-with-lease origin lkwtcozzi', get_new_command(Command('git push origin lkwtcozzi', '', '')))

    def test_diversity_5(self):
        self.assertEqual('git push --force-with-lease origin zgxthrzgwi', get_new_command(Command('git push origin zgxthrzgwi', '', '')))

    def test_diversity_6(self):
        self.assertEqual('git push --force-with-lease origin hmbxmqhj', get_new_command(Command('git push origin hmbxmqhj', '', '')))

    def test_diversity_7(self):
        self.assertEqual('git push --force-with-lease origin gihzekpvb', get_new_command(Command('git push origin gihzekpvb', '', '')))

    def test_diversity_8(self):
        self.assertEqual('git push --force-with-lease origin dmohflhdh', get_new_command(Command('git push origin dmohflhdh', '', '')))

    def test_diversity_9(self):
        self.assertEqual('git push --force-with-lease origin hixjuk', get_new_command(Command('git push origin hixjuk', '', '')))

    def test_diversity_10(self):
        self.assertEqual('git push --force-with-lease origin yyyes', get_new_command(Command('git push origin yyyes', '', '')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git push origin qjbzpwr', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git push origin mbddhpzysz', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git push origin vpxgdrqm', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git push origin iqzlfast', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git push origin hjgzjchxxv', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git push origin guwwagss', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git push origin vcogxkbiu', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git push origin brtbetubq', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git push origin ydxrn', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git push origin zynnitmggx', '', '! [rejected] failed to push some refs to origin Updates were rejected because the tip of your current branch is behind')))
