import unittest
import time
from luigi.scheduler import CentralPlannerScheduler, FAILED

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_gbfcnst', [('assistant', True)])
            sch.add_task(worker='W_gbfcnst', task_id='A_gbfcnst', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_gbfcnst')
            status = sch.task_list('', '')['A_gbfcnst']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_ppegkcr', [('assistant', True)])
            sch.add_task(worker='W_ppegkcr', task_id='A_ppegkcr', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_ppegkcr')
            status = sch.task_list('', '')['A_ppegkcr']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_fmoz', [('assistant', True)])
            sch.add_task(worker='W_fmoz', task_id='A_fmoz', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_fmoz')
            status = sch.task_list('', '')['A_fmoz']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_qpxnw', [('assistant', True)])
            sch.add_task(worker='W_qpxnw', task_id='A_qpxnw', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_qpxnw')
            status = sch.task_list('', '')['A_qpxnw']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_vhufi', [('assistant', True)])
            sch.add_task(worker='W_vhufi', task_id='A_vhufi', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_vhufi')
            status = sch.task_list('', '')['A_vhufi']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_fmmjvq', [('assistant', True)])
            sch.add_task(worker='W_fmmjvq', task_id='A_fmmjvq', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_fmmjvq')
            status = sch.task_list('', '')['A_fmmjvq']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_laghq', [('assistant', True)])
            sch.add_task(worker='W_laghq', task_id='A_laghq', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_laghq')
            status = sch.task_list('', '')['A_laghq']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_ffhumkp', [('assistant', True)])
            sch.add_task(worker='W_ffhumkp', task_id='A_ffhumkp', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_ffhumkp')
            status = sch.task_list('', '')['A_ffhumkp']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_eycx', [('assistant', True)])
            sch.add_task(worker='W_eycx', task_id='A_eycx', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_eycx')
            status = sch.task_list('', '')['A_eycx']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_worker('W_mrvgq', [('assistant', True)])
            sch.add_task(worker='W_mrvgq', task_id='A_mrvgq', status=FAILED, assistant=True)
            time.time = lambda: 101
            sch.ping(worker='W_mrvgq')
            status = sch.task_list('', '')['A_mrvgq']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_lfwnhc', task_id='A_lfwnhc', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_lfwnhc')
            status = sch.task_list('', '')['A_lfwnhc']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_ecbr', task_id='A_ecbr', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_ecbr')
            status = sch.task_list('', '')['A_ecbr']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_srmj', task_id='A_srmj', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_srmj')
            status = sch.task_list('', '')['A_srmj']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_jrtvvgh', task_id='A_jrtvvgh', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_jrtvvgh')
            status = sch.task_list('', '')['A_jrtvvgh']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_imunhsk', task_id='A_imunhsk', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_imunhsk')
            status = sch.task_list('', '')['A_imunhsk']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_aimci', task_id='A_aimci', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_aimci')
            status = sch.task_list('', '')['A_aimci']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_coqz', task_id='A_coqz', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_coqz')
            status = sch.task_list('', '')['A_coqz']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_xfhtm', task_id='A_xfhtm', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_xfhtm')
            status = sch.task_list('', '')['A_xfhtm']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_nxzquitqy', task_id='A_nxzquitqy', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_nxzquitqy')
            status = sch.task_list('', '')['A_nxzquitqy']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(**{'retry_delay': 100, 'remove_delay': 1000, 'worker_disconnect_delay': 10, 'disable_persist': 10, 'disable_window': 10, 'disable_failures': 3, 'disable_hard_timeout': 3600})
            sch.add_task(worker='W_yhqijb', task_id='A_yhqijb', status=FAILED)
            time.time = lambda: 101
            sch.ping(worker='W_yhqijb')
            status = sch.task_list('', '')['A_yhqijb']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'PENDING')
