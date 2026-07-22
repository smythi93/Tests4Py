import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2066.1')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_2(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2036.5')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_3(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2044.5')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_4(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2058.5')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_5(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2018.4')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_6(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2010.1')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_7(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2020.0')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_8(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2096.5')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_9(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2053.0')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_10(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'os', '2034.5')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('ubuntu', 'lsb', '2018.1')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Ubuntu', result)

    def test_diversity_2(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'lsb', '2077.5')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_3(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('ubuntu', 'os', '2072.7')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Ubuntu', result)

    def test_diversity_4(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('steamos', 'os', '2022.8')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True SteamOS', result)

    def test_diversity_5(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('steamos', 'os', '2031.4')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True SteamOS', result)

    def test_diversity_6(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'lsb', '2003.6')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_7(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('ubuntu', 'lsb', '2045.3')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Ubuntu', result)

    def test_diversity_8(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('ubuntu', 'os', '2003.5')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Ubuntu', result)

    def test_diversity_9(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'lsb', '2010.8')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)

    def test_diversity_10(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        distro, path_kind, version = ('kali', 'lsb', '2018.1')
        if distro == 'kali':
            data = 'NAME="Kali GNU/Linux Rolling" VERSION="' + version + '"'
        elif distro == 'ubuntu':
            data = 'NAME="Ubuntu" VERSION="' + version + '"'
        else:
            data = 'NAME="SteamOS" VERSION="' + version + '"'
        path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'
        df = DistributionFiles(module=None)
        matched, facts = df.parse_distribution_file_Debian(distro, data, path, {'distribution_release': 'NA'})
        result = '%s %s' % (matched, facts.get('distribution'))
        self.assertEqual('True Kali', result)
