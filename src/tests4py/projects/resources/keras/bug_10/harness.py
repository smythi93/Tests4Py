import importlib.util
import os
import sys
import types

import numpy as np


def _load_training_utils():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    backend = types.ModuleType("keras.backend")
    for a in ["is_tensor", "int_shape", "floatx"]:
        setattr(backend, a, lambda *x, **k: None)
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
    C = int(sys.argv[4])
    rng = np.random.RandomState(seed)
    y = rng.randint(0, C, size=n)
    sw = rng.randint(1, 6, size=n)
    cw = {c: int(rng.randint(2, 6)) for c in range(C)}
    if mode == "both":
        r = tu.standardize_weights(y, sample_weight=sw, class_weight=cw)
    else:
        r = tu.standardize_weights(y, sample_weight=sw, class_weight=None)
    print(",".join(str(int(v)) for v in np.asarray(r).ravel()))
