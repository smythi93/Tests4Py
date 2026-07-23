import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    check = sys.argv[1]  # getnone | getx | total
    nf_none = int(sys.argv[2])
    nf_x = int(sys.argv[3])
    nb_none = int(sys.argv[4])
    nb_x = int(sys.argv[5])

    from keras.layers import Input, SimpleRNN
    from keras.layers import wrappers

    x = Input(shape=(3, 2))
    layer = wrappers.Bidirectional(SimpleRNN(3))
    _ = layer(x)

    counter = [0]

    def add(target_layer, n, inputs):
        for _ in range(n):
            target_layer.add_update(counter[0], inputs=inputs)
            counter[0] += 1

    add(layer.forward_layer, nf_none, None)
    add(layer.forward_layer, nf_x, x)
    add(layer.backward_layer, nb_none, None)
    add(layer.backward_layer, nb_x, x)

    # The buggy Bidirectional does not override get_updates_for, so it only sees
    # the FORWARD layer's updates; the fix collects forward + backward.
    if check == "getnone":
        print(len(layer.get_updates_for(None)))
    elif check == "getx":
        print(len(layer.get_updates_for(x)))
    else:
        print(len(layer.updates))
