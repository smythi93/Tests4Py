import importlib.util
import os
import sys
import types


def _load():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    backend = types.ModuleType("keras.backend")
    for name, module in [
        ("keras", keras),
        ("keras.utils", utils),
        ("keras.backend", backend),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "utils", "conv_utils.py")
    spec = importlib.util.spec_from_file_location("keras.utils.conv_utils", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.utils.conv_utils"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    conv_utils = _load()
    mode = sys.argv[1]
    dim = int(sys.argv[2])
    stride = int(sys.argv[3])
    kernel = int(sys.argv[4])
    padding = sys.argv[5]
    op = sys.argv[6]
    out_pad = None if op == "none" else int(op)
    dilation = int(sys.argv[7])
    if mode == "dil":
        result = conv_utils.deconv_length(
            dim, stride, kernel, padding, out_pad, dilation
        )
    else:
        result = conv_utils.deconv_length(dim, stride, kernel, padding, out_pad)
    print(result)
