from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_2(self):
        return '-ps /f FormSet -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_3(self):
        return '-ps /f FormTuple -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_4(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_5(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_6(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_7(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_8(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_9(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'

    def test_diversity_10(self):
        return '-ps /f FormList -u /f -m post -d {\\"items\\":[1,2,3]}'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '-ps /f FormInt[1] -u /f -m post -d {\\"items\\":1}'

    def test_diversity_2(self):
        return "-ps /f FormInt[1] -u /f -m post"

    def test_diversity_3(self):
        return "-gs /valid/ Item -m get -u /valid/"

    def test_diversity_4(self):
        return "-gs /valid/ Item -m get -u /valid/"

    def test_diversity_5(self):
        return "-gs /valid/ Item -m get -u /valid/"

    def test_diversity_6(self):
        return "-gs /valid/ Item -m get -u /valid/"

    def test_diversity_7(self):
        return "-gs /valid/ Item -m get -u /valid/"

    def test_diversity_8(self):
        return "-gs /valid/ Item -m get -u /valid/"

    def test_diversity_9(self):
        return "-gs /valid/ Item -m get -u /valid/"

    def test_diversity_10(self):
        return "-gs /valid/ Item -m get -u /valid/"
