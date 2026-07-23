import unittest
import luigi.contrib.hive as hive

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nwdssebh'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Wdssebh'))

    def test_diversity_2(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\noapu'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Oapu'))

    def test_diversity_3(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nwcjbyn'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Wcjbyn'))

    def test_diversity_4(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\npavocv'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Pavocv'))

    def test_diversity_5(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nejhn'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Ejhn'))

    def test_diversity_6(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\ncsmtd'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Csmtd'))

    def test_diversity_7(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nitrlsjp'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Itrlsjp'))

    def test_diversity_8(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\neekvmyh'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Eekvmyh'))

    def test_diversity_9(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nlbrmbqmyw'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Lbrmbqmyw'))

    def test_diversity_10(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nwtfs'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('Wtfs'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nxrkqxw'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('xrkqxw'))

    def test_diversity_2(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\ngphhn'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('gphhn'))

    def test_diversity_3(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nvugnoiv'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('vugnoiv'))

    def test_diversity_4(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nytaiijb'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('ytaiijb'))

    def test_diversity_5(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\ntsuyueb'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('tsuyueb'))

    def test_diversity_6(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\noedopzzjl'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('oedopzzjl'))

    def test_diversity_7(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nnwakeby'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('nwakeby'))

    def test_diversity_8(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\nxyeqq'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('xyeqq'))

    def test_diversity_9(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\ngvpzmbgx'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('gvpzmbgx'))

    def test_diversity_10(self):
        hive.run_hive_cmd = lambda *a, **k: 'OK\ndfrugr'
        client = hive.HiveCommandClient()
        self.assertTrue(client.table_exists('dfrugr'))
