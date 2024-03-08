import unittest
from thefuck.rules.git_add import match, get_new_command
from tests.utils import Command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('git add -- zAjCxGVngifvleN && git submodule update zAjCxGVngifvleN', get_new_command(
            Command('GIT SUBMODULE UPDATE zAjCxGVngifvleN', '',
                    "error: pathspec 'zAjCxGVngifvleN' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git submodule update hHAnhHgLKGvlZ', '', '')))

    def test_diversity_3(self):
        self.assertEqual('git add -- MxPfwsXrzI && git submodule update MxPfwsXrzI', get_new_command(
            Command('GIT SUBMODULE UPDATE MxPfwsXrzI', '',
                    "error: pathspec 'MxPfwsXrzI' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git commit MvrDrCNhPBHuC', '', '')))

    def test_diversity_5(self):
        self.assertEqual('git add -- IAjrih && git commit IAjrih', get_new_command(Command('GIT COMMIT IAjrih', '',
                                                                                           "error: pathspec 'IAjrih' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_6(self):
        self.assertEqual('git add -- aaSFKv && git submodule update aaSFKv', get_new_command(
            Command('GIT SUBMODULE UPDATE aaSFKv', '',
                    "error: pathspec 'aaSFKv' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_7(self):
        self.assertEqual('git add -- LFXPjNV && git commit LFXPjNV', get_new_command(Command('GIT COMMIT LFXPjNV', '',
                                                                                             "error: pathspec 'LFXPjNV' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git submodule update WlkCUZEtaY', '', '')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git commit jfjasduej', '', '')))

    def test_diversity_10(self):
        self.assertEqual('git add -- DfxaSUY && git commit DfxaSUY', get_new_command(Command('GIT COMMIT DfxaSUY', '',
                                                                                             "error: pathspec 'DfxaSUY' did not match any file(s) known to git. Did you forget to 'git add'?")))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git submodule update MmhXCRUzYjMes', '',
                                             "error: pathspec 'MmhXCRUzYjMes' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git commit xSxlBlHhuHZ', '',
                                             "error: pathspec 'xSxlBlHhuHZ' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_3(self):
        self.assertEqual('git add -- SoCvsHAx && git submodule update SoCvsHAx', get_new_command(
            Command('git submodule update SoCvsHAx', '',
                    "error: pathspec 'SoCvsHAx' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_4(self):
        self.assertEqual('git add -- fVLkEjrFAaRIbmG && git commit fVLkEjrFAaRIbmG', get_new_command(
            Command('git commit fVLkEjrFAaRIbmG', '',
                    "error: pathspec 'fVLkEjrFAaRIbmG' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git submodule update JRSQS', '',
                                             "error: pathspec 'JRSQS' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git commit bNxDAd', '',
                                             "error: pathspec 'bNxDAd' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_7(self):
        self.assertEqual('git add -- wfqpuEIwxnxMp && git submodule update wfqpuEIwxnxMp', get_new_command(
            Command('git submodule update wfqpuEIwxnxMp', '',
                    "error: pathspec 'wfqpuEIwxnxMp' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git commit toFLkaI', '',
                                             "error: pathspec 'toFLkaI' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_9(self):
        self.assertEqual('git add -- oakKlxDRN && git submodule update oakKlxDRN', get_new_command(
            Command('git submodule update oakKlxDRN', '',
                    "error: pathspec 'oakKlxDRN' did not match any file(s) known to git. Did you forget to 'git add'?")))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git commit FYYTFHiYpD', '',
                                             "error: pathspec 'FYYTFHiYpD' did not match any file(s) known to git. Did you forget to 'git add'?")))
