import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'octjq', 'bjojax')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/octjq bjojax', actual)

    def test_diversity_2(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'for', 'fioe')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/for fioe', actual)

    def test_diversity_3(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'xtmi', 'epoc')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/xtmi epoc', actual)

    def test_diversity_4(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'rdzxza', 'ccn')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/rdzxza ccn', actual)

    def test_diversity_5(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'vzvg', 'wcxmr')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/vzvg wcxmr', actual)

    def test_diversity_6(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'aiu', 'nylz')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/aiu nylz', actual)

    def test_diversity_7(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'snz', 'rodwgz')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/snz rodwgz', actual)

    def test_diversity_8(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'srcz', 'nhu')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/srcz nhu', actual)

    def test_diversity_9(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'ihodo', 'uzic')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/ihodo uzic', actual)

    def test_diversity_10(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('esc', 'ejn', 'mnns')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/ejn mnns', actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'rsx', 'avur')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/rsxavur', actual)

    def test_diversity_2(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'rwuwzy', 'ieaz')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/rwuwzyieaz', actual)

    def test_diversity_3(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'bbyd', 'tqbh')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/bbydtqbh', actual)

    def test_diversity_4(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'hwojqy', 'phvskq')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/hwojqyphvskq', actual)

    def test_diversity_5(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'uax', 'oxa')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/uaxoxa', actual)

    def test_diversity_6(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'kwwwb', 'kns')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/kwwwbkns', actual)

    def test_diversity_7(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'tzulm', 'ntfxpj')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/tzulmntfxpj', actual)

    def test_diversity_8(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'dxamht', 'oynze')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/dxamhtoynze', actual)

    def test_diversity_9(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'pgq', 'wch')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/pgqwch', actual)

    def test_diversity_10(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        mode, name1, name2 = ('plain', 'wsl', 'clx')
        if mode == 'esc':
            mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2
        else:
            mount_raw = '/mnt/' + name1 + name2
        entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]
        lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
        with mock.patch.object(linux.LinuxHardware, '_mtab_entries', return_value=entries), mock.patch.object(linux.LinuxHardware, '_find_bind_mounts', return_value=[]), mock.patch.object(linux.LinuxHardware, '_lsblk_uuid', return_value={}), mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', return_value=''):
            result = lh.get_mount_facts()
        mounts = result['mounts']
        actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'
        self.assertEqual('/mnt/wslclx', actual)
