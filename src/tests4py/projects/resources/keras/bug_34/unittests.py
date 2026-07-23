import unittest


def _t4p_fitgen_workers_runs(mode, indim, nc, seed):
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
        workers = 0 if mode == "workers0" else 1
        model.fit_generator(
            seq, steps_per_epoch=len(seq), epochs=1, workers=workers, verbose=0
        )
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 3, 2, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 4, 3, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 5, 2, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 2, 4, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 6, 2, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 3, 5, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 4, 2, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 5, 3, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 2, 2, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers0', 6, 4, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 3, 2, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 4, 3, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 5, 2, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 2, 4, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 6, 2, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 3, 5, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 4, 2, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 5, 3, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 2, 2, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_fitgen_workers_runs('workers1', 6, 4, 19))
