import unittest

from scrapy.http import Response


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        response = Response(url='http://vvtm.net')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_2(self):
        response = Response(url='http://axzawnfq.net')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_3(self):
        response = Response(url='http://tsvn.com')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_4(self):
        response = Response(url='http://nfyu.io')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_5(self):
        response = Response(url='http://ggglouj.io')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_6(self):
        response = Response(url='http://hjmibz.io')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_7(self):
        response = Response(url='http://xrez.net')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_8(self):
        response = Response(url='http://rediwwtf.io')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_9(self):
        response = Response(url='http://rehi.net')
        self.assertRaises(ValueError, response.follow, None)

    def test_diversity_10(self):
        response = Response(url='http://xpy.com')
        self.assertRaises(ValueError, response.follow, None)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        response = Response(url='http://iulw.io')
        self.assertEqual('http://wyxj.org/ehgi', response.follow('http://wyxj.org/ehgi').url)

    def test_diversity_2(self):
        response = Response(url='http://advlu.net')
        self.assertEqual('http://zqczja.org/hhhad/qmc', response.follow('http://zqczja.org/hhhad/qmc').url)

    def test_diversity_3(self):
        response = Response(url='http://trhcdnt.org')
        self.assertEqual('http://tnen.io/gd/tsehv', response.follow('http://tnen.io/gd/tsehv').url)

    def test_diversity_4(self):
        response = Response(url='http://ayqpk.com')
        self.assertEqual('http://gawbvftc.org/sy/zrsc/hzo', response.follow('http://gawbvftc.org/sy/zrsc/hzo').url)

    def test_diversity_5(self):
        response = Response(url='http://xek.com')
        self.assertEqual('http://bafdq.org/jhwwkl/zai/ash', response.follow('http://bafdq.org/jhwwkl/zai/ash').url)

    def test_diversity_6(self):
        response = Response(url='http://depsalcv.com')
        self.assertEqual('http://yqni.io/vpwj/qgyyn/bbt', response.follow('http://yqni.io/vpwj/qgyyn/bbt').url)

    def test_diversity_7(self):
        response = Response(url='http://rxtlwazb.org')
        self.assertEqual('http://tscdj.io/vumrkh/gp', response.follow('http://tscdj.io/vumrkh/gp').url)

    def test_diversity_8(self):
        response = Response(url='http://sjnbbqnh.com')
        self.assertEqual('http://svpblf.org/kisxjk', response.follow('http://svpblf.org/kisxjk').url)

    def test_diversity_9(self):
        response = Response(url='http://eal.com')
        self.assertEqual('http://kcbfbfid.io/wuvw/neavf', response.follow('http://kcbfbfid.io/wuvw/neavf').url)

    def test_diversity_10(self):
        response = Response(url='http://gryemxc.org')
        self.assertEqual('http://jelaqvsd.com/nigg/sgv/dtks', response.follow('http://jelaqvsd.com/nigg/sgv/dtks').url)
