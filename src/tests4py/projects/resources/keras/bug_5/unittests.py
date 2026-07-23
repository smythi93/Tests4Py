import unittest


def _t4p_get_file(mode, fname):
    import os
    import sys
    import types
    import hashlib
    import tempfile
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
    tmp = tempfile.mkdtemp()
    os.environ['KERAS_HOME'] = tmp
    content = ('data-' + fname).encode()
    file_hash = hashlib.sha256(content).hexdigest()
    datadir = os.path.join(tmp, 'datasets')
    os.makedirs(datadir, exist_ok=True)
    with open(os.path.join(datadir, fname), 'wb') as fp:
        fp.write(content)
    origin = 'http://127.0.0.1:1/' + fname
    if mode == 'none':
        module.get_file(fname, origin=origin, cache_dir=None, file_hash=file_hash)
    else:
        module.get_file(fname, origin=origin, cache_dir=tmp, file_hash=file_hash)
    return 'OK'


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_9h9kcg'))

    def test_diversity_2(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_mz8xtn'))

    def test_diversity_3(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_l891bj8sa'))

    def test_diversity_4(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_4bis0h1ol'))

    def test_diversity_5(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_a3olwigflfhw'))

    def test_diversity_6(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_zoqvd36j3zkj'))

    def test_diversity_7(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_v2rcjm'))

    def test_diversity_8(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_iurgj920'))

    def test_diversity_9(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_4lm6amyr'))

    def test_diversity_10(self):
        self.assertEqual('OK', _t4p_get_file('none', 't4p_t8oxh7ity'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_murzbdsghy8'))

    def test_diversity_2(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_h5hszh3r8'))

    def test_diversity_3(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_2apdmt9'))

    def test_diversity_4(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_lc1pa10x3j4n'))

    def test_diversity_5(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_xwctiaqbp33s'))

    def test_diversity_6(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_zjeuwks9xtcr'))

    def test_diversity_7(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_le9dvw'))

    def test_diversity_8(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_kigx6rzqa9n'))

    def test_diversity_9(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_t3olpecu39dk'))

    def test_diversity_10(self):
        self.assertEqual('OK', _t4p_get_file('explicit', 't4p_0h678oag9rmb'))
