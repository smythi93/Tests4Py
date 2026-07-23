import unittest
import luigi


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        class Task_insig_ulvdqx(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_ulvdqx(x='vxulvdqx', y='vyulvdqx')
        other = Task_insig_ulvdqx.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_2(self):
        class Task_insig_kguycwiu(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_kguycwiu(x='vxkguycwiu', y='vykguycwiu')
        other = Task_insig_kguycwiu.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_3(self):
        class Task_insig_lxjqjz(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_lxjqjz(x='vxlxjqjz', y='vylxjqjz')
        other = Task_insig_lxjqjz.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_4(self):
        class Task_insig_vadgduarj(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_vadgduarj(x='vxvadgduarj', y='vyvadgduarj')
        other = Task_insig_vadgduarj.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_5(self):
        class Task_insig_allyz(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_allyz(x='vxallyz', y='vyallyz')
        other = Task_insig_allyz.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_6(self):
        class Task_insig_nshpshtcm(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_nshpshtcm(x='vxnshpshtcm', y='vynshpshtcm')
        other = Task_insig_nshpshtcm.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_7(self):
        class Task_insig_tmtgdw(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_tmtgdw(x='vxtmtgdw', y='vytmtgdw')
        other = Task_insig_tmtgdw.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_8(self):
        class Task_insig_zqoqsr(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_zqoqsr(x='vxzqoqsr', y='vyzqoqsr')
        other = Task_insig_zqoqsr.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_9(self):
        class Task_insig_xdgbekos(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_xdgbekos(x='vxxdgbekos', y='vyxdgbekos')
        other = Task_insig_xdgbekos.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_10(self):
        class Task_insig_qydharb(luigi.Task):
            x = luigi.Parameter()
            y = luigi.Parameter(significant=False)
        original = Task_insig_qydharb(x='vxqydharb', y='vyqydharb')
        other = Task_insig_qydharb.from_str_params(original.to_str_params())
        self.assertEqual(original, other)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        class Task_sig_iguid(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_iguid(x='vxiguid', z='vziguid')
        other = Task_sig_iguid.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_2(self):
        class Task_sig_chbbbm(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_chbbbm(x='vxchbbbm', z='vzchbbbm')
        other = Task_sig_chbbbm.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_3(self):
        class Task_sig_wtcxvioye(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_wtcxvioye(x='vxwtcxvioye', z='vzwtcxvioye')
        other = Task_sig_wtcxvioye.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_4(self):
        class Task_sig_rumdehe(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_rumdehe(x='vxrumdehe', z='vzrumdehe')
        other = Task_sig_rumdehe.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_5(self):
        class Task_sig_mwwhnus(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_mwwhnus(x='vxmwwhnus', z='vzmwwhnus')
        other = Task_sig_mwwhnus.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_6(self):
        class Task_sig_swfhl(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_swfhl(x='vxswfhl', z='vzswfhl')
        other = Task_sig_swfhl.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_7(self):
        class Task_sig_cntzojh(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_cntzojh(x='vxcntzojh', z='vzcntzojh')
        other = Task_sig_cntzojh.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_8(self):
        class Task_sig_ijhx(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_ijhx(x='vxijhx', z='vzijhx')
        other = Task_sig_ijhx.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_9(self):
        class Task_sig_dbpnawwoc(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_dbpnawwoc(x='vxdbpnawwoc', z='vzdbpnawwoc')
        other = Task_sig_dbpnawwoc.from_str_params(original.to_str_params())
        self.assertEqual(original, other)

    def test_diversity_10(self):
        class Task_sig_pxlks(luigi.Task):
            x = luigi.Parameter()
            z = luigi.Parameter()
        original = Task_sig_pxlks(x='vxpxlks', z='vzpxlks')
        other = Task_sig_pxlks.from_str_params(original.to_str_params())
        self.assertEqual(original, other)
