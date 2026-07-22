from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'numeric 614 614 gt'

    def test_diversity_2(self):
        return 'alpha opqah opqah gt'

    def test_diversity_3(self):
        return 'alpha i i gt'

    def test_diversity_4(self):
        return 'numeric 451 451 gt'

    def test_diversity_5(self):
        return 'alpha m m gt'

    def test_diversity_6(self):
        return 'alpha haihs haihs gt'

    def test_diversity_7(self):
        return 'alpha ga ga gt'

    def test_diversity_8(self):
        return 'alpha um um gt'

    def test_diversity_9(self):
        return 'numeric 856 856 gt'

    def test_diversity_10(self):
        return 'alpha gp gp gt'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'numeric 495 615 gt'

    def test_diversity_2(self):
        return 'numeric 386 920 eq'

    def test_diversity_3(self):
        return 'numeric 116 478 gt'

    def test_diversity_4(self):
        return 'numeric 525 392 eq'

    def test_diversity_5(self):
        return 'alpha wz w lt'

    def test_diversity_6(self):
        return 'numeric 351 148 le'

    def test_diversity_7(self):
        return 'alpha hoz zzkqb ge'

    def test_diversity_8(self):
        return 'numeric 182 500 le'

    def test_diversity_9(self):
        return 'numeric 657 521 ge'

    def test_diversity_10(self):
        return 'alpha na pnt ge'
