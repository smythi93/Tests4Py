from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'total_dis 153'

    def test_diversity_2(self):
        return 'total_dis 263'

    def test_diversity_3(self):
        return 'total_dis 864'

    def test_diversity_4(self):
        return 'total_dis 306'

    def test_diversity_5(self):
        return 'total_dis 287'

    def test_diversity_6(self):
        return 'total_dis 346'

    def test_diversity_7(self):
        return 'total_dis 718'

    def test_diversity_8(self):
        return 'total_dis 481'

    def test_diversity_9(self):
        return 'total_dis 300'

    def test_diversity_10(self):
        return 'total_dis 546'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'range_dis 61'

    def test_diversity_2(self):
        return 'range_dis 982'

    def test_diversity_3(self):
        return 'range_dis 607'

    def test_diversity_4(self):
        return 'list_dis 764'

    def test_diversity_5(self):
        return 'range_dis 991'

    def test_diversity_6(self):
        return 'range_dis 255'

    def test_diversity_7(self):
        return 'list_dis 20'

    def test_diversity_8(self):
        return 'range_dis 287'

    def test_diversity_9(self):
        return 'list_dis 218'

    def test_diversity_10(self):
        return 'list_dis 781'

