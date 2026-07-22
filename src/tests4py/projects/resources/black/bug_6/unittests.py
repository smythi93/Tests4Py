import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        mode = black.FileMode(target_versions={black.TargetVersion.PY37})
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertRaises(Exception, self.run_black, 'async = lambda: 720\nasync()\n')

    def test_diversity_2(self):
        self.assertRaises(Exception, self.run_black, 'def async():\n    hious = 754\n    return hious\n')

    def test_diversity_3(self):
        self.assertRaises(Exception, self.run_black, 'await = 343\nawait()\n')

    def test_diversity_4(self):
        self.assertRaises(Exception, self.run_black, 'def nez():\n    await = 952\n    return await\n')

    def test_diversity_5(self):
        self.assertRaises(Exception, self.run_black, 'def await():\n    jrqbgxi = 457\n    return jrqbgxi\n')

    def test_diversity_6(self):
        self.assertRaises(Exception, self.run_black, 'def uhnjtaya():\n    async = 442\n    return async\n')

    def test_diversity_7(self):
        self.assertRaises(Exception, self.run_black, 'def iwhdcfvq():\n    await = 733\n    return await\n')

    def test_diversity_8(self):
        self.assertRaises(Exception, self.run_black, 'await = lambda: 825\nawait()\n')

    def test_diversity_9(self):
        self.assertRaises(Exception, self.run_black, 'def async():\n    osxugpm = 137\n    return osxugpm\n')

    def test_diversity_10(self):
        self.assertRaises(Exception, self.run_black, 'await = 860\nawait()\n')

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        mode = black.FileMode(target_versions={black.TargetVersion.PY37})
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertEqual('async def wsc():\n    await wgphs()\n', self.run_black('async def wsc():\n    await wgphs()\n'))

    def test_diversity_2(self):
        self.assertEqual('async def ozwr():\n    await rmf()\n', self.run_black('async def ozwr():\n    await rmf()\n'))

    def test_diversity_3(self):
        self.assertEqual('mbbki = 3\n', self.run_black('mbbki = 3\n'))

    def test_diversity_4(self):
        self.assertEqual('pkbq = 9\n', self.run_black('pkbq = 9\n'))

    def test_diversity_5(self):
        self.assertEqual('kaor = 3\n', self.run_black('kaor = 3\n'))

    def test_diversity_6(self):
        self.assertEqual('async def zntdmza():\n    await uwgaii()\n', self.run_black('async def zntdmza():\n    await uwgaii()\n'))

    def test_diversity_7(self):
        self.assertEqual('def norzfmjb(mstsdw):\n    return 2\n', self.run_black('def norzfmjb(mstsdw):\n    return 2\n'))

    def test_diversity_8(self):
        self.assertEqual('async def wmvhw():\n    await onri()\n', self.run_black('async def wmvhw():\n    await onri()\n'))

    def test_diversity_9(self):
        self.assertEqual('cjw = 1\n', self.run_black('cjw = 1\n'))

    def test_diversity_10(self):
        self.assertEqual('kphryyd = 0\n', self.run_black('kphryyd = 0\n'))
