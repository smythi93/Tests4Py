import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unified_strdate


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('20030810', unified_strdate('10/08/2003 08:07:49'))

    def test_diversity_2(self):
        self.assertEqual('19810714', unified_strdate('14/07/1981 03:33:06'))

    def test_diversity_3(self):
        self.assertEqual('20010727', unified_strdate('27/07/2001 21:16:41'))

    def test_diversity_4(self):
        self.assertEqual('19820604', unified_strdate('04/06/1982 22:44:51'))

    def test_diversity_5(self):
        self.assertEqual('19801009', unified_strdate('09/10/1980 04:54:53'))

    def test_diversity_6(self):
        self.assertEqual('20160626', unified_strdate('26/06/2016 14:46:04'))

    def test_diversity_7(self):
        self.assertEqual('19750707', unified_strdate('07/07/1975 01:57:18'))

    def test_diversity_8(self):
        self.assertEqual('19720417', unified_strdate('17/04/1972 02:50:59'))

    def test_diversity_9(self):
        self.assertEqual('20140610', unified_strdate('10/06/2014 14:04:37'))

    def test_diversity_10(self):
        self.assertEqual('19860223', unified_strdate('23/02/1986 13:12:06'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('19950423', unified_strdate('April 23, 1995'))

    def test_diversity_2(self):
        self.assertEqual('19990908', unified_strdate('September 8, 1999'))

    def test_diversity_3(self):
        self.assertEqual('19930417', unified_strdate('April 17, 1993'))

    def test_diversity_4(self):
        self.assertEqual('19960319', unified_strdate('1996/03/19 01:52:22'))

    def test_diversity_5(self):
        self.assertEqual('20040316', unified_strdate('March 16, 2004'))

    def test_diversity_6(self):
        self.assertEqual('20050811', unified_strdate('2005/08/11 01:39:10'))

    def test_diversity_7(self):
        self.assertEqual('19790903', unified_strdate('September 3, 1979'))

    def test_diversity_8(self):
        self.assertEqual('19800122', unified_strdate('January 22, 1980'))

    def test_diversity_9(self):
        self.assertEqual('20100225', unified_strdate('February 25, 2010'))

    def test_diversity_10(self):
        self.assertEqual('19830114', unified_strdate('1983/01/14 10:13:52'))
