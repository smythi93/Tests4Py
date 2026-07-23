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
    backend.epsilon = lambda: 1e-7
    engine = types.ModuleType("keras.engine")
    engine.__path__ = []
    tu = types.ModuleType("keras.engine.training_utils")
    tu.standardize_input_data = lambda *a, **k: None
    for name, module in [
        ("keras", keras),
        ("keras.utils", utils),
        ("keras.utils.generic_utils", gu),
        ("keras.backend", backend),
        ("keras.engine", engine),
        ("keras.engine.training_utils", tu),
    ]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), "keras", "callbacks.py")
    spec = importlib.util.spec_from_file_location("keras.callbacks", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["keras.callbacks"] = module
    spec.loader.exec_module(module)
    return module


class _Model(object):
    def __init__(self):
        self.w = None
        self.stop_training = False

    def get_weights(self):
        return [self.w]

    def set_weights(self, ws):
        self.w = ws[0]


if __name__ == "__main__":
    callbacks = _load_callbacks()
    mode = sys.argv[1]
    base = int(sys.argv[2])
    patience = int(sys.argv[3])
    model = _Model()
    if mode == "restore":
        cb = callbacks.EarlyStopping(
            monitor="loss", patience=patience, restore_best_weights=True
        )
    else:
        cb = callbacks.EarlyStopping(monitor="loss", patience=patience)
    cb.model = model
    cb.on_train_begin()
    losses = [10.0, 5.0] + [8.0] * patience
    for e, loss in enumerate(losses):
        model.w = base + e
        cb.on_epoch_end(e, {"loss": loss})
        if model.stop_training:
            break
    print(str(model.w))
