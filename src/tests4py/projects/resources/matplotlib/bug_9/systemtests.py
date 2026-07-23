from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'stale 3.488 1.77'

    def test_diversity_2(self):
        return 'stale 3.422 1.616'

    def test_diversity_3(self):
        return 'stale 5.57 2.879'

    def test_diversity_4(self):
        return 'stale 4.794 2.254'

    def test_diversity_5(self):
        return 'stale 3.744 2.709'

    def test_diversity_6(self):
        return 'stale 2.64 1.632'

    def test_diversity_7(self):
        return 'stale 4.56 2.376'

    def test_diversity_8(self):
        return 'stale 4.107 1.741'

    def test_diversity_9(self):
        return 'stale 4.015 2.356'

    def test_diversity_10(self):
        return 'stale 3.102 2.266'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'normal -0.574 3.191'

    def test_diversity_2(self):
        return 'normal -1.271 2.276'

    def test_diversity_3(self):
        return 'normal -1.057 2.914'

    def test_diversity_4(self):
        return 'normal -1.032 2.858'

    def test_diversity_5(self):
        return 'normal -2.25 2.907'

    def test_diversity_6(self):
        return 'normal -1.965 2.536'

    def test_diversity_7(self):
        return 'normal -2.153 3.791'

    def test_diversity_8(self):
        return 'normal -2.334 2.888'

    def test_diversity_9(self):
        return 'normal -0.894 2.382'

    def test_diversity_10(self):
        return 'normal -1.636 2.259'
