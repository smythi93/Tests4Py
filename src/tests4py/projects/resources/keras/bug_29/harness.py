import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


def _make_metric():
    import keras
    import keras.backend as K

    class BinaryTruePositives(keras.layers.Layer):
        def __init__(self, name="true_positives", **kwargs):
            super(BinaryTruePositives, self).__init__(name=name, **kwargs)
            self.stateful = True
            self.true_positives = K.variable(value=0, dtype="int32")

        def reset_states(self):
            K.set_value(self.true_positives, 0)

        def __call__(self, y_true, y_pred):
            y_true = K.cast(y_true, "int32")
            y_pred = K.cast(K.round(y_pred), "int32")
            correct_preds = K.cast(K.equal(y_pred, y_true), "int32")
            true_pos = K.cast(K.sum(correct_preds * y_true), "int32")
            current_true_pos = self.true_positives * 1
            self.add_update(
                K.update_add(self.true_positives, true_pos), inputs=[y_true, y_pred]
            )
            return current_true_pos + true_pos

    return BinaryTruePositives()


if __name__ == "__main__":
    mode = sys.argv[1]  # dict | list
    samples = int(sys.argv[2])
    seed = int(sys.argv[3])

    import numpy as np
    import keras

    try:
        np.random.seed(seed)
        metric_fn = _make_metric()
        inputs = keras.Input(shape=(2,))
        # A strongly positive bias makes the model predict 1 throughout, so the
        # stateful true-positive count is reliably > 0 (otherwise an all-zero
        # predictor would leave nothing for the missing reset to accumulate).
        outputs = keras.layers.Dense(
            1,
            activation="sigmoid",
            name="out",
            bias_initializer=keras.initializers.Constant(5.0),
        )(inputs)
        model = keras.Model(inputs, outputs)
        if mode == "dict":
            # In dict metrics mode the buggy Model never resets the stateful
            # metric, so it accumulates across fit/evaluate.
            model.compile("sgd", "binary_crossentropy", metrics={"out": ["acc", metric_fn]})
        else:
            model.compile("sgd", "binary_crossentropy", metrics=["acc", metric_fn])
        x = np.random.random((samples, 2))
        y = np.random.randint(2, size=(samples, 1))
        model.fit(x, y, epochs=1, batch_size=10, verbose=0)
        idx = [i for i, n in enumerate(model.metrics_names) if "true_positives" in n][0]
        outs = model.evaluate(x, y, batch_size=10, verbose=0)
        preds = model.predict(x)
        ref = np.sum(np.logical_and(preds[:, 0] > 0.5, y[:, 0] == 1))
        print("MATCH" if np.isclose(outs[idx], ref, atol=1e-4) else "MISMATCH")
    except Exception:
        print("ERR")
