import unittest
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.vagrant_up import get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(
            ['vagrant up devbox  && vagrant QMsLOtlmKw devbox', 'vagrant up  && vagrant QMsLOtlmKw devbox'],
            get_new_command(Command('vagrant QMsLOtlmKw devbox', '',
                                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                            Settings()))

    def test_diversity_2(self):
        self.assertEqual(
            ['vagrant up devbox  && vagrant rncAYcExnyxW devbox', 'vagrant up  && vagrant rncAYcExnyxW devbox'],
            get_new_command(Command('vagrant rncAYcExnyxW devbox', '',
                                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                            Settings()))

    def test_diversity_3(self):
        self.assertEqual(['vagrant up devbox  && vagrant sekhpj devbox', 'vagrant up  && vagrant sekhpj devbox'],
                         get_new_command(Command('vagrant sekhpj devbox', '',
                                                 'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                         Settings()))

    def test_diversity_4(self):
        self.assertEqual(['vagrant up devbox  && vagrant YAarzH devbox', 'vagrant up  && vagrant YAarzH devbox'],
                         get_new_command(Command('vagrant YAarzH devbox', '',
                                                 'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                         Settings()))

    def test_diversity_5(self):
        self.assertEqual(
            ['vagrant up devbox  && vagrant rVYvfYqswhRuEOK devbox', 'vagrant up  && vagrant rVYvfYqswhRuEOK devbox'],
            get_new_command(Command('vagrant rVYvfYqswhRuEOK devbox', '',
                                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                            Settings()))

    def test_diversity_6(self):
        self.assertEqual(
            ['vagrant up devbox  && vagrant qQWhblpxdBII devbox', 'vagrant up  && vagrant qQWhblpxdBII devbox'],
            get_new_command(Command('vagrant qQWhblpxdBII devbox', '',
                                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                            Settings()))

    def test_diversity_7(self):
        self.assertEqual(['vagrant up devbox  && vagrant nvTaSPv devbox', 'vagrant up  && vagrant nvTaSPv devbox'],
                         get_new_command(Command('vagrant nvTaSPv devbox', '',
                                                 'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                         Settings()))

    def test_diversity_8(self):
        self.assertEqual(
            ['vagrant up devbox  && vagrant EmQSMmleoch devbox', 'vagrant up  && vagrant EmQSMmleoch devbox'],
            get_new_command(Command('vagrant EmQSMmleoch devbox', '',
                                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                            Settings()))

    def test_diversity_9(self):
        self.assertEqual(['vagrant up devbox  && vagrant lbCSiUSt devbox', 'vagrant up  && vagrant lbCSiUSt devbox'],
                         get_new_command(Command('vagrant lbCSiUSt devbox', '',
                                                 'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                         Settings()))

    def test_diversity_10(self):
        self.assertEqual(
            ['vagrant up devbox  && vagrant tFsJwIsAaLbc devbox', 'vagrant up  && vagrant tFsJwIsAaLbc devbox'],
            get_new_command(Command('vagrant tFsJwIsAaLbc devbox', '',
                                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                            Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('vagrant up devbox && vagrant HAwcDCD devbox', get_new_command(
            Command('vagrant HAwcDCD devbox', '',
                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
            Settings()))

    def test_diversity_2(self):
        self.assertEqual('vagrant up devbox && vagrant lspZj devbox', get_new_command(
            Command('vagrant lspZj devbox', '',
                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
            Settings()))

    def test_diversity_3(self):
        self.assertEqual('vagrant up  && vagrant oRmBnDNcIi', get_new_command(Command('vagrant oRmBnDNcIi', '',
                                                                                      'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                                                              Settings()))

    def test_diversity_4(self):
        self.assertEqual('vagrant up devbox && vagrant NApcfPr devbox', get_new_command(
            Command('vagrant NApcfPr devbox', '',
                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
            Settings()))

    def test_diversity_5(self):
        self.assertEqual('vagrant up  && vagrant YSHVecsyJWw', get_new_command(Command('vagrant YSHVecsyJWw', '',
                                                                                       'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                                                               Settings()))

    def test_diversity_6(self):
        self.assertEqual('vagrant up  && vagrant muNIu', get_new_command(Command('vagrant muNIu', '',
                                                                                 'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                                                         Settings()))

    def test_diversity_7(self):
        self.assertEqual('vagrant up devbox && vagrant BdCLlRoOSjCgIK devbox', get_new_command(
            Command('vagrant BdCLlRoOSjCgIK devbox', '',
                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
            Settings()))

    def test_diversity_8(self):
        self.assertEqual('vagrant up devbox && vagrant nlvmrhEMYNLFDV devbox', get_new_command(
            Command('vagrant nlvmrhEMYNLFDV devbox', '',
                    'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
            Settings()))

    def test_diversity_9(self):
        self.assertEqual('vagrant up  && vagrant cHaBPJvxmjnCoI', get_new_command(Command('vagrant cHaBPJvxmjnCoI', '',
                                                                                          'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                                                                  Settings()))

    def test_diversity_10(self):
        self.assertEqual('vagrant up  && vagrant EejNROForqOs', get_new_command(Command('vagrant EejNROForqOs', '',
                                                                                        'VM must be running to open SSH connection. Run `vagrant up`\nto start the virtual machine.'),
                                                                                Settings()))
