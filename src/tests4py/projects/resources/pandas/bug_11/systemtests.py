from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "['e', 'f', 'f'] {'a': [109, 103, 194], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_2(self):
        return "['e', 'f', 'f'] {'a': [102, 193, 94], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_3(self):
        return "['e', 'f', 'f'] {'a': [192, 109, 194], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_4(self):
        return "['e', 'f', 'f'] {'a': [92, 93, 104], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_5(self):
        return "['e', 'f', 'f'] {'a': [9, 193, 14], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_6(self):
        return "['e', 'f', 'f'] {'a': [921, 93, 10], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_7(self):
        return "['e', 'f', 'f'] {'a': [10, 10, 1], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_8(self):
        return "['e', 'f', 'f'] {'a': [19, 13, 14], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_9(self):
        return "['e', 'f', 'f'] {'a': [12, 19, 19], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"

    def test_diversity_10(self):
        return "['e', 'f', 'f'] {'a': [12, 19, 1094], 'b': [1095, 1096, 1097]} [1098, 1099, 1100] [1101, 1102, 1103]"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [1095, 16, 1097]} [1098, 1099, 1100] [1101, 1102, 13]"

    def test_diversity_2(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [1, 16, 1097]} [1098, 109, 110] [1101, 112, 103]"

    def test_diversity_3(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [109, 106, 1097]} [1098, 199, 110] [1101, 102, 113]"

    def test_diversity_4(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [105, 196, 107]} [1098, 109, 1100] [101, 102, 1103]"

    def test_diversity_5(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [19, 1096, 97]} [1098, 99, 1100] [111, 102, 113]"

    def test_diversity_6(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [15, 1096, 197]} [109, 1099, 1100] [11, 12, 13]"

    def test_diversity_7(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [95, 1096, 109]} [10, 1099, 1100] [1101, 102, 13]"

    def test_diversity_8(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [109, 1096, 1097]} [198, 1099, 1100] [101, 112, 11]"

    def test_diversity_9(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [195, 1096, 1097]} [108, 1099, 1100] [101, 112, 3]"

    def test_diversity_10(self):
        return "['f', 'e', 'g'] {'a': [1092, 1093, 1094], 'b': [195, 1096, 1097]} [98, 1099, 1100] [111, 112, 3]"
