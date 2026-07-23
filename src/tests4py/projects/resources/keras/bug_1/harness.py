import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import numpy as np


_INITS = {
    "uniform": "RandomUniform",
    "normal": "RandomNormal",
    "truncated": "TruncatedNormal",
    "varscale": "VarianceScaling",
}


def _build(name, seed):
    from keras import initializers

    cls = getattr(initializers, _INITS[name])
    return cls(seed=seed)


if __name__ == "__main__":
    mode = sys.argv[1]
    name = sys.argv[2]
    seed = int(sys.argv[3])
    rows = int(sys.argv[4])
    cols = int(sys.argv[5])

    import keras.backend as K

    init = _build(name, seed)
    if mode == "diff":
        a = np.asarray(K.eval(init((rows, cols))))
        b = np.asarray(K.eval(init((rows, cols))))
        # Fixed keras increments the seed after every call, so two consecutive
        # calls of a *seeded* initializer produce different draws.  The buggy
        # version keeps the same seed and returns identical arrays.
        print("1" if not np.allclose(a, b) else "0")
    else:  # shape
        a = np.asarray(K.eval(init((rows, cols))))
        print(tuple(a.shape))
