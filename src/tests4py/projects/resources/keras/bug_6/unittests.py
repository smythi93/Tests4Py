import unittest


def _t4p_weighted_masked(mode, seed, n, m):
    import os
    import sys
    import types
    import warnings
    import importlib.util
    import numpy as np
    warnings.filterwarnings('ignore')
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend')
    backend.floatx = lambda: 'float32'
    backend.epsilon = lambda: 1e-7
    backend.cast = lambda x, dtype: np.asarray(x).astype(dtype)
    backend.mean = lambda x, axis=None: np.mean(x, axis=axis)
    backend.ndim = lambda x: np.asarray(x).ndim
    backend.not_equal = lambda x, y: np.asarray(x) != y
    backend.is_tensor = lambda x: False
    backend.int_shape = lambda x: None
    losses = types.ModuleType('keras.losses')
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    class Sequence(object):
        pass
    utils.Sequence = Sequence
    gu = types.ModuleType('keras.utils.generic_utils')
    gu.to_list = lambda x: x if isinstance(x, list) else [x]
    for name, module in [('keras', keras), ('keras.backend', backend),
                         ('keras.losses', losses), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'engine', 'training_utils.py')
    spec = importlib.util.spec_from_file_location('keras.engine.training_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.engine.training_utils'] = module
    spec.loader.exec_module(module)
    fn = lambda yt, yp: (yp - yt) ** 2
    weighted = module.weighted_masked_objective(fn)
    rng = np.random.RandomState(seed)
    yt = rng.randint(0, 10, size=(n, m)).astype('float64')
    yp = rng.randint(0, 10, size=(n, m)).astype('float64')
    if mode == 'mask0':
        mask = np.zeros((n, m))
        res = weighted(yt, yp, None, mask)
    else:
        res = weighted(yt, yp, None, None)
    return repr(float(res))


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 924, 4, 5))

    def test_diversity_2(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 5738, 3, 5))

    def test_diversity_3(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 7776, 5, 3))

    def test_diversity_4(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 2944, 4, 2))

    def test_diversity_5(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 5452, 5, 4))

    def test_diversity_6(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 1592, 5, 2))

    def test_diversity_7(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 6801, 2, 5))

    def test_diversity_8(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 3512, 2, 3))

    def test_diversity_9(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 2355, 5, 5))

    def test_diversity_10(self):
        self.assertEqual('0.0', _t4p_weighted_masked('mask0', 5305, 3, 5))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('6.75', _t4p_weighted_masked('nomask', 9434, 2, 2))

    def test_diversity_2(self):
        self.assertEqual('5.9', _t4p_weighted_masked('nomask', 2917, 5, 2))

    def test_diversity_3(self):
        self.assertEqual('12.75', _t4p_weighted_masked('nomask', 5957, 4, 2))

    def test_diversity_4(self):
        self.assertEqual('13.75', _t4p_weighted_masked('nomask', 5886, 2, 2))

    def test_diversity_5(self):
        self.assertEqual('19.416666666666668', _t4p_weighted_masked('nomask', 5314, 4, 3))

    def test_diversity_6(self):
        self.assertEqual('4.25', _t4p_weighted_masked('nomask', 5321, 4, 3))

    def test_diversity_7(self):
        self.assertEqual('13.583333333333334', _t4p_weighted_masked('nomask', 8164, 3, 4))

    def test_diversity_8(self):
        self.assertEqual('19.72', _t4p_weighted_masked('nomask', 1559, 5, 5))

    def test_diversity_9(self):
        self.assertEqual('9.75', _t4p_weighted_masked('nomask', 8225, 2, 2))

    def test_diversity_10(self):
        self.assertEqual('10.0', _t4p_weighted_masked('nomask', 918, 2, 5))
