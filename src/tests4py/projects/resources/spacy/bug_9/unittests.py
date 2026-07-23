import unittest
from spacy.errors import Warnings



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'epgwh'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_2(self):
        tag = 'geufzt'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_3(self):
        tag = 'uwdeeo'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_4(self):
        tag = 'ugny'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_5(self):
        tag = 'irmzrus'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_6(self):
        tag = 'nsoawvlsxg'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_7(self):
        tag = 'yahsmvitv'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_8(self):
        tag = 'cuyqfdcjy'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_9(self):
        tag = 'kubgp'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)

    def test_diversity_10(self):
        tag = 'qdsvlgbo'
        value = getattr(Warnings, 'W022')
        self.assertTrue(value.startswith('[' + 'W022' + '] '))
        self.assertGreater(len(value), len('W022') + 3)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'ekunkkq'
        value = getattr(Warnings, 'W005')
        self.assertTrue(value.startswith('[' + 'W005' + '] '))
        self.assertGreater(len(value), len('W005') + 3)

    def test_diversity_2(self):
        tag = 'crjxh'
        value = getattr(Warnings, 'W017')
        self.assertTrue(value.startswith('[' + 'W017' + '] '))
        self.assertGreater(len(value), len('W017') + 3)

    def test_diversity_3(self):
        tag = 'nfkjuxc'
        value = getattr(Warnings, 'W006')
        self.assertTrue(value.startswith('[' + 'W006' + '] '))
        self.assertGreater(len(value), len('W006') + 3)

    def test_diversity_4(self):
        tag = 'sshjnb'
        value = getattr(Warnings, 'W006')
        self.assertTrue(value.startswith('[' + 'W006' + '] '))
        self.assertGreater(len(value), len('W006') + 3)

    def test_diversity_5(self):
        tag = 'dmwjthxikj'
        value = getattr(Warnings, 'W003')
        self.assertTrue(value.startswith('[' + 'W003' + '] '))
        self.assertGreater(len(value), len('W003') + 3)

    def test_diversity_6(self):
        tag = 'mzlvgt'
        value = getattr(Warnings, 'W002')
        self.assertTrue(value.startswith('[' + 'W002' + '] '))
        self.assertGreater(len(value), len('W002') + 3)

    def test_diversity_7(self):
        tag = 'ltokexh'
        value = getattr(Warnings, 'W002')
        self.assertTrue(value.startswith('[' + 'W002' + '] '))
        self.assertGreater(len(value), len('W002') + 3)

    def test_diversity_8(self):
        tag = 'flfgskks'
        value = getattr(Warnings, 'W004')
        self.assertTrue(value.startswith('[' + 'W004' + '] '))
        self.assertGreater(len(value), len('W004') + 3)

    def test_diversity_9(self):
        tag = 'qijtn'
        value = getattr(Warnings, 'W008')
        self.assertTrue(value.startswith('[' + 'W008' + '] '))
        self.assertGreater(len(value), len('W008') + 3)

    def test_diversity_10(self):
        tag = 'fovae'
        value = getattr(Warnings, 'W002')
        self.assertTrue(value.startswith('[' + 'W002' + '] '))
        self.assertGreater(len(value), len('W002') + 3)
