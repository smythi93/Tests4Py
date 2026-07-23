import unittest
from thefuck.rules.dnf_no_such_command import match, _parse_operations
from thefuck.types import Command

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):self.assertEqual(['group', 'help', 'repomanage', 'reposync'], _parse_operations('group    description\nhelp    description\nrepomanage    description\nreposync    description'))

    def test_diversity_2(self):self.assertEqual(['remove', 'makecache', 'copr', 'repomanage'], _parse_operations('remove    description\nmakecache    description\ncopr    description\nrepomanage    description'))

    def test_diversity_3(self):self.assertEqual(['check', 'history', 'config-manager', 'list', 'distro-sync'], _parse_operations('check    description\nhistory    description\nconfig-manager    description\nlist    description\ndistro-sync    description'))

    def test_diversity_4(self):self.assertEqual(['autoremove', 'downgrade', 'provides', 'repolist', 'makecache'], _parse_operations('autoremove    description\ndowngrade    description\nprovides    description\nrepolist    description\nmakecache    description'))

    def test_diversity_5(self):self.assertEqual(['install', 'deplist', 'swap', 'makecache'], _parse_operations('install    description\ndeplist    description\nswap    description\nmakecache    description'))

    def test_diversity_6(self):self.assertEqual(['reposync', 'check'], _parse_operations('reposync    description\ncheck    description'))

    def test_diversity_7(self):self.assertEqual(['help', 'downgrade'], _parse_operations('help    description\ndowngrade    description'))

    def test_diversity_8(self):self.assertEqual(['updateinfo', 'playground', 'distro-sync'], _parse_operations('updateinfo    description\nplayground    description\ndistro-sync    description'))

    def test_diversity_9(self):self.assertEqual(['mark', 'repograph', 'autoremove', 'config-manager', 'copr', 'help'], _parse_operations('mark    description\nrepograph    description\nautoremove    description\nconfig-manager    description\ncopr    description\nhelp    description'))

    def test_diversity_10(self):self.assertEqual(['makecache', 'check-update', 'autoremove'], _parse_operations('makecache    description\ncheck-update    description\nautoremove    description'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):self.assertEqual(True, match(Command('dnf copr mIDxMjTNwO', 'No such command: copr.')))

    def test_diversity_2(self):self.assertEqual(True, match(Command('dnf upgrade tUZoFJYUMAtsDDO', 'No such command: upgrade.')))

    def test_diversity_3(self):self.assertEqual(True, match(Command('dnf reinstall YXlGdGDSw', 'No such command: reinstall.')))

    def test_diversity_4(self):self.assertEqual(True, match(Command('dnf install jDyDbpWywuJ', 'No such command: install.')))

    def test_diversity_5(self):self.assertEqual(True, match(Command('dnf builddep dNZMdQHlETvqfh', 'No such command: builddep.')))

    def test_diversity_6(self):self.assertEqual(True, match(Command('dnf download jvxrd', 'No such command: download.')))

    def test_diversity_7(self):self.assertEqual(True, match(Command('dnf makecache WLVwc', 'No such command: makecache.')))

    def test_diversity_8(self):self.assertEqual(True, match(Command('dnf repolist MXuniVdFw', 'No such command: repolist.')))

    def test_diversity_9(self):self.assertEqual(True, match(Command('dnf download ktBYoyseWN', 'No such command: download.')))

    def test_diversity_10(self):self.assertEqual(True, match(Command('dnf download DKgwyljEbsee', 'No such command: download.')))
