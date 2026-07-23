import unittest


def _t4p_fitgen_runs(mode, indim, nc, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence
    import keras.backend as K

    K.clear_session()

    class MySeq(Sequence):
        def __init__(self, n, bs, indim, nc, seed):
            self.n = n
            self.bs = bs
            self.indim = indim
            self.nc = nc
            self.rng = np.random.RandomState(seed)

        def __len__(self):
            return self.n

        def __getitem__(self, i):
            return (
                self.rng.random_sample((self.bs, self.indim)),
                self.rng.random_sample((self.bs, self.nc)),
            )

    try:
        model = Sequential()
        model.add(Dense(nc, input_shape=(indim,)))
        model.compile("sgd", "mse")
        seq = MySeq(4, 5, indim, nc, seed)
        if mode == "nostep":
            model.fit_generator(seq, epochs=1, verbose=0)
        else:
            model.fit_generator(seq, steps_per_epoch=len(seq), epochs=1, verbose=0)
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 3, 2, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 4, 3, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 5, 2, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 2, 4, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 6, 2, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 3, 5, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 4, 2, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 5, 3, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 2, 2, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_fitgen_runs('nostep', 6, 4, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 3, 2, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 4, 3, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 5, 2, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 2, 4, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 6, 2, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 3, 5, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 4, 2, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 5, 3, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 2, 2, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_fitgen_runs('withstep', 6, 4, 19))
