import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'ptby rspp', 'id': 't_mnjueh'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_uegjw', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_uegjw', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_2(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'iewnoi oqll', 'id': 't_uhhivz'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_jjkxv', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_jjkxv', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_3(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'dcdid mbhcogy', 'id': 't_odaotrzb'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_xbovw', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_xbovw', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_4(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'fpzfujvx uensodf', 'id': 't_aurfvabx'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_vkewou', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_vkewou', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_5(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'aalw rtoonc', 'id': 't_upjtrfhm'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_voeu', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_voeu', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_6(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'hkmrvj cgkrmwi', 'id': 't_nabqlegy'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_bjuailw', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_bjuailw', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_7(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'rjusbgdl pjaw', 'id': 't_naygq'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_ikbhsoa', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_ikbhsoa', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_8(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'fnulqp mtvifk', 'id': 't_jixw'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_tdlwc', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_tdlwc', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_9(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'vuws cgxiv', 'id': 't_lvtgnwkw'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_lpgl', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_lpgl', _ydl.downloaded_info_dicts[0]['id'])

    def test_diversity_10(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'iglt cjmy', 'id': 't_iyxzzvdu'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_tjrn', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('f_tjrn', _ydl.downloaded_info_dicts[0]['id'])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'eofi clsxowq', 'id': 't_qqwpc'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_mckvymav', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('eofi clsxowq', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_2(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'clcoqoj pjoyydqf', 'id': 't_mkypwp'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_wpbpgnel', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('clcoqoj pjoyydqf', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_3(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'cpnol emfczy', 'id': 't_covc'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_dlcuma', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('cpnol emfczy', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_4(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'mfhjwkiy lceh', 'id': 't_hvxs'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_sowgfgg', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('mfhjwkiy lceh', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_5(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'jrradh mhoh', 'id': 't_hwwxfg'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_dfom', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('jrradh mhoh', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_6(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'abrapcym kjbykqhh', 'id': 't_ghydd'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_ccjl', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('abrapcym kjbykqhh', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_7(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'sdjfmwp zuewv', 'id': 't_uyyqoxxs'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_wzcnb', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('sdjfmwp zuewv', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_8(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'cvihx lffercv', 'id': 't_ikifscl'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_jpvzad', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('cvihx lffercv', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_9(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'qfkpodud xyomrhpv', 'id': 't_xyfuz'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_ptaqtrn', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('qfkpodud xyomrhpv', _ydl.downloaded_info_dicts[0]['title'])

    def test_diversity_10(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL()
        class Foo1IE(InfoExtractor):
            _VALID_URL = 'foo1:'

            def _real_extract(self, url):
                return {'_type': 'url_transparent', 'url': 'foo2:', 'ie_key': 'Foo2', 'title': 'qpjww ooboxdhv', 'id': 't_yjzib'}
        class Foo2IE(InfoExtractor):
            _VALID_URL = 'foo2:'

            def _real_extract(self, url):
                return {'_type': 'url', 'url': 'foo3:', 'ie_key': 'Foo3'}
        class Foo3IE(InfoExtractor):
            _VALID_URL = 'foo3:'

            def _real_extract(self, url):
                return {'formats': [{'url': 'http://localhost/sample.mp4'}], 'id': 'f_qcdz', 'title': 'foo3 title', 'extractor': 'testex', 'extractor_key': 'TestEx'}
        _ydl.add_info_extractor(Foo1IE(_ydl))
        _ydl.add_info_extractor(Foo2IE(_ydl))
        _ydl.add_info_extractor(Foo3IE(_ydl))
        _ydl.extract_info('foo1:')
        self.assertEqual('qpjww ooboxdhv', _ydl.downloaded_info_dicts[0]['title'])
