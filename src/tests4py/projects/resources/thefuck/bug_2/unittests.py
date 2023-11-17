import unittest
from thefuck.utils import get_all_executables


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin")

    def test_diversity_2(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user2\\bin")

    def test_diversity_3(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user3\\bin")

    def test_diversity_4(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user4\\bin")

    def test_diversity_5(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user5\\bin")

    def test_diversity_6(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user6\\bin")

    def test_diversity_7(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user7\\bin")

    def test_diversity_8(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user8\\bin")

    def test_diversity_9(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user9\\bin")

    def test_diversity_10(self):
        self.assertEqual("C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user10\\bin")


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIn('mount', get_all_executables())

    def test_diversity_2(self):
        self.assertIn('last', get_all_executables())

    def test_diversity_3(self):
        self.assertIn('heap', get_all_executables())

    def test_diversity_4(self):
        self.assertIn('pip', get_all_executables())

    def test_diversity_5(self):
        self.assertIn('istack', get_all_executables())

    def test_diversity_6(self):
        self.assertIn('jarsigner', get_all_executables())

    def test_diversity_7(self):
        self.assertIn('libtool', get_all_executables)

    def test_diversity_8(self):
        self.assertIn('nl', get_all_executables())

    def test_diversity_9(self):
        self.assertIn('bundler', get_all_executables())

    def test_diversity_10(self):
        self.assertIn('ifconfig', get_all_executables())
