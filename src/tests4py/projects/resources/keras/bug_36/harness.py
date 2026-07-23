import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    strides = int(sys.argv[1])
    filters = int(sys.argv[2])
    numstep = int(sys.argv[3])
    stacksize = int(sys.argv[4])
    batch = int(sys.argv[5])
    df = sys.argv[6]  # last | first

    import numpy as np
    import keras
    from keras.layers import SeparableConv1D, Input
    from keras.models import Model

    data_format = "channels_last" if df == "last" else "channels_first"
    keras.backend.clear_session()
    try:
        if df == "last":
            inp = Input((numstep, stacksize))
            x = np.random.random((batch, numstep, stacksize))
        else:
            inp = Input((stacksize, numstep))
            x = np.random.random((batch, stacksize, numstep))
        # The buggy separable_conv1d builds an unequal (H, W) stride tuple, which
        # TF's depthwise_conv2d rejects for strides > 1.
        layer = SeparableConv1D(
            filters, 3, strides=strides, padding="valid", data_format=data_format
        )
        model = Model(inp, layer(inp))
        model.predict(x)
        print("OK")
    except Exception:
        print("ERR")
