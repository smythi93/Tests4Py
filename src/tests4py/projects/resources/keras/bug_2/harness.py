import importlib.util
import os
import sys
import types

import numpy as np


def _load_numpy_backend():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    backend = types.ModuleType("keras.backend")
    backend.__path__ = []
    common = types.ModuleType("keras.backend.common")
    common.floatx = lambda: "float32"
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    utils.to_categorical = lambda *a, **k: None
    gu = types.ModuleType("keras.utils.generic_utils")
    gu.transpose_shape = lambda *a, **k: None
    for name, module in [
        ("keras", keras),
        ("keras.backend", backend),
        ("keras.backend.common", common),
        ("keras.utils", utils),
        ("keras.utils.generic_utils", gu),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "backend", "numpy_backend.py")
    spec = importlib.util.spec_from_file_location("keras.backend.numpy_backend", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.backend.numpy_backend"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    nb = _load_numpy_backend()
    mode = sys.argv[1]
    seed = int(sys.argv[2])
    n = int(sys.argv[3])
    c = int(sys.argv[4])
    k = int(sys.argv[5])
    if mode == "topk":
        rng = np.random.RandomState(seed)
        preds = np.stack([rng.permutation(c) for _ in range(n)]).astype("float32")
        targets = rng.randint(0, c, size=n)
        r = np.asarray(nb.in_top_k(preds, targets, k))
    else:
        rng = np.random.RandomState(seed)
        a = rng.randint(0, 100, size=n)
        b = rng.randint(0, 100, size=n)
        r = np.asarray(nb.greater(a, b))
    print("".join("1" if x else "0" for x in r.astype(bool).ravel()))
