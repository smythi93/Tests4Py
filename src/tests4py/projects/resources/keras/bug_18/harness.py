import os
import sys

os.environ.setdefault("KERAS_BACKEND", "tensorflow")


if __name__ == "__main__":
    mode = sys.argv[1]  # withmeta | plain
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    import keras.backend as K

    try:
        from tensorflow.core.protobuf import config_pb2

        x = K.placeholder(shape=())
        y = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        kwargs = {}
        if mode == "withmeta":
            # The buggy Function rejects `options`/`run_metadata` session kwargs.
            kwargs["options"] = config_pb2.RunOptions(output_partition_graphs=True)
            kwargs["run_metadata"] = run_metadata
        f = K.function(inputs=[x, y], outputs=[x + y], **kwargs)
        out = f([a, b])
        ok = abs(float(out[0]) - (a + b)) < 1e-4
        if mode == "withmeta":
            ok = ok and len(run_metadata.partition_graphs) > 0
        print("OK" if ok else "BAD")
    except Exception:
        print("ERR")
