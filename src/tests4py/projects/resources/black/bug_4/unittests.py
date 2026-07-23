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
        self.assertEqual('print("dseokr")\n', self.run_black('\\\n\n\n\n\n\n\nprint("dseokr")\n'))

    def test_diversity_2(self):
        self.assertEqual('iner = {"grmbiand": 15}\n', self.run_black('\\\n\n\n\n\n\niner = {"grmbiand": 15}\n'))

    def test_diversity_3(self):
        self.assertEqual('hqu = [1, 4, 98]\n', self.run_black('\\\n\n\n\n\n\nhqu = [1, 4, 98]\n'))

    def test_diversity_4(self):
        self.assertEqual('print("pqyua")\n', self.run_black('\\\n\n\nprint("pqyua")\n'))

    def test_diversity_5(self):
        self.assertEqual('gijanpp = {"oijctgyn": 29}\n', self.run_black('\\\n\n\n\ngijanpp = {"oijctgyn": 29}\n'))

    def test_diversity_6(self):
        self.assertEqual('wmyem = [32, 86, 92]\n', self.run_black('\\\n\n\n\nwmyem = [32, 86, 92]\n'))

    def test_diversity_7(self):
        self.assertEqual('hoixanb = 897\n', self.run_black('\\\n\n\n\nhoixanb = 897\n'))

    def test_diversity_8(self):
        self.assertEqual('fjeclnf = [12, 50, 67, 70]\n', self.run_black('\\\n\n\n\nfjeclnf = [12, 50, 67, 70]\n'))

    def test_diversity_9(self):
        self.assertEqual('kyw = 726\n', self.run_black('\\\n\n\n\n\nkyw = 726\n'))

    def test_diversity_10(self):
        self.assertEqual('ncinl = 615\n', self.run_black('\\\n\n\n\n\n\nncinl = 615\n'))

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
        self.assertEqual('print("hlgev")\n', self.run_black('print("hlgev")\n'))

    def test_diversity_2(self):
        self.assertEqual('imrvx = 37\n', self.run_black('imrvx = 37\n'))

    def test_diversity_3(self):
        self.assertEqual('def suhyrdww():\n    return 710\n', self.run_black('def suhyrdww():\n    return 710\n'))

    def test_diversity_4(self):
        self.assertEqual('juad = [25, 10]\n', self.run_black('juad = [25, 10]\n'))

    def test_diversity_5(self):
        self.assertEqual('dipqm = 252\n', self.run_black('\n\n\ndipqm = 252\n'))

    def test_diversity_6(self):
        self.assertEqual('print("mylocm")\n', self.run_black('print("mylocm")\n'))

    def test_diversity_7(self):
        self.assertEqual('print("xdk")\n', self.run_black('\n\nprint("xdk")\n'))

    def test_diversity_8(self):
        self.assertEqual('wegtmz = 92\n', self.run_black('wegtmz = 92\n'))

    def test_diversity_9(self):
        self.assertEqual('qutvnsyy = {"fwkcxq": 49}\n', self.run_black('\n\n\nqutvnsyy = {"fwkcxq": 49}\n'))

    def test_diversity_10(self):
        self.assertEqual('print("brpdft")\n', self.run_black('\nprint("brpdft")\n'))
