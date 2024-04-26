from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "123"

    def test_diversity_2(self):
        return "321"

    def test_diversity_3(self):
        return "65"

    def test_diversity_4(self):
        return "77"

    def test_diversity_5(self):
        return "232"

    def test_diversity_6(self):
        return "545"

    def test_diversity_7(self):
        return "2131"

    def test_diversity_8(self):
        return "5345"

    def test_diversity_9(self):
        return "3628"

    def test_diversity_10(self):
        return "544"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "akaskHJEi"

    def test_diversity_2(self):
        return "SAKjhkdui"

    def test_diversity_3(self):
        return "SDFJSDksd"

    def test_diversity_4(self):
        return "LWLAsere"

    def test_diversity_5(self):
        return "fweweSDER"

    def test_diversity_6(self):
        return "ASDseffa"

    def test_diversity_7(self):
        return "freferiIADIA"

    def test_diversity_8(self):
        return "SADAjhsadjJ"

    def test_diversity_9(self):
        return "ASDAKadkkAD"

    def test_diversity_10(self):
        return "ylQtOPVYFmC"
