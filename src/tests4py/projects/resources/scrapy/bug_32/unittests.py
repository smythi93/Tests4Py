import unittest

# noinspection PyUnresolvedReferences
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings, default_settings


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        rp = CrawlerProcess({'oklz': 'ebpwbwpc'})
        self.assertEqual('ebpwbwpc', rp.settings['oklz'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_2(self):
        rp = CrawlerProcess({'ocbdl': 'omlc'})
        self.assertEqual('omlc', rp.settings['ocbdl'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_3(self):
        rp = CrawlerProcess({'qbhsetcj': 'aum'})
        self.assertEqual('aum', rp.settings['qbhsetcj'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_4(self):
        rp = CrawlerProcess({'ergwkix': 'sdm'})
        self.assertEqual('sdm', rp.settings['ergwkix'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_5(self):
        rp = CrawlerProcess({'ykoc': 'dgtj'})
        self.assertEqual('dgtj', rp.settings['ykoc'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_6(self):
        rp = CrawlerProcess({'juqdtxo': 'shpacmjm'})
        self.assertEqual('shpacmjm', rp.settings['juqdtxo'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_7(self):
        rp = CrawlerProcess({'nmvy': 'kfdvmfve'})
        self.assertEqual('kfdvmfve', rp.settings['nmvy'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_8(self):
        rp = CrawlerProcess({'sakhjenr': 'qidgo'})
        self.assertEqual('qidgo', rp.settings['sakhjenr'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_9(self):
        rp = CrawlerProcess({'zefvq': 'ubyzb'})
        self.assertEqual('ubyzb', rp.settings['zefvq'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_10(self):
        rp = CrawlerProcess({'bks': 'zoh'})
        self.assertEqual('zoh', rp.settings['bks'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        rp = CrawlerProcess(Settings({'gjsedeyv': 'pioaeu'}))
        self.assertEqual('pioaeu', rp.settings['gjsedeyv'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_2(self):
        rp = CrawlerProcess(Settings({'opwlxyi': 'ofl'}))
        self.assertEqual('ofl', rp.settings['opwlxyi'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_3(self):
        rp = CrawlerProcess(Settings({'rlng': 'ibf'}))
        self.assertEqual('ibf', rp.settings['rlng'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_4(self):
        rp = CrawlerProcess(Settings({'eofdfgj': 'nqycqci'}))
        self.assertEqual('nqycqci', rp.settings['eofdfgj'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_5(self):
        rp = CrawlerProcess(Settings({'xtjbt': 'gsgktrmt'}))
        self.assertEqual('gsgktrmt', rp.settings['xtjbt'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_6(self):
        rp = CrawlerProcess(Settings({'lzwfwh': 'vbtcux'}))
        self.assertEqual('vbtcux', rp.settings['lzwfwh'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_7(self):
        rp = CrawlerProcess(Settings({'majy': 'eckc'}))
        self.assertEqual('eckc', rp.settings['majy'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_8(self):
        rp = CrawlerProcess(Settings({'osruf': 'vjhbd'}))
        self.assertEqual('vjhbd', rp.settings['osruf'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_9(self):
        rp = CrawlerProcess(Settings({'xjfsaedf': 'cswlfsq'}))
        self.assertEqual('cswlfsq', rp.settings['xjfsaedf'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])

    def test_diversity_10(self):
        rp = CrawlerProcess(Settings({'qpca': 'czpukmu'}))
        self.assertEqual('czpukmu', rp.settings['qpca'])
        self.assertEqual(default_settings.RETRY_ENABLED, rp.settings['RETRY_ENABLED'])
