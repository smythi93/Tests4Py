import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_newline(kind, nonce):
        import os
        import tempfile
        from pathlib import Path
        import black
        d = tempfile.mkdtemp()
        path = Path(os.path.join(d, 'f_' + nonce + '.py'))
        newline = b'\r\n' if kind == 'crlf' else b'\n'
        path.write_bytes(newline.join([b'def f(  ):', b'    pass']))
        black.format_file_in_place(path, 88, False, black.WriteBack.YES)
        return b'\r\n' in path.read_bytes()

    def test_diversity_1(self):
        self.assertTrue(self.run_newline('crlf', 'ajgldrpobs'))

    def test_diversity_2(self):
        self.assertTrue(self.run_newline('crlf', 'lqzxjaxtu'))

    def test_diversity_3(self):
        self.assertTrue(self.run_newline('crlf', 'otleczkxm'))

    def test_diversity_4(self):
        self.assertTrue(self.run_newline('crlf', 'ooymiln'))

    def test_diversity_5(self):
        self.assertTrue(self.run_newline('crlf', 'iygjxl'))

    def test_diversity_6(self):
        self.assertTrue(self.run_newline('crlf', 'erkfyymefi'))

    def test_diversity_7(self):
        self.assertTrue(self.run_newline('crlf', 'umsoxhtgz'))

    def test_diversity_8(self):
        self.assertTrue(self.run_newline('crlf', 'mkbdak'))

    def test_diversity_9(self):
        self.assertTrue(self.run_newline('crlf', 'shttffuyb'))

    def test_diversity_10(self):
        self.assertTrue(self.run_newline('crlf', 'tmoyavw'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_newline(kind, nonce):
        import os
        import tempfile
        from pathlib import Path
        import black
        d = tempfile.mkdtemp()
        path = Path(os.path.join(d, 'f_' + nonce + '.py'))
        newline = b'\r\n' if kind == 'crlf' else b'\n'
        path.write_bytes(newline.join([b'def f(  ):', b'    pass']))
        black.format_file_in_place(path, 88, False, black.WriteBack.YES)
        return b'\r\n' in path.read_bytes()

    def test_diversity_1(self):
        self.assertFalse(self.run_newline('lf', 'qytqjiibfc'))

    def test_diversity_2(self):
        self.assertFalse(self.run_newline('lf', 'qscpvcipsh'))

    def test_diversity_3(self):
        self.assertFalse(self.run_newline('lf', 'jgytnlkgkh'))

    def test_diversity_4(self):
        self.assertFalse(self.run_newline('lf', 'joycsgoqwa'))

    def test_diversity_5(self):
        self.assertFalse(self.run_newline('lf', 'squppuerfc'))

    def test_diversity_6(self):
        self.assertFalse(self.run_newline('lf', 'dxocuhxqm'))

    def test_diversity_7(self):
        self.assertFalse(self.run_newline('lf', 'dhzupbswa'))

    def test_diversity_8(self):
        self.assertFalse(self.run_newline('lf', 'lfmpvhotq'))

    def test_diversity_9(self):
        self.assertFalse(self.run_newline('lf', 'cngnfqe'))

    def test_diversity_10(self):
        self.assertFalse(self.run_newline('lf', 'fvrilam'))
