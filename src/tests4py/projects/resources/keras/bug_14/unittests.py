import unittest


def _t4p_sparse_top_k(mode, seed, n):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    K = types.ModuleType('keras.backend')
    K.mean = lambda x, axis=None: np.mean(x, axis=axis)
    K.cast = lambda x, dtype: np.asarray(x).astype('int32' if dtype == 'int32' else dtype)
    K.max = lambda x, axis=None: np.max(x, axis=axis)
    K.flatten = lambda x: np.asarray(x).flatten()
    def in_top_k(preds, targets, k):
        top_k = np.argsort(-np.asarray(preds))[:, :k]
        t = np.asarray(targets).reshape(-1, 1)
        return np.any(t == top_k, axis=-1)
    K.in_top_k = in_top_k
    losses = types.ModuleType('keras.losses')
    losses.__getattr__ = lambda name: (lambda *a, **k: None)
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    gu = types.ModuleType('keras.utils.generic_utils')
    gu.__getattr__ = lambda name: (lambda *a, **k: None)
    for name, module in [('keras', keras), ('keras.backend', K),
                         ('keras.losses', losses), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'metrics.py')
    spec = importlib.util.spec_from_file_location('keras.metrics', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.metrics'] = module
    spec.loader.exec_module(module)
    perm = np.random.RandomState(seed).permutation(n)
    ypred = np.eye(n)[perm]
    if mode == 'flat':
        y_true = perm
    else:
        y_true = perm.reshape(-1, 1)
    res = module.sparse_top_k_categorical_accuracy(y_true, ypred, 1)
    return repr(float(np.asarray(res)))


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 2277, 7))

    def test_diversity_2(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 3370, 2))

    def test_diversity_3(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 7689, 2))

    def test_diversity_4(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 3805, 5))

    def test_diversity_5(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 5949, 4))

    def test_diversity_6(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 7831, 2))

    def test_diversity_7(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 6049, 2))

    def test_diversity_8(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 1965, 7))

    def test_diversity_9(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 9158, 4))

    def test_diversity_10(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('flat', 571, 2))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 6133, 6))

    def test_diversity_2(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 4975, 8))

    def test_diversity_3(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 6024, 4))

    def test_diversity_4(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 7853, 2))

    def test_diversity_5(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 7849, 3))

    def test_diversity_6(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 2153, 6))

    def test_diversity_7(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 6299, 8))

    def test_diversity_8(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 3233, 3))

    def test_diversity_9(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 1359, 2))

    def test_diversity_10(self):
        self.assertEqual('1.0', _t4p_sparse_top_k('col', 8940, 3))
