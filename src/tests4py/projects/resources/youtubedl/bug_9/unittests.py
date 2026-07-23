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
        _ydl = _YDL({'format': 'bestvideo[filesize>=188675475]+worstaudio/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'nymf', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'ikegcq', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'mqptsp', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['mqptsp'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[filesize>=80846739]+bestaudio/best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'rmko', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'gzuyjc', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'fpf', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['fpf'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[height>=898587499]+worstaudio/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'rbic', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'ovhszt', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'iqp', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['iqp'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[fps>=76672442]+bestaudio/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'vsj', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'wryk', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'hgk', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['hgk'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[width>=535345386]+worstaudio/best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'uubwt', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'cdlea', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'dled', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['dled'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[width>=443600719]+bestaudio/best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'czit', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'zfbed', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'hazt', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['hazt'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[height>=556624637]+worstaudio/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'uug', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'bocz', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'fjjm', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['fjjm'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[filesize>=372837042]+worstaudio/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'sfbasx', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'aac', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'yjdok', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['yjdok'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[fps>=782998410]+bestaudio/worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'kqwf', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'drlwh', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'sjxd', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['sjxd'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo[abr>=768467667]+worstaudio/best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'fqctn', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'tohle', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'drveqb', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['drveqb'], [d['format_id'] for d in _ydl.downloaded_info_dicts])


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
        _ydl = _YDL({'format': 'bestvideo+bestaudio'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'idz', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'bcsx', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'swtbx', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['idz+bcsx'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo+bestaudio'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'dqmp', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'rsz', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'qah', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['dqmp+rsz'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'yhl', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'vwuib', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'igh', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['igh'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'tslnkt', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'klvc', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'reugs', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['reugs'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'bestvideo'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'nqebrv', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'kfogmd', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'rcr', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['nqebrv'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'rugln', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'abj', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'czlrda', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['czlrda'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'tjebqp', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'utmof', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'ufv', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['ufv'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'lxajs', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'ytjalg', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'wnvncb', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['wnvncb'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'worst'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'cyxdjq', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'rkit', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'tewura', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['tewura'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

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
        _ydl = _YDL({'format': 'best'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'oztjxa', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'none', 'tbr': 100}, {'format_id': 'crk', 'ext': 'm4a', 'url': 'http://_/', 'vcodec': 'none', 'acodec': 'aac', 'tbr': 50}, {'format_id': 'hofhi', 'ext': 'mp4', 'url': 'http://_/', 'vcodec': 'h264', 'acodec': 'aac', 'tbr': 150}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual(['hofhi'], [d['format_id'] for d in _ydl.downloaded_info_dicts])
