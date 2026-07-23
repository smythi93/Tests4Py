import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width>2661]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'pui', 'width': 628, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'zrmmcp', 'width': 597, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'xbgr', 'width': 431, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'pzy', 'width': 1661, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'xqwpm', 'width': 174, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_2(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width>2912]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'qye', 'width': 863, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'rizjbk', 'width': 1288, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'agquna', 'width': 1912, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'ntmtxd', 'width': 488, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'gggq', 'width': 412, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_3(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width>2908]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'aysa', 'width': 1908, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'xcwmxp', 'width': 312, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'tvothr', 'width': 1345, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'oldat', 'width': 585, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_4(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width>2499]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'zeoev', 'width': 1096, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'vcz', 'width': 1499, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'whlne', 'width': 471, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_5(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst[width>2959]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'yzazmw', 'width': 666, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'trzm', 'width': 1959, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'obdb', 'width': 894, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_6(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst[width>2290]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'mlgmn', 'width': 521, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'alns', 'width': 1290, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'notapr', 'width': 222, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'cqzo', 'width': 568, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'sth', 'width': 237, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_7(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'worst[width>2445]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'uosix', 'width': 383, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'vfm', 'width': 1445, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'bvvmyw', 'width': 1434, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_8(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width>2960]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'vhkowr', 'width': 1960, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'bnfj', 'width': 776, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'tag', 'width': 643, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'dtbtou', 'width': 208, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'zcyrbf', 'width': 1261, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_9(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width>2959]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'fgryq', 'width': 505, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'kaxd', 'width': 1718, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'wopo', 'width': 1959, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'qdz', 'width': 792, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'udmd', 'width': 808, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_10(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width>2858]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'soab', 'width': 643, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'dxprhs', 'width': 1226, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'llk', 'width': 609, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'dmhqqd', 'width': 1858, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual([], [d['format_id'] for d in _ydl.downloaded_info_dicts])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width=608]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'vsl', 'width': 1316, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'rrpo', 'width': 635, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'fnoco', 'width': 669, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'kdfmik', 'width': 608, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'xjbqiy', 'width': 1058, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['kdfmik'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_2(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'all[width>=1007]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'fjk', 'width': 1766, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'kgkgzb', 'width': 1740, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'bhc', 'width': 1007, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'txi', 'width': 1700, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['fjk', 'kgkgzb', 'bhc', 'txi'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_3(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'all[width>=576]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'zgitqm', 'width': 888, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'nhcx', 'width': 1100, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'prl', 'width': 576, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'hisir', 'width': 1125, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'aje', 'width': 1089, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['zgitqm', 'nhcx', 'prl', 'hisir', 'aje'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_4(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width=200]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'zllm', 'width': 1854, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'ovjeka', 'width': 635, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'kkxab', 'width': 337, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'fok', 'width': 200, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'wheut', 'width': 1142, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['fok'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_5(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width=415]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'ntbzj', 'width': 415, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'bvgajh', 'width': 546, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'gsvbo', 'width': 554, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['ntbzj'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_6(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'all[width>=257]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'nakkt', 'width': 257, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'lbp', 'width': 1697, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'iggqpp', 'width': 1856, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['nakkt', 'lbp', 'iggqpp'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_7(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'all[width>=114]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'kggsu', 'width': 1027, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'uejeqe', 'width': 1912, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'bshcfd', 'width': 114, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'zoz', 'width': 1003, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['kggsu', 'uejeqe', 'bshcfd', 'zoz'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_8(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'all[width>=866]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'wpv', 'width': 866, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'wuh', 'width': 1831, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'aqhsjc', 'width': 1580, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['wpv', 'wuh', 'aqhsjc'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_9(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'all[width>=377]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'poea', 'width': 377, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'slqxw', 'width': 1593, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'ioj', 'width': 1708, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['poea', 'slqxw', 'ioj'], [d['format_id'] for d in _ydl.downloaded_info_dicts])

    def test_diversity_10(self):
        from test.helper import FakeYDL
        from youtube_dl.utils import ExtractorError
        class _YDL(FakeYDL):

            def __init__(self, *a, **k):
                super(_YDL, self).__init__(*a, **k)
                self.downloaded_info_dicts = []

            def process_info(self, info_dict):
                self.downloaded_info_dicts.append(info_dict)

            def to_screen(self, msg):
                pass
        _ydl = _YDL({'format': 'best[width=789]'})
        try:
            _ydl.process_ie_result(dict({'formats': [{'format_id': 'wsfi', 'width': 789, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'ceb', 'width': 1140, 'url': 'http://_/', 'ext': 'unknown'}, {'format_id': 'iwxu', 'width': 189, 'url': 'http://_/', 'ext': 'unknown'}], 'id': 'testid', 'title': 't', 'extractor': 'testex', 'extractor_key': 'TestEx'}))
        except ExtractorError:
            pass
        self.assertEqual(['wsfi'], [d['format_id'] for d in _ydl.downloaded_info_dicts])
