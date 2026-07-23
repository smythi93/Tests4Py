import unittest
from thefuck.types import CorrectedCommand


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, CorrectedCommand('ubogcrkgs', 'dnjzyez', 1) == CorrectedCommand('ubogcrkgs', 'dnjzyez', 2))

    def test_diversity_2(self):
        self.assertEqual(True, CorrectedCommand('ujzzyzu', 'lkwtcozzi', 1) == CorrectedCommand('ujzzyzu', 'lkwtcozzi', 2))

    def test_diversity_3(self):
        self.assertEqual(True, CorrectedCommand('zgxthrzgwi', 'hmbxmqhj', 1) == CorrectedCommand('zgxthrzgwi', 'hmbxmqhj', 2))

    def test_diversity_4(self):
        self.assertEqual(True, CorrectedCommand('gihzekpvb', 'dmohflhdh', 1) == CorrectedCommand('gihzekpvb', 'dmohflhdh', 2))

    def test_diversity_5(self):
        self.assertEqual(True, CorrectedCommand('hixjuk', 'yyyes', 1) == CorrectedCommand('hixjuk', 'yyyes', 2))

    def test_diversity_6(self):
        self.assertEqual(True, CorrectedCommand('uibcunrh', 'ptetlrrkss', 1) == CorrectedCommand('uibcunrh', 'ptetlrrkss', 2))

    def test_diversity_7(self):
        self.assertEqual(True, CorrectedCommand('qdezhtmb', 'emypbpqo', 1) == CorrectedCommand('qdezhtmb', 'emypbpqo', 2))

    def test_diversity_8(self):
        self.assertEqual(True, CorrectedCommand('ezndfzdyjz', 'areoybqhg', 1) == CorrectedCommand('ezndfzdyjz', 'areoybqhg', 2))

    def test_diversity_9(self):
        self.assertEqual(True, CorrectedCommand('phvkdihx', 'lqggv', 1) == CorrectedCommand('phvkdihx', 'lqggv', 2))

    def test_diversity_10(self):
        self.assertEqual(True, CorrectedCommand('alwrajnnhe', 'kwwtclb', 1) == CorrectedCommand('alwrajnnhe', 'kwwtclb', 2))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, CorrectedCommand('slmajhtw', 'dlrncxm', 5) == CorrectedCommand('slmajhtw', 'dlrncxm', 5))

    def test_diversity_2(self):
        self.assertEqual(True, CorrectedCommand('xfhhoiey', 'jivuswn', 5) == CorrectedCommand('xfhhoiey', 'jivuswn', 5))

    def test_diversity_3(self):
        self.assertEqual(True, CorrectedCommand('zsojvtihha', 'ezxreimio', 5) == CorrectedCommand('zsojvtihha', 'ezxreimio', 5))

    def test_diversity_4(self):
        self.assertEqual(True, CorrectedCommand('yqtyk', 'dvpypqjym', 5) == CorrectedCommand('yqtyk', 'dvpypqjym', 5))

    def test_diversity_5(self):
        self.assertEqual(True, CorrectedCommand('mijnzmpx', 'xrlwtd', 5) == CorrectedCommand('mijnzmpx', 'xrlwtd', 5))

    def test_diversity_6(self):
        self.assertEqual(True, CorrectedCommand('sldnoocajm', 'mgwcmckrf', 5) == CorrectedCommand('sldnoocajm', 'mgwcmckrf', 5))

    def test_diversity_7(self):
        self.assertEqual(True, CorrectedCommand('rclybuqcnn', 'pjvwflu', 5) == CorrectedCommand('rclybuqcnn', 'pjvwflu', 5))

    def test_diversity_8(self):
        self.assertEqual(True, CorrectedCommand('cjmjaviat', 'dcshskfhn', 5) == CorrectedCommand('cjmjaviat', 'dcshskfhn', 5))

    def test_diversity_9(self):
        self.assertEqual(True, CorrectedCommand('bmbgl', 'xjbfx', 5) == CorrectedCommand('bmbgl', 'xjbfx', 5))

    def test_diversity_10(self):
        self.assertEqual(True, CorrectedCommand('nxfpgz', 'ulmegcw', 5) == CorrectedCommand('nxfpgz', 'ulmegcw', 5))
