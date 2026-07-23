import unittest


def _t4p_rnn_states(mode, ns, idim, odim, ts, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    import keras.backend as K

    K.clear_session()
    try:
        rng = np.random.RandomState(seed)
        x = rng.random_sample((ns, ts, idim)).astype("float32")
        h0 = rng.random_sample((ns, odim)).astype("float32")
        wi = rng.random_sample((idim, odim)).astype("float32")
        wh = rng.random_sample((odim, odim)).astype("float32")
        x_k = K.variable(x)
        h0_k = [K.variable(h0), K.variable(np.concatenate([h0, h0], axis=-1))]
        wi_k = K.variable(wi)
        wh_k = K.variable(wh)

        def rnn_fn(x_k, h_k):
            y_k = K.dot(x_k, wi_k) + K.dot(h_k[0], wh_k)
            return y_k, [y_k, K.concatenate([y_k, y_k], axis=-1)]

        kwargs = {}
        if mode == "mask":
            m = rng.randint(2, size=(ns, ts))
            kwargs["mask"] = K.variable(m)
        last, outs, states = K.rnn(rnn_fn, x_k, h0_k, **kwargs)
        o = np.asarray(K.eval(outs))
        s1 = np.asarray(K.eval(states[1]))
        return o.shape == (ns, ts, odim) and s1.shape == (ns, 2 * odim)
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_rnn_states('mask', 4, 5, 3, 6, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_rnn_states('mask', 3, 4, 2, 5, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_rnn_states('mask', 5, 6, 4, 7, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_rnn_states('mask', 2, 3, 3, 4, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_rnn_states('mask', 6, 5, 2, 8, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_rnn_states('mask', 4, 7, 3, 5, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_rnn_states('mask', 3, 5, 5, 6, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_rnn_states('mask', 5, 4, 2, 7, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_rnn_states('mask', 2, 6, 4, 5, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_rnn_states('mask', 6, 3, 3, 6, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_rnn_states('nomask', 4, 5, 3, 6, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_rnn_states('nomask', 3, 4, 2, 5, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_rnn_states('nomask', 5, 6, 4, 7, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_rnn_states('nomask', 2, 3, 3, 4, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_rnn_states('nomask', 6, 5, 2, 8, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_rnn_states('nomask', 4, 7, 3, 5, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_rnn_states('nomask', 3, 5, 5, 6, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_rnn_states('nomask', 5, 4, 2, 7, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_rnn_states('nomask', 2, 6, 4, 5, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_rnn_states('nomask', 6, 3, 3, 6, 19))
