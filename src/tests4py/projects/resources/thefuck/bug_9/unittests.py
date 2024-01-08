import unittest
from thefuck.types import Command
from thefuck.rules.git_push import get_new_command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('git push --set-upstream origin yZJGXGbjlF', get_new_command(Command('git push -u', '',
                                                                                              'fatal: The current branch yZJGXGbjlF has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin yZJGXGbjlF\n\n')))

    def test_diversity_2(self):
        self.assertEqual('git push --set-upstream origin DgjMqrANplk', get_new_command(Command('git push --force', '',
                                                                                               'fatal: The current branch DgjMqrANplk has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin DgjMqrANplk\n\n')))

    def test_diversity_3(self):
        self.assertEqual('git push --set-upstream origin yjfkwfe', get_new_command(Command('git push -u', '',
                                                                                           'fatal: The current branch yjfkwfe has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin yjfkwfe\n\n')))

    def test_diversity_4(self):
        self.assertEqual('git push --set-upstream origin ebrihwebjh', get_new_command(Command('git push -u', '',
                                                                                              'fatal: The current branch ebrihwebjh has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin ebrihwebjh\n\n')))

    def test_diversity_5(self):
        self.assertEqual('git push --set-upstream origin asPAva', get_new_command(Command('git push --force', '',
                                                                                          'fatal: The current branch asPAva has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin asPAva\n\n')))

    def test_diversity_6(self):
        self.assertEqual('git push --set-upstream origin yrlqncoa', get_new_command(Command('git push -u', '',
                                                                                            'fatal: The current branch yrlqncoa has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin yrlqncoa\n\n')))

    def test_diversity_7(self):
        self.assertEqual('git push --set-upstream origin oejwebkwh', get_new_command(Command('git push -u', '',
                                                                                             'fatal: The current branch oejwebkwh has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin oejwebkwh\n\n')))

    def test_diversity_8(self):
        self.assertEqual('git push --set-upstream origin uyrjqmknks', get_new_command(Command('git push --force', '',
                                                                                              'fatal: The current branch uyrjqmknks has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin uyrjqmknks\n\n')))

    def test_diversity_9(self):
        self.assertEqual('git push --set-upstream origin oiqehknsjdhl', get_new_command(Command('git push -u', '',
                                                                                                'fatal: The current branch oiqehknsjdhl has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin oiqehknsjdhl\n\n')))

    def test_diversity_10(self):
        self.assertEqual('git push --set-upstream origin tqbsbxgjaji', get_new_command(Command('git push --force', '',
                                                                                               'fatal: The current branch tqbsbxgjaji has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin tqbsbxgjaji\n\n')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('git push --set-upstream origin uUmDS', get_new_command(Command('git push -u origin', '',
                                                                                         'fatal: The current branch uUmDS has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin uUmDS\n\n')))

    def test_diversity_2(self):
        self.assertEqual('git push --set-upstream origin YUHdVku',
                         get_new_command(Command('git push --set-upstream origin', '',
                                                 'fatal: The current branch YUHdVku has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin YUHdVku\n\n')))

    def test_diversity_3(self):
        self.assertEqual('git push --set-upstream origin hFGok --quiet', get_new_command(Command('git push --quiet', '',
                                                                                                 'fatal: The current branch hFGok has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin hFGok\n\n')))

    def test_diversity_4(self):
        self.assertEqual('git push --set-upstream origin uenrk', get_new_command(Command('git push -u origin', '',
                                                                                         'fatal: The current branch uenrk has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin uenrk\n\n')))

    def test_diversity_5(self):
        self.assertEqual('git push --set-upstream origin hFGok --quiet', get_new_command(Command('git push --quiet', '',
                                                                                                 'fatal: The current branch master has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin hFGok\n\n')))

    def test_diversity_6(self):
        self.assertEqual('git push --set-upstream origin yvBGvYzwLCvuz', get_new_command(Command('git push', '',
                                                                                                 'fatal: The current branch yvBGvYzwLCvuz has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin yvBGvYzwLCvuz\n\n')))

    def test_diversity_7(self):
        self.assertEqual('git push --set-upstream origin wweerw', get_new_command(Command('git push -u origin', '',
                                                                                          'fatal: The current branch wweerw has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin wweerw\n\n')))

    def test_diversity_8(self):
        self.assertEqual('git push --set-upstream origin hyryvqQ --quiet',
                         get_new_command(Command('git push --quiet', '',
                                                 'fatal: The current branch hyryvqQ has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin hyryvqQ\n\n')))

    def test_diversity_9(self):
        self.assertEqual('git push --set-upstream origin yhrbkvjfhi', get_new_command(Command('git push', '',
                                                                                              'fatal: The current branch yhrbkvjfhi has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin yhrbkvjfhi\n\n')))

    def test_diversity_10(self):
        self.assertEqual('git push --set-upstream origin OHAKEpk',
                         get_new_command(Command('git push --set-upstream origin', '',
                                                 'fatal: The current branch OHAKEpk has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin OHAKEpk\n\n')))
