import unittest
import types
import luigi.scheduler

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        w = luigi.scheduler.Worker(7883)
        cfg = types.SimpleNamespace(worker_disconnect_delay=99807)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_2(self):
        w = luigi.scheduler.Worker(64660)
        cfg = types.SimpleNamespace(worker_disconnect_delay=60988)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_3(self):
        w = luigi.scheduler.Worker(69134)
        cfg = types.SimpleNamespace(worker_disconnect_delay=77893)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_4(self):
        w = luigi.scheduler.Worker(65182)
        cfg = types.SimpleNamespace(worker_disconnect_delay=52345)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_5(self):
        w = luigi.scheduler.Worker(90623)
        cfg = types.SimpleNamespace(worker_disconnect_delay=23207)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_6(self):
        w = luigi.scheduler.Worker(43700)
        cfg = types.SimpleNamespace(worker_disconnect_delay=26586)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_7(self):
        w = luigi.scheduler.Worker(27525)
        cfg = types.SimpleNamespace(worker_disconnect_delay=18976)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_8(self):
        w = luigi.scheduler.Worker(55171)
        cfg = types.SimpleNamespace(worker_disconnect_delay=80523)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_9(self):
        w = luigi.scheduler.Worker(25678)
        cfg = types.SimpleNamespace(worker_disconnect_delay=18016)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_10(self):
        w = luigi.scheduler.Worker(4811)
        cfg = types.SimpleNamespace(worker_disconnect_delay=71791)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        w = luigi.scheduler.Worker(30759, last_active=93248)
        cfg = types.SimpleNamespace(worker_disconnect_delay=23625)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_2(self):
        w = luigi.scheduler.Worker(44208, last_active=59239)
        cfg = types.SimpleNamespace(worker_disconnect_delay=90526)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_3(self):
        w = luigi.scheduler.Worker(91579, last_active=91057)
        cfg = types.SimpleNamespace(worker_disconnect_delay=51014)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_4(self):
        w = luigi.scheduler.Worker(92553, last_active=37148)
        cfg = types.SimpleNamespace(worker_disconnect_delay=14394)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_5(self):
        w = luigi.scheduler.Worker(93560, last_active=662)
        cfg = types.SimpleNamespace(worker_disconnect_delay=37342)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_6(self):
        w = luigi.scheduler.Worker(1863, last_active=41927)
        cfg = types.SimpleNamespace(worker_disconnect_delay=34482)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_7(self):
        w = luigi.scheduler.Worker(85413, last_active=16292)
        cfg = types.SimpleNamespace(worker_disconnect_delay=88598)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_8(self):
        w = luigi.scheduler.Worker(55585, last_active=25141)
        cfg = types.SimpleNamespace(worker_disconnect_delay=17861)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_9(self):
        w = luigi.scheduler.Worker(90557, last_active=17595)
        cfg = types.SimpleNamespace(worker_disconnect_delay=22693)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_10(self):
        w = luigi.scheduler.Worker(14012, last_active=88893)
        cfg = types.SimpleNamespace(worker_disconnect_delay=67782)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)
