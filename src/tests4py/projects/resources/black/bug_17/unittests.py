import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_empty(kind, nonce):
        import tempfile
        from pathlib import Path
        import black
        path = Path(tempfile.mkdtemp()) / ('f_' + nonce + '.py')
        if kind == 'empty':
            path.write_bytes(b'')
        else:
            path.write_bytes(b'x = 1\n')
        try:
            black.format_file_in_place(path, 88, False, black.WriteBack.YES)
            return True
        except Exception:
            return False

    def test_diversity_1(self):
        self.assertTrue(self.run_empty('empty', 'vuosof'))

    def test_diversity_2(self):
        self.assertTrue(self.run_empty('empty', 'semmlhser'))

    def test_diversity_3(self):
        self.assertTrue(self.run_empty('empty', 'rsxqjceuko'))

    def test_diversity_4(self):
        self.assertTrue(self.run_empty('empty', 'dojqglsuon'))

    def test_diversity_5(self):
        self.assertTrue(self.run_empty('empty', 'vcceyjlr'))

    def test_diversity_6(self):
        self.assertTrue(self.run_empty('empty', 'dvepwhpp'))

    def test_diversity_7(self):
        self.assertTrue(self.run_empty('empty', 'rebqhimiyi'))

    def test_diversity_8(self):
        self.assertTrue(self.run_empty('empty', 'kkczckgqxr'))

    def test_diversity_9(self):
        self.assertTrue(self.run_empty('empty', 'caqxqtnp'))

    def test_diversity_10(self):
        self.assertTrue(self.run_empty('empty', 'tzoukfet'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_empty(kind, nonce):
        import tempfile
        from pathlib import Path
        import black
        path = Path(tempfile.mkdtemp()) / ('f_' + nonce + '.py')
        if kind == 'empty':
            path.write_bytes(b'')
        else:
            path.write_bytes(b'x = 1\n')
        try:
            black.format_file_in_place(path, 88, False, black.WriteBack.YES)
            return True
        except Exception:
            return False

    def test_diversity_1(self):
        self.assertTrue(self.run_empty('nonempty', 'vmftnr'))

    def test_diversity_2(self):
        self.assertTrue(self.run_empty('nonempty', 'bixgjesd'))

    def test_diversity_3(self):
        self.assertTrue(self.run_empty('nonempty', 'rtxnwawy'))

    def test_diversity_4(self):
        self.assertTrue(self.run_empty('nonempty', 'umdkfowuu'))

    def test_diversity_5(self):
        self.assertTrue(self.run_empty('nonempty', 'ywjyholdt'))

    def test_diversity_6(self):
        self.assertTrue(self.run_empty('nonempty', 'psedzcb'))

    def test_diversity_7(self):
        self.assertTrue(self.run_empty('nonempty', 'omodzhg'))

    def test_diversity_8(self):
        self.assertTrue(self.run_empty('nonempty', 'vxdvltpg'))

    def test_diversity_9(self):
        self.assertTrue(self.run_empty('nonempty', 'kmlxnliwlx'))

    def test_diversity_10(self):
        self.assertTrue(self.run_empty('nonempty', 'rehjfmdmk'))
