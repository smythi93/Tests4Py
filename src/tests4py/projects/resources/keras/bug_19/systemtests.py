from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "6125 1256 'reverse_state_order' True"

    def test_diversity_2(self):
        return "65 56 'reverse_state_order' True"

    def test_diversity_3(self):
        return "185 16 'reverse_state_order' True"

    def test_diversity_4(self):
        return "65 6 'reverse_state_order' True"

    def test_diversity_5(self):
        return "615 126 'reverse_state_order' True"

    def test_diversity_6(self):
        return "61 156 'reverse_state_order' True"

    def test_diversity_7(self):
        return "5 125 'reverse_state_order' True"

    def test_diversity_8(self):
        return "25 256 'reverse_state_order' True"

    def test_diversity_9(self):
        return "15 126 'reverse_state_order' True"

    def test_diversity_10(self):
        return "61 5670 'reverse_state_order' True"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "6 8"

    def test_diversity_2(self):
        return "61 874"

    def test_diversity_3(self):
        return "65 724"

    def test_diversity_4(self):
        return "21 84"

    def test_diversity_5(self):
        return "521 7"

    def test_diversity_6(self):
        return "61 24"

    def test_diversity_7(self):
        return "652 824"

    def test_diversity_8(self):
        return "6521 4"

    def test_diversity_9(self):
        return "621 724"

    def test_diversity_10(self):
        return "65 87"
