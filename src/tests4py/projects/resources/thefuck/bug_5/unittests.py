import unittest
from thefuck.rules.git_push import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git pushpull --set-upstream <remote> <a>',
                                             'fatal: The current branch [a] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [a]')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git pushpull --set-upstream <remote> <b>',
                                             'fatal: The current branch [b] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [b]')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git pushpull --set-upstream <remote> <c>',
                                             'fatal: The current branch [c] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [c]')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git pushpull --set-upstream <remote> <d>',
                                             'fatal: The current branch [d] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [d]')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git pushpull --set-upstream <remote> <e>',
                                             'fatal: The current branch [e] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [e]')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <f> SELECT * FROM users',
                                              'fatal: The current branch [f] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [f]')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <g> SELECT * FROM users',
                                              'fatal: The current branch [g] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [g]')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <h> SELECT * FROM users',
                                              'fatal: The current branch [h] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [h]')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <i> SELECT * FROM users',
                                              'fatal: The current branch [i] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [i]')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('git push --set-upstream <remote> <j> SELECT * FROM users',
                                              'fatal: The current branch [j] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [j]')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <k>',
                                             'fatal: The current branch [k] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [k]')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <l>',
                                             'fatal: The current branch [l] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [l]')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <m>',
                                             'fatal: The current branch [m] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [m]')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <n>',
                                             'fatal: The current branch [n] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [n]')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git push --set-upstream <remote> <o>',
                                             'fatal: The current branch [o] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [o]')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <p>',
                                              'fatal: The current branch [p] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [p]')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <q>',
                                              'fatal: The current branch [q] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [q]')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <r>',
                                              'fatal: The current branch [r] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [r]')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <s>',
                                              'fatal: The current branch [s] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [s]')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('git pull --set-upstream <remote> <t>',
                                              'fatal: The current branch [t] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [t]')))
