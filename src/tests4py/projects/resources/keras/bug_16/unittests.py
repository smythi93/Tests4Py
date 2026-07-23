import unittest


def _t4p_seq_config_type(nlayers, units, indim):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.models import Sequential
    from keras.layers import Dense
    import keras.backend as K

    K.clear_session()
    model = Sequential()
    model.add(Dense(units, input_shape=(indim,)))
    for _ in range(nlayers - 1):
        model.add(Dense(units))
    return isinstance(model.get_config(), dict)


def _t4p_seq_nlayers(nlayers, units, indim):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.models import Sequential
    from keras.layers import Dense
    import keras.backend as K

    K.clear_session()
    model = Sequential()
    model.add(Dense(units, input_shape=(indim,)))
    for _ in range(nlayers - 1):
        model.add(Dense(units))
    return len(model.layers)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_seq_config_type(1, 4, 3))

    def test_diversity_2(self):
        self.assertTrue(_t4p_seq_config_type(2, 5, 4))

    def test_diversity_3(self):
        self.assertTrue(_t4p_seq_config_type(3, 4, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_seq_config_type(1, 6, 5))

    def test_diversity_5(self):
        self.assertTrue(_t4p_seq_config_type(2, 3, 3))

    def test_diversity_6(self):
        self.assertTrue(_t4p_seq_config_type(3, 7, 4))

    def test_diversity_7(self):
        self.assertTrue(_t4p_seq_config_type(1, 4, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_seq_config_type(2, 5, 2))

    def test_diversity_9(self):
        self.assertTrue(_t4p_seq_config_type(3, 6, 3))

    def test_diversity_10(self):
        self.assertTrue(_t4p_seq_config_type(1, 8, 4))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(1, _t4p_seq_nlayers(1, 4, 3))

    def test_diversity_2(self):
        self.assertEqual(2, _t4p_seq_nlayers(2, 5, 4))

    def test_diversity_3(self):
        self.assertEqual(3, _t4p_seq_nlayers(3, 4, 2))

    def test_diversity_4(self):
        self.assertEqual(1, _t4p_seq_nlayers(1, 6, 5))

    def test_diversity_5(self):
        self.assertEqual(2, _t4p_seq_nlayers(2, 3, 3))

    def test_diversity_6(self):
        self.assertEqual(3, _t4p_seq_nlayers(3, 7, 4))

    def test_diversity_7(self):
        self.assertEqual(1, _t4p_seq_nlayers(1, 4, 6))

    def test_diversity_8(self):
        self.assertEqual(2, _t4p_seq_nlayers(2, 5, 2))

    def test_diversity_9(self):
        self.assertEqual(3, _t4p_seq_nlayers(3, 6, 3))

    def test_diversity_10(self):
        self.assertEqual(1, _t4p_seq_nlayers(1, 8, 4))
