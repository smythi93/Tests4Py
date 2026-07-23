import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('numeric', '279', '279', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_2(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'uyh', 'uyh', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_3(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 's', 's', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_4(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('numeric', '319', '319', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_5(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'wfnnp', 'wfnnp', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_6(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'dwkm', 'dwkm', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_7(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'xgvkg', 'xgvkg', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_8(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'zn', 'zn', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_9(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'i', 'i', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_10(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'sao', 'sao', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'onib', 'zefot', 'ge')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_2(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('numeric', '993', '138', 'ge')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(True, ops[op](left, right))

    def test_diversity_3(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'fyah', 't', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_4(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('numeric', '750', '698', 'ne')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(True, ops[op](left, right))

    def test_diversity_5(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('numeric', '486', '540', 'le')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(True, ops[op](left, right))

    def test_diversity_6(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('numeric', '785', '458', 'ne')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(True, ops[op](left, right))

    def test_diversity_7(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'rld', 'ugsxt', 'ne')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(True, ops[op](left, right))

    def test_diversity_8(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('numeric', '814', '981', 'eq')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_9(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'mt', 'q', 'gt')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(False, ops[op](left, right))

    def test_diversity_10(self):
        from ansible.utils.version import _Alpha, _Numeric
        ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, 'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, 'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}
        kind, a, b, op = ('alpha', 'pl', 'jcs', 'ge')
        if kind == 'numeric':
            left, right = (_Numeric(int(a)), _Numeric(int(b)))
        else:
            left, right = (_Alpha(a), _Alpha(b))
        self.assertEqual(True, ops[op](left, right))
