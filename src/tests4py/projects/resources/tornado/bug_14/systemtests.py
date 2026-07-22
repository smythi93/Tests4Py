from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'DEFAULT_THEN_TRUE toyb'

    def test_diversity_2(self):
        return 'SINGLE_TRUE enig'

    def test_diversity_3(self):
        return 'DEFAULT_THEN_TRUE brlncjrc'

    def test_diversity_4(self):
        return 'DEFAULT_THEN_TRUE wwcrljv'

    def test_diversity_5(self):
        return 'SINGLE_TRUE cacqiac'

    def test_diversity_6(self):
        return 'SINGLE_TRUE rkdq'

    def test_diversity_7(self):
        return 'SINGLE_TRUE atpr'

    def test_diversity_8(self):
        return 'SINGLE_TRUE bqfeil'

    def test_diversity_9(self):
        return 'DEFAULT_THEN_TRUE jfvuth'

    def test_diversity_10(self):
        return 'SINGLE_TRUE syztorbj'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'MC_FALSE blsivhr'

    def test_diversity_2(self):
        return 'MC_FALSE yspylptn'

    def test_diversity_3(self):
        return 'DEFAULT mplsyky'

    def test_diversity_4(self):
        return 'DEFAULT xdconqy'

    def test_diversity_5(self):
        return 'MC_FALSE fqqdprrq'

    def test_diversity_6(self):
        return 'MC_FALSE cadpcn'

    def test_diversity_7(self):
        return 'DEFAULT ovrvu'

    def test_diversity_8(self):
        return 'DOUBLE_DEFAULT gwdyl'

    def test_diversity_9(self):
        return 'DEFAULT qzqvcxi'

    def test_diversity_10(self):
        return 'DEFAULT okme'
