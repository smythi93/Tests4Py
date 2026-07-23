import importlib.util
import inspect
import os
import sys
import types

import numpy as np


def _load_wrapper():
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
    return module


class _FakeModel(object):
    def __init__(self, n):
        self.n = n

    def predict(self, x, **kwargs):
        return np.zeros((self.n, 1))


if __name__ == "__main__":
    wrapper = _load_wrapper()
    n = int(sys.argv[1])
    feat = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    reg = wrapper.KerasRegressor(build_fn=lambda: None)
    reg.model = _FakeModel(n)
    x = np.zeros((n, feat))
    preds = reg.predict(x)
    print("RESULT:" + repr(tuple(preds.shape)))
