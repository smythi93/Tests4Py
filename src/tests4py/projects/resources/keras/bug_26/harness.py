import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # mask | nomask
    ns = int(sys.argv[2])
    idim = int(sys.argv[3])
    odim = int(sys.argv[4])
    ts = int(sys.argv[5])
    seed = int(sys.argv[6])

    import numpy as np
    import keras.backend as K

    try:
        rng = np.random.RandomState(seed)
        x = rng.random_sample((ns, ts, idim)).astype("float32")
        h0 = rng.random_sample((ns, odim)).astype("float32")
        wi = rng.random_sample((idim, odim)).astype("float32")
        wh = rng.random_sample((odim, odim)).astype("float32")
        x_k = K.variable(x)
        # Two states of DIFFERENT width: odim and 2*odim.
        h0_k = [K.variable(h0), K.variable(np.concatenate([h0, h0], axis=-1))]
        wi_k = K.variable(wi)
        wh_k = K.variable(wh)

        def rnn_fn(x_k, h_k):
            y_k = K.dot(x_k, wi_k) + K.dot(h_k[0], wh_k)
            return y_k, [y_k, K.concatenate([y_k, y_k], axis=-1)]

        kwargs = {}
        if mode == "mask":
            # The buggy rnn tiles the mask to the OUTPUT width for every state,
            # so the wider second state fails the tf.where shape check.
            m = rng.randint(2, size=(ns, ts))
            kwargs["mask"] = K.variable(m)
        last, outs, states = K.rnn(rnn_fn, x_k, h0_k, **kwargs)
        o = np.asarray(K.eval(outs))
        s1 = np.asarray(K.eval(states[1]))
        ok = o.shape == (ns, ts, odim) and s1.shape == (ns, 2 * odim)
        print("OK" if ok else "BAD")
    except Exception:
        print("ERR")
