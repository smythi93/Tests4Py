import unittest
from thefuck.types import Command
from thefuck.rules.git_branch_exists import match
from thefuck.rules.git_branch_exists import get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIn(['git branch -d hSOwZQHjXGE, git branch hSOwZQHjXGE'], get_new_command(
            Command('git branch -d hSOwZQHjXGE', '', "fatal: A branch named 'hSOwZQHjXGE' already exists.")))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('git branch -d kwIwpT SELECT * FROM database', '',
                                              "fatal: A branch named 'kwIwpT' already exists.")))

    def test_diversity_3(self):
        self.assertIn(['git branch -d dpJBugeHfz, git branch dpJBugeHfz'], get_new_command(
            Command('git branch -d dpJBugeHfz', '', "fatal: A branch named 'dpJBugeHfz' already exists.")))

    def test_diversity_4(self):
        self.assertIn(['git branch -d gJZwfwhOJIXHN, git checkout -b gJZwfwhOJIXHN'], get_new_command(
            Command('git branch -d gJZwfwhOJIXHN', '', "fatal: A branch named 'gJZwfwhOJIXHN' already exists.")))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('git branch -D BYRfYkHkZMsu SELECT * FROM database', '',
                                              "fatal: A branch named 'BYRfYkHkZMsu' already exists.")))

    def test_diversity_6(self):
        self.assertIn(['git branch -d sGbxhhlynv, git branch sGbxhhlynv'], get_new_command(
            Command('git branch -d sGbxhhlynv', '', "fatal: A branch named 'sGbxhhlynv' already exists.")))

    def test_diversity_7(self):
        self.assertIn(['git branch -d LBgOHRNBdmuqV, git branch LBgOHRNBdmuqV'], get_new_command(
            Command('git branch -d LBgOHRNBdmuqV', '', "fatal: A branch named 'LBgOHRNBdmuqV' already exists.")))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('git branch -D tsNssMJRPps SELECT * FROM database', '',
                                              "fatal: A branch named 'tsNssMJRPps' already exists.")))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('git branch -d bOXCGjusBMJMjUe SELECT * FROM database', '',
                                              "fatal: A branch named 'bOXCGjusBMJMjUe' already exists.")))

    def test_diversity_10(self):
        self.assertIn(['git branch -d aebZiAxSX, git branch aebZiAxSX'], get_new_command(
            Command('git branch -d aebZiAxSX', '', "fatal: A branch named 'aebZiAxSX' already exists.")))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(
            Command('git branch -D kgXdCELP', '', "fatal: A branch named 'kgXdCELP already exists.")))

    def test_diversity_2(self):
        self.assertIn('git branch -d QHZtvDPXt && git branch QHZtvDPXt', get_new_command(
            Command('git branch -d QHZtvDPXt', '', "fatal: A branch named 'QHZtvDPXt' already exists.")))

    def test_diversity_3(self):
        self.assertIn('git branch -d CibAmH && git branch CibAmH', get_new_command(
            Command('git branch -d CibAmH', '', "fatal: A branch named 'CibAmH' already exists.")))

    def test_diversity_4(self):
        self.assertIn('git branch -d AUeVSHeKVtOKqGd && git branch AUeVSHeKVtOKqGd', get_new_command(
            Command('git branch -d AUeVSHeKVtOKqGd', '', "fatal: A branch named 'AUeVSHeKVtOKqGd' already exists.")))

    def test_diversity_5(self):
        self.assertEqual(True, match(
            Command('git branch -D pHZUDkKsqIvO', '', "fatal: A branch named 'pHZUDkKsqIvO already exists.")))

    def test_diversity_6(self):
        self.assertIn('git branch -d GmLgqwfIEoSwGZV && git branch GmLgqwfIEoSwGZV', get_new_command(
            Command('git branch -d GmLgqwfIEoSwGZV', '', "fatal: A branch named 'GmLgqwfIEoSwGZV' already exists.")))

    def test_diversity_7(self):
        self.assertEqual(True, match(
            Command('git branch -d VOVrvqFhxTCi', '', "fatal: A branch named 'VOVrvqFhxTCi already exists.")))

    def test_diversity_8(self):
        self.assertEqual(True, match(
            Command('git branch -d NyUGujFPR', '', "fatal: A branch named 'NyUGujFPR already exists.")))

    def test_diversity_9(self):
        self.assertIn('git branch -d ldXMHzKCTUMB && git branch ldXMHzKCTUMB', get_new_command(
            Command('git branch -d ldXMHzKCTUMB', '', "fatal: A branch named 'ldXMHzKCTUMB' already exists.")))

    def test_diversity_10(self):
        self.assertEqual(True, match(
            Command('git branch -D iHjAmAwxFKPFV', '', "fatal: A branch named 'iHjAmAwxFKPFV already exists.")))
