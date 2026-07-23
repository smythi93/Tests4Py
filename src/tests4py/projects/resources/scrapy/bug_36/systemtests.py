from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'none from_crawler 96035'

    def test_diversity_2(self):
        return 'none from_crawler 25384'

    def test_diversity_3(self):
        return 'none from_crawler 21193'

    def test_diversity_4(self):
        return 'none from_crawler 34222'

    def test_diversity_5(self):
        return 'none from_settings 46518'

    def test_diversity_6(self):
        return 'none from_crawler 76684'

    def test_diversity_7(self):
        return 'none from_settings 94237'

    def test_diversity_8(self):
        return 'none from_crawler 42211'

    def test_diversity_9(self):
        return 'none from_crawler 3522'

    def test_diversity_10(self):
        return 'none from_settings 87019'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'ok from_settings 39144'

    def test_diversity_2(self):
        return 'ok from_crawler 74188'

    def test_diversity_3(self):
        return 'ok from_crawler 16288'

    def test_diversity_4(self):
        return 'ok from_settings 80186'

    def test_diversity_5(self):
        return 'ok from_settings 69605'

    def test_diversity_6(self):
        return 'ok from_settings 19418'

    def test_diversity_7(self):
        return 'ok from_settings 24900'

    def test_diversity_8(self):
        return 'ok from_settings 60141'

    def test_diversity_9(self):
        return 'ok from_crawler 453'

    def test_diversity_10(self):
        return 'ok from_settings 76037'
