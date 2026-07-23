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
        self.assertEqual('def ppcxsn(\n    rabyslkwpolxmnrtmeplnavsevpwnaxjzpoiiyefcavuiddyhplchmlhquitrqdqbxdnvzgdmeynsfryhzaaz,\n):\n    ...\n', self.run_black('def ppcxsn(rabyslkwpolxmnrtmeplnavsevpwnaxjzpoiiyefcavuiddyhplchmlhquitrqdqbxdnvzgdmeynsfryhzaaz):\n    ...\n'))

    def test_diversity_2(self):
        self.assertEqual('def zrzsy(\n    qptfxqqzfcuxlrxtxzwwcnjzwlqixuvormabjhsooqhjpmozcnsxqzulpocemiiqbhhnfenncrmsgexcmvdkjqp,\n):\n    ...\n', self.run_black('def zrzsy(qptfxqqzfcuxlrxtxzwwcnjzwlqixuvormabjhsooqhjpmozcnsxqzulpocemiiqbhhnfenncrmsgexcmvdkjqp):\n    ...\n'))

    def test_diversity_3(self):
        self.assertEqual('def fhh(\n    wojorgbwcxrxybwraosovoyyuvlujiyhxvawsnlsmwdfgyvajkdjbdzrengqfknclhihxzewpdojqsmsricqtscancn,\n):\n    ...\n', self.run_black('def fhh(wojorgbwcxrxybwraosovoyyuvlujiyhxvawsnlsmwdfgyvajkdjbdzrengqfknclhihxzewpdojqsmsricqtscancn):\n    ...\n'))

    def test_diversity_4(self):
        self.assertEqual('def pjymao(\n    mkqxigcoesoyvsjzzgmuzvnvaaqvfnfjuwrldlkdsbxjnixwnogmklpdzaookcyknhyzwchyxhauftbonyldahasttlkm,\n):\n    ...\n', self.run_black('def pjymao(mkqxigcoesoyvsjzzgmuzvnvaaqvfnfjuwrldlkdsbxjnixwnogmklpdzaookcyknhyzwchyxhauftbonyldahasttlkm):\n    ...\n'))

    def test_diversity_5(self):
        self.assertEqual('def hxl(\n    brlxptpzszcaffdrnneafdopeqaelywikueqcdcccemimvuqwyugjegwihtanphrumjrverrepcqnydrb,\n):\n    ...\n', self.run_black('def hxl(brlxptpzszcaffdrnneafdopeqaelywikueqcdcccemimvuqwyugjegwihtanphrumjrverrepcqnydrb):\n    ...\n'))

    def test_diversity_6(self):
        self.assertEqual('def vcsbk(\n    kolhsunymclmigbtexsdfnftjowhewpszmxhtovdichqituzxqwurhlqkwsofgylbrdlfmzbfbtvlpvpk,\n):\n    return 8\n', self.run_black('def vcsbk(kolhsunymclmigbtexsdfnftjowhewpszmxhtovdichqituzxqwurhlqkwsofgylbrdlfmzbfbtvlpvpk):\n    return 8\n'))

    def test_diversity_7(self):
        self.assertEqual('def bra(\n    ugvkkrgngkqiraxypwgswgetpwgyluidlbxyyruralcaepvjljzfjvmbtlofuygigvmyzawixnawikvxpxsawl,\n):\n    pass\n', self.run_black('def bra(ugvkkrgngkqiraxypwgswgetpwgyluidlbxyyruralcaepvjljzfjvmbtlofuygigvmyzawixnawikvxpxsawl):\n    pass\n'))

    def test_diversity_8(self):
        self.assertEqual('def aey(\n    vikxpbvjgrnydjlvtxpyoyinaszqczxklfaivjegmzhsurudivienytvshcrtttwnvzeztsbezydawcrllwutskuv,\n):\n    ...\n', self.run_black('def aey(vikxpbvjgrnydjlvtxpyoyinaszqczxklfaivjegmzhsurudivienytvshcrtttwnvzeztsbezydawcrllwutskuv):\n    ...\n'))

    def test_diversity_9(self):
        self.assertEqual('def rozy(\n    aafnrescxhysijgzxprrfakpdybaewbafertlopexazrovuozzcbdtqgqjskqecejluvwnciqqennzirgttr,\n):\n    return 4\n', self.run_black('def rozy(aafnrescxhysijgzxprrfakpdybaewbafertlopexazrovuozzcbdtqgqjskqecejluvwnciqqennzirgttr):\n    return 4\n'))

    def test_diversity_10(self):
        self.assertEqual('def ilfe(\n    nxqioyohpryizcpxpmaakpmpjvunuzmlixzgdawqvftaoktqcwwtilkpmizpybupwsyakdbonjuuqlpitvqyrbjeorm,\n):\n    ...\n', self.run_black('def ilfe(nxqioyohpryizcpxpmaakpmpjvunuzmlixzgdawqvftaoktqcwwtilkpmizpybupwsyakdbonjuuqlpitvqyrbjeorm):\n    ...\n'))

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
        self.assertEqual('ixaxuqoa = {"jtvgf": 25}\n', self.run_black('ixaxuqoa = {"jtvgf": 25}\n'))

    def test_diversity_2(self):
        self.assertEqual('def srtz(bzvev, sfny):\n    ...\n', self.run_black('def srtz(bzvev, sfny):\n    ...\n'))

    def test_diversity_3(self):
        self.assertEqual('def ltellbt(yodp, yhdvahz):\n    pass\n', self.run_black('def ltellbt(yodp, yhdvahz):\n    pass\n'))

    def test_diversity_4(self):
        self.assertEqual('chlex = [91, 83, 57, 74]\n', self.run_black('chlex = [91, 83, 57, 74]\n'))

    def test_diversity_5(self):
        self.assertEqual('kegyvw = [56, 10]\n', self.run_black('kegyvw = [56, 10]\n'))

    def test_diversity_6(self):
        self.assertEqual('ozutoxj = [60, 24, 29, 57]\n', self.run_black('ozutoxj = [60, 24, 29, 57]\n'))

    def test_diversity_7(self):
        self.assertEqual('def pladnom(jmdurxny):\n    ...\n', self.run_black('def pladnom(jmdurxny):\n    ...\n'))

    def test_diversity_8(self):
        self.assertEqual('def yaobify(guq, deedhr):\n    return 7\n', self.run_black('def yaobify(guq, deedhr):\n    return 7\n'))

    def test_diversity_9(self):
        self.assertEqual('def phhev(wkqzady, goz):\n    pass\n', self.run_black('def phhev(wkqzady, goz):\n    pass\n'))

    def test_diversity_10(self):
        self.assertEqual('def dcarzfo(skof):\n    ...\n', self.run_black('def dcarzfo(skof):\n    ...\n'))
