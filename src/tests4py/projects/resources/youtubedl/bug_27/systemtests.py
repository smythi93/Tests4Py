from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'value 07:07:00:093'

    def test_diversity_2(self):
        return 'value 09:02:42:710'

    def test_diversity_3(self):
        return 'value 01:06:49:364'

    def test_diversity_4(self):
        return 'value 03:01:01:808'

    def test_diversity_5(self):
        return 'value 00:22:41:639'

    def test_diversity_6(self):
        return 'value 07:39:29:153'

    def test_diversity_7(self):
        return 'value 01:11:45:118'

    def test_diversity_8(self):
        return 'value 00:32:31:902'

    def test_diversity_9(self):
        return 'value 03:04:42:555'

    def test_diversity_10(self):
        return 'value 07:04:38:692'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'value 527.9'

    def test_diversity_2(self):
        return 'value 276.8'

    def test_diversity_3(self):
        return 'value 309.7'

    def test_diversity_4(self):
        return 'value 272'

    def test_diversity_5(self):
        return 'value 464.8s'

    def test_diversity_6(self):
        return 'value 520.1'

    def test_diversity_7(self):
        return 'value 341.2'

    def test_diversity_8(self):
        return 'value 06:10:03'

    def test_diversity_9(self):
        return 'value 508.2'

    def test_diversity_10(self):
        return 'value 570.3'
