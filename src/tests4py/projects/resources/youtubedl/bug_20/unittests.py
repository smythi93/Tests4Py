import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import get_element_by_attribute


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('kbauv', get_element_by_attribute('id', 'rqsuwj', '<p selected id="rqsuwj">kbauv</p>'))

    def test_diversity_2(self):
        self.assertEqual('mpjkuga', get_element_by_attribute('rel', 'rgty', '<span checked rel="rgty">mpjkuga</span>'))

    def test_diversity_3(self):
        self.assertEqual('sqlxw', get_element_by_attribute('itemprop', 'pwnpnij', '<p selected itemprop="pwnpnij">sqlxw</p>'))

    def test_diversity_4(self):
        self.assertEqual('mpmmlst', get_element_by_attribute('id', 'hweypw', '<span id="hweypw" selected>mpmmlst</span>'))

    def test_diversity_5(self):
        self.assertEqual('iys', get_element_by_attribute('role', 'dumodug', '<section role="dumodug" checked>iys</section>'))

    def test_diversity_6(self):
        self.assertEqual('cfpijs', get_element_by_attribute('rel', 'rrmyxc', '<span rel="rrmyxc" disabled>cfpijs</span>'))

    def test_diversity_7(self):
        self.assertEqual('xezapxx', get_element_by_attribute('name', 'cbrlizy', '<span name="cbrlizy" required>xezapxx</span>'))

    def test_diversity_8(self):
        self.assertEqual('nigxkr', get_element_by_attribute('id', 'vwpp', '<section id="vwpp" hidden>nigxkr</section>'))

    def test_diversity_9(self):
        self.assertEqual('qfxak', get_element_by_attribute('id', 'xegy', '<p itemscope id="xegy">qfxak</p>'))

    def test_diversity_10(self):
        self.assertEqual('sviv', get_element_by_attribute('itemprop', 'vjxj', '<div itemprop="vjxj" selected>sviv</div>'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('lnycoi', get_element_by_attribute('name', 'und', '<div name="und">lnycoi</div>'))

    def test_diversity_2(self):
        self.assertEqual('tgeq', get_element_by_attribute('name', 'wmweuf', '<span name="wmweuf">tgeq</span>'))

    def test_diversity_3(self):
        self.assertEqual('irka', get_element_by_attribute('name', 'zzfn', '<section name="zzfn">irka</section>'))

    def test_diversity_4(self):
        self.assertEqual('rakk', get_element_by_attribute('id', 'vawv', '<p id="vawv">rakk</p>'))

    def test_diversity_5(self):
        self.assertEqual('mahoy', get_element_by_attribute('rel', 'tuuo', '<section rel="tuuo">mahoy</section>'))

    def test_diversity_6(self):
        self.assertEqual('eebuje', get_element_by_attribute('rel', 'kflc', '<a rel="kflc">eebuje</a>'))

    def test_diversity_7(self):
        self.assertEqual('xkm', get_element_by_attribute('itemprop', 'jdranus', '<span itemprop="jdranus">xkm</span>'))

    def test_diversity_8(self):
        self.assertEqual('lgktna', get_element_by_attribute('id', 'wmbh', '<p id="wmbh">lgktna</p>'))

    def test_diversity_9(self):
        self.assertEqual('lihc', get_element_by_attribute('name', 'feahtma', '<p name="feahtma">lihc</p>'))

    def test_diversity_10(self):
        self.assertEqual('nkonqn', get_element_by_attribute('rel', 'oinprk', '<div rel="oinprk">nkonqn</div>'))
