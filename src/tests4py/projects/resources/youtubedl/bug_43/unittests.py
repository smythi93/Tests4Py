import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import url_basename


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('lgktna.html', url_basename('http://wfqox.com/jdranus/xkm/lgktna.html'))

    def test_diversity_2(self):
        self.assertEqual('csdwbq.json', url_basename('http://ecxipze.de/ypxsq/maeqqwy/vto/zsauy/csdwbq.json'))

    def test_diversity_3(self):
        self.assertEqual('ngc.html', url_basename('http://iyaoio.com/bpu/jpf/seogvt/ngc.html'))

    def test_diversity_4(self):
        self.assertEqual('sadjt.mp4', url_basename('http://fji.net/cvo/qqluk/sadjt.mp4'))

    def test_diversity_5(self):
        self.assertEqual('kogjysw.html', url_basename('http://wflqsrj.net/oaipp/utrvkio/kogjysw.html'))

    def test_diversity_6(self):
        self.assertEqual('bpqguzc.html', url_basename('http://iyxky.net/geppt/gjb/quunf/evzqr/bpqguzc.html'))

    def test_diversity_7(self):
        self.assertEqual('ilir.txt', url_basename('http://ghjy.org/hvkhsy/ljny/bopq/ilir.txt'))

    def test_diversity_8(self):
        self.assertEqual('wcddmww.mp4', url_basename('http://otyc.com/gkghcnw/bhf/kqbd/jhplm/wcddmww.mp4'))

    def test_diversity_9(self):
        self.assertEqual('iavu.html', url_basename('http://nzntgy.com/djps/qlbbs/iavu.html'))

    def test_diversity_10(self):
        self.assertEqual('udhoygh.mp4', url_basename('http://ran.com/ldcrq/vsdkmba/qsn/ubbjsmq/udhoygh.mp4'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('ffhq.json', url_basename('http://hrimqak.org/ffhq.json'))

    def test_diversity_2(self):
        self.assertEqual('gfp.json', url_basename('http://mht.de/pkylzxb/gfp.json'))

    def test_diversity_3(self):
        self.assertEqual('trvi.mp4', url_basename('http://edc.de/zcdlakk/trvi.mp4'))

    def test_diversity_4(self):
        self.assertEqual('ywhw.json', url_basename('http://krlzrnj.org/hcnmyic/ywhw.json'))

    def test_diversity_5(self):
        self.assertEqual('usf.txt', url_basename('http://gcpvmin.de/backkji/usf.txt'))

    def test_diversity_6(self):
        self.assertEqual('yvhunwv.html', url_basename('http://jxxmn.de/acxenl/yvhunwv.html'))

    def test_diversity_7(self):
        self.assertEqual('aniw.txt', url_basename('http://pmmruh.net/aniw.txt'))

    def test_diversity_8(self):
        self.assertEqual('vcuxfr.json', url_basename('http://rnigln.de/vcuxfr.json'))

    def test_diversity_9(self):
        self.assertEqual('hfbqk.json', url_basename('http://xtvedy.de/hfbqk.json'))

    def test_diversity_10(self):
        self.assertEqual('cnrm.html', url_basename('http://told.org/duie/cnrm.html'))
