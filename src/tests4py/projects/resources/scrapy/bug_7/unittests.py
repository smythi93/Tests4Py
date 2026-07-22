import unittest

from scrapy.http import HtmlResponse, FormRequest


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        response = HtmlResponse(url='http://vvtm.net', body='<html><body><form action="  ii/km/gbd "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://vvtm.net/ii/km/gbd', request.url)

    def test_diversity_2(self):
        response = HtmlResponse(url='http://nuevjzl.io', body='<html><body><form action="  lcm/ouj/ommsqg  "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://nuevjzl.io/lcm/ouj/ommsqg', request.url)

    def test_diversity_3(self):
        response = HtmlResponse(url='http://xrez.net', body='<html><body><form action="  ed/wgun/rodj "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://xrez.net/ed/wgun/rodj', request.url)

    def test_diversity_4(self):
        response = HtmlResponse(url='http://xubqg.com', body='<html><body><form action=" hhhu "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://xubqg.com/hhhu', request.url)

    def test_diversity_5(self):
        response = HtmlResponse(url='http://jpox.net', body='<html><body><form action="  hg "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://jpox.net/hg', request.url)

    def test_diversity_6(self):
        response = HtmlResponse(url='http://advlu.net', body='<html><body><form action=" czjaez/hhhad  "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://advlu.net/czjaez/hhhad', request.url)

    def test_diversity_7(self):
        response = HtmlResponse(url='http://etr.net', body='<html><body><form action=" ej/tgt "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://etr.net/ej/tgt', request.url)

    def test_diversity_8(self):
        response = HtmlResponse(url='http://wmdalts.org', body='<html><body><form action="  vzay/pkwzr "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://wmdalts.org/vzay/pkwzr', request.url)

    def test_diversity_9(self):
        response = HtmlResponse(url='http://wnl.org', body='<html><body><form action=" cdcfq "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://wnl.org/cdcfq', request.url)

    def test_diversity_10(self):
        response = HtmlResponse(url='http://afd.org', body='<html><body><form action=" oeu "></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://afd.org/oeu', request.url)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        response = HtmlResponse(url='http://booz.net', body='<html><body><form action="qsgw"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://booz.net/qsgw', request.url)

    def test_diversity_2(self):
        response = HtmlResponse(url='http://tzaidjas.com', body='<html><body><form action="psalcv"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://tzaidjas.com/psalcv', request.url)

    def test_diversity_3(self):
        response = HtmlResponse(url='http://fub.net', body='<html><body><form action="tvpwj"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://fub.net/tvpwj', request.url)

    def test_diversity_4(self):
        response = HtmlResponse(url='http://qgyynd.com', body='<html><body><form action="tshk"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://qgyynd.com/tshk', request.url)

    def test_diversity_5(self):
        response = HtmlResponse(url='http://lwazbft.net', body='<html><body><form action="djyiv"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://lwazbft.net/djyiv', request.url)

    def test_diversity_6(self):
        response = HtmlResponse(url='http://cfjtaa.com', body='<html><body><form action="jnbbqn/ckyu/zq"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://cfjtaa.com/jnbbqn/ckyu/zq', request.url)

    def test_diversity_7(self):
        response = HtmlResponse(url='http://qdboar.net', body='<html><body><form action="healq/akcbfb/mtd"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://qdboar.net/healq/akcbfb/mtd', request.url)

    def test_diversity_8(self):
        response = HtmlResponse(url='http://jaite.io', body='<html><body><form action="eavf/gryemx/xd"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://jaite.io/eavf/gryemx/xd', request.url)

    def test_diversity_9(self):
        response = HtmlResponse(url='http://wcjqr.org', body='<html><body><form action="yj"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://wcjqr.org/yj', request.url)

    def test_diversity_10(self):
        response = HtmlResponse(url='http://sdesg.io', body='<html><body><form action="an/sro"></form></body></html>'.encode('utf-8'), encoding='utf-8')
        request = FormRequest.from_response(response)
        self.assertEqual('http://sdesg.io/an/sro', request.url)
