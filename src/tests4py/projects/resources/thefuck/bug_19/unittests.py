import unittest
from thefuck.types import Command
from thefuck.rules.git_push_force import match, get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git push rCYDUlkF', '', 'Everything up-to-date')))

    def test_diversity_2(self):
        self.assertEqual('git push --force CsdJkuBHuDmkW', get_new_command(Command('git PUSH CsdJkuBHuDmkW', '', '')))

    def test_diversity_3(self):
        self.assertEqual('git push --force kTofMoYehTQ', get_new_command(Command('git PUSH kTofMoYehTQ', '', '')))

    def test_diversity_4(self):
        self.assertEqual('git push --force vOwqwMyiW', get_new_command(Command('git PUSH vOwqwMyiW', '', '')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git push TjruwEsqChYg', '', 'Everything up-to-date')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git push HGbHhnuqYaoY', '',
                                             '\n        Counting objects: 3, done.\n        Delta compression using up to 4 threads.\n        Compressing objects: 100% (2/2), done.\n        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.\n        Total 3 (delta 0), reused 0 (delta 0)\n        To /tmp/bar\n           514eed3..f269c79  master -> master\n        ')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git push DebXFRvrFv', '',
                                             '\n        Counting objects: 3, done.\n        Delta compression using up to 4 threads.\n        Compressing objects: 100% (2/2), done.\n        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.\n        Total 3 (delta 0), reused 0 (delta 0)\n        To /tmp/bar\n           514eed3..f269c79  master -> master\n        ')))

    def test_diversity_8(self):
        self.assertEqual('git push --force oovGPY', get_new_command(Command('git PUSH oovGPY', '', '')))

    def test_diversity_9(self):
        self.assertEqual('git push --force CMOwD', get_new_command(Command('git PUSH CMOwD', '', '')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git push wreRgb', '', 'Everything up-to-date')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git push ihFNYYWRfcGdXmP', '',
                                             "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        ")))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git push IdDon', '',
                                             "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        ")))

    def test_diversity_3(self):
        self.assertEqual('git push --force rGDKK', get_new_command(Command('git push rGDKK', '', '')))

    def test_diversity_4(self):
        self.assertEqual('git push --force cJYleMbNFim', get_new_command(Command('git push cJYleMbNFim', '', '')))

    def test_diversity_5(self):
        self.assertEqual('git push --force PKkyPYamdpcuhut',
                         get_new_command(Command('git push PKkyPYamdpcuhut', '', '')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git push VgjuZYJvtg', '',
                                             "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        ")))

    def test_diversity_7(self):
        self.assertEqual('git push --force tlKfaS', get_new_command(Command('git push tlKfaS', '', '')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git push zxIdxSJDquYxITD', '',
                                             "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        ")))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git push ObbufQTF', '',
                                             "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        ")))

    def test_diversity_10(self):
        self.assertEqual('git push --force KNTGs', get_new_command(Command('git push KNTGs', '', '')))
