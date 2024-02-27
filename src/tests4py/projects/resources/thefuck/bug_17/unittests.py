import unittest
from thefuck.shells.bash import Bash


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        bash = Bash()
        self.assertIn('theXPUCZodRGDXvpok', bash.app_alias('XPUCZodRGDXvpok'))

    def test_diversity_2(self):
        bash = Bash()
        self.assertIn('theRLUbxcRVNF', bash.app_alias('RLUbxcRVNF'))

    def test_diversity_3(self):
        bash = Bash()
        self.assertIn('theWJdwKLvDu', bash.app_alias('WJdwKLvDu'))

    def test_diversity_4(self):
        bash = Bash()
        self.assertIn('theqOeOMBOfEkpFyRc', bash.app_alias('qOeOMBOfEkpFyRc'))

    def test_diversity_5(self):
        bash = Bash()
        self.assertIn('thetUubxfyg', bash.app_alias('tUubxfyg'))

    def test_diversity_6(self):
        bash = Bash()
        self.assertIn('themCtYmqSiIpwMiHK', bash.app_alias('mCtYmqSiIpwMiHK'))

    def test_diversity_7(self):
        bash = Bash()
        self.assertIn('theHEcGxWaJ', bash.app_alias('HEcGxWaJ'))

    def test_diversity_8(self):
        bash = Bash()
        self.assertIn('theiOKbl', bash.app_alias('iOKbl'))

    def test_diversity_9(self):
        bash = Bash()
        self.assertIn('theSrWXsEHmXMpYblG', bash.app_alias('SrWXsEHmXMpYblG'))

    def test_diversity_10(self):
        bash = Bash()
        self.assertIn('theWFaaEAkoadnJamb', bash.app_alias('WFaaEAkoadnJamb'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        bash = Bash()
        self.assertIn('TF_ALIAS=kFyrnj', bash.app_alias('kFyrnj'))

    def test_diversity_2(self):
        bash = Bash()
        self.assertIn('alias qdaDDugWGi', bash.app_alias('qdaDDugWGi'))

    def test_diversity_3(self):
        bash = Bash()
        self.assertIn('alias uthODVr', bash.app_alias('uthODVr'))

    def test_diversity_4(self):
        bash = Bash()
        self.assertIn('TF_ALIAS=DAnFXKkf', bash.app_alias('DAnFXKkf'))

    def test_diversity_5(self):
        bash = Bash()
        self.assertIn('TF_ALIAS=bnzsIqaJK', bash.app_alias('bnzsIqaJK'))

    def test_diversity_6(self):
        bash = Bash()
        self.assertIn('TF_ALIAS=YBeptA', bash.app_alias('YBeptA'))

    def test_diversity_7(self):
        bash = Bash()
        self.assertIn('alias ZWXZoAJbbGKI', bash.app_alias('ZWXZoAJbbGKI'))

    def test_diversity_8(self):
        bash = Bash()
        self.assertIn('alias ZBnWysrr', bash.app_alias('ZBnWysrr'))

    def test_diversity_9(self):
        bash = Bash()
        self.assertIn('TF_ALIAS=CGLuHxJlUF', bash.app_alias('CGLuHxJlUF'))

    def test_diversity_10(self):
        bash = Bash()
        self.assertIn('TF_ALIAS=emhliynnTpGlDXU', bash.app_alias('emhliynnTpGlDXU'))
