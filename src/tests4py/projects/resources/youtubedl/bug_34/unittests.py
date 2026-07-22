import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ppkw': {'xsype': 'gxkrmgh'}}, json.loads(js_to_json("{'ppkw':{'xsype':'gxkrmgh'}}")))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qfxak': {'xegy': 'ssb'}}, json.loads(js_to_json("{'qfxak':{'xegy':'ssb'}}")))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'sviv': {'vjxj': 'lrbuave'}}, json.loads(js_to_json("{'sviv':{'vjxj':'lrbuave'}}")))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'oidwul': {'jedh': 'hibllt'}}, json.loads(js_to_json("{'oidwul':{'jedh':'hibllt'}}")))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'vvvod': {'zfnxir': 'rnjefo'}}, json.loads(js_to_json("{'vvvod':{'zfnxir':'rnjefo'}}")))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wvg': {'kmi': 'ntuuohp'}}, json.loads(js_to_json("{'wvg':{'kmi':'ntuuohp'}}")))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'hoy': {'otkflc': 'eebuje'}}, json.loads(js_to_json("{'hoy':{'otkflc':'eebuje'}}")))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'unag': {'anusaby': 'she'}}, json.loads(js_to_json("{'unag':{'anusaby':'she'}}")))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'mbhleeq': {'nahry': 'feahtma'}}, json.loads(js_to_json("{'mbhleeq':{'nahry':'feahtma'}}")))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'vto': {'lihc': 'zsauy'}}, json.loads(js_to_json("{'vto':{'lihc':'zsauy'}}")))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'zenkinq': 4293, 'qis': 1250, 'konq': 'lpaapcr'}, json.loads(js_to_json("{'zenkinq':4293,'qis':1250,'konq':'lpaapcr'}")))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'aoiotcu': 9135, 'eogvtvi': 7064, 'uac': 295}, json.loads(js_to_json("{'aoiotcu':9135,'eogvtvi':7064,'uac':295}")))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'djtc': 'aipp', 'ccqjjc': 7133}, json.loads(js_to_json("{'djtc':'aipp','ccqjjc':7133}")))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'flqsrjr': 5103, 'vkioq': 'eqzl', 'kogjysw': 'wxquu'}, json.loads(js_to_json("{'flqsrjr':5103,'vkioq':'eqzl','kogjysw':'wxquu'}")))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'hyqbpq': 'cqjhv', 'qruiyx': 'gyplj', 'fhm': 2999}, json.loads(js_to_json("{'hyqbpq':'cqjhv','qruiyx':'gyplj','fhm':2999}")))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'opqwxg': 'kpgil'}, json.loads(js_to_json("{'opqwxg':'kpgil'}")))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qvs': 783, 'gkghcnw': 'tjkqb'}, json.loads(js_to_json("{'qvs':783,'gkghcnw':'tjkqb'}")))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'jhplm': 9433}, json.loads(js_to_json("{'jhplm':9433}")))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'zdjc': 4826, 'yczzwc': 7358, 'aufigxl': 'bsqkj'}, json.loads(js_to_json("{'zdjc':4826,'yczzwc':7358,'aufigxl':'bsqkj'}")))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qnciy': 'jka', 'uijtl': 'oubbjsm', 'mhyveia': 3}, json.loads(js_to_json("{'qnciy':'jka','uijtl':'oubbjsm','mhyveia':3}")))
