import importlib.util
import os
import signal
import sys
import types


def _load_data_utils():
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
    data_utils = _load_data_utils()
    mode = sys.argv[1]
    val = int(sys.argv[2])

    def faulty():
        raise IndexError("t4p fault %d" % val)
        yield val

    def good():
        while True:
            yield val

    try:
        signal.signal(
            signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError())
        )
        signal.alarm(15)
    except Exception:
        pass
    gen = faulty() if mode == "fault" else good()
    enq = data_utils.GeneratorEnqueuer(gen, use_multiprocessing=False)
    enq.start(1, 10)
    out = enq.get()
    try:
        next(out)
        result = "OK"
    except IndexError:
        result = "IndexError"
    except BaseException as e:
        result = type(e).__name__
    try:
        enq.stop()
    except Exception:
        pass
    try:
        signal.alarm(0)
    except Exception:
        pass
    print("RESULT:" + result)
