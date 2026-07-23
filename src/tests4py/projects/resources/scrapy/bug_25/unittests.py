import unittest

# noinspection PyUnresolvedReferences
from scrapy.http import HtmlResponse, FormRequest


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        response = HtmlResponse(url='http://tvayhm.com/', body=b'<html><head><base href="http://aocwo.org/"></head><body><form action="vnuqvejm"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://aocwo.org/vnuqvejm', req.url)

    def test_diversity_2(self):
        response = HtmlResponse(url='http://rpjjrqbk.com/', body=b'<html><head><base href="http://ndw.org/"></head><body><form action="ocp.html"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://ndw.org/ocp.html', req.url)

    def test_diversity_3(self):
        response = HtmlResponse(url='http://luprlvm.com/', body=b'<html><head><base href="http://bkvq.org/"></head><body><form action="ayloyv"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://bkvq.org/ayloyv', req.url)

    def test_diversity_4(self):
        response = HtmlResponse(url='http://geq.com/', body=b'<html><head><base href="http://fdyj.org/"></head><body><form action="qxun.html"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://fdyj.org/qxun.html', req.url)

    def test_diversity_5(self):
        response = HtmlResponse(url='http://jmmkj.com/', body=b'<html><head><base href="http://zctkuso.org/"></head><body><form action="xoeqntg"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://zctkuso.org/xoeqntg', req.url)

    def test_diversity_6(self):
        response = HtmlResponse(url='http://new.com/', body=b'<html><head><base href="http://xeicr.org/"></head><body><form action="sejhcps"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://xeicr.org/sejhcps', req.url)

    def test_diversity_7(self):
        response = HtmlResponse(url='http://sqvbqas.com/', body=b'<html><head><base href="http://ugsrhlh.org/"></head><body><form action="hhwhl/sub"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://ugsrhlh.org/hhwhl/sub', req.url)

    def test_diversity_8(self):
        response = HtmlResponse(url='http://ahtzi.com/', body=b'<html><head><base href="http://yglvbl.org/"></head><body><form action="xujbb"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://yglvbl.org/xujbb', req.url)

    def test_diversity_9(self):
        response = HtmlResponse(url='http://vkay.com/', body=b'<html><head><base href="http://rsxi.org/"></head><body><form action="zxbwzcw/sub"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://rsxi.org/zxbwzcw/sub', req.url)

    def test_diversity_10(self):
        response = HtmlResponse(url='http://cry.com/', body=b'<html><head><base href="http://bzbcym.org/"></head><body><form action="tuxt/sub"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://bzbcym.org/tuxt/sub', req.url)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        response = HtmlResponse(url='http://esobcsnv.com/', body=b'<html><head></head><body><form action="http://encl.net/qtjuynh"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://encl.net/qtjuynh', req.url)

    def test_diversity_2(self):
        response = HtmlResponse(url='http://sfzxki.com/', body=b'<html><head></head><body><form action="http://xelbm.net/gfhpvwjw"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://xelbm.net/gfhpvwjw', req.url)

    def test_diversity_3(self):
        response = HtmlResponse(url='http://imba.com/', body=b'<html><head></head><body><form action="http://cku.net/drajygi"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://cku.net/drajygi', req.url)

    def test_diversity_4(self):
        response = HtmlResponse(url='http://blm.com/', body=b'<html><head></head><body><form action="http://ogx.net/aibyaa"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://ogx.net/aibyaa', req.url)

    def test_diversity_5(self):
        response = HtmlResponse(url='http://pcq.com/', body=b'<html><head></head><body><form action="http://nuhckont.net/znwgjlz"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://nuhckont.net/znwgjlz', req.url)

    def test_diversity_6(self):
        response = HtmlResponse(url='http://ssxci.com/', body=b'<html><head></head><body><form action="http://agxlh.net/zpxnoz"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://agxlh.net/zpxnoz', req.url)

    def test_diversity_7(self):
        response = HtmlResponse(url='http://ezv.com/', body=b'<html><head></head><body><form action="http://issddpn.net/sqdlo"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://issddpn.net/sqdlo', req.url)

    def test_diversity_8(self):
        response = HtmlResponse(url='http://fyrudkua.com/', body=b'<html><head></head><body><form action="http://uskjp.net/rqr"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://uskjp.net/rqr', req.url)

    def test_diversity_9(self):
        response = HtmlResponse(url='http://vbqlmvf.com/', body=b'<html><head></head><body><form action="http://daeuwav.net/omjfhfyk"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://daeuwav.net/omjfhfyk', req.url)

    def test_diversity_10(self):
        response = HtmlResponse(url='http://mzpilg.com/', body=b'<html><head></head><body><form action="http://tzfrz.net/egyzk"></form></body></html>', encoding='utf-8')
        req = FormRequest.from_response(response)
        self.assertEqual('http://tzfrz.net/egyzk', req.url)

