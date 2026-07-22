import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_diff_header(kind, nonce):
        import os
        import sys as _sys
        import tempfile
        from io import StringIO
        from pathlib import Path
        import black
        d = tempfile.mkdtemp()
        name = 'f_' + nonce + '.py'
        with open(os.path.join(d, name), 'w') as f:
            f.write('x=1\n')
        cwd = None
        if kind == 'subdir':
            src = Path(os.path.join(d, name))
        else:
            cwd = os.getcwd()
            os.chdir(d)
            src = Path(name)
        expected = str(src)
        hold = _sys.stdout
        _sys.stdout = StringIO()
        try:
            black.format_file_in_place(src, 88, False, black.WriteBack.DIFF)
            _sys.stdout.seek(0)
            out = _sys.stdout.read()
        finally:
            _sys.stdout = hold
            if cwd is not None:
                os.chdir(cwd)
        first = out.splitlines()[0] if out else ''
        marker = '  (original)'
        header = first[4:first.index(marker)] if first.startswith('--- ') and marker in first else ''
        return (header, expected)

    def test_diversity_1(self):
        header, expected = self.run_diff_header('subdir', 'ynuhixchy')
        self.assertEqual(expected, header)

    def test_diversity_2(self):
        header, expected = self.run_diff_header('subdir', 'peyjcmkh')
        self.assertEqual(expected, header)

    def test_diversity_3(self):
        header, expected = self.run_diff_header('subdir', 'rfgdpa')
        self.assertEqual(expected, header)

    def test_diversity_4(self):
        header, expected = self.run_diff_header('subdir', 'vxuknvvapu')
        self.assertEqual(expected, header)

    def test_diversity_5(self):
        header, expected = self.run_diff_header('subdir', 'qgbkreamnw')
        self.assertEqual(expected, header)

    def test_diversity_6(self):
        header, expected = self.run_diff_header('subdir', 'zddnnrayfj')
        self.assertEqual(expected, header)

    def test_diversity_7(self):
        header, expected = self.run_diff_header('subdir', 'jxdqwuwuon')
        self.assertEqual(expected, header)

    def test_diversity_8(self):
        header, expected = self.run_diff_header('subdir', 'vwqobk')
        self.assertEqual(expected, header)

    def test_diversity_9(self):
        header, expected = self.run_diff_header('subdir', 'dglcsvgty')
        self.assertEqual(expected, header)

    def test_diversity_10(self):
        header, expected = self.run_diff_header('subdir', 'ehzmszm')
        self.assertEqual(expected, header)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_diff_header(kind, nonce):
        import os
        import sys as _sys
        import tempfile
        from io import StringIO
        from pathlib import Path
        import black
        d = tempfile.mkdtemp()
        name = 'f_' + nonce + '.py'
        with open(os.path.join(d, name), 'w') as f:
            f.write('x=1\n')
        cwd = None
        if kind == 'subdir':
            src = Path(os.path.join(d, name))
        else:
            cwd = os.getcwd()
            os.chdir(d)
            src = Path(name)
        expected = str(src)
        hold = _sys.stdout
        _sys.stdout = StringIO()
        try:
            black.format_file_in_place(src, 88, False, black.WriteBack.DIFF)
            _sys.stdout.seek(0)
            out = _sys.stdout.read()
        finally:
            _sys.stdout = hold
            if cwd is not None:
                os.chdir(cwd)
        first = out.splitlines()[0] if out else ''
        marker = '  (original)'
        header = first[4:first.index(marker)] if first.startswith('--- ') and marker in first else ''
        return (header, expected)

    def test_diversity_1(self):
        header, expected = self.run_diff_header('relative', 'krrsrvimh')
        self.assertEqual(expected, header)

    def test_diversity_2(self):
        header, expected = self.run_diff_header('relative', 'whzzrogp')
        self.assertEqual(expected, header)

    def test_diversity_3(self):
        header, expected = self.run_diff_header('relative', 'fsecuq')
        self.assertEqual(expected, header)

    def test_diversity_4(self):
        header, expected = self.run_diff_header('relative', 'japuotan')
        self.assertEqual(expected, header)

    def test_diversity_5(self):
        header, expected = self.run_diff_header('relative', 'qczaxxlzqm')
        self.assertEqual(expected, header)

    def test_diversity_6(self):
        header, expected = self.run_diff_header('relative', 'gczqykdx')
        self.assertEqual(expected, header)

    def test_diversity_7(self):
        header, expected = self.run_diff_header('relative', 'wmwizopoqm')
        self.assertEqual(expected, header)

    def test_diversity_8(self):
        header, expected = self.run_diff_header('relative', 'irnoeedjh')
        self.assertEqual(expected, header)

    def test_diversity_9(self):
        header, expected = self.run_diff_header('relative', 'ojhhlzzzj')
        self.assertEqual(expected, header)

    def test_diversity_10(self):
        header, expected = self.run_diff_header('relative', 'jpoqloaac')
        self.assertEqual(expected, header)
