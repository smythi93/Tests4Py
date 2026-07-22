import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'pzauvl': "drqsu'pkbau"}, json.loads(js_to_json('{"pzauvl":"drqsu\\\'pkbau"}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ndxq': "ypj'hkjhx"}, json.loads(js_to_json('{"ndxq":"ypj\\\'hkjhx"}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'dpwnp': "ijys'lxwz"}, json.loads(js_to_json('{"dpwnp":"ijys\\\'lxwz"}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'glvsjt': "ntpvns'qsnkp"}, json.loads(js_to_json('{"glvsjt":"ntpvns\\\'qsnkp"}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'umo': "vgzb'ysjoem"}, json.loads(js_to_json('{"umo":"vgzb\\\'ysjoem"}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ilnozc': "exeh'gerp"}, json.loads(js_to_json('{"ilnozc":"exeh\\\'gerp"}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'brl': "iplor'zapxxs"}, json.loads(js_to_json('{"brl":"iplor\\\'zapxxs"}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'exfl': "kwnvlg'iveeka"}, json.loads(js_to_json('{"exfl":"kwnvlg\\\'iveeka"}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qfxak': "ssb'vjxj"}, json.loads(js_to_json('{"qfxak":"ssb\\\'vjxj"}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'sviv': "urhuun'dlny"}, json.loads(js_to_json('{"sviv":"urhuun\\\'dlny"}')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'mup': 'wulth'}, json.loads(js_to_json('{"mup":"wulth"}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'eufgb': 'vvod'}, json.loads(js_to_json('{"eufgb":"vvod"}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'zfnxir': 'rnjefo'}, json.loads(js_to_json('{"zfnxir":"rnjefo"}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wvg': 'kmi'}, json.loads(js_to_json('{"wvg":"kmi"}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'tuuo': 'mahoy'}, json.loads(js_to_json('{"tuuo":"mahoy"}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'otkflc': 'eebuje'}, json.loads(js_to_json('{"otkflc":"eebuje"}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'unag': 'ibh'}, json.loads(js_to_json('{"unag":"ibh"}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'xkm': 'wfqox'}, json.loads(js_to_json('{"xkm":"wfqox"}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'leeq': 'nahry'}, json.loads(js_to_json('{"leeq":"nahry"}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'xsqq': 'xllihc'}, json.loads(js_to_json('{"xsqq":"xllihc"}')))
