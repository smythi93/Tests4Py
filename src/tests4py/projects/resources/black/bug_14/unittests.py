import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        try:
            return black.format_str(src, line_length=88)
        except TypeError:
            pass
        mode = None
        for attr in ('Mode', 'FileMode'):
            if hasattr(black, attr):
                try:
                    mode = getattr(black, attr)()
                except Exception:
                    mode = None
                break
        if mode is None:
            return black.format_str(src)
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertEqual('from __future__ import absolute_import as _ilqp\n', self.run_black('from __future__ import absolute_import as _ilqp\n'))

    def test_diversity_2(self):
        self.assertEqual('from __future__ import generators as _wxuha\n', self.run_black('from __future__ import generators as _wxuha\n'))

    def test_diversity_3(self):
        self.assertEqual('from __future__ import nested_scopes as _rmzdrtv\n', self.run_black('from __future__ import nested_scopes as _rmzdrtv\n'))

    def test_diversity_4(self):
        self.assertEqual('from __future__ import unicode_literals as _zony\n', self.run_black('from __future__ import unicode_literals as _zony\n'))

    def test_diversity_5(self):
        self.assertEqual('from __future__ import nested_scopes as _mswxem\n', self.run_black('from __future__ import nested_scopes as _mswxem\n'))

    def test_diversity_6(self):
        self.assertEqual('from __future__ import division as _tzh\n', self.run_black('from __future__ import division as _tzh\n'))

    def test_diversity_7(self):
        self.assertEqual('from __future__ import division as _gtqrervj\n', self.run_black('from __future__ import division as _gtqrervj\n'))

    def test_diversity_8(self):
        self.assertEqual('from __future__ import generator_stop as _blfrxjic\n', self.run_black('from __future__ import generator_stop as _blfrxjic\n'))

    def test_diversity_9(self):
        self.assertEqual('from __future__ import generator_stop as _uscr\n', self.run_black('from __future__ import generator_stop as _uscr\n'))

    def test_diversity_10(self):
        self.assertEqual('from __future__ import generator_stop as _tvxfgajv\n', self.run_black('from __future__ import generator_stop as _tvxfgajv\n'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        try:
            return black.format_str(src, line_length=88)
        except TypeError:
            pass
        mode = None
        for attr in ('Mode', 'FileMode'):
            if hasattr(black, attr):
                try:
                    mode = getattr(black, attr)()
                except Exception:
                    mode = None
                break
        if mode is None:
            return black.format_str(src)
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertEqual('gixqz = 2\n', self.run_black('gixqz = 2\n'))

    def test_diversity_2(self):
        self.assertEqual('from __future__ import with_statement\n', self.run_black('from __future__ import with_statement\n'))

    def test_diversity_3(self):
        self.assertEqual('tdex = 8\n', self.run_black('tdex = 8\n'))

    def test_diversity_4(self):
        self.assertEqual('from __future__ import generator_stop, generators\n', self.run_black('from __future__ import generator_stop, generators\n'))

    def test_diversity_5(self):
        self.assertEqual('yfm = 4\n', self.run_black('yfm = 4\n'))

    def test_diversity_6(self):
        self.assertEqual('from __future__ import absolute_import, unicode_literals\n', self.run_black('from __future__ import absolute_import, unicode_literals\n'))

    def test_diversity_7(self):
        self.assertEqual('from __future__ import generators\n', self.run_black('from __future__ import generators\n'))

    def test_diversity_8(self):
        self.assertEqual('from __future__ import division\n', self.run_black('from __future__ import division\n'))

    def test_diversity_9(self):
        self.assertEqual('from __future__ import generator_stop, nested_scopes\n', self.run_black('from __future__ import generator_stop, nested_scopes\n'))

    def test_diversity_10(self):
        self.assertEqual('from __future__ import nested_scopes, absolute_import\n', self.run_black('from __future__ import nested_scopes, absolute_import\n'))
