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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vwPNzehTF')
            return _P(b'eemkrxwWhE')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vwPNzehTF', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vfpEUYWpgwOaYRA')
            return _P(b'eIhpokDoPAoGjO')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vfpEUYWpgwOaYRA', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vcEzcpzDi')
            return _P(b'ePveynCQt')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vcEzcpzDi', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vjgYSanQKA')
            return _P(b'ecgcoictiHKQDt')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vjgYSanQKA', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vXTSOHedwM')
            return _P(b'eJYoTOcVNaGeBoit')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vXTSOHedwM', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vVOLkAFewmWOUPq')
            return _P(b'ekGRqaF')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vVOLkAFewmWOUPq', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vrYXrRuiHRsmBzy')
            return _P(b'eYOYEkwgMmLypq')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vrYXrRuiHRsmBzy', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vBIgHSJWYEKRLm')
            return _P(b'eRWNBkTtZW')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vBIgHSJWYEKRLm', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vIIWkRJagQYNMg')
            return _P(b'eaumhrxRfne')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vIIWkRJagQYNMg', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version vNdRgBbk')
            return _P(b'emKeHEzm')
        _f.Popen = _fp
        self.assertEqual('Fish Shell vNdRgBbk', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version tDTcbLPjJOZvvI')
            return _P(b'tDTcbLPjJOZvvI')
        _f.Popen = _fp
        self.assertEqual('Fish Shell tDTcbLPjJOZvvI', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version JTNyaeOGZRCVE')
            return _P(b'JTNyaeOGZRCVE')
        _f.Popen = _fp
        self.assertEqual('Fish Shell JTNyaeOGZRCVE', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version VcNbOP')
            return _P(b'VcNbOP')
        _f.Popen = _fp
        self.assertEqual('Fish Shell VcNbOP', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version MLNYAhAZbVyLYed')
            return _P(b'MLNYAhAZbVyLYed')
        _f.Popen = _fp
        self.assertEqual('Fish Shell MLNYAhAZbVyLYed', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version JoCSHUXq')
            return _P(b'JoCSHUXq')
        _f.Popen = _fp
        self.assertEqual('Fish Shell JoCSHUXq', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version fXAIAzL')
            return _P(b'fXAIAzL')
        _f.Popen = _fp
        self.assertEqual('Fish Shell fXAIAzL', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version fGtSMis')
            return _P(b'fGtSMis')
        _f.Popen = _fp
        self.assertEqual('Fish Shell fGtSMis', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version ACWOIVGCcVmyHt')
            return _P(b'ACWOIVGCcVmyHt')
        _f.Popen = _fp
        self.assertEqual('Fish Shell ACWOIVGCcVmyHt', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version QFLdjTeLp')
            return _P(b'QFLdjTeLp')
        _f.Popen = _fp
        self.assertEqual('Fish Shell QFLdjTeLp', _f.Fish().info())

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

        def _fp(args, *a, **k):
            if '--version' in args:
                return _P(b'fish, version zbTgr')
            return _P(b'zbTgr')
        _f.Popen = _fp
        self.assertEqual('Fish Shell zbTgr', _f.Fish().info())
