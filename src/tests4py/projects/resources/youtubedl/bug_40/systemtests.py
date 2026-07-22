from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'ytdl !Q 138193304849869414'

    def test_diversity_2(self):
        return 'ytdl !B 42'

    def test_diversity_3(self):
        return 'ytdl !B 181'

    def test_diversity_4(self):
        return 'ytdl !H 2284'

    def test_diversity_5(self):
        return 'ytdl !B 8'

    def test_diversity_6(self):
        return 'ytdl !I 1990923381'

    def test_diversity_7(self):
        return 'ytdl !B 93'

    def test_diversity_8(self):
        return 'ytdl !B 7'

    def test_diversity_9(self):
        return 'ytdl !Q 17799292253133767281'

    def test_diversity_10(self):
        return 'ytdl !B 238'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'std !B 45'

    def test_diversity_2(self):
        return 'std !B 138'

    def test_diversity_3(self):
        return 'std !B 154'

    def test_diversity_4(self):
        return 'std !Q 6553005604873783821'

    def test_diversity_5(self):
        return 'std !H 26218'

    def test_diversity_6(self):
        return 'std !Q 106626587810730954'

    def test_diversity_7(self):
        return 'std !H 61974'

    def test_diversity_8(self):
        return 'std !Q 999356049167737306'

    def test_diversity_9(self):
        return 'std !Q 2660863980327693600'

    def test_diversity_10(self):
        return 'std !I 3311333766'
