import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'xcz', 'acex')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_2(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'mvf', 'ylbqdh')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_3(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'fxfiswz', 'vksnu')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_4(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'rqvlc', 'ctyum')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_5(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'qygdi', 'gqh')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_6(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'sxoa', 'emh')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_7(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'aqd', 'dea')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_8(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'dhdqpux', 'rks')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_9(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'dcc', 'qtx')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_10(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('patch', 'rggpp', 'djpbil')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'amhsaco', 'qotw')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_2(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'whoaqpu', 'rjiyla')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_3(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'kzfirfw', 'kxpr')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_4(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'wtqhc', 'zygz')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_5(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'typvqkb', 'odvawh')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_6(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'fkr', 'qce')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_7(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'srnd', 'xzniqtc')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_8(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'mhs', 'cwn')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_9(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'dgbkkx', 'qbmssau')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)

    def test_diversity_10(self):
        import os
        from unittest import mock
        import ansible.utils.py3compat as py3compat
        from ansible.plugins.loader import lookup_loader
        mode, var, value = ('real', 'idzqmzp', 'ypgxgf')
        env_lookup = lookup_loader.get('env')
        if mode == 'patch':
            os.environ.pop(var, None)
            with mock.patch.object(py3compat.environ, 'get', lambda x, y=None: value):
                retval = env_lookup.run([var], None)
        else:
            os.environ[var] = value
            retval = env_lookup.run([var], None)
        actual = retval[0] if retval else 'EMPTY'
        self.assertEqual(value, actual)
