import unittest

# noinspection PyUnresolvedReferences
from markup import remove_html_markup


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            'Matlab "Usage" is controversial.',
            remove_html_markup('<li>Matlab "Usage" is controversial.<li>'),
        )

    def test_diversity_2(self):
        self.assertEqual(
            'C# "Error" is easy.',
            remove_html_markup('<audio>C# "Error" is easy.<audio>'),
        )

    def test_diversity_3(self):
        self.assertEqual(
            'R "Program" is controversial.',
            remove_html_markup('<aside>R "Program" is controversial.<aside>'),
        )

    def test_diversity_4(self):
        self.assertEqual(
            'Matlab "Error" is difficult.',
            remove_html_markup('<datalist>Matlab "Error" is difficult.<datalist>'),
        )

    def test_diversity_5(self):
        self.assertAlmostEqual(
            'Ruby "Book" is complex.',
            remove_html_markup('<img>Ruby "Book" is complex.<img>'),
        )

    def test_diversity_6(self):
        self.assertEqual(
            'Python "Book" is hard.',
            remove_html_markup('<footer>Python "Book" is hard.<footer>'),
        )

    def test_diversity_7(self):
        self.assertEqual(
            'R "Book" is controversial.',
            remove_html_markup('<article>R "Book" is controversial.<article>'),
        )

    def test_diversity_8(self):
        self.assertEqual(
            'C "Project" is complex.',
            remove_html_markup('<section>C "Project" is complex.<section>'),
        )

    def test_diversity_9(self):
        self.assertEqual(
            'Java "Language" is good.',
            remove_html_markup('<embed>Java "Language" is good.<embed>'),
        )

    def test_diversity_10(self):
        self.assertAlmostEqual(
            'Java "Error" is difficult.',
            remove_html_markup('<canvas>Java "Error" is difficult.<canvas>'),
        )


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            "R Fundamental is complex.",
            remove_html_markup("<output>R 'Fundamental' is complex.<output>"),
        )

    def test_diversity_2(self):
        self.assertEqual(
            "Pearl 'Syntax' is hard.",
            remove_html_markup("<video>Pearl 'Syntax' is hard.<video>"),
        )

    def test_diversity_3(self):
        self.assertEqual(
            "Rust 'Usage' is hard.",
            remove_html_markup("<datalist>Rust 'Usage' is hard.<datalist>"),
        )

    def test_diversity_4(self):
        self.assertEqual(
            "C 'Usage' is difficult.",
            remove_html_markup("<title>C 'Usage' is difficult.<title>"),
        )

    def test_diversity_5(self):
        self.assertAlmostEqual(
            "Python 'Project' is controversial.",
            remove_html_markup("<header>Python 'Project' is controversial.<header>"),
        )

    def test_diversity_6(self):
        self.assertEqual(
            'R "Language" is easy.',
            remove_html_markup("<body>R 'Language' is easy.<body>"),
        )

    def test_diversity_7(self):
        self.assertEqual(
            'PHP "Project" is cool.',
            remove_html_markup("<search>PHP 'Project' is cool.<search>"),
        )

    def test_diversity_8(self):
        self.assertEqual(
            "Java 'Book' is controversial.",
            remove_html_markup("<ul>Java 'Book' is controversial.<ul>"),
        )

    def test_diversity_9(self):
        self.assertEqual(
            "Matlab 'Usage' is difficult.",
            remove_html_markup("<hr>Matlab 'Usage' is difficult.<hr>"),
        )

    def test_diversity_10(self):
        self.assertAlmostEqual(
            'Javascript "Code" is cool.',
            remove_html_markup("<head>Javascript 'Code' is cool.<head>"),
        )
