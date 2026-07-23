import unittest
import time
from luigi.scheduler import CentralPlannerScheduler, FAILED

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_iqwoluxxd', [])
            sch.ping(worker='w_iqwoluxxd')
            time.time = lambda: 2
            sch.add_task(worker='w_iqwoluxxd', task_id='A_iqwoluxxd')
            sch.add_task(worker='w_iqwoluxxd', task_id='B_iqwoluxxd', deps=['A_iqwoluxxd'])
            sch.get_work(worker='w_iqwoluxxd')
            sch.add_task(worker='w_iqwoluxxd', task_id='A_iqwoluxxd', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_iqwoluxxd')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_zdskem', [])
            sch.ping(worker='w_zdskem')
            time.time = lambda: 2
            sch.add_task(worker='w_zdskem', task_id='A_zdskem')
            sch.add_task(worker='w_zdskem', task_id='B_zdskem', deps=['A_zdskem'])
            sch.get_work(worker='w_zdskem')
            sch.add_task(worker='w_zdskem', task_id='A_zdskem', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_zdskem')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_nviao', [])
            sch.ping(worker='w_nviao')
            time.time = lambda: 2
            sch.add_task(worker='w_nviao', task_id='A_nviao')
            sch.add_task(worker='w_nviao', task_id='B_nviao', deps=['A_nviao'])
            sch.get_work(worker='w_nviao')
            sch.add_task(worker='w_nviao', task_id='A_nviao', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_nviao')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_tdhgnho', [])
            sch.ping(worker='w_tdhgnho')
            time.time = lambda: 2
            sch.add_task(worker='w_tdhgnho', task_id='A_tdhgnho')
            sch.add_task(worker='w_tdhgnho', task_id='B_tdhgnho', deps=['A_tdhgnho'])
            sch.get_work(worker='w_tdhgnho')
            sch.add_task(worker='w_tdhgnho', task_id='A_tdhgnho', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_tdhgnho')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_nsgm', [])
            sch.ping(worker='w_nsgm')
            time.time = lambda: 2
            sch.add_task(worker='w_nsgm', task_id='A_nsgm')
            sch.add_task(worker='w_nsgm', task_id='B_nsgm', deps=['A_nsgm'])
            sch.get_work(worker='w_nsgm')
            sch.add_task(worker='w_nsgm', task_id='A_nsgm', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_nsgm')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_aznrn', [])
            sch.ping(worker='w_aznrn')
            time.time = lambda: 2
            sch.add_task(worker='w_aznrn', task_id='A_aznrn')
            sch.add_task(worker='w_aznrn', task_id='B_aznrn', deps=['A_aznrn'])
            sch.get_work(worker='w_aznrn')
            sch.add_task(worker='w_aznrn', task_id='A_aznrn', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_aznrn')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_jpsm', [])
            sch.ping(worker='w_jpsm')
            time.time = lambda: 2
            sch.add_task(worker='w_jpsm', task_id='A_jpsm')
            sch.add_task(worker='w_jpsm', task_id='B_jpsm', deps=['A_jpsm'])
            sch.get_work(worker='w_jpsm')
            sch.add_task(worker='w_jpsm', task_id='A_jpsm', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_jpsm')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_qcspazp', [])
            sch.ping(worker='w_qcspazp')
            time.time = lambda: 2
            sch.add_task(worker='w_qcspazp', task_id='A_qcspazp')
            sch.add_task(worker='w_qcspazp', task_id='B_qcspazp', deps=['A_qcspazp'])
            sch.get_work(worker='w_qcspazp')
            sch.add_task(worker='w_qcspazp', task_id='A_qcspazp', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_qcspazp')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_cblr', [])
            sch.ping(worker='w_cblr')
            time.time = lambda: 2
            sch.add_task(worker='w_cblr', task_id='A_cblr')
            sch.add_task(worker='w_cblr', task_id='B_cblr', deps=['A_cblr'])
            sch.get_work(worker='w_cblr')
            sch.add_task(worker='w_cblr', task_id='A_cblr', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_cblr')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
            sch.add_worker('w_vigpzuku', [])
            sch.ping(worker='w_vigpzuku')
            time.time = lambda: 2
            sch.add_task(worker='w_vigpzuku', task_id='A_vigpzuku')
            sch.add_task(worker='w_vigpzuku', task_id='B_vigpzuku', deps=['A_vigpzuku'])
            sch.get_work(worker='w_vigpzuku')
            sch.add_task(worker='w_vigpzuku', task_id='A_vigpzuku', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_vigpzuku')
        finally:
            time.time = _orig
        self.assertTrue(True)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_brff', [])
            sch.ping(worker='w_brff')
            time.time = lambda: 2
            sch.add_task(worker='w_brff', task_id='A_brff')
            sch.add_task(worker='w_brff', task_id='B_brff', deps=['A_brff'])
            sch.get_work(worker='w_brff')
            sch.add_task(worker='w_brff', task_id='A_brff', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_brff')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_2(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_fskssr', [])
            sch.ping(worker='w_fskssr')
            time.time = lambda: 2
            sch.add_task(worker='w_fskssr', task_id='A_fskssr')
            sch.add_task(worker='w_fskssr', task_id='B_fskssr', deps=['A_fskssr'])
            sch.get_work(worker='w_fskssr')
            sch.add_task(worker='w_fskssr', task_id='A_fskssr', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_fskssr')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_3(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_qenynamue', [])
            sch.ping(worker='w_qenynamue')
            time.time = lambda: 2
            sch.add_task(worker='w_qenynamue', task_id='A_qenynamue')
            sch.add_task(worker='w_qenynamue', task_id='B_qenynamue', deps=['A_qenynamue'])
            sch.get_work(worker='w_qenynamue')
            sch.add_task(worker='w_qenynamue', task_id='A_qenynamue', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_qenynamue')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_4(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_myexgy', [])
            sch.ping(worker='w_myexgy')
            time.time = lambda: 2
            sch.add_task(worker='w_myexgy', task_id='A_myexgy')
            sch.add_task(worker='w_myexgy', task_id='B_myexgy', deps=['A_myexgy'])
            sch.get_work(worker='w_myexgy')
            sch.add_task(worker='w_myexgy', task_id='A_myexgy', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_myexgy')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_5(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_gzqbeci', [])
            sch.ping(worker='w_gzqbeci')
            time.time = lambda: 2
            sch.add_task(worker='w_gzqbeci', task_id='A_gzqbeci')
            sch.add_task(worker='w_gzqbeci', task_id='B_gzqbeci', deps=['A_gzqbeci'])
            sch.get_work(worker='w_gzqbeci')
            sch.add_task(worker='w_gzqbeci', task_id='A_gzqbeci', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_gzqbeci')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_6(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_nrxwskzmv', [])
            sch.ping(worker='w_nrxwskzmv')
            time.time = lambda: 2
            sch.add_task(worker='w_nrxwskzmv', task_id='A_nrxwskzmv')
            sch.add_task(worker='w_nrxwskzmv', task_id='B_nrxwskzmv', deps=['A_nrxwskzmv'])
            sch.get_work(worker='w_nrxwskzmv')
            sch.add_task(worker='w_nrxwskzmv', task_id='A_nrxwskzmv', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_nrxwskzmv')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_7(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_jcfxw', [])
            sch.ping(worker='w_jcfxw')
            time.time = lambda: 2
            sch.add_task(worker='w_jcfxw', task_id='A_jcfxw')
            sch.add_task(worker='w_jcfxw', task_id='B_jcfxw', deps=['A_jcfxw'])
            sch.get_work(worker='w_jcfxw')
            sch.add_task(worker='w_jcfxw', task_id='A_jcfxw', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_jcfxw')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_8(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_tpguycko', [])
            sch.ping(worker='w_tpguycko')
            time.time = lambda: 2
            sch.add_task(worker='w_tpguycko', task_id='A_tpguycko')
            sch.add_task(worker='w_tpguycko', task_id='B_tpguycko', deps=['A_tpguycko'])
            sch.get_work(worker='w_tpguycko')
            sch.add_task(worker='w_tpguycko', task_id='A_tpguycko', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_tpguycko')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_9(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_rxxd', [])
            sch.ping(worker='w_rxxd')
            time.time = lambda: 2
            sch.add_task(worker='w_rxxd', task_id='A_rxxd')
            sch.add_task(worker='w_rxxd', task_id='B_rxxd', deps=['A_rxxd'])
            sch.get_work(worker='w_rxxd')
            sch.add_task(worker='w_rxxd', task_id='A_rxxd', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_rxxd')
        finally:
            time.time = _orig
        self.assertTrue(True)

    def test_diversity_10(self):
        _orig = time.time
        try:
            time.time = lambda: 1
            sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100, disable_failures=100)
            sch.add_worker('w_avuazhvu', [])
            sch.ping(worker='w_avuazhvu')
            time.time = lambda: 2
            sch.add_task(worker='w_avuazhvu', task_id='A_avuazhvu')
            sch.add_task(worker='w_avuazhvu', task_id='B_avuazhvu', deps=['A_avuazhvu'])
            sch.get_work(worker='w_avuazhvu')
            sch.add_task(worker='w_avuazhvu', task_id='A_avuazhvu', status=FAILED)
            time.time = lambda: 10
            sch.prune()
            sch.get_work(worker='w_avuazhvu')
        finally:
            time.time = _orig
        self.assertTrue(True)
