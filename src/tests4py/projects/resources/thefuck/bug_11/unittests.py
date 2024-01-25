import unittest
from thefuck.rules.git_push import get_new_command
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git push --set-upstream origin master', get_new_command(Command(
            'fatal: The current branch has no upstream RQZQyYuKlTy.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push')))

    def test_diversity_2(self):
        self.assertEqual('git push --set-upstream origin master --quiet', get_new_command(Command(
            'fatal: The current branch has no upstream gjjPNn.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push --quiet')))

    def test_diversity_3(self):
        self.assertEqual('git push --set-upstream origin master', get_new_command(Command(
            'fatal: The current branch has no upstream kWqhOQItL.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push')))

    def test_diversity_4(self):
        self.assertEqual('git push --set-upstream origin master -u origin', get_new_command(Command(
            'fatal: The current branch has no upstream xLOebi.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push -u origin')))

    def test_diversity_5(self):
        self.assertEqual('git push --set-upstream origin master -u origin', get_new_command(Command(
            'fatal: The current branch has no upstream IeMPodxvgKvUlLL.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push -u origin')))

    def test_diversity_6(self):
        self.assertEqual('git push --set-upstream origin master --set-upstream origin', get_new_command(Command(
            'fatal: The current branch has no upstream znKkcLylOoMgH.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push --set-upstream origin')))

    def test_diversity_7(self):
        self.assertEqual('git push --set-upstream origin master -u origin', get_new_command(Command(
            'fatal: The current branch has no upstream lTBhFbAcWfrCC.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push -u origin')))

    def test_diversity_8(self):
        self.assertEqual('git push --set-upstream origin master -u origin', get_new_command(Command(
            'fatal: The current branch has no upstream cAAZrkPN.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push -u origin')))

    def test_diversity_9(self):
        self.assertEqual('git push --set-upstream origin master', get_new_command(Command(
            'fatal: The current branch has no upstream TspNlUaMLncoD.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push')))

    def test_diversity_10(self):
        self.assertEqual('git push --set-upstream origin master', get_new_command(Command(
            'fatal: The current branch has no upstream xCjXRR.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ',
            '', 'git push')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('git push --set-upstream origin master --quiet', get_new_command(
            Command('git push --quiet', '',
                    'fatal: The current branch has no upstream PYnKNJs.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_2(self):
        self.assertEqual('git push --set-upstream origin master -u origin', get_new_command(
            Command('git push -u origin', '',
                    'fatal: The current branch has no upstream ftkXAEwPKoWZ.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_3(self):
        self.assertEqual('git push --set-upstream origin master --set-upstream origin', get_new_command(
            Command('git push --set-upstream origin', '',
                    'fatal: The current branch has no upstream iMDAPTIv.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_4(self):
        self.assertEqual('git push --set-upstream origin master', get_new_command(Command('git push', '',
                                                                                          'fatal: The current branch has no upstream NTYor.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_5(self):
        self.assertEqual('git push --set-upstream origin master --set-upstream origin', get_new_command(
            Command('git push --set-upstream origin', '',
                    'fatal: The current branch has no upstream duCvvNKrMtTH.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_6(self):
        self.assertEqual('git push --set-upstream origin master', get_new_command(Command('git push', '',
                                                                                          'fatal: The current branch has no upstream kHkDoNOxW.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_7(self):
        self.assertEqual('git push --set-upstream origin master', get_new_command(Command('git push', '',
                                                                                          'fatal: The current branch has no upstream InqVJAifxGFJpEy.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_8(self):
        self.assertEqual('git push --set-upstream origin master -u origin', get_new_command(
            Command('git push -u origin', '',
                    'fatal: The current branch has no upstream gvsbOfl.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_9(self):
        self.assertEqual('git push --set-upstream origin master --quiet', get_new_command(
            Command('git push --quiet', '',
                    'fatal: The current branch has no upstream LqPLuyG.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))

    def test_diversity_10(self):
        self.assertEqual('git push --set-upstream origin master --quiet', get_new_command(
            Command('git push --quiet', '',
                    'fatal: The current branch has no upstream YydlwquqXw.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ')))
