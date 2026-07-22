import importlib.util
import os
import sys

import numpy as np


def _load(relpath, name):
    path = os.path.join(os.getcwd(), *relpath.split("/"))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    np_utils = _load("keras/utils/np_utils.py", "t4p_np_utils")
    mode = sys.argv[1]
    num_classes = int(sys.argv[2])
    vals = [int(x) for x in sys.argv[3:]]
    if mode == "col":
        y = np.array(vals).reshape(-1, 1)
    else:
        y = np.array(vals)
    out = np_utils.to_categorical(y, num_classes)
    print(tuple(out.shape))
