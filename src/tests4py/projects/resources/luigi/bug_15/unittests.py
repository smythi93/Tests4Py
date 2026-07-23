import unittest
import time
from luigi.scheduler import CentralPlannerScheduler

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_vrbqa', [('assistant', True)])
            sch.ping(worker='AS_vrbqa')
            sch.add_task(worker='UP_vrbqa', task_id='T_vrbqa', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_vrbqa')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_vrbqa')
            sch.prune()
            exists = 'T_vrbqa' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_xayxpk', [('assistant', True)])
            sch.ping(worker='AS_xayxpk')
            sch.add_task(worker='UP_xayxpk', task_id='T_xayxpk', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_xayxpk')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_xayxpk')
            sch.prune()
            exists = 'T_xayxpk' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_xuyd', [('assistant', True)])
            sch.ping(worker='AS_xuyd')
            sch.add_task(worker='UP_xuyd', task_id='T_xuyd', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_xuyd')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_xuyd')
            sch.prune()
            exists = 'T_xuyd' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_nqtno', [('assistant', True)])
            sch.ping(worker='AS_nqtno')
            sch.add_task(worker='UP_nqtno', task_id='T_nqtno', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_nqtno')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_nqtno')
            sch.prune()
            exists = 'T_nqtno' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_ooiizl', [('assistant', True)])
            sch.ping(worker='AS_ooiizl')
            sch.add_task(worker='UP_ooiizl', task_id='T_ooiizl', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_ooiizl')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_ooiizl')
            sch.prune()
            exists = 'T_ooiizl' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_fmoqrkwa', [('assistant', True)])
            sch.ping(worker='AS_fmoqrkwa')
            sch.add_task(worker='UP_fmoqrkwa', task_id='T_fmoqrkwa', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_fmoqrkwa')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_fmoqrkwa')
            sch.prune()
            exists = 'T_fmoqrkwa' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_lxpjiht', [('assistant', True)])
            sch.ping(worker='AS_lxpjiht')
            sch.add_task(worker='UP_lxpjiht', task_id='T_lxpjiht', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_lxpjiht')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_lxpjiht')
            sch.prune()
            exists = 'T_lxpjiht' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_hbvyyab', [('assistant', True)])
            sch.ping(worker='AS_hbvyyab')
            sch.add_task(worker='UP_hbvyyab', task_id='T_hbvyyab', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_hbvyyab')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_hbvyyab')
            sch.prune()
            exists = 'T_hbvyyab' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_zgpcumsr', [('assistant', True)])
            sch.ping(worker='AS_zgpcumsr')
            sch.add_task(worker='UP_zgpcumsr', task_id='T_zgpcumsr', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_zgpcumsr')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_zgpcumsr')
            sch.prune()
            exists = 'T_zgpcumsr' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_tost', [('assistant', True)])
            sch.ping(worker='AS_tost')
            sch.add_task(worker='UP_tost', task_id='T_tost', status='UNKNOWN')
            time.time = lambda: 100000
            sch.ping(worker='AS_tost')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_tost')
            sch.prune()
            exists = 'T_tost' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_prwdzsm', [('assistant', True)])
            sch.ping(worker='AS_prwdzsm')
            sch.add_task(worker='UP_prwdzsm', task_id='T_prwdzsm', status='DISABLED')
            time.time = lambda: 100000
            sch.ping(worker='AS_prwdzsm')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_prwdzsm')
            sch.prune()
            exists = 'T_prwdzsm' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_ytdkwcpuv', [('assistant', True)])
            sch.ping(worker='AS_ytdkwcpuv')
            sch.add_task(worker='UP_ytdkwcpuv', task_id='T_ytdkwcpuv', status='DONE')
            time.time = lambda: 100000
            sch.ping(worker='AS_ytdkwcpuv')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_ytdkwcpuv')
            sch.prune()
            exists = 'T_ytdkwcpuv' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_nrag', [('assistant', True)])
            sch.ping(worker='AS_nrag')
            sch.add_task(worker='UP_nrag', task_id='T_nrag', status='DISABLED')
            time.time = lambda: 100000
            sch.ping(worker='AS_nrag')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_nrag')
            sch.prune()
            exists = 'T_nrag' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_pycteqmbh', [('assistant', True)])
            sch.ping(worker='AS_pycteqmbh')
            sch.add_task(worker='UP_pycteqmbh', task_id='T_pycteqmbh', status='DONE')
            time.time = lambda: 100000
            sch.ping(worker='AS_pycteqmbh')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_pycteqmbh')
            sch.prune()
            exists = 'T_pycteqmbh' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_djzcqx', [('assistant', True)])
            sch.ping(worker='AS_djzcqx')
            sch.add_task(worker='UP_djzcqx', task_id='T_djzcqx', status='DISABLED')
            time.time = lambda: 100000
            sch.ping(worker='AS_djzcqx')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_djzcqx')
            sch.prune()
            exists = 'T_djzcqx' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_xjsvag', [('assistant', True)])
            sch.ping(worker='AS_xjsvag')
            sch.add_task(worker='UP_xjsvag', task_id='T_xjsvag', status='DISABLED')
            time.time = lambda: 100000
            sch.ping(worker='AS_xjsvag')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_xjsvag')
            sch.prune()
            exists = 'T_xjsvag' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_rtgu', [('assistant', True)])
            sch.ping(worker='AS_rtgu')
            sch.add_task(worker='UP_rtgu', task_id='T_rtgu', status='DISABLED')
            time.time = lambda: 100000
            sch.ping(worker='AS_rtgu')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_rtgu')
            sch.prune()
            exists = 'T_rtgu' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_uotr', [('assistant', True)])
            sch.ping(worker='AS_uotr')
            sch.add_task(worker='UP_uotr', task_id='T_uotr', status='DONE')
            time.time = lambda: 100000
            sch.ping(worker='AS_uotr')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_uotr')
            sch.prune()
            exists = 'T_uotr' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_tdcf', [('assistant', True)])
            sch.ping(worker='AS_tdcf')
            sch.add_task(worker='UP_tdcf', task_id='T_tdcf', status='DISABLED')
            time.time = lambda: 100000
            sch.ping(worker='AS_tdcf')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_tdcf')
            sch.prune()
            exists = 'T_tdcf' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=100000000000)
            sch.add_worker('AS_waxddl', [('assistant', True)])
            sch.ping(worker='AS_waxddl')
            sch.add_task(worker='UP_waxddl', task_id='T_waxddl', status='DISABLED')
            time.time = lambda: 100000
            sch.ping(worker='AS_waxddl')
            sch.prune()
            time.time = lambda: 200000
            sch.ping(worker='AS_waxddl')
            sch.prune()
            exists = 'T_waxddl' in sch.task_list(None, '')
        finally:
            time.time = _orig
        self.assertFalse(exists)
