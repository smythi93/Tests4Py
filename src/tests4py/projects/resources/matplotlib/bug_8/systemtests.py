from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'y true -1.116 1.929'

    def test_diversity_2(self):
        return 'x true -0.796 1.873'

    def test_diversity_3(self):
        return 'x none -0.515 1.305'

    def test_diversity_4(self):
        return 'y none -0.862 1.217'

    def test_diversity_5(self):
        return 'x true -1.622 0.55'

    def test_diversity_6(self):
        return 'x none -1.756 0.476'

    def test_diversity_7(self):
        return 'x true -1.405 1.773'

    def test_diversity_8(self):
        return 'x none -1.367 1.803'

    def test_diversity_9(self):
        return 'x none -0.772 0.81'

    def test_diversity_10(self):
        return 'y none -1.387 1.609'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'y false -0.879 1.847'

    def test_diversity_2(self):
        return 'x false -1.294 0.908'

    def test_diversity_3(self):
        return 'x false -1.151 0.809'

    def test_diversity_4(self):
        return 'y false -1.15 0.842'

    def test_diversity_5(self):
        return 'x false -1.166 0.677'

    def test_diversity_6(self):
        return 'x false -0.488 1.54'

    def test_diversity_7(self):
        return 'x false -1.069 1.117'

    def test_diversity_8(self):
        return 'x false -1.855 0.39'

    def test_diversity_9(self):
        return 'y false -1.159 1.905'

    def test_diversity_10(self):
        return 'y false -1.585 1.828'
