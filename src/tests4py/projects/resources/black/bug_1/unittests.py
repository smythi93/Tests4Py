import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_mono(kind, nonce):
        import asyncio
        import os
        import tempfile
        from unittest.mock import patch
        from click.testing import CliRunner
        import black
        asyncio.set_event_loop(asyncio.new_event_loop())
        d = tempfile.mkdtemp()
        files = [os.path.join(d, 'f_' + nonce + '_' + str(i) + '.py') for i in range(2)]
        for f in files:
            with open(f, 'w') as fh:
                fh.write("print('hello')")
        if kind == 'patched':
            with patch('black.ProcessPoolExecutor') as mock_executor:
                mock_executor.side_effect = OSError()
                CliRunner().invoke(black.main, [d])
        else:
            CliRunner().invoke(black.main, [d])
        return all((open(f).read() == 'print("hello")\n' for f in files))

    def test_diversity_1(self):
        self.assertTrue(self.run_mono('patched', 'kihniua'))

    def test_diversity_2(self):
        self.assertTrue(self.run_mono('patched', 'niwawphhmf'))

    def test_diversity_3(self):
        self.assertTrue(self.run_mono('patched', 'dfplmlster'))

    def test_diversity_4(self):
        self.assertTrue(self.run_mono('patched', 'ckcpwa'))

    def test_diversity_5(self):
        self.assertTrue(self.run_mono('patched', 'ljqgsbr'))

    def test_diversity_6(self):
        self.assertTrue(self.run_mono('patched', 'iclvhhm'))

    def test_diversity_7(self):
        self.assertTrue(self.run_mono('patched', 'smxlgall'))

    def test_diversity_8(self):
        self.assertTrue(self.run_mono('patched', 'beyzeq'))

    def test_diversity_9(self):
        self.assertTrue(self.run_mono('patched', 'qxyxeeta'))

    def test_diversity_10(self):
        self.assertTrue(self.run_mono('patched', 'veejdby'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_mono(kind, nonce):
        import asyncio
        import os
        import tempfile
        from unittest.mock import patch
        from click.testing import CliRunner
        import black
        asyncio.set_event_loop(asyncio.new_event_loop())
        d = tempfile.mkdtemp()
        files = [os.path.join(d, 'f_' + nonce + '_' + str(i) + '.py') for i in range(2)]
        for f in files:
            with open(f, 'w') as fh:
                fh.write("print('hello')")
        if kind == 'patched':
            with patch('black.ProcessPoolExecutor') as mock_executor:
                mock_executor.side_effect = OSError()
                CliRunner().invoke(black.main, [d])
        else:
            CliRunner().invoke(black.main, [d])
        return all((open(f).read() == 'print("hello")\n' for f in files))

    def test_diversity_1(self):
        self.assertTrue(self.run_mono('normal', 'jwpalhauav'))

    def test_diversity_2(self):
        self.assertTrue(self.run_mono('normal', 'ubllsykdao'))

    def test_diversity_3(self):
        self.assertTrue(self.run_mono('normal', 'ifsgqp'))

    def test_diversity_4(self):
        self.assertTrue(self.run_mono('normal', 'erbwfnkcil'))

    def test_diversity_5(self):
        self.assertTrue(self.run_mono('normal', 'tvrvpjxiug'))

    def test_diversity_6(self):
        self.assertTrue(self.run_mono('normal', 'kidlxh'))

    def test_diversity_7(self):
        self.assertTrue(self.run_mono('normal', 'qwcxffiht'))

    def test_diversity_8(self):
        self.assertTrue(self.run_mono('normal', 'zboduhma'))

    def test_diversity_9(self):
        self.assertTrue(self.run_mono('normal', 'bkjibstpnu'))

    def test_diversity_10(self):
        self.assertTrue(self.run_mono('normal', 'rqkmrh'))
