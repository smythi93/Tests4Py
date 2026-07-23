import importlib.util
import os
import sys
import types


def _load_callbacks():
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
    backend = types.ModuleType("keras.backend")
    backend.get_value = lambda var: var["v"]
    backend.set_value = lambda var, val: var.__setitem__("v", val)
    backend.epsilon = lambda: 1e-7
    engine = types.ModuleType("keras.engine")
    engine.__path__ = []
    topo = types.ModuleType("keras.engine.topology")

    class Layer(object):
        pass

    topo.Layer = Layer
    for name, module in [
        ("keras", keras),
        ("keras.utils", utils),
        ("keras.utils.generic_utils", gu),
        ("keras.backend", backend),
        ("keras.engine", engine),
        ("keras.engine.topology", topo),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "callbacks.py")
    spec = importlib.util.spec_from_file_location("keras.callbacks", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.callbacks"] = module
    spec.loader.exec_module(module)
    return module


class _Opt(object):
    def __init__(self, lr):
        self.lr = {"v": lr}


class _Model(object):
    def __init__(self, lr):
        self.optimizer = _Opt(lr)


if __name__ == "__main__":
    callbacks = _load_callbacks()
    mode = sys.argv[1]
    lr0_pow = int(sys.argv[2])
    patience = int(sys.argv[3])
    lr0 = 2.0 ** lr0_pow
    epochs = patience + 1 if mode == "reduce" else patience
    model = _Model(lr0)
    cb = callbacks.ReduceLROnPlateau(
        monitor="loss", factor=0.5, patience=patience, cooldown=0, min_lr=0
    )
    cb.model = model
    cb.on_train_begin()
    for e in range(epochs):
        cb.on_epoch_end(e, {"loss": 0.5})
    print(repr(float(model.optimizer.lr["v"])))
