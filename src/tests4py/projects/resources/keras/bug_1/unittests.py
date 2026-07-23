import unittest


def _t4p_init(name, seed, rows, cols):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras.backend as K
    from keras import initializers

    mapping = {
        "uniform": "RandomUniform",
        "normal": "RandomNormal",
        "truncated": "TruncatedNormal",
        "varscale": "VarianceScaling",
    }
    init = getattr(initializers, mapping[name])(seed=seed)
    a = np.asarray(K.eval(init((rows, cols))))
    b = np.asarray(K.eval(init((rows, cols))))
    return a, b


def _t4p_init_diff(name, seed, rows, cols):
    a, b = _t4p_init(name, seed, rows, cols)
    return not np.allclose(a, b)


def _t4p_init_shape(name, seed, rows, cols):
    a, _ = _t4p_init(name, seed, rows, cols)
    return tuple(a.shape)


import numpy as np


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_init_diff('uniform', 1337, 4, 3))

    def test_diversity_2(self):
        self.assertTrue(_t4p_init_diff('normal', 7, 5, 2))

    def test_diversity_3(self):
        self.assertTrue(_t4p_init_diff('truncated', 42, 3, 3))

    def test_diversity_4(self):
        self.assertTrue(_t4p_init_diff('varscale', 100, 6, 4))

    def test_diversity_5(self):
        self.assertTrue(_t4p_init_diff('uniform', 555, 2, 5))

    def test_diversity_6(self):
        self.assertTrue(_t4p_init_diff('normal', 888, 4, 4))

    def test_diversity_7(self):
        self.assertTrue(_t4p_init_diff('truncated', 271, 5, 5))

    def test_diversity_8(self):
        self.assertTrue(_t4p_init_diff('varscale', 12, 3, 6))

    def test_diversity_9(self):
        self.assertTrue(_t4p_init_diff('uniform', 9001, 7, 2))

    def test_diversity_10(self):
        self.assertTrue(_t4p_init_diff('normal', 314, 2, 8))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual((4, 3), _t4p_init_shape('uniform', 11, 4, 3))

    def test_diversity_2(self):
        self.assertEqual((5, 2), _t4p_init_shape('normal', 22, 5, 2))

    def test_diversity_3(self):
        self.assertEqual((3, 3), _t4p_init_shape('truncated', 33, 3, 3))

    def test_diversity_4(self):
        self.assertEqual((6, 4), _t4p_init_shape('varscale', 44, 6, 4))

    def test_diversity_5(self):
        self.assertEqual((2, 5), _t4p_init_shape('uniform', 55, 2, 5))

    def test_diversity_6(self):
        self.assertEqual((4, 4), _t4p_init_shape('normal', 66, 4, 4))

    def test_diversity_7(self):
        self.assertEqual((5, 5), _t4p_init_shape('truncated', 77, 5, 5))

    def test_diversity_8(self):
        self.assertEqual((3, 6), _t4p_init_shape('varscale', 88, 3, 6))

    def test_diversity_9(self):
        self.assertEqual((7, 2), _t4p_init_shape('uniform', 99, 7, 2))

    def test_diversity_10(self):
        self.assertEqual((2, 8), _t4p_init_shape('normal', 101, 2, 8))
