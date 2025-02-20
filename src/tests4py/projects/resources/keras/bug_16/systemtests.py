from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "562 'name'"

    def test_diversity_2(self):
        return "974 'name'"

    def test_diversity_3(self):
        return "33 'name'"

    def test_diversity_4(self):
        return "4 'name'"

    def test_diversity_5(self):
        return "32 'name'"

    def test_diversity_6(self):
        return "3 'name'"

    def test_diversity_7(self):
        return "2386 'name'"

    def test_diversity_8(self):
        return "66 'name'"

    def test_diversity_9(self):
        return "87 'name'"

    def test_diversity_10(self):
        return "8734 'name'"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "3 'name' 'config'"

    def test_diversity_2(self):
        return "4890 'name' 'config'"

    def test_diversity_3(self):
        return "44 'name' 'config'"

    def test_diversity_4(self):
        return "65 'name' 'config'"

    def test_diversity_5(self):
        return "3134 'name' 'config'"

    def test_diversity_6(self):
        return "4376 'name' 'config'"

    def test_diversity_7(self):
        return "316 'name' 'config'"

    def test_diversity_8(self):
        return "176 'name' 'config'"

    def test_diversity_9(self):
        return "376 'name' 'config'"

    def test_diversity_10(self):
        return "317 'name' 'config'"
