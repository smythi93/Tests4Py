import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # datatensor | normal
    D = int(sys.argv[2])
    units = int(sys.argv[3])
    n = int(sys.argv[4])
    seed = int(sys.argv[5])

    import numpy as np
    import tensorflow as tf
    from keras.layers import Input, Dense, Dropout
    from keras.models import Model
    import keras.backend as K

    rng = np.random.RandomState(seed)
    try:
        if mode == "datatensor":
            data = rng.random_sample((n, D)).astype("float32")
            a = Input(tensor=tf.Variable(data, dtype=tf.float32))
            a2 = Dense(units, name="d1")(a)
            a2 = Dropout(0.5)(a2)
            model = Model(a, a2)
            model.add_loss(K.mean(a2))
            model.compile(optimizer="rmsprop", loss=None, metrics=["mse"])

            def gen():
                while True:
                    # x is None (framework-native data tensor); the buggy loop
                    # computes batch_size from x and hits None.shape.
                    yield (None, None)

            model.evaluate_generator(gen(), steps=3)
            model.predict_generator(gen(), steps=3)
        else:
            a = Input(shape=(D,))
            out = Dense(units)(a)
            model = Model(a, out)
            model.compile("rmsprop", "mse", metrics=["mse"])

            def gen():
                while True:
                    yield (
                        rng.random_sample((5, D)),
                        rng.random_sample((5, units)),
                    )

            model.evaluate_generator(gen(), steps=3)
        print("OK")
    except Exception:
        print("ERR")
