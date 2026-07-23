import unittest
from tornado.httputil import url_concat



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('https://atcntrjg.net/nucol/su?jg=16&fd=94', url_concat('https://atcntrjg.net/nucol/su?jg=16&fd=94', None))

    def test_diversity_2(self):
        self.assertEqual('https://ykpb.com/maiscr', url_concat('https://ykpb.com/maiscr', None))

    def test_diversity_3(self):
        self.assertEqual('https://yjfqyfog.io/cs/pgkp/zj', url_concat('https://yjfqyfog.io/cs/pgkp/zj', None))

    def test_diversity_4(self):
        self.assertEqual('https://luikj.io/qr/gu/ovcxjf?coj=35&up=76', url_concat('https://luikj.io/qr/gu/ovcxjf?coj=35&up=76', None))

    def test_diversity_5(self):
        self.assertEqual('https://lfzqvoo.org/ykwhyp/wifag/oglabd?rul=44&tgw=36', url_concat('https://lfzqvoo.org/ykwhyp/wifag/oglabd?rul=44&tgw=36', None))

    def test_diversity_6(self):
        self.assertEqual('https://szmsqdz.com/mroas?i=57', url_concat('https://szmsqdz.com/mroas?i=57', None))

    def test_diversity_7(self):
        self.assertEqual('https://wmftslzi.io/umqipu?j=73&o=1', url_concat('https://wmftslzi.io/umqipu?j=73&o=1', None))

    def test_diversity_8(self):
        self.assertEqual('https://xofo.org/fyxomk/gjyulo?wgx=73', url_concat('https://xofo.org/fyxomk/gjyulo?wgx=73', None))

    def test_diversity_9(self):
        self.assertEqual('https://liipych.com/hap/ri/fw?ga=47&f=31', url_concat('https://liipych.com/hap/ri/fw?ga=47&f=31', None))

    def test_diversity_10(self):
        self.assertEqual('https://ldwpak.io/gxi/hsby?w=88&h=88', url_concat('https://ldwpak.io/gxi/hsby?w=88&h=88', None))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('https://kwuujlk.com/nto/ykgowk/tnj?kt=780', url_concat('https://kwuujlk.com/nto/ykgowk/tnj', [('kt', '780')]))

    def test_diversity_2(self):
        self.assertEqual('https://savf.io/ygm/samig?n=334&fha=qyef', url_concat('https://savf.io/ygm/samig', [('n', '334'), ('fha', 'qyef')]))

    def test_diversity_3(self):
        self.assertEqual('https://gbukjkqb.net/rc/hvxth/qpnrfq?astc=dak&e=906', url_concat('https://gbukjkqb.net/rc/hvxth/qpnrfq', [('astc', 'dak'), ('e', '906')]))

    def test_diversity_4(self):
        self.assertEqual('https://nlands.com/ujjdno/jcfxpy?mj=553', url_concat('https://nlands.com/ujjdno/jcfxpy', [('mj', '553')]))

    def test_diversity_5(self):
        self.assertEqual('https://kpcjyb.org/nj/ivky?qke=mfh&czql=279&o=409', url_concat('https://kpcjyb.org/nj/ivky', [('qke', 'mfh'), ('czql', '279'), ('o', '409')]))

    def test_diversity_6(self):
        self.assertEqual('https://pneuqrdh.org/uswmiu?by=guaux&ei=nlsxl&uhgb=ubm', url_concat('https://pneuqrdh.org/uswmiu', [('by', 'guaux'), ('ei', 'nlsxl'), ('uhgb', 'ubm')]))

    def test_diversity_7(self):
        self.assertEqual('https://enornuc.net/rzpqk/fjhl/rp?v=161&hy=bizkg', url_concat('https://enornuc.net/rzpqk/fjhl/rp', [('v', '161'), ('hy', 'bizkg')]))

    def test_diversity_8(self):
        self.assertEqual('https://qqtopgv.com/ruo?upxl=zm&lk=eme&uixk=374', url_concat('https://qqtopgv.com/ruo', [('upxl', 'zm'), ('lk', 'eme'), ('uixk', '374')]))

    def test_diversity_9(self):
        self.assertEqual('https://fxtbjwg.com/miwxm/tonyzr/jb?u=38&khwi=yl', url_concat('https://fxtbjwg.com/miwxm/tonyzr/jb', [('u', '38'), ('khwi', 'yl')]))

    def test_diversity_10(self):
        self.assertEqual('https://jvptcit.com/dw/mzix/pyd?oip=459&hyal=xhge', url_concat('https://jvptcit.com/dw/mzix/pyd', [('oip', '459'), ('hyal', 'xhge')]))
