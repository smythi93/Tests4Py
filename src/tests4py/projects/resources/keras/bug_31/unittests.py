import unittest


def _t4p_ctc_runs(batch, T, L, num_classes, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras.backend as K

    K.clear_session()
    try:
        rng = np.random.RandomState(seed)
        y_pred = rng.random_sample((batch, T, num_classes)).astype("float32")
        y_pred = y_pred / y_pred.sum(axis=-1, keepdims=True)
        y_true = rng.randint(0, num_classes - 1, size=(batch, L)).astype("float32")
        input_length = np.full((batch, 1), T, dtype="float32")
        label_length = np.full((batch, 1), L, dtype="float32")
        cost = K.ctc_batch_cost(
            K.variable(y_true),
            K.variable(y_pred),
            K.variable(input_length),
            K.variable(label_length),
        )
        c = np.asarray(K.eval(cost))
        return c.shape == (batch, 1) and bool(np.all(np.isfinite(c)))
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_ctc_runs(1, 6, 2, 5, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_ctc_runs(1, 7, 3, 6, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_ctc_runs(1, 8, 2, 4, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_ctc_runs(1, 5, 2, 5, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_ctc_runs(1, 9, 4, 7, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_ctc_runs(1, 6, 3, 6, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_ctc_runs(1, 10, 2, 5, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_ctc_runs(1, 7, 2, 4, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_ctc_runs(1, 8, 3, 6, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_ctc_runs(1, 6, 2, 7, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_ctc_runs(2, 6, 2, 5, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_ctc_runs(3, 7, 3, 6, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_ctc_runs(2, 8, 2, 4, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_ctc_runs(4, 5, 2, 5, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_ctc_runs(2, 9, 4, 7, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_ctc_runs(3, 6, 3, 6, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_ctc_runs(2, 10, 2, 5, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_ctc_runs(5, 7, 2, 4, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_ctc_runs(2, 8, 3, 6, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_ctc_runs(3, 6, 2, 7, 19))
