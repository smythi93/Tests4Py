import unittest


def _t4p_val_data_accessed(mode, indim, nc, seed):
    import os
    import tempfile

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence
    import keras.backend as K

    K.clear_session()

    class TrackSeq(Sequence):
        def __init__(self, n, bs, indim, nc, seed, path):
            self.n = n
            self.bs = bs
            self.indim = indim
            self.nc = nc
            self.rng = np.random.RandomState(seed)
            self.path = path

        def __len__(self):
            return self.n

        def __getitem__(self, i):
            with open(self.path, "a") as f:
                f.write("x")
            return (
                self.rng.random_sample((self.bs, self.indim)),
                self.rng.random_sample((self.bs, self.nc)),
            )

    try:
        model = Sequential()
        model.add(Dense(nc, input_shape=(indim,)))
        model.compile("sgd", "mse")
        tpath = tempfile.mktemp()
        open(tpath, "w").close()
        vpath = tempfile.mktemp()
        open(vpath, "w").close()
        train = TrackSeq(4, 5, indim, nc, seed, tpath)
        val = TrackSeq(3, 5, indim, nc, seed + 1, vpath)
        model.fit_generator(
            train,
            steps_per_epoch=len(train),
            validation_data=val,
            validation_steps=len(val),
            epochs=1,
            workers=0,
            verbose=0,
        )
        count = len(open(vpath).read()) if mode == "val" else len(open(tpath).read())
        return count > 0
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_val_data_accessed('val', 3, 2, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_val_data_accessed('val', 4, 3, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_val_data_accessed('val', 5, 2, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_val_data_accessed('val', 2, 4, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_val_data_accessed('val', 6, 2, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_val_data_accessed('val', 3, 5, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_val_data_accessed('val', 4, 2, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_val_data_accessed('val', 5, 3, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_val_data_accessed('val', 2, 2, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_val_data_accessed('val', 6, 4, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_val_data_accessed('train', 3, 2, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_val_data_accessed('train', 4, 3, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_val_data_accessed('train', 5, 2, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_val_data_accessed('train', 2, 4, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_val_data_accessed('train', 6, 2, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_val_data_accessed('train', 3, 5, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_val_data_accessed('train', 4, 2, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_val_data_accessed('train', 5, 3, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_val_data_accessed('train', 2, 2, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_val_data_accessed('train', 6, 4, 19))
