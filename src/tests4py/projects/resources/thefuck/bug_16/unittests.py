import unittest
from thefuck.shells.bash import Bash
from thefuck.shells.zsh import Zsh


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        b = Bash()
        self.assertIn("alias GCjolSgmPqG='TF_CMD=$(TF_ALIAS", b.app_alias('GCjolSgmPqG'))

    def test_diversity_2(self):
        b = Bash()
        self.assertIn("alias EKxBZWZrTLTv='TF_CMD=$(TF_ALIAS", b.app_alias('EKxBZWZrTLTv'))

    def test_diversity_3(self):
        b = Bash()
        self.assertIn('$(TF_ALIAS=RSfqQwkygEOqzhO PYTHONIOENCODING', b.app_alias('RSfqQwkygEOqzhO'))

    def test_diversity_4(self):
        z = Zsh()
        self.assertIn('$(TF_ALIAS=SnHVSwEGn PYTHONIOENCODING', z.app_alias('SnHVSwEGn'))

    def test_diversity_5(self):
        z = Zsh()
        self.assertIn(' history -s $TF_CMD', z.app_alias('jJjEC'))

    def test_diversity_6(self):
        b = Bash()
        self.assertIn('$(TF_ALIAS=qFlNJuuNoKE PYTHONIOENCODING', b.app_alias('qFlNJuuNoKE'))

    def test_diversity_7(self):
        b = Bash()
        self.assertIn('PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES', b.app_alias('ZwVDHcNJvXrN'))

    def test_diversity_8(self):
        z = Zsh()
        self.assertIn("alias SurKMnM='TF_CMD=$(TF_ALIAS", z.app_alias('SurKMnM'))

    def test_diversity_9(self):
        z = Zsh()
        self.assertIn("alias JGYwhGPW='TF_CMD=$(TF_ALIAS", z.app_alias('JGYwhGPW'))

    def test_diversity_10(self):
        z = Zsh()
        self.assertIn(' history -s $TF_CMD', z.app_alias('JvNwbbmvxZiMMI'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        z = Zsh()
        self.assertIn('TF_ALIAS=kqrdhAfvab', z.app_alias('kqrdhAfvab'))

    def test_diversity_2(self):
        b = Bash()
        self.assertIn('  eval $TF_CMD ', b.app_alias('zsocxSnwiuy'))

    def test_diversity_3(self):
        b = Bash()
        self.assertIn('PYTHONIOENCODING=utf-8', b.app_alias('nLtjSVYqXYpE'))

    def test_diversity_4(self):
        z = Zsh()
        self.assertIn('PYTHONIOENCODING=utf-8', z.app_alias('bWJsuf'))

    def test_diversity_5(self):
        z = Zsh()
        self.assertIn('TF_ALIAS=Uedyq', z.app_alias('Uedyq'))

    def test_diversity_6(self):
        b = Bash()
        self.assertIn('alias IPYBHnTvVAWs', b.app_alias('IPYBHnTvVAWs'))

    def test_diversity_7(self):
        z = Zsh()
        self.assertIn('alias uZUQbWmJHUMg', z.app_alias('uZUQbWmJHUMg'))

    def test_diversity_8(self):
        b = Bash()
        self.assertIn('TF_ALIAS=wWPgowPFX', b.app_alias('wWPgowPFX'))

    def test_diversity_9(self):
        b = Bash()
        self.assertIn(' history -s $TF_CMD', b.app_alias('OBSVQVLoEQylrA'))

    def test_diversity_10(self):
        b = Bash()
        self.assertIn('  eval $TF_CMD ', b.app_alias('WrSgjfmkChjGBJ'))
