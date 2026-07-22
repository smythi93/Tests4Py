import unittest
from thefuck.rules.no_command import match
from thefuck.types import Command

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):self.assertEqual(False, match(Command('headd qiEWcOorMV', '', 'headd: not found')))

    def test_diversity_2(self):self.assertEqual(False, match(Command('lss wTFYWmSEgFacUh', '', 'lss: not found')))

    def test_diversity_3(self):self.assertEqual(False, match(Command('catt XZDfheuy', '', 'catt: not found')))

    def test_diversity_4(self):self.assertEqual(False, match(Command('uniqq WRpkgvy', '', 'uniqq: not found')))

    def test_diversity_5(self):self.assertEqual(False, match(Command('gitt crPPQ', '', 'gitt: not found')))

    def test_diversity_6(self):self.assertEqual(False, match(Command('wcc zlnAIxLOJSbzYBq', '', 'wcc: not found')))

    def test_diversity_7(self):self.assertEqual(False, match(Command('wcc xrshsxfyR', '', 'wcc: not found')))

    def test_diversity_8(self):self.assertEqual(False, match(Command('pwdd HneNWX', '', 'pwdd: not found')))

    def test_diversity_9(self):self.assertEqual(False, match(Command('envv EYKlLWRQtMjEZ', '', 'envv: not found')))

    def test_diversity_10(self):self.assertEqual(False, match(Command('envv EYjhlJRJjjuO', '', 'envv: not found')))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):self.assertEqual(True, match(Command('rmm oSBUKn', '', 'rmm: not found')))

    def test_diversity_2(self):self.assertEqual(True, match(Command('pwdd fQlsqLOyGgip', '', 'pwdd: not found')))

    def test_diversity_3(self):self.assertEqual(True, match(Command('envv jSYWcobaydzzo', '', 'envv: not found')))

    def test_diversity_4(self):self.assertEqual(True, match(Command('datee QwrpdIBCJMRwjy', '', 'datee: not found')))

    def test_diversity_5(self):self.assertEqual(True, match(Command('lss finEVRUlahPt', '', 'lss: not found')))

    def test_diversity_6(self):self.assertEqual(True, match(Command('pwdd iAEDgrPEYf', '', 'pwdd: not found')))

    def test_diversity_7(self):self.assertEqual(True, match(Command('catt DerUH', '', 'catt: not found')))

    def test_diversity_8(self):self.assertEqual(True, match(Command('grepp XJyWlT', '', 'grepp: not found')))

    def test_diversity_9(self):self.assertEqual(True, match(Command('gitt YMKIM', '', 'gitt: not found')))

    def test_diversity_10(self):self.assertEqual(True, match(Command('wcc KLSqD', '', 'wcc: not found')))