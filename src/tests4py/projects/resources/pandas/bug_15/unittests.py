import unittest
from pandas._testing import assert_index_equal, round_trip_pickle
from pandas import date_range


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        dti = date_range('18760322', periods=963, tz='UTC', name='LoqOncCI')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_2(self):
        dti = date_range('21510108', periods=328, tz='UTC', name='JAfoggbBzzdCaxw')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_3(self):
        dti = date_range('18930920', periods=116, tz='US/Eastern', name='fJLUYDPNzsQ')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_4(self):
        dti = date_range('18521206', periods=790, tz='US/Eastern', name='KIVjMRxRbDvtn')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_5(self):
        dti = date_range('20740827', periods=938, tz='dateutil/US/Pacific', name='ZLwphwwicBepLEO')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_6(self):
        dti = date_range('19420725', periods=698, tz='US/Eastern', name='DWsGNUzQMG')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_7(self):
        dti = date_range('18480106', periods=836, tz='UTC', name='PtBjVNyGvg')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_8(self):
        dti = date_range('18170317', periods=132, tz='UTC', name='AGCEdFAKkra')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_9(self):
        dti = date_range('18361002', periods=540, tz='UTC', name='GoCTgMC')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_10(self):
        dti = date_range('21730218', periods=785, tz='dateutil/US/Pacific', name='PqDhyiVjn')
        dti = dti._with_freq(None)
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        dti = date_range('19320212', periods=799, tz='UTC', name='iFvTevHJZBydGI')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_2(self):
        dti = date_range('21660402', periods=905, tz='Asia/Tokyo', name='hKuMegzU')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_3(self):
        dti = date_range('21430215', periods=100, tz='dateutil/Asia/Singapore', name='SsFxxEyUs')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_4(self):
        dti = date_range('18041206', periods=652, tz='dateutil/US/Pacific', name='vPyFYXX')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_5(self):
        dti = date_range('19820112', periods=284, tz='Asia/Tokyo', name='pVQNOduQPGiAt')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_6(self):
        dti = date_range('20750315', periods=364, tz='dateutil/US/Pacific', name='TZyXZWlqrJO')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_7(self):
        dti = date_range('21141027', periods=610, tz='UTC', name='WxVRjdlzAtYEzO')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_8(self):
        dti = date_range('19430301', periods=499, tz='US/Eastern', name='UgQcmKffqFiOQc')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_9(self):
        dti = date_range('19810308', periods=818, tz='dateutil/Asia/Singapore', name='GAdXxdOvKmhH')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))

    def test_diversity_10(self):
        dti = date_range('20750618', periods=632, tz='dateutil/US/Pacific', name='wcFlkZcf')
        dti = dti._with_freq('infer')
        res = round_trip_pickle(dti)
        self.assertEqual(None, assert_index_equal(res, dti))
