import unittest


def _t4p_sepconv1d_runs(strides, filters, numstep, stacksize, batch, df):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    from keras.layers import SeparableConv1D, Input
    from keras.models import Model

    data_format = "channels_last" if df == "last" else "channels_first"
    keras.backend.clear_session()
    try:
        if df == "last":
            inp = Input((numstep, stacksize))
            x = np.random.random((batch, numstep, stacksize))
        else:
            inp = Input((stacksize, numstep))
            x = np.random.random((batch, stacksize, numstep))
        layer = SeparableConv1D(
            filters, 3, strides=strides, padding="valid", data_format=data_format
        )
        model = Model(inp, layer(inp))
        model.predict(x)
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_sepconv1d_runs(2, 6, 9, 3, 2, 'last'))

    def test_diversity_2(self):
        self.assertTrue(_t4p_sepconv1d_runs(3, 6, 9, 3, 2, 'last'))

    def test_diversity_3(self):
        self.assertTrue(_t4p_sepconv1d_runs(2, 4, 8, 2, 2, 'last'))

    def test_diversity_4(self):
        self.assertTrue(_t4p_sepconv1d_runs(2, 6, 9, 3, 2, 'first'))

    def test_diversity_5(self):
        self.assertTrue(_t4p_sepconv1d_runs(3, 5, 10, 3, 2, 'first'))

    def test_diversity_6(self):
        self.assertTrue(_t4p_sepconv1d_runs(2, 8, 7, 4, 3, 'last'))

    def test_diversity_7(self):
        self.assertTrue(_t4p_sepconv1d_runs(3, 6, 12, 3, 2, 'last'))

    def test_diversity_8(self):
        self.assertTrue(_t4p_sepconv1d_runs(2, 5, 9, 3, 2, 'first'))

    def test_diversity_9(self):
        self.assertTrue(_t4p_sepconv1d_runs(2, 6, 11, 2, 2, 'last'))

    def test_diversity_10(self):
        self.assertTrue(_t4p_sepconv1d_runs(3, 7, 8, 3, 2, 'first'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 6, 9, 3, 2, 'last'))

    def test_diversity_2(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 6, 9, 3, 2, 'first'))

    def test_diversity_3(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 4, 8, 2, 2, 'last'))

    def test_diversity_4(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 5, 10, 3, 2, 'first'))

    def test_diversity_5(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 8, 7, 4, 3, 'last'))

    def test_diversity_6(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 6, 12, 3, 2, 'last'))

    def test_diversity_7(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 5, 9, 3, 2, 'first'))

    def test_diversity_8(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 6, 11, 2, 2, 'last'))

    def test_diversity_9(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 7, 8, 3, 2, 'first'))

    def test_diversity_10(self):
        self.assertTrue(_t4p_sepconv1d_runs(1, 3, 9, 3, 2, 'last'))
