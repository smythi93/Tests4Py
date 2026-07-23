import unittest
import os
from thefuck.shells.fish import Fish

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzvoQdNQ,zzuHVM,zzCgssuh'
        self.assertIn('man', Fish()._get_overridden_aliases())

    def test_diversity_2(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzUclB,zzdCLIn'
        self.assertIn('open', Fish()._get_overridden_aliases())

    def test_diversity_3(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzWPJvI,zzSAakE'
        self.assertIn('cd', Fish()._get_overridden_aliases())

    def test_diversity_4(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzvFAKpSG,zzwgXw'
        self.assertIn('man', Fish()._get_overridden_aliases())

    def test_diversity_5(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzSVD,zzCYbt,zzPPUfr,zzyVhCbQ'
        self.assertIn('ls', Fish()._get_overridden_aliases())

    def test_diversity_6(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzTij,zznHwA'
        self.assertIn('man', Fish()._get_overridden_aliases())

    def test_diversity_7(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzSmIGD,zzIEKZna'
        self.assertIn('ls', Fish()._get_overridden_aliases())

    def test_diversity_8(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzdJNeU,zzbzIcw,zzjBMs,zzsDZ'
        self.assertIn('ls', Fish()._get_overridden_aliases())

    def test_diversity_9(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzcfd,zzQiSVXr,zzJIi'
        self.assertIn('ls', Fish()._get_overridden_aliases())

    def test_diversity_10(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzvXHS,zzpbd,zzIlmjhsu,zzfZCsXIc'
        self.assertIn('grep', Fish()._get_overridden_aliases())

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzNyZm,zzKZwGpqz,zzjbzcbpk'
        self.assertIn('zzKZwGpqz', Fish()._get_overridden_aliases())

    def test_diversity_2(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzVGTM,zzWLpx'
        self.assertIn('zzWLpx', Fish()._get_overridden_aliases())

    def test_diversity_3(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzKWc,zzDNVayK,zzkVh'
        self.assertIn('zzkVh', Fish()._get_overridden_aliases())

    def test_diversity_4(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzbpPw,zzYsXJuE,zzOUgJU,zzzqzGlI'
        self.assertIn('zzbpPw', Fish()._get_overridden_aliases())

    def test_diversity_5(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzipOPCFv,zzDjnqvoG,zzQnk,zzFAdWtE'
        self.assertIn('zzipOPCFv', Fish()._get_overridden_aliases())

    def test_diversity_6(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzquTjg,zzSpIMrr,zzddozuno,zzURmU'
        self.assertIn('zzURmU', Fish()._get_overridden_aliases())

    def test_diversity_7(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzwOccyEU,zzDudE,zzPilWEU'
        self.assertIn('zzDudE', Fish()._get_overridden_aliases())

    def test_diversity_8(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzDVoSyV,zzxGcGjfq'
        self.assertIn('zzDVoSyV', Fish()._get_overridden_aliases())

    def test_diversity_9(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzdlL,zzbZecwoD'
        self.assertIn('zzdlL', Fish()._get_overridden_aliases())

    def test_diversity_10(self):
        os.environ['TF_OVERRIDDEN_ALIASES'] = 'zzYxNE,zzmAKf'
        self.assertIn('zzmAKf', Fish()._get_overridden_aliases())
