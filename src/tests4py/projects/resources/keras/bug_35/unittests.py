import unittest


def _t4p_standardize(mode, seed, n, mult, rescale):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    backend = types.ModuleType('keras.backend')
    backend.image_data_format = lambda: 'channels_last'
    backend.floatx = lambda: 'float32'
    backend.epsilon = lambda: 1e-7
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    du = types.ModuleType('keras.utils.data_utils')
    class Sequence(object):
        pass
    du.Sequence = Sequence
    for name, module in [('keras', keras), ('keras.backend', backend),
                         ('keras.utils', utils), ('keras.utils.data_utils', du)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'preprocessing', 'image.py')
    spec = importlib.util.spec_from_file_location('keras.preprocessing.image', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.preprocessing.image'] = module
    spec.loader.exec_module(module)
    rng = np.random.RandomState(seed)
    x = rng.randint(0, 10, size=(n, 2, 2, 3)).astype('int64')
    if mode == 'pf':
        idg = module.ImageDataGenerator(
            preprocessing_function=lambda a: a * mult, rescale=rescale,
            data_format='channels_last')
    else:
        idg = module.ImageDataGenerator(
            preprocessing_function=None, rescale=rescale,
            data_format='channels_last')
    out = np.asarray(idg.standardize(x))
    return ",".join(str(int(v)) for v in out.ravel())


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('15,0,27,27,0,21,3,0,6,21,15,18,21,27,12,24,21,24,6,9,18,24,12,24', _t4p_standardize('pf', 1482, 2, 4, 3))

    def test_diversity_2(self):
        self.assertEqual('8,0,20,36,16,32,4,16,28,12,12,36', _t4p_standardize('pf', 497, 1, 2, 4))

    def test_diversity_3(self):
        self.assertEqual('12,12,2,0,10,12,0,14,18,16,14,12,6,12,8,0,14,4,16,10,10,14,14,6,10,0,4,8,6,0,4,10,6,2,14,18', _t4p_standardize('pf', 3484, 3, 3, 2))

    def test_diversity_4(self):
        self.assertEqual('9,24,18,6,15,3,24,27,27,21,18,18,15,15,3,6,18,3,15,9,21,21,3,0', _t4p_standardize('pf', 7510, 2, 2, 3))

    def test_diversity_5(self):
        self.assertEqual('3,24,18,18,21,15,24,3,0,24,27,24', _t4p_standardize('pf', 5078, 1, 2, 3))

    def test_diversity_6(self):
        self.assertEqual('16,8,2,0,14,10,8,8,14,0,16,12,4,2,2,16,8,18,12,12,18,14,16,18', _t4p_standardize('pf', 708, 2, 4, 2))

    def test_diversity_7(self):
        self.assertEqual('12,4,0,16,6,8,16,10,4,12,12,4', _t4p_standardize('pf', 6448, 1, 4, 2))

    def test_diversity_8(self):
        self.assertEqual('18,4,16,14,4,2,10,16,4,14,0,16', _t4p_standardize('pf', 7593, 1, 5, 2))

    def test_diversity_9(self):
        self.assertEqual('21,21,9,6,0,18,12,12,21,18,12,3', _t4p_standardize('pf', 5965, 1, 2, 3))

    def test_diversity_10(self):
        self.assertEqual('6,3,12,15,15,15,18,24,6,3,12,3,12,18,18,12,3,6,12,9,27,18,24,24,12,12,9,18,18,15,12,6,21,18,12,0', _t4p_standardize('pf', 303, 3, 3, 3))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('24,8,16,32,24,12,16,32,32,16,4,32,8,4,36,36,24,12,24,32,0,28,28,8,4,16,4,0,4,36,24,8,36,24,0,12', _t4p_standardize('nopf', 4186, 3, 2, 4))

    def test_diversity_2(self):
        self.assertEqual('16,36,20,36,0,16,12,16,36,0,36,24,8,32,36,4,8,4,0,20,12,28,12,0,36,12,28,36,8,8,0,8,28,20,32,28', _t4p_standardize('nopf', 5428, 3, 3, 4))

    def test_diversity_3(self):
        self.assertEqual('27,6,21,15,21,0,6,12,0,9,0,24,3,0,18,18,0,9,6,15,0,18,9,15,24,3,24,15,12,21,3,21,27,12,27,0', _t4p_standardize('nopf', 9271, 3, 4, 3))

    def test_diversity_4(self):
        self.assertEqual('27,3,9,24,3,6,18,21,3,18,15,21,21,12,3,18,24,0,15,9,3,24,27,6', _t4p_standardize('nopf', 3820, 2, 2, 3))

    def test_diversity_5(self):
        self.assertEqual('18,6,18,10,4,10,0,6,2,16,6,8', _t4p_standardize('nopf', 195, 1, 2, 2))

    def test_diversity_6(self):
        self.assertEqual('6,6,16,16,16,12,2,6,14,12,12,0,2,10,6,10,12,0,6,0,18,12,6,8,0,4,14,4,8,14,16,18,6,0,6,4', _t4p_standardize('nopf', 4564, 3, 4, 2))

    def test_diversity_7(self):
        self.assertEqual('28,4,36,16,0,8,20,24,4,0,36,12,0,12,4,36,12,16,36,4,28,36,4,36,20,12,4,0,0,0,28,28,32,24,4,32', _t4p_standardize('nopf', 2388, 3, 5, 4))

    def test_diversity_8(self):
        self.assertEqual('15,6,0,9,24,21,0,3,9,15,6,21,18,6,0,27,18,18,6,27,9,0,6,3,12,3,3,3,9,15,3,6,3,12,18,0', _t4p_standardize('nopf', 7258, 3, 4, 3))

    def test_diversity_9(self):
        self.assertEqual('16,32,24,0,12,4,20,12,16,20,20,32,20,8,8,28,4,12,24,28,0,32,0,12,8,20,36,28,0,24,16,32,8,32,24,8', _t4p_standardize('nopf', 7489, 3, 5, 4))

    def test_diversity_10(self):
        self.assertEqual('8,0,0,0,12,4,18,10,10,4,14,8,10,6,16,8,4,4,12,8,16,16,14,4', _t4p_standardize('nopf', 850, 2, 2, 2))
