import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'hkk': '04:31:12'}, json.loads(js_to_json('{"hkk": "04:31:12"}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'kfupp': '06:49:35'}, json.loads(js_to_json('{"kfupp": "06:49:35"}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'pfgggi': '07:13:24'}, json.loads(js_to_json('{"pfgggi": "07:13:24"}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'tugars': '05:47:20'}, json.loads(js_to_json('{"tugars": "05:47:20"}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'svbyw': '00:35:53'}, json.loads(js_to_json('{"svbyw": "00:35:53"}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'vcb': '03:26:19'}, json.loads(js_to_json('{"vcb": "03:26:19"}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'cqr': '00:25:22'}, json.loads(js_to_json('{"cqr": "00:25:22"}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qqbrb': '04:11:53'}, json.loads(js_to_json('{"qqbrb": "04:11:53"}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'gjrw': '05:42:16'}, json.loads(js_to_json('{"gjrw": "05:42:16"}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qmjex': '03:31:43'}, json.loads(js_to_json('{"qmjex": "03:31:43"}')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'tttflv': 'llq'}, json.loads(js_to_json('{"tttflv": "llq"}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ppj': 'klzgrtm'}, json.loads(js_to_json('{"ppj": "klzgrtm"}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'lie': 'peno'}, json.loads(js_to_json('{"lie": "peno"}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'xujkpf': 'bvoklre'}, json.loads(js_to_json('{"xujkpf": "bvoklre"}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'uiv': 'fmyrt'}, json.loads(js_to_json('{"uiv": "fmyrt"}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'jwztwoo': 77065}, json.loads(js_to_json('{"jwztwoo": 77065}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ivqqiy': 'rotbhgo'}, json.loads(js_to_json('{"ivqqiy": "rotbhgo"}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'cihl': 15126}, json.loads(js_to_json('{"cihl": 15126}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'sghkpmn': 93383}, json.loads(js_to_json('{"sghkpmn": 93383}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'xotpooq': 'kosiuqq'}, json.loads(js_to_json('{"xotpooq": "kosiuqq"}')))
