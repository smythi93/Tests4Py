import unittest


def _t4p_deconv_length(mode, dim, stride, kernel, padding, out_pad, dilation):
    import os
    import sys
    import types
    import importlib.util
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    backend = types.ModuleType('keras.backend')
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.backend', backend)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'conv_utils.py')
    spec = importlib.util.spec_from_file_location('keras.utils.conv_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.utils.conv_utils'] = module
    spec.loader.exec_module(module)
    op = None if out_pad == 'none' else int(out_pad)
    if mode == 'dil':
        return module.deconv_length(dim, stride, kernel, padding, op, dilation)
    return module.deconv_length(dim, stride, kernel, padding, op)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(29, _t4p_deconv_length('dil', 11, 3, 2, 'full', '1', 3))

    def test_diversity_2(self):
        self.assertEqual(14, _t4p_deconv_length('dil', 7, 2, 5, 'same', '1', 2))

    def test_diversity_3(self):
        self.assertEqual(6, _t4p_deconv_length('dil', 5, 2, 2, 'full', 'none', 3))

    def test_diversity_4(self):
        self.assertEqual(13, _t4p_deconv_length('dil', 3, 3, 2, 'valid', '2', 4))

    def test_diversity_5(self):
        self.assertEqual(9, _t4p_deconv_length('dil', 9, 1, 4, 'same', '0', 2))

    def test_diversity_6(self):
        self.assertEqual(7, _t4p_deconv_length('dil', 3, 3, 1, 'full', 'none', 2))

    def test_diversity_7(self):
        self.assertEqual(16, _t4p_deconv_length('dil', 2, 3, 5, 'valid', 'none', 3))

    def test_diversity_8(self):
        self.assertEqual(30, _t4p_deconv_length('dil', 10, 3, 4, 'same', '2', 4))

    def test_diversity_9(self):
        self.assertEqual(28, _t4p_deconv_length('dil', 11, 3, 2, 'full', 'none', 3))

    def test_diversity_10(self):
        self.assertEqual(12, _t4p_deconv_length('dil', 6, 1, 4, 'valid', '0', 2))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(17, _t4p_deconv_length('nodil', 9, 2, 1, 'same', '0', 1))

    def test_diversity_2(self):
        self.assertEqual(24, _t4p_deconv_length('nodil', 10, 3, 5, 'full', 'none', 1))

    def test_diversity_3(self):
        self.assertEqual(3, _t4p_deconv_length('nodil', 3, 1, 1, 'valid', 'none', 1))

    def test_diversity_4(self):
        self.assertEqual(19, _t4p_deconv_length('nodil', 10, 2, 1, 'valid', '0', 1))

    def test_diversity_5(self):
        self.assertEqual(18, _t4p_deconv_length('nodil', 9, 2, 4, 'same', 'none', 1))

    def test_diversity_6(self):
        self.assertEqual(11, _t4p_deconv_length('nodil', 7, 1, 5, 'valid', '0', 1))

    def test_diversity_7(self):
        self.assertEqual(20, _t4p_deconv_length('nodil', 8, 3, 3, 'full', '0', 1))

    def test_diversity_8(self):
        self.assertEqual(4, _t4p_deconv_length('nodil', 7, 1, 4, 'full', '0', 1))

    def test_diversity_9(self):
        self.assertEqual(13, _t4p_deconv_length('nodil', 5, 3, 1, 'valid', '0', 1))

    def test_diversity_10(self):
        self.assertEqual(14, _t4p_deconv_length('nodil', 6, 3, 3, 'full', 'none', 1))
