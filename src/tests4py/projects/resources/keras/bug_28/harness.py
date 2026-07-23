import importlib.util
import os
import sys
import types

import numpy as np


def _load_sequence():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    prep = types.ModuleType("keras.preprocessing")
    prep.__path__ = []
    data_utils = types.ModuleType("keras.utils.data_utils")

    class Sequence(object):
        def __iter__(self):
            for i in range(len(self)):
                yield self[i]

    data_utils.Sequence = Sequence
    sys.modules["keras"] = keras
    sys.modules["keras.utils"] = utils
    sys.modules["keras.preprocessing"] = prep
    sys.modules["keras.utils.data_utils"] = data_utils
    path = os.path.join(os.getcwd(), "keras", "preprocessing", "sequence.py")
    spec = importlib.util.spec_from_file_location("keras.preprocessing.sequence", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.preprocessing.sequence"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    sequence = _load_sequence()
    n = int(sys.argv[1])
    length = int(sys.argv[2])
    batch_size = int(sys.argv[3])
    stride = int(sys.argv[4])
    data = np.arange(n).reshape(-1, 1)
    g = sequence.TimeseriesGenerator(
        data, data, length=length, batch_size=batch_size, stride=stride
    )
    print(len(g))
