import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unified_timestamp


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(395465586, unified_timestamp('Sun, 14 Jul 1982 03:33:06 +0000'))

    def test_diversity_2(self):
        self.assertEqual(1723583801, unified_timestamp('Tue, 13 Aug 2024 21:16:41 +0000'))

    def test_diversity_3(self):
        self.assertEqual(730507870, unified_timestamp('Fri, 23 Feb 1993 22:51:10 +0000'))

    def test_diversity_4(self):
        self.assertEqual(1872717650, unified_timestamp('Sun, 05 May 2029 23:20:50 +0000'))

    def test_diversity_5(self):
        self.assertEqual(944187913, unified_timestamp('Mon, 03 Dec 1999 02:25:13 +0000'))

    def test_diversity_6(self):
        self.assertEqual(1842916472, unified_timestamp('Sun, 26 May 2028 01:14:32 +0000'))

    def test_diversity_7(self):
        self.assertEqual(219144544, unified_timestamp('Fri, 11 Dec 1976 09:29:04 +0000'))

    def test_diversity_8(self):
        self.assertEqual(541084326, unified_timestamp('Thu, 23 Feb 1987 13:12:06 +0000'))

    def test_diversity_9(self):
        self.assertEqual(440352952, unified_timestamp('Sun, 15 Dec 1983 16:15:52 +0000'))

    def test_diversity_10(self):
        self.assertEqual(766621571, unified_timestamp('Fri, 17 Apr 1994 22:26:11 +0000'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(452345649, unified_timestamp('1984/05/02 11:34:09 +0000'))

    def test_diversity_2(self):
        self.assertEqual(1032170888, unified_timestamp('2002/09/16 10:08:08 +0000'))

    def test_diversity_3(self):
        self.assertEqual(150267214, unified_timestamp('1974/10/06 04:53:34 +0000'))

    def test_diversity_4(self):
        self.assertEqual(187506042, unified_timestamp('1975/12/11 05:00:42 +0000'))

    def test_diversity_5(self):
        self.assertEqual(1390272530, unified_timestamp('2014/01/21 02:48:50 +0000'))

    def test_diversity_6(self):
        self.assertEqual(323529947, unified_timestamp('1980/04/02 13:25:47 +0000'))

    def test_diversity_7(self):
        self.assertEqual(672787499, unified_timestamp('1991/04/27 21:24:59 +0000'))

    def test_diversity_8(self):
        self.assertEqual(1779137899, unified_timestamp('2026/05/18 20:58:19 +0000'))

    def test_diversity_9(self):
        self.assertEqual(898541649, unified_timestamp('1998/06/22 18:54:09 +0000'))

    def test_diversity_10(self):
        self.assertEqual(1725351446, unified_timestamp('2024/09/03 08:17:26 +0000'))
