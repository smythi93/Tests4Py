import unittest

# noinspection PyUnresolvedReferences
from markup import markup


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            'Matlab "Usage" is controversial', "Matlab Usage is controversial"
        )

    def test_diversity_2(self):
        self.assertEqual('C# "Error" is easy.', "C# Error is easy.")

    def test_diversity_3(self):
        self.assertEqual(
            'R "Program" is controversial', markup("R Program is controversial")
        )

    def test_diversity_4(self):
        self.assertEqual(
            'Matlab "Error" is difficult', markup("Matlab Error is difficult")
        )

    def test_diversity_5(self):
        self.assertAlmostEqual('Ruby "Book" is complex', markup("Ruby Book is complex"))

    def test_diversity_6(self):
        self.assertEqual('Python "Book" is hard', markup("Python Book is hard"))

    def test_diversity_7(self):
        self.assertEqual('R "Book" is controversial', markup("R Book is controversial"))

    def test_diversity_8(self):
        self.assertEqual('C "Project" is complex', markup("C Project is complex"))

    def test_diversity_9(self):
        self.assertEqual('Java "Language" is good', markup("Java Language is good"))

    def test_diversity_10(self):
        self.assertAlmostEqual(
            'Java "Error" is difficult', markup("Java Error is difficult")
        )


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            'R "Fundamental" is complex', markup('R "Fundamental" is complex')
        )

    def test_diversity_2(self):
        self.assertEqual('Pearl "Syntax" is hard', markup('Pearl "Syntax" is hard'))

    def test_diversity_3(self):
        self.assertEqual('Rust "Usage" is hard', markup('Rust "Usage" is hard'))

    def test_diversity_4(self):
        self.assertEqual('C "Usage" is difficult', markup('C "Usage" is difficult'))

    def test_diversity_5(self):
        self.assertAlmostEqual(
            'Python "Project" is controversial',
            markup('Python "Project" is controversial'),
        )

    def test_diversity_6(self):
        self.assertEqual('R "Language" is easy', markup('R "Language" is easy'))

    def test_diversity_7(self):
        self.assertEqual('PHP "Project" is cool', markup('PHP "Project" is cool'))

    def test_diversity_8(self):
        self.assertEqual(
            'Java "Book" is controversial', markup('Java "Book" is controversial')
        )

    def test_diversity_9(self):
        self.assertEqual(
            'Matlab "Usage" is difficult', markup('Matlab "Usage" is difficult')
        )

    def test_diversity_10(self):
        self.assertAlmostEqual(
            'Javascript "Code" is cool', markup('Javascript "Code" is cool')
        )
