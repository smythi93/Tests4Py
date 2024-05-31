import unittest
import numpy
import pandas
from pandas import CategoricalIndex


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        dti = pandas.date_range('1200-2-7', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(None, ci)

    def test_diversity_2(self):
        dti = pandas.date_range('1301-2-2', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_3(self):
        dti = pandas.date_range('1102-2-10', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_4(self):
        dti = pandas.date_range('1443-8-22', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(numpy.nan, ci)

    def test_diversity_5(self):
        dti = pandas.date_range('1143-2-7', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(None, ci)

    def test_diversity_6(self):
        dti = pandas.date_range('1532-8-12', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_7(self):
        dti = pandas.date_range('1267-8-24', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(numpy.nan, ci)

    def test_diversity_8(self):
        dti = pandas.date_range('1071-2-22', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_9(self):
        dti = pandas.date_range('1453-2-17', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(None, ci)

    def test_diversity_10(self):
        dti = pandas.date_range('1342-2-12', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        dti = pandas.date_range('1895-2-7', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(None, ci)

    def test_diversity_2(self):
        dti = pandas.date_range('1882-2-2', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_3(self):
        dti = pandas.date_range('2002-2-10', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_4(self):
        dti = pandas.date_range('1793-8-22', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(numpy.nan, ci)

    def test_diversity_5(self):
        dti = pandas.date_range('1789-2-7', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(None, ci)

    def test_diversity_6(self):
        dti = pandas.date_range('1999-8-12', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_7(self):
        dti = pandas.date_range('1963-8-24', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(numpy.nan, ci)

    def test_diversity_8(self):
        dti = pandas.date_range('2000-2-22', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)

    def test_diversity_9(self):
        dti = pandas.date_range('1895-2-17', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(None, ci)

    def test_diversity_10(self):
        dti = pandas.date_range('1876-2-12', periods=100).insert(0, pandas.NaT)
        ci = CategoricalIndex(dti)
        self.assertIn(pandas.NaT, ci)
