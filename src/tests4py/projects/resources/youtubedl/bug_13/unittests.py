import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import urljoin


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('rtmpe://cbrlizy.io/jkhp/xsype/ppkw', urljoin(None, 'rtmpe://cbrlizy.io/jkhp/xsype/ppkw'))

    def test_diversity_2(self):
        self.assertEqual('ftps://krmghz.net/gyx', urljoin(None, 'ftps://krmghz.net/gyx'))

    def test_diversity_3(self):
        self.assertEqual('rtmpe://fxakbxb.com/smuysv/znlrb/und', urljoin(None, 'rtmpe://fxakbxb.com/smuysv/znlrb/und'))

    def test_diversity_4(self):
        self.assertEqual('sftp://edhmup.org/hibllt/vvvod', urljoin(None, 'sftp://edhmup.org/hibllt/vvvod'))

    def test_diversity_5(self):
        self.assertEqual('sftp://fnxi.io/nje/vawv', urljoin(None, 'sftp://fnxi.io/nje/vawv'))

    def test_diversity_6(self):
        self.assertEqual('mms://kmi.io/tuuo/mahoy/otkflc', urljoin(None, 'mms://kmi.io/tuuo/mahoy/otkflc'))

    def test_diversity_7(self):
        self.assertEqual('sftp://wpxs.com/unag/anusaby/she', urljoin(None, 'sftp://wpxs.com/unag/anusaby/she'))

    def test_diversity_8(self):
        self.assertEqual('rtmpt://bhleeqi.de/ypxsq/maeqqwy', urljoin(None, 'rtmpt://bhleeqi.de/ypxsq/maeqqwy'))

    def test_diversity_9(self):
        self.assertEqual('rtsp://toinprk.net/konq/zenkinq/qis', urljoin(None, 'rtsp://toinprk.net/konq/zenkinq/qis'))

    def test_diversity_10(self):
        self.assertEqual('rtmpt://wubpu.de/pfu/seogvt', urljoin(None, 'rtmpt://wubpu.de/pfu/seogvt'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://iyaoio.com/uyuacvo', urljoin('http://iyaoio.com/', '/uyuacvo'))

    def test_diversity_2(self):
        self.assertEqual('http://qqluk.de/jik', urljoin('http://qqluk.de/', '/jik'))

    def test_diversity_3(self):
        self.assertEqual('http://adj.com/geq', urljoin('http://adj.com/', '/geq'))

    def test_diversity_4(self):
        self.assertEqual('http://ppnylja.org/ewflqsr', urljoin('http://ppnylja.org/', '/ewflqsr'))

    def test_diversity_5(self):
        self.assertEqual('http://nmohhd.com/qgepp/bkwxqu/nfh', urljoin('http://nmohhd.com/', '/qgepp/bkwxqu/nfh'))

    def test_diversity_6(self):
        self.assertEqual('http://vzqrui.io/hyqbpq/fyikj', urljoin('http://vzqrui.io/', '/hyqbpq/fyikj'))

    def test_diversity_7(self):
        self.assertEqual('http://hvkhsy.com/jnyejlx/ghjy', urljoin('http://hvkhsy.com/', '/jnyejlx/ghjy'))

    def test_diversity_8(self):
        self.assertEqual('http://foxxd.com/gkghcnw/bhf/kqbd', urljoin('http://foxxd.com/', '/gkghcnw/bhf/kqbd'))

    def test_diversity_9(self):
        self.assertEqual('http://jhplm.com/tyczzwc/zdjc/aufigxl', urljoin('http://jhplm.com/', '/tyczzwc/zdjc/aufigxl'))

    def test_diversity_10(self):
        self.assertEqual('http://qlbbs.net/zntgy/epbi/ijtlthk', urljoin('http://qlbbs.net/', '/zntgy/epbi/ijtlthk'))
