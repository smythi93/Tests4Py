import unittest
from thefuck.types import RulesNamesList
from thefuck.types import Rule


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIn(Rule('sEHf', '', '', '', '', '', ''), RulesNamesList(['YFrXV', 'hCyiw']))

    def test_diversity_2(self):
        self.assertIn(Rule('BPUGKuP', '', '', '', '', '', ''), RulesNamesList(['xccc', 'Lwyu']))

    def test_diversity_3(self):
        self.assertIn(Rule('hfNVy', '', '', '', '', '', ''), RulesNamesList(['oWPLK', 'KjCCnH']))

    def test_diversity_4(self):
        self.assertIn(Rule('YayIdCL', '', '', '', '', '', ''), RulesNamesList(['rSDM', 'MuNLD']))

    def test_diversity_5(self):
        self.assertIn(Rule('amysk', '', '', '', '', '', ''), RulesNamesList(['mZFSTi', 'SbDPPf']))

    def test_diversity_6(self):
        self.assertIn(Rule('iale', '', '', '', '', '', ''), RulesNamesList(['vDCyPolR', 'KBTX']))

    def test_diversity_7(self):
        self.assertIn(Rule('qXlO', '', '', '', '', '', ''), RulesNamesList(['uwKB', 'AcqZvH']))

    def test_diversity_8(self):
        self.assertIn(Rule('mqAfNP', '', '', '', '', '', ''), RulesNamesList(['TvjlP', 'MDkBKiPb']))

    def test_diversity_9(self):
        self.assertIn(Rule('ftsc', '', '', '', '', '', ''), RulesNamesList(['QkLzjZ', 'RhZMVdp']))

    def test_diversity_10(self):
        self.assertIn(Rule('RLnLgVvn', '', '', '', '', '', ''), RulesNamesList(['vXhQ', 'sKDoim']))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIn(Rule('dNrrSFd', '', '', '', '', '', ''), RulesNamesList(['dNrrSFd', 'BaPmByO']))

    def test_diversity_2(self):
        self.assertIn(Rule('ysaIJ', '', '', '', '', '', ''), RulesNamesList(['ysaIJ', 'bOkG']))

    def test_diversity_3(self):
        self.assertIn(Rule('PqTyiFR', '', '', '', '', '', ''), RulesNamesList(['PqTyiFR', 'OSAuRe']))

    def test_diversity_4(self):
        self.assertIn(Rule('JTvUgEZ', '', '', '', '', '', ''), RulesNamesList(['JTvUgEZ', 'OUeudd']))

    def test_diversity_5(self):
        self.assertIn(Rule('HQzuzQWE', '', '', '', '', '', ''), RulesNamesList(['HQzuzQWE', 'eAQy']))

    def test_diversity_6(self):
        self.assertIn(Rule('wrLmtF', '', '', '', '', '', ''), RulesNamesList(['wrLmtF', 'RhwBOul']))

    def test_diversity_7(self):
        self.assertIn(Rule('HRaYMqd', '', '', '', '', '', ''), RulesNamesList(['HRaYMqd', 'ZDCcu']))

    def test_diversity_8(self):
        self.assertIn(Rule('wtSQ', '', '', '', '', '', ''), RulesNamesList(['wtSQ', 'BCWqYN']))

    def test_diversity_9(self):
        self.assertIn(Rule('KQApuJ', '', '', '', '', '', ''), RulesNamesList(['KQApuJ', 'YimnoCtJ']))

    def test_diversity_10(self):
        self.assertIn(Rule('aKZP', '', '', '', '', '', ''), RulesNamesList(['aKZP', 'MRxzXL']))
