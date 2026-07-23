import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # multi | single
    dim = int(sys.argv[2])
    seed = int(sys.argv[3])

    import numpy as np
    import keras

    try:
        input_layer = keras.Input(shape=(dim,))
        if mode == "multi":
            layer1 = keras.layers.Lambda(lambda x: [x + 1, x], lambda s: [s, s])
            x_a, x_b = layer1(input_layer)

            class SwapLayer(keras.layers.Layer):
                def call(self, inputs, **kwargs):
                    return [inputs[1], inputs[0]]

                def compute_output_shape(self, s):
                    return [s[1], s[0]]

            x_a, x_b = SwapLayer()([x_a, x_b])
            model = keras.Model(inputs=[input_layer], outputs=[x_a, x_b])
        else:
            out = keras.layers.Dense(dim)(input_layer)
            model = keras.Model(inputs=[input_layer], outputs=[out])
        # The buggy clone_model calls compute_mask on layers that do not support
        # masking, breaking the multi-output clone.
        new_model = keras.models.clone_model(model)
        x = np.random.RandomState(seed).random_sample((6, dim))
        new_model.predict(x)
        print("OK")
    except Exception:
        print("ERR")
