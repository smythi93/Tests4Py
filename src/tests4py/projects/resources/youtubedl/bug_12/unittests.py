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
        _ydl = _YDL({'format': '[format_id!=ujkmtf-kgbfpw]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'ujkmtf-kgbfpw', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'xdopdv-bfzaom', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('xdopdv-bfzaom', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=qhvli-nwkqfl]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'yje-afyda', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'qhvli-nwkqfl', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('yje-afyda', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=vtukht-rudryk]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'vtukht-rudryk', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'yyraa-tvfnf', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('yyraa-tvfnf', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=qpk-aim]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'kcs-csy', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'qpk-aim', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('kcs-csy', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=pjncti-ikg]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'pjncti-ikg', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'gvht-aeio', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('gvht-aeio', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=eyvx-ovy]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'eyvx-ovy', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'nxhpdb-tqtw', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('nxhpdb-tqtw', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=vhtul-iypi]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'nnaqch-nuqpj', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'vhtul-iypi', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('nnaqch-nuqpj', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=jhl-qspv]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'kfk-dtbaqj', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'jhl-qspv', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('kfk-dtbaqj', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=fmw-jqqwu]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'fmw-jqqwu', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'appry-zwmo', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('appry-zwmo', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id!=ygac-luokpk]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'gieio-scjwcb', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'ygac-luokpk', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('gieio-scjwcb', _ydl.downloaded_info_dicts[0]['format_id'])


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
        _ydl = _YDL({'format': '[format_id=ikx-kaja]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'cia-fccl', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'ikx-kaja', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('ikx-kaja', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=yuo-ijvhm]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'yuo-ijvhm', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'hbc-zkslkl', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('yuo-ijvhm', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=tcgdz-ruswav]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'oxcpjc-aontfl', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'tcgdz-ruswav', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('tcgdz-ruswav', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=czgf-mpd]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'ofwxz-wgswwc', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'czgf-mpd', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('czgf-mpd', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=yeb-xrwqt]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'yeb-xrwqt', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'hgk-bjjzu', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('yeb-xrwqt', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=wus-yko]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'jgr-yqt', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'wus-yko', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('wus-yko', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=iyqz-nke]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'hzg-rtukj', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'iyqz-nke', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('iyqz-nke', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=ythmyv-yhi]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'gex-loez', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'ythmyv-yhi', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('ythmyv-yhi', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=hxgqh-qnaupu]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'rlhi-jwywng', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'hxgqh-qnaupu', 'ext': 'webm', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('hxgqh-qnaupu', _ydl.downloaded_info_dicts[0]['format_id'])

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
        _ydl = _YDL({'format': '[format_id=vng-trjuyu]'})
        _ydl.process_ie_result(dict({'formats': [{'format_id': 'nvaspb-ivji', 'ext': 'flv', 'url': 'http://localhost/sample.mp4'}, {'format_id': 'vng-trjuyu', 'ext': 'mp4', 'url': 'http://localhost/sample.mp4'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        self.assertEqual('vng-trjuyu', _ydl.downloaded_info_dicts[0]['format_id'])
