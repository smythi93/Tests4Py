from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'default 37647 88964'

    def test_diversity_2(self):
        return 'default 26718 30087'

    def test_diversity_3(self):
        return 'default 27482 16439'

    def test_diversity_4(self):
        return 'default 42964 18569'

    def test_diversity_5(self):
        return 'default 26752 49469'

    def test_diversity_6(self):
        return 'default 98097 17181'

    def test_diversity_7(self):
        return 'default 44511 75220'

    def test_diversity_8(self):
        return 'default 63452 89131'

    def test_diversity_9(self):
        return 'default 71365 2685'

    def test_diversity_10(self):
        return 'default 94277 21723'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'explicit 11850 45969 47086'

    def test_diversity_2(self):
        return 'explicit 87224 62937 89254'

    def test_diversity_3(self):
        return 'explicit 61324 87109 24333'

    def test_diversity_4(self):
        return 'explicit 18117 75630 20729'

    def test_diversity_5(self):
        return 'explicit 55009 71463 59497'

    def test_diversity_6(self):
        return 'explicit 9446 91589 8317'

    def test_diversity_7(self):
        return 'explicit 6711 37001 67715'

    def test_diversity_8(self):
        return 'explicit 4603 28708 60744'

    def test_diversity_9(self):
        return 'explicit 7183 92531 28155'

    def test_diversity_10(self):
        return 'explicit 82918 14685 85754'
