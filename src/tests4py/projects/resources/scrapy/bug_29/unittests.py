import unittest

# noinspection PyUnresolvedReferences
from scrapy.http import Request
from scrapy.utils.request import request_httprepr


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(b'GET /efvqi/by HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///efvqi/by')))

    def test_diversity_2(self):
        self.assertEqual(b'GET /bk HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///bk')))

    def test_diversity_3(self):
        self.assertEqual(b'GET /chgjse.dat HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///chgjse.dat')))

    def test_diversity_4(self):
        self.assertEqual(b'GET /vksxur.txt HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///vksxur.txt')))

    def test_diversity_5(self):
        self.assertEqual(b'GET /ispxta/zo/kby HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///ispxta/zo/kby')))

    def test_diversity_6(self):
        self.assertEqual(b'GET /ngcs/fn.dat HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///ngcs/fn.dat')))

    def test_diversity_7(self):
        self.assertEqual(b'GET /mqk/pn/ycq.log HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///mqk/pn/ycq.log')))

    def test_diversity_8(self):
        self.assertEqual(b'GET /xtjb HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///xtjb')))

    def test_diversity_9(self):
        self.assertEqual(b'GET /tle/mtkt/wfw.json HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///tle/mtkt/wfw.json')))

    def test_diversity_10(self):
        self.assertEqual(b'GET /in/uxd/ca HTTP/1.1\r\nHost: \r\n\r\n', request_httprepr(Request('file:///in/uxd/ca')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(b'GET /grmg HTTP/1.1\r\nHost: ckcjvf.net\r\n\r\n', request_httprepr(Request('http://ckcjvf.net/grmg')))

    def test_diversity_2(self):
        self.assertEqual(b'GET /wlfsqt/plnfcz/luvwby?oqqy=144 HTTP/1.1\r\nHost: xjfsaedf.com\r\n\r\n', request_httprepr(Request('http://xjfsaedf.com/wlfsqt/plnfcz/luvwby?oqqy=144')))

    def test_diversity_3(self):
        self.assertEqual(b'GET /hacca HTTP/1.1\r\nHost: wdcjh.org\r\n\r\n', request_httprepr(Request('ftp://wdcjh.org/hacca')))

    def test_diversity_4(self):
        self.assertEqual(b'GET /qin?m=147 HTTP/1.1\r\nHost: yxznr.net\r\n\r\n', request_httprepr(Request('https://yxznr.net/qin?m=147')))

    def test_diversity_5(self):
        self.assertEqual(b'GET /tjt HTTP/1.1\r\nHost: cmygzbti.com\r\n\r\n', request_httprepr(Request('http://cmygzbti.com/tjt')))

    def test_diversity_6(self):
        self.assertEqual(b'GET /ddfpk?xqlq=954 HTTP/1.1\r\nHost: hrzh.net\r\n\r\n', request_httprepr(Request('http://hrzh.net/ddfpk?xqlq=954')))

    def test_diversity_7(self):
        self.assertEqual(b'GET /rjhlj HTTP/1.1\r\nHost: vlvlazc.org\r\n\r\n', request_httprepr(Request('https://vlvlazc.org/rjhlj')))

    def test_diversity_8(self):
        self.assertEqual(b'GET /xakia/hl?sxsv=332 HTTP/1.1\r\nHost: akcl.net\r\n\r\n', request_httprepr(Request('https://akcl.net/xakia/hl?sxsv=332')))

    def test_diversity_9(self):
        self.assertEqual(b'GET /kmvmo/pc?lbr=143 HTTP/1.1\r\nHost: ylimnfj.com\r\n\r\n', request_httprepr(Request('https://ylimnfj.com/kmvmo/pc?lbr=143')))

    def test_diversity_10(self):
        self.assertEqual(b'GET /irhe HTTP/1.1\r\nHost: feene.net\r\n\r\n', request_httprepr(Request('https://feene.net/irhe')))
