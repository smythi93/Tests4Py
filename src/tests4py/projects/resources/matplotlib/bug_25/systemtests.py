from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '-44.269 13.429 44.795 -29.478'

    def test_diversity_2(self):
        return '39.944 -43.047 -20.611 -36.43 6.168 -40.032'

    def test_diversity_3(self):
        return '37.765 48.949 9.265'

    def test_diversity_4(self):
        return '25.54 -25.375 16.099 -32.087 -17.28'

    def test_diversity_5(self):
        return '36.445 48.591 -10.554'

    def test_diversity_6(self):
        return '10.297 -25.739 -17.787 -27.43 -24.178'

    def test_diversity_7(self):
        return '-30.605 34.114 -19.658 -26.717'

    def test_diversity_8(self):
        return '-35.439 -30.699 -4.963 38.619 9.966 35.369'

    def test_diversity_9(self):
        return '42.761 26.244 -38.771 -39.908 45.786'

    def test_diversity_10(self):
        return '31.664 -7.895 32.605'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '-39.687 -26.633 -26.616 38.184'

    def test_diversity_2(self):
        return '-37.805 33.44 37.261'

    def test_diversity_3(self):
        return '-26.156 -14.005 0.209 29.787 44.064'

    def test_diversity_4(self):
        return '-33.437 -16.738 31.378 34.374 41.659 42.741'

    def test_diversity_5(self):
        return '-48.51 -34.971 -24.245 31.665'

    def test_diversity_6(self):
        return '-34.535 -8.052 4.489 4.757 15.703'

    def test_diversity_7(self):
        return '-40.301 -25.392 -23.287 28.655'

    def test_diversity_8(self):
        return '-23.479 -0.979 4.865'

    def test_diversity_9(self):
        return '-34.079 -17.862 21.59 43.551 44.374'

    def test_diversity_10(self):
        return '-47.688 -35.072 -3.494 16.665 23.497 43.271'
