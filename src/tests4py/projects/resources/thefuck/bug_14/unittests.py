import unittest
from thefuck.shells.fish import Fish

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _marker = 'h1lR7xHpfrfN'
        f = Fish()
        self.assertIn('zzQYOzG', f._get_overridden_aliases())

    def test_diversity_2(self):
        _marker = 'jtQVnonW6e7k'
        f = Fish()
        self.assertIn('zzNFy', f._get_overridden_aliases())

    def test_diversity_3(self):
        _marker = 'VsUJdo8IQRlT'
        f = Fish()
        self.assertIn('zzducCi', f._get_overridden_aliases())

    def test_diversity_4(self):
        _marker = 'oqco6eCfOJMn'
        f = Fish()
        self.assertIn('zzAaYRl', f._get_overridden_aliases())

    def test_diversity_5(self):
        _marker = 'fKKnEUKXSWZb'
        f = Fish()
        self.assertIn('zzHYs', f._get_overridden_aliases())

    def test_diversity_6(self):
        _marker = 'C57hV3ACo5t3'
        f = Fish()
        self.assertIn('zzHRmZv', f._get_overridden_aliases())

    def test_diversity_7(self):
        _marker = 'rPHnCjWCy3Pg'
        f = Fish()
        self.assertIn('zzVCDSPXK', f._get_overridden_aliases())

    def test_diversity_8(self):
        _marker = 'GBBkEuwYfaEI'
        f = Fish()
        self.assertIn('zzWewcjODb', f._get_overridden_aliases())

    def test_diversity_9(self):
        _marker = 'K4iwxwJK1gHO'
        f = Fish()
        self.assertIn('zzKgW', f._get_overridden_aliases())

    def test_diversity_10(self):
        _marker = 'm4lbzv4NGIkB'
        f = Fish()
        self.assertIn('zzucRq', f._get_overridden_aliases())

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _marker = 'mhn6ktlnFcqU'
        f = Fish()
        self.assertIn('grep', f._get_overridden_aliases())

    def test_diversity_2(self):
        _marker = 'vT19ZpxFBIsV'
        f = Fish()
        self.assertIn('ls', f._get_overridden_aliases())

    def test_diversity_3(self):
        _marker = 'UFJlJKHK7pSS'
        f = Fish()
        self.assertIn('ls', f._get_overridden_aliases())

    def test_diversity_4(self):
        _marker = 'BLOd5ex7PONf'
        f = Fish()
        self.assertIn('cd', f._get_overridden_aliases())

    def test_diversity_5(self):
        _marker = 'oROfSeFzwNSe'
        f = Fish()
        self.assertIn('man', f._get_overridden_aliases())

    def test_diversity_6(self):
        _marker = 'eFWtYTFOJgUX'
        f = Fish()
        self.assertIn('open', f._get_overridden_aliases())

    def test_diversity_7(self):
        _marker = 'E6aTYP7omFBB'
        f = Fish()
        self.assertIn('grep', f._get_overridden_aliases())

    def test_diversity_8(self):
        _marker = '9ksVphKfYc5u'
        f = Fish()
        self.assertIn('cd', f._get_overridden_aliases())

    def test_diversity_9(self):
        _marker = 'J9JJewpYMBIq'
        f = Fish()
        self.assertIn('ls', f._get_overridden_aliases())

    def test_diversity_10(self):
        _marker = 'N5pm8jj80MVM'
        f = Fish()
        self.assertIn('man', f._get_overridden_aliases())