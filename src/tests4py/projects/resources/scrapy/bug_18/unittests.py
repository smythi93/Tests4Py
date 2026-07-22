import unittest

from scrapy.responsetypes import responsetypes
import scrapy.http


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIs(scrapy.http.XmlResponse, responsetypes.from_content_disposition(b'attachment; filename=vtm\xe0.xml'))

    def test_diversity_2(self):
        self.assertIs(scrapy.http.TextResponse, responsetypes.from_content_disposition(b'attachment; filename=zawnf\xe9dl.txt'))

    def test_diversity_3(self):
        self.assertIs(scrapy.http.XmlResponse, responsetypes.from_content_disposition(b'attachment; filename=nuevjzl\xb5l.xml'))

    def test_diversity_4(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=mdufo\xb5hjm.html'))

    def test_diversity_5(self):
        self.assertIs(scrapy.http.TextResponse, responsetypes.from_content_disposition(b'attachment; filename=bzmx\xdft.txt'))

    def test_diversity_6(self):
        self.assertIs(scrapy.http.Response, responsetypes.from_content_disposition(b'attachment; filename=rdepw\xf6j'))

    def test_diversity_7(self):
        self.assertIs(scrapy.http.Response, responsetypes.from_content_disposition(b'attachment; filename=rehi\xe0'))

    def test_diversity_8(self):
        self.assertIs(scrapy.http.TextResponse, responsetypes.from_content_disposition(b'attachment; filename=ciulwkw\xf6ct.txt'))

    def test_diversity_9(self):
        self.assertIs(scrapy.http.XmlResponse, responsetypes.from_content_disposition(b'attachment; filename=gbns\xe9ad.xml'))

    def test_diversity_10(self):
        self.assertIs(scrapy.http.Response, responsetypes.from_content_disposition(b'attachment; filename=unky\xf1zj'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=ezlyt.html'))

    def test_diversity_2(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=jdnt.html'))

    def test_diversity_3(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=wkejeqfn.html'))

    def test_diversity_4(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=wmdalts.html'))

    def test_diversity_5(self):
        self.assertIs(scrapy.http.Response, responsetypes.from_content_disposition(b'attachment; filename=vzayq'))

    def test_diversity_6(self):
        self.assertIs(scrapy.http.Response, responsetypes.from_content_disposition(b'attachment; filename="wzr"'))

    def test_diversity_7(self):
        self.assertIs(scrapy.http.XmlResponse, responsetypes.from_content_disposition(b'attachment; filename=wnl.xml'))

    def test_diversity_8(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=cdcfqz.html'))

    def test_diversity_9(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=afd.html'))

    def test_diversity_10(self):
        self.assertIs(scrapy.http.HtmlResponse, responsetypes.from_content_disposition(b'attachment; filename=oeub.html'))
