from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'flat 107 648 251 674 425'

    def test_diversity_2(self):
        return 'flat 185 373 197'

    def test_diversity_3(self):
        return 'flat 558 668 850 446 560 920'

    def test_diversity_4(self):
        return 'flat 566 125 33 212 429 643'

    def test_diversity_5(self):
        return 'flat 942 666 780 101 788 647'

    def test_diversity_6(self):
        return 'flat 481'

    def test_diversity_7(self):
        return 'flat 887 575 543'

    def test_diversity_8(self):
        return 'flat 266'

    def test_diversity_9(self):
        return 'flat 810 631 238 686 420 361'

    def test_diversity_10(self):
        return 'flat 854 498 335 749'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nested 947 151'

    def test_diversity_2(self):
        return 'nested 183 522'

    def test_diversity_3(self):
        return 'nested 883 599 971 297'

    def test_diversity_4(self):
        return 'nested 282 905 606 101 86 959'

    def test_diversity_5(self):
        return 'nested 701 152 410 413 572 642 164 85'

    def test_diversity_6(self):
        return 'nested 932 87 220 286 791 217'

    def test_diversity_7(self):
        return 'nested 422 956 403 646 96 681'

    def test_diversity_8(self):
        return 'nested 912 406 186 13'

    def test_diversity_9(self):
        return 'nested 178 233 729 480'

    def test_diversity_10(self):
        return 'nested 873 657 67 285 998 967'
