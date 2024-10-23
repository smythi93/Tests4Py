import unittest
import pandas
from pandas._testing import assert_index_equal
from datetime import timedelta


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        index = pandas.date_range('1/1/2000', periods=3232, freq='R')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_2(self):
        index = pandas.date_range('1/1/2000', periods=9827, freq='P')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_3(self):
        index = pandas.date_range('1/1/2000', periods=43, freq='R')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_4(self):
        index = pandas.date_range('1/1/2000', periods=1111, freq='P')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_5(self):
        index = pandas.date_range('1/1/2000', periods=54, freq='R')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_6(self):
        index = pandas.date_range('1/1/2000', periods=32, freq='P')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_7(self):
        index = pandas.date_range('1/1/2000', periods=54, freq='R')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_8(self):
        index = pandas.date_range('1/1/2000', periods=6712, freq='P')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_9(self):
        index = pandas.date_range('1/1/2000', periods=6090, freq='R')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_10(self):
        index = pandas.date_range('1/1/2000', periods=9827, freq='P')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        index = pandas.date_range('1/1/2000', periods=9711, freq='D')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_2(self):
        index = pandas.date_range('1/1/2000', periods=8345, freq='D')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_3(self):
        index = pandas.date_range('1/1/2000', periods=86, freq='B')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_4(self):
        index = pandas.date_range('1/1/2000', periods=362, freq='D')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_5(self):
        index = pandas.date_range('1/1/2000', periods=123, freq='B')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_6(self):
        index = pandas.date_range('1/1/2000', periods=30, freq='D')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_7(self):
        index = pandas.date_range('1/1/2000', periods=400, freq='B')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_8(self):
        index = pandas.date_range('1/1/2000', periods=993, freq='B')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_9(self):
        index = pandas.date_range('1/1/2000', periods=886, freq='D')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))

    def test_diversity_10(self):
        index = pandas.date_range('1/1/2000', periods=12, freq='D')
        shifted = index + timedelta(1)
        back = shifted + timedelta(-1)
        back = back._with_freq('infer')
        self.assertEqual(None, assert_index_equal(index, back))
