import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_black_config(kind, nonce=''):
        import os
        import tempfile
        from click.testing import CliRunner
        import black
        d = tempfile.mkdtemp()
        src = os.path.join(d, 's.py')
        with open(src, 'w') as f:
            f.write('x = 1\n')
        if kind == 'invalid':
            config = os.path.join(d, 'does_not_exist.toml')
        else:
            config = os.path.join(d, 'cfg.toml')
            with open(config, 'w') as f:
                f.write('')
        result = CliRunner().invoke(black.main, ['--config', config, '--check', src])
        return result.exit_code

    def test_diversity_1(self):
        self.assertEqual(2, self.run_black_config('invalid', 'czimfadyx'))

    def test_diversity_2(self):
        self.assertEqual(2, self.run_black_config('invalid', 'kozdbbch'))

    def test_diversity_3(self):
        self.assertEqual(2, self.run_black_config('invalid', 'rbsuoctis'))

    def test_diversity_4(self):
        self.assertEqual(2, self.run_black_config('invalid', 'ilhflpnpve'))

    def test_diversity_5(self):
        self.assertEqual(2, self.run_black_config('invalid', 'obccoioi'))

    def test_diversity_6(self):
        self.assertEqual(2, self.run_black_config('invalid', 'aqjtysqobw'))

    def test_diversity_7(self):
        self.assertEqual(2, self.run_black_config('invalid', 'lhzkgew'))

    def test_diversity_8(self):
        self.assertEqual(2, self.run_black_config('invalid', 'ggawkf'))

    def test_diversity_9(self):
        self.assertEqual(2, self.run_black_config('invalid', 'jhynuoqgi'))

    def test_diversity_10(self):
        self.assertEqual(2, self.run_black_config('invalid', 'rkelbxqw'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_black_config(kind, nonce=''):
        import os
        import tempfile
        from click.testing import CliRunner
        import black
        d = tempfile.mkdtemp()
        src = os.path.join(d, 's.py')
        with open(src, 'w') as f:
            f.write('x = 1\n')
        if kind == 'invalid':
            config = os.path.join(d, 'does_not_exist.toml')
        else:
            config = os.path.join(d, 'cfg.toml')
            with open(config, 'w') as f:
                f.write('')
        result = CliRunner().invoke(black.main, ['--config', config, '--check', src])
        return result.exit_code

    def test_diversity_1(self):
        self.assertEqual(0, self.run_black_config('valid', 'tthxhq'))

    def test_diversity_2(self):
        self.assertEqual(0, self.run_black_config('valid', 'lbhimy'))

    def test_diversity_3(self):
        self.assertEqual(0, self.run_black_config('valid', 'dgmscvgqj'))

    def test_diversity_4(self):
        self.assertEqual(0, self.run_black_config('valid', 'gncgqzcb'))

    def test_diversity_5(self):
        self.assertEqual(0, self.run_black_config('valid', 'ovmdufx'))

    def test_diversity_6(self):
        self.assertEqual(0, self.run_black_config('valid', 'gebhvim'))

    def test_diversity_7(self):
        self.assertEqual(0, self.run_black_config('valid', 'rcsrtkxahq'))

    def test_diversity_8(self):
        self.assertEqual(0, self.run_black_config('valid', 'pxxuuexm'))

    def test_diversity_9(self):
        self.assertEqual(0, self.run_black_config('valid', 'auxarxrfq'))

    def test_diversity_10(self):
        self.assertEqual(0, self.run_black_config('valid', 'zpkunxo'))
