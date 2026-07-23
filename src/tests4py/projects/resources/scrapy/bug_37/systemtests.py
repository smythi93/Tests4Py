from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'noscheme dHZ1d3loOmVkbG9lbw=='

    def test_diversity_2(self):
        return 'noscheme bGFuOnRheXd1ZWNr'

    def test_diversity_3(self):
        return 'noscheme enZkZm86a2FibA=='

    def test_diversity_4(self):
        return 'noscheme Y2V6ZjplZGNz'

    def test_diversity_5(self):
        return 'noscheme b3Z4eTpyaWJsZnFm'

    def test_diversity_6(self):
        return 'noscheme bGpocGltYmw6aXhycQ=='

    def test_diversity_7(self):
        return 'noscheme a2VkOmdsYWNu'

    def test_diversity_8(self):
        return 'noscheme amFrOnZyYW1iaXVk'

    def test_diversity_9(self):
        return 'noscheme eG95cTpybHRx'

    def test_diversity_10(self):
        return 'noscheme cnJvcXd4Y2E6eGprcmtjZw=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'scheme aHR0cDovL3R0bnRwLm9yZy9zZWk='

    def test_diversity_2(self):
        return 'scheme aHR0cDovL3B0Z25zdnVnLmlvL3JnbHhkeg=='

    def test_diversity_3(self):
        return 'scheme aHR0cDovL3p4dXVqci5jb20vYnFpcGt5L2pyZA=='

    def test_diversity_4(self):
        return 'scheme aHR0cDovL2FtZXAuY29tL3RidGxleC9haWs='

    def test_diversity_5(self):
        return 'scheme aHR0cDovL25nb2QuY29tL2J1bmN0L2pzYQ=='

    def test_diversity_6(self):
        return 'scheme aHR0cDovL2FwZS5pby9oZmgvd2JodQ=='

    def test_diversity_7(self):
        return 'scheme aHR0cDovL2t3Z21wLm5ldC9qemh3Y24vbnl6YW5wL3B1ZWs='

    def test_diversity_8(self):
        return 'scheme aHR0cDovL3FvbWRwYWIub3JnL2xtL2ZmdGVwL3pybQ=='

    def test_diversity_9(self):
        return 'scheme aHR0cDovL3V0by5jb20vb2ZobQ=='

    def test_diversity_10(self):
        return 'scheme aHR0cDovL2xkZnF4Lm5ldC9xbnMvdW0vc2ZxYQ=='
