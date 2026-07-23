import unittest
from httpie import cli

def run_parse(item):
    kt = cli.KeyValueType(cli.SEP_HEADERS, cli.SEP_DATA, cli.SEP_DATA_RAW_JSON, cli.SEP_FILES)
    kv = kt(item)
    return (kv.key, kv.value, kv.sep)

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(('spv:=', 'wiostoy', '='), run_parse('spv\\:==wiostoy'))

    def test_diversity_2(self):
        self.assertEqual(('swua:=', 'ubnb', ':'), run_parse('swua\\:=:ubnb'))

    def test_diversity_3(self):
        self.assertEqual(('pfezuk:=', 'kjfescam', '@'), run_parse('pfezuk\\:=@kjfescam'))

    def test_diversity_4(self):
        self.assertEqual(('gxjgwdcj:=', 'khc', ':'), run_parse('gxjgwdcj\\:=:khc'))

    def test_diversity_5(self):
        self.assertEqual(('cceo:=', 'xaxprac', ':'), run_parse('cceo\\:=:xaxprac'))

    def test_diversity_6(self):
        self.assertEqual(('yogm:=', 'zsenonnn', '='), run_parse('yogm\\:==zsenonnn'))

    def test_diversity_7(self):
        self.assertEqual(('uujgv:=', 'kmqvlkua', ':'), run_parse('uujgv\\:=:kmqvlkua'))

    def test_diversity_8(self):
        self.assertEqual(('sfqvspsa:=', 'mqez', ':'), run_parse('sfqvspsa\\:=:mqez'))

    def test_diversity_9(self):
        self.assertEqual(('vrs:=', 'ucxva', ':'), run_parse('vrs\\:=:ucxva'))

    def test_diversity_10(self):
        self.assertEqual(('vbpirg:=', 'pqdl', ':'), run_parse('vbpirg\\:=:pqdl'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(('hcptl:oevdqo', 'oevdqo', ':'), run_parse('hcptl\\:oevdqo:oevdqo'))

    def test_diversity_2(self):
        self.assertEqual(('wvss=ezmbzm', 'ezmbzm', '='), run_parse('wvss\\=ezmbzm=ezmbzm'))

    def test_diversity_3(self):
        self.assertEqual(('lks', 'nrjdkrr', '='), run_parse('lks=nrjdkrr'))

    def test_diversity_4(self):
        self.assertEqual(('ggcunm', 'ppigfns', '='), run_parse('ggcunm=ppigfns'))

    def test_diversity_5(self):
        self.assertEqual(('yuogx', 'ldpws', '='), run_parse('yuogx=ldpws'))

    def test_diversity_6(self):
        self.assertEqual(('vwyatjj', 'yfz', ':'), run_parse('vwyatjj:yfz'))

    def test_diversity_7(self):
        self.assertEqual(('edcbc', 'ieefbm', '='), run_parse('edcbc=ieefbm'))

    def test_diversity_8(self):
        self.assertEqual(('alne:fsna', 'fsna', ':'), run_parse('alne\\:fsna:fsna'))

    def test_diversity_9(self):
        self.assertEqual(('modfe:irvkccv', 'irvkccv', ':'), run_parse('modfe\\:irvkccv:irvkccv'))

    def test_diversity_10(self):
        self.assertEqual(('lunb', 'kgfpq', ':'), run_parse('lunb:kgfpq'))