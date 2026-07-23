import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'tdf': 70000000.0}, json.loads(js_to_json('{"tdf":7E7}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'zryx': 5000000000.0}, json.loads(js_to_json('{"zryx":5E9}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ipdnth': 700000.0}, json.loads(js_to_json('{"ipdnth":7e5}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'hhvkjv': 400000000.0}, json.loads(js_to_json('{"hhvkjv":4e8}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ibklrm': 700000000.0}, json.loads(js_to_json('{"ibklrm":7e8}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'prjez': 800000000.0}, json.loads(js_to_json('{"prjez":8e8}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'rcjubd': 6000000.0}, json.loads(js_to_json('{"rcjubd":6E6}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'rpoyo': 900000.0}, json.loads(js_to_json('{"rpoyo":9e5}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'iiig': 9000000000.0}, json.loads(js_to_json('{"iiig":9e9}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'gdaa': 10000.0}, json.loads(js_to_json('{"gdaa":1e4}')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'nlnbt': 5000}, json.loads(js_to_json('{"nlnbt":5000}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'sxfnq': 298}, json.loads(js_to_json('{"sxfnq":298}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wfmrr': 2293}, json.loads(js_to_json('{"wfmrr":2293}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'dyg': 2692}, json.loads(js_to_json('{"dyg":2692}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wisonp': 7313}, json.loads(js_to_json('{"wisonp":7313}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'jyt': 6692}, json.loads(js_to_json('{"jyt":6692}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'pbf': 3248}, json.loads(js_to_json('{"pbf":3248}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'yntpz': 489}, json.loads(js_to_json('{"yntpz":489}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'uvlimt': 3966}, json.loads(js_to_json('{"uvlimt":3966}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wjj': 2852}, json.loads(js_to_json('{"wjj":2852}')))
