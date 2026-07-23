import unittest
from luigi.scheduler import Scheduler

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_ocximx', task_id='A_ocximx')
        sch.get_work(worker='X_ocximx')
        sch.add_task(worker='Y_ocximx', task_id='A_ocximx', status='UNKNOWN')
        status = sch.task_list('', '')['A_ocximx']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_2(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_pcwnanmh', task_id='A_pcwnanmh')
        sch.get_work(worker='X_pcwnanmh')
        sch.add_task(worker='Y_pcwnanmh', task_id='A_pcwnanmh', status='UNKNOWN')
        status = sch.task_list('', '')['A_pcwnanmh']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_3(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_vqmdzwg', task_id='A_vqmdzwg')
        sch.get_work(worker='X_vqmdzwg')
        sch.add_task(worker='Y_vqmdzwg', task_id='A_vqmdzwg', status='UNKNOWN')
        status = sch.task_list('', '')['A_vqmdzwg']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_4(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_djcmave', task_id='A_djcmave')
        sch.get_work(worker='X_djcmave')
        sch.add_task(worker='Y_djcmave', task_id='A_djcmave', status='UNKNOWN')
        status = sch.task_list('', '')['A_djcmave']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_5(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_atwby', task_id='A_atwby')
        sch.get_work(worker='X_atwby')
        sch.add_task(worker='Y_atwby', task_id='A_atwby', status='UNKNOWN')
        status = sch.task_list('', '')['A_atwby']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_6(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_yjrjdwxp', task_id='A_yjrjdwxp')
        sch.get_work(worker='X_yjrjdwxp')
        sch.add_task(worker='Y_yjrjdwxp', task_id='A_yjrjdwxp', status='UNKNOWN')
        status = sch.task_list('', '')['A_yjrjdwxp']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_7(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_ybodxy', task_id='A_ybodxy')
        sch.get_work(worker='X_ybodxy')
        sch.add_task(worker='Y_ybodxy', task_id='A_ybodxy', status='UNKNOWN')
        status = sch.task_list('', '')['A_ybodxy']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_8(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_qeuk', task_id='A_qeuk')
        sch.get_work(worker='X_qeuk')
        sch.add_task(worker='Y_qeuk', task_id='A_qeuk', status='UNKNOWN')
        status = sch.task_list('', '')['A_qeuk']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_9(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_kzykcsjum', task_id='A_kzykcsjum')
        sch.get_work(worker='X_kzykcsjum')
        sch.add_task(worker='Y_kzykcsjum', task_id='A_kzykcsjum', status='UNKNOWN')
        status = sch.task_list('', '')['A_kzykcsjum']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_10(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_jyibwjmi', task_id='A_jyibwjmi')
        sch.get_work(worker='X_jyibwjmi')
        sch.add_task(worker='Y_jyibwjmi', task_id='A_jyibwjmi', status='UNKNOWN')
        status = sch.task_list('', '')['A_jyibwjmi']['status']
        self.assertEqual(status, 'RUNNING')

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_ygqfj', task_id='A_ygqfj')
        sch.get_work(worker='X_ygqfj')
        sch.add_task(worker='Y_ygqfj', task_id='A_ygqfj', status='PENDING')
        status = sch.task_list('', '')['A_ygqfj']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_2(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_ezow', task_id='A_ezow')
        sch.get_work(worker='X_ezow')
        sch.add_task(worker='Y_ezow', task_id='A_ezow', status='PENDING')
        status = sch.task_list('', '')['A_ezow']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_3(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_nlqwgtapg', task_id='A_nlqwgtapg')
        sch.get_work(worker='X_nlqwgtapg')
        sch.add_task(worker='Y_nlqwgtapg', task_id='A_nlqwgtapg', status='PENDING')
        status = sch.task_list('', '')['A_nlqwgtapg']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_4(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_asdwzd', task_id='A_asdwzd')
        sch.get_work(worker='X_asdwzd')
        sch.add_task(worker='Y_asdwzd', task_id='A_asdwzd', status='PENDING')
        status = sch.task_list('', '')['A_asdwzd']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_5(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_culrqv', task_id='A_culrqv')
        sch.get_work(worker='X_culrqv')
        sch.add_task(worker='Y_culrqv', task_id='A_culrqv', status='PENDING')
        status = sch.task_list('', '')['A_culrqv']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_6(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_yutgot', task_id='A_yutgot')
        sch.get_work(worker='X_yutgot')
        sch.add_task(worker='Y_yutgot', task_id='A_yutgot', status='PENDING')
        status = sch.task_list('', '')['A_yutgot']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_7(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_hkbd', task_id='A_hkbd')
        sch.get_work(worker='X_hkbd')
        sch.add_task(worker='Y_hkbd', task_id='A_hkbd', status='PENDING')
        status = sch.task_list('', '')['A_hkbd']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_8(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_sgsu', task_id='A_sgsu')
        sch.get_work(worker='X_sgsu')
        sch.add_task(worker='Y_sgsu', task_id='A_sgsu', status='PENDING')
        status = sch.task_list('', '')['A_sgsu']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_9(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_mmqrnmqs', task_id='A_mmqrnmqs')
        sch.get_work(worker='X_mmqrnmqs')
        sch.add_task(worker='Y_mmqrnmqs', task_id='A_mmqrnmqs', status='PENDING')
        status = sch.task_list('', '')['A_mmqrnmqs']['status']
        self.assertEqual(status, 'RUNNING')

    def test_diversity_10(self):
        sch = Scheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'retry_count': 3, 'disable_hard_timeout': 3600})
        sch.add_task(worker='X_wgiflsis', task_id='A_wgiflsis')
        sch.get_work(worker='X_wgiflsis')
        sch.add_task(worker='Y_wgiflsis', task_id='A_wgiflsis', status='PENDING')
        status = sch.task_list('', '')['A_wgiflsis']['status']
        self.assertEqual(status, 'RUNNING')
