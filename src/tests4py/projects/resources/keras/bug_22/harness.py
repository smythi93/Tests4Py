import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # masked | nomask
    units = int(sys.argv[2])
    dim = int(sys.argv[3])
    ts = int(sys.argv[4])

    from keras import layers
    from keras.models import Model, Sequential

    try:
        inputs = layers.Input(shape=(ts, dim))
        if mode == "masked":
            # A masked tensor must flow into the Sequential's InputLayer; the
            # buggy InputLayer has supports_masking=False and raises.
            x = layers.Masking(mask_value=0.0)(inputs)
        else:
            x = inputs
        s = Sequential()
        s.add(layers.Dense(units, input_shape=(dim,)))
        s.add(layers.Activation("relu"))
        x = layers.wrappers.TimeDistributed(s)(x)
        model = Model(inputs=inputs, outputs=x)
        model.compile(optimizer="rmsprop", loss="mse")
        print("OK")
    except Exception:
        print("ERR")
