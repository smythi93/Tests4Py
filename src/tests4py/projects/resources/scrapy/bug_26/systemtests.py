from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'override 5 58 418 818'

    def test_diversity_2(self):
        return 'override 2 968 182 657'

    def test_diversity_3(self):
        return 'override 6 117 927 691'

    def test_diversity_4(self):
        return 'override 1 875 191 601'

    def test_diversity_5(self):
        return 'override 1 499 298 421'

    def test_diversity_6(self):
        return 'override 4 411 673 966'

    def test_diversity_7(self):
        return 'override 7 457 939 175'

    def test_diversity_8(self):
        return 'override 8 7 117 545'

    def test_diversity_9(self):
        return 'override 3 449 240 768'

    def test_diversity_10(self):
        return 'override 5 603 641 838'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'clean 4 575 346 446'

    def test_diversity_2(self):
        return 'clean 4 869 613 488'

    def test_diversity_3(self):
        return 'clean 4 304 240 897'

    def test_diversity_4(self):
        return 'clean 6 435 400 111'

    def test_diversity_5(self):
        return 'clean 2 799 344 263'

    def test_diversity_6(self):
        return 'clean 4 200 353 251'

    def test_diversity_7(self):
        return 'clean 2 751 315 405'

    def test_diversity_8(self):
        return 'clean 8 703 383 674'

    def test_diversity_9(self):
        return 'clean 7 867 113 307'

    def test_diversity_10(self):
        return 'clean 8 997 573 99'
