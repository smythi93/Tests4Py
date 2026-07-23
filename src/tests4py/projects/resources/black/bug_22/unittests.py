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
        self.assertEqual('blds = vtold(\n    # before comment here\n    excgn.imhztkb(\n        uqad=17,\n        qtnhoh=84,\n        # keep this internal comment intact\n        ilzo=7,\n    )\n    # after comment here\n)\n', self.run_black('blds = vtold(\n    # before comment here\n    excgn.imhztkb(\n        uqad=17,\n        qtnhoh=84,\n        # keep this internal comment intact\n        ilzo=7,\n    )\n    # after comment here\n)\n'))

    def test_diversity_2(self):
        self.assertEqual('mfuzw = kfhbdm(\n    # before comment here\n    chfnpn.jjt(\n        bahacv=86,\n        jkx=48,\n        # keep this internal comment intact\n        nayreo=6,\n    )\n    # after comment here\n)\n', self.run_black('mfuzw = kfhbdm(\n    # before comment here\n    chfnpn.jjt(\n        bahacv=86,\n        jkx=48,\n        # keep this internal comment intact\n        nayreo=6,\n    )\n    # after comment here\n)\n'))

    def test_diversity_3(self):
        self.assertEqual('efr = tuc(\n    # before comment here\n    kjcg.uoizihxq(\n        diljplew=15,\n        dprby=29,\n        # keep this internal comment intact\n        iascsj=61,\n    )\n    # after comment here\n)\n', self.run_black('efr = tuc(\n    # before comment here\n    kjcg.uoizihxq(\n        diljplew=15,\n        dprby=29,\n        # keep this internal comment intact\n        iascsj=61,\n    )\n    # after comment here\n)\n'))

    def test_diversity_4(self):
        self.assertEqual('tvckn = nuc(\n    # before comment here\n    olb.knar(\n        qhfmuhce=88,\n        gbjkupdk=45,\n        # keep this internal comment intact\n        erem=95,\n    )\n    # after comment here\n)\n', self.run_black('tvckn = nuc(\n    # before comment here\n    olb.knar(\n        qhfmuhce=88,\n        gbjkupdk=45,\n        # keep this internal comment intact\n        erem=95,\n    )\n    # after comment here\n)\n'))

    def test_diversity_5(self):
        self.assertEqual('qov = iajg(\n    # before comment here\n    mlgoy.ujuupp(\n        yonbvam=79,\n        xyml=34,\n        # keep this internal comment intact\n        lepimlta=26,\n    )\n    # after comment here\n)\n', self.run_black('qov = iajg(\n    # before comment here\n    mlgoy.ujuupp(\n        yonbvam=79,\n        xyml=34,\n        # keep this internal comment intact\n        lepimlta=26,\n    )\n    # after comment here\n)\n'))

    def test_diversity_6(self):
        self.assertEqual('tqwpjw = lubpdf(\n    # before comment here\n    cjy.ajcukdbm(\n        sern=89,\n        gaqiwhnb=31,\n        # keep this internal comment intact\n        wdpq=63,\n    )\n    # after comment here\n)\n', self.run_black('tqwpjw = lubpdf(\n    # before comment here\n    cjy.ajcukdbm(\n        sern=89,\n        gaqiwhnb=31,\n        # keep this internal comment intact\n        wdpq=63,\n    )\n    # after comment here\n)\n'))

    def test_diversity_7(self):
        self.assertEqual('oijnhpjz = cmmf(\n    # before comment here\n    gio.oec(\n        tbkrhk=14,\n        nxzmn=15,\n        # keep this internal comment intact\n        lpmzoky=34,\n    )\n    # after comment here\n)\n', self.run_black('oijnhpjz = cmmf(\n    # before comment here\n    gio.oec(\n        tbkrhk=14,\n        nxzmn=15,\n        # keep this internal comment intact\n        lpmzoky=34,\n    )\n    # after comment here\n)\n'))

    def test_diversity_8(self):
        self.assertEqual('zveivx = lsbnij(\n    # before comment here\n    ygr.skxsdbae(\n        frhp=59,\n        fgcpx=98,\n        # keep this internal comment intact\n        rvzjipt=10,\n    )\n    # after comment here\n)\n', self.run_black('zveivx = lsbnij(\n    # before comment here\n    ygr.skxsdbae(\n        frhp=59,\n        fgcpx=98,\n        # keep this internal comment intact\n        rvzjipt=10,\n    )\n    # after comment here\n)\n'))

    def test_diversity_9(self):
        self.assertEqual('echngxj = nkqkkrsu(\n    # before comment here\n    mnzrprnq.dialie(\n        snniwh=72,\n        czl=50,\n        # keep this internal comment intact\n        yyko=35,\n    )\n    # after comment here\n)\n', self.run_black('echngxj = nkqkkrsu(\n    # before comment here\n    mnzrprnq.dialie(\n        snniwh=72,\n        czl=50,\n        # keep this internal comment intact\n        yyko=35,\n    )\n    # after comment here\n)\n'))

    def test_diversity_10(self):
        self.assertEqual('pfrqakpp = sok(\n    # before comment here\n    rzpcy.zhbwbm(\n        ktsoj=22,\n        jrbgfhho=78,\n        # keep this internal comment intact\n        smq=81,\n    )\n    # after comment here\n)\n', self.run_black('pfrqakpp = sok(\n    # before comment here\n    rzpcy.zhbwbm(\n        ktsoj=22,\n        jrbgfhho=78,\n        # keep this internal comment intact\n        smq=81,\n    )\n    # after comment here\n)\n'))

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
        self.assertEqual('yciwmv = [38, 98, 3, 76]\n', self.run_black('yciwmv = [38, 98, 3, 76]\n'))

    def test_diversity_2(self):
        self.assertEqual('mjbshjuo = txcg(abxqcucn, qrdnw)  # trailing comment\n', self.run_black('mjbshjuo = txcg(abxqcucn, qrdnw)  # trailing comment\n'))

    def test_diversity_3(self):
        self.assertEqual('uxbr = qwykm(\n    chemd,\n    # inner comment\n    cloedf,\n)\n', self.run_black('uxbr = qwykm(\n    chemd,\n    # inner comment\n    cloedf,\n)\n'))

    def test_diversity_4(self):
        self.assertEqual('wjyoolab = rrpao(dfug, zcvh)  # trailing comment\n', self.run_black('wjyoolab = rrpao(dfug, zcvh)  # trailing comment\n'))

    def test_diversity_5(self):
        self.assertEqual('uzeeuzm = wvnxi(gocc, fzhd)  # trailing comment\n', self.run_black('uzeeuzm = wvnxi(gocc, fzhd)  # trailing comment\n'))

    def test_diversity_6(self):
        self.assertEqual('ilken = jpveki(dqjuz, wivxhagt)  # trailing comment\n', self.run_black('ilken = jpveki(dqjuz, wivxhagt)  # trailing comment\n'))

    def test_diversity_7(self):
        self.assertEqual('dvtczhr = cnrnzla(\n    xtxdco,\n    # inner comment\n    rur,\n)\n', self.run_black('dvtczhr = cnrnzla(\n    xtxdco,\n    # inner comment\n    rur,\n)\n'))

    def test_diversity_8(self):
        self.assertEqual('sujc = kmdtct(\n    yvmj,\n    # inner comment\n    ktrwbxc,\n)\n', self.run_black('sujc = kmdtct(\n    yvmj,\n    # inner comment\n    ktrwbxc,\n)\n'))

    def test_diversity_9(self):
        self.assertEqual('nsukm = [96, 71, 1, 81]\n', self.run_black('nsukm = [96, 71, 1, 81]\n'))

    def test_diversity_10(self):
        self.assertEqual('xdsts = nbgn(bjmoroy, umydasi)  # trailing comment\n', self.run_black('xdsts = nbgn(bjmoroy, umydasi)  # trailing comment\n'))
