import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # deferred | explicit
    inner_units = int(sys.argv[2])
    out_units = int(sys.argv[3])
    indim = int(sys.argv[4])
    seed = int(sys.argv[5])

    import numpy as np
    import keras

    try:
        inner = keras.models.Sequential()
        if mode == "deferred":
            # No input_shape -> deferred build.  The buggy Sequential reads the
            # nested first layer's batch_input_shape unconditionally and fails.
            inner.add(keras.layers.Dense(inner_units))
        else:
            inner.add(keras.layers.Dense(inner_units, input_shape=(indim,)))
        inner.add(keras.layers.Dense(inner_units))
        model = keras.models.Sequential()
        model.add(inner)
        model.add(keras.layers.Dense(out_units))
        model.compile("sgd", "mse")
        rng = np.random.RandomState(seed)
        model.train_on_batch(
            rng.random_sample((2, indim)), rng.random_sample((2, out_units))
        )
        print("OK")
    except Exception:
        print("ERR")
