import unittest
import numpy as np
from keras import metrics
from keras import backend as K


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1997))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_2(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=4750))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_3(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1108))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_4(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=3280))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_5(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=273))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_6(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2560))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_7(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1770))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_8(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=3292))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_9(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2950))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_10(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2673))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 0.5
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=3919))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_2(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=722))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_3(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1251))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_4(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=4933))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_5(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=4478))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_6(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=4529))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_7(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2828))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_8(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=4182))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_9(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1725))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0

    def test_diversity_10(self):
        y_pred = K.variable(np.array([[0.3, 0.2, 0.1], [0.1, 0.2, 0.7]]))
        y_true = K.variable(np.array([[0, 1, 0], [1, 0, 0]]))
        success_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2389))
        assert success_result == 1
        partial_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=2))
        assert partial_result == 1.0
        failure_result = K.eval(metrics.sparse_top_k_categorical_accuracy(y_true, y_pred, k=1))
        assert failure_result == 0
