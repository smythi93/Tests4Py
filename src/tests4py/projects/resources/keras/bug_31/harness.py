import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    batch = int(sys.argv[1])
    T = int(sys.argv[2])
    L = int(sys.argv[3])
    num_classes = int(sys.argv[4])
    seed = int(sys.argv[5])

    import numpy as np
    import keras.backend as K

    try:
        rng = np.random.RandomState(seed)
        y_pred = rng.random_sample((batch, T, num_classes)).astype("float32")
        y_pred = y_pred / y_pred.sum(axis=-1, keepdims=True)
        y_true = rng.randint(0, num_classes - 1, size=(batch, L)).astype("float32")
        input_length = np.full((batch, 1), T, dtype="float32")
        label_length = np.full((batch, 1), L, dtype="float32")
        # The buggy ctc_batch_cost squeezes label/input length without an axis,
        # collapsing the (batch, 1) tensors to a scalar when batch == 1.
        cost = K.ctc_batch_cost(
            K.variable(y_true),
            K.variable(y_pred),
            K.variable(input_length),
            K.variable(label_length),
        )
        c = np.asarray(K.eval(cost))
        print("OK" if (c.shape == (batch, 1) and np.all(np.isfinite(c))) else "BAD")
    except Exception:
        print("ERR")
