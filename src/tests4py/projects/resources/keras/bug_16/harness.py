import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # cfgtype | nlayers
    nlayers = int(sys.argv[2])
    units = int(sys.argv[3])
    indim = int(sys.argv[4])

    from keras.models import Sequential
    from keras.layers import Dense

    model = Sequential()
    model.add(Dense(units, input_shape=(indim,)))
    for _ in range(nlayers - 1):
        model.add(Dense(units))

    if mode == "cfgtype":
        # Fixed Sequential.get_config returns a dict; the buggy version returns
        # a bare list of layer configs.
        print(type(model.get_config()).__name__)
    else:
        print(len(model.layers))
