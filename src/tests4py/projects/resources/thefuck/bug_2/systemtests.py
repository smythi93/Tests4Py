from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'Zq9qrMYME3voTHcrL5'

    def test_diversity_2(self):
        return 'Zq9hZYLWwH4Ep'

    def test_diversity_3(self):
        return 'Zq9nXRUi8wdK'

    def test_diversity_4(self):
        return 'Zq99LBjMimD8iMrGrru'

    def test_diversity_5(self):
        return 'Zq9b8rOaJAA5NgM'

    def test_diversity_6(self):
        return 'Zq9JMwcyCfca'

    def test_diversity_7(self):
        return 'Zq9NDA8MT9UZs8mMog'

    def test_diversity_8(self):
        return 'Zq9PBM6u0cE9MhksIG'

    def test_diversity_9(self):
        return 'Zq94c1pq1gAa9'

    def test_diversity_10(self):
        return 'Zq98NKPiWHh9rgT1'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nohup'

    def test_diversity_2(self):
        return 'cvfsdb'

    def test_diversity_3(self):
        return 'shasum5.34'

    def test_diversity_4(self):
        return 'avmediainfo'

    def test_diversity_5(self):
        return 'expand'

    def test_diversity_6(self):
        return 'fstyp_msdos'

    def test_diversity_7(self):
        return 'lockf'

    def test_diversity_8(self):
        return 'graphicssession'

    def test_diversity_9(self):
        return 'col'

    def test_diversity_10(self):
        return 'usdtree'
