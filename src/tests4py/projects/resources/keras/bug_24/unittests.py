import unittest


def _t4p_tensorboard_fits(mode, D, nc, nh, seed):
    import os
    import tempfile

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras
    from keras.layers import Input, Dense, Lambda, GlobalAveragePooling1D, add, dot
    from keras.models import Model
    from keras import callbacks
    import keras.backend as K

    K.clear_session()
    try:
        rng = np.random.RandomState(seed)
        logs = tempfile.mkdtemp()
        inp1 = Input((D, D))
        inp2 = Input((D, D))
        inp_3d = add([inp1, inp2])
        inp_2d = GlobalAveragePooling1D()(inp_3d)
        inp_pair = Lambda(lambda x: x)([inp_3d, inp_2d])
        hidden = dot(inp_pair, axes=-1)
        hidden = Dense(nh, activation="relu")(hidden)
        output = Dense(nc, activation="softmax")(hidden)
        model = Model(inputs=[inp1, inp2], outputs=output)
        model.compile(
            loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"]
        )
        n = 10
        X = [rng.random_sample((n, D, D)), rng.random_sample((n, D, D))]
        Y = keras.utils.to_categorical(rng.randint(0, nc, size=(n,)), nc)
        hist = 1 if mode == "hist" else 0
        cb = [callbacks.TensorBoard(log_dir=logs, histogram_freq=hist, batch_size=5)]
        model.fit(
            X, Y, batch_size=5, validation_data=(X, Y), callbacks=cb, epochs=1, verbose=0
        )
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 4, 2, 5, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 5, 3, 6, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 3, 2, 4, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 6, 2, 5, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 4, 3, 7, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 5, 2, 4, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 3, 3, 6, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 6, 2, 5, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 4, 2, 8, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_tensorboard_fits('hist', 5, 3, 5, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 4, 2, 5, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 5, 3, 6, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 3, 2, 4, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 6, 2, 5, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 4, 3, 7, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 5, 2, 4, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 3, 3, 6, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 6, 2, 5, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 4, 2, 8, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_tensorboard_fits('nohist', 5, 3, 5, 19))
