from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'True PHP -s 127.0.0.0:2068'

    def test_diversity_2(self):
        return 'True PHP -s 127.1.0.1:458'

    def test_diversity_3(self):
        return 'True PHP -s localhost:2040'

    def test_diversity_4(self):
        return 'True php -S localhost:4965 router.php'

    def test_diversity_5(self):
        return 'True PHP -s localhost:4996 -t /path/to/your/project'

    def test_diversity_6(self):
        return 'True PHP -s 127.0.0.0:405'

    def test_diversity_7(self):
        return 'True php -S 127.0.1.0:2172'

    def test_diversity_8(self):
        return 'True php -S 127.0.1.0:3897'

    def test_diversity_9(self):
        return 'True PHP -s localhost:4393'

    def test_diversity_10(self):
        return 'True PHP -s localhost:3390'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'True php -s 127.1.1.1:1897'

    def test_diversity_2(self):
        return 'True php -s localhost:1363 -c /path/to/php.ini'

    def test_diversity_3(self):
        return 'True php -s 127.1.0.1:1957'

    def test_diversity_4(self):
        return 'True php -s localhost:3225 -c /path/to/php.ini'

    def test_diversity_5(self):
        return 'True php -s 127.1.1.1:1084'

    def test_diversity_6(self):
        return 'True php -s 127.1.1.1:3731'

    def test_diversity_7(self):
        return 'True php -s 127.0.1.0:2880'

    def test_diversity_8(self):
        return 'True php -s 127.1.1.1:2398'

    def test_diversity_9(self):
        return 'True php -s 127.0.1.0:2877'

    def test_diversity_10(self):
        return 'True php -s 127.1.0.1:3013'
