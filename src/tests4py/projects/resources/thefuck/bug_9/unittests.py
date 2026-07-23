import unittest
from thefuck.rules.git_push import get_new_command
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git push --set-upstream origin ubogcrkgs', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin ubogcrkgs\n\n')))

    def test_diversity_2(self):
        self.assertEqual('git push --set-upstream origin dnjzyez', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin dnjzyez\n\n')))

    def test_diversity_3(self):
        self.assertEqual('git push --set-upstream origin ujzzyzu', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin ujzzyzu\n\n')))

    def test_diversity_4(self):
        self.assertEqual('git push --set-upstream origin lkwtcozzi', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin lkwtcozzi\n\n')))

    def test_diversity_5(self):
        self.assertEqual('git push --set-upstream origin zgxthrzgwi', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin zgxthrzgwi\n\n')))

    def test_diversity_6(self):
        self.assertEqual('git push --set-upstream origin hmbxmqhj', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin hmbxmqhj\n\n')))

    def test_diversity_7(self):
        self.assertEqual('git push --set-upstream origin gihzekpvb', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin gihzekpvb\n\n')))

    def test_diversity_8(self):
        self.assertEqual('git push --set-upstream origin dmohflhdh', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin dmohflhdh\n\n')))

    def test_diversity_9(self):
        self.assertEqual('git push --set-upstream origin hixjuk', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin hixjuk\n\n')))

    def test_diversity_10(self):
        self.assertEqual('git push --set-upstream origin yyyes', get_new_command(Command('git push -u', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin yyyes\n\n')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git push --set-upstream origin master origin qjbzpwr', get_new_command(Command('git push origin qjbzpwr', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_2(self):
        self.assertEqual('git push --set-upstream origin master origin mbddhpzysz', get_new_command(Command('git push origin mbddhpzysz', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_3(self):
        self.assertEqual('git push --set-upstream origin master origin vpxgdrqm', get_new_command(Command('git push origin vpxgdrqm', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_4(self):
        self.assertEqual('git push --set-upstream origin master origin iqzlfast', get_new_command(Command('git push origin iqzlfast', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_5(self):
        self.assertEqual('git push --set-upstream origin master origin hjgzjchxxv', get_new_command(Command('git push origin hjgzjchxxv', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_6(self):
        self.assertEqual('git push --set-upstream origin master origin guwwagss', get_new_command(Command('git push origin guwwagss', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_7(self):
        self.assertEqual('git push --set-upstream origin master origin vcogxkbiu', get_new_command(Command('git push origin vcogxkbiu', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_8(self):
        self.assertEqual('git push --set-upstream origin master origin brtbetubq', get_new_command(Command('git push origin brtbetubq', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_9(self):
        self.assertEqual('git push --set-upstream origin master origin ydxrn', get_new_command(Command('git push origin ydxrn', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))

    def test_diversity_10(self):
        self.assertEqual('git push --set-upstream origin master origin zynnitmggx', get_new_command(Command('git push origin zynnitmggx', '', 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream use\n\n    git push --set-upstream origin master\n\n')))
