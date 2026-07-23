import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # shared | simple
    D = int(sys.argv[2])
    out = int(sys.argv[3])
    seed = int(sys.argv[4])

    import numpy as np
    from keras.layers import Input, Dense, Reshape, concatenate
    from keras.models import Model

    try:
        input_shape = (1, D)
        inp = Input(shape=input_shape)
        if mode == "shared":
            # A shared layer applied at heterogeneous depth: the buggy
            # from_config reconstructs the nodes in the wrong order and mis-wires
            # the concatenate.
            A = Dense(D, name="layer_a")
            r1 = Reshape((D,))(inp)
            Aout1 = A(r1)
            r2 = Reshape((D,))(A(inp))
            Aout2 = A(r2)
            c1 = concatenate([Aout2, Aout1])
            output = Dense(out, name="layer_b")(c1)
        else:
            r1 = Reshape((D,))(inp)
            h = Dense(D)(r1)
            output = Dense(out)(h)
        model = Model(inputs=inp, outputs=output)
        x = np.random.RandomState(seed).random_sample((5,) + input_shape)
        model.predict(x)
        config = model.get_config()
        weights = model.get_weights()
        model2 = Model.from_config(config)
        model2.set_weights(weights)
        model2.predict(x)
        print("OK")
    except Exception:
        print("ERR")
