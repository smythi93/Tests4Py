import unittest


def _t4p_early_stopping(mode, base, patience):
    import os
    import sys
    import types
    import importlib.util
    keras = types.ModuleType('keras'); keras.__path__ = []
    utils = types.ModuleType('keras.utils'); utils.__path__ = []
    gu = types.ModuleType('keras.utils.generic_utils')
    class Progbar(object):
        def __init__(self, *a, **k):
            pass
        def update(self, *a, **k):
            pass
    gu.Progbar = Progbar
    backend = types.ModuleType('keras.backend')
    backend.epsilon = lambda: 1e-7
    engine = types.ModuleType('keras.engine'); engine.__path__ = []
    tu = types.ModuleType('keras.engine.training_utils')
    tu.standardize_input_data = lambda *a, **k: None
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu), ('keras.backend', backend),
                         ('keras.engine', engine),
                         ('keras.engine.training_utils', tu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'callbacks.py')
    spec = importlib.util.spec_from_file_location('keras.callbacks', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.callbacks'] = module
    spec.loader.exec_module(module)
    class Model(object):
        def __init__(self):
            self.w = None
            self.stop_training = False
        def get_weights(self):
            return [self.w]
        def set_weights(self, ws):
            self.w = ws[0]
    model = Model()
    if mode == 'restore':
        cb = module.EarlyStopping(monitor='loss', patience=patience,
                                  restore_best_weights=True)
    else:
        cb = module.EarlyStopping(monitor='loss', patience=patience)
    cb.model = model
    cb.on_train_begin()
    losses = [10.0, 5.0] + [8.0] * patience
    for e, loss in enumerate(losses):
        model.w = base + e
        cb.on_epoch_end(e, {'loss': loss})
        if model.stop_training:
            break
    return str(model.w)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('284', _t4p_early_stopping('restore', 283, 1))

    def test_diversity_2(self):
        self.assertEqual('882', _t4p_early_stopping('restore', 881, 3))

    def test_diversity_3(self):
        self.assertEqual('520', _t4p_early_stopping('restore', 519, 1))

    def test_diversity_4(self):
        self.assertEqual('483', _t4p_early_stopping('restore', 482, 2))

    def test_diversity_5(self):
        self.assertEqual('560', _t4p_early_stopping('restore', 559, 1))

    def test_diversity_6(self):
        self.assertEqual('124', _t4p_early_stopping('restore', 123, 2))

    def test_diversity_7(self):
        self.assertEqual('831', _t4p_early_stopping('restore', 830, 1))

    def test_diversity_8(self):
        self.assertEqual('826', _t4p_early_stopping('restore', 825, 3))

    def test_diversity_9(self):
        self.assertEqual('141', _t4p_early_stopping('restore', 140, 2))

    def test_diversity_10(self):
        self.assertEqual('194', _t4p_early_stopping('restore', 193, 4))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('880', _t4p_early_stopping('default', 874, 5))

    def test_diversity_2(self):
        self.assertEqual('624', _t4p_early_stopping('default', 620, 3))

    def test_diversity_3(self):
        self.assertEqual('443', _t4p_early_stopping('default', 437, 5))

    def test_diversity_4(self):
        self.assertEqual('336', _t4p_early_stopping('default', 334, 1))

    def test_diversity_5(self):
        self.assertEqual('153', _t4p_early_stopping('default', 149, 3))

    def test_diversity_6(self):
        self.assertEqual('170', _t4p_early_stopping('default', 166, 3))

    def test_diversity_7(self):
        self.assertEqual('525', _t4p_early_stopping('default', 522, 2))

    def test_diversity_8(self):
        self.assertEqual('210', _t4p_early_stopping('default', 204, 5))

    def test_diversity_9(self):
        self.assertEqual('390', _t4p_early_stopping('default', 387, 2))

    def test_diversity_10(self):
        self.assertEqual('692', _t4p_early_stopping('default', 688, 3))
