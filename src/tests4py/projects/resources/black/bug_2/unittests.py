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
        self.assertEqual('# fmt: off\n@register([\n    2, 3,\n    0, 0,\n])\n# fmt: on\ndef dwzkdtf():\n    pass\n', self.run_black('# fmt: off\n@register([\n    2, 3,\n    0, 0,\n])\n# fmt: on\ndef dwzkdtf(): pass\n'))

    def test_diversity_2(self):
        self.assertEqual('# fmt: off\n@route([\n    1, 1,\n    4, 8,\n])\n# fmt: on\ndef kee():\n    pass\n', self.run_black('# fmt: off\n@route([\n    1, 1,\n    4, 8,\n])\n# fmt: on\ndef kee(): pass\n'))

    def test_diversity_3(self):
        self.assertEqual('# fmt: off\n@test([\n    6, 9,\n    3, 1,\n])\n# fmt: on\ndef uyy():\n    pass\n', self.run_black('# fmt: off\n@test([\n    6, 9,\n    3, 1,\n])\n# fmt: on\ndef uyy(): pass\n'))

    def test_diversity_4(self):
        self.assertEqual('# fmt: off\n@route([\n    7, 1,\n    7, 0,\n])\n# fmt: on\ndef cclcj():\n    pass\n', self.run_black('# fmt: off\n@route([\n    7, 1,\n    7, 0,\n])\n# fmt: on\ndef cclcj(): pass\n'))

    def test_diversity_5(self):
        self.assertEqual('# fmt: off\n@test([\n    2, 3,\n    2, 6,\n])\n# fmt: on\ndef gjacwfm():\n    pass\n', self.run_black('# fmt: off\n@test([\n    2, 3,\n    2, 6,\n])\n# fmt: on\ndef gjacwfm(): pass\n'))

    def test_diversity_6(self):
        self.assertEqual('# fmt: off\n@check([\n    3, 8,\n    3, 8,\n])\n# fmt: on\ndef dot():\n    pass\n', self.run_black('# fmt: off\n@check([\n    3, 8,\n    3, 8,\n])\n# fmt: on\ndef dot(): pass\n'))

    def test_diversity_7(self):
        self.assertEqual('# fmt: off\n@check([\n    0, 9,\n    5, 4,\n])\n# fmt: on\ndef dtnmxth():\n    pass\n', self.run_black('# fmt: off\n@check([\n    0, 9,\n    5, 4,\n])\n# fmt: on\ndef dtnmxth(): pass\n'))

    def test_diversity_8(self):
        self.assertEqual('# fmt: off\n@test([\n    6, 3,\n    2, 7,\n])\n# fmt: on\ndef iitrgdj():\n    pass\n', self.run_black('# fmt: off\n@test([\n    6, 3,\n    2, 7,\n])\n# fmt: on\ndef iitrgdj(): pass\n'))

    def test_diversity_9(self):
        self.assertEqual('# fmt: off\n@test([\n    3, 5,\n    7, 0,\n])\n# fmt: on\ndef tjj():\n    pass\n', self.run_black('# fmt: off\n@test([\n    3, 5,\n    7, 0,\n])\n# fmt: on\ndef tjj(): pass\n'))

    def test_diversity_10(self):
        self.assertEqual('# fmt: off\n@check([\n    6, 8,\n    1, 6,\n])\n# fmt: on\ndef qpwa():\n    pass\n', self.run_black('# fmt: off\n@check([\n    6, 8,\n    1, 6,\n])\n# fmt: on\ndef qpwa(): pass\n'))

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
        self.assertEqual('# fmt: off\n@route([\n    2, 4,\n    1, 1,\n])\n# fmt: on\ndef gocxwzj():\n    pass\n', self.run_black('# fmt: off\n@route([\n    2, 4,\n    1, 1,\n])\n# fmt: on\ndef gocxwzj():\n    pass\n'))

    def test_diversity_2(self):
        self.assertEqual('# fmt: off\n@wrap([\n    0, 5,\n    2, 0,\n])\n# fmt: on\ndef ttqo():\n    pass\n', self.run_black('# fmt: off\n@wrap([\n    0, 5,\n    2, 0,\n])\n# fmt: on\ndef ttqo():\n    pass\n'))

    def test_diversity_3(self):
        self.assertEqual('# fmt: off\n@cache([\n    4, 6,\n    9, 6,\n])\n# fmt: on\ndef digigzu():\n    pass\n', self.run_black('# fmt: off\n@cache([\n    4, 6,\n    9, 6,\n])\n# fmt: on\ndef digigzu():\n    pass\n'))

    def test_diversity_4(self):
        self.assertEqual('# fmt: off\n@test([\n    8, 0,\n    8, 8,\n])\n# fmt: on\ndef ygbx():\n    pass\n', self.run_black('# fmt: off\n@test([\n    8, 0,\n    8, 8,\n])\n# fmt: on\ndef ygbx():\n    pass\n'))

    def test_diversity_5(self):
        self.assertEqual('# fmt: off\n@route([\n    1, 8,\n    7, 5,\n])\n# fmt: on\ndef dzbaiufd():\n    pass\n', self.run_black('# fmt: off\n@route([\n    1, 8,\n    7, 5,\n])\n# fmt: on\ndef dzbaiufd():\n    pass\n'))

    def test_diversity_6(self):
        self.assertEqual('# fmt: off\n@given([\n    5, 1,\n    7, 5,\n])\n# fmt: on\ndef gzkhkwg():\n    pass\n', self.run_black('# fmt: off\n@given([\n    5, 1,\n    7, 5,\n])\n# fmt: on\ndef gzkhkwg():\n    pass\n'))

    def test_diversity_7(self):
        self.assertEqual('# fmt: off\n@register([\n    4, 2,\n    8, 7,\n])\n# fmt: on\ndef huye():\n    pass\n', self.run_black('# fmt: off\n@register([\n    4, 2,\n    8, 7,\n])\n# fmt: on\ndef huye():\n    pass\n'))

    def test_diversity_8(self):
        self.assertEqual('# fmt: off\n@test([\n    1, 5,\n    6, 7,\n])\n# fmt: on\ndef ragolbln():\n    pass\n', self.run_black('# fmt: off\n@test([\n    1, 5,\n    6, 7,\n])\n# fmt: on\ndef ragolbln():\n    pass\n'))

    def test_diversity_9(self):
        self.assertEqual('# fmt: off\n@cache([\n    0, 5,\n    4, 3,\n])\n# fmt: on\ndef wmc():\n    pass\n', self.run_black('# fmt: off\n@cache([\n    0, 5,\n    4, 3,\n])\n# fmt: on\ndef wmc():\n    pass\n'))

    def test_diversity_10(self):
        self.assertEqual('# fmt: off\n@given([\n    2, 3,\n    6, 2,\n])\n# fmt: on\ndef aneotdz():\n    pass\n', self.run_black('# fmt: off\n@given([\n    2, 3,\n    6, 2,\n])\n# fmt: on\ndef aneotdz():\n    pass\n'))
