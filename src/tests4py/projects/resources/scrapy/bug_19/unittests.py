import unittest

from scrapy.http import Request
from scrapy.http.cookies import WrappedRequest


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('vtm.net', WrappedRequest(Request('http://vtm.net/ii/km/gbd')).host)

    def test_diversity_2(self):
        self.assertEqual('eoianfyu.io', WrappedRequest(Request('http://eoianfyu.io/lcm/ouj/ommsqg')).origin_req_host)

    def test_diversity_3(self):
        self.assertEqual('eagtmr.com', WrappedRequest(Request('http://eagtmr.com/diw')).origin_req_host)

    def test_diversity_4(self):
        self.assertEqual('rodjo.com', WrappedRequest(Request('http://rodjo.com/ubqg/ciulwk')).host)

    def test_diversity_5(self):
        self.assertEqual('jpox.net', WrappedRequest(Request('http://jpox.net/hg')).host)

    def test_diversity_6(self):
        self.assertEqual('http', WrappedRequest(Request('http://vad.io/nk')).type)

    def test_diversity_7(self):
        self.assertEqual('http://zjaez.io/tncj/qmc', WrappedRequest(Request('http://zjaez.io/tncj/qmc')).full_url)

    def test_diversity_8(self):
        self.assertEqual('http://wkejeqfn.org/wmdalt', WrappedRequest(Request('http://wkejeqfn.org/wmdalt')).full_url)

    def test_diversity_9(self):
        self.assertEqual('hvjxtm.org', WrappedRequest(Request('http://hvjxtm.org/wz/sf')).host)

    def test_diversity_10(self):
        self.assertEqual('http://vftcdc.org/zrsc/hzo/xe', WrappedRequest(Request('http://vftcdc.org/zrsc/hzo/xe')).full_url)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('cjqt.com', WrappedRequest(Request('http://cjqt.com/qtdnfq')).get_origin_req_host())

    def test_diversity_2(self):
        self.assertEqual('wytzai.org', WrappedRequest(Request('http://wytzai.org/shyd')).get_host())

    def test_diversity_3(self):
        self.assertEqual('psalcvb.com', WrappedRequest(Request('http://psalcvb.com/dtvp/bqgy/sbbtsh')).get_host())

    def test_diversity_4(self):
        self.assertEqual('lwazbft.net', WrappedRequest(Request('http://lwazbft.net/djyiv')).get_origin_req_host())

    def test_diversity_5(self):
        self.assertEqual('rkh.com', WrappedRequest(Request('http://rkh.com/ps/jnbbqn')).get_origin_req_host())

    def test_diversity_6(self):
        self.assertEqual('http', WrappedRequest(Request('http://asv.com/kzx/kisxjk')).get_type())

    def test_diversity_7(self):
        self.assertEqual('http://nyev.com/fppqo/idlja/vwwk', WrappedRequest(Request('http://nyev.com/fppqo/idlja/vwwk')).get_full_url())

    def test_diversity_8(self):
        self.assertEqual('http', WrappedRequest(Request('http://kskp.net/ye/lxxdj/cjq')).get_type())

    def test_diversity_9(self):
        self.assertEqual('ann.net', WrappedRequest(Request('http://ann.net/desg/hanfp/babkad')).get_host())

    def test_diversity_10(self):
        self.assertEqual('http://emzyoeuf.com/bdg', WrappedRequest(Request('http://emzyoeuf.com/bdg')).get_full_url())
