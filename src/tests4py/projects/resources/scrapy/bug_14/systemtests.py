from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'application/X-Gzip'

    def test_diversity_2(self):
        return 'APPLICATION/GZIP'

    def test_diversity_3(self):
        return 'Application/GZip'

    def test_diversity_4(self):
        return 'application/x-gzip;charset=qtn'

    def test_diversity_5(self):
        return 'application/gzip;charset=hgtr'

    def test_diversity_6(self):
        return 'application/X-GZIP;charset=mwkxg'

    def test_diversity_7(self):
        return 'application/x-gzip;charset=jguqd'

    def test_diversity_8(self):
        return 'application/gzip;charset=rhabpah'

    def test_diversity_9(self):
        return 'application/X-GZIP;charset=kzlpwr'

    def test_diversity_10(self):
        return 'application/x-gzip;charset=pqj'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'application/x-gzip'

    def test_diversity_2(self):
        return 'application/gzip'

    def test_diversity_3(self):
        return 'application/gziptmr'

    def test_diversity_4(self):
        return 'text/lfunc'

    def test_diversity_5(self):
        return 'image/hde'

    def test_diversity_6(self):
        return 'application/gzipcncmrn'

    def test_diversity_7(self):
        return 'text/ilkvgk'

    def test_diversity_8(self):
        return 'image/wybdso'

    def test_diversity_9(self):
        return 'application/gzipvkz'

    def test_diversity_10(self):
        return 'text/joy'

