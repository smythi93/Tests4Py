import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # workers0 | workers1
    indim = int(sys.argv[2])
    nc = int(sys.argv[3])
    seed = int(sys.argv[4])

    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence

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
        # With workers=0 there is no enqueuer, so the buggy code calls next() on
        # the Sequence directly -- but a Sequence is not an iterator.
        model.fit_generator(
            seq, steps_per_epoch=len(seq), epochs=1, workers=workers, verbose=0
        )
        print("OK")
    except Exception:
        print("ERR")
