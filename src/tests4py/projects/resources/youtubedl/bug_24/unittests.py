import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('sihonvo=16511', {'sihonvo': '16511'}))

    def test_diversity_2(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('skcuhyom=97396', {'skcuhyom': '97396'}))

    def test_diversity_3(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('vuhrji=97636', {'vuhrji': '97636'}))

    def test_diversity_4(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('nlssaxs!=93439', {'nlssaxs': '93439'}))

    def test_diversity_5(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('ziembjjm!=84597', {'ziembjjm': '84597'}))

    def test_diversity_6(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('skbodgsb!=68114', {'skbodgsb': '68114'}))

    def test_diversity_7(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('qrfoie!=31140', {'qrfoie': '31140'}))

    def test_diversity_8(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('germvvc=44886', {'germvvc': '44886'}))

    def test_diversity_9(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('ysdy!=41235', {'ysdy': '41235'}))

    def test_diversity_10(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('fywoum=56375', {'fywoum': '56375'}))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('tgpox=70213', {'tgpox': 70213}))

    def test_diversity_2(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('vxvar=91512', {'vxvar': 91512}))

    def test_diversity_3(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('amfy=pmgarih', {'amfy': 'pmgarih'}))

    def test_diversity_4(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('uqdlmg=64', {'uqdlmg': '393'}))

    def test_diversity_5(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('nmehgs=22', {'nmehgs': '394'}))

    def test_diversity_6(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('wdltbj=54351', {'wdltbj': 54351}))

    def test_diversity_7(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('lhgyn=ljvwv', {'lhgyn': 'ljvwv'}))

    def test_diversity_8(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('xacr=101', {'xacr': '319'}))

    def test_diversity_9(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('satddhhh=ghtka', {'satddhhh': 'ghtka'}))

    def test_diversity_10(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('exhg=145', {'exhg': '147'}))
