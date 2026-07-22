import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['fsy', 'bic']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: bic, fsy', msg)

    def test_diversity_2(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['vbndes', 'byqh', 'nmki']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: byqh, nmki, vbndes', msg)

    def test_diversity_3(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['nx', 'waib', 'dkc', 'ylzeve']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: dkc, nx, waib, ylzeve', msg)

    def test_diversity_4(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['pkvo', 'mv']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: mv, pkvo', msg)

    def test_diversity_5(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['tb', 'gq', 'sdihpz']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: gq, sdihpz, tb', msg)

    def test_diversity_6(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['cptsbu', 'xacnxl', 'eh', 'ptfvwu']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: cptsbu, eh, ptfvwu, xacnxl', msg)

    def test_diversity_7(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['xxa', 'iiiob']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: iiiob, xxa', msg)

    def test_diversity_8(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['lh', 'flr']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: flr, lh', msg)

    def test_diversity_9(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['uys', 'ucy']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: ucy, uys', msg)

    def test_diversity_10(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['qloox', 'olu']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: olu, qloox', msg)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['gnen', 'rtpe', 'uvtq']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: gnen, rtpe, uvtq', msg)

    def test_diversity_2(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['nzlxt', 'xdxd', 'yf']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: nzlxt, xdxd, yf', msg)

    def test_diversity_3(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['ca', 'ebeluk', 'ldmapk', 'rxqyz']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: ca, ebeluk, ldmapk, rxqyz', msg)

    def test_diversity_4(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['ero', 'scpo', 'ta']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: ero, scpo, ta', msg)

    def test_diversity_5(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['zfyqnd', 'zts']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: zfyqnd, zts', msg)

    def test_diversity_6(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['aije', 'jg']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: aije, jg', msg)

    def test_diversity_7(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['fzwvt', 'tlruo']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: fzwvt, tlruo', msg)

    def test_diversity_8(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['lmdtqo', 'owdu', 'uuym', 'vpnv']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: lmdtqo, owdu, uuym, vpnv', msg)

    def test_diversity_9(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['ch', 'fjny', 'lzbw']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: ch, fjny, lzbw', msg)

    def test_diversity_10(self):
        from collections import OrderedDict
        from ansible.module_utils.common.validation import check_required_arguments
        from ansible.module_utils._text import to_native
        names = ['jn', 'zn']
        spec = OrderedDict(((n, {'required': True}) for n in names))
        try:
            check_required_arguments(spec, {})
            msg = 'NO_ERROR'
        except TypeError as e:
            msg = to_native(e)
        self.assertEqual('missing required arguments: jn, zn', msg)
