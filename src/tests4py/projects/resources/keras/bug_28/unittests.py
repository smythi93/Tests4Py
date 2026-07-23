import unittest


def _t4p_timeseries_len(n, length, batch_size, stride):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    prep = types.ModuleType('keras.preprocessing'); prep.__path__ = []
    data_utils = types.ModuleType('keras.utils.data_utils')
    class Sequence(object):
        def __iter__(self):
            for i in range(len(self)):
                yield self[i]
    data_utils.Sequence = Sequence
    sys.modules['keras'] = keras
    sys.modules['keras.utils'] = utils
    sys.modules['keras.preprocessing'] = prep
    sys.modules['keras.utils.data_utils'] = data_utils
    path = os.path.join(os.getcwd(), 'keras', 'preprocessing', 'sequence.py')
    spec = importlib.util.spec_from_file_location('keras.preprocessing.sequence', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.preprocessing.sequence'] = module
    spec.loader.exec_module(module)
    data = np.arange(n).reshape(-1, 1)
    g = module.TimeseriesGenerator(data, data, length=length,
                                   batch_size=batch_size, stride=stride)
    return len(g)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(9, _t4p_timeseries_len(14, 5, 1, 1))

    def test_diversity_2(self):
        self.assertEqual(7, _t4p_timeseries_len(9, 2, 1, 1))

    def test_diversity_3(self):
        self.assertEqual(6, _t4p_timeseries_len(10, 4, 1, 1))

    def test_diversity_4(self):
        self.assertEqual(6, _t4p_timeseries_len(8, 2, 1, 1))

    def test_diversity_5(self):
        self.assertEqual(7, _t4p_timeseries_len(10, 3, 1, 1))

    def test_diversity_6(self):
        self.assertEqual(12, _t4p_timeseries_len(17, 5, 1, 1))

    def test_diversity_7(self):
        self.assertEqual(2, _t4p_timeseries_len(8, 6, 1, 1))

    def test_diversity_8(self):
        self.assertEqual(5, _t4p_timeseries_len(10, 5, 1, 1))

    def test_diversity_9(self):
        self.assertEqual(3, _t4p_timeseries_len(9, 6, 1, 1))

    def test_diversity_10(self):
        self.assertEqual(12, _t4p_timeseries_len(14, 2, 1, 1))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(1, _t4p_timeseries_len(9, 6, 4, 3))

    def test_diversity_2(self):
        self.assertEqual(2, _t4p_timeseries_len(11, 2, 2, 3))

    def test_diversity_3(self):
        self.assertEqual(1, _t4p_timeseries_len(4, 2, 3, 1))

    def test_diversity_4(self):
        self.assertEqual(2, _t4p_timeseries_len(10, 2, 3, 2))

    def test_diversity_5(self):
        self.assertEqual(4, _t4p_timeseries_len(15, 3, 3, 1))

    def test_diversity_6(self):
        self.assertEqual(2, _t4p_timeseries_len(10, 4, 4, 1))

    def test_diversity_7(self):
        self.assertEqual(7, _t4p_timeseries_len(17, 3, 2, 1))

    def test_diversity_8(self):
        self.assertEqual(1, _t4p_timeseries_len(8, 4, 4, 3))

    def test_diversity_9(self):
        self.assertEqual(1, _t4p_timeseries_len(5, 2, 3, 3))

    def test_diversity_10(self):
        self.assertEqual(1, _t4p_timeseries_len(13, 6, 4, 3))
