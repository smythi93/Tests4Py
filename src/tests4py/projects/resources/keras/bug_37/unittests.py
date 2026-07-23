import unittest


def _t4p_bidir_layers(mode, dim, timesteps, units):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K
    from keras.layers import Input, LSTM
    from keras.layers import wrappers
    from keras.models import Model

    K.clear_session()
    input1 = Input((timesteps, dim))
    layer = wrappers.Bidirectional(
        LSTM(units, return_state=True, return_sequences=True)
    )
    state = layer(input1)[1:]
    input2 = Input((timesteps, dim))
    if mode == "withstate":
        output = wrappers.Bidirectional(LSTM(units))(input2, initial_state=state)
    else:
        output = wrappers.Bidirectional(LSTM(units))(input2)
    model = Model([input1, input2], output)
    return len(model.layers)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 5, 3, 3))

    def test_diversity_2(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 4, 4, 2))

    def test_diversity_3(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 6, 3, 5))

    def test_diversity_4(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 3, 5, 3))

    def test_diversity_5(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 7, 2, 4))

    def test_diversity_6(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 5, 4, 6))

    def test_diversity_7(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 4, 3, 3))

    def test_diversity_8(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 6, 5, 2))

    def test_diversity_9(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 3, 4, 5))

    def test_diversity_10(self):
        self.assertEqual(4, _t4p_bidir_layers('withstate', 8, 3, 4))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 5, 3, 3))

    def test_diversity_2(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 4, 4, 2))

    def test_diversity_3(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 6, 3, 5))

    def test_diversity_4(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 3, 5, 3))

    def test_diversity_5(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 7, 2, 4))

    def test_diversity_6(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 5, 4, 6))

    def test_diversity_7(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 4, 3, 3))

    def test_diversity_8(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 6, 5, 2))

    def test_diversity_9(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 3, 4, 5))

    def test_diversity_10(self):
        self.assertEqual(2, _t4p_bidir_layers('plain', 8, 3, 4))
