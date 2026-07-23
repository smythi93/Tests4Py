import unittest

from scrapy.http import Request


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertRaises(ValueError, Request, 'vvtm:zqiiq')

    def test_diversity_2(self):
        self.assertRaises(ValueError, Request, 'wnfqjt:eoianfyu')

    def test_diversity_3(self):
        self.assertRaises(ValueError, Request, 'polcmdu:jpkh')

    def test_diversity_4(self):
        self.assertRaises(ValueError, Request, 'sqgtl:xrez')

    def test_diversity_5(self):
        self.assertRaises(ValueError, Request, 'rdepw:wtfr')

    def test_diversity_6(self):
        self.assertRaises(ValueError, Request, 'mrehiiy:pyvciul')

    def test_diversity_7(self):
        self.assertRaises(ValueError, Request, 'egugct:xgbn')

    def test_diversity_8(self):
        self.assertRaises(ValueError, Request, 'ivadvlun:zqczja')

    def test_diversity_9(self):
        self.assertRaises(ValueError, Request, 'zmhh:ncjdn')

    def test_diversity_10(self):
        self.assertRaises(ValueError, Request, 'etr:kejeq')


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://tnen.io/gd/tsehv', Request('http://tnen.io/gd/tsehv').url)

    def test_diversity_2(self):
        self.assertEqual('http://ayqpk.com/fwnl/ftcdcf/iqccaf', Request('http://ayqpk.com/fwnl/ftcdcf/iqccaf').url)

    def test_diversity_3(self):
        self.assertEqual('http://zota.org/eubaf/oo/ojh', Request('http://zota.org/eubaf/oo/ojh').url)

    def test_diversity_4(self):
        self.assertEqual('http://wklrfmei.com/hy/xn', Request('http://wklrfmei.com/hy/xn').url)

    def test_diversity_5(self):
        self.assertEqual('http://salcvbyq.net/tvpwj', Request('http://salcvbyq.net/tvpwj').url)

    def test_diversity_6(self):
        self.assertEqual('http://qgyynd.com/tshk', Request('http://qgyynd.com/tshk').url)

    def test_diversity_7(self):
        self.assertEqual('http://lwazbft.net/djyiv', Request('http://lwazbft.net/djyiv').url)

    def test_diversity_8(self):
        self.assertEqual('http://cfjtaa.com/jnbbqn/ckyu/zq', Request('http://cfjtaa.com/jnbbqn/ckyu/zq').url)

    def test_diversity_9(self):
        self.assertEqual('http://qdboar.net/healq/akcbfb/mtd', Request('http://qdboar.net/healq/akcbfb/mtd').url)

    def test_diversity_10(self):
        self.assertEqual('http://jaite.io/eavf/gryemx/xd', Request('http://jaite.io/eavf/gryemx/xd').url)
