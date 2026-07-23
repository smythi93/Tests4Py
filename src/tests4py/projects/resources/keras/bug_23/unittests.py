import unittest


def _t4p_nested_seq_runs(mode, inner_units, out_units, indim, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    import keras.backend as K

    K.clear_session()
    try:
        inner = keras.models.Sequential()
        if mode == "deferred":
            inner.add(keras.layers.Dense(inner_units))
        else:
            inner.add(keras.layers.Dense(inner_units, input_shape=(indim,)))
        inner.add(keras.layers.Dense(inner_units))
        model = keras.models.Sequential()
        model.add(inner)
        model.add(keras.layers.Dense(out_units))
        model.compile("sgd", "mse")
        rng = np.random.RandomState(seed)
        model.train_on_batch(
            rng.random_sample((2, indim)), rng.random_sample((2, out_units))
        )
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 3, 5, 4, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 4, 6, 3, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 5, 4, 2, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 2, 7, 5, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 6, 3, 4, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 3, 5, 6, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 4, 4, 3, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 5, 6, 2, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 2, 3, 5, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_nested_seq_runs('deferred', 6, 5, 4, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 3, 5, 4, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 4, 6, 3, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 5, 4, 2, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 2, 7, 5, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 6, 3, 4, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 3, 5, 6, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 4, 4, 3, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 5, 6, 2, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 2, 3, 5, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_nested_seq_runs('explicit', 6, 5, 4, 19))
