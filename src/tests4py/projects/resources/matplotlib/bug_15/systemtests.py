from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'basekw 0.759 0.951 -6.64 17.165 10 10.248'

    def test_diversity_2(self):
        return 'basekw 1.504 1.155 -13.43 12.663 10 5.496'

    def test_diversity_3(self):
        return 'basekw 2.446 1.379 -11.387 26.444 e 18.741'

    def test_diversity_4(self):
        return 'basekw 1.75 1.443 -11.308 22.952 2 -0.727'

    def test_diversity_5(self):
        return 'basekw 2.028 1.897 -15.231 6.694 10 -5.827'

    def test_diversity_6(self):
        return 'basekw 1.608 1.33 -23.555 19.258 2 -5.656'

    def test_diversity_7(self):
        return 'basekw 0.766 0.771 -16.844 18.266 2 -2.998'

    def test_diversity_8(self):
        return 'basekw 0.7 0.836 -29.187 28.693 2 -1.943'

    def test_diversity_9(self):
        return 'basekw 0.657 0.807 -18.151 19.281 2 4.363'

    def test_diversity_10(self):
        return 'basekw 1.906 1.135 -14.477 21.773 2 5.137'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nobase 2.496 1.986 -21.753 8.574 e -2.35'

    def test_diversity_2(self):
        return 'nobase 2.384 1.139 -14.729 9.275 e 6.074'

    def test_diversity_3(self):
        return 'nobase 0.946 1.651 -29.712 13.328 e -1.338'

    def test_diversity_4(self):
        return 'nobase 1.009 1.954 -25.282 6.129 e 2.304'

    def test_diversity_5(self):
        return 'nobase 0.913 1.501 -15.249 13.201 e -2.699'

    def test_diversity_6(self):
        return 'nobase 1.728 0.917 -26.804 19.656 e -13.057'

    def test_diversity_7(self):
        return 'nobase 1.838 1.615 -29.381 8.748 e -26.241'

    def test_diversity_8(self):
        return 'nobase 1.74 1.45 -14.885 11.695 e -1.056'

    def test_diversity_9(self):
        return 'nobase 1.977 1.886 -17.84 7.103 e -3.084'

    def test_diversity_10(self):
        return 'nobase 2.795 1.568 -7.595 9.597 e -1.125'
