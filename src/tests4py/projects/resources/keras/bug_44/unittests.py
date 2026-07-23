import unittest

_LAYERS = {"simple": "SimpleRNN", "gru": "GRU", "lstm": "LSTM"}


def _t4p_rnn_layer(layer_name, units, emb):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.layers import recurrent

    layer = getattr(recurrent, _LAYERS[layer_name])(units)
    layer.build((None, None, emb))
    return layer


def _t4p_frozen_trainable_count(layer_name, units, emb):
    layer = _t4p_rnn_layer(layer_name, units, emb)
    layer.trainable = False
    return len(layer.trainable_weights)


def _t4p_all_trainable(layer_name, units, emb):
    layer = _t4p_rnn_layer(layer_name, units, emb)
    return len(layer.trainable_weights) == len(layer.weights) and len(layer.weights) > 0


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('simple', 5, 4))

    def test_diversity_2(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('gru', 6, 3))

    def test_diversity_3(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('lstm', 4, 5))

    def test_diversity_4(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('simple', 7, 2))

    def test_diversity_5(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('gru', 3, 6))

    def test_diversity_6(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('lstm', 8, 3))

    def test_diversity_7(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('simple', 4, 7))

    def test_diversity_8(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('gru', 5, 5))

    def test_diversity_9(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('lstm', 6, 4))

    def test_diversity_10(self):
        self.assertEqual(0, _t4p_frozen_trainable_count('simple', 3, 8))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_all_trainable('simple', 5, 4))

    def test_diversity_2(self):
        self.assertTrue(_t4p_all_trainable('gru', 6, 3))

    def test_diversity_3(self):
        self.assertTrue(_t4p_all_trainable('lstm', 4, 5))

    def test_diversity_4(self):
        self.assertTrue(_t4p_all_trainable('simple', 7, 2))

    def test_diversity_5(self):
        self.assertTrue(_t4p_all_trainable('gru', 3, 6))

    def test_diversity_6(self):
        self.assertTrue(_t4p_all_trainable('lstm', 8, 3))

    def test_diversity_7(self):
        self.assertTrue(_t4p_all_trainable('simple', 4, 7))

    def test_diversity_8(self):
        self.assertTrue(_t4p_all_trainable('gru', 5, 5))

    def test_diversity_9(self):
        self.assertTrue(_t4p_all_trainable('lstm', 6, 4))

    def test_diversity_10(self):
        self.assertTrue(_t4p_all_trainable('simple', 3, 8))
