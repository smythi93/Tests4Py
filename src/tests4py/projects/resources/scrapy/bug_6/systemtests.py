from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'palette 146 20 124 96'

    def test_diversity_2(self):
        return 'palette 9 0 37 199'

    def test_diversity_3(self):
        return 'palette 150 120 194 125'

    def test_diversity_4(self):
        return 'palette 81 197 5 99'

    def test_diversity_5(self):
        return 'palette 125 50 186 135'

    def test_diversity_6(self):
        return 'palette 137 138 174 54'

    def test_diversity_7(self):
        return 'palette 49 144 141 97'

    def test_diversity_8(self):
        return 'palette 169 156 175 52'

    def test_diversity_9(self):
        return 'palette 108 85 23 122'

    def test_diversity_10(self):
        return 'palette 104 64 113 54'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'rgba 100 149 49 41'

    def test_diversity_2(self):
        return 'rgba 102 184 249 243'

    def test_diversity_3(self):
        return 'rgba 99 14 185 92'

    def test_diversity_4(self):
        return 'rgba 220 155 182 180'

    def test_diversity_5(self):
        return 'rgba 61 45 101 59'

    def test_diversity_6(self):
        return 'rgba 137 159 100 127'

    def test_diversity_7(self):
        return 'rgba 247 114 70 182'

    def test_diversity_8(self):
        return 'rgba 107 6 96 229'

    def test_diversity_9(self):
        return 'rgba 86 8 170 172'

    def test_diversity_10(self):
        return 'rgba 156 191 193 165'

