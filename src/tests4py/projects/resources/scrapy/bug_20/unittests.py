import unittest

from scrapy.spiders import SitemapSpider
from scrapy.http import TextResponse


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://vvtm.org/robots.txt', body=b'User-agent: *\nSitemap: http://nuevjzl.net/olcmdu.xml\nSitemap: http://jpkh.org/qgtlea.xml\nDisallow: /ii\nSitemap: http://kmu.com/jts.xml\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://nuevjzl.net/olcmdu.xml', 'http://jpkh.org/qgtlea.xml', 'http://kmu.com/jts.xml'], urls)

    def test_diversity_2(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://rdepw.com/robots.txt', body=b'Sitemap: http://huegug.com/teeehgi.xml\nDisallow: /jnm\nSitemap: http://advlu.net/kynib.xml\nSitemap: http://ehiiyx.net/yvciu.xml\nUser-agent: *\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://huegug.com/teeehgi.xml', 'http://advlu.net/kynib.xml', 'http://ehiiyx.net/yvciu.xml'], urls)

    def test_diversity_3(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://hhhadx.net/robots.txt', body=b'Disallow: /tetrh\nSitemap: http://dntg.net/scwmdal.xml\nUser-agent: *\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://dntg.net/scwmdal.xml'], urls)

    def test_diversity_4(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://hvjxtm.com/robots.txt', body=b'Disallow: /coqag\nUser-agent: *\nSitemap: http://bvftcdc.com/iqccafd.xml\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://bvftcdc.com/iqccafd.xml'], urls)

    def test_diversity_5(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://xek.com/robots.txt', body=b'Sitemap: http://tdnfqsg.org/zaid.xml\nDisallow: /bafd\nSitemap: http://shyde.net/alcvby.xml\nSitemap: http://bxdtvpwj.org/eyrs.xml\nUser-agent: *\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://tdnfqsg.org/zaid.xml', 'http://shyde.net/alcvby.xml', 'http://bxdtvpwj.org/eyrs.xml'], urls)

    def test_diversity_6(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://nrxtlwaz.com/robots.txt', body=b'Sitemap: http://gbj.net/umrk.xml\nSitemap: http://taabs.org/jcudack.xml\nDisallow: /hmg\nUser-agent: *\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://gbj.net/umrk.xml', 'http://taabs.org/jcudack.xml'], urls)

    def test_diversity_7(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://qdboar.org/robots.txt', body=b'Sitemap: http://sfp.net/qomt.xml\nSitemap: http://ryemxcp.net/wcjqr.xml\nSitemap: http://ljai.com/neavfn.xml\nUser-agent: *\nDisallow: /healq\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://sfp.net/qomt.xml', 'http://ryemxcp.net/wcjqr.xml', 'http://ljai.com/neavfn.xml'], urls)

    def test_diversity_8(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://zsdesgv.org/robots.txt', body=b'User-agent: *\nSitemap: http://psbabkad.net/yxe.xml\nDisallow: /an\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://psbabkad.net/yxe.xml'], urls)

    def test_diversity_9(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://oeuf.net/robots.txt', body=b'Disallow: /cb\nSitemap: http://gtl.com/bsh.xml\nUser-agent: *\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://gtl.com/bsh.xml'], urls)

    def test_diversity_10(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://tcgb.net/robots.txt', body=b'Disallow: /xpyzh\nSitemap: http://ojxrfqz.org/idtt.xml\nUser-agent: *\nSitemap: http://uzmnn.com/manifj.xml\nSitemap: http://cajzlwvi.org/bnpgc.xml\n', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual(['http://ojxrfqz.org/idtt.xml', 'http://uzmnn.com/manifj.xml', 'http://cajzlwvi.org/bnpgc.xml'], urls)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://fiqqlvq.com/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_2(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://yjeh.com/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_3(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://cuoufgf.org/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_4(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://btgcu.org/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_5(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://ynn.com/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_6(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://szjjp.com/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_7(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://ryudw.org/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_8(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://zcyjwm.com/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_9(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://gfr.com/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)

    def test_diversity_10(self):
        spider = SitemapSpider.__new__(SitemapSpider)
        response = TextResponse(url='http://grgejhl.net/robots.txt', body=b'', encoding='utf-8')
        urls = [r.url for r in spider._parse_sitemap(response)]
        self.assertEqual([], urls)
