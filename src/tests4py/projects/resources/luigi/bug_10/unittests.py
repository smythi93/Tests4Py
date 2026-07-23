import unittest
import luigi.scheduler

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_lhzda', task_id='TP_lhzda', status='PENDING')
        sch.add_task(worker='OW_lhzda', task_id='OP_lhzda', status='PENDING')
        sch.add_task(worker='TW_lhzda', task_id='DN_lhzda', status='DONE')
        st = sch._state
        target = st.get_worker('TW_lhzda')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_lhzda'})

    def test_diversity_2(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_zqtx', task_id='TP_zqtx', status='PENDING')
        sch.add_task(worker='OW_zqtx', task_id='OP_zqtx', status='PENDING')
        sch.add_task(worker='TW_zqtx', task_id='DN_zqtx', status='DONE')
        st = sch._state
        target = st.get_worker('TW_zqtx')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_zqtx'})

    def test_diversity_3(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_qhyxm', task_id='TP_qhyxm', status='PENDING')
        sch.add_task(worker='OW_qhyxm', task_id='OP_qhyxm', status='PENDING')
        sch.add_task(worker='TW_qhyxm', task_id='DN_qhyxm', status='DONE')
        st = sch._state
        target = st.get_worker('TW_qhyxm')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_qhyxm'})

    def test_diversity_4(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_ttdxpsna', task_id='TP_ttdxpsna', status='PENDING')
        sch.add_task(worker='OW_ttdxpsna', task_id='OP_ttdxpsna', status='PENDING')
        sch.add_task(worker='TW_ttdxpsna', task_id='DN_ttdxpsna', status='DONE')
        st = sch._state
        target = st.get_worker('TW_ttdxpsna')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_ttdxpsna'})

    def test_diversity_5(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_zreoghii', task_id='TP_zreoghii', status='PENDING')
        sch.add_task(worker='OW_zreoghii', task_id='OP_zreoghii', status='PENDING')
        sch.add_task(worker='TW_zreoghii', task_id='DN_zreoghii', status='DONE')
        st = sch._state
        target = st.get_worker('TW_zreoghii')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_zreoghii'})

    def test_diversity_6(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_hjjjiv', task_id='TP_hjjjiv', status='PENDING')
        sch.add_task(worker='OW_hjjjiv', task_id='OP_hjjjiv', status='PENDING')
        sch.add_task(worker='TW_hjjjiv', task_id='DN_hjjjiv', status='DONE')
        st = sch._state
        target = st.get_worker('TW_hjjjiv')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_hjjjiv'})

    def test_diversity_7(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_cfbtoh', task_id='TP_cfbtoh', status='PENDING')
        sch.add_task(worker='OW_cfbtoh', task_id='OP_cfbtoh', status='PENDING')
        sch.add_task(worker='TW_cfbtoh', task_id='DN_cfbtoh', status='DONE')
        st = sch._state
        target = st.get_worker('TW_cfbtoh')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_cfbtoh'})

    def test_diversity_8(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_nzcrljkav', task_id='TP_nzcrljkav', status='PENDING')
        sch.add_task(worker='OW_nzcrljkav', task_id='OP_nzcrljkav', status='PENDING')
        sch.add_task(worker='TW_nzcrljkav', task_id='DN_nzcrljkav', status='DONE')
        st = sch._state
        target = st.get_worker('TW_nzcrljkav')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_nzcrljkav'})

    def test_diversity_9(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_mqtxokaie', task_id='TP_mqtxokaie', status='PENDING')
        sch.add_task(worker='OW_mqtxokaie', task_id='OP_mqtxokaie', status='PENDING')
        sch.add_task(worker='TW_mqtxokaie', task_id='DN_mqtxokaie', status='DONE')
        st = sch._state
        target = st.get_worker('TW_mqtxokaie')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_mqtxokaie'})

    def test_diversity_10(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_uqpaqhd', task_id='TP_uqpaqhd', status='PENDING')
        sch.add_task(worker='OW_uqpaqhd', task_id='OP_uqpaqhd', status='PENDING')
        sch.add_task(worker='TW_uqpaqhd', task_id='DN_uqpaqhd', status='DONE')
        st = sch._state
        target = st.get_worker('TW_uqpaqhd')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_uqpaqhd'})

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_xbiuvck', task_id='TP_xbiuvck', status='PENDING')
        sch.add_task(worker='OW_xbiuvck', task_id='OP_xbiuvck', status='PENDING')
        sch.add_task(worker='OW_xbiuvck', task_id='EP1_xbiuvck', status='PENDING')
        sch.add_task(worker='OW_xbiuvck', task_id='EP2_xbiuvck', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_xbiuvck')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_xbiuvck'})

    def test_diversity_2(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_xvlbru', task_id='TP_xvlbru', status='PENDING')
        sch.add_task(worker='OW_xvlbru', task_id='OP_xvlbru', status='PENDING')
        sch.add_task(worker='OW_xvlbru', task_id='EP1_xvlbru', status='PENDING')
        sch.add_task(worker='OW_xvlbru', task_id='EP2_xvlbru', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_xvlbru')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_xvlbru'})

    def test_diversity_3(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_eabsgi', task_id='TP_eabsgi', status='PENDING')
        sch.add_task(worker='OW_eabsgi', task_id='OP_eabsgi', status='PENDING')
        sch.add_task(worker='OW_eabsgi', task_id='EP1_eabsgi', status='PENDING')
        sch.add_task(worker='OW_eabsgi', task_id='EP2_eabsgi', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_eabsgi')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_eabsgi'})

    def test_diversity_4(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_syaf', task_id='TP_syaf', status='PENDING')
        sch.add_task(worker='OW_syaf', task_id='OP_syaf', status='PENDING')
        sch.add_task(worker='OW_syaf', task_id='EP1_syaf', status='PENDING')
        sch.add_task(worker='OW_syaf', task_id='EP2_syaf', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_syaf')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_syaf'})

    def test_diversity_5(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_xryfiq', task_id='TP_xryfiq', status='PENDING')
        sch.add_task(worker='OW_xryfiq', task_id='OP_xryfiq', status='PENDING')
        sch.add_task(worker='OW_xryfiq', task_id='EP1_xryfiq', status='PENDING')
        sch.add_task(worker='OW_xryfiq', task_id='EP2_xryfiq', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_xryfiq')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_xryfiq'})

    def test_diversity_6(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_uznd', task_id='TP_uznd', status='PENDING')
        sch.add_task(worker='OW_uznd', task_id='OP_uznd', status='PENDING')
        sch.add_task(worker='OW_uznd', task_id='EP1_uznd', status='PENDING')
        sch.add_task(worker='OW_uznd', task_id='EP2_uznd', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_uznd')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_uznd'})

    def test_diversity_7(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_nflkokw', task_id='TP_nflkokw', status='PENDING')
        sch.add_task(worker='OW_nflkokw', task_id='OP_nflkokw', status='PENDING')
        sch.add_task(worker='OW_nflkokw', task_id='EP1_nflkokw', status='PENDING')
        sch.add_task(worker='OW_nflkokw', task_id='EP2_nflkokw', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_nflkokw')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_nflkokw'})

    def test_diversity_8(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_ypvmv', task_id='TP_ypvmv', status='PENDING')
        sch.add_task(worker='OW_ypvmv', task_id='OP_ypvmv', status='PENDING')
        sch.add_task(worker='OW_ypvmv', task_id='EP1_ypvmv', status='PENDING')
        sch.add_task(worker='OW_ypvmv', task_id='EP2_ypvmv', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_ypvmv')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_ypvmv'})

    def test_diversity_9(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_wdrsxz', task_id='TP_wdrsxz', status='PENDING')
        sch.add_task(worker='OW_wdrsxz', task_id='OP_wdrsxz', status='PENDING')
        sch.add_task(worker='OW_wdrsxz', task_id='EP1_wdrsxz', status='PENDING')
        sch.add_task(worker='OW_wdrsxz', task_id='EP2_wdrsxz', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_wdrsxz')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_wdrsxz'})

    def test_diversity_10(self):
        sch = luigi.scheduler.Scheduler()
        sch.add_task(worker='TW_dxhu', task_id='TP_dxhu', status='PENDING')
        sch.add_task(worker='OW_dxhu', task_id='OP_dxhu', status='PENDING')
        sch.add_task(worker='OW_dxhu', task_id='EP1_dxhu', status='PENDING')
        sch.add_task(worker='OW_dxhu', task_id='EP2_dxhu', status='PENDING')
        st = sch._state
        target = st.get_worker('TW_dxhu')
        got = {t.id for t in target.get_pending_tasks(st)}
        self.assertEqual(got, {'TP_dxhu'})
