import unittest


def _t4p_lstm_runs(units, ts, emb, batch, use_bias):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras import backend as K
    from keras.layers import LSTM, Input
    from keras.models import Model

    K.clear_session()
    try:
        inp = Input((ts, emb))
        out = LSTM(units, implementation=1, use_bias=use_bias)(inp)
        model = Model(inp, out)
        y = model.predict(np.random.random((batch, ts, emb)))
        return tuple(y.shape) == (batch, units)
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_lstm_runs(3, 5, 4, 2, False))

    def test_diversity_2(self):
        self.assertTrue(_t4p_lstm_runs(4, 6, 3, 2, False))

    def test_diversity_3(self):
        self.assertTrue(_t4p_lstm_runs(5, 4, 6, 3, False))

    def test_diversity_4(self):
        self.assertTrue(_t4p_lstm_runs(2, 7, 5, 2, False))

    def test_diversity_5(self):
        self.assertTrue(_t4p_lstm_runs(6, 3, 4, 2, False))

    def test_diversity_6(self):
        self.assertTrue(_t4p_lstm_runs(4, 5, 7, 3, False))

    def test_diversity_7(self):
        self.assertTrue(_t4p_lstm_runs(3, 6, 3, 2, False))

    def test_diversity_8(self):
        self.assertTrue(_t4p_lstm_runs(5, 5, 5, 2, False))

    def test_diversity_9(self):
        self.assertTrue(_t4p_lstm_runs(2, 4, 8, 3, False))

    def test_diversity_10(self):
        self.assertTrue(_t4p_lstm_runs(6, 7, 2, 2, False))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_lstm_runs(3, 5, 4, 2, True))

    def test_diversity_2(self):
        self.assertTrue(_t4p_lstm_runs(4, 6, 3, 2, True))

    def test_diversity_3(self):
        self.assertTrue(_t4p_lstm_runs(5, 4, 6, 3, True))

    def test_diversity_4(self):
        self.assertTrue(_t4p_lstm_runs(2, 7, 5, 2, True))

    def test_diversity_5(self):
        self.assertTrue(_t4p_lstm_runs(6, 3, 4, 2, True))

    def test_diversity_6(self):
        self.assertTrue(_t4p_lstm_runs(4, 5, 7, 3, True))

    def test_diversity_7(self):
        self.assertTrue(_t4p_lstm_runs(3, 6, 3, 2, True))

    def test_diversity_8(self):
        self.assertTrue(_t4p_lstm_runs(5, 5, 5, 2, True))

    def test_diversity_9(self):
        self.assertTrue(_t4p_lstm_runs(2, 4, 8, 3, True))

    def test_diversity_10(self):
        self.assertTrue(_t4p_lstm_runs(6, 7, 2, 2, True))
