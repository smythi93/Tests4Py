import unittest
from thefuck.types import Command
from thefuck.rules.php_s import match


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            True, match(Command("PHP -s localhost:4902 -t /path/to/your/project", ""))
        )

    def test_diversity_2(self):
        self.assertEqual(
            True, match(Command("php -S localhost:1231 -c /path/to/php.ini", ""))
        )

    def test_diversity_3(self):
        self.assertEqual(True, match(Command("PHP -s 127.1.0.1:4511", "")))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command("php -S localhost:2610 router.php", "")))

    def test_diversity_5(self):
        self.assertEqual(
            True, match(Command("php -S localhost:433 -c /path/to/php.ini", ""))
        )

    def test_diversity_6(self):
        self.assertEqual(True, match(Command("PHP -s 127.1.0.1:1745", "")))

    def test_diversity_7(self):
        self.assertEqual(
            True, match(Command("PHP -s localhost:42 -c /path/to/php.ini", ""))
        )

    def test_diversity_8(self):
        self.assertEqual(
            True, match(Command("php -S localhost:55 -c /path/to/php.ini", ""))
        )

    def test_diversity_9(self):
        self.assertEqual(True, match(Command("php -S localhost:1026 router.php", "")))

    def test_diversity_10(self):
        self.assertEqual(
            True, match(Command("php -S localhost:1174 -c /path/to/php.ini", ""))
        )


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            True, match(Command("php -s localhost:4000 -t /path/to/your/project", ""))
        )

    def test_diversity_2(self):
        self.assertEqual(
            True, match(Command("php -s localhost:4469 -t /path/to/your/project", ""))
        )

    def test_diversity_3(self):
        self.assertEqual(True, match(Command("php -s localhost:1002", "")))

    def test_diversity_4(self):
        self.assertEqual(
            True, match(Command("php -s localhost:3047 -c /path/to/php.ini", ""))
        )

    def test_diversity_5(self):
        self.assertEqual(True, match(Command("php -s 127.0.1.0:1544", "")))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command("php -s 127.0.1.0:4451", "")))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command("php -s localhost:1232 router.php", "")))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command("php -s 127.0.1.0:685", "")))

    def test_diversity_9(self):
        self.assertEqual(
            True, match(Command("php -s localhost:3465 -t /path/to/your/project", ""))
        )

    def test_diversity_10(self):
        self.assertEqual(
            True, match(Command("php -s localhost:2131 -t /path/to/your/project", ""))
        )
