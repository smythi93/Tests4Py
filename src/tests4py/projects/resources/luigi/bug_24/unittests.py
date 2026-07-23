import unittest
from luigi.contrib.spark import SparkSubmitTask


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--fkkwcgzh', {'zjydmz': 'itofeice'}), ['--fkkwcgzh', 'zjydmz=itofeice'])

    def test_diversity_2(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--wtxgfsx', {'lqtxwhp': 'wkaridx'}), ['--wtxgfsx', 'lqtxwhp=wkaridx'])

    def test_diversity_3(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--vfchyz', {'cdbll': 'tiyyxtbb'}), ['--vfchyz', 'cdbll=tiyyxtbb'])

    def test_diversity_4(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--lepgxc', {'zdaf': 'pxgtsz'}), ['--lepgxc', 'zdaf=pxgtsz'])

    def test_diversity_5(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--qljd', {'djz': 'mdqyja'}), ['--qljd', 'djz=mdqyja'])

    def test_diversity_6(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--gtme', {'kcvagt': 'vsfxcpde'}), ['--gtme', 'kcvagt=vsfxcpde'])

    def test_diversity_7(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--lcs', {'juadaqb': 'akt'}), ['--lcs', 'juadaqb=akt'])

    def test_diversity_8(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--jvz', {'qkb': 'pzusd'}), ['--jvz', 'qkb=pzusd'])

    def test_diversity_9(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--lufz', {'ubkgoj': 'jnmkjgu'}), ['--lufz', 'ubkgoj=jnmkjgu'])

    def test_diversity_10(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--pheqdpqz', {'broix': 'lspc'}), ['--pheqdpqz', 'broix=lspc'])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--cmpld', {}), [])

    def test_diversity_2(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--vkbbyio', {}), [])

    def test_diversity_3(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--sherrrg', {}), [])

    def test_diversity_4(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--lfs', {}), [])

    def test_diversity_5(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--edkjtli', {}), [])

    def test_diversity_6(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--pwjubma', {}), [])

    def test_diversity_7(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--ptumdl', {}), [])

    def test_diversity_8(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--wsm', {}), [])

    def test_diversity_9(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--xrbmvsxh', {}), [])

    def test_diversity_10(self):
        self.assertEqual(SparkSubmitTask._dict_arg(None, '--kdfabs', {}), [])
