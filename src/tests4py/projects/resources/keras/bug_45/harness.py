import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    units = int(sys.argv[1])
    ts = int(sys.argv[2])
    emb = int(sys.argv[3])
    batch = int(sys.argv[4])
    mode = sys.argv[5]  # bias | nobias

    import numpy as np
    from keras.layers import LSTM, Input
    from keras.models import Model

    try:
        inp = Input((ts, emb))
        # implementation=1 exercises the per-gate matmul path; the buggy cell
        # adds bias unconditionally there, raising when use_bias=False.
        out = LSTM(units, implementation=1, use_bias=(mode == "bias"))(inp)
        model = Model(inp, out)
        y = model.predict(np.random.random((batch, ts, emb)))
        print("OK" if tuple(y.shape) == (batch, units) else "BADSHAPE")
    except Exception:
        print("ERR")
