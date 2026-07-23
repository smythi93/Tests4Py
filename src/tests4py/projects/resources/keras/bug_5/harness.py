import hashlib
import importlib.util
import os
import sys
import tempfile
import types


def _load():
    keras = types.ModuleType("keras")
    keras.__path__ = []
    utils = types.ModuleType("keras.utils")
    utils.__path__ = []
    gu = types.ModuleType("keras.utils.generic_utils")

    class Progbar(object):
        def __init__(self, *a, **k):
            pass

        def update(self, *a, **k):
            pass

    gu.Progbar = Progbar
    for name, module in [
        ("keras", keras),
        ("keras.utils", utils),
        ("keras.utils.generic_utils", gu),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "utils", "data_utils.py")
    spec = importlib.util.spec_from_file_location("keras.utils.data_utils", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.utils.data_utils"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    data_utils = _load()
    mode = sys.argv[1]
    fname = sys.argv[2]
    tmp = tempfile.mkdtemp()
    os.environ["KERAS_HOME"] = tmp
    content = ("data-" + fname).encode()
    file_hash = hashlib.sha256(content).hexdigest()
    datadir = os.path.join(tmp, "datasets")
    os.makedirs(datadir, exist_ok=True)
    with open(os.path.join(datadir, fname), "wb") as fp:
        fp.write(content)
    origin = "http://127.0.0.1:1/" + fname
    if mode == "none":
        data_utils.get_file(fname, origin=origin, cache_dir=None, file_hash=file_hash)
    else:
        data_utils.get_file(fname, origin=origin, cache_dir=tmp, file_hash=file_hash)
    print("RESULT:OK")
