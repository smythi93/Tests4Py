import unittest


def _t4p_numpy_backend(mode, seed, n, c, k):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend'); backend.__path__ = []
    common = types.ModuleType('keras.backend.common')
    common.floatx = lambda: 'float32'
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    utils.to_categorical = lambda *a, **k: None
    gu = types.ModuleType('keras.utils.generic_utils')
    gu.transpose_shape = lambda *a, **k: None
    for name, module in [('keras', keras), ('keras.backend', backend),
                         ('keras.backend.common', common), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'backend', 'numpy_backend.py')
    spec = importlib.util.spec_from_file_location('keras.backend.numpy_backend', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.backend.numpy_backend'] = module
    spec.loader.exec_module(module)
    if mode == 'topk':
        rng = np.random.RandomState(seed)
        preds = np.stack([rng.permutation(c) for _ in range(n)]).astype('float32')
        targets = rng.randint(0, c, size=n)
        r = np.asarray(module.in_top_k(preds, targets, k))
    else:
        rng = np.random.RandomState(seed)
        a = rng.randint(0, 100, size=n)
        b = rng.randint(0, 100, size=n)
        r = np.asarray(module.greater(a, b))
    return "".join('1' if x else '0' for x in r.astype(bool).ravel())


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('10111010', _t4p_numpy_backend('topk', 6316, 8, 6, 4))

    def test_diversity_2(self):
        self.assertEqual('0110', _t4p_numpy_backend('topk', 3245, 4, 8, 4))

    def test_diversity_3(self):
        self.assertEqual('111011', _t4p_numpy_backend('topk', 920, 6, 6, 4))

    def test_diversity_4(self):
        self.assertEqual('0011101', _t4p_numpy_backend('topk', 591, 7, 5, 2))

    def test_diversity_5(self):
        self.assertEqual('010001', _t4p_numpy_backend('topk', 3890, 6, 8, 5))

    def test_diversity_6(self):
        self.assertEqual('1001', _t4p_numpy_backend('topk', 8568, 4, 6, 3))

    def test_diversity_7(self):
        self.assertEqual('1001', _t4p_numpy_backend('topk', 7800, 4, 6, 4))

    def test_diversity_8(self):
        self.assertEqual('1110010', _t4p_numpy_backend('topk', 602, 7, 4, 2))

    def test_diversity_9(self):
        self.assertEqual('010010', _t4p_numpy_backend('topk', 7322, 6, 6, 3))

    def test_diversity_10(self):
        self.assertEqual('1011', _t4p_numpy_backend('topk', 751, 4, 8, 7))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('111', _t4p_numpy_backend('greater', 1636, 3, 6, 3))

    def test_diversity_2(self):
        self.assertEqual('0101', _t4p_numpy_backend('greater', 190, 4, 4, 1))

    def test_diversity_3(self):
        self.assertEqual('01010', _t4p_numpy_backend('greater', 2044, 5, 4, 1))

    def test_diversity_4(self):
        self.assertEqual('000110', _t4p_numpy_backend('greater', 3244, 6, 4, 2))

    def test_diversity_5(self):
        self.assertEqual('0011', _t4p_numpy_backend('greater', 5745, 4, 5, 3))

    def test_diversity_6(self):
        self.assertEqual('110111', _t4p_numpy_backend('greater', 5511, 6, 4, 2))

    def test_diversity_7(self):
        self.assertEqual('1010101', _t4p_numpy_backend('greater', 940, 7, 4, 2))

    def test_diversity_8(self):
        self.assertEqual('1011001', _t4p_numpy_backend('greater', 6414, 7, 7, 3))

    def test_diversity_9(self):
        self.assertEqual('100111', _t4p_numpy_backend('greater', 5725, 6, 4, 1))

    def test_diversity_10(self):
        self.assertEqual('10011', _t4p_numpy_backend('greater', 9104, 5, 5, 1))
