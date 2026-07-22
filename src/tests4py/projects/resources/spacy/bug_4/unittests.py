import unittest
from spacy.cli.converters.conllu2json import read_conllx



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t_\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t5\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t1\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_2(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t0\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t5\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t0\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t_\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_3(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t5\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t_\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t0\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_4(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t_\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t3\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_5(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t0\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t_\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_6(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t_\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t0\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_7(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t_\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t0\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_8(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t_\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_9(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t_\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t3\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_10(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t5\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t_\tdep\t_\t_\n6\tw5\t_\tNOUN\tNN\t_\t5\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t2\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_2(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t0\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_3(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t0\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t0\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t5\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t5\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t5\tdep\t_\t_\n6\tw5\t_\tNOUN\tNN\t_\t5\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_4(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t2\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_5(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t1\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_6(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t6\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t6\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t0\tdep\t_\t_\n6\tw5\t_\tNOUN\tNN\t_\t3\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_7(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t2\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_8(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t1\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t0\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_9(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t3\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t0\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))

    def test_diversity_10(self):
        text = '1\tw0\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n2\tw1\t_\tNOUN\tNN\t_\t0\tdep\t_\t_\n3\tw2\t_\tNOUN\tNN\t_\t2\tdep\t_\t_\n4\tw3\t_\tNOUN\tNN\t_\t4\tdep\t_\t_\n5\tw4\t_\tNOUN\tNN\t_\t5\tdep\t_\t_'
        result = list(read_conllx(text))
        self.assertEqual(1, len(result))
