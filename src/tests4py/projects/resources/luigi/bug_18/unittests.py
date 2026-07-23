import unittest
import time
from luigi.scheduler import CentralPlannerScheduler, FAILED, DISABLED

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_ojwfvbbwu', task_id='T_ojwfvbbwu', status=FAILED)
            sch.add_task(worker='w_ojwfvbbwu', task_id='T_ojwfvbbwu', status=FAILED)
            sch.add_task(worker='w_ojwfvbbwu', task_id='T_ojwfvbbwu', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_ojwfvbbwu']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_ncdknd', task_id='T_ncdknd', status=FAILED)
            sch.add_task(worker='w_ncdknd', task_id='T_ncdknd', status=FAILED)
            sch.add_task(worker='w_ncdknd', task_id='T_ncdknd', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_ncdknd']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_dyfnkhwkv', task_id='T_dyfnkhwkv', status=FAILED)
            sch.add_task(worker='w_dyfnkhwkv', task_id='T_dyfnkhwkv', status=FAILED)
            sch.add_task(worker='w_dyfnkhwkv', task_id='T_dyfnkhwkv', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_dyfnkhwkv']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_zixbrq', task_id='T_zixbrq', status=FAILED)
            sch.add_task(worker='w_zixbrq', task_id='T_zixbrq', status=FAILED)
            sch.add_task(worker='w_zixbrq', task_id='T_zixbrq', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_zixbrq']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_ytiz', task_id='T_ytiz', status=FAILED)
            sch.add_task(worker='w_ytiz', task_id='T_ytiz', status=FAILED)
            sch.add_task(worker='w_ytiz', task_id='T_ytiz', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_ytiz']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_fktajm', task_id='T_fktajm', status=FAILED)
            sch.add_task(worker='w_fktajm', task_id='T_fktajm', status=FAILED)
            sch.add_task(worker='w_fktajm', task_id='T_fktajm', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_fktajm']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_gqvsoihu', task_id='T_gqvsoihu', status=FAILED)
            sch.add_task(worker='w_gqvsoihu', task_id='T_gqvsoihu', status=FAILED)
            sch.add_task(worker='w_gqvsoihu', task_id='T_gqvsoihu', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_gqvsoihu']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_eyhb', task_id='T_eyhb', status=FAILED)
            sch.add_task(worker='w_eyhb', task_id='T_eyhb', status=FAILED)
            sch.add_task(worker='w_eyhb', task_id='T_eyhb', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_eyhb']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_vwmfm', task_id='T_vwmfm', status=FAILED)
            sch.add_task(worker='w_vwmfm', task_id='T_vwmfm', status=FAILED)
            sch.add_task(worker='w_vwmfm', task_id='T_vwmfm', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_vwmfm']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_wninwjlm', task_id='T_wninwjlm', status=FAILED)
            sch.add_task(worker='w_wninwjlm', task_id='T_wninwjlm', status=FAILED)
            sch.add_task(worker='w_wninwjlm', task_id='T_wninwjlm', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_wninwjlm']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_bzidnbfvp', task_id='T_bzidnbfvp', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_bzidnbfvp']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_tttxfrs', task_id='T_tttxfrs', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_tttxfrs']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_ckvngi', task_id='T_ckvngi', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_ckvngi']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_elql', task_id='T_elql', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_elql']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_vogovcy', task_id='T_vogovcy', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_vogovcy']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_ceayg', task_id='T_ceayg', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_ceayg']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_kxmzu', task_id='T_kxmzu', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_kxmzu']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_semlu', task_id='T_semlu', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_semlu']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_hlzlfljc', task_id='T_hlzlfljc', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_hlzlfljc']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
            sch.add_task(worker='w_ejhbguh', task_id='T_ejhbguh', status=DISABLED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_ejhbguh']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'DISABLED')
