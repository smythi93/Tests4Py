from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'none aHR0cDovL3R2dXd5aC5pbw== eA=='

    def test_diversity_2(self):
        return 'none aHR0cDovL2xhbi5pbw== eA=='

    def test_diversity_3(self):
        return 'none aHR0cDovL2lrYWJsa3Uub3Jn eA=='

    def test_diversity_4(self):
        return 'none aHR0cDovL2hubmEuY29t eA=='

    def test_diversity_5(self):
        return 'none aHR0cDovL2huc3J1Z2wubmV0 eA=='

    def test_diversity_6(self):
        return 'none aHR0cDovL3dtaGYubmV0 eA=='

    def test_diversity_7(self):
        return 'none aHR0cDovL29ya24ub3Jn eA=='

    def test_diversity_8(self):
        return 'none aHR0cDovL2lmYy5pbw== eA=='

    def test_diversity_9(self):
        return 'none aHR0cDovL2xrZ2x2bm5uLm5ldA== eA=='

    def test_diversity_10(self):
        return 'none aHR0cDovL2p5emZ4Zi5jb20= eA=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'url aHR0cDovL2p3Z3Eub3Jn aHR0cDovL3R0bnRwLm9yZy9zZWk='

    def test_diversity_2(self):
        return 'url aHR0cDovL2FyZS5vcmc= aHR0cDovL2NreHB0Lm9yZy9zdnVnd2YvcmdseGR6L3p2ZGY='

    def test_diversity_3(self):
        return 'url aHR0cDovL3Vqci5jb20= aHR0cDovL3FhbXV6eC5vcmcvb2MveGlm'

    def test_diversity_4(self):
        return 'url aHR0cDovL21lcHVjbmt1Lmlv aHR0cDovL2V4ZWplZS5vcmcvcmlibGZxL3RuZw=='

    def test_diversity_5(self):
        return 'url aHR0cDovL25jdGV3cWguaW8= aHR0cDovL2pocGltYmxmLm9yZy9hcA=='

    def test_diversity_6(self):
        return 'url aHR0cDovL2lrcWp3a2VkLm5ldA== aHR0cDovL2lmZHkuY29tL2liY2RmL25ldGF3Yw=='

    def test_diversity_7(self):
        return 'url aHR0cDovL25wdWVrYXIuaW8= aHR0cDovL3JvcGlsLm5ldC91ZG9iYy9jZQ=='

    def test_diversity_8(self):
        return 'url aHR0cDovL2JmZnRlcC5vcmc= aHR0cDovL3p5eG95cWV0LmNvbS9ieGIvY28vemZq'

    def test_diversity_9(self):
        return 'url aHR0cDovL2tya2Mub3Jn aHR0cDovL2hvZXN6ay5vcmcvbnMvdW0vc2ZxYQ=='

    def test_diversity_10(self):
        return 'url aHR0cDovL2RweS5vcmc= aHR0cDovL2Z2cW5hLmlvL2txc3Zvei9oYm13bXE='
