import unittest

from youtube_dl.utils import unescapeHTML


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(unescapeHTML('&a&quot;'), '&a"')

    def test_diversity_2(self):
        self.assertEqual(unescapeHTML('&a&eacute;'), '&aé')

    def test_diversity_3(self):
        self.assertEqual(unescapeHTML('&anna&&eacute;ric'), '&anna&éric')

    def test_diversity_4(self):
        self.assertEqual(unescapeHTML('&anna&#47;&eacute;ric'), '&anna/éric')

    def test_diversity_5(self):
        self.assertEqual(unescapeHTML('&&#47;'), '&/')

    def test_diversity_6(self):
        self.assertEqual(unescapeHTML('&&#x2F;'), '&/')

    def test_diversity_7(self):
        self.assertEqual(unescapeHTML('&&period;'), '&.')

    def test_diversity_8(self):
        self.assertEqual(unescapeHTML('&&apos;'), '&\'')

    def test_diversity_9(self):
        self.assertEqual(unescapeHTML('&&apos;&period;'), '&\'.')

    def test_diversity_10(self):
        self.assertEqual(unescapeHTML('&period;&&apos;'), '.&\'')


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(unescapeHTML('%20;'), '%20;')

    def test_diversity_2(self):
        self.assertEqual(unescapeHTML('&#x2F;'), '/')

    def test_diversity_3(self):
        self.assertEqual(unescapeHTML('&#47;'), '/')

    def test_diversity_4(self):
        self.assertEqual(unescapeHTML('&eacute;'), 'é')

    def test_diversity_5(self):
        self.assertEqual(unescapeHTML('&#2013266066;'), '&#2013266066;')

    def test_diversity_6(self):
        self.assertEqual(unescapeHTML('&period;&apos;'), '.\'')

    def test_diversity_7(self):
        self.assertEqual(unescapeHTML('&eacute;ric'), 'éric')

    def test_diversity_8(self):
        self.assertEqual(unescapeHTML('&period;'), '.')

    def test_diversity_9(self):
        self.assertEqual(unescapeHTML('&apos;'), '\'')

    def test_diversity_10(self):
        self.assertEqual(unescapeHTML('%10;'), '%10;')
