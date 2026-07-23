import unittest
from thefuck.types import SortedCorrectedCommandsSequence
from thefuck.types import CorrectedCommand
from thefuck.types import Settings


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'ubogcrkgs': 'v'}))._realise() or 'OK'))

    def test_diversity_2(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'dnjzyez': 'v'}))._realise() or 'OK'))

    def test_diversity_3(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'ujzzyzu': 'v'}))._realise() or 'OK'))

    def test_diversity_4(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'lkwtcozzi': 'v'}))._realise() or 'OK'))

    def test_diversity_5(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'zgxthrzgwi': 'v'}))._realise() or 'OK'))

    def test_diversity_6(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'hmbxmqhj': 'v'}))._realise() or 'OK'))

    def test_diversity_7(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'gihzekpvb': 'v'}))._realise() or 'OK'))

    def test_diversity_8(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'dmohflhdh': 'v'}))._realise() or 'OK'))

    def test_diversity_9(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'hixjuk': 'v'}))._realise() or 'OK'))

    def test_diversity_10(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([]), Settings({'yyyes': 'v'}))._realise() or 'OK'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('qjbzpwr', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_2(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('mbddhpzysz', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_3(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('vpxgdrqm', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_4(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('iqzlfast', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_5(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('hjgzjchxxv', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_6(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('guwwagss', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_7(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('vcogxkbiu', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_8(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('brtbetubq', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_9(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('ydxrn', '', 1)]), Settings({}))._realise() or 'OK'))

    def test_diversity_10(self):
        self.assertEqual('OK', (SortedCorrectedCommandsSequence(iter([CorrectedCommand('zynnitmggx', '', 1)]), Settings({}))._realise() or 'OK'))
