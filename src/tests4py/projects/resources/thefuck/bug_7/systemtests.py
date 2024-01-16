from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "PHP -s localhost:4902 -t /path/to/your/project"

    def test_diversity_2(self):
        return "PHP -s localhost:2049 -t /path/to/your/project"

    def test_diversity_3(self):
        return "php -S localhost:1231 -c /path/to/php.ini"

    def test_diversity_4(self):
        return "php -S localhost:3112 -c /path/to/php.ini"

    def test_diversity_5(self):
        return "php -S localhost:1026 router.php"

    def test_diversity_6(self):
        return "php -S localhost:2610 router.php"

    def test_diversity_7(self):
        return "PHP -s 127.1.0.1:1019"

    def test_diversity_8(self):
        return "PHP -s 127.1.0.1:918"

    def test_diversity_9(self):
        return "PHP -s 127.1.0.1:817"

    def test_diversity_10(self):
        return "php -S localhost:400 -c /path/to/php.ini"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "php -s localhost:54 -t /path/to/your/project"

    def test_diversity_2(self):
        return "php -s localhost:1231 -t /path/to/your/project"

    def test_diversity_3(self):
        return "php -s localhost:812"

    def test_diversity_4(self):
        return "php -s localhost:1299 router.php"

    def test_diversity_5(self):
        return "php -s localhost:1002"

    def test_diversity_6(self):
        return "php -s localhost:2222 -c /path/to/php.ini"

    def test_diversity_7(self):
        return "php -s localhost:230"

    def test_diversity_8(self):
        return "php -s localhost:676 -c /path/to/php.ini"

    def test_diversity_9(self):
        return "php -s localhost:987 router.php"

    def test_diversity_10(self):
        return "php -s localhost:66 -t /path/to/your/project"
