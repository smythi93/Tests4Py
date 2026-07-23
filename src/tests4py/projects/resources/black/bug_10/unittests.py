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
        self.assertEqual('if 2:\n    if 5:\n        wamwtw = 9\n    # wjvo\n    avo = 0\n', self.run_black('if 2:\n\tif 5:\n\t\twamwtw = 9\n\t# wjvo\n\tavo = 0\n'))

    def test_diversity_2(self):
        self.assertEqual('if 2:\n    if 2:\n        mqas = 9\n    # qmgj\n    pass\n', self.run_black('if 2:\n\tif 2:\n\t\tmqas = 9\n\t# qmgj\n\tpass\n'))

    def test_diversity_3(self):
        self.assertEqual('if 1:\n    if 4:\n        brmbwwp = 6\n    # lcqj\n    pass\n', self.run_black('if 1:\n\tif 4:\n\t\tbrmbwwp = 6\n\t# lcqj\n\tpass\n'))

    def test_diversity_4(self):
        self.assertEqual('if 3:\n    if 3:\n        pass\n    # bloajd\n    pass\n', self.run_black('if 3:\n\tif 3:\n\t\tpass\n\t# bloajd\n\tpass\n'))

    def test_diversity_5(self):
        self.assertEqual('if 4:\n    if 1:\n        via = 6\n    # hfwx\n    purzma = 5\n', self.run_black('if 4:\n\tif 1:\n\t\tvia = 6\n\t# hfwx\n\tpurzma = 5\n'))

    def test_diversity_6(self):
        self.assertEqual('if 1:\n    if 3:\n        mvunq = 3\n    # gxgg\n    pass\n', self.run_black('if 1:\n\tif 3:\n\t\tmvunq = 3\n\t# gxgg\n\tpass\n'))

    def test_diversity_7(self):
        self.assertEqual('if 3:\n    if 2:\n        pass\n    # lnue\n    pass\n', self.run_black('if 3:\n\tif 2:\n\t\tpass\n\t# lnue\n\tpass\n'))

    def test_diversity_8(self):
        self.assertEqual('if 4:\n    if 3:\n        pass\n    # krayn\n    pass\n', self.run_black('if 4:\n\tif 3:\n\t\tpass\n\t# krayn\n\tpass\n'))

    def test_diversity_9(self):
        self.assertEqual('if 1:\n    if 2:\n        pass\n    # jmb\n    yimzdryu = 4\n', self.run_black('if 1:\n\tif 2:\n\t\tpass\n\t# jmb\n\tyimzdryu = 4\n'))

    def test_diversity_10(self):
        self.assertEqual('if 1:\n    if 5:\n        pass\n    # xqh\n    pass\n', self.run_black('if 1:\n\tif 5:\n\t\tpass\n\t# xqh\n\tpass\n'))

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
        self.assertEqual('if 1:\n    if 3:\n        pass\n        # abhgls\n    pass\n', self.run_black('if 1:\n\tif 3:\n\t\tpass\n\t\t# abhgls\n\tpass\n'))

    def test_diversity_2(self):
        self.assertEqual('if 2:\n    if 1:\n        awdoiplf = 1\n        # abfcea\n    pass\n', self.run_black('if 2:\n    if 1:\n        awdoiplf = 1\n        # abfcea\n    pass\n'))

    def test_diversity_3(self):
        self.assertEqual('if 2:\n    if 4:\n        ltwvyk = 5\n        # ahsrmuu\n    pass\n', self.run_black('if 2:\n\tif 4:\n\t\tltwvyk = 5\n\t\t# ahsrmuu\n\tpass\n'))

    def test_diversity_4(self):
        self.assertEqual('if 5:\n    if 3:\n        vunzpvt = 9\n        # tfdjbdjb\n    pyvszzt = 3\n', self.run_black('if 5:\n\tif 3:\n\t\tvunzpvt = 9\n\t\t# tfdjbdjb\n\tpyvszzt = 3\n'))

    def test_diversity_5(self):
        self.assertEqual('if 3:\n    if 3:\n        pass\n        # kkbewtz\n    slik = 7\n', self.run_black('if 3:\n    if 3:\n        pass\n        # kkbewtz\n    slik = 7\n'))

    def test_diversity_6(self):
        self.assertEqual('if 5:\n    if 5:\n        brmchjo = 3\n        # vwql\n    pass\n', self.run_black('if 5:\n    if 5:\n        brmchjo = 3\n        # vwql\n    pass\n'))

    def test_diversity_7(self):
        self.assertEqual('if 4:\n    if 3:\n        bmlglfm = 3\n        # uffnllia\n    hkam = 2\n', self.run_black('if 4:\n    if 3:\n        bmlglfm = 3\n        # uffnllia\n    hkam = 2\n'))

    def test_diversity_8(self):
        self.assertEqual('if 2:\n    if 2:\n        xbaf = 0\n        # ufqdlqae\n    szndgg = 5\n', self.run_black('if 2:\n    if 2:\n        xbaf = 0\n        # ufqdlqae\n    szndgg = 5\n'))

    def test_diversity_9(self):
        self.assertEqual('if 5:\n    if 5:\n        pass\n        # cajcfd\n    pass\n', self.run_black('if 5:\n\tif 5:\n\t\tpass\n\t\t# cajcfd\n\tpass\n'))

    def test_diversity_10(self):
        self.assertEqual('if 5:\n    if 2:\n        hpqq = 6\n        # pvcc\n    cwst = 8\n', self.run_black('if 5:\n    if 2:\n        hpqq = 6\n        # pvcc\n    cwst = 8\n'))
