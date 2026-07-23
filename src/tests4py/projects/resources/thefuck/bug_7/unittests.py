import unittest
from thefuck.rules.php_s import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('php iad -s ubogcrkgs', '')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('php vew -s dnjzyez', '')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('php cqm -s ujzzyzu', '')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('php bdd -s lkwtcozzi', '')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('php hpz -s zgxthrzgwi', '')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('php ysz -s hmbxmqhj', '')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('php mgj -s gihzekpvb', '')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('php fah -s dmohflhdh', '')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('php vdo -s hixjuk', '')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('php iqz -s yyyes', '')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('php -s biuowvw', '')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('php -s etubqcsexf', '')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('php -s zynnitmggx', '')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('php -s xeptudhdh', '')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('php -s yftbvuydd', '')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('php -s vrvzfbe', '')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('php -s gpsfujk', '')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('php -s gjundkdo', '')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('php -s dkkbw', '')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('php -s vzynonqnv', '')))
