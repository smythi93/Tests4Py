import importlib.util
import os
import sys
import types
import warnings

import numpy as np

warnings.filterwarnings("ignore")


def _load_training_utils():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    backend = types.ModuleType("keras.backend")
    backend.floatx = lambda: "float32"
    backend.epsilon = lambda: 1e-7
    backend.cast = lambda x, dtype: np.asarray(x).astype(dtype)
    backend.mean = lambda x, axis=None: np.mean(x, axis=axis)
    backend.ndim = lambda x: np.asarray(x).ndim
    backend.not_equal = lambda x, y: np.asarray(x) != y
    backend.is_tensor = lambda x: False
    backend.int_shape = lambda x: None
    losses = types.ModuleType("keras.losses")
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []

    class Sequence(object):
        pass

    utils.Sequence = Sequence
    gu = types.ModuleType("keras.utils.generic_utils")
    gu.to_list = lambda x: x if isinstance(x, list) else [x]
    for name, module in [
        ("keras", keras),
        ("keras.backend", backend),
        ("keras.losses", losses),
        ("keras.utils", utils),
        ("keras.utils.generic_utils", gu),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "engine", "training_utils.py")
    spec = importlib.util.spec_from_file_location("keras.engine.training_utils", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.engine.training_utils"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    tu = _load_training_utils()
    mode = sys.argv[1]
    seed = int(sys.argv[2])
    n = int(sys.argv[3])
    m = int(sys.argv[4])
    fn = lambda yt, yp: (yp - yt) ** 2
    weighted = tu.weighted_masked_objective(fn)
    rng = np.random.RandomState(seed)
    yt = rng.randint(0, 10, size=(n, m)).astype("float64")
    yp = rng.randint(0, 10, size=(n, m)).astype("float64")
    if mode == "mask0":
        mask = np.zeros((n, m))
        res = weighted(yt, yp, None, mask)
    else:
        res = weighted(yt, yp, None, None)
    print(repr(float(res)))
