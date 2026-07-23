import unittest
from thefuck.shells.bash import Bash


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('TF_SHELL_ALIASES=$(alias) thefuck', ('TF_SHELL_ALIASES=$(alias) thefuck' if 'TF_SHELL_ALIASES=$(alias) thefuck' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_2(self):
        self.assertEqual('$(TF_SHELL_ALIASES=$(alias) thefuck', ('$(TF_SHELL_ALIASES=$(alias) thefuck' if '$(TF_SHELL_ALIASES=$(alias) thefuck' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_3(self):
        self.assertEqual('TF_CMD=$(TF_SHELL_ALIASES=', ('TF_CMD=$(TF_SHELL_ALIASES=' if 'TF_CMD=$(TF_SHELL_ALIASES=' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_4(self):
        self.assertEqual('=$(TF_SHELL_ALIASES=$(alias) thefuck $', ('=$(TF_SHELL_ALIASES=$(alias) thefuck $' if '=$(TF_SHELL_ALIASES=$(alias) thefuck $' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_5(self):
        self.assertEqual('TF_SHELL_ALIASES=$(alias) thefuck $(', ('TF_SHELL_ALIASES=$(alias) thefuck $(' if 'TF_SHELL_ALIASES=$(alias) thefuck $(' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_6(self):
        self.assertEqual('$(TF_SHELL_ALIASES=$(alias) thefuck $(fc', ('$(TF_SHELL_ALIASES=$(alias) thefuck $(fc' if '$(TF_SHELL_ALIASES=$(alias) thefuck $(fc' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_7(self):
        self.assertEqual('TF_CMD=$(TF_SHELL_ALIASES=$(alias)', ('TF_CMD=$(TF_SHELL_ALIASES=$(alias)' if 'TF_CMD=$(TF_SHELL_ALIASES=$(alias)' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_8(self):
        self.assertEqual('TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln', ('TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln' if 'TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_9(self):
        self.assertEqual('$(alias) thefuck $(fc -ln -1))', ('$(alias) thefuck $(fc -ln -1))' if '$(alias) thefuck $(fc -ln -1))' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_10(self):
        self.assertEqual('TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln -1', ('TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln -1' if 'TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln -1' in Bash().app_alias('fuck') else 'MISS'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('PYTHONIOENCODING=utf-8', ('PYTHONIOENCODING=utf-8' if 'PYTHONIOENCODING=utf-8' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_2(self):
        self.assertEqual('eval $TF_CMD', ('eval $TF_CMD' if 'eval $TF_CMD' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_3(self):
        self.assertEqual('TF_ALIAS=fuck', ('TF_ALIAS=fuck' if 'TF_ALIAS=fuck' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_4(self):
        self.assertEqual('$(fc -ln -1)', ('$(fc -ln -1)' if '$(fc -ln -1)' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_5(self):
        self.assertEqual('history -s $TF_CMD', ('history -s $TF_CMD' if 'history -s $TF_CMD' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_6(self):
        self.assertEqual('alias fuck=', ('alias fuck=' if 'alias fuck=' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_7(self):
        self.assertEqual('TF_CMD=$(', ('TF_CMD=$(' if 'TF_CMD=$(' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_8(self):
        self.assertEqual('thefuck $(fc -ln -1)', ('thefuck $(fc -ln -1)' if 'thefuck $(fc -ln -1)' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_9(self):
        self.assertEqual('&& history -s $TF_CMD', ('&& history -s $TF_CMD' if '&& history -s $TF_CMD' in Bash().app_alias('fuck') else 'MISS'))

    def test_diversity_10(self):
        self.assertEqual('=utf-8 TF_CMD=', ('=utf-8 TF_CMD=' if '=utf-8 TF_CMD=' in Bash().app_alias('fuck') else 'MISS'))
