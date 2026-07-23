import unittest


def _t4p_datatensor_eval_runs(mode, D, units, n, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import tensorflow as tf
    from keras.layers import Input, Dense, Dropout
    from keras.models import Model
    import keras.backend as K

    K.clear_session()
    rng = np.random.RandomState(seed)
    try:
        if mode == "datatensor":
            data = rng.random_sample((n, D)).astype("float32")
            a = Input(tensor=tf.Variable(data, dtype=tf.float32))
            a2 = Dense(units, name="d1")(a)
            a2 = Dropout(0.5)(a2)
            model = Model(a, a2)
            model.add_loss(K.mean(a2))
            model.compile(optimizer="rmsprop", loss=None, metrics=["mse"])

            def gen():
                while True:
                    yield (None, None)

            model.evaluate_generator(gen(), steps=3)
            model.predict_generator(gen(), steps=3)
        else:
            a = Input(shape=(D,))
            out = Dense(units)(a)
            model = Model(a, out)
            model.compile("rmsprop", "mse", metrics=["mse"])

            def gen():
                while True:
                    yield (rng.random_sample((5, D)), rng.random_sample((5, units)))

            model.evaluate_generator(gen(), steps=3)
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 3, 4, 10, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 4, 5, 8, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 5, 3, 12, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 2, 6, 9, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 6, 4, 7, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 3, 5, 11, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 4, 3, 6, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 5, 6, 10, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 2, 4, 8, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_datatensor_eval_runs('datatensor', 6, 5, 9, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 3, 4, 10, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 4, 5, 8, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 5, 3, 12, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 2, 6, 9, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 6, 4, 7, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 3, 5, 11, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 4, 3, 6, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 5, 6, 10, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 2, 4, 8, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_datatensor_eval_runs('normal', 6, 5, 9, 19))
