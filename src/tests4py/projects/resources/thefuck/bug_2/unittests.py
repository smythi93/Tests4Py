import unittest
import os
from thefuck.utils import get_all_executables
import thefuck.utils as _tfu

# The buggy get_all_executables splits $PATH on a hard-coded ':' instead of
# os.pathsep. Force a Windows-style separator so the fault is observable: with
# ';' the buggy code sees one bogus directory and finds nothing, the fixed code
# splits correctly. memoize is disabled so every test recomputes.
_tfu.memoize.disabled = True
_DIRS = ["/usr/bin", "/bin", "/usr/sbin", "/sbin"]


def _semi():
    os.pathsep = ";"
    os.environ["PATH"] = ";".join(_DIRS)


def _plain():
    os.pathsep = ":"
    os.environ["PATH"] = ":".join(_DIRS)


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _semi(); self.assertIn("git", get_all_executables())

    def test_diversity_2(self):
        _semi(); self.assertIn("ls", get_all_executables())

    def test_diversity_3(self):
        _semi(); self.assertIn("cat", get_all_executables())

    def test_diversity_4(self):
        _semi(); self.assertIn("echo", get_all_executables())

    def test_diversity_5(self):
        _semi(); self.assertIn("cp", get_all_executables())

    def test_diversity_6(self):
        _semi(); self.assertIn("mv", get_all_executables())

    def test_diversity_7(self):
        _semi(); self.assertIn("rm", get_all_executables())

    def test_diversity_8(self):
        _semi(); self.assertIn("date", get_all_executables())

    def test_diversity_9(self):
        _semi(); self.assertIn("grep", get_all_executables())

    def test_diversity_10(self):
        _semi(); self.assertIn("sort", get_all_executables())


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _plain(); self.assertIn("head", get_all_executables())

    def test_diversity_2(self):
        _plain(); self.assertIn("tail", get_all_executables())

    def test_diversity_3(self):
        _plain(); self.assertIn("uniq", get_all_executables())

    def test_diversity_4(self):
        _plain(); self.assertIn("wc", get_all_executables())

    def test_diversity_5(self):
        _plain(); self.assertIn("pwd", get_all_executables())

    def test_diversity_6(self):
        _plain(); self.assertIn("sed", get_all_executables())

    def test_diversity_7(self):
        _plain(); self.assertIn("awk", get_all_executables())

    def test_diversity_8(self):
        _plain(); self.assertIn("find", get_all_executables())

    def test_diversity_9(self):
        _plain(); self.assertIn("tar", get_all_executables())

    def test_diversity_10(self):
        _plain(); self.assertIn("curl", get_all_executables())
