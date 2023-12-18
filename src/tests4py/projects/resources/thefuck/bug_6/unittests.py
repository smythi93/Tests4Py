import unittest
from thefuck.types import Command
from thefuck.rules.git_branch_exists import match
from thefuck.rules.git_branch_exists import get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIn(False, match(Command('git branch -D -A- ', "fatal: A branch named 'A already exists.")))

    def test_diversity_2(self):
        self.assertEqual(False,
                         match(Command('git branch -D -B- ', "fatal: A branch named 'B already exists.")))

    def test_diversity_3(self):
        self.assertEqual(['git branch -D C, git checkout -b C'], get_new_command(
            Command('git branch -D C', 'fatal: A branch named C already exists.')))

    def test_diversity_4(self):
        self.assertEqual(['git branch -D D, git checkout -b D'], get_new_command(
            Command('git branch -D D', 'fatal: A branch named D already exists.')))

    def test_diversity_5(self):
        self.assertEqual(True, match(
            Command('git branch -D E SELECT * FROM database', "A branch named 'E already exists.")))

    def test_diversity_6(self):
        self.assertIn(True, match(
            Command('git branch -D F SELECT * FROM database', "A branch named 'F already exists.")))

    def test_diversity_7(self):
        self.assertEqual(['git branch -D G, git checkout -b G'], get_new_command(
            Command('git branch -D G', 'fatal: A branch named G already exists.')))

    def test_diversity_8(self):
        self.assertIn(['git branch -D H, git checkout -b H'], get_new_command(
            Command('git branch -D H', 'fatal: A branch named H already exists.')))

    def test_diversity_9(self):
        self.assertEqual(False,
                         match(Command('git branch -D -I- ', "fatal: A branch named 'I already exists.")))

    def test_diversity_10(self):
        self.assertIn(['git branch -D J, git checkout -b J'], get_new_command(
            Command('git branch -D J', 'fatal: A branch named J already exists.')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git branch -d K', "fatal: A branch named 'K already exists.")))

    def test_diversity_2(self):
        self.assertIn(False, match(Command('git branch -d L', "fatal : A branch named 'L' already exists.")))

    def test_diversity_3(self):
        self.assertIn('git branch -d M && git checkout -b M', get_new_command(Command('git branch -d M', "fatal: A branch named 'M' already exists.")))

    def test_diversity_4(self):
        self.assertEqual('git branch -d N && git branch N', get_new_command(Command('git branch -d N', "fatal: A branch named 'N' already exists.")))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git branch -d O', "fatal: A branch named 'O already exists.")))

    def test_diversity_6(self):
        self.assertIn('git branch -d P && git checkout -b P', get_new_command(Command('git branch -d P', "fatal: A branch named 'P' already exists.")))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git branch -d Q', "fatal: A branch named 'Q already exists.")))

    def test_diversity_8(self):
        self.assertIn('git branch -d R && git checkout -b R', get_new_command(Command('git branch -d R', "fatal: A branch named 'R' already exists.")))

    def test_diversity_9(self):
        self.assertEqual('git branch -d S && git branch S', get_new_command(Command('git branch -d S', "fatal: A branch named 'S' already exists.")))

    def test_diversity_10(self):
        self.assertEqual('git branch -d T && git branch T', get_new_command(
            Command('git branch -d T', "fatal: A branch named 'T' already exists.")))
