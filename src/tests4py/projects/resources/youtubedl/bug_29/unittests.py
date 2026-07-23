import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unified_strdate


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(None, unified_strdate('ybljz'))

    def test_diversity_2(self):
        self.assertEqual(None, unified_strdate('pylsww vhlp'))

    def test_diversity_3(self):
        self.assertEqual(None, unified_strdate('kgtqcxmvf'))

    def test_diversity_4(self):
        self.assertEqual(None, unified_strdate('clms frfqrkf'))

    def test_diversity_5(self):
        self.assertEqual(None, unified_strdate('mbvmvbzmy jktjsqpy'))

    def test_diversity_6(self):
        self.assertEqual(None, unified_strdate('whpqkkjh'))

    def test_diversity_7(self):
        self.assertEqual(None, unified_strdate('hdbbz'))

    def test_diversity_8(self):
        self.assertEqual(None, unified_strdate('fjkyywzhn'))

    def test_diversity_9(self):
        self.assertEqual(None, unified_strdate('nrwsjp'))

    def test_diversity_10(self):
        self.assertEqual(None, unified_strdate('nyydprf'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('19851206', unified_strdate('December 6, 1985'))

    def test_diversity_2(self):
        self.assertEqual('20020923', unified_strdate('September 23, 2002'))

    def test_diversity_3(self):
        self.assertEqual('20190728', unified_strdate('July 28, 2019'))

    def test_diversity_4(self):
        self.assertEqual('19900323', unified_strdate('March 23, 1990'))

    def test_diversity_5(self):
        self.assertEqual('20051018', unified_strdate('October 18, 2005'))

    def test_diversity_6(self):
        self.assertEqual('20091028', unified_strdate('October 28, 2009'))

    def test_diversity_7(self):
        self.assertEqual('19980112', unified_strdate('January 12, 1998'))

    def test_diversity_8(self):
        self.assertEqual('19740625', unified_strdate('June 25, 1974'))

    def test_diversity_9(self):
        self.assertEqual('20130702', unified_strdate('July 2, 2013'))

    def test_diversity_10(self):
        self.assertEqual('20081003', unified_strdate('October 3, 2008'))
