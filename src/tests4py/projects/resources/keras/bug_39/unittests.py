import unittest


def _t4p_progbar_update(mode, vals):
    import os
    import io
    import contextlib
    import importlib.util
    path = os.path.join(os.getcwd(), 'keras', 'utils', 'generic_utils.py')
    spec = importlib.util.spec_from_file_location('t4p_generic_utils', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    target = None if mode == 'none' else int(mode)
    p = module.Progbar(target, width=30, verbose=1, interval=1e12)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        for v in vals:
            p.update(v)
    return 'OK'


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [13, 12, 1]))

    def test_diversity_2(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [14, 4, 5]))

    def test_diversity_3(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [10]))

    def test_diversity_4(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [11, 1, 17, 6]))

    def test_diversity_5(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [20]))

    def test_diversity_6(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [20, 3, 13]))

    def test_diversity_7(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [19, 5, 13]))

    def test_diversity_8(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [1, 8]))

    def test_diversity_9(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [7, 16, 4, 4]))

    def test_diversity_10(self):
        self.assertEqual('OK', _t4p_progbar_update('none', [7, 17, 10]))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('OK', _t4p_progbar_update('7', [0, 11, 14]))

    def test_diversity_2(self):
        self.assertEqual('OK', _t4p_progbar_update('6', [12, 18, 11, 12]))

    def test_diversity_3(self):
        self.assertEqual('OK', _t4p_progbar_update('4', [4, 10, 9, 13]))

    def test_diversity_4(self):
        self.assertEqual('OK', _t4p_progbar_update('6', [6, 7, 16]))

    def test_diversity_5(self):
        self.assertEqual('OK', _t4p_progbar_update('4', [9, 7, 4, 8]))

    def test_diversity_6(self):
        self.assertEqual('OK', _t4p_progbar_update('13', [17, 14]))

    def test_diversity_7(self):
        self.assertEqual('OK', _t4p_progbar_update('13', [0, 15, 5]))

    def test_diversity_8(self):
        self.assertEqual('OK', _t4p_progbar_update('18', [13, 17]))

    def test_diversity_9(self):
        self.assertEqual('OK', _t4p_progbar_update('3', [17]))

    def test_diversity_10(self):
        self.assertEqual('OK', _t4p_progbar_update('19', [16, 1, 16, 5]))
