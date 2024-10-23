from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '{i: [252, 65]}, [(252, 65), (46, 982)'

    def test_diversity_2(self):
        return '{a: [9, 5]}, [(9, 5), (6, 4)'

    def test_diversity_3(self):
        return '{b: [95, 580]}, [(95, 580), (756, 75)'

    def test_diversity_4(self):
        return '{d: [54, 23]}, [(54, 23), (63, 32)'

    def test_diversity_5(self):
        return '{x: [55, 453]}, [(55, 453), (65, 652)'

    def test_diversity_6(self):
        return '{t: [12, 573]}, [(12, 573), (43, 32)'

    def test_diversity_7(self):
        return '{u: [333, 763]}, [(333, 763), (41, 76)'

    def test_diversity_8(self):
        return '{s: [213, 74]}, [(213, 74), (96, 623)'

    def test_diversity_9(self):
        return '{h: [65, 134]}, [(65, 134), (99, 1)'

    def test_diversity_10(self):
        return '{k: [23, 874]}, [(23, 874), (78, 639)'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '{l: [123, 588]}, [(123, 588), (462, 232)'

    def test_diversity_2(self):
        return '{p: [765, 58]}, [(765, 58), (463, 234)'

    def test_diversity_3(self):
        return '{i: [435, 54]}, [(435, 54), (87, 764)'

    def test_diversity_4(self):
        return '{q: [213, 38]}, [(213, 38), (65, 231)'

    def test_diversity_5(self):
        return '{e: [423, 788]}, [(423, 788), (23, 952)'

    def test_diversity_6(self):
        return '{o: [555, 88]}, [(555, 88), (435, 932)'

    def test_diversity_7(self):
        return '{j: [33, 11]}, [(33, 11), (123, 345)'

    def test_diversity_8(self):
        return '{n: [110, 63]}, [(110, 63), (62, 212)'

    def test_diversity_9(self):
        return '{z: [9, 84]}, [(9, 84), (44, 582)'

    def test_diversity_10(self):
        return '{v: [5, 523]}, [(5, 523), (16, 382)'
