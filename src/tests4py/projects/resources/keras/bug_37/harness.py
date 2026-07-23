import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # withstate | plain
    dim = int(sys.argv[2])
    timesteps = int(sys.argv[3])
    units = int(sys.argv[4])

    from keras.layers import Input, LSTM
    from keras.layers import wrappers
    from keras.models import Model

    input1 = Input((timesteps, dim))
    layer = wrappers.Bidirectional(
        LSTM(units, return_state=True, return_sequences=True)
    )
    state = layer(input1)[1:]
    input2 = Input((timesteps, dim))
    if mode == "withstate":
        # Fixed Bidirectional.__call__ wires the initial_state list as extra
        # model inputs (giving 4 layers); the buggy version silently drops them
        # (2 layers).
        output = wrappers.Bidirectional(LSTM(units))(input2, initial_state=state)
    else:
        output = wrappers.Bidirectional(LSTM(units))(input2)
    model = Model([input1, input2], output)
    print(len(model.layers))
