import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'pzauvl': 'drqsu\npkbau'}, json.loads(js_to_json('{"pzauvl":"drqsu\\npkbau"}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ndxq': 'ypj\nhkjhx'}, json.loads(js_to_json('{"ndxq":"ypj\\nhkjhx"}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'dpwnp': 'ijys\nlxwz'}, json.loads(js_to_json('{"dpwnp":"ijys\\nlxwz"}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'glvsjt': 'ntpvns\nqsnkp'}, json.loads(js_to_json('{"glvsjt":"ntpvns\\nqsnkp"}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'umo': 'vgzb\nysjoem'}, json.loads(js_to_json('{"umo":"vgzb\\nysjoem"}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ilnozc': 'exeh\ngerp'}, json.loads(js_to_json('{"ilnozc":"exeh\\ngerp"}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'brl': 'iplor\nzapxxs'}, json.loads(js_to_json('{"brl":"iplor\\nzapxxs"}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'exfl': 'kwnvlg\niveeka'}, json.loads(js_to_json('{"exfl":"kwnvlg\\niveeka"}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qfxak': 'ssb\nvjxj'}, json.loads(js_to_json('{"qfxak":"ssb\\nvjxj"}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'sviv': 'urhuun\ndlny'}, json.loads(js_to_json('{"sviv":"urhuun\\ndlny"}')))


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
