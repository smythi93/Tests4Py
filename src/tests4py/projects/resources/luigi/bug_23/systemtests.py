from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'default 30358 39700'

    def test_diversity_2(self):
        return 'default 89257 88837'

    def test_diversity_3(self):
        return 'default 9090 36130'

    def test_diversity_4(self):
        return 'default 65929 27440'

    def test_diversity_5(self):
        return 'default 48751 28203'

    def test_diversity_6(self):
        return 'default 93145 8309'

    def test_diversity_7(self):
        return 'default 7560 98590'

    def test_diversity_8(self):
        return 'default 49923 72003'

    def test_diversity_9(self):
        return 'default 51029 32686'

    def test_diversity_10(self):
        return 'default 64596 2092'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'explicit 6983 91937 71146'

    def test_diversity_2(self):
        return 'explicit 99228 72737 71723'

    def test_diversity_3(self):
        return 'explicit 72563 14641 19062'

    def test_diversity_4(self):
        return 'explicit 87305 24516 9601'

    def test_diversity_5(self):
        return 'explicit 32350 71455 48208'

    def test_diversity_6(self):
        return 'explicit 18625 76096 9747'

    def test_diversity_7(self):
        return 'explicit 89224 88644 40629'

    def test_diversity_8(self):
        return 'explicit 30135 72866 28428'

    def test_diversity_9(self):
        return 'explicit 45409 96133 65414'

    def test_diversity_10(self):
        return 'explicit 12802 86899 71275'
