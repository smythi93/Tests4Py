import importlib.util
import os
import unittest

import numpy as np

def _t4p_to_categorical_shape(mode, num_classes, vals):
    import os
    import importlib.util
    import numpy as np
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'np_utils.py')
    spec = importlib.util.spec_from_file_location('t4p_np_utils', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if mode == 'col':
        y = np.array(vals).reshape(-1, 1)
    else:
        y = np.array(vals)
    return tuple(module.to_categorical(y, num_classes).shape)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual((3, 9), _t4p_to_categorical_shape('col', 9, [7, 0, 7]))

    def test_diversity_2(self):
        self.assertEqual((8, 7), _t4p_to_categorical_shape('col', 7, [5, 3, 0, 4, 0, 6, 0, 4]))

    def test_diversity_3(self):
        self.assertEqual((6, 2), _t4p_to_categorical_shape('col', 2, [1, 1, 1, 1, 0, 1]))

    def test_diversity_4(self):
        self.assertEqual((5, 4), _t4p_to_categorical_shape('col', 4, [2, 3, 2, 0, 0]))

    def test_diversity_5(self):
        self.assertEqual((3, 8), _t4p_to_categorical_shape('col', 8, [6, 7, 5]))

    def test_diversity_6(self):
        self.assertEqual((6, 4), _t4p_to_categorical_shape('col', 4, [1, 3, 0, 0, 1, 1]))

    def test_diversity_7(self):
        self.assertEqual((4, 11), _t4p_to_categorical_shape('col', 11, [3, 9, 4, 1]))

    def test_diversity_8(self):
        self.assertEqual((8, 9), _t4p_to_categorical_shape('col', 9, [8, 4, 6, 7, 0, 0, 1, 7]))

    def test_diversity_9(self):
        self.assertEqual((4, 4), _t4p_to_categorical_shape('col', 4, [0, 0, 0, 2]))

    def test_diversity_10(self):
        self.assertEqual((7, 10), _t4p_to_categorical_shape('col', 10, [1, 5, 7, 3, 8, 0, 6]))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual((6, 10), _t4p_to_categorical_shape('flat', 10, [7, 9, 4, 9, 2, 3]))

    def test_diversity_2(self):
        self.assertEqual((8, 2), _t4p_to_categorical_shape('flat', 2, [0, 1, 1, 0, 1, 0, 1, 0]))

    def test_diversity_3(self):
        self.assertEqual((2, 7), _t4p_to_categorical_shape('flat', 7, [0, 0]))

    def test_diversity_4(self):
        self.assertEqual((3, 7), _t4p_to_categorical_shape('flat', 7, [2, 0, 4]))

    def test_diversity_5(self):
        self.assertEqual((7, 8), _t4p_to_categorical_shape('flat', 8, [4, 7, 0, 5, 1, 0, 1]))

    def test_diversity_6(self):
        self.assertEqual((5, 3), _t4p_to_categorical_shape('flat', 3, [1, 1, 0, 1, 0]))

    def test_diversity_7(self):
        self.assertEqual((3, 4), _t4p_to_categorical_shape('flat', 4, [3, 1, 2]))

    def test_diversity_8(self):
        self.assertEqual((5, 12), _t4p_to_categorical_shape('flat', 12, [1, 9, 7, 8, 10]))

    def test_diversity_9(self):
        self.assertEqual((4, 12), _t4p_to_categorical_shape('flat', 12, [6, 5, 7, 2]))

    def test_diversity_10(self):
        self.assertEqual((4, 4), _t4p_to_categorical_shape('flat', 4, [3, 1, 1, 2]))
