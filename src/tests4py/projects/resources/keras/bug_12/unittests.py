import unittest
import numpy as np
from keras import backend as K, metrics


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        y_a = K.variable(np.random.randint(0, 115.0, (6, 3, 1)), dtype=K.floatx())
        y_b_shape = (6, 3, 1) + (115.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_2(self):
        y_a = K.variable(np.random.randint(0, 989.0, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (989.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_3(self):
        y_a = K.variable(np.random.randint(0, 344.0, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (344.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_4(self):
        y_a = K.variable(np.random.randint(0, 431.0, (6, 3, 1)), dtype=K.floatx())
        y_b_shape = (6, 3, 1) + (431.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_5(self):
        y_a = K.variable(np.random.randint(0, 965.0, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (965.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_6(self):
        y_a = K.variable(np.random.randint(0, 663.0, (6, 3)), dtype=K.floatx())
        y_b_shape = (6, 3) + (663.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_7(self):
        y_a = K.variable(np.random.randint(0, 176.0, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (176.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_8(self):
        y_a = K.variable(np.random.randint(0, 243.0, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (243.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_9(self):
        y_a = K.variable(np.random.randint(0, 773.0, (6, 3)), dtype=K.floatx())
        y_b_shape = (6, 3) + (773.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_10(self):
        y_a = K.variable(np.random.randint(0, 813.0, (6, 3, 1)), dtype=K.floatx())
        y_b_shape = (6, 3, 1) + (813.0,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        y_a = K.variable(np.random.randint(0, 772, (6, 3)), dtype=K.floatx())
        y_b_shape = (6, 3) + (772,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_2(self):
        y_a = K.variable(np.random.randint(0, 496, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (496,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_3(self):
        y_a = K.variable(np.random.randint(0, 875, (6, 3)), dtype=K.floatx())
        y_b_shape = (6, 3) + (875,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_4(self):
        y_a = K.variable(np.random.randint(0, 669, (6, 3, 1)), dtype=K.floatx())
        y_b_shape = (6, 3, 1) + (669,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_5(self):
        y_a = K.variable(np.random.randint(0, 518, (6, 3)), dtype=K.floatx())
        y_b_shape = (6, 3) + (518,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_6(self):
        y_a = K.variable(np.random.randint(0, 96, (6, 3, 1)), dtype=K.floatx())
        y_b_shape = (6, 3, 1) + (96,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_7(self):
        y_a = K.variable(np.random.randint(0, 704, (6, 3, 1)), dtype=K.floatx())
        y_b_shape = (6, 3, 1) + (704,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_8(self):
        y_a = K.variable(np.random.randint(0, 55, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (55,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_9(self):
        y_a = K.variable(np.random.randint(0, 715, (6, 3)), dtype=K.floatx())
        y_b_shape = (6, 3) + (715,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))

    def test_diversity_10(self):
        y_a = K.variable(np.random.randint(0, 143, (6,)), dtype=K.floatx())
        y_b_shape = (6,) + (143,)
        y_b = K.variable(np.random.random(y_b_shape), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        assert np.allclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc))
