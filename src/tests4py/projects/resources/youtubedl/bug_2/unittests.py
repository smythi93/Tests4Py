import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="vxldda" bandwidth="5707023"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="amjyt" bandwidth="3577800"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="afimyf" bandwidth="1491834"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="afimyf" bandwidth="113159"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['afimyf', 'afimyf', 'amjyt', 'vxldda'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_2(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="bwb" bandwidth="2777936"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="bsg" bandwidth="59225"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="bsg" bandwidth="4941640"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="ohyxp" bandwidth="4816511"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['bsg', 'bsg', 'bwb', 'ohyxp'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_3(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="hhnj" bandwidth="1155451"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="tmpt" bandwidth="119944"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="tmpt" bandwidth="2322010"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['hhnj', 'tmpt', 'tmpt'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_4(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="zxr" bandwidth="3155790"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="zrqkdb" bandwidth="363185"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="isnul" bandwidth="4876288"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="isnul" bandwidth="134712"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['isnul', 'isnul', 'zrqkdb', 'zxr'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_5(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="dydmx" bandwidth="5030281"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="ztv" bandwidth="3171004"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="ztv" bandwidth="57585"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['dydmx', 'ztv', 'ztv'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_6(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="vadwub" bandwidth="151745"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="xttsy" bandwidth="3942429"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="vadwub" bandwidth="913450"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="kyepm" bandwidth="1280018"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['kyepm', 'vadwub', 'vadwub', 'xttsy'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_7(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="zucc" bandwidth="629877"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="zucc" bandwidth="135416"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="tmr" bandwidth="4488905"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="aylj" bandwidth="5086410"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['aylj', 'tmr', 'zucc', 'zucc'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_8(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="wajaa" bandwidth="90139"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="wajaa" bandwidth="3590173"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="gdxql" bandwidth="4950472"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['gdxql', 'wajaa', 'wajaa'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_9(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="wuo" bandwidth="109258"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="wuo" bandwidth="564236"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="ifin" bandwidth="2892084"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['ifin', 'wuo', 'wuo'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_10(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="rwcuqm" bandwidth="157499"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="sllyv" bandwidth="1478909"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="rwcuqm" bandwidth="5768389"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="hnul" bandwidth="5034344"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['hnul', 'rwcuqm', 'rwcuqm', 'sllyv'], sorted((f['format_id'] for f in _formats)))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="xlj" bandwidth="4635718"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="dumna" bandwidth="5770778"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['dumna', 'xlj'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_2(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="bunpo" bandwidth="3721948"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="sspxbc" bandwidth="924721"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="qonvx" bandwidth="4267596"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="ncpldo" bandwidth="577752"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['bunpo', 'ncpldo', 'qonvx', 'sspxbc'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_3(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="coxa" bandwidth="3479459"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="gby" bandwidth="5372136"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['coxa', 'gby'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_4(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="puxbq" bandwidth="4021577"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="yvl" bandwidth="1743180"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['puxbq', 'yvl'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_5(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="uaq" bandwidth="534234"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="hfzovw" bandwidth="4657588"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="bqbnkf" bandwidth="4693604"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['bqbnkf', 'hfzovw', 'uaq'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_6(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="tvd" bandwidth="1127332"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="mqhscn" bandwidth="4009883"></Representation></AdaptationSet><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="gld" bandwidth="4735722"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['gld', 'mqhscn', 'tvd'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_7(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="video/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="bld" bandwidth="3529997"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="jcp" bandwidth="2178912"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="maiimy" bandwidth="2684551"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="unchz" bandwidth="4968325"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['bld', 'jcp', 'maiimy', 'unchz'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_8(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="bsxaui" bandwidth="321857"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="tkas" bandwidth="1617908"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['bsxaui', 'tkas'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_9(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="sxsq" bandwidth="509758"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="fuk" bandwidth="697117"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="xrih" bandwidth="3035954"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['fuk', 'sxsq', 'xrih'], sorted((f['format_id'] for f in _formats)))

    def test_diversity_10(self):
        from test.helper import FakeYDL
        from youtube_dl.extractor.common import InfoExtractor
        from youtube_dl.compat import compat_etree_fromstring
        class _IE(InfoExtractor):
            _VALID_URL = 'https?://.*'
        _ie = _IE(FakeYDL())
        _formats = _ie._parse_mpd_formats(compat_etree_fromstring('<?xml version="1.0" encoding="UTF-8"?><MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT10S"><Period><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="fdaijp" bandwidth="1787691"></Representation></AdaptationSet><AdaptationSet mimeType="audio/mp4" codecs="mp4a.40.2"><SegmentTemplate timescale="1000000" initialization="i_$RepresentationID$.m4d" media="s_$RepresentationID$_$Number$.m4d" duration="2000000" startNumber="0"></SegmentTemplate><Representation id="pdrkr" bandwidth="2525459"></Representation></AdaptationSet></Period></MPD>'.encode('utf-8')), mpd_url='http://unknown/manifest.mpd')
        self.assertEqual(['fdaijp', 'pdrkr'], sorted((f['format_id'] for f in _formats)))
