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
        self.assertEqual('print bnhbq, svdwtvlm\n', self.run_black('print bnhbq, svdwtvlm\n'))

    def test_diversity_2(self):
        self.assertEqual('print "tirow"\n', self.run_black('print "tirow"\n'))

    def test_diversity_3(self):
        self.assertEqual('print "qckpcipe"\n', self.run_black('print "qckpcipe"\n'))

    def test_diversity_4(self):
        self.assertEqual('print imvdd, ldv\n', self.run_black('print imvdd, ldv\n'))

    def test_diversity_5(self):
        self.assertEqual('print ihm, jrnuqgga\n', self.run_black('print ihm, jrnuqgga\n'))

    def test_diversity_6(self):
        self.assertEqual('print yzvm, soqmfkh\n', self.run_black('print yzvm, soqmfkh\n'))

    def test_diversity_7(self):
        self.assertEqual('print "gqch"\n', self.run_black('print "gqch"\n'))

    def test_diversity_8(self):
        self.assertEqual('print nxika\n', self.run_black('print nxika\n'))

    def test_diversity_9(self):
        self.assertEqual('print xqotrwke, ykhuq\n', self.run_black('print xqotrwke, ykhuq\n'))

    def test_diversity_10(self):
        self.assertEqual('print "itc"\n', self.run_black('print "itc"\n'))

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
        self.assertEqual('zefmb = 3\n', self.run_black('zefmb = 3\n'))

    def test_diversity_2(self):
        self.assertEqual('wtybfyu = 4\n', self.run_black('wtybfyu = 4\n'))

    def test_diversity_3(self):
        self.assertEqual('print("emxovf")\n', self.run_black('print("emxovf")\n'))

    def test_diversity_4(self):
        self.assertEqual('def ogrpz(bhmbir):\n    return 5\n', self.run_black('def ogrpz(bhmbir):\n    return 5\n'))

    def test_diversity_5(self):
        self.assertEqual('print("xenlji")\n', self.run_black('print("xenlji")\n'))

    def test_diversity_6(self):
        self.assertEqual('def xzrrrqq(rksbhp):\n    return 1\n', self.run_black('def xzrrrqq(rksbhp):\n    return 1\n'))

    def test_diversity_7(self):
        self.assertEqual('enqigan = 2\n', self.run_black('enqigan = 2\n'))

    def test_diversity_8(self):
        self.assertEqual('def pxpyp(zyqib):\n    return 4\n', self.run_black('def pxpyp(zyqib):\n    return 4\n'))

    def test_diversity_9(self):
        self.assertEqual('def rualztc(bpwrunw):\n    return 3\n', self.run_black('def rualztc(bpwrunw):\n    return 3\n'))

    def test_diversity_10(self):
        self.assertEqual('print("rkqppgjl")\n', self.run_black('print("rkqppgjl")\n'))
