import unittest
from thefuck.types import Command
from thefuck.rules.man import get_new_command

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):self.assertEqual('man 5 write', get_new_command(Command('man 4 write', 'Output Message: aZwUGwrnFHl', '')))

    def test_diversity_2(self):self.assertEqual(['read --help', 'man 5 read', 'man 4 read'], get_new_command(Command('man read', 'Output Message: ITvbETMwe', '')))

    def test_diversity_3(self):self.assertEqual('man -s 4 read', get_new_command(Command('man -s 5 read', 'Output Message: mJzWYOZcHWcn', '')))

    def test_diversity_4(self):self.assertEqual('man -s 5 write', get_new_command(Command('man -s 4 write', 'Output Message: eBCXVsOzmsgyIkl', '')))

    def test_diversity_5(self):self.assertEqual(['read --help', 'man 5 read', 'man 4 read'], get_new_command(Command('man read', 'Output Message: ofrrzrdWqnVB', '')))

    def test_diversity_6(self):self.assertEqual('man 4 write', get_new_command(Command('man 5 write', 'Output Message: MieDOf', '')))

    def test_diversity_7(self):self.assertEqual('man -s 5 read', get_new_command(Command('man -s 4 read', 'Output Message: xyxUNqNRCctqqs', '')))

    def test_diversity_8(self):self.assertEqual('man -s 5 write', get_new_command(Command('man -s 4 write', 'Output Message: bdQTlLv', '')))

    def test_diversity_9(self):self.assertEqual('man 4 read', get_new_command(Command('man 5 read', 'Output Message: zoipUQuYYi', '')))

    def test_diversity_10(self):self.assertEqual('man -s 5 read', get_new_command(Command('man -s 4 read', 'Output Message: BuQBeBmNboFn', '')))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):self.assertEqual('man 2 read', get_new_command(Command('man 3 read', 'Output Message: NPkKQraBz', '')))

    def test_diversity_2(self):self.assertEqual('man -s 2 read', get_new_command(Command('man -s 3 read', 'Output Message: dBORRHTk', '')))

    def test_diversity_3(self):self.assertEqual('man -s 2 write', get_new_command(Command('man -s 3 write', 'Output Message: TdpAD', '')))

    def test_diversity_4(self):self.assertEqual('man 2 read', get_new_command(Command('man 3 read', 'Output Message: hefNYp', '')))

    def test_diversity_5(self):self.assertEqual('man -s2 read', get_new_command(Command('man -s3 read', 'Output Message: MqRToLOO', '')))

    def test_diversity_6(self):self.assertEqual('man -s 3 read', get_new_command(Command('man -s 2 read', 'Output Message: oIfOLzvVkvYA', '')))

    def test_diversity_7(self):self.assertEqual('man 2 read', get_new_command(Command('man 3 read', 'Output Message: qGhEuBtHc', '')))

    def test_diversity_8(self):self.assertEqual('man 2 read', get_new_command(Command('man 3 read', 'Output Message: HhlnP', '')))

    def test_diversity_9(self):self.assertEqual('man -s3 read', get_new_command(Command('man -s2 read', 'Output Message: HknDHa', '')))

    def test_diversity_10(self):self.assertEqual('man -s 2 write', get_new_command(Command('man -s 3 write', 'Output Message: mfALlwHbWhPiWn', '')))