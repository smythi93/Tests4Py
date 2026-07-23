import unittest

from scrapy.http import Request
from scrapy.http.cookies import WrappedRequest


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        request = Request('http://example.com', headers={b'X-Test': b'vvt\xffozqii'})
        wrapped = WrappedRequest(request)
        self.assertEqual('vvt�ozqii', wrapped.get_header('X-Test'))

    def test_diversity_2(self):
        request = Request('http://example.com', headers={b'X-Test': b'km\xffgbd'})
        wrapped = WrappedRequest(request)
        self.assertEqual('km�gbd', wrapped.get_header('X-Test'))

    def test_diversity_3(self):
        request = Request('http://example.com', headers={b'X-Test': b'svnue\xffjzl'})
        wrapped = WrappedRequest(request)
        self.assertEqual('svnue�jzl', wrapped.get_header('X-Test'))

    def test_diversity_4(self):
        request = Request('http://example.com', headers={b'X-Test': b'olcmd\xffjpk'})
        wrapped = WrappedRequest(request)
        self.assertEqual('olcmd�jpk', wrapped.get_header('X-Test'))

    def test_diversity_5(self):
        request = Request('http://example.com', headers={b'X-Test': b'msqg\xffmxrez'})
        wrapped = WrappedRequest(request)
        self.assertEqual('msqg�mxrez', wrapped.get_header('X-Test'))

    def test_diversity_6(self):
        request = Request('http://example.com', headers={b'X-Test': b'rdep\xffwtf'})
        wrapped = WrappedRequest(request)
        self.assertEqual('rdep�wtf', wrapped.get_header('X-Test'))

    def test_diversity_7(self):
        request = Request('http://example.com', headers={b'X-Test': b'djobx\xffxp'})
        wrapped = WrappedRequest(request)
        self.assertEqual('djobx�xp', wrapped.get_header('X-Test'))

    def test_diversity_8(self):
        request = Request('http://example.com', headers={b'X-Test': b'fh\xfflwkw'})
        wrapped = WrappedRequest(request)
        self.assertEqual('fh�lwkw', wrapped.get_header('X-Test'))

    def test_diversity_9(self):
        request = Request('http://example.com', headers={b'X-Test': b'jpo\xffgbn'})
        wrapped = WrappedRequest(request)
        self.assertEqual('jpo�gbn', wrapped.get_header('X-Test'))

    def test_diversity_10(self):
        request = Request('http://example.com', headers={b'X-Test': b'bhll\xffebizq'})
        wrapped = WrappedRequest(request)
        self.assertEqual('bhll�ebizq', wrapped.get_header('X-Test'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        request = Request('http://example.com', headers={b'X-Test': b'ibth'})
        wrapped = WrappedRequest(request)
        self.assertEqual('ibth', wrapped.get_header('X-Test'))

    def test_diversity_2(self):
        request = Request('http://example.com', headers={b'X-Test': b'lytncjdnte'})
        wrapped = WrappedRequest(request)
        self.assertEqual('lytncjdnte', wrapped.get_header('X-Test'))

    def test_diversity_3(self):
        request = Request('http://example.com', headers={b'X-Test': b'rhcd'})
        wrapped = WrappedRequest(request)
        self.assertEqual('rhcd', wrapped.get_header('X-Test'))

    def test_diversity_4(self):
        request = Request('http://example.com', headers={b'X-Test': b'tgtnen'})
        wrapped = WrappedRequest(request)
        self.assertEqual('tgtnen', wrapped.get_header('X-Test'))

    def test_diversity_5(self):
        request = Request('http://example.com', headers={b'X-Test': b'mdaltsehvj'})
        wrapped = WrappedRequest(request)
        self.assertEqual('mdaltsehvj', wrapped.get_header('X-Test'))

    def test_diversity_6(self):
        request = Request('http://example.com', headers={b'X-Test': b'pkwzrsfwnl'})
        wrapped = WrappedRequest(request)
        self.assertEqual('pkwzrsfwnl', wrapped.get_header('X-Test'))

    def test_diversity_7(self):
        request = Request('http://example.com', headers={b'X-Test': b'cjxssy'})
        wrapped = WrappedRequest(request)
        self.assertEqual('cjxssy', wrapped.get_header('X-Test'))

    def test_diversity_8(self):
        request = Request('http://example.com', headers={b'X-Test': b'zrscthzo'})
        wrapped = WrappedRequest(request)
        self.assertEqual('zrscthzo', wrapped.get_header('X-Test'))

    def test_diversity_9(self):
        request = Request('http://example.com', headers={b'X-Test': b'xek'})
        wrapped = WrappedRequest(request)
        self.assertEqual('xek', wrapped.get_header('X-Test'))

    def test_diversity_10(self):
        request = Request('http://example.com', headers={b'X-Test': b'ubaf'})
        wrapped = WrappedRequest(request)
        self.assertEqual('ubaf', wrapped.get_header('X-Test'))
