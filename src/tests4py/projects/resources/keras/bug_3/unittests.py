import unittest


def _t4p_clone_runs(mode, dim, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    import keras.backend as K

    K.clear_session()
    try:
        input_layer = keras.Input(shape=(dim,))
        if mode == "multi":
            layer1 = keras.layers.Lambda(lambda x: [x + 1, x], lambda s: [s, s])
            x_a, x_b = layer1(input_layer)

            class SwapLayer(keras.layers.Layer):
                def call(self, inputs, **kwargs):
                    return [inputs[1], inputs[0]]

                def compute_output_shape(self, s):
                    return [s[1], s[0]]

            x_a, x_b = SwapLayer()([x_a, x_b])
            model = keras.Model(inputs=[input_layer], outputs=[x_a, x_b])
        else:
            out = keras.layers.Dense(dim)(input_layer)
            model = keras.Model(inputs=[input_layer], outputs=[out])
        new_model = keras.models.clone_model(model)
        x = np.random.RandomState(seed).random_sample((6, dim))
        new_model.predict(x)
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_clone_runs('multi', 4, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_clone_runs('multi', 5, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_clone_runs('multi', 3, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_clone_runs('multi', 6, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_clone_runs('multi', 4, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_clone_runs('multi', 7, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_clone_runs('multi', 5, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_clone_runs('multi', 3, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_clone_runs('multi', 8, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_clone_runs('multi', 6, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_clone_runs('single', 4, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_clone_runs('single', 5, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_clone_runs('single', 3, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_clone_runs('single', 6, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_clone_runs('single', 4, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_clone_runs('single', 7, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_clone_runs('single', 5, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_clone_runs('single', 3, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_clone_runs('single', 8, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_clone_runs('single', 6, 19))
