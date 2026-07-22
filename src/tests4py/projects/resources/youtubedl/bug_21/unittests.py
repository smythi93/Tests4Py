import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import urljoin


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://oemyyi.net/ozc/exeh/gerp', urljoin(b'http://oemyyi.net/', '/ozc/exeh/gerp'))

    def test_diversity_2(self):
        self.assertEqual('http://ugi.org/sxezap/xsype/ppkw', urljoin(b'http://ugi.org/', b'/sxezap/xsype/ppkw'))

    def test_diversity_3(self):
        self.assertEqual('http://vlgoi.org/xegy', urljoin('http://vlgoi.org/', b'/xegy'))

    def test_diversity_4(self):
        self.assertEqual('http://fxakbxb.com/smuysv/znlrb/und', urljoin(b'http://fxakbxb.com/', '/smuysv/znlrb/und'))

    def test_diversity_5(self):
        self.assertEqual('http://edhmup.org/hibllt/vvvod', urljoin(b'http://edhmup.org/', '/hibllt/vvvod'))

    def test_diversity_6(self):
        self.assertEqual('http://fnxi.net/nje/vawv/rakk', urljoin(b'http://fnxi.net/', '/nje/vawv/rakk'))

    def test_diversity_7(self):
        self.assertEqual('http://ntuuohp.de/dzotkfl/yee', urljoin('http://ntuuohp.de/', b'/dzotkfl/yee'))

    def test_diversity_8(self):
        self.assertEqual('http://utfbj.com/anusaby/she', urljoin(b'http://utfbj.com/', b'/anusaby/she'))

    def test_diversity_9(self):
        self.assertEqual('http://oxglgk.org/xvi/feahtma/lihc', urljoin('http://oxglgk.org/', b'/xvi/feahtma/lihc'))

    def test_diversity_10(self):
        self.assertEqual('http://toinprk.net/konq/zenkinq/qis', urljoin(b'http://toinprk.net/', b'/konq/zenkinq/qis'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://mwubpuw.org/pcrseog', urljoin('http://mwubpuw.org/', '/pcrseog'))

    def test_diversity_2(self):
        self.assertEqual('http://viyaoio.com/uyuacvo', urljoin('http://viyaoio.com/', '/uyuacvo'))

    def test_diversity_3(self):
        self.assertEqual('http://qqluk.de/jik', urljoin('http://qqluk.de/', '/jik'))

    def test_diversity_4(self):
        self.assertEqual('http://adj.com/geq', urljoin('http://adj.com/', '/geq'))

    def test_diversity_5(self):
        self.assertEqual('http://ppnylja.org/ewflqsr', urljoin('http://ppnylja.org/', '/ewflqsr'))

    def test_diversity_6(self):
        self.assertEqual('http://nmohhd.com/qgepp/bkwxqu/nfh', urljoin('http://nmohhd.com/', '/qgepp/bkwxqu/nfh'))

    def test_diversity_7(self):
        self.assertEqual('http://vzqrui.net/ylnyq/guzcq', urljoin('http://vzqrui.net/', '/ylnyq/guzcq'))

    def test_diversity_8(self):
        self.assertEqual('http://lkyrg.com/jnyejlx/ghjy', urljoin('http://lkyrg.com/', '/jnyejlx/ghjy'))

    def test_diversity_9(self):
        self.assertEqual('http://foxxd.com/gkghcnw/bhf/kqbd', urljoin('http://foxxd.com/', '/gkghcnw/bhf/kqbd'))

    def test_diversity_10(self):
        self.assertEqual('http://jhplm.com/tyczzwc/zdjc/aufigxl', urljoin('http://jhplm.com/', '/tyczzwc/zdjc/aufigxl'))
