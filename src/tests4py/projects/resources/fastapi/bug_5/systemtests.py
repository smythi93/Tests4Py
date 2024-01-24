from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_2(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_3(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_4(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_5(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_6(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_7(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_8(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_9(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"

    def test_diversity_10(self):
        return "-gs /c ModelCA -u /c -m get -ma a pwd -mb b"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"

    def test_diversity_2(self):
        return "-gs /a ModelB -u /a -m get -ma a pwd -mb b"

    def test_diversity_3(self):
        return "-gs /b ModelA -u /b -m get -ma a pwd -mb b"

    def test_diversity_4(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"

    def test_diversity_5(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"

    def test_diversity_6(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"

    def test_diversity_7(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"

    def test_diversity_8(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"

    def test_diversity_9(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"

    def test_diversity_10(self):
        return "-gs /c ModelCB -u /c -m get -ma a pwd -mb b"
