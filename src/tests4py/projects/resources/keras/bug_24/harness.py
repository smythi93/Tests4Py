import os
import sys
import tempfile

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # hist | nohist
    D = int(sys.argv[2])
    nc = int(sys.argv[3])
    nh = int(sys.argv[4])
    seed = int(sys.argv[5])

    import numpy as np
    import keras
    from keras.layers import Input, Dense, Lambda, GlobalAveragePooling1D, add, dot
    from keras.models import Model
    from keras import callbacks

    try:
        rng = np.random.RandomState(seed)
        logs = tempfile.mkdtemp()
        inp1 = Input((D, D))
        inp2 = Input((D, D))
        inp_3d = add([inp1, inp2])
        inp_2d = GlobalAveragePooling1D()(inp_3d)
        # A layer with a LIST of output tensors; the buggy TensorBoard passes
        # that list straight to tf.summary.histogram and fails.
        inp_pair = Lambda(lambda x: x)([inp_3d, inp_2d])
        hidden = dot(inp_pair, axes=-1)
        hidden = Dense(nh, activation="relu")(hidden)
        output = Dense(nc, activation="softmax")(hidden)
        model = Model(inputs=[inp1, inp2], outputs=output)
        model.compile(
            loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"]
        )
        n = 10
        X = [rng.random_sample((n, D, D)), rng.random_sample((n, D, D))]
        Y = keras.utils.to_categorical(rng.randint(0, nc, size=(n,)), nc)
        hist = 1 if mode == "hist" else 0
        cb = [callbacks.TensorBoard(log_dir=logs, histogram_freq=hist, batch_size=5)]
        model.fit(
            X, Y, batch_size=5, validation_data=(X, Y), callbacks=cb, epochs=1, verbose=0
        )
        print("OK")
    except Exception:
        print("ERR")
