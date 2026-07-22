import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'shh': 700}, json.loads(js_to_json('{"shh":700}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wluei': 2000}, json.loads(js_to_json('{"wluei":2000}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'hvveqe': 60000}, json.loads(js_to_json('{"hvveqe":60000}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'fnylr': 10000}, json.loads(js_to_json('{"fnylr":10000}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'rcjubd': 6000}, json.loads(js_to_json('{"rcjubd":6000}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'hriyh': 40000}, json.loads(js_to_json('{"hriyh":40000}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'bsfnx': 8000}, json.loads(js_to_json('{"bsfnx":8000}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'tpo': 4000}, json.loads(js_to_json('{"tpo":4000}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'daazz': 3000}, json.loads(js_to_json('{"daazz":3000}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'lnbth': 80000}, json.loads(js_to_json('{"lnbth":80000}')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'jcxa': 3625}, json.loads(js_to_json('{"jcxa":3625}')))

    def test_diversity_2(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wqbn': 79}, json.loads(js_to_json('{"wqbn":79}')))

    def test_diversity_3(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'wisonp': 114}, json.loads(js_to_json('{"wisonp":114}')))

    def test_diversity_4(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'xpbfuj': 7451}, json.loads(js_to_json('{"xpbfuj":7451}')))

    def test_diversity_5(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'uvlimt': 78}, json.loads(js_to_json('{"uvlimt":78}')))

    def test_diversity_6(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'pkbau': 6752}, json.loads(js_to_json('{"pkbau":6752}')))

    def test_diversity_7(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'qbxmp': 344}, json.loads(js_to_json('{"qbxmp":344}')))

    def test_diversity_8(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'aizdp': 56}, json.loads(js_to_json('{"aizdp":56}')))

    def test_diversity_9(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'ijys': 2921}, json.loads(js_to_json('{"ijys":2921}')))

    def test_diversity_10(self):
        import json
        from youtube_dl.utils import js_to_json
        self.assertEqual({'glvsjt': 576}, json.loads(js_to_json('{"glvsjt":576}')))
