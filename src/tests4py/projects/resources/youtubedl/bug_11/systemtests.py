from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):

    def test_diversity_1(self):
        return "-i 523"

    def test_diversity_2(self):
        return '-i 123.456'

    def test_diversity_3(self):
        return '-i .1'

    def test_diversity_4(self):
        return '-i 100.1'

    def test_diversity_5(self):
        return '-i -100'

    def test_diversity_6(self):
        return '-i -5.5'

    def test_diversity_7(self):
        return '-i -123,4'

    def test_diversity_8(self):
        return '-i -123.3'

    def test_diversity_9(self):
        return '-i -0.1'

    def test_diversity_10(self):
        return '-i -1'



class TestsPassing(PassingSystemtests):

    def test_diversity_1(self):
        return '-s 123,456'

    def test_diversity_2(self):
        return '-s 123.456'

    def test_diversity_3(self):
        return '-s .1'

    def test_diversity_4(self):
        return '-s 100.1'

    def test_diversity_5(self):
        return '-s -100'

    def test_diversity_6(self):
        return '-s -5.5'

    def test_diversity_7(self):
        return '-s -123,4'

    def test_diversity_8(self):
        return '-s -123.3'

    def test_diversity_9(self):
        return '-s -0.1'

    def test_diversity_10(self):
        return '-s -1'
