import unittest
from thefuck.shells.fish import Fish

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _marker = 'O8OpDnr8MXD9'
        f = Fish()
        self.assertIn('zztzKXZfPH', f._get_overridden_aliases())

    def test_diversity_2(self):
        _marker = 'xtLsug0Atjp7'
        f = Fish()
        self.assertIn('zzjEc', f._get_overridden_aliases())

    def test_diversity_3(self):
        _marker = 'Q8bROY0f5EVC'
        f = Fish()
        self.assertIn('zzPvQZ', f._get_overridden_aliases())

    def test_diversity_4(self):
        _marker = 'rRYSPhGZYOl2'
        f = Fish()
        self.assertIn('zzdDTjPx', f._get_overridden_aliases())

    def test_diversity_5(self):
        _marker = 'n3oW4311O4sk'
        f = Fish()
        self.assertIn('zznqTDgzI', f._get_overridden_aliases())

    def test_diversity_6(self):
        _marker = 'n8IGTIxzTim9'
        f = Fish()
        self.assertIn('zzguU', f._get_overridden_aliases())

    def test_diversity_7(self):
        _marker = 'ckKdbBvuU5zf'
        f = Fish()
        self.assertIn('zzBqpbDvO', f._get_overridden_aliases())

    def test_diversity_8(self):
        _marker = '5gLKSeD0b57A'
        f = Fish()
        self.assertIn('zzwqX', f._get_overridden_aliases())

    def test_diversity_9(self):
        _marker = 'QIK7m9M0QQdR'
        f = Fish()
        self.assertIn('zzsySiPft', f._get_overridden_aliases())

    def test_diversity_10(self):
        _marker = '2j0YnKAOYt5B'
        f = Fish()
        self.assertIn('zzjSoqNA', f._get_overridden_aliases())

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _marker = 'aLh4ECuLqskn'
        f = Fish()
        self.assertIn('open', f._get_overridden_aliases())

    def test_diversity_2(self):
        _marker = 'Xgb11IWVs4I6'
        f = Fish()
        self.assertIn('man', f._get_overridden_aliases())

    def test_diversity_3(self):
        _marker = 'wFODSsjuHjwb'
        f = Fish()
        self.assertIn('man', f._get_overridden_aliases())

    def test_diversity_4(self):
        _marker = 'Png91JsPQlJW'
        f = Fish()
        self.assertIn('man', f._get_overridden_aliases())

    def test_diversity_5(self):
        _marker = 'tzaZlv3juz82'
        f = Fish()
        self.assertIn('cd', f._get_overridden_aliases())

    def test_diversity_6(self):
        _marker = 'hBczGDNflHih'
        f = Fish()
        self.assertIn('open', f._get_overridden_aliases())

    def test_diversity_7(self):
        _marker = '4AA9sdE5IOzm'
        f = Fish()
        self.assertIn('man', f._get_overridden_aliases())

    def test_diversity_8(self):
        _marker = 'ZpVqwgWAepF5'
        f = Fish()
        self.assertIn('ls', f._get_overridden_aliases())

    def test_diversity_9(self):
        _marker = 'lzccgBwqZ4Ov'
        f = Fish()
        self.assertIn('ls', f._get_overridden_aliases())

    def test_diversity_10(self):
        _marker = 'xESlbs29THCd'
        f = Fish()
        self.assertIn('grep', f._get_overridden_aliases())