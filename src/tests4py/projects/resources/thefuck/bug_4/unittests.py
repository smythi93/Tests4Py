import unittest

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias OjKLZh=PyTQgUKEBa')
        self.assertEqual({'OjKLZh': 'PyTQgUKEBa'}, _f._get_aliases(set()))

    def test_diversity_2(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias mAKDHDihKwM=voWwPKFBcuWGGS')
        self.assertEqual({'mAKDHDihKwM': 'voWwPKFBcuWGGS'}, _f._get_aliases(set()))

    def test_diversity_3(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias rAAypWIenMpOG=UgyHfneuYJc')
        self.assertEqual({'rAAypWIenMpOG': 'UgyHfneuYJc'}, _f._get_aliases(set()))

    def test_diversity_4(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias KmskZQVKq=OxEBQAgXGii')
        self.assertEqual({'KmskZQVKq': 'OxEBQAgXGii'}, _f._get_aliases(set()))

    def test_diversity_5(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias VsOwLyX=HsPxtrescRB')
        self.assertEqual({'VsOwLyX': 'HsPxtrescRB'}, _f._get_aliases(set()))

    def test_diversity_6(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias AkZcTVKwPD=kZlqTNKbilwo')
        self.assertEqual({'AkZcTVKwPD': 'kZlqTNKbilwo'}, _f._get_aliases(set()))

    def test_diversity_7(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias IbavlAbVAXNbLw=EFyvMMsqGWSJxrA')
        self.assertEqual({'IbavlAbVAXNbLw': 'EFyvMMsqGWSJxrA'}, _f._get_aliases(set()))

    def test_diversity_8(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias XuvQOJTHuop=CdfUdtDA')
        self.assertEqual({'XuvQOJTHuop': 'CdfUdtDA'}, _f._get_aliases(set()))

    def test_diversity_9(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias jFZdRnwi=bVmGQqyyTpHxb')
        self.assertEqual({'jFZdRnwi': 'bVmGQqyyTpHxb'}, _f._get_aliases(set()))

    def test_diversity_10(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias QjqxccFuw=PckWRsVjxfcD')
        self.assertEqual({'QjqxccFuw': 'PckWRsVjxfcD'}, _f._get_aliases(set()))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias ssflxodfXN pSfXqGtDAyfDi')
        self.assertEqual({'ssflxodfXN': 'pSfXqGtDAyfDi'}, _f._get_aliases(set()))

    def test_diversity_2(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias AsZoGzqTIsk EfapccPaN')
        self.assertEqual({'AsZoGzqTIsk': 'EfapccPaN'}, _f._get_aliases(set()))

    def test_diversity_3(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias fQSgIyoGmRlJ JXJIz')
        self.assertEqual({'fQSgIyoGmRlJ': 'JXJIz'}, _f._get_aliases(set()))

    def test_diversity_4(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias ENsbQriRZbg uFSzYewhUd')
        self.assertEqual({'ENsbQriRZbg': 'uFSzYewhUd'}, _f._get_aliases(set()))

    def test_diversity_5(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias tasQzfgSCu sVDoWfUU')
        self.assertEqual({'tasQzfgSCu': 'sVDoWfUU'}, _f._get_aliases(set()))

    def test_diversity_6(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias tciOdlmbtW mmdjiwPmWlCu')
        self.assertEqual({'tciOdlmbtW': 'mmdjiwPmWlCu'}, _f._get_aliases(set()))

    def test_diversity_7(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias CpvxCFaAh WmMbKFynwIR')
        self.assertEqual({'CpvxCFaAh': 'WmMbKFynwIR'}, _f._get_aliases(set()))

    def test_diversity_8(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias ipjIUgzjnxfhlAp sCdNEYsYveM')
        self.assertEqual({'ipjIUgzjnxfhlAp': 'sCdNEYsYveM'}, _f._get_aliases(set()))

    def test_diversity_9(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias kljaX MSwRGurRhoFNrUz')
        self.assertEqual({'kljaX': 'MSwRGurRhoFNrUz'}, _f._get_aliases(set()))

    def test_diversity_10(self):
        import io
        import thefuck.shells.fish as _f
        from thefuck.utils import cache as _cache, memoize as _memoize
        _cache.disabled = True
        _memoize.disabled = True

        class _P:

            def __init__(self, d):
                self.stdout = io.BytesIO(d)

            def wait(self, *a, **k):
                return 0
        _f.Popen = lambda *a, **k: _P(b'alias PhzhsUDwDeUBwM BfkyBBYta')
        self.assertEqual({'PhzhsUDwDeUBwM': 'BfkyBBYta'}, _f._get_aliases(set()))
