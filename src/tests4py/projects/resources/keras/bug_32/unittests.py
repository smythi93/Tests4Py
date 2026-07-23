import unittest


def _t4p_reduce_lr(mode, lr0_pow, patience):
    import os
    import sys
    import types
    import importlib.util
    import numpy as np
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
    backend.get_value = lambda var: var['v']
    backend.set_value = lambda var, val: var.__setitem__('v', val)
    backend.epsilon = lambda: 1e-7
    engine = types.ModuleType('keras.engine'); engine.__path__ = []
    topo = types.ModuleType('keras.engine.topology')
    class Layer(object):
        pass
    topo.Layer = Layer
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu), ('keras.backend', backend),
                         ('keras.engine', engine), ('keras.engine.topology', topo)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'callbacks.py')
    spec = importlib.util.spec_from_file_location('keras.callbacks', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.callbacks'] = module
    spec.loader.exec_module(module)
    lr0 = 2.0 ** lr0_pow
    epochs = patience + 1 if mode == 'reduce' else patience
    class Opt(object):
        def __init__(self, lr):
            self.lr = {'v': lr}
    class Model(object):
        def __init__(self, lr):
            self.optimizer = Opt(lr)
    model = Model(lr0)
    cb = module.ReduceLROnPlateau(monitor='loss', factor=0.5, patience=patience,
                                  cooldown=0, min_lr=0)
    cb.model = model
    cb.on_train_begin()
    for e in range(epochs):
        cb.on_epoch_end(e, {'loss': 0.5})
    return repr(float(model.optimizer.lr['v']))


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('1.0', _t4p_reduce_lr('reduce', 1, 1))

    def test_diversity_2(self):
        self.assertEqual('1.0', _t4p_reduce_lr('reduce', 1, 6))

    def test_diversity_3(self):
        self.assertEqual('16.0', _t4p_reduce_lr('reduce', 5, 6))

    def test_diversity_4(self):
        self.assertEqual('8.0', _t4p_reduce_lr('reduce', 4, 6))

    def test_diversity_5(self):
        self.assertEqual('2.0', _t4p_reduce_lr('reduce', 2, 2))

    def test_diversity_6(self):
        self.assertEqual('4.0', _t4p_reduce_lr('reduce', 3, 5))

    def test_diversity_7(self):
        self.assertEqual('2.0', _t4p_reduce_lr('reduce', 2, 1))

    def test_diversity_8(self):
        self.assertEqual('32.0', _t4p_reduce_lr('reduce', 6, 3))

    def test_diversity_9(self):
        self.assertEqual('1.0', _t4p_reduce_lr('reduce', 1, 2))

    def test_diversity_10(self):
        self.assertEqual('8.0', _t4p_reduce_lr('reduce', 4, 1))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('8.0', _t4p_reduce_lr('noreduce', 3, 6))

    def test_diversity_2(self):
        self.assertEqual('4.0', _t4p_reduce_lr('noreduce', 2, 2))

    def test_diversity_3(self):
        self.assertEqual('64.0', _t4p_reduce_lr('noreduce', 6, 6))

    def test_diversity_4(self):
        self.assertEqual('32.0', _t4p_reduce_lr('noreduce', 5, 2))

    def test_diversity_5(self):
        self.assertEqual('2.0', _t4p_reduce_lr('noreduce', 1, 5))

    def test_diversity_6(self):
        self.assertEqual('8.0', _t4p_reduce_lr('noreduce', 3, 2))

    def test_diversity_7(self):
        self.assertEqual('32.0', _t4p_reduce_lr('noreduce', 5, 5))

    def test_diversity_8(self):
        self.assertEqual('16.0', _t4p_reduce_lr('noreduce', 4, 6))

    def test_diversity_9(self):
        self.assertEqual('32.0', _t4p_reduce_lr('noreduce', 5, 6))

    def test_diversity_10(self):
        self.assertEqual('32.0', _t4p_reduce_lr('noreduce', 5, 3))
