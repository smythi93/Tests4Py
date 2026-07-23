import unittest
from thefuck.rules.git_push import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch ubogcrkgs has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin ubogcrkgs')))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch dnjzyez has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin dnjzyez')))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch ujzzyzu has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin ujzzyzu')))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch lkwtcozzi has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin lkwtcozzi')))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch zgxthrzgwi has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin zgxthrzgwi')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch hmbxmqhj has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin hmbxmqhj')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch gihzekpvb has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin gihzekpvb')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch dmohflhdh has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin dmohflhdh')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch hixjuk has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin hixjuk')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('git push', 'fatal: The current branch yyyes has no upstream branch. To push the current branch and set the remote as upstream use git pull --set-upstream origin yyyes')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch qjbzpwr has no upstream branch. To push the current branch use git push --set-upstream origin qjbzpwr')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch mbddhpzysz has no upstream branch. To push the current branch use git push --set-upstream origin mbddhpzysz')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch vpxgdrqm has no upstream branch. To push the current branch use git push --set-upstream origin vpxgdrqm')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch iqzlfast has no upstream branch. To push the current branch use git push --set-upstream origin iqzlfast')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch hjgzjchxxv has no upstream branch. To push the current branch use git push --set-upstream origin hjgzjchxxv')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch guwwagss has no upstream branch. To push the current branch use git push --set-upstream origin guwwagss')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch vcogxkbiu has no upstream branch. To push the current branch use git push --set-upstream origin vcogxkbiu')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch brtbetubq has no upstream branch. To push the current branch use git push --set-upstream origin brtbetubq')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch ydxrn has no upstream branch. To push the current branch use git push --set-upstream origin ydxrn')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git push', 'fatal: The current branch zynnitmggx has no upstream branch. To push the current branch use git push --set-upstream origin zynnitmggx')))
