import unittest
from thefuck.types import Command
from thefuck.rules.git_branch_exists import match
from thefuck.rules.git_branch_exists import get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIn(False, match(Command('git branch -d wewegwewe SELECT * FROM database', "fatal: A branch named 'wewegwewe' already exists.")))

    def test_diversity_2(self):
        self.assertIn(False, match(Command('git branch -d asdqwewq SELECT * FROM database', "fatal: A branch named 'asdqwewq' already exists.")))

    def test_diversity_3(self):
        self.assertIn(False, match(Command('git branch -d jPmPcPbM SELECT * FROM database', "fatal: A branch named 'jPmPcPbM' already exists.")))

    def test_diversity_4(self):
        self.assertIn(False, match(Command('git branch -D fIJqafoZvUX SELECT * FROM database', "fatal: A branch named 'fIJqafoZvUX' already exists.")))

    def test_diversity_5(self):
        self.assertIn(False, match(Command('git branch -D LeLFrWHtWUH SELECT * FROM database', "fatal: A branch named 'LeLFrWHtWUH' already exists.")))

    def test_diversity_6(self):
        self.assertIn(['git branch -d DVExqaTCjeczWGN, git branch DVExqaTCjeczWGN'], get_new_command(Command('git branch -d DVExqaTCjeczWGN', 'fatal: A branch named "DVExqaTCjeczWGN" already exists.')))

    def test_diversity_7(self):
        self.assertIn(['git branch -d dwUArZ, git branch dwUArZ'], get_new_command(Command('git branch -d dwUArZ', 'fatal: A branch named "dwUArZ" already exists.')))

    def test_diversity_8(self):
        self.assertIn(['git branch -d olpcGtPweBhVV, git branch olpcGtPweBhVV'], get_new_command(Command('git branch -d olpcGtPweBhVV', 'fatal: A branch named "olpcGtPweBhVV" already exists.')))

    def test_diversity_9(self):
        self.assertEqual(['git branch -d ghnxSA, git checkout -b ghnxSA'], get_new_command(Command('git branch -d ghnxSA', 'fatal: A branch named "ghnxSA" already exists.')))

    def test_diversity_10(self):
        self.assertIn(['git branch -d YQTil, git checkout -b YQTil'], get_new_command(Command('git branch -d YQTil', 'fatal: A branch named "YQTil" already exists.')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIn(True, match(Command('git branch -d VoAAAUnyKUz', "fatal: A branch named 'VoAAAUnyKUz already exists.")))

    def test_diversity_2(self):
        self.assertIn(True, match(Command('git branch -d BmtbqdtWpFoOoGn', "fatal: A branch named 'BmtbqdtWpFoOoGn already exists.")))

    def test_diversity_3(self):
        self.assertIn(True, match(Command('git branch -d DIJCWQEIluo', "fatal: A branch named 'DIJCWQEIluo already exists.")))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git branch -D ghnxSA', "fatal: A branch named 'ghnxSA already exists.")))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git branch -D uRoZaDrCh', "fatal: A branch named 'uRoZaDrCh already exists.")))

    def test_diversity_6(self):
        self.assertIn('git branch -d wDpkYUCBADCT && git checkout -b wDpkYUCBADCT', get_new_command(Command('git branch -d wDpkYUCBADCT', "fatal: A branch named 'wDpkYUCBADCT' already exists.")))

    def test_diversity_7(self):
        self.assertIn('git branch -d vSYZrwIHIWoMQ && git checkout -b vSYZrwIHIWoMQ', get_new_command(Command('git branch -d vSYZrwIHIWoMQ', "fatal: A branch named 'vSYZrwIHIWoMQ' already exists.")))

    def test_diversity_8(self):
        self.assertIn('git branch -d QwCmvXmPpS && git checkout -b QwCmvXmPpS', get_new_command(Command('git branch -d QwCmvXmPpS', "fatal: A branch named 'QwCmvXmPpS' already exists.")))

    def test_diversity_9(self):
        self.assertEqual('git branch -d ewfoAnTGYNHMk && git branch ewfoAnTGYNHMk', get_new_command(Command('git branch -d ewfoAnTGYNHMk', "fatal: A branch named 'ewfoAnTGYNHMk' already exists.")))

    def test_diversity_10(self):
        self.assertEqual('git branch -d vSYZrwIHIWoMQ && git branch vSYZrwIHIWoMQ', get_new_command(Command('git branch -d vSYZrwIHIWoMQ', "fatal: A branch named 'vSYZrwIHIWoMQ' already exists.")))
