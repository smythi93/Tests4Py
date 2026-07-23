from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'ppc64 6'

    def test_diversity_2(self):
        return 'ppc 3'

    def test_diversity_3(self):
        return 'ppc64le 3'

    def test_diversity_4(self):
        return 'ppc 5'

    def test_diversity_5(self):
        return 'ppc64le 2'

    def test_diversity_6(self):
        return 'ppc 7'

    def test_diversity_7(self):
        return 'ppc64le 8'

    def test_diversity_8(self):
        return 'ppc64 4'

    def test_diversity_9(self):
        return 'ppc64 3'

    def test_diversity_10(self):
        return 'ppc 6'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'x86_64 8'

    def test_diversity_2(self):
        return 'x86_64 3'

    def test_diversity_3(self):
        return 'amd64 3'

    def test_diversity_4(self):
        return 'amd64 8'

    def test_diversity_5(self):
        return 'amd64 4'

    def test_diversity_6(self):
        return 'i386 7'

    def test_diversity_7(self):
        return 'x86_64 4'

    def test_diversity_8(self):
        return 'x86_64 6'

    def test_diversity_9(self):
        return 'amd64 2'

    def test_diversity_10(self):
        return 'i386 5'
