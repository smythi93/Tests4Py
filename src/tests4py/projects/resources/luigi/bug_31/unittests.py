import unittest
from luigi.scheduler import CentralPlannerScheduler, DONE

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('fygaqvvx', task_id='srku', runnable=False)
        r = sch.get_work('jjunrcxsw', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_2(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('rgasv', task_id='wedix', runnable=False)
        r = sch.get_work('byzpmini', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_3(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('flkx', task_id='zrhgzlg', runnable=False)
        r = sch.get_work('qrtu', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_4(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('mxmnhzrf', task_id='tzjtys', runnable=False)
        r = sch.get_work('dnhmpzq', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_5(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('xxlecmu', task_id='kbgmnmtkm', runnable=False)
        r = sch.get_work('loxve', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_6(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('emyb', task_id='opnva', runnable=False)
        r = sch.get_work('xhetr', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_7(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('zdeac', task_id='oovckbsdx', runnable=False)
        r = sch.get_work('tjiih', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_8(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('kjtby', task_id='jelimru', runnable=False)
        r = sch.get_work('gplggnvvd', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_9(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('lumbibbo', task_id='bbobe', runnable=False)
        r = sch.get_work('fhirgnbe', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_10(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('krqufpdb', task_id='qpsiwdu', runnable=False)
        r = sch.get_work('greq', assistant=True)
        self.assertIsNone(r['task_id'])

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('ooqe', task_id='tqlkd', status=DONE)
        r = sch.get_work('xeiys', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_2(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('gfyoawpx', task_id='uakrnr', status=DONE)
        r = sch.get_work('dcveipgxb', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_3(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('rkgqixf', task_id='xqbwom', status=DONE)
        r = sch.get_work('oijxagfub', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_4(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('qrxw', task_id='kziiraaey', status=DONE)
        r = sch.get_work('wmdset', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_5(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('bmkb', task_id='ksfy', status=DONE)
        r = sch.get_work('lsbz', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_6(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('mxuyxi', task_id='ecqwr', status=DONE)
        r = sch.get_work('xnvhq', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_7(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('gvxpsgt', task_id='tbjtcmwyc', status=DONE)
        r = sch.get_work('omwodvq', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_8(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('wnzh', task_id='ckuhspg', status=DONE)
        r = sch.get_work('wfdqsabul', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_9(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('nnhhbsr', task_id='ngczukhu', status=DONE)
        r = sch.get_work('otrpz', assistant=True)
        self.assertIsNone(r['task_id'])

    def test_diversity_10(self):
        sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3})
        sch.add_task('ntyegxf', task_id='yeqzacrrd', status=DONE)
        r = sch.get_work('tkhxea', assistant=True)
        self.assertIsNone(r['task_id'])
