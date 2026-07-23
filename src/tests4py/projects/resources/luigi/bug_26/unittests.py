import unittest
from luigi.contrib.hadoop_jar import HadoopJarJobRunner, HadoopJarJobError

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        class FakeJob_pkcte:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_pkcte())

    def test_diversity_2(self):

        class FakeJob_vfaxfw:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_vfaxfw())

    def test_diversity_3(self):

        class FakeJob_kghhugo:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_kghhugo())

    def test_diversity_4(self):

        class FakeJob_cpzvm:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_cpzvm())

    def test_diversity_5(self):

        class FakeJob_fjwrgp:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_fjwrgp())

    def test_diversity_6(self):

        class FakeJob_jtrskk:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_jtrskk())

    def test_diversity_7(self):

        class FakeJob_rdhzcu:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_rdhzcu())

    def test_diversity_8(self):

        class FakeJob_uiailc:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_uiailc())

    def test_diversity_9(self):

        class FakeJob_xzbi:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_xzbi())

    def test_diversity_10(self):

        class FakeJob_jymi:

            def ssh(self):
                return None

            def jar(self):
                return None
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_jymi())

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):

        class FakeJob_gfei:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_gfei/gfei.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_gfei())

    def test_diversity_2(self):

        class FakeJob_xosrue:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_xosrue/xosrue.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_xosrue())

    def test_diversity_3(self):

        class FakeJob_bboye:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_bboye/bboye.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_bboye())

    def test_diversity_4(self):

        class FakeJob_cgswosqlu:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_cgswosqlu/cgswosqlu.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_cgswosqlu())

    def test_diversity_5(self):

        class FakeJob_qxutake:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_qxutake/qxutake.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_qxutake())

    def test_diversity_6(self):

        class FakeJob_zlwy:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_zlwy/zlwy.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_zlwy())

    def test_diversity_7(self):

        class FakeJob_fvbjww:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_fvbjww/fvbjww.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_fvbjww())

    def test_diversity_8(self):

        class FakeJob_dcgyptb:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_dcgyptb/dcgyptb.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_dcgyptb())

    def test_diversity_9(self):

        class FakeJob_clpylw:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_clpylw/clpylw.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_clpylw())

    def test_diversity_10(self):

        class FakeJob_abivfxqq:

            def ssh(self):
                return None

            def jar(self):
                return '/no/such/dir_abivfxqq/abivfxqq.jar'
        runner = HadoopJarJobRunner()
        self.assertRaises(HadoopJarJobError, runner.run_job, FakeJob_abivfxqq())
