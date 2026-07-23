import unittest


def _t4p_bidir_count(check, nf_none, nf_x, nb_none, nb_x):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K
    from keras.layers import Input, SimpleRNN
    from keras.layers import wrappers

    K.clear_session()
    x = Input(shape=(3, 2))
    layer = wrappers.Bidirectional(SimpleRNN(3))
    _ = layer(x)
    counter = [0]

    def add(target_layer, n, inputs):
        for _ in range(n):
            target_layer.add_update(counter[0], inputs=inputs)
            counter[0] += 1

    add(layer.forward_layer, nf_none, None)
    add(layer.forward_layer, nf_x, x)
    add(layer.backward_layer, nb_none, None)
    add(layer.backward_layer, nb_x, x)
    if check == "getnone":
        return len(layer.get_updates_for(None))
    elif check == "getx":
        return len(layer.get_updates_for(x))
    return len(layer.updates)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(2, _t4p_bidir_count('getnone', 1, 1, 1, 1))

    def test_diversity_2(self):
        self.assertEqual(5, _t4p_bidir_count('getnone', 2, 0, 3, 0))

    def test_diversity_3(self):
        self.assertEqual(2, _t4p_bidir_count('getnone', 0, 1, 2, 0))

    def test_diversity_4(self):
        self.assertEqual(4, _t4p_bidir_count('getnone', 3, 2, 1, 0))

    def test_diversity_5(self):
        self.assertEqual(4, _t4p_bidir_count('getnone', 2, 1, 2, 1))

    def test_diversity_6(self):
        self.assertEqual(2, _t4p_bidir_count('getx', 1, 1, 1, 1))

    def test_diversity_7(self):
        self.assertEqual(5, _t4p_bidir_count('getx', 0, 2, 0, 3))

    def test_diversity_8(self):
        self.assertEqual(2, _t4p_bidir_count('getx', 2, 0, 1, 2))

    def test_diversity_9(self):
        self.assertEqual(3, _t4p_bidir_count('getx', 1, 2, 2, 1))

    def test_diversity_10(self):
        self.assertEqual(4, _t4p_bidir_count('getx', 3, 1, 0, 3))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(4, _t4p_bidir_count('total', 1, 1, 1, 1))

    def test_diversity_2(self):
        self.assertEqual(5, _t4p_bidir_count('total', 2, 0, 3, 0))

    def test_diversity_3(self):
        self.assertEqual(5, _t4p_bidir_count('total', 0, 2, 0, 3))

    def test_diversity_4(self):
        self.assertEqual(6, _t4p_bidir_count('total', 2, 1, 1, 2))

    def test_diversity_5(self):
        self.assertEqual(6, _t4p_bidir_count('total', 3, 2, 1, 0))

    def test_diversity_6(self):
        self.assertEqual(4, _t4p_bidir_count('total', 1, 0, 2, 1))

    def test_diversity_7(self):
        self.assertEqual(8, _t4p_bidir_count('total', 2, 2, 2, 2))

    def test_diversity_8(self):
        self.assertEqual(2, _t4p_bidir_count('total', 0, 1, 1, 0))

    def test_diversity_9(self):
        self.assertEqual(6, _t4p_bidir_count('total', 3, 0, 0, 3))

    def test_diversity_10(self):
        self.assertEqual(7, _t4p_bidir_count('total', 1, 3, 2, 1))
