import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")

_LAYERS = {"simple": "SimpleRNN", "gru": "GRU", "lstm": "LSTM"}


if __name__ == "__main__":
    layer_name = sys.argv[1]
    units = int(sys.argv[2])
    emb = int(sys.argv[3])
    mode = sys.argv[4]

    from keras.layers import recurrent

    layer = getattr(recurrent, _LAYERS[layer_name])(units)
    layer.build((None, None, emb))
    if mode == "frozen":
        # Fixed keras returns no trainable weights once a layer is frozen; the
        # buggy version keeps reporting the cell's trainable weights.
        layer.trainable = False
        print(len(layer.trainable_weights))
    else:  # trainable
        ok = (
            len(layer.trainable_weights) == len(layer.weights)
            and len(layer.weights) > 0
        )
        print("1" if ok else "0")
