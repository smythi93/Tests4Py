import unittest
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.ls_lah import match


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('ls -lah /sGzXFXZtleQhC', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('ls -lah /GFZElgNtlGcELai', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('pacman -s rLBHRuHR', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('pacman -s WArGColaH', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('ls -lah /hDdXTgPNIu', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('pacman -s gcbBMERgo', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('pacman -s xlbAsoRtPKRhZhC', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('ls -lah /VUSjpjL', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('ls -lah /TRVxodoKo', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('ls -lah /psaCbLg', '', ''), Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('ls /meWAsmJNnMxhG', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('ls wkyNbG.py', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('ls /rymAInKKiIZpUoy', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('ls /ZpvgvMdgeM', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('ls ZgcmTBx.py', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('ls SNUIjzCSbF.py', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('ls /MpdlqHKKKJHoQh', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('ls cstuWwjzf.py', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('ls uxUXMrez.py', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('ls hFsaymDLFNXKd.py', '', ''), Settings()))
