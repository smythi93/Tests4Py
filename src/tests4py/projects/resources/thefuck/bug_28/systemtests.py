from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "'True' 'col' '366' '142'"

    def test_diversity_2(self):
        return "'True' 'col' '238' '310'"

    def test_diversity_3(self):
        return "'True' 'col' '146' '75'"

    def test_diversity_4(self):
        return "'True' 'col' '305' '231'"

    def test_diversity_5(self):
        return "'True' 'col' '243' '294'"

    def test_diversity_6(self):
        return "'True' 'col' '133' '3'"

    def test_diversity_7(self):
        return "'True' 'col' '37' '319'"

    def test_diversity_8(self):
        return "'True' 'col' '244' '340'"

    def test_diversity_9(self):
        return "'True' 'col' '152' '25'"

    def test_diversity_10(self):
        return "'True' 'col' '102' '75'"

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "'False' 'nocol' '100' '224'"

    def test_diversity_2(self):
        return "'False' 'nocol' '121' '275'"

    def test_diversity_3(self):
        return "'False' 'nocol' '366' '62'"

    def test_diversity_4(self):
        return "'False' 'nocol' '21' '396'"

    def test_diversity_5(self):
        return "'False' 'nocol' '262' '287'"

    def test_diversity_6(self):
        return "'False' 'nocol' '361' '46'"

    def test_diversity_7(self):
        return "'False' 'nocol' '96' '330'"

    def test_diversity_8(self):
        return "'False' 'nocol' '258' '303'"

    def test_diversity_9(self):
        return "'False' 'nocol' '223' '39'"

    def test_diversity_10(self):
        return "'False' 'nocol' '332' '274'"
