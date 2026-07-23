from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'topk 6316 8 6 4'

    def test_diversity_2(self):
        return 'topk 3245 4 8 4'

    def test_diversity_3(self):
        return 'topk 920 6 6 4'

    def test_diversity_4(self):
        return 'topk 591 7 5 2'

    def test_diversity_5(self):
        return 'topk 3890 6 8 5'

    def test_diversity_6(self):
        return 'topk 8568 4 6 3'

    def test_diversity_7(self):
        return 'topk 7800 4 6 4'

    def test_diversity_8(self):
        return 'topk 602 7 4 2'

    def test_diversity_9(self):
        return 'topk 7322 6 6 3'

    def test_diversity_10(self):
        return 'topk 751 4 8 7'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'greater 1636 3 6 3'

    def test_diversity_2(self):
        return 'greater 190 4 4 1'

    def test_diversity_3(self):
        return 'greater 2044 5 4 1'

    def test_diversity_4(self):
        return 'greater 3244 6 4 2'

    def test_diversity_5(self):
        return 'greater 5745 4 5 3'

    def test_diversity_6(self):
        return 'greater 5511 6 4 2'

    def test_diversity_7(self):
        return 'greater 940 7 4 2'

    def test_diversity_8(self):
        return 'greater 6414 7 7 3'

    def test_diversity_9(self):
        return 'greater 5725 6 4 1'

    def test_diversity_10(self):
        return 'greater 9104 5 5 1'
