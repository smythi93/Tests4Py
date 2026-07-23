import unittest


def _t4p_from_config_runs(mode, D, out, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.layers import Input, Dense, Reshape, concatenate
    from keras.models import Model
    import keras.backend as K

    K.clear_session()
    try:
        input_shape = (1, D)
        inp = Input(shape=input_shape)
        if mode == "shared":
            A = Dense(D, name="layer_a")
            r1 = Reshape((D,))(inp)
            Aout1 = A(r1)
            r2 = Reshape((D,))(A(inp))
            Aout2 = A(r2)
            c1 = concatenate([Aout2, Aout1])
            output = Dense(out, name="layer_b")(c1)
        else:
            r1 = Reshape((D,))(inp)
            h = Dense(D)(r1)
            output = Dense(out)(h)
        model = Model(inputs=inp, outputs=output)
        x = np.random.RandomState(seed).random_sample((5,) + input_shape)
        model.predict(x)
        config = model.get_config()
        weights = model.get_weights()
        model2 = Model.from_config(config)
        model2.set_weights(weights)
        model2.predict(x)
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_from_config_runs('shared', 12, 2, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_from_config_runs('shared', 8, 3, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_from_config_runs('shared', 10, 2, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_from_config_runs('shared', 6, 4, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_from_config_runs('shared', 14, 2, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_from_config_runs('shared', 9, 5, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_from_config_runs('shared', 7, 3, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_from_config_runs('shared', 16, 2, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_from_config_runs('shared', 11, 4, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_from_config_runs('shared', 13, 3, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_from_config_runs('simple', 12, 2, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_from_config_runs('simple', 8, 3, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_from_config_runs('simple', 10, 2, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_from_config_runs('simple', 6, 4, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_from_config_runs('simple', 14, 2, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_from_config_runs('simple', 9, 5, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_from_config_runs('simple', 7, 3, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_from_config_runs('simple', 16, 2, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_from_config_runs('simple', 11, 4, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_from_config_runs('simple', 13, 3, 19))
