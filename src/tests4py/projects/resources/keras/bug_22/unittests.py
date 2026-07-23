import unittest


def _t4p_masked_seq_builds(mode, units, dim, ts):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K
    from keras import layers
    from keras.models import Model, Sequential

    K.clear_session()
    try:
        inputs = layers.Input(shape=(ts, dim))
        if mode == "masked":
            x = layers.Masking(mask_value=0.0)(inputs)
        else:
            x = inputs
        s = Sequential()
        s.add(layers.Dense(units, input_shape=(dim,)))
        s.add(layers.Activation("relu"))
        x = layers.wrappers.TimeDistributed(s)(x)
        model = Model(inputs=inputs, outputs=x)
        model.compile(optimizer="rmsprop", loss="mse")
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 5, 4, 3))

    def test_diversity_2(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 6, 3, 4))

    def test_diversity_3(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 4, 5, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 3, 4, 5))

    def test_diversity_5(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 7, 2, 3))

    def test_diversity_6(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 5, 6, 4))

    def test_diversity_7(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 8, 3, 2))

    def test_diversity_8(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 4, 4, 6))

    def test_diversity_9(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 6, 5, 3))

    def test_diversity_10(self):
        self.assertTrue(_t4p_masked_seq_builds('masked', 3, 3, 4))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 5, 4, 3))

    def test_diversity_2(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 6, 3, 4))

    def test_diversity_3(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 4, 5, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 3, 4, 5))

    def test_diversity_5(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 7, 2, 3))

    def test_diversity_6(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 5, 6, 4))

    def test_diversity_7(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 8, 3, 2))

    def test_diversity_8(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 4, 4, 6))

    def test_diversity_9(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 6, 5, 3))

    def test_diversity_10(self):
        self.assertTrue(_t4p_masked_seq_builds('nomask', 3, 3, 4))
