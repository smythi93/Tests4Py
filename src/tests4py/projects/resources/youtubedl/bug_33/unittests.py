import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import parse_iso8601


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(1487976446, parse_iso8601('2017-02-25T08:17:26.63351+0930'))

    def test_diversity_2(self):
        self.assertEqual(993642289, parse_iso8601('2001-06-27T14:14:49.13275+0230'))

    def test_diversity_3(self):
        self.assertEqual(1426244410, parse_iso8601('2015-03-13T20:30:10.042+0930'))

    def test_diversity_4(self):
        self.assertEqual(976917066, parse_iso8601('2000-12-15T21:51:06.625946Z'))

    def test_diversity_5(self):
        self.assertEqual(1528829383, parse_iso8601('2018-06-12T09:19:43.949-0930'))

    def test_diversity_6(self):
        self.assertEqual(1513731092, parse_iso8601('2017-12-20T06:21:32.92182+0530'))

    def test_diversity_7(self):
        self.assertEqual(1049886535, parse_iso8601('2003-04-09T11:08:55.055Z'))

    def test_diversity_8(self):
        self.assertEqual(1284299912, parse_iso8601('2010-09-12T13:58:32.0996Z'))

    def test_diversity_9(self):
        self.assertEqual(1315083531, parse_iso8601('2011-09-03T20:58:51.245Z'))

    def test_diversity_10(self):
        self.assertEqual(1095717849, parse_iso8601('2004-09-20T19:04:09.582466-0300'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(1474626293, parse_iso8601('2016-09-23T12:54:53+0230'))

    def test_diversity_2(self):
        self.assertEqual(991590533, parse_iso8601('2001-06-03T11:48:53-0600'))

    def test_diversity_3(self):
        self.assertEqual(1570097679, parse_iso8601('2019-10-03T10:14:39Z'))

    def test_diversity_4(self):
        self.assertEqual(1316781451, parse_iso8601('2011-09-23T12:37:31Z'))

    def test_diversity_5(self):
        self.assertEqual(967240398, parse_iso8601('2000-08-26T02:53:18+0500'))

    def test_diversity_6(self):
        self.assertEqual(1448482544, parse_iso8601('2015-11-25T20:15:44Z'))

    def test_diversity_7(self):
        self.assertEqual(1318425064, parse_iso8601('2011-10-12T13:11:04-0000'))

    def test_diversity_8(self):
        self.assertEqual(1161375369, parse_iso8601('2006-10-20T17:46:09-0230'))

    def test_diversity_9(self):
        self.assertEqual(1606978763, parse_iso8601('2020-12-02T19:29:23-1130'))

    def test_diversity_10(self):
        self.assertEqual(1247570058, parse_iso8601('2009-07-14T11:14:18Z'))
