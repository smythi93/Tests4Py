import unittest
from thefuck.shells.bash import Bash
from thefuck.shells.zsh import Zsh


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('TF_CMD=$(TF_ALIAS=fuck', ('TF_CMD=$(TF_ALIAS=fuck' if 'TF_CMD=$(TF_ALIAS=fuck' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_2(self):
        self.assertEqual("alias fuck='TF_CMD=$(TF_ALIAS=", ("alias fuck='TF_CMD=$(TF_ALIAS=" if "alias fuck='TF_CMD=$(TF_ALIAS=" in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_3(self):
        self.assertEqual('TF_CMD=$(TF_ALIAS=fuck PYTHONIOENCODING', ('TF_CMD=$(TF_ALIAS=fuck PYTHONIOENCODING' if 'TF_CMD=$(TF_ALIAS=fuck PYTHONIOENCODING' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_4(self):
        self.assertEqual('$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8', ('$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8' if '$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_5(self):
        self.assertEqual("'TF_CMD=$(TF_ALIAS=fuck", ("'TF_CMD=$(TF_ALIAS=fuck" if "'TF_CMD=$(TF_ALIAS=fuck" in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_6(self):
        self.assertEqual('=$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES', ('=$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES' if '=$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_7(self):
        self.assertEqual('TF_CMD=$(TF_ALIAS=fuck', ('TF_CMD=$(TF_ALIAS=fuck' if 'TF_CMD=$(TF_ALIAS=fuck' in Zsh().app_alias('fuck') else 'MISS'))

    def test_diversity_8(self):
        self.assertEqual('$(alias) thefuck $(fc -ln -1 | tail', ('$(alias) thefuck $(fc -ln -1 | tail' if '$(alias) thefuck $(fc -ln -1 | tail' in Zsh().app_alias('fuck') else 'MISS'))

    def test_diversity_9(self):
        self.assertEqual("alias fuck='TF_CMD=$(TF_ALIAS=fuck", ("alias fuck='TF_CMD=$(TF_ALIAS=fuck" if "alias fuck='TF_CMD=$(TF_ALIAS=fuck" in Zsh().app_alias('fuck') else 'MISS'))

    def test_diversity_10(self):
        self.assertEqual('PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES=$(alias) thefuck', ('PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES=$(alias) thefuck' if 'PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES=$(alias) thefuck' in Zsh().app_alias('fuck') else 'MISS'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('PYTHONIOENCODING=utf-8', ('PYTHONIOENCODING=utf-8' if 'PYTHONIOENCODING=utf-8' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_2(self):
        self.assertEqual('TF_SHELL_ALIASES=$(alias)', ('TF_SHELL_ALIASES=$(alias)' if 'TF_SHELL_ALIASES=$(alias)' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_3(self):
        self.assertEqual('eval $TF_CMD', ('eval $TF_CMD' if 'eval $TF_CMD' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_4(self):
        self.assertEqual('history -s $TF_CMD', ('history -s $TF_CMD' if 'history -s $TF_CMD' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_5(self):
        self.assertEqual('$(fc -ln -1)', ('$(fc -ln -1)' if '$(fc -ln -1)' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_6(self):
        self.assertEqual('PYTHONIOENCODING=utf-8', ('PYTHONIOENCODING=utf-8' if 'PYTHONIOENCODING=utf-8' in Zsh().app_alias('fuck') else 'MISS'))

    def test_diversity_7(self):
        self.assertEqual('TF_SHELL_ALIASES=$(alias)', ('TF_SHELL_ALIASES=$(alias)' if 'TF_SHELL_ALIASES=$(alias)' in Zsh().app_alias('fuck') else 'MISS'))

    def test_diversity_8(self):
        self.assertEqual('eval $TF_CMD', ('eval $TF_CMD' if 'eval $TF_CMD' in Zsh().app_alias('fuck') else 'MISS'))

    def test_diversity_9(self):
        self.assertEqual('print -s $TF_CMD', ('print -s $TF_CMD' if 'print -s $TF_CMD' in Zsh().app_alias('fuck') else 'MISS'))

    def test_diversity_10(self):
        self.assertEqual('tail -n 1', ('tail -n 1' if 'tail -n 1' in Zsh().app_alias('fuck') else 'MISS'))
