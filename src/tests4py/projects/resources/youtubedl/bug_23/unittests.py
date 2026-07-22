import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'vawv': 'kmi', 'tuuo': 'asd'}, json.loads(js_to_json('{"vawv":"kmi" , //otkflc\n"tuuo":"asd"}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'eebuje': 822, 'nag': 353}, json.loads(js_to_json('{"eebuje":822 , //usa\n"nag":353}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'kms': 'fqox', 'leeq': 'xvi'}, json.loads(js_to_json('{"kms":"fqox" , //xsqq\n"leeq":"xvi"}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'xllihc': 853, 'oinprk': 'konq'}, json.loads(js_to_json('{"xllihc":853 , //rccs\n"oinprk":"konq"}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qyqi': 628, 'gwbxlp': 'pfu'}, json.loads(js_to_json('{"qyqi":628 , //seogvt\n"gwbxlp":"pfu"}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'iyaoio': 89, 'yuac': 570}, json.loads(js_to_json('{"iyaoio":89 , //qqluk\n"yuac":570}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'fji': 'adj', 'cgeq': 505}, json.loads(js_to_json('{"fji":"adj" , //nyl\n"cgeq":505}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'vkioq': 725, 'elmdnm': 312}, json.loads(js_to_json('{"vkioq":725 , //gjysw\n"elmdnm":312}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qgepp': 59, 'kwxqu': 519}, json.loads(js_to_json('{"qgepp":59 , //fhm\n"kwxqu":519}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qruiyx': 'qbpqgu', 'cqjhv': 'gyplj'}, json.loads(js_to_json('{"qruiyx":"qbpqgu" , //bopq\n"cqjhv":"gyplj"}')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ghjy': 228, 'oxxdt': 'eltle'}, json.loads(js_to_json('{"ghjy":228,"oxxdt":"eltle"}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wwrbqt': 'ypezwj', 'eoubg': 488}, json.loads(js_to_json('{"wwrbqt":"ypezwj","eoubg":488}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'czzwcd': 'jcoczd', 'gxlzhj': 'bsqkj'}, json.loads(js_to_json('{"czzwcd":"jcoczd","gxlzhj":"bsqkj"}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'tgyrep': 'uijtl', 'qnciy': 'jka'}, json.loads(js_to_json('{"tgyrep":"uijtl","qnciy":"jka"}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'snox': 531, 'jwbbr': 'wudh'}, json.loads(js_to_json('{"snox":531,"jwbbr":"wudh"}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ghub': 298, 'rimqa': 'tfsua'}, json.loads(js_to_json('{"ghub":298,"rimqa":"tfsua"}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'nqmhtz': 55, 'kylzxb': 268}, json.loads(js_to_json('{"nqmhtz":55,"kylzxb":268}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'fpx': 26, 'qtiy': 82}, json.loads(js_to_json('{"fpx":26,"qtiy":82}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'dla': 'txfipx', 'bkk': 455}, json.loads(js_to_json('{"dla":"txfipx","bkk":455}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'njnyoi': 579, 'mwgjm': 148}, json.loads(js_to_json('{"njnyoi":579,"mwgjm":148}')))
