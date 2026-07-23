import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")

if __name__ == "__main__":
    u1 = int(sys.argv[1])
    u2 = int(sys.argv[2])
    ts = int(sys.argv[3])
    emb = int(sys.argv[4])
    rs = sys.argv[5]

    from keras.layers import recurrent

    cells = [recurrent.LSTMCell(u1), recurrent.LSTMCell(u2)]
    layer = recurrent.RNN(
        cells, return_state=True, return_sequences=(rs == "seq")
    )
    out = layer.compute_output_shape((None, ts, emb))
    print(out)
