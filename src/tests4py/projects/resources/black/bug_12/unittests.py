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
        self.assertEqual('for ((mgzomtuj in {}) or {})[1] in qihfod:\n    igqnby = 2\n', self.run_black('for ((mgzomtuj in {}) or {})[1] in qihfod:\n    igqnby = 2\n'))

    def test_diversity_2(self):
        self.assertEqual('for ((kwcfeycs in {}) or {})[2] in zhe:\n    pass\n', self.run_black('for ((kwcfeycs in {}) or {})[2] in zhe:\n    pass\n'))

    def test_diversity_3(self):
        self.assertEqual('for ((tgcdxb in {}) or {})["fjrs"] in vhvnyha:\n    hldefsgz = 4\n', self.run_black('for ((tgcdxb in {}) or {})["fjrs"] in vhvnyha:\n    hldefsgz = 4\n'))

    def test_diversity_4(self):
        self.assertEqual('for ((asl in {}) or {})["mmb"] in fon:\n    kvosaup = 6\n', self.run_black('for ((asl in {}) or {})["mmb"] in fon:\n    kvosaup = 6\n'))

    def test_diversity_5(self):
        self.assertEqual('for ((iawjtzv in {}) or {})["bfxogee"] in xac:\n    zecrteb = 0\n', self.run_black('for ((iawjtzv in {}) or {})["bfxogee"] in xac:\n    zecrteb = 0\n'))

    def test_diversity_6(self):
        self.assertEqual('for ((procpals in {}) or {})["prtpokcm"] in ufkt:\n    pass\n', self.run_black('for ((procpals in {}) or {})["prtpokcm"] in ufkt:\n    pass\n'))

    def test_diversity_7(self):
        self.assertEqual('for ((rgzv in {}) or {})[7] in ewtm:\n    pass\n', self.run_black('for ((rgzv in {}) or {})[7] in ewtm:\n    pass\n'))

    def test_diversity_8(self):
        self.assertEqual('for ((wnjrypye in {}) or {})["nuwmr"] in refyk:\n    qpd = 5\n', self.run_black('for ((wnjrypye in {}) or {})["nuwmr"] in refyk:\n    qpd = 5\n'))

    def test_diversity_9(self):
        self.assertEqual('for ((eiwrdjr in {}) or {})["tycrgenk"] in nmwrohe:\n    pass\n', self.run_black('for ((eiwrdjr in {}) or {})["tycrgenk"] in nmwrohe:\n    pass\n'))

    def test_diversity_10(self):
        self.assertEqual('for ((etaxwv in {}) or {})["qnh"] in ymwbbi:\n    dcqmqlx = 5\n', self.run_black('for ((etaxwv in {}) or {})["qnh"] in ymwbbi:\n    dcqmqlx = 5\n'))

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
        self.assertEqual('dexuzu = lambda fsbzeiz: 9\n', self.run_black('dexuzu = lambda fsbzeiz: 9\n'))

    def test_diversity_2(self):
        self.assertEqual('for lktvuk in gxwt:\n    pass\n', self.run_black('for lktvuk in gxwt:\n    pass\n'))

    def test_diversity_3(self):
        self.assertEqual('for pevw in ppbbyjbg:\n    pass\n', self.run_black('for pevw in ppbbyjbg:\n    pass\n'))

    def test_diversity_4(self):
        self.assertEqual('for ahuzq in yxsuv:\n    pass\n', self.run_black('for ahuzq in yxsuv:\n    pass\n'))

    def test_diversity_5(self):
        self.assertEqual('for kwq in cjl:\n    pass\n', self.run_black('for kwq in cjl:\n    pass\n'))

    def test_diversity_6(self):
        self.assertEqual('djxh = 44\n', self.run_black('djxh = 44\n'))

    def test_diversity_7(self):
        self.assertEqual('zyyi = lambda mszu: 6\n', self.run_black('zyyi = lambda mszu: 6\n'))

    def test_diversity_8(self):
        self.assertEqual('for fkkcaxz in rjmrf:\n    pass\n', self.run_black('for fkkcaxz in rjmrf:\n    pass\n'))

    def test_diversity_9(self):
        self.assertEqual('iqvxun = {"ruggf": 8}\n', self.run_black('iqvxun = {"ruggf": 8}\n'))

    def test_diversity_10(self):
        self.assertEqual('ctlq = lambda xukfw: 9\n', self.run_black('ctlq = lambda xukfw: 9\n'))
