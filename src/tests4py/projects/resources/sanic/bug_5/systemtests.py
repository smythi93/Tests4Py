from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'INFO ERROR nzuwz'

    def test_diversity_2(self):
        return 'DEBUG INFO zaofrhjd'

    def test_diversity_3(self):
        return 'CRITICAL WARNING apkggmc'

    def test_diversity_4(self):
        return 'CRITICAL WARNING nvvn'

    def test_diversity_5(self):
        return 'WARNING DEBUG hjbb'

    def test_diversity_6(self):
        return 'ERROR WARNING hoaxhja'

    def test_diversity_7(self):
        return 'ERROR DEBUG agdtnv'

    def test_diversity_8(self):
        return 'ERROR DEBUG ixpmssyy'

    def test_diversity_9(self):
        return 'ERROR INFO ztfi'

    def test_diversity_10(self):
        return 'WARNING DEBUG qllrlt'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'WARNING WARNING ymnkri'

    def test_diversity_2(self):
        return 'WARNING WARNING upsmruvp'

    def test_diversity_3(self):
        return 'CRITICAL CRITICAL xgvcrb'

    def test_diversity_4(self):
        return 'WARNING WARNING azni'

    def test_diversity_5(self):
        return 'CRITICAL CRITICAL lquqlxwn'

    def test_diversity_6(self):
        return 'CRITICAL CRITICAL vxtadz'

    def test_diversity_7(self):
        return 'ERROR ERROR bnnbgt'

    def test_diversity_8(self):
        return 'CRITICAL CRITICAL ktqmt'

    def test_diversity_9(self):
        return 'WARNING WARNING qpzwh'

    def test_diversity_10(self):
        return 'ERROR ERROR zflwpi'
