import unittest


def _t4p_standardize_weights(mode, seed, n, C):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend')
    for a in ['is_tensor', 'int_shape', 'floatx']:
        setattr(backend, a, lambda *x, **k: None)
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
    rng = np.random.RandomState(seed)
    y = rng.randint(0, C, size=n)
    sw = rng.randint(1, 6, size=n)
    cw = {c: int(rng.randint(2, 6)) for c in range(C)}
    if mode == 'both':
        r = module.standardize_weights(y, sample_weight=sw, class_weight=cw)
    else:
        r = module.standardize_weights(y, sample_weight=sw, class_weight=None)
    return ",".join(str(int(v)) for v in np.asarray(r).ravel())


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('20,15,15,9', _t4p_standardize_weights('both', 9895, 4, 2))

    def test_diversity_2(self):
        self.assertEqual('9,12,15,6,3,3', _t4p_standardize_weights('both', 6729, 6, 5))

    def test_diversity_3(self):
        self.assertEqual('25,9,2,8', _t4p_standardize_weights('both', 2692, 4, 5))

    def test_diversity_4(self):
        self.assertEqual('6,12,6', _t4p_standardize_weights('both', 3347, 3, 4))

    def test_diversity_5(self):
        self.assertEqual('4,6,12,16,20,6,8', _t4p_standardize_weights('both', 4406, 7, 3))

    def test_diversity_6(self):
        self.assertEqual('10,3,10,5,6,15', _t4p_standardize_weights('both', 6421, 6, 4))

    def test_diversity_7(self):
        self.assertEqual('8,6,6', _t4p_standardize_weights('both', 8496, 3, 2))

    def test_diversity_8(self):
        self.assertEqual('10,10,15,12,10,16,5', _t4p_standardize_weights('both', 8643, 7, 4))

    def test_diversity_9(self):
        self.assertEqual('15,5,12,8', _t4p_standardize_weights('both', 2429, 4, 3))

    def test_diversity_10(self):
        self.assertEqual('6,15,20,20', _t4p_standardize_weights('both', 416, 4, 5))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('3,3,1,5,2,4,2,3', _t4p_standardize_weights('onlysw', 1754, 8, 2))

    def test_diversity_2(self):
        self.assertEqual('2,2,2', _t4p_standardize_weights('onlysw', 459, 3, 2))

    def test_diversity_3(self):
        self.assertEqual('1,5,1,2,3,5,3', _t4p_standardize_weights('onlysw', 9901, 7, 2))

    def test_diversity_4(self):
        self.assertEqual('4,5,5,1', _t4p_standardize_weights('onlysw', 4616, 4, 3))

    def test_diversity_5(self):
        self.assertEqual('3,2,4,5', _t4p_standardize_weights('onlysw', 1031, 4, 4))

    def test_diversity_6(self):
        self.assertEqual('5,4,5,3,5', _t4p_standardize_weights('onlysw', 9321, 5, 3))

    def test_diversity_7(self):
        self.assertEqual('5,5,1,4', _t4p_standardize_weights('onlysw', 8669, 4, 4))

    def test_diversity_8(self):
        self.assertEqual('1,1,4,2,5', _t4p_standardize_weights('onlysw', 2295, 5, 2))

    def test_diversity_9(self):
        self.assertEqual('2,3,5,1,5,5', _t4p_standardize_weights('onlysw', 7874, 6, 5))

    def test_diversity_10(self):
        self.assertEqual('3,3,1,3,2', _t4p_standardize_weights('onlysw', 652, 5, 3))
