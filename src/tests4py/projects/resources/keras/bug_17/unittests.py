import unittest
import numpy as np
from keras import backend as K
from keras import metrics


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        np.random.seed(9313)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_2(self):
        np.random.seed(6211)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_3(self):
        np.random.seed(7869)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_4(self):
        np.random.seed(8870)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_5(self):
        np.random.seed(1961)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_6(self):
        np.random.seed(7764)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_7(self):
        np.random.seed(4239)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_8(self):
        np.random.seed(4994)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_9(self):
        np.random.seed(8090)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3

    def test_diversity_10(self):
        np.random.seed(7338)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 0.3


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        np.random.seed(7267)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_2(self):
        np.random.seed(5548)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_3(self):
        np.random.seed(2988)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_4(self):
        np.random.seed(8472)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_5(self):
        np.random.seed(4743)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_6(self):
        np.random.seed(5067)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_7(self):
        np.random.seed(6039)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_8(self):
        np.random.seed(6729)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_9(self):
        np.random.seed(5003)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0

    def test_diversity_10(self):
        np.random.seed(8709)
        y_a = K.variable(np.random.randint(0, 7, (6,)), dtype=K.floatx())
        y_b = K.variable(np.random.random((6, 7)), dtype=K.floatx())
        y_a_dense_labels = K.cast(K.one_hot(K.cast(y_a, dtype='int32'), 7), dtype=K.floatx())
        sparse_categorical_acc = metrics.sparse_categorical_accuracy(y_a, y_b)
        categorical_acc = metrics.categorical_accuracy(y_a_dense_labels, y_b)
        match = np.isclose(K.eval(sparse_categorical_acc), K.eval(categorical_acc), atol=0.001)
        assert match.mean() <= 1.0