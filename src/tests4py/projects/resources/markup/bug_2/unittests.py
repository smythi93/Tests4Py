import unittest

# noinspection PyUnresolvedReferences
from markup import markup


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            'Matlab "Usage" is controversial.',
            markup('<li>Matlab "Usage" is controversial.<li>'),
        )

    def test_diversity_2(self):
        self.assertEqual(
            'C# "Error" is easy.', markup('<audio>C# "Error" is easy.<audio>')
        )

    def test_diversity_3(self):
        self.assertEqual(
            'R "Program" is controversial.',
            markup('<aside>R "Program" is controversial.<aside>'),
        )

    def test_diversity_4(self):
        self.assertEqual(
            'Matlab "Error" is difficult.',
            markup('<datalist>Matlab "Error" is difficult.<datalist>'),
        )

    def test_diversity_5(self):
        self.assertAlmostEqual(
            'Ruby "Book" is complex.', markup('<img>Ruby "Book" is complex.<img>')
        )

    def test_diversity_6(self):
        self.assertEqual(
            'Python "Book" is hard.', markup('<footer>Python "Book" is hard.<footer>')
        )

    def test_diversity_7(self):
        self.assertEqual(
            'R "Book" is controversial.',
            markup('<article>R "Book" is controversial.<article>'),
        )

    def test_diversity_8(self):
        self.assertEqual(
            'C "Project" is complex.',
            markup('<section>C "Project" is complex.<section>'),
        )

    def test_diversity_9(self):
        self.assertEqual(
            'Java "Language" is good.', markup('<embed>Java "Language" is good.<embed>')
        )

    def test_diversity_10(self):
        self.assertAlmostEqual(
            'Java "Error" is difficult.',
            markup('<canvas>Java "Error" is difficult.<canvas>'),
        )


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            "R Fundamental is complex.",
            markup("<output>R 'Fundamental' is complex.<output>"),
        )

    def test_diversity_2(self):
        self.assertEqual(
            "Pearl 'Syntax' is hard.", markup("<video>Pearl 'Syntax' is hard.<video>")
        )

    def test_diversity_3(self):
        self.assertEqual(
            "Rust 'Usage' is hard.", markup("<datalist>Rust 'Usage' is hard.<datalist>")
        )

    def test_diversity_4(self):
        self.assertEqual(
            "C 'Usage' is difficult.", markup("<title>C 'Usage' is difficult.<title>")
        )

    def test_diversity_5(self):
        self.assertAlmostEqual(
            "Python 'Project' is controversial.",
            markup("<header>Python 'Project' is controversial.<header>"),
        )

    def test_diversity_6(self):
        self.assertEqual(
            'R "Language" is easy.', markup("<body>R 'Language' is easy.<body>")
        )

    def test_diversity_7(self):
        self.assertEqual(
            'PHP "Project" is cool.', markup("<search>PHP 'Project' is cool.<search>")
        )

    def test_diversity_8(self):
        self.assertEqual(
            "Java 'Book' is controversial.",
            markup("<ul>Java 'Book' is controversial.<ul>"),
        )

    def test_diversity_9(self):
        self.assertEqual(
            "Matlab 'Usage' is difficult.",
            markup("<hr>Matlab 'Usage' is difficult.<hr>"),
        )

    def test_diversity_10(self):
        self.assertAlmostEqual(
            'Javascript "Code" is cool.',
            markup("<head>Javascript 'Code' is cool.<head>"),
        )
