import unittest
from thefuck.rules.git_push import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <A>',
                                             b'fatal: The current branch [A] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [A]')))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <B>', 100)))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <C>',
                                             b'fatal: The current branch [C] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [C]')))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <D>',
                                             b'fatal: The current branch [D] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [D]')))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <E>', 10)))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <F>',
                                              b'fatal: The current branch [F] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [F]')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <G>',
                                              b'fatal: The current branch [G] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [G]')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <H>', 1)))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <I>',
                                              b'fatal: The current branch [I] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [I]')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <J>',
                                              b'fatal: The current branch [J] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [J]')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <K>',
                                             'fatal: The current branch [K] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [K]')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <L>',
                                             'fatal: The current branch [L] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [L]')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <M>',
                                             'fatal: The current branch [M] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [M]')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <N>',
                                             'fatal: The current branch [N] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [N]')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <O>',
                                             'fatal: The current branch [O] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [O]')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <P>',
                                              'fatal: The current branch [P] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [P]')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <Q>',
                                              'fatal: The current branch [Q] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [Q]')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <R>',
                                              'fatal: The current branch [R] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [R]')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <S>',
                                              'fatal: The current branch [S] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [S]')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <T>',
                                              'fatal: The current branch [T] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [T]')))
