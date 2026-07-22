import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unescapeHTML


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('&#974757464;', unescapeHTML('&#974757464;'))

    def test_diversity_2(self):
        self.assertEqual('&#2022917459;', unescapeHTML('&#2022917459;'))

    def test_diversity_3(self):
        self.assertEqual('&#13527080;', unescapeHTML('&#13527080;'))

    def test_diversity_4(self):
        self.assertEqual('&#x127800f0;', unescapeHTML('&#x127800f0;'))

    def test_diversity_5(self):
        self.assertEqual('&#x54353130;', unescapeHTML('&#x54353130;'))

    def test_diversity_6(self):
        self.assertEqual('&#x1574f0ed;', unescapeHTML('&#x1574f0ed;'))

    def test_diversity_7(self):
        self.assertEqual('&#164825333;', unescapeHTML('&#164825333;'))

    def test_diversity_8(self):
        self.assertEqual('&#x150f0ece;', unescapeHTML('&#x150f0ece;'))

    def test_diversity_9(self):
        self.assertEqual('&#1197971684;', unescapeHTML('&#1197971684;'))

    def test_diversity_10(self):
        self.assertEqual('&#310879448;', unescapeHTML('&#310879448;'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('壃', unescapeHTML('&#22723;'))

    def test_diversity_2(self):
        self.assertEqual('螺', unescapeHTML('&#34746;'))

    def test_diversity_3(self):
        self.assertEqual('ꯇ', unescapeHTML('&#43975;'))

    def test_diversity_4(self):
        self.assertEqual('瑣', unescapeHTML('&#x7463;'))

    def test_diversity_5(self):
        self.assertEqual('檰', unescapeHTML('&#27312;'))

    def test_diversity_6(self):
        self.assertEqual('꦳', unescapeHTML('&#xa9b3;'))

    def test_diversity_7(self):
        self.assertEqual('ⶇ', unescapeHTML('&#11655;'))

    def test_diversity_8(self):
        self.assertEqual('➲', unescapeHTML('&#x27b2;'))

    def test_diversity_9(self):
        self.assertEqual('➱', unescapeHTML('&#x27b1;'))

    def test_diversity_10(self):
        self.assertEqual('ત', unescapeHTML('&#xaa4;'))
