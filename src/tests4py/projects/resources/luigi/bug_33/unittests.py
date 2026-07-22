import unittest
import luigi



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        class Task_pos_fmukwd_kjfrpnri(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_fmukwd_kjfrpnri('fmukwd', 'kjfrpnri')
        self.assertIsNotNone(t)

    def test_diversity_2(self):
        class Task_pos_qdv_zrijl(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_qdv_zrijl('qdv', 'zrijl')
        self.assertIsNotNone(t)

    def test_diversity_3(self):
        class Task_pos_htpzwsoj_etp(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_htpzwsoj_etp('htpzwsoj', 'etp')
        self.assertIsNotNone(t)

    def test_diversity_4(self):
        class Task_pos_yonqr_fqsglto(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_yonqr_fqsglto('yonqr', 'fqsglto')
        self.assertIsNotNone(t)

    def test_diversity_5(self):
        class Task_pos_sioryc_kaf(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_sioryc_kaf('sioryc', 'kaf')
        self.assertIsNotNone(t)

    def test_diversity_6(self):
        class Task_pos_pyo_olvf(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_pyo_olvf('pyo', 'olvf')
        self.assertIsNotNone(t)

    def test_diversity_7(self):
        class Task_pos_yxx_lth(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_yxx_lth('yxx', 'lth')
        self.assertIsNotNone(t)

    def test_diversity_8(self):
        class Task_pos_wjg_ezbhua(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_wjg_ezbhua('wjg', 'ezbhua')
        self.assertIsNotNone(t)

    def test_diversity_9(self):
        class Task_pos_vhp_bavcfd(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_vhp_bavcfd('vhp', 'bavcfd')
        self.assertIsNotNone(t)

    def test_diversity_10(self):
        class Task_pos_wlere_yphjn(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_pos_wlere_yphjn('wlere', 'yphjn')
        self.assertIsNotNone(t)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        class Task_allkw_ylrryzol_zfms(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_ylrryzol_zfms(x='ylrryzol', y='zfms')
        self.assertIsNotNone(t)

    def test_diversity_2(self):
        class Task_allkw_brnxtgos_mfwvk(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_brnxtgos_mfwvk(x='brnxtgos', y='mfwvk')
        self.assertIsNotNone(t)

    def test_diversity_3(self):
        class Task_allkw_wxgymqy_mdhuf(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_wxgymqy_mdhuf(x='wxgymqy', y='mdhuf')
        self.assertIsNotNone(t)

    def test_diversity_4(self):
        class Task_allkw_zubetfwk_sie(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_zubetfwk_sie(x='zubetfwk', y='sie')
        self.assertIsNotNone(t)

    def test_diversity_5(self):
        class Task_allkw_sduvx_tbuav(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_sduvx_tbuav(x='sduvx', y='tbuav')
        self.assertIsNotNone(t)

    def test_diversity_6(self):
        class Task_allkw_kqga_nsslj(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_kqga_nsslj(x='kqga', y='nsslj')
        self.assertIsNotNone(t)

    def test_diversity_7(self):
        class Task_allkw_eemcmlz_abzzbeep(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_eemcmlz_abzzbeep(x='eemcmlz', y='abzzbeep')
        self.assertIsNotNone(t)

    def test_diversity_8(self):
        class Task_kw_ywgg_tgzxs(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_kw_ywgg_tgzxs('ywgg', y='tgzxs')
        self.assertIsNotNone(t)

    def test_diversity_9(self):
        class Task_allkw_kezeyy_cnpmpr(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_kezeyy_cnpmpr(x='kezeyy', y='cnpmpr')
        self.assertIsNotNone(t)

    def test_diversity_10(self):
        class Task_allkw_awndezio_dtamldpt(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        t = Task_allkw_awndezio_dtamldpt(x='awndezio', y='dtamldpt')
        self.assertIsNotNone(t)
