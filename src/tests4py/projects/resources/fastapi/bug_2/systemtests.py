from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-ws / dep -os dep over -m websocket -u /"

    def test_diversity_2(self):
        return "-ws / dep -os dep over -ds dep2 -m websocket -u /"

    def test_diversity_3(self):
        return "-ws / dep -os dep over -ds dep2 -m websocket -d {} -u /"

    def test_diversity_4(self):
        return "-ws / dep -os dep over -ds dep2 -m websocket -d [] -u /"

    def test_diversity_5(self):
        return '-ws / dep -os dep over -ds dep2 -m websocket -d "[1,2,0.0,\\"test\\"]" -u /'

    def test_diversity_6(self):
        return '-ws / dep -os dep over -ds dep2 -m websocket -d "[1,2,0.0,\\"test\\"]" -u /'

    def test_diversity_7(self):
        return '-ws / dep -os dep over -ds dep2 -m websocket -d "{\\"d\\":1,\\"t\\":\\"test\\"}" -u /'

    def test_diversity_8(self):
        return '-os dep over -ds dep2 -m websocket -ws / dep -d "[1,2,0.0,\\"test\\"]" -u /'

    def test_diversity_9(self):
        return '-ws / dep -os dep over -ds dep2 -m websocket -d "\\"test\\"" -u /'

    def test_diversity_10(self):
        return "-ws /test dep2 -ws /test2 dep -os dep over -os dep2 over2 -m websocket -u /test"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-ws / dep -ds dep -m websocket -u /"

    def test_diversity_2(self):
        return "-ws /test dep -ds dep -m websocket -u /test"

    def test_diversity_3(self):
        return (
            "-ws /test dep2 -ws /test2 dep -os dep over -ds dep2 -m websocket -u /test"
        )

    def test_diversity_4(self):
        return "-ws / dep -ds dep -m websocket -u /"

    def test_diversity_5(self):
        return "-ws / dep -ds dep -m websocket -u /"

    def test_diversity_6(self):
        return "-ws / dep -ds dep -m websocket -u /"

    def test_diversity_7(self):
        return "-ws / dep -ds dep -m websocket -u /"

    def test_diversity_8(self):
        return "-gs /valid/ OtherItem -m get -u /valid/"

    def test_diversity_9(self):
        return "-gs /valid/ Item -a aliased_name -m get -u /valid/"

    def test_diversity_10(self):
        return "-gs /valid/ Item -m get -u /valid/"
