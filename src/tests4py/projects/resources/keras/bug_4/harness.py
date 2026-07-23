import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # strict | lenient
    num_classes = int(sys.argv[2])
    samples = int(sys.argv[3])
    indim = int(sys.argv[4])
    seed = int(sys.argv[5])

    import numpy as np
    from tensorflow import train
    from keras import optimizers
    from keras.models import Sequential
    from keras.layers import Dense

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
        # The buggy TFOptimizer passes params POSITIONALLY, which a
        # keyword-only compute_gradients rejects.
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
        print("OK")
    except Exception:
        print("ERR")
