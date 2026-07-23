import unittest


def _t4p_generator_enqueuer(mode, val):
    import os
    import sys
    import types
    import signal
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
    for name, module in [('keras', keras), ('keras.utils', utils),
                         ('keras.utils.generic_utils', gu)]:
        sys.modules[name] = module
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'data_utils.py')
    spec = importlib.util.spec_from_file_location('keras.utils.data_utils', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['keras.utils.data_utils'] = module
    spec.loader.exec_module(module)

    def faulty():
        raise IndexError('t4p fault %d' % val)
        yield val

    def good():
        while True:
            yield val

    try:
        signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
        signal.alarm(15)
    except Exception:
        pass
    gen = faulty() if mode == 'fault' else good()
    enq = module.GeneratorEnqueuer(gen, use_multiprocessing=False)
    enq.start(1, 10)
    out = enq.get()
    try:
        next(out)
        result = 'OK'
    except IndexError:
        result = 'IndexError'
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
    return result


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 21590))

    def test_diversity_2(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 17826))

    def test_diversity_3(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 46368))

    def test_diversity_4(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 91507))

    def test_diversity_5(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 53642))

    def test_diversity_6(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 47174))

    def test_diversity_7(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 36256))

    def test_diversity_8(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 82052))

    def test_diversity_9(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 67721))

    def test_diversity_10(self):
        self.assertEqual('IndexError', _t4p_generator_enqueuer('fault', 32767))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 46184))

    def test_diversity_2(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 3782))

    def test_diversity_3(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 2394))

    def test_diversity_4(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 98366))

    def test_diversity_5(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 75860))

    def test_diversity_6(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 7766))

    def test_diversity_7(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 25220))

    def test_diversity_8(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 29324))

    def test_diversity_9(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 39993))

    def test_diversity_10(self):
        self.assertEqual('OK', _t4p_generator_enqueuer('good', 86039))
