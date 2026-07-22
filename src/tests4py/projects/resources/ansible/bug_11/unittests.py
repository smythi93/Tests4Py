import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'evxvev')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  evxvev  \n@', actual)

    def test_diversity_2(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'pwkfe')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  pwkfe  \n@', actual)

    def test_diversity_3(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'ymnyv')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  ymnyv  \n@', actual)

    def test_diversity_4(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'iakm')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  iakm  \n@', actual)

    def test_diversity_5(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'awxnn')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  awxnn  \n@', actual)

    def test_diversity_6(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'jekzhg')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  jekzhg  \n@', actual)

    def test_diversity_7(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'cynx')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  cynx  \n@', actual)

    def test_diversity_8(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'mwxrh')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  mwxrh  \n@', actual)

    def test_diversity_9(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'xkqzze')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  xkqzze  \n@', actual)

    def test_diversity_10(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('pad', 'yzi')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\n  yzi  \n@', actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('nl', 'equrfp')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\nequrfp\n@', actual)

    def test_diversity_2(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('plain', 'eeb')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\neeb\n@', actual)

    def test_diversity_3(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('nl', 'dntu')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\ndntu\n@', actual)

    def test_diversity_4(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('plain', 'cjbxmg')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\ncjbxmg\n@', actual)

    def test_diversity_5(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('plain', 'dznw')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\ndznw\n@', actual)

    def test_diversity_6(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('plain', 'wiodl')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\nwiodl\n@', actual)

    def test_diversity_7(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('plain', 'aben')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\naben\n@', actual)

    def test_diversity_8(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('nl', 'warqw')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\nwarqw\n@', actual)

    def test_diversity_9(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('nl', 'ycuj')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\nycuj\n@', actual)

    def test_diversity_10(self):
        from types import SimpleNamespace
        from ansible.modules.network.ios.ios_banner import map_obj_to_commands
        mode, word = ('nl', 'acs')
        if mode == 'pad':
            text = '  ' + word + '  '
        elif mode == 'nl':
            text = chr(10) + word + chr(10)
        else:
            text = word
        module = SimpleNamespace(params={'state': 'present', 'banner': 'login'})
        cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)
        actual = cmds[0] if cmds else 'NONE'
        self.assertEqual('banner login @\nacs\n@', actual)
