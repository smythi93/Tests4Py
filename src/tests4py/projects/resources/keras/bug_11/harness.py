import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # duck | real
    indim = int(sys.argv[2])
    nc = int(sys.argv[3])
    seed = int(sys.argv[4])

    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence

    class DuckSeq(object):
        # Quacks like a Sequence (len + getitem, use_sequence_api) but is NOT a
        # subclass -- mirrors a keras_preprocessing iterator.
        use_sequence_api = True

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

    class RealSeq(Sequence):
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
        seq = (
            DuckSeq(4, 5, indim, nc, seed)
            if mode == "duck"
            else RealSeq(4, 5, indim, nc, seed)
        )
        # No steps_per_epoch: the buggy code only recognizes strict Sequence
        # subclasses, so a duck-typed Sequence raises.
        model.fit_generator(seq, epochs=1, verbose=0)
        print("OK")
    except Exception:
        print("ERR")
