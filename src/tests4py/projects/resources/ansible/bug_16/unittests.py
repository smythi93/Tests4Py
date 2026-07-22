import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc64', 4)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_2(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc64', 5)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_3(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc64le', 6)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_4(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc64le', 8)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_5(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc', 8)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_6(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc64le', 4)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_7(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc64', 6)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_8(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc', 7)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_9(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc', 4)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_10(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('ppc64le', 2)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('i386', 5)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_2(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('x86_64', 4)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_3(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('amd64', 4)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_4(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('x86_64', 3)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_5(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('i386', 7)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_6(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('x86_64', 6)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_7(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('x86_64', 2)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_8(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('x86_64', 7)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_9(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('i386', 6)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))

    def test_diversity_10(self):
        from unittest import mock
        from ansible.module_utils.facts.hardware import linux
        arch, n = ('x86_64', 8)
        lines = []
        if arch.startswith(('ppc', 'powerpc')):
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('cpu : POWER8 (architected), altivec supported')
            lines.append('timebase : 512000000')
        else:
            for k in range(n):
                lines.append('processor : %d' % k)
                lines.append('vendor_id : GenuineIntel')
                lines.append('model name : Intel(R) Xeon(R) CPU')
        inst = linux.LinuxHardware(mock.Mock())
        with mock.patch('os.path.exists', return_value=False), mock.patch('os.access', return_value=True), mock.patch('ansible.module_utils.facts.hardware.linux.get_file_lines', side_effect=[[], lines]):
            facts = inst.get_cpu_facts(collected_facts={'ansible_architecture': arch})
        self.assertEqual(n, facts.get('processor_count'))
