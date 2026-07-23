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
        self.assertEqual('from ivrag import (\n    kyseu,\n    invpn,\n    rijsxmrc,\n    #  bfghqmm\n    #  brqju\n)\n', self.run_black('from ivrag import (\n    kyseu,\n    invpn,\n    rijsxmrc,\n    #  bfghqmm\n    #  brqju\n)\n'))

    def test_diversity_2(self):
        self.assertEqual('from ykfhmzyo import (\n    pwiqwp,\n    slhc,\n    xrzdjs,\n    #  ehuhieg\n    #  sdib\n)\n', self.run_black('from ykfhmzyo import (\n    pwiqwp,\n    slhc,\n    xrzdjs,\n    #  ehuhieg\n    #  sdib\n)\n'))

    def test_diversity_3(self):
        self.assertEqual('from jlsvuzx import (\n    wwqki,\n    cofniut,\n    #  scatixi\n    #  qbzlblnv\n)\n', self.run_black('from jlsvuzx import (\n    wwqki,\n    cofniut,\n    #  scatixi\n    #  qbzlblnv\n)\n'))

    def test_diversity_4(self):
        self.assertEqual('from kpw import (\n    dutb,\n    tkorchg,\n    #  fkvkkuwc\n    #  whvoep\n)\n', self.run_black('from kpw import (\n    dutb,\n    tkorchg,\n    #  fkvkkuwc\n    #  whvoep\n)\n'))

    def test_diversity_5(self):
        self.assertEqual('from bxar import (\n    humbfrx,\n    jkof,\n    ndbhqtsy,\n    #  nbokdg\n    #  pzgj\n)\n', self.run_black('from bxar import (\n    humbfrx,\n    jkof,\n    ndbhqtsy,\n    #  nbokdg\n    #  pzgj\n)\n'))

    def test_diversity_6(self):
        self.assertEqual('from zyro import (\n    tdtfbt,\n    psymj,\n    mkx,\n    dnwof,\n    #  geg\n    #  wdtrclw\n)\n', self.run_black('from zyro import (\n    tdtfbt,\n    psymj,\n    mkx,\n    dnwof,\n    #  geg\n    #  wdtrclw\n)\n'))

    def test_diversity_7(self):
        self.assertEqual('from bwxygiml import (\n    qnc,\n    eyejxr,\n    rip,\n    #  mquk\n    #  alnx\n)\n', self.run_black('from bwxygiml import (\n    qnc,\n    eyejxr,\n    rip,\n    #  mquk\n    #  alnx\n)\n'))

    def test_diversity_8(self):
        self.assertEqual('from uql import (\n    rpaknsko,\n    zdzqeq,\n    vstjs,\n    pkyqugib,\n    #  cokaf\n)\n', self.run_black('from uql import (\n    rpaknsko,\n    zdzqeq,\n    vstjs,\n    pkyqugib,\n    #  cokaf\n)\n'))

    def test_diversity_9(self):
        self.assertEqual('from gmikgk import (\n    eupomhv,\n    dshcgsd,\n    xrh,\n    #  mwjpozho\n    #  bgn\n)\n', self.run_black('from gmikgk import (\n    eupomhv,\n    dshcgsd,\n    xrh,\n    #  mwjpozho\n    #  bgn\n)\n'))

    def test_diversity_10(self):
        self.assertEqual('from zaknnnh import (\n    osglgw,\n    eojjjxs,\n    vmuy,\n    #  loxor\n    #  myohvex\n)\n', self.run_black('from zaknnnh import (\n    osglgw,\n    eojjjxs,\n    vmuy,\n    #  loxor\n    #  myohvex\n)\n'))

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
        self.assertEqual('import ilwjgvd\n', self.run_black('import ilwjgvd\n'))

    def test_diversity_2(self):
        self.assertEqual('from uybhncrd import vuntm, ibfhf\n', self.run_black('from uybhncrd import vuntm, ibfhf\n'))

    def test_diversity_3(self):
        self.assertEqual('from rph import qymk, oqxpnim\n', self.run_black('from rph import qymk, oqxpnim\n'))

    def test_diversity_4(self):
        self.assertEqual('from wqe import qqvlo, kujewp\n', self.run_black('from wqe import qqvlo, kujewp\n'))

    def test_diversity_5(self):
        self.assertEqual('knnv = [33, 99, 31, 80]\n', self.run_black('knnv = [33, 99, 31, 80]\n'))

    def test_diversity_6(self):
        self.assertEqual('print("forbfpb")\n', self.run_black('print("forbfpb")\n'))

    def test_diversity_7(self):
        self.assertEqual('xbth = 153\n', self.run_black('xbth = 153\n'))

    def test_diversity_8(self):
        self.assertEqual('import fdygnmw\n', self.run_black('import fdygnmw\n'))

    def test_diversity_9(self):
        self.assertEqual('import pujunb\n', self.run_black('import pujunb\n'))

    def test_diversity_10(self):
        self.assertEqual('obymha = 658\n', self.run_black('obymha = 658\n'))
