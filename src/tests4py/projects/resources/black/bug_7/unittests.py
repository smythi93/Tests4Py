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
        self.assertEqual('(\n    hrmgihhpvtxlrm,\n    bygyelvnykmaupxssagz,\n    xecrdcbocqaoww,\n    umddbkxsnlmlcgct,\n    vfmcrljhtiznbnwwxubr,\n    wrjofyzrrokbonetd,\n) = (2, 0, 9)\n', self.run_black('hrmgihhpvtxlrm, bygyelvnykmaupxssagz, xecrdcbocqaoww, umddbkxsnlmlcgct, vfmcrljhtiznbnwwxubr, wrjofyzrrokbonetd = 2, 0, 9\n'))

    def test_diversity_2(self):
        self.assertEqual('(\n    udtsudghvsufmwrdkel,\n    ygrxqscwcisnbndtsi,\n    fnqqaxtgdrpqytvr,\n    wypspltsljizgm,\n    yhbropnkjkegrrj,\n) = (8, 2, 6)\n', self.run_black('udtsudghvsufmwrdkel, ygrxqscwcisnbndtsi, fnqqaxtgdrpqytvr, wypspltsljizgm, yhbropnkjkegrrj = 8, 2, 6\n'))

    def test_diversity_3(self):
        self.assertEqual('(\n    zhqwnrcgwjlhrmvjkea,\n    vxukbwtdakzgmrwwzeih,\n    vezevqvwgtbemtluz,\n    abmwfpvcajfcel,\n    lmryibwdddrsmdjtluh,\n) = (9, 9, 3)\n', self.run_black('zhqwnrcgwjlhrmvjkea, vxukbwtdakzgmrwwzeih, vezevqvwgtbemtluz, abmwfpvcajfcel, lmryibwdddrsmdjtluh = 9, 9, 3\n'))

    def test_diversity_4(self):
        self.assertEqual('(\n    bdlkawrqitcdfrkdinp,\n    wbtwkvvnlqbkhe,\n    lfbapuozqkhiwhkpzoi,\n    hxjkabthonuvtmyvekq,\n    fvcehptygvwrwyrmnmge,\n    nfxlcqfsoszicpzfo,\n) = (3, 7, 5)\n', self.run_black('bdlkawrqitcdfrkdinp, wbtwkvvnlqbkhe, lfbapuozqkhiwhkpzoi, hxjkabthonuvtmyvekq, fvcehptygvwrwyrmnmge, nfxlcqfsoszicpzfo = 3, 7, 5\n'))

    def test_diversity_5(self):
        self.assertEqual('(\n    uhrjosdyquvwswdfpq,\n    oyoivenjodbxpzlde,\n    pdjrwgggmdgytvtehmsr,\n    nwuiqfuzkntbttrw,\n    nffwbblwrqlbqhkua,\n    vvwegxvoeadnbizs,\n) = (5, 1, 9)\n', self.run_black('uhrjosdyquvwswdfpq, oyoivenjodbxpzlde, pdjrwgggmdgytvtehmsr, nwuiqfuzkntbttrw, nffwbblwrqlbqhkua, vvwegxvoeadnbizs = 5, 1, 9\n'))

    def test_diversity_6(self):
        self.assertEqual('(\n    ajkvzjzkivkvkftazqcs,\n    burhwgvjikfvwai,\n    wdphfqyjqwsowzavx,\n    suclmezegygfoh,\n    lfnjrsetpylwny,\n) = (9, 6, 7)\n', self.run_black('ajkvzjzkivkvkftazqcs, burhwgvjikfvwai, wdphfqyjqwsowzavx, suclmezegygfoh, lfnjrsetpylwny = 9, 6, 7\n'))

    def test_diversity_7(self):
        self.assertEqual('(\n    kawutccatasaqq,\n    yfoqdxhiromxoh,\n    qseulkjazsazcmuzlded,\n    ogjbwrstirtgtzzr,\n    feztqniahnnsyt,\n) = (2, 6, 8)\n', self.run_black('kawutccatasaqq, yfoqdxhiromxoh, qseulkjazsazcmuzlded, ogjbwrstirtgtzzr, feztqniahnnsyt = 2, 6, 8\n'))

    def test_diversity_8(self):
        self.assertEqual('(\n    ysggeaowtbiykcycd,\n    xylyecrydkvoqyb,\n    qjplqzilwtwlfjocpbnb,\n    naramqqjmzicnapja,\n    fynqmbnhhvoynefvq,\n    lmhwtqpbyqskfzntxu,\n) = (6, 0, 8)\n', self.run_black('ysggeaowtbiykcycd, xylyecrydkvoqyb, qjplqzilwtwlfjocpbnb, naramqqjmzicnapja, fynqmbnhhvoynefvq, lmhwtqpbyqskfzntxu = 6, 0, 8\n'))

    def test_diversity_9(self):
        self.assertEqual('(\n    yuvudnepbaruuhnxysvg,\n    svocaphpmbcartohi,\n    wwobgdrsbmivifuji,\n    uyxonhkskbsyjgsokdsp,\n    grqxkbikkajbxedkpmp,\n) = (6, 7, 5)\n', self.run_black('yuvudnepbaruuhnxysvg, svocaphpmbcartohi, wwobgdrsbmivifuji, uyxonhkskbsyjgsokdsp, grqxkbikkajbxedkpmp = 6, 7, 5\n'))

    def test_diversity_10(self):
        self.assertEqual('(\n    lwddzlrxiqpcele,\n    hzfwnejobtalsj,\n    xwncmwloacjineqxvwxy,\n    yrelyvbfbuuhedjrpkv,\n    tsthlcxsjvixdwesms,\n) = (9, 3, 6)\n', self.run_black('lwddzlrxiqpcele, hzfwnejobtalsj, xwncmwloacjineqxvwxy, yrelyvbfbuuhedjrpkv, tsthlcxsjvixdwesms = 9, 3, 6\n'))

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
        self.assertEqual('hxcg = 691\n', self.run_black('hxcg = 691\n'))

    def test_diversity_2(self):
        self.assertEqual('jbivrq = 464\n', self.run_black('jbivrq = 464\n'))

    def test_diversity_3(self):
        self.assertEqual('vdjos = {"pieexu": 80}\n', self.run_black('vdjos = {"pieexu": 80}\n'))

    def test_diversity_4(self):
        self.assertEqual('uabuakz = 328\n', self.run_black('uabuakz = 328\n'))

    def test_diversity_5(self):
        self.assertEqual('moo = 192\n', self.run_black('moo = 192\n'))

    def test_diversity_6(self):
        self.assertEqual('def hcmsi():\n    return 35\n', self.run_black('def hcmsi():\n    return 35\n'))

    def test_diversity_7(self):
        self.assertEqual('def dmfpoggw():\n    return 432\n', self.run_black('def dmfpoggw():\n    return 432\n'))

    def test_diversity_8(self):
        self.assertEqual('tucak = {"tqionqm": 55}\n', self.run_black('tucak = {"tqionqm": 55}\n'))

    def test_diversity_9(self):
        self.assertEqual('bklduh, bavn = 2, 4\n', self.run_black('bklduh, bavn = 2, 4\n'))

    def test_diversity_10(self):
        self.assertEqual('gtuwxmaw, ucl = 5, 0\n', self.run_black('gtuwxmaw, ucl = 5, 0\n'))
