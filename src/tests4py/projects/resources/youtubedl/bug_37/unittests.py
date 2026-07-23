import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import uppercase_escape


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('limt㻵wj', uppercase_escape('limt\\U00003ef5wj'))

    def test_diversity_2(self):
        self.assertEqual('kbau鯫odzrgt', uppercase_escape('kbau\\U00009bebodzrgt'))

    def test_diversity_3(self):
        self.assertEqual('mpjkug̽pgoa', uppercase_escape('mpjkug\\U0000033dpgoa'))

    def test_diversity_4(self):
        self.assertEqual('npn卾jysq', uppercase_escape('npn\\U0000537ejysq'))

    def test_diversity_5(self):
        self.assertEqual('zeazs㸰lvs', uppercase_escape('zeazs\\U00003e30lvs'))

    def test_diversity_6(self):
        self.assertEqual('ypwn숸pvnsuj', uppercase_escape('ypwn\\U0000c238pvnsuj'))

    def test_diversity_7(self):
        self.assertEqual('sn柊dumodu', uppercase_escape('sn\\U000067cadumodu'))

    def test_diversity_8(self):
        self.assertEqual('zbk䰨joemyy', uppercase_escape('zbk\\U00004c28joemyy'))

    def test_diversity_9(self):
        self.assertEqual('yxcv瞔be', uppercase_escape('yxcv\\U00007794be'))

    def test_diversity_10(self):
        self.assertEqual('ehyg⥼pbug', uppercase_escape('ehyg\\U0000297cpbug'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('iplojkhxxsype', uppercase_escape('iplojkhxxsype'))

    def test_diversity_2(self):
        self.assertEqual('llnigxgoive', uppercase_escape('llnigxgoive'))

    def test_diversity_3(self):
        self.assertEqual('egyxjfxakbx', uppercase_escape('egyxjfxakbx'))

    def test_diversity_4(self):
        self.assertEqual('vvsmuys', uppercase_escape('vvsmuys'))

    def test_diversity_5(self):
        self.assertEqual('znlrhuedlnycupgxyw', uppercase_escape('znlrhuedlnycupgxyw'))

    def test_diversity_6(self):
        self.assertEqual('weuftgehzzfnx', uppercase_escape('weuftgehzzfnx'))

    def test_diversity_7(self):
        self.assertEqual('kaywqvajgtkmi', uppercase_escape('kaywqvajgtkmi'))

    def test_diversity_8(self):
        self.assertEqual('ntuuohahoylwkflye', uppercase_escape('ntuuohahoylwkflye'))

    def test_diversity_9(self):
        self.assertEqual('bujetujdranu', uppercase_escape('bujetujdranu'))

    def test_diversity_10(self):
        self.assertEqual('abyatwwmbglgknahr', uppercase_escape('abyatwwmbglgknahr'))
