import importlib.util
import os
import sys
import types

import numpy as np


def _load_metrics():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    K = types.ModuleType("keras.backend")
    K.mean = lambda x, axis=None: np.mean(x, axis=axis)
    K.cast = lambda x, dtype: np.asarray(x).astype(
        "int32" if dtype == "int32" else dtype
    )
    K.max = lambda x, axis=None: np.max(x, axis=axis)
    K.flatten = lambda x: np.asarray(x).flatten()

    def in_top_k(preds, targets, k):
        top_k = np.argsort(-np.asarray(preds))[:, :k]
        t = np.asarray(targets).reshape(-1, 1)
        return np.any(t == top_k, axis=-1)

    K.in_top_k = in_top_k
    losses = types.ModuleType("keras.losses")
    losses.__getattr__ = lambda name: (lambda *a, **k: None)
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    gu = types.ModuleType("keras.utils.generic_utils")
    gu.__getattr__ = lambda name: (lambda *a, **k: None)
    for name, module in [
        ("keras", keras),
        ("keras.backend", K),
        ("keras.losses", losses),
        ("keras.utils", utils),
        ("keras.utils.generic_utils", gu),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "metrics.py")
    spec = importlib.util.spec_from_file_location("keras.metrics", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.metrics"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    metrics = _load_metrics()
    mode = sys.argv[1]
    seed = int(sys.argv[2])
    n = int(sys.argv[3])
    perm = np.random.RandomState(seed).permutation(n)
    ypred = np.eye(n)[perm]
    if mode == "flat":
        y_true = perm
    else:
        y_true = perm.reshape(-1, 1)
    res = metrics.sparse_top_k_categorical_accuracy(y_true, ypred, 1)
    print(repr(float(np.asarray(res))))
