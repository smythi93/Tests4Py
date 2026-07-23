import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


def _make_cell_class():
    import keras

    class MinimalRNNCell(keras.layers.Layer):
        def __init__(self, units, **kwargs):
            self.units = units
            self.state_size = units
            super(MinimalRNNCell, self).__init__(**kwargs)

        def build(self, input_shape):
            # RNN cells receive an input shape WITHOUT the time axis, so it must
            # be 2-D.  The buggy StackedRNNCells.build passes a 3-tuple to the
            # inner cells, tripping this assertion.
            assert len(input_shape) == 2
            self.kernel = self.add_weight(
                shape=(input_shape[-1], self.units),
                initializer="uniform",
                name="kernel",
            )
            self.recurrent_kernel = self.add_weight(
                shape=(self.units, self.units),
                initializer="uniform",
                name="recurrent_kernel",
            )
            self.built = True

        def call(self, inputs, states):
            prev_output = states[0]
            h = keras.backend.dot(inputs, self.kernel)
            output = h + keras.backend.dot(prev_output, self.recurrent_kernel)
            return output, [output]

    return MinimalRNNCell


if __name__ == "__main__":
    mode = sys.argv[1]
    u1 = int(sys.argv[2])
    u2 = int(sys.argv[3])
    emb = int(sys.argv[4])
    batch = int(sys.argv[5])
    ts = int(sys.argv[6])

    import numpy as np
    import keras
    from keras.layers import RNN, Input

    Cell = _make_cell_class()
    try:
        x = Input((None, emb))
        if mode == "stack":
            layer = RNN([Cell(u1), Cell(u2)])
        else:
            layer = RNN(Cell(u1))
        y = layer(x)
        model = keras.models.Model(x, y)
        model.predict(np.random.random((batch, ts, emb)))
        print("OK")
    except Exception:
        print("ERR")
