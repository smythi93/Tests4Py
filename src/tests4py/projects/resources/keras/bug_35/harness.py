import importlib.util
import os
import sys
import types

import numpy as np


def _load_image():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    backend = types.ModuleType("keras.backend")
    backend.image_data_format = lambda: "channels_last"
    backend.floatx = lambda: "float32"
    backend.epsilon = lambda: 1e-7
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    du = types.ModuleType("keras.utils.data_utils")

    class Sequence(object):
        pass

    du.Sequence = Sequence
    for name, module in [
        ("keras", keras),
        ("keras.backend", backend),
        ("keras.utils", utils),
        ("keras.utils.data_utils", du),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "preprocessing", "image.py")
    spec = importlib.util.spec_from_file_location("keras.preprocessing.image", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.preprocessing.image"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    image = _load_image()
    mode = sys.argv[1]
    seed = int(sys.argv[2])
    n = int(sys.argv[3])
    mult = int(sys.argv[4])
    rescale = int(sys.argv[5])
    rng = np.random.RandomState(seed)
    x = rng.randint(0, 10, size=(n, 2, 2, 3)).astype("int64")
    if mode == "pf":
        idg = image.ImageDataGenerator(
            preprocessing_function=lambda a: a * mult,
            rescale=rescale,
            data_format="channels_last",
        )
    else:
        idg = image.ImageDataGenerator(
            preprocessing_function=None,
            rescale=rescale,
            data_format="channels_last",
        )
    out = np.asarray(idg.standardize(x))
    print(",".join(str(int(v)) for v in out.ravel()))
