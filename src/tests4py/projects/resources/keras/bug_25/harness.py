import importlib.util
import os
import sys
import types

import numpy as np


def _load():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    apps = types.ModuleType("keras.applications")
    apps.__path__ = []
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    data_utils = types.ModuleType("keras.utils.data_utils")
    data_utils.get_file = lambda *a, **k: None
    backend = types.ModuleType("keras.backend")
    backend.image_data_format = lambda: "channels_last"
    backend.floatx = lambda: "float32"
    for name, module in [
        ("keras", keras),
        ("keras.applications", apps),
        ("keras.utils", utils),
        ("keras.utils.data_utils", data_utils),
        ("keras.backend", backend),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "applications", "imagenet_utils.py")
    spec = importlib.util.spec_from_file_location(
        "keras.applications.imagenet_utils", path
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.applications.imagenet_utils"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    imagenet_utils = _load()
    mode = sys.argv[1]
    dtype = sys.argv[2]
    h = int(sys.argv[3])
    w = int(sys.argv[4])
    base = (np.arange(h * w * 3) % 256).reshape(h, w, 3)
    arr = base.astype("int32") if dtype == "int" else base.astype("float64")
    imagenet_utils.preprocess_input(arr, "channels_last", mode)
    print("RESULT:OK")
