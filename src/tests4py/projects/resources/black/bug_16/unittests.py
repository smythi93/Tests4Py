import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_symlink(kind, nonce):
        import os
        import re
        import tempfile
        from pathlib import Path
        import black
        root = Path(tempfile.mkdtemp()).resolve()
        child = root / ('link_' + nonce + '.py')
        if kind == 'symlink':
            outside = Path(tempfile.mkdtemp()).resolve() / 'target.py'
            outside.write_text('x = 1\n')
            os.symlink(str(outside), str(child))
        else:
            child.write_text('x = 1\n')
        include = re.compile(black.DEFAULT_INCLUDES)
        exclude = re.compile(black.DEFAULT_EXCLUDES)
        report = black.Report()
        try:
            list(black.gen_python_files_in_dir(root, root, include, exclude, report))
            return True
        except Exception:
            return False

    def test_diversity_1(self):
        self.assertTrue(self.run_symlink('symlink', 'yqpgipvcid'))

    def test_diversity_2(self):
        self.assertTrue(self.run_symlink('symlink', 'qnfgyttim'))

    def test_diversity_3(self):
        self.assertTrue(self.run_symlink('symlink', 'hekojtvycf'))

    def test_diversity_4(self):
        self.assertTrue(self.run_symlink('symlink', 'tkpbbxqtje'))

    def test_diversity_5(self):
        self.assertTrue(self.run_symlink('symlink', 'jphryyve'))

    def test_diversity_6(self):
        self.assertTrue(self.run_symlink('symlink', 'fkciotqey'))

    def test_diversity_7(self):
        self.assertTrue(self.run_symlink('symlink', 'mrbhwrqi'))

    def test_diversity_8(self):
        self.assertTrue(self.run_symlink('symlink', 'qlfzhik'))

    def test_diversity_9(self):
        self.assertTrue(self.run_symlink('symlink', 'dryvdf'))

    def test_diversity_10(self):
        self.assertTrue(self.run_symlink('symlink', 'clbrav'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_symlink(kind, nonce):
        import os
        import re
        import tempfile
        from pathlib import Path
        import black
        root = Path(tempfile.mkdtemp()).resolve()
        child = root / ('link_' + nonce + '.py')
        if kind == 'symlink':
            outside = Path(tempfile.mkdtemp()).resolve() / 'target.py'
            outside.write_text('x = 1\n')
            os.symlink(str(outside), str(child))
        else:
            child.write_text('x = 1\n')
        include = re.compile(black.DEFAULT_INCLUDES)
        exclude = re.compile(black.DEFAULT_EXCLUDES)
        report = black.Report()
        try:
            list(black.gen_python_files_in_dir(root, root, include, exclude, report))
            return True
        except Exception:
            return False

    def test_diversity_1(self):
        self.assertTrue(self.run_symlink('normal', 'mjlpmls'))

    def test_diversity_2(self):
        self.assertTrue(self.run_symlink('normal', 'sclcxzou'))

    def test_diversity_3(self):
        self.assertTrue(self.run_symlink('normal', 'bhfeqexyi'))

    def test_diversity_4(self):
        self.assertTrue(self.run_symlink('normal', 'gulvneordb'))

    def test_diversity_5(self):
        self.assertTrue(self.run_symlink('normal', 'wzruuyrhh'))

    def test_diversity_6(self):
        self.assertTrue(self.run_symlink('normal', 'zqpcpg'))

    def test_diversity_7(self):
        self.assertTrue(self.run_symlink('normal', 'mlcorrjms'))

    def test_diversity_8(self):
        self.assertTrue(self.run_symlink('normal', 'qudnwptuv'))

    def test_diversity_9(self):
        self.assertTrue(self.run_symlink('normal', 'hctuow'))

    def test_diversity_10(self):
        self.assertTrue(self.run_symlink('normal', 'muzjeroml'))
