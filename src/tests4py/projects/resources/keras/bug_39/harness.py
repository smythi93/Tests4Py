import contextlib
import importlib.util
import io
import os
import sys


def _load(relpath, name):
    path = os.path.join(os.getcwd(), *relpath.split("/"))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    generic_utils = _load("keras/utils/generic_utils.py", "t4p_generic_utils")
    mode = sys.argv[1]
    vals = [int(x) for x in sys.argv[2:]]
    target = None if mode == "none" else int(mode)
    progbar = generic_utils.Progbar(target, width=30, verbose=1, interval=1e12)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        for v in vals:
            progbar.update(v)
    print("RESULT:OK")
