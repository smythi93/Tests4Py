import unittest
import time
from luigi.scheduler import CentralPlannerScheduler, FAILED

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_buvjp', task_id='T_buvjp', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_buvjp']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_vsopv', task_id='T_vsopv', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_vsopv']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_ucxja', task_id='T_ucxja', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_ucxja']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_gqzn', task_id='T_gqzn', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_gqzn']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_kdlgkx', task_id='T_kdlgkx', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_kdlgkx']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_gyjrts', task_id='T_gyjrts', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_gyjrts']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_pdhrajp', task_id='T_pdhrajp', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_pdhrajp']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_lnnjl', task_id='T_lnnjl', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_lnnjl']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_qcvjgykk', task_id='T_qcvjgykk', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_qcvjgykk']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1, disable_persist=100)
            sch.add_task(worker='w_zrygy', task_id='T_zrygy', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_zrygy']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_woqyg', task_id='T_woqyg', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_woqyg']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_wksponr', task_id='T_wksponr', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_wksponr']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_dbiijvuz', task_id='T_dbiijvuz', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_dbiijvuz']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_xlpnvfeg', task_id='T_xlpnvfeg', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_xlpnvfeg']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_grngkcoi', task_id='T_grngkcoi', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_grngkcoi']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_zbykvml', task_id='T_zbykvml', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_zbykvml']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_juallo', task_id='T_juallo', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_juallo']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_xaombgr', task_id='T_xaombgr', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_xaombgr']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_jnvrur', task_id='T_jnvrur', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_jnvrur']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 0
            sch = CentralPlannerScheduler(disable_failures=1000, disable_persist=100)
            sch.add_task(worker='w_saiwyrgdw', task_id='T_saiwyrgdw', status=FAILED)
            time.time = lambda: 101
            status = sch.task_list('', '')['T_saiwyrgdw']['status']
        finally:
            time.time = _orig
        self.assertEqual(status, 'FAILED')
