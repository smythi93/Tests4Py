import importlib.util
import inspect
import os
import sys
import types
import unittest

import numpy as np


def _t4p_regressor_predict_shape(n, feat):
    keras = types.ModuleType("keras")
    keras.__path__ = []
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    np_utils = types.ModuleType("keras.utils.np_utils")
    np_utils.to_categorical = lambda *a, **k: None
    gu = types.ModuleType("keras.utils.generic_utils")

    def has_arg(fn, name, accept_all=False):
        try:
            sig = inspect.signature(fn)
        except (TypeError, ValueError):
            return False
        if accept_all:
            for param in sig.parameters.values():
                if param.kind == inspect.Parameter.VAR_KEYWORD:
                    return True
        return name in sig.parameters

    gu.has_arg = has_arg
    gu.to_list = lambda x: x if isinstance(x, list) else [x]
    models = types.ModuleType("keras.models")

    class Sequential(object):
        def fit(self, x, y, **kwargs):
            pass

        def predict(self, x, **kwargs):
            pass

        def predict_classes(self, x, **kwargs):
            pass

        def evaluate(self, x, y, **kwargs):
            pass

    models.Sequential = Sequential
    for _name, _module in [
        ("keras", keras),
        ("keras.utils", utils),
        ("keras.utils.np_utils", np_utils),
        ("keras.utils.generic_utils", gu),
        ("keras.models", models),
    ]:
        sys.modules[_name] = _module
    path = os.path.join(os.getcwd(), "keras", "wrappers", "scikit_learn.py")
    spec = importlib.util.spec_from_file_location("keras.wrappers.scikit_learn", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.wrappers.scikit_learn"] = module
    spec.loader.exec_module(module)

    class _FakeModel(object):
        def predict(self, x, **kwargs):
            return np.zeros((n, 1))

    reg = module.KerasRegressor(build_fn=lambda: None)
    reg.model = _FakeModel()
    x = np.zeros((n, feat))
    return tuple(reg.predict(x).shape)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 2))

    def test_diversity_2(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 3))

    def test_diversity_3(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 4))

    def test_diversity_4(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 5))

    def test_diversity_5(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 6))

    def test_diversity_6(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 7))

    def test_diversity_7(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 8))

    def test_diversity_8(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 9))

    def test_diversity_9(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 10))

    def test_diversity_10(self):
        self.assertEqual((1,), _t4p_regressor_predict_shape(1, 11))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual((2,), _t4p_regressor_predict_shape(2, 2))

    def test_diversity_2(self):
        self.assertEqual((3,), _t4p_regressor_predict_shape(3, 4))

    def test_diversity_3(self):
        self.assertEqual((4,), _t4p_regressor_predict_shape(4, 3))

    def test_diversity_4(self):
        self.assertEqual((5,), _t4p_regressor_predict_shape(5, 5))

    def test_diversity_5(self):
        self.assertEqual((6,), _t4p_regressor_predict_shape(6, 6))

    def test_diversity_6(self):
        self.assertEqual((7,), _t4p_regressor_predict_shape(7, 4))

    def test_diversity_7(self):
        self.assertEqual((8,), _t4p_regressor_predict_shape(8, 7))

    def test_diversity_8(self):
        self.assertEqual((9,), _t4p_regressor_predict_shape(9, 5))

    def test_diversity_9(self):
        self.assertEqual((10,), _t4p_regressor_predict_shape(10, 8))

    def test_diversity_10(self):
        self.assertEqual((12,), _t4p_regressor_predict_shape(12, 6))
