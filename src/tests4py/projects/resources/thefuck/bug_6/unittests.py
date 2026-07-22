import unittest
from thefuck.rules.git_branch_exists import match
from thefuck.rules.git_branch_exists import get_new_command
from thefuck.types import Command

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):self.assertIn(['git branch -d ijLsADOwbJ, git checkout -b ijLsADOwbJ'], get_new_command(Command('git branch -d ijLsADOwbJ', "fatal: A branch named 'ijLsADOwbJ' already exists.")))

    def test_diversity_2(self):self.assertEqual(False, match(Command('git branch -d BRNdxeTIhFrWD SELECT * FROM database', "fatal: A branch named 'BRNdxeTIhFrWD' already exists.")))

    def test_diversity_3(self):self.assertIn(['git branch -d LrwKb, git branch LrwKb'], get_new_command(Command('git branch -d LrwKb', "fatal: A branch named 'LrwKb' already exists.")))

    def test_diversity_4(self):self.assertEqual(False, match(Command('git branch -d rgNUKPlYMtJABB SELECT * FROM database', "fatal: A branch named 'rgNUKPlYMtJABB' already exists.")))

    def test_diversity_5(self):self.assertIn(['git branch -d dCGkA, git branch dCGkA'], get_new_command(Command('git branch -d dCGkA', "fatal: A branch named 'dCGkA' already exists.")))

    def test_diversity_6(self):self.assertIn(['git branch -d OzdCPCJbOhFr, git checkout -b OzdCPCJbOhFr'], get_new_command(Command('git branch -d OzdCPCJbOhFr', "fatal: A branch named 'OzdCPCJbOhFr' already exists.")))

    def test_diversity_7(self):self.assertIn(['git branch -d qkkOuKzSs, git branch qkkOuKzSs'], get_new_command(Command('git branch -d qkkOuKzSs', "fatal: A branch named 'qkkOuKzSs' already exists.")))

    def test_diversity_8(self):self.assertIn(['git branch -d XseHvgmGXZ, git branch XseHvgmGXZ'], get_new_command(Command('git branch -d XseHvgmGXZ', "fatal: A branch named 'XseHvgmGXZ' already exists.")))

    def test_diversity_9(self):self.assertEqual(False, match(Command('git branch -d OcREB SELECT * FROM database', "fatal: A branch named 'OcREB' already exists.")))

    def test_diversity_10(self):self.assertIn(['git branch -d SEbVBSwy, git branch SEbVBSwy'], get_new_command(Command('git branch -d SEbVBSwy', "fatal: A branch named 'SEbVBSwy' already exists.")))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):self.assertIn('git branch -d eXivAnPdhCLRpJ && git branch eXivAnPdhCLRpJ', get_new_command(Command('git branch -d eXivAnPdhCLRpJ', "fatal: A branch named 'eXivAnPdhCLRpJ' already exists.")))

    def test_diversity_2(self):self.assertEqual(True, match(Command('git branch -D uvwDj', "fatal: A branch named 'uvwDj already exists.")))

    def test_diversity_3(self):self.assertIn('git branch -d bTeCkHtWpkiG && git branch bTeCkHtWpkiG', get_new_command(Command('git branch -d bTeCkHtWpkiG', "fatal: A branch named 'bTeCkHtWpkiG' already exists.")))

    def test_diversity_4(self):self.assertEqual(True, match(Command('git branch -d WZXYoOeFKNcye', "fatal: A branch named 'WZXYoOeFKNcye already exists.")))

    def test_diversity_5(self):self.assertEqual(True, match(Command('git branch -D XgyTRRgYBVIGqAT', "fatal: A branch named 'XgyTRRgYBVIGqAT already exists.")))

    def test_diversity_6(self):self.assertIn('git branch -d YkBAucQGnEzx && git branch YkBAucQGnEzx', get_new_command(Command('git branch -d YkBAucQGnEzx', "fatal: A branch named 'YkBAucQGnEzx' already exists.")))

    def test_diversity_7(self):self.assertEqual(True, match(Command('git branch -D rLtwBxFchv', "fatal: A branch named 'rLtwBxFchv already exists.")))

    def test_diversity_8(self):self.assertIn('git branch -d DnJUleaafUseYK && git checkout -b DnJUleaafUseYK', get_new_command(Command('git branch -d DnJUleaafUseYK', "fatal: A branch named 'DnJUleaafUseYK' already exists.")))

    def test_diversity_9(self):self.assertIn('git branch -d asLEhRmdcjrF && git branch asLEhRmdcjrF', get_new_command(Command('git branch -d asLEhRmdcjrF', "fatal: A branch named 'asLEhRmdcjrF' already exists.")))

    def test_diversity_10(self):self.assertEqual(True, match(Command('git branch -d rEBrCRsJTX', "fatal: A branch named 'rEBrCRsJTX already exists.")))