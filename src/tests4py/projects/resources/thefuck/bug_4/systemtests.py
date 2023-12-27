from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    # Create Fish() Shell instance, _get_aliases(fish.get_overridden_aliases()) -
    # Result should be like "Error retrieving overridden" for failing values
    # There is no input so, no input provided
    def test_diversity_1(self):
        return ""

    def test_diversity_2(self):
        return ""

    def test_diversity_3(self):
        return ""

    def test_diversity_4(self):
        return ""

    def test_diversity_5(self):
        return ""

    def test_diversity_6(self):
        return ""

    def test_diversity_7(self):
        return ""

    def test_diversity_8(self):
        return ""

    def test_diversity_9(self):
        return ""

    def test_diversity_10(self):
        return ""


class TestsPassing(PassingSystemtests):
    # Create Fish() Shell instance, _get_aliases(fish.get_overridden_aliases()) -
    # Result should be like "cd ~/Downloads" or just "cd" for passing values
    # There is no input so, no input provided
    def test_diversity_1(self):
        return ""

    def test_diversity_2(self):
        return ""

    def test_diversity_3(self):
        return ""

    def test_diversity_4(self):
        return ""

    def test_diversity_5(self):
        return ""

    def test_diversity_6(self):
        return ""

    def test_diversity_7(self):
        return ""

    def test_diversity_8(self):
        return ""

    def test_diversity_9(self):
        return ""

    def test_diversity_10(self):
        return ""
