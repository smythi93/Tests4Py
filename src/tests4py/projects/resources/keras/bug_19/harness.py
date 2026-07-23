import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")

if __name__ == "__main__":
    u1 = int(sys.argv[1])
    u2 = int(sys.argv[2])

    from keras.layers import recurrent

    layer = recurrent.RNN([recurrent.LSTMCell(u1), recurrent.LSTMCell(u2)])
    # Fixed keras reports the stacked state sizes in natural cell order
    # (u1, u1, u2, u2); the buggy version reverses them.
    print(tuple(layer.cell.state_size))
