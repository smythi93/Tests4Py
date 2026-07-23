import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', '4993c62e4a370de6d9042998372cdb0f', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '4993c62e4a370de6d9042998372cdb0f'], attach)

    def test_diversity_2(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', '8b469db26fa71c0bba75f51c5253b92a', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '8b469db26fa71c0bba75f51c5253b92a'], attach)

    def test_diversity_3(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', 'd269fe4d935bf0926a366faea801257f', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', 'd269fe4d935bf0926a366faea801257f'], attach)

    def test_diversity_4(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', '70969eb9f3b0cb2c1818b49144c35d10', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '70969eb9f3b0cb2c1818b49144c35d10'], attach)

    def test_diversity_5(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', '146bdb7cf88c4d53976b555581cee0a2', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '146bdb7cf88c4d53976b555581cee0a2'], attach)

    def test_diversity_6(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', 'badd8383927999eb9640559305f63289', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', 'badd8383927999eb9640559305f63289'], attach)

    def test_diversity_7(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', '01e7d40854cd6cdb983a279dd1a83b47', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '01e7d40854cd6cdb983a279dd1a83b47'], attach)

    def test_diversity_8(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', '96d14a176459059516de55100dbc6d64', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '96d14a176459059516de55100dbc6d64'], attach)

    def test_diversity_9(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', 'fc3531993cffcc2ff9bc126362c9fcc9', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', 'fc3531993cffcc2ff9bc126362c9fcc9'], attach)

    def test_diversity_10(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('noq', 'b31de827ad65bdc7795ad59106f89f54', None)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', 'b31de827ad65bdc7795ad59106f89f54'], attach)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', '0d06a7843355f2e3ffe0cc78cbf4d60a', 5)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '0d06a7843355f2e3ffe0cc78cbf4d60a', '--quantity', '5'], attach)

    def test_diversity_2(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', '4da6aead1886561b909ce99fd9c53b8b', 2)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '4da6aead1886561b909ce99fd9c53b8b', '--quantity', '2'], attach)

    def test_diversity_3(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', 'da79993c6eb7ca79e4c0ea6be5db85db', 8)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', 'da79993c6eb7ca79e4c0ea6be5db85db', '--quantity', '8'], attach)

    def test_diversity_4(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', '164815d6442e34f4b852b0d075bbca05', 3)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '164815d6442e34f4b852b0d075bbca05', '--quantity', '3'], attach)

    def test_diversity_5(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', 'fd31fd3ee0690197c451250b5d331da1', 5)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', 'fd31fd3ee0690197c451250b5d331da1', '--quantity', '5'], attach)

    def test_diversity_6(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', '101b4a7b3a736e4ae831372275aa95a5', 2)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '101b4a7b3a736e4ae831372275aa95a5', '--quantity', '2'], attach)

    def test_diversity_7(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', '74631a68c01dea03c7ec94931f4674a6', 9)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '74631a68c01dea03c7ec94931f4674a6', '--quantity', '9'], attach)

    def test_diversity_8(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', '64ba9f79689745aa47343bdf65743d30', 2)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '64ba9f79689745aa47343bdf65743d30', '--quantity', '2'], attach)

    def test_diversity_9(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', 'fb5271cd9a20f955bb43c99ab68b65ba', 9)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', 'fb5271cd9a20f955bb43c99ab68b65ba', '--quantity', '9'], attach)

    def test_diversity_10(self):
        import contextlib, io, json
        from unittest import mock
        from ansible.module_utils import basic
        from ansible.module_utils._text import to_bytes
        from ansible.modules.packaging.os import redhat_subscription
        mode, pool_id, quantity = ('withq', '60ad9fe81d0db0aac53d08cabc3a10f9', 4)
        basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'state': 'present', 'username': 'admin', 'password': 'admin', 'org_id': 'admin', 'pool_ids': [{pool_id: quantity}] if mode == 'withq' else [pool_id]}}))
        available = chr(10).join(['Subscription Name:   SP Server', 'Pool ID:             ' + pool_id, 'Available:           5', ''])
        calls = []
        def fake_run_command(args, *a, **kw):
            calls.append(args)
            joined = ' '.join(args) if isinstance(args, (list, tuple)) else args
            if 'identity' in joined:
                return (1, 'This system is not yet registered.', '')
            if 'list' in joined and '--available' in joined:
                return (0, available, '')
            return (0, '', '')
        with mock.patch.object(redhat_subscription.RegistrationBase, 'REDHAT_REPO', create=True), mock.patch.object(redhat_subscription, 'isfile', return_value=False), mock.patch.object(redhat_subscription, 'unlink', return_value=True), mock.patch.object(basic.AnsibleModule, 'get_bin_path', return_value='/testbin/subscription-manager'), mock.patch.object(basic.AnsibleModule, 'run_command', side_effect=fake_run_command):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    redhat_subscription.main()
            except SystemExit:
                pass
        attach = None
        for c in calls:
            if isinstance(c, (list, tuple)) and 'attach' in c and ('--pool' in c):
                attach = list(c)
                break
        self.assertEqual(['/testbin/subscription-manager', 'attach', '--pool', '60ad9fe81d0db0aac53d08cabc3a10f9', '--quantity', '4'], attach)
