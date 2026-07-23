import unittest


def _t4p_tfoptimizer_fits(mode, num_classes, samples, indim, seed):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import numpy as np
    from tensorflow import train
    from keras import optimizers
    from keras.models import Sequential
    from keras.layers import Dense
    import keras.backend as K

    K.clear_session()

    class StrictOpt(train.Optimizer):
        wrapping_optimizer = train.AdamOptimizer()

        def compute_gradients(self, loss, **kwargs):
            return super(StrictOpt, self).compute_gradients(loss, **kwargs)

        def apply_gradients(self, gv, **kwargs):
            return self.wrapping_optimizer.apply_gradients(gv, **kwargs)

    class LenientOpt(train.Optimizer):
        wrapping_optimizer = train.AdamOptimizer()

        def compute_gradients(self, loss, var_list=None, **kwargs):
            return super(LenientOpt, self).compute_gradients(
                loss, var_list=var_list, **kwargs
            )

        def apply_gradients(self, gv, **kwargs):
            return self.wrapping_optimizer.apply_gradients(gv, **kwargs)

    try:
        Opt = StrictOpt if mode == "strict" else LenientOpt
        tf_opt = Opt(use_locking=False, name="T4POpt%d" % seed)
        optimizer = optimizers.TFOptimizer(tf_opt)
        model = Sequential()
        model.add(Dense(num_classes, input_shape=(indim,)))
        model.compile(loss="mean_squared_error", optimizer=optimizer)
        rng = np.random.RandomState(seed)
        model.fit(
            rng.random_sample((samples, indim)),
            rng.random_sample((samples, num_classes)),
            epochs=1,
            batch_size=samples,
            verbose=0,
        )
        return True
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 2, 5, 3, 0))

    def test_diversity_2(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 3, 6, 4, 1))

    def test_diversity_3(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 4, 4, 2, 2))

    def test_diversity_4(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 2, 8, 5, 3))

    def test_diversity_5(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 5, 5, 3, 4))

    def test_diversity_6(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 3, 4, 4, 5))

    def test_diversity_7(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 2, 6, 2, 6))

    def test_diversity_8(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 4, 7, 3, 7))

    def test_diversity_9(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 3, 5, 5, 8))

    def test_diversity_10(self):
        self.assertTrue(_t4p_tfoptimizer_fits('strict', 5, 4, 2, 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 2, 5, 3, 10))

    def test_diversity_2(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 3, 6, 4, 11))

    def test_diversity_3(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 4, 4, 2, 12))

    def test_diversity_4(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 2, 8, 5, 13))

    def test_diversity_5(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 5, 5, 3, 14))

    def test_diversity_6(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 3, 4, 4, 15))

    def test_diversity_7(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 2, 6, 2, 16))

    def test_diversity_8(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 4, 7, 3, 17))

    def test_diversity_9(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 3, 5, 5, 18))

    def test_diversity_10(self):
        self.assertTrue(_t4p_tfoptimizer_fits('lenient', 5, 4, 2, 19))
