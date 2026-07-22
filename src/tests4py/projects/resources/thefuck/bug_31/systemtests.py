from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('Integer value cannot be used', 6584)"

    def test_diversity_2(self):
        return "('Integer value cannot be used', 3173)"

    def test_diversity_3(self):
        return "('Integer value cannot be used', 5725)"

    def test_diversity_4(self):
        return "('Integer value cannot be used', 6713)"

    def test_diversity_5(self):
        return "('Integer value cannot be used', 7688)"

    def test_diversity_6(self):
        return "('Integer value cannot be used', 831)"

    def test_diversity_7(self):
        return "('Integer value cannot be used', 7087)"

    def test_diversity_8(self):
        return "('Integer value cannot be used', 8525)"

    def test_diversity_9(self):
        return "('Integer value cannot be used', 2400)"

    def test_diversity_10(self):
        return "('Integer value cannot be used', 2300)"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('git diff WwtFAy --staged', 'git diff WwtFAy')"

    def test_diversity_2(self):
        return "('git diff UGEGam --staged', 'git diff UGEGam')"

    def test_diversity_3(self):
        return "('git diff FTTXdZIOfbJZNad --staged', 'git diff FTTXdZIOfbJZNad')"

    def test_diversity_4(self):
        return "('git diff IPcufiDZHDoiNu --staged', 'git diff IPcufiDZHDoiNu')"

    def test_diversity_5(self):
        return "('git diff ZEphHJ --staged', 'git diff ZEphHJ')"

    def test_diversity_6(self):
        return "('git diff bZvRAKerTyGG --staged', 'git diff bZvRAKerTyGG')"

    def test_diversity_7(self):
        return "('git diff lAWHfo --staged', 'git diff lAWHfo')"

    def test_diversity_8(self):
        return "('git diff uFTMTKH --staged', 'git diff uFTMTKH')"

    def test_diversity_9(self):
        return "('git diff ImLqggZvUxo --staged', 'git diff ImLqggZvUxo')"

    def test_diversity_10(self):
        return "('git diff nTxqcrTYX --staged', 'git diff nTxqcrTYX')"
