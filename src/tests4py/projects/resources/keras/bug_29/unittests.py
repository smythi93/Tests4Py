import unittest


def _t4p_stateful_metric_matches(mode, samples, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    import keras.backend as K

    K.clear_session()

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

    try:
        np.random.seed(seed)
        metric_fn = BinaryTruePositives()
        inputs = keras.Input(shape=(2,))
        outputs = keras.layers.Dense(
            1,
            activation="sigmoid",
            name="out",
            bias_initializer=keras.initializers.Constant(5.0),
        )(inputs)
        model = keras.Model(inputs, outputs)
        if mode == "dict":
            model.compile(
                "sgd", "binary_crossentropy", metrics={"out": ["acc", metric_fn]}
            )
        else:
            model.compile("sgd", "binary_crossentropy", metrics=["acc", metric_fn])
        x = np.random.random((samples, 2))
        y = np.random.randint(2, size=(samples, 1))
        model.fit(x, y, epochs=1, batch_size=10, verbose=0)
        idx = [i for i, n in enumerate(model.metrics_names) if "true_positives" in n][0]
        outs = model.evaluate(x, y, batch_size=10, verbose=0)
        preds = model.predict(x)
        ref = np.sum(np.logical_and(preds[:, 0] > 0.5, y[:, 0] == 1))
        return bool(np.isclose(outs[idx], ref, atol=1e-4))
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 200, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 250, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 180, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 300, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 160, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 220, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 190, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 270, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 150, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_stateful_metric_matches('dict', 240, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 200, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 250, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 180, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 300, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 160, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 220, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 190, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 270, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 150, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_stateful_metric_matches('list', 240, 19))
