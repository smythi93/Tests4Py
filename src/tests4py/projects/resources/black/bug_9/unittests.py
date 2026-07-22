import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        mode = black.FileMode(target_versions={black.TargetVersion.PY27})
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertEqual('from __future__ import print_function\n\nprint(tqcroh, uetl, file=sys.stderr)\n', self.run_black('from __future__ import print_function\n\nprint(tqcroh, uetl, file=sys.stderr)\n'))

    def test_diversity_2(self):
        self.assertEqual('from __future__ import print_function\n\nprint(tfdob, tdpsj, end="")\n', self.run_black('from __future__ import print_function\n\nprint(tfdob, tdpsj, end="")\n'))

    def test_diversity_3(self):
        self.assertEqual('from __future__ import print_function\n\nprint(umqgjctq, ceodv, sep=", ")\n', self.run_black('from __future__ import print_function\n\nprint(umqgjctq, ceodv, sep=", ")\n'))

    def test_diversity_4(self):
        self.assertEqual('from __future__ import print_function\n\nprint(jqqomc, end="")\n', self.run_black('from __future__ import print_function\n\nprint(jqqomc, end="")\n'))

    def test_diversity_5(self):
        self.assertEqual('from __future__ import print_function\n\nprint(fap, end="")\n', self.run_black('from __future__ import print_function\n\nprint(fap, end="")\n'))

    def test_diversity_6(self):
        self.assertEqual('from __future__ import print_function\n\nprint(zuigscsa, winnwz, file=sys.stderr)\n', self.run_black('from __future__ import print_function\n\nprint(zuigscsa, winnwz, file=sys.stderr)\n'))

    def test_diversity_7(self):
        self.assertEqual('from __future__ import print_function\n\nprint(lgyh, nxxi, file=sys.stderr)\n', self.run_black('from __future__ import print_function\n\nprint(lgyh, nxxi, file=sys.stderr)\n'))

    def test_diversity_8(self):
        self.assertEqual('from __future__ import print_function\n\nprint(pelqzsjj, ofmrur, file=sys.stderr)\n', self.run_black('from __future__ import print_function\n\nprint(pelqzsjj, ofmrur, file=sys.stderr)\n'))

    def test_diversity_9(self):
        self.assertEqual('from __future__ import print_function\n\nprint(feoad, optlq, esns, flush=True)\n', self.run_black('from __future__ import print_function\n\nprint(feoad, optlq, esns, flush=True)\n'))

    def test_diversity_10(self):
        self.assertEqual('from __future__ import print_function\n\nprint(yrwxkdn, yleuq, ksjgx, sep=", ")\n', self.run_black('from __future__ import print_function\n\nprint(yrwxkdn, yleuq, ksjgx, sep=", ")\n'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        mode = black.FileMode(target_versions={black.TargetVersion.PY27})
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertEqual('dogzu = 7\n', self.run_black('dogzu = 7\n'))

    def test_diversity_2(self):
        self.assertEqual('qlc = [2, 8]\n', self.run_black('qlc = [2, 8]\n'))

    def test_diversity_3(self):
        self.assertEqual('def sfsj(dgzcvdk):\n    return 0\n', self.run_black('def sfsj(dgzcvdk):\n    return 0\n'))

    def test_diversity_4(self):
        self.assertEqual('hjbcnqw = [3, 5]\n', self.run_black('hjbcnqw = [3, 5]\n'))

    def test_diversity_5(self):
        self.assertEqual('fcroj = 2\n', self.run_black('fcroj = 2\n'))

    def test_diversity_6(self):
        self.assertEqual('rmf = 0\n', self.run_black('rmf = 0\n'))

    def test_diversity_7(self):
        self.assertEqual('def lfbikrb(nmjpsvl):\n    return 2\n', self.run_black('def lfbikrb(nmjpsvl):\n    return 2\n'))

    def test_diversity_8(self):
        self.assertEqual('xyq = [2, 1]\n', self.run_black('xyq = [2, 1]\n'))

    def test_diversity_9(self):
        self.assertEqual('quighxtj = 5\n', self.run_black('quighxtj = 5\n'))

    def test_diversity_10(self):
        self.assertEqual('def ahmpw(rrtqx):\n    return 0\n', self.run_black('def ahmpw(rrtqx):\n    return 0\n'))
