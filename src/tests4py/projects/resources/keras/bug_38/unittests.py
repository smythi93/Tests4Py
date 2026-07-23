import unittest


def _t4p_make_cell():
    import keras

    class MinimalRNNCell(keras.layers.Layer):
        def __init__(self, units, **kwargs):
            self.units = units
            self.state_size = units
            super(MinimalRNNCell, self).__init__(**kwargs)

        def build(self, input_shape):
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


def _t4p_stack_runs(mode, u1, u2, emb, batch, ts):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    from keras.layers import RNN, Input

    keras.backend.clear_session()
    Cell = _t4p_make_cell()
    try:
        x = Input((None, emb))
        if mode == "stack":
            layer = RNN([Cell(u1), Cell(u2)])
        else:
            layer = RNN(Cell(u1))
        y = layer(x)
        model = keras.models.Model(x, y)
        model.predict(np.random.random((batch, ts, emb)))
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_stack_runs('stack', 8, 16, 5, 6, 5))

    def test_diversity_2(self):
        self.assertTrue(_t4p_stack_runs('stack', 4, 6, 3, 4, 4))

    def test_diversity_3(self):
        self.assertTrue(_t4p_stack_runs('stack', 5, 10, 6, 2, 5))

    def test_diversity_4(self):
        self.assertTrue(_t4p_stack_runs('stack', 3, 7, 4, 3, 6))

    def test_diversity_5(self):
        self.assertTrue(_t4p_stack_runs('stack', 6, 12, 8, 2, 3))

    def test_diversity_6(self):
        self.assertTrue(_t4p_stack_runs('stack', 8, 4, 7, 3, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_stack_runs('stack', 5, 5, 3, 2, 7))

    def test_diversity_8(self):
        self.assertTrue(_t4p_stack_runs('stack', 7, 3, 5, 4, 4))

    def test_diversity_9(self):
        self.assertTrue(_t4p_stack_runs('stack', 2, 8, 8, 3, 5))

    def test_diversity_10(self):
        self.assertTrue(_t4p_stack_runs('stack', 6, 9, 4, 2, 6))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_stack_runs('single', 8, 16, 5, 6, 5))

    def test_diversity_2(self):
        self.assertTrue(_t4p_stack_runs('single', 4, 6, 3, 4, 4))

    def test_diversity_3(self):
        self.assertTrue(_t4p_stack_runs('single', 5, 10, 6, 2, 5))

    def test_diversity_4(self):
        self.assertTrue(_t4p_stack_runs('single', 3, 7, 4, 3, 6))

    def test_diversity_5(self):
        self.assertTrue(_t4p_stack_runs('single', 6, 12, 8, 2, 3))

    def test_diversity_6(self):
        self.assertTrue(_t4p_stack_runs('single', 8, 4, 7, 3, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_stack_runs('single', 5, 5, 3, 2, 7))

    def test_diversity_8(self):
        self.assertTrue(_t4p_stack_runs('single', 7, 3, 5, 4, 4))

    def test_diversity_9(self):
        self.assertTrue(_t4p_stack_runs('single', 2, 8, 8, 3, 5))

    def test_diversity_10(self):
        self.assertTrue(_t4p_stack_runs('single', 6, 9, 4, 2, 6))
