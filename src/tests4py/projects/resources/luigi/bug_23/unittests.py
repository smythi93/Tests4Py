import unittest
import types
import luigi.scheduler

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        w = luigi.scheduler.Worker(34908)
        cfg = types.SimpleNamespace(worker_disconnect_delay=69381)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_2(self):
        w = luigi.scheduler.Worker(13630)
        cfg = types.SimpleNamespace(worker_disconnect_delay=73161)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_3(self):
        w = luigi.scheduler.Worker(41442)
        cfg = types.SimpleNamespace(worker_disconnect_delay=56275)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_4(self):
        w = luigi.scheduler.Worker(50194)
        cfg = types.SimpleNamespace(worker_disconnect_delay=1026)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_5(self):
        w = luigi.scheduler.Worker(4371)
        cfg = types.SimpleNamespace(worker_disconnect_delay=6284)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_6(self):
        w = luigi.scheduler.Worker(38679)
        cfg = types.SimpleNamespace(worker_disconnect_delay=76059)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_7(self):
        w = luigi.scheduler.Worker(98642)
        cfg = types.SimpleNamespace(worker_disconnect_delay=87930)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_8(self):
        w = luigi.scheduler.Worker(86465)
        cfg = types.SimpleNamespace(worker_disconnect_delay=45481)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_9(self):
        w = luigi.scheduler.Worker(58794)
        cfg = types.SimpleNamespace(worker_disconnect_delay=15743)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_10(self):
        w = luigi.scheduler.Worker(86989)
        cfg = types.SimpleNamespace(worker_disconnect_delay=93287)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        w = luigi.scheduler.Worker(79275, last_active=55037)
        cfg = types.SimpleNamespace(worker_disconnect_delay=58640)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_2(self):
        w = luigi.scheduler.Worker(57647, last_active=49147)
        cfg = types.SimpleNamespace(worker_disconnect_delay=94421)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_3(self):
        w = luigi.scheduler.Worker(15119, last_active=56289)
        cfg = types.SimpleNamespace(worker_disconnect_delay=33726)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_4(self):
        w = luigi.scheduler.Worker(83960, last_active=44123)
        cfg = types.SimpleNamespace(worker_disconnect_delay=74223)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_5(self):
        w = luigi.scheduler.Worker(71983, last_active=5470)
        cfg = types.SimpleNamespace(worker_disconnect_delay=96463)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_6(self):
        w = luigi.scheduler.Worker(84484, last_active=15879)
        cfg = types.SimpleNamespace(worker_disconnect_delay=19507)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_7(self):
        w = luigi.scheduler.Worker(31474, last_active=39999)
        cfg = types.SimpleNamespace(worker_disconnect_delay=80483)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_8(self):
        w = luigi.scheduler.Worker(10604, last_active=46225)
        cfg = types.SimpleNamespace(worker_disconnect_delay=33478)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_9(self):
        w = luigi.scheduler.Worker(2214, last_active=6149)
        cfg = types.SimpleNamespace(worker_disconnect_delay=72219)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)

    def test_diversity_10(self):
        w = luigi.scheduler.Worker(11820, last_active=49034)
        cfg = types.SimpleNamespace(worker_disconnect_delay=31593)
        w.prune(cfg)
        self.assertIsNotNone(w.last_active)
