import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('stopped', 'xbq', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|shutdown|vrf xbq|shutdown', '|'.join(commands))

    def test_diversity_2(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('started', 'salkts', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|no shutdown|vrf salkts|no shutdown', '|'.join(commands))

    def test_diversity_3(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('stopped', 'rthpi', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|shutdown|vrf rthpi|shutdown', '|'.join(commands))

    def test_diversity_4(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('stopped', 'dezey', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|shutdown|vrf dezey|shutdown', '|'.join(commands))

    def test_diversity_5(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('started', 'aoift', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|no shutdown|vrf aoift|no shutdown', '|'.join(commands))

    def test_diversity_6(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('stopped', 'dlbxa', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|shutdown|vrf dlbxa|shutdown', '|'.join(commands))

    def test_diversity_7(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('stopped', 'yqa', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|shutdown|vrf yqa|shutdown', '|'.join(commands))

    def test_diversity_8(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('started', 'lapm', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|no shutdown|vrf lapm|no shutdown', '|'.join(commands))

    def test_diversity_9(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('stopped', 'jrxzil', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|shutdown|vrf jrxzil|shutdown', '|'.join(commands))

    def test_diversity_10(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('started', 'ozn', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|no shutdown|vrf ozn|no shutdown', '|'.join(commands))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'qrlm', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf qrlm', '|'.join(commands))

    def test_diversity_2(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('stopped', 'none', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|shutdown', '|'.join(commands))

    def test_diversity_3(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'hrxq', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf hrxq', '|'.join(commands))

    def test_diversity_4(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'imwps', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf imwps', '|'.join(commands))

    def test_diversity_5(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'wgb', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf wgb', '|'.join(commands))

    def test_diversity_6(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'sfv', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf sfv', '|'.join(commands))

    def test_diversity_7(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('started', 'none', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|no shutdown', '|'.join(commands))

    def test_diversity_8(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'gwd', 'started', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf gwd', '|'.join(commands))

    def test_diversity_9(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'gmhm', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf gmhm', '|'.join(commands))

    def test_diversity_10(self):
        from ansible.modules.network.eos.eos_eapi import map_obj_to_commands
        keys = ['http', 'http_port', 'https', 'https_port', 'local_http', 'local_http_port', 'socket']
        ws, wv, hs, hv = ('none', 'wkl', 'stopped', 'none')
        def val(x):
            return None if x == 'none' else x
        want = {k: None for k in keys}
        want['state'], want['vrf'] = (val(ws), val(wv))
        have = {k: None for k in keys}
        have['state'], have['vrf'] = (val(hs), val(hv))
        commands = map_obj_to_commands((want, have), None, [])
        self.assertEqual('management api http-commands|vrf wkl', '|'.join(commands))
