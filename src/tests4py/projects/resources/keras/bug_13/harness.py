import os
import sys
import tempfile

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # val | train
    indim = int(sys.argv[2])
    nc = int(sys.argv[3])
    seed = int(sys.argv[4])

    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.utils import Sequence

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
        # The buggy fit_generator validates using the TRAINING generator, so the
        # validation Sequence is never actually read.
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
        print("ACCESSED" if count > 0 else "NOTACCESSED")
    except Exception:
        print("ERR")
