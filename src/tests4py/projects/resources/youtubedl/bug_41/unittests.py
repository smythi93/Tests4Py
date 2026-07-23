import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unified_strdate


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('19740907', unified_strdate('1974-09-07'))

    def test_diversity_2(self):
        self.assertEqual('19790112', unified_strdate('1979-01-12'))

    def test_diversity_3(self):
        self.assertEqual('20190217', unified_strdate('2019-02-17'))

    def test_diversity_4(self):
        self.assertEqual('19791110', unified_strdate('1979-11-10'))

    def test_diversity_5(self):
        self.assertEqual('19990114', unified_strdate('1999-01-14'))

    def test_diversity_6(self):
        self.assertEqual('19871126', unified_strdate('1987-11-26'))

    def test_diversity_7(self):
        self.assertEqual('19720309', unified_strdate('1972-03-09'))

    def test_diversity_8(self):
        self.assertEqual('19790528', unified_strdate('1979-05-28'))

    def test_diversity_9(self):
        self.assertEqual('19790802', unified_strdate('1979-08-02'))

    def test_diversity_10(self):
        self.assertEqual('20060725', unified_strdate('2006-07-25'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('19920811', unified_strdate('11 August 1992'))

    def test_diversity_2(self):
        self.assertEqual('19990802', unified_strdate('2 August 1999'))

    def test_diversity_3(self):
        self.assertEqual('20001006', unified_strdate('October 6, 2000'))

    def test_diversity_4(self):
        self.assertEqual('20190927', unified_strdate('September 27, 2019'))

    def test_diversity_5(self):
        self.assertEqual('19870225', unified_strdate('February 25, 1987'))

    def test_diversity_6(self):
        self.assertEqual('19970217', unified_strdate('February 17, 1997'))

    def test_diversity_7(self):
        self.assertEqual('20010727', unified_strdate('27 July 2001'))

    def test_diversity_8(self):
        self.assertEqual('19861107', unified_strdate('November 7, 1986'))

    def test_diversity_9(self):
        self.assertEqual('20141226', unified_strdate('26 December 2014'))

    def test_diversity_10(self):
        self.assertEqual('20070505', unified_strdate('5 May 2007'))
