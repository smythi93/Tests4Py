import unittest
from thefuck.types import Command, Settings
from thefuck.rules.vagrant_up import get_new_command

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant bSEfPopOjnMqvAh IqdKp', '', ''), Settings()), list))

    def test_diversity_2(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant mhyhwPCPhSfK ovzsqwk', '', ''), Settings()), list))

    def test_diversity_3(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant tfSGrywUGWk aADPKIrGjJipAz', '', ''), Settings()), list))

    def test_diversity_4(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant ViLTM LKqaRcyu', '', ''), Settings()), list))

    def test_diversity_5(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant qwCfTi lpJJulXPLq', '', ''), Settings()), list))

    def test_diversity_6(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant kSzGQwLebv nlTIkuNiaAzgJzz', '', ''), Settings()), list))

    def test_diversity_7(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant TdQJblCc hOInNqLJMeGnuZ', '', ''), Settings()), list))

    def test_diversity_8(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant gVjuKzHeZXyVk gsbTneB', '', ''), Settings()), list))

    def test_diversity_9(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant hYFFRXSQLgfK zDjOpMqLZQ', '', ''), Settings()), list))

    def test_diversity_10(self):
        self.assertEqual(True, isinstance(get_new_command(Command('vagrant ZbaaByiexgscu YqXNklPxjR', '', ''), Settings()), list))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant rXyVazJH', '', ''), Settings()), list))

    def test_diversity_2(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant DNYftVaxnx', '', ''), Settings()), list))

    def test_diversity_3(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant viwzmICeJ', '', ''), Settings()), list))

    def test_diversity_4(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant yEKHeK', '', ''), Settings()), list))

    def test_diversity_5(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant oGLjPfgWtNv', '', ''), Settings()), list))

    def test_diversity_6(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant NtktldO', '', ''), Settings()), list))

    def test_diversity_7(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant FolzOBuxtlzjR', '', ''), Settings()), list))

    def test_diversity_8(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant TjgKpOh', '', ''), Settings()), list))

    def test_diversity_9(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant mKIpQa', '', ''), Settings()), list))

    def test_diversity_10(self):
        self.assertEqual(False, isinstance(get_new_command(Command('vagrant HuuMDzWHAp', '', ''), Settings()), list))
