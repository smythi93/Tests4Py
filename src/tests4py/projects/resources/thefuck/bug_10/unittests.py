import unittest
from thefuck.types import Command
from thefuck.rules.git_push import get_new_command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('man -s4 write', get_new_command(Command('man -s5 write', 'Output Message: NaYdiirEs', '')))

    def test_diversity_2(self):
        self.assertEqual(['read --help', 'man 5 read', 'man 4 read'], get_new_command(Command('man read', 'Output Message: pRAcoFwDDM', '')))

    def test_diversity_3(self):
        self.assertEqual(['read --help', 'man 5 read', 'man 4 read'], get_new_command(Command('man read', 'Output Message: qqlFCwwt', '')))

    def test_diversity_4(self):
        self.assertEqual('man 5 read', get_new_command(Command('man 4 read', 'Output Message: wfodG', '')))

    def test_diversity_5(self):
        self.assertEqual(['missing --help', 'man 5 missing', 'man 4 missing'],get_new_command(Command('man missing', 'Output Message: EjkNONDIvDpd', 'No manual entry for missing\n')))

    def test_diversity_6(self):
        self.assertEqual('man 4 read', get_new_command(Command('man 5 read', 'Output Message: FweuoUvJlUWsS', '')))

    def test_diversity_7(self):
        self.assertEqual(['read --help', 'man 5 read', 'man 4 read'], get_new_command(Command('man read', 'Output Message: EjpeKmKTzXYOeEK', '')))

    def test_diversity_8(self):
        self.assertEqual('man 4 read', get_new_command(Command('man 5 read', 'Output Message: lmbZwZe', '')))

    def test_diversity_9(self):
        self.assertEqual(['missing --help', 'man 5 missing', 'man 4 missing'], get_new_command(Command('man missing', 'Output Message: cVRVsecitAf', 'No manual entry for missing\n')))

    def test_diversity_10(self):
        self.assertEqual('man 4 read', get_new_command(Command('man 5 read', 'Output Message: IoEcQKViBKhm', '')))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('man -s2 read', get_new_command(Command('man -s3 read', 'Output Message: RskCrCzUeRMc', '')))

    def test_diversity_2(self):
        self.assertEqual('man -s 2 read', get_new_command(Command('man -s 3 read', 'Output Message: rRgvPU', '')))

    def test_diversity_3(self):
        self.assertEqual('man -s3 read', get_new_command(Command('man -s2 read', 'Output Message: PUaKdqDRFvndJ', '')))

    def test_diversity_4(self):
        self.assertEqual('man 2 read', get_new_command(Command('man 3 read', 'Output Message: MRnvIHUDX', '')))

    def test_diversity_5(self):
        self.assertEqual('man -s 3 read', get_new_command(Command('man -s 2 read', 'Output Message: kxqTeTeZCEhVXc', '')))

    def test_diversity_6(self):
        self.assertEqual('man 3 write', get_new_command(Command('man 2 write', 'Output Message: uRQBNIfmY', '')))

    def test_diversity_7(self):
        self.assertEqual('man 3 read', get_new_command(Command('man 2 read', 'Output Message: XRmzjoMJQuSg', '')))

    def test_diversity_8(self):
        self.assertEqual('man -s2 read', get_new_command(Command('man -s3 read', 'Output Message: TxeSHTFYCIadDW', '')))

    def test_diversity_9(self):
        self.assertEqual(['missing --help', 'man 3 missing', 'man 2 missing'], get_new_command(Command('man missing', 'Output Message: ZnaVcODmdpJYSs', 'No manual entry for missing\n')))

    def test_diversity_10(self):
        self.assertEqual('man -s 3 write', get_new_command(Command('man -s 2 write', 'Output Message: BPeJCFYPEulfcFE', '')))
