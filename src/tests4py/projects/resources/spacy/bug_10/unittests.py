import unittest
from spacy.errors import Errors



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'imokh'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_2(self):
        tag = 'bfebalz'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_3(self):
        tag = 'brssmdbg'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_4(self):
        tag = 'nlawykm'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_5(self):
        tag = 'azemt'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_6(self):
        tag = 'xntwqqgrap'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_7(self):
        tag = 'rtgmveevf'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_8(self):
        tag = 'qtvvz'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_9(self):
        tag = 'xzakrvw'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)

    def test_diversity_10(self):
        tag = 'hsocto'
        value = getattr(Errors, 'E171')
        self.assertTrue(value.startswith('[' + 'E171' + '] '))
        self.assertGreater(len(value), len('E171') + 3)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'ugyut'
        value = getattr(Errors, 'E017')
        self.assertTrue(value.startswith('[' + 'E017' + '] '))
        self.assertGreater(len(value), len('E017') + 3)

    def test_diversity_2(self):
        tag = 'awlvpsxe'
        value = getattr(Errors, 'E027')
        self.assertTrue(value.startswith('[' + 'E027' + '] '))
        self.assertGreater(len(value), len('E027') + 3)

    def test_diversity_3(self):
        tag = 'zygqrifha'
        value = getattr(Errors, 'E002')
        self.assertTrue(value.startswith('[' + 'E002' + '] '))
        self.assertGreater(len(value), len('E002') + 3)

    def test_diversity_4(self):
        tag = 'ugcpuk'
        value = getattr(Errors, 'E037')
        self.assertTrue(value.startswith('[' + 'E037' + '] '))
        self.assertGreater(len(value), len('E037') + 3)

    def test_diversity_5(self):
        tag = 'cjgfiympxd'
        value = getattr(Errors, 'E004')
        self.assertTrue(value.startswith('[' + 'E004' + '] '))
        self.assertGreater(len(value), len('E004') + 3)

    def test_diversity_6(self):
        tag = 'oldjmp'
        value = getattr(Errors, 'E013')
        self.assertTrue(value.startswith('[' + 'E013' + '] '))
        self.assertGreater(len(value), len('E013') + 3)

    def test_diversity_7(self):
        tag = 'dnmbercno'
        value = getattr(Errors, 'E022')
        self.assertTrue(value.startswith('[' + 'E022' + '] '))
        self.assertGreater(len(value), len('E022') + 3)

    def test_diversity_8(self):
        tag = 'onutnxcum'
        value = getattr(Errors, 'E004')
        self.assertTrue(value.startswith('[' + 'E004' + '] '))
        self.assertGreater(len(value), len('E004') + 3)

    def test_diversity_9(self):
        tag = 'bbdijajbk'
        value = getattr(Errors, 'E003')
        self.assertTrue(value.startswith('[' + 'E003' + '] '))
        self.assertGreater(len(value), len('E003') + 3)

    def test_diversity_10(self):
        tag = 'smrehaue'
        value = getattr(Errors, 'E023')
        self.assertTrue(value.startswith('[' + 'E023' + '] '))
        self.assertGreater(len(value), len('E023') + 3)
