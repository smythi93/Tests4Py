import unittest
from pandas.core.series import Series
from pandas import period_range
from pandas import date_range
from pandas import Timedelta
from pandas._testing import assert_index_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2014')
        series = Series(1, index=index, name='udSjkkLeglNBu')
        exp_index = date_range('1/1/2001', end='1/1/2014', freq='D')
        result = series.to_timestamp(how='end')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('udSjkkLeglNBu', result.name)

    def test_diversity_2(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2086')
        series = Series(1, index=index, name='SsEGIwAqSNDXVHk')
        exp_index = date_range('1/1/2001', end='1/1/2086', freq='D')
        result = series.to_timestamp(how='end')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('SsEGIwAqSNDXVHk', result.name)

    def test_diversity_3(self):
        index = period_range(freq='A', start='1/1/2001', end='1/1/2085')
        series = Series(1, index=index, name='BgdxgADcajJgR')
        exp_index = date_range('1/1/2001', end='1/1/2085', freq='A')
        result = series.to_timestamp(how='end')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('BgdxgADcajJgR', result.name)

    def test_diversity_4(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2033')
        series = Series(1, index=index, name='mNgybXNw')
        exp_index = date_range('1/1/2001', end='1/1/2033', freq='D')
        result = series.to_timestamp(how='end')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('mNgybXNw', result.name)

    def test_diversity_5(self):
        index = period_range(freq='A', start='1/1/2001', end='1/1/2080')
        series = Series(1, index=index, name='HrLMCjs')
        exp_index = date_range('1/1/2001', end='1/1/2080', freq='A')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('HrLMCjs', result.name)

    def test_diversity_6(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2032')
        series = Series(1, index=index, name='BsHIQkLempMba')
        exp_index = date_range('1/1/2001', end='1/1/2032', freq='D')
        result = series.to_timestamp(how='end')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('BsHIQkLempMba', result.name)

    def test_diversity_7(self):
        index = period_range(freq='A', start='1/1/2001', end='1/1/2081')
        series = Series(1, index=index, name='eoIWroeGnV')
        exp_index = date_range('1/1/2001', end='1/1/2081', freq='A')
        result = series.to_timestamp(how='end')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('eoIWroeGnV', result.name)

    def test_diversity_8(self):
        index = period_range(freq='A', start='1/1/2001', end='1/1/2069')
        series = Series(1, index=index, name='aEozDsWBaqS')
        exp_index = date_range('1/1/2001', end='1/1/2069', freq='A')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('aEozDsWBaqS', result.name)

    def test_diversity_9(self):
        index = period_range(freq='A', start='1/1/2001', end='1/1/2086')
        series = Series(1, index=index, name='TFSrUrNdU')
        exp_index = date_range('1/1/2001', end='1/1/2086', freq='A')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('TFSrUrNdU', result.name)

    def test_diversity_10(self):
        index = period_range(freq='A', start='1/1/2001', end='1/1/2038')
        series = Series(1, index=index, name='sUbfsPBeSWBlCU')
        exp_index = date_range('1/1/2001', end='1/1/2038', freq='A')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('sUbfsPBeSWBlCU', result.name)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2014')
        series = Series(1, index=index, name='ryTSlAxEQvH')
        exp_index = date_range('1/1/2001', end='1/1/2014', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('ryTSlAxEQvH', result.name)

    def test_diversity_2(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2012')
        series = Series(1, index=index, name='ftpXpAOR')
        exp_index = date_range('1/1/2001', end='1/1/2012', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('ftpXpAOR', result.name)

    def test_diversity_3(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2076')
        series = Series(1, index=index, name='YmNhURQZ')
        exp_index = date_range('1/1/2001', end='1/1/2076', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('YmNhURQZ', result.name)

    def test_diversity_4(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2056')
        series = Series(1, index=index, name='MhfYwQNAYucTatQ')
        exp_index = date_range('1/1/2001', end='1/1/2056', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('MhfYwQNAYucTatQ', result.name)

    def test_diversity_5(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2044')
        series = Series(1, index=index, name='ZqVLupxVecYjZe')
        exp_index = date_range('1/1/2001', end='1/1/2044', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('ZqVLupxVecYjZe', result.name)

    def test_diversity_6(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2031')
        series = Series(1, index=index, name='PeRpfFgAT')
        exp_index = date_range('1/1/2001', end='1/1/2031', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('PeRpfFgAT', result.name)

    def test_diversity_7(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2082')
        series = Series(1, index=index, name='XWqYlFnm')
        exp_index = date_range('1/1/2001', end='1/1/2082', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('XWqYlFnm', result.name)

    def test_diversity_8(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2060')
        series = Series(1, index=index, name='pJdXWgucBX')
        exp_index = date_range('1/1/2001', end='1/1/2060', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('pJdXWgucBX', result.name)

    def test_diversity_9(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2078')
        series = Series(1, index=index, name='HIdaVjMeb')
        exp_index = date_range('1/1/2001', end='1/1/2078', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('HIdaVjMeb', result.name)

    def test_diversity_10(self):
        index = period_range(freq='D', start='1/1/2001', end='1/1/2017')
        series = Series(1, index=index, name='HuHlQqc')
        exp_index = date_range('1/1/2001', end='1/1/2017', freq='D')
        result = series.to_timestamp(how='start')
        exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
        assert_index_equal(result.index, exp_index)
        self.assertEqual('HuHlQqc', result.name)
