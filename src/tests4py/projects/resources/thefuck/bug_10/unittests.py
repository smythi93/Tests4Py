import unittest
from thefuck.types import Command
from thefuck.rules.man import get_new_command

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(1, len(get_new_command(Command('man dYWIb', '', 'No manual entry for dYWIb'))))

    def test_diversity_2(self):
        self.assertEqual(1, len(get_new_command(Command('man ocpgikFvOFrmH', '', 'No manual entry for ocpgikFvOFrmH'))))

    def test_diversity_3(self):
        self.assertEqual(1, len(get_new_command(Command('man puIHnCB', '', 'No manual entry for puIHnCB'))))

    def test_diversity_4(self):
        self.assertEqual(1, len(get_new_command(Command('man tZyNzEPDTKZC', '', 'No manual entry for tZyNzEPDTKZC'))))

    def test_diversity_5(self):
        self.assertEqual(1, len(get_new_command(Command('man DvyXvTAUhpff', '', 'No manual entry for DvyXvTAUhpff'))))

    def test_diversity_6(self):
        self.assertEqual(1, len(get_new_command(Command('man srBuqRf', '', 'No manual entry for srBuqRf'))))

    def test_diversity_7(self):
        self.assertEqual(1, len(get_new_command(Command('man qllByiPXNN', '', 'No manual entry for qllByiPXNN'))))

    def test_diversity_8(self):
        self.assertEqual(1, len(get_new_command(Command('man PHZVbDAw', '', 'No manual entry for PHZVbDAw'))))

    def test_diversity_9(self):
        self.assertEqual(1, len(get_new_command(Command('man zeXhz', '', 'No manual entry for zeXhz'))))

    def test_diversity_10(self):
        self.assertEqual(1, len(get_new_command(Command('man RQepOV', '', 'No manual entry for RQepOV'))))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(3, len(get_new_command(Command('man IvpbHscWuFy', '', 'some output KIvNrT'))))

    def test_diversity_2(self):
        self.assertEqual(3, len(get_new_command(Command('man UKtNhVXdiOH', '', 'some output UpmSL'))))

    def test_diversity_3(self):
        self.assertEqual(3, len(get_new_command(Command('man RzkVHsRpD', '', 'some output StQikFPegJUwvMy'))))

    def test_diversity_4(self):
        self.assertEqual(3, len(get_new_command(Command('man gUzLzyZi', '', 'some output mAXDjzJKH'))))

    def test_diversity_5(self):
        self.assertEqual(3, len(get_new_command(Command('man kuSPPo', '', 'some output UIJERLkvQWbyc'))))

    def test_diversity_6(self):
        self.assertEqual(3, len(get_new_command(Command('man RKJarcAtbJD', '', 'some output ljKuBUQSlei'))))

    def test_diversity_7(self):
        self.assertEqual(3, len(get_new_command(Command('man shksdZPkx', '', 'some output FoSvyJjzlLB'))))

    def test_diversity_8(self):
        self.assertEqual(3, len(get_new_command(Command('man cXgEPcydUIA', '', 'some output uynybrFnQ'))))

    def test_diversity_9(self):
        self.assertEqual(3, len(get_new_command(Command('man aKeyfu', '', 'some output mXLogFvDI'))))

    def test_diversity_10(self):
        self.assertEqual(3, len(get_new_command(Command('man WuXmAJkprdkyZ', '', 'some output gfxIjDFFye'))))
