import unittest


def _t4p_preprocess_input(mode, dtype, h, w):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    apps = types.ModuleType('keras.applications'); apps.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    data_utils = types.ModuleType('keras.utils.data_utils')
    data_utils.get_file = lambda *a, **k: None
    backend = types.ModuleType('keras.backend')
    backend.image_data_format = lambda: 'channels_last'
    backend.floatx = lambda: 'float32'
    for name, module in [('keras', keras), ('keras.applications', apps),
                         ('keras.utils', utils),
                         ('keras.utils.data_utils', data_utils),
                         ('keras.backend', backend)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'applications', 'imagenet_utils.py')
    spec = importlib.util.spec_from_file_location(
        'keras.applications.imagenet_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.applications.imagenet_utils'] = module
    spec.loader.exec_module(module)
    base = (np.arange(h * w * 3) % 256).reshape(h, w, 3)
    arr = base.astype('int32') if dtype == 'int' else base.astype('float64')
    module.preprocess_input(arr, 'channels_last', mode)
    return 'OK'


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'int', 4, 3))

    def test_diversity_2(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'int', 5, 3))

    def test_diversity_3(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'int', 2, 3))

    def test_diversity_4(self):
        self.assertEqual('OK', _t4p_preprocess_input('caffe', 'int', 6, 2))

    def test_diversity_5(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'int', 2, 4))

    def test_diversity_6(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'int', 4, 3))

    def test_diversity_7(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'int', 5, 4))

    def test_diversity_8(self):
        self.assertEqual('OK', _t4p_preprocess_input('caffe', 'int', 2, 4))

    def test_diversity_9(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'int', 2, 6))

    def test_diversity_10(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'int', 3, 6))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'float', 5, 6))

    def test_diversity_2(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'float', 6, 2))

    def test_diversity_3(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'float', 3, 6))

    def test_diversity_4(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'float', 3, 3))

    def test_diversity_5(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'float', 4, 6))

    def test_diversity_6(self):
        self.assertEqual('OK', _t4p_preprocess_input('caffe', 'float', 3, 3))

    def test_diversity_7(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'float', 6, 3))

    def test_diversity_8(self):
        self.assertEqual('OK', _t4p_preprocess_input('tf', 'float', 3, 4))

    def test_diversity_9(self):
        self.assertEqual('OK', _t4p_preprocess_input('torch', 'float', 5, 2))

    def test_diversity_10(self):
        self.assertEqual('OK', _t4p_preprocess_input('caffe', 'float', 4, 2))
