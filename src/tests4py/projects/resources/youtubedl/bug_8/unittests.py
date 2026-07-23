import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst/worst,best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'roq', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2207}, {'format_id': 'dekdn', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2159}, {'format_id': 'ouwv', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1957}, {'format_id': 'pvzvh', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2246}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['roq', 'pvzvh'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_2(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'wqf', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2958}, {'format_id': 'xejq', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2558}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['xejq', 'wqf'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_3(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/worst,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'bszh', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2354}, {'format_id': 'zrga', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1446}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['zrga', 'bszh'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_4(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'vglu', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 81}, {'format_id': 'wmbjwz', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2174}, {'format_id': 'lrzgc', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 923}, {'format_id': 'khqm', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 522}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['khqm', 'vglu'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_5(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'nrmwpg', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1535}, {'format_id': 'nnub', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1328}, {'format_id': 'mkj', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2352}, {'format_id': 'tlycn', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1512}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['tlycn', 'nrmwpg'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_6(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'tzmvmj', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 412}, {'format_id': 'hyl', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2013}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['hyl', 'tzmvmj'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_7(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst/best,best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'ilq', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2875}, {'format_id': 'yzho', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2323}, {'format_id': 'ymw', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 500}, {'format_id': 'fvulrx', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2800}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['ilq', 'fvulrx'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_8(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst/worst,best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'tict', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1341}, {'format_id': 'pkrjj', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 791}, {'format_id': 'kbqyhw', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1078}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['tict', 'kbqyhw'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_9(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/worst,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'uwvyq', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1871}, {'format_id': 'abrg', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1434}, {'format_id': 'meqngy', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2545}, {'format_id': 'nyxv', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 420}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['nyxv', 'uwvyq'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_10(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'dtso', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 995}, {'format_id': 'gjurtz', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1973}, {'format_id': 'wbev', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 594}, {'format_id': 'gzdjf', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2999}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['gzdjf', 'dtso'], [d['format_id'] for d in _ydl.downloaded_info_dicts])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'ghhn', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1496}, {'format_id': 'urnjz', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 632}, {'format_id': 'jtyply', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 302}, {'format_id': 'edtes', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2265}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['edtes', 'ghhn'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_2(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'pxtovl', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1809}, {'format_id': 'fxgwfm', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 687}, {'format_id': 'mnqys', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 252}, {'format_id': 'wtwho', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1096}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['wtwho'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_3(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'fvbb', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1735}, {'format_id': 'blss', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1533}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['blss', 'fvbb'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_4(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'hom', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2135}, {'format_id': 'btitd', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2484}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['btitd', 'hom'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_5(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst,best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'stttb', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1986}, {'format_id': 'xwlhea', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 835}, {'format_id': 'awmup', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1644}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['stttb', 'awmup'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_6(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best,worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'ljcfe', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2058}, {'format_id': 'fpf', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1762}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['fpf', 'ljcfe'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_7(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst,best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'jcy', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 873}, {'format_id': 'lhyie', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 234}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['jcy', 'lhyie'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_8(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst,best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'zjtw', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1868}, {'format_id': 'rggqlq', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 562}, {'format_id': 'mcpc', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2235}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['zjtw', 'mcpc'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_9(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'mfkyq', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2037}, {'format_id': 'hpqe', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2379}, {'format_id': 'rhimd', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 2479}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['rhimd'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_10(self):
        from test.helper import FakeYDL
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst,best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'qyqzp', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 510}, {'format_id': 'iooat', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 1870}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['qyqzp', 'iooat'], [d['format_id'] for d in _ydl.downloaded_info_dicts])
