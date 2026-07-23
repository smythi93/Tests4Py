from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '-ar omp -m get -u /openapi.json'

    def test_diversity_2(self):
        return '-ar dvm -m get -u /openapi.json'

    def test_diversity_3(self):
        return '-ar cwmobtk -m get -u /openapi.json'

    def test_diversity_4(self):
        return '-ar dag -m get -u /openapi.json'

    def test_diversity_5(self):
        return '-ar uuy -m get -u /openapi.json'

    def test_diversity_6(self):
        return '-ar amug -m get -u /openapi.json'

    def test_diversity_7(self):
        return '-ar gszmeht -m get -u /openapi.json'

    def test_diversity_8(self):
        return '-ar xyzrsfw -m get -u /openapi.json'

    def test_diversity_9(self):
        return '-ar cxfgaqr -m get -u /openapi.json'

    def test_diversity_10(self):
        return '-ar ytlpdczc -m get -u /openapi.json'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '-gs /esbyhpbd/ Item -m get -u /esbyhpbd/'

    def test_diversity_2(self):
        return '-gs /fffd/ Item -m get -u /fffd/'

    def test_diversity_3(self):
        return '-gs /pgyjjc/ Item -m get -u /pgyjjc/'

    def test_diversity_4(self):
        return '-gs /onwctc/ Item -m get -u /onwctc/'

    def test_diversity_5(self):
        return '-gs /bexlnx/ Item -m get -u /bexlnx/'

    def test_diversity_6(self):
        return '-gs /qdpbuerx/ Item -m get -u /qdpbuerx/'

    def test_diversity_7(self):
        return '-gs /tbllh/ Item -m get -u /tbllh/'

    def test_diversity_8(self):
        return '-gs /wljqz/ Item -m get -u /wljqz/'

    def test_diversity_9(self):
        return '-gs /wafane/ Item -m get -u /wafane/'

    def test_diversity_10(self):
        return '-gs /oatfba/ Item -m get -u /oatfba/'
