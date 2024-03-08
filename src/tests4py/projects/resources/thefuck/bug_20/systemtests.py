from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'unzip abGYJ.zip, NfMFixvKoZhvND.zip' '' ''

    def test_diversity_2(self):
        return 'unzip KUlVMKuah\\ WwAvJuXzJw.zip' '' ''

    def test_diversity_3(self):
        return 'unzip KweNZAOyhvB.zip, bYogNneZlkGDYKU.zip' '' ''

    def test_diversity_4(self):
        return 'unzip iXcVfQyzPqIlQP\\ noePSJtge.zip' '' ''

    def test_diversity_5(self):
        return "unzip 'wrIzCEo kTbdO.zip'" '' ''

    def test_diversity_6(self):
        return "unzip 'sgFyxBNW SvsZqnTA.zip'" '' ''

    def test_diversity_7(self):
        return 'unzip jYYbrDwaWptJ.zip, uyopElXi.zip' '' ''

    def test_diversity_8(self):
        return 'unzip xaMGlDBopY\\ dZmlixXEjixM.zip' '' ''

    def test_diversity_9(self):
        return 'unzip oKrja.zip, AvIHK.zip' '' ''

    def test_diversity_10(self):
        return 'unzip lgeWWVqTUfOdIc.zip, lxkQWl.zip' '' ''


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'unzip JoFFeu' '' ''

    def test_diversity_2(self):
        return 'unzip ojBLQgBOHksoHA' '' ''

    def test_diversity_3(self):
        return 'unzip HZzjhBEi' '' ''

    def test_diversity_4(self):
        return 'unzip vuJRTjLAeYK' '' ''

    def test_diversity_5(self):
        return 'unzip cCtXqphc.zip' '' ''

    def test_diversity_6(self):
        return 'unzip GdFeLDvcOP.zip' '' ''

    def test_diversity_7(self):
        return 'unzip sXxFlJICq.zip' '' ''

    def test_diversity_8(self):
        return 'unzip XqAMufH.zip' '' ''

    def test_diversity_9(self):
        return 'unzip keJpgSsSe' '' ''

    def test_diversity_10(self):
        return 'unzip TcpSnB' '' ''
