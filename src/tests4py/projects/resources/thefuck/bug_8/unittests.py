import unittest
from thefuck.rules.dnf_no_such_command import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(False, match(Command('dnf list git', 'No such command')))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command("dnf upgrade '@Web Server'", 'No such command')))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('dnf downgrade gimp', 'No such command')))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('dnf install vlc', 'No such command')))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('dnf needs-restarting firefox', 'No such command')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('dnf downgrade tito', 'No such command')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('dnf debuginfo-install nginx', 'No such command')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('dnf repomanage git', 'No such command')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command("dnf help '@Web Server'", 'No such command')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('dnf repomanage tito', 'No such command')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(True, match(Command('dnf repooquery nano',
                                             'No such command: repooquery. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command repoquery" \n        ')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('dnf cheeck httpd',
                                             'No such command: cheeck. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command check" \n        ')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('dnf sheell git',
                                             'No such command: sheell. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command shell" \n        ')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('dnf upgrade-minimale vlc',
                                             'No such command: upgrade-minimale. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command upgrade-minimal" \n        ')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('dnf proovides nano',
                                             'No such command: proovides. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command provides" \n        ')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command("dnf maark '@docker'",
                                             'No such command: maark. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command mark" \n        ')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('dnf upgrade-minimale firefox',
                                             'No such command: upgrade-minimale. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command upgrade-minimal" \n        ')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('dnf cleean neofetch',
                                             'No such command: cleean. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command clean" \n        ')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('dnf instaall firefox',
                                             'No such command: instaall. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command install" \n        ')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('dnf upgrade-minimale httpd',
                                             'No such command: upgrade-minimale. Please use /usr/bin/dnf --help\n        It could be a DNF plugin command, try: dnf install "dnf-command upgrade-minimal" \n        ')))
