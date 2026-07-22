from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'hex 252048691'

    def test_diversity_2(self):
        return 'dec 195769762'

    def test_diversity_3(self):
        return 'dec 1443285705'

    def test_diversity_4(self):
        return 'dec 212473846'

    def test_diversity_5(self):
        return 'hex 509659236'

    def test_diversity_6(self):
        return 'dec 67286704'

    def test_diversity_7(self):
        return 'dec 744334505'

    def test_diversity_8(self):
        return 'hex 1323568254'

    def test_diversity_9(self):
        return 'hex 320132783'

    def test_diversity_10(self):
        return 'dec 394298273'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'dec 991'

    def test_diversity_2(self):
        return 'hex 16405'

    def test_diversity_3(self):
        return 'dec 43762'

    def test_diversity_4(self):
        return 'hex 4526'

    def test_diversity_5(self):
        return 'dec 33786'

    def test_diversity_6(self):
        return 'dec 17700'

    def test_diversity_7(self):
        return 'dec 42279'

    def test_diversity_8(self):
        return 'hex 31558'

    def test_diversity_9(self):
        return 'hex 17495'

    def test_diversity_10(self):
        return 'dec 42990'
