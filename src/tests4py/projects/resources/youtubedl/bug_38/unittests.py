import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'gennuwiso=pvbbjvk', urlencode_postdata({'gennuwiso': 'pvbbjvk'}))

    def test_diversity_2(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'pbf=fyntpzauv', urlencode_postdata({'pbf': 'fyntpzauv'}))

    def test_diversity_3(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'ydrqsu=tpkbauvpo', urlencode_postdata({'ydrqsu': 'tpkbauvpo'}))

    def test_diversity_4(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'ndxq=ypj', urlencode_postdata({'ndxq': 'ypj'}))

    def test_diversity_5(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'jkugaizd=afojehv', urlencode_postdata({'jkugaizd': 'afojehv'}))

    def test_diversity_6(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'sqlxw=sglvsjt', urlencode_postdata({'sqlxw': 'sglvsjt'}))

    def test_diversity_7(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'wntpvnsuj=snk', urlencode_postdata({'wntpvnsuj': 'snk'}))

    def test_diversity_8(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'dumodug=bkhnkwpr', urlencode_postdata({'dumodug': 'bkhnkwpr'}))

    def test_diversity_9(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'yilnozcf=xehyger', urlencode_postdata({'yilnozcf': 'xehyger'}))

    def test_diversity_10(self):
        from youtube_dl.utils import urlencode_postdata
        self.assertEqual(b'cbrlizy=orjkhphv', urlencode_postdata({'cbrlizy': 'orjkhphv'}))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        from urllib.parse import urlencode
        self.assertEqual(b'ypexf=pkwnvl', urlencode({'ypexf': 'pkwnvl'}).encode('ascii'))

    def test_diversity_2(self):
        from urllib.parse import urlencode
        self.assertEqual(b'rmghz=egyxjo', urlencode({'rmghz': 'egyxjo'}).encode('ascii'))

    def test_diversity_3(self):
        from urllib.parse import urlencode
        self.assertEqual(b'xakbxb=gqsmuysvi', urlencode({'xakbxb': 'gqsmuysvi'}).encode('ascii'))

    def test_diversity_4(self):
        from urllib.parse import urlencode
        self.assertEqual(b'nlrbuaved=edhmup', urlencode({'nlrbuaved': 'edhmup'}).encode('ascii'))

    def test_diversity_5(self):
        from urllib.parse import urlencode
        self.assertEqual(b'wulth=eufgb', urlencode({'wulth': 'eufgb'}).encode('ascii'))

    def test_diversity_6(self):
        from urllib.parse import urlencode
        self.assertEqual(b'eqzhzzfnx=sqrnj', urlencode({'eqzhzzfnx': 'sqrnj'}).encode('ascii'))

    def test_diversity_7(self):
        from urllib.parse import urlencode
        self.assertEqual(b'qvaw=lrakkyqnt', urlencode({'qvaw': 'lrakkyqnt'}).encode('ascii'))

    def test_diversity_8(self):
        from urllib.parse import urlencode
        self.assertEqual(b'osmmahoyl=tkflckwpx', urlencode({'osmmahoyl': 'tkflckwpx'}).encode('ascii'))

    def test_diversity_9(self):
        from urllib.parse import urlencode
        self.assertEqual(b'jetunagn=nusab', urlencode({'jetunagn': 'nusab'}).encode('ascii'))

    def test_diversity_10(self):
        from urllib.parse import urlencode
        self.assertEqual(b'atwfqo=glgkt', urlencode({'atwfqo': 'glgkt'}).encode('ascii'))
