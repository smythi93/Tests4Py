import unittest
from thefuck.rules.pip_unknown_command import get_new_command
from thefuck.types import Command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_2(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_3(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_4(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_5(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_6(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_7(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_8(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_9(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))

    def test_diversity_10(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip --1nstl numpy', 'ERROR: unknown command "--1nstl", maybe you meant "install"')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_2(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))
    def test_diversity_3(self):

        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_4(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_5(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_6(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_7(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_8(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_9(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))

    def test_diversity_10(self):
        self.assertEqual('pip install numpy', get_new_command(
            Command('pip instl numpy', 'ERROR: unknown command "instl", maybe you meant "install"')))
