from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'hex aHR0cDovL2tiZS5leGFtcGxlLm5ldC94YiVhMHBtaw=='

    def test_diversity_2(self):
        return 'hex aHR0cDovL3J2bGVhbi5leGFtcGxlLmlvL3RxeiU5ZG9sZg=='

    def test_diversity_3(self):
        return 'hex aHR0cDovL2h3amsuZXhhbXBsZS5jb20vZ2ZpciViY2tsanI='

    def test_diversity_4(self):
        return 'hex aHR0cDovL2htby5leGFtcGxlLmNvbS9iZmduJWI3a2s='

    def test_diversity_5(self):
        return 'hex aHR0cDovL2V4b3UuZXhhbXBsZS5jb20va3Z1b2UlOGRoeQ=='

    def test_diversity_6(self):
        return 'hex aHR0cDovL2RtdmhycWIuZXhhbXBsZS5uZXQvbnB6aCU5ZWF5dGY='

    def test_diversity_7(self):
        return 'hex aHR0cDovL29vdGlyLmV4YW1wbGUub3JnL2ZkJTlhY2g='

    def test_diversity_8(self):
        return 'hex aHR0cDovL3VsZC5leGFtcGxlLmlvL3hlJWE2eXV2'

    def test_diversity_9(self):
        return 'hex aHR0cDovL3hlc2lzbmpxLmV4YW1wbGUubmV0L2dqJTg4amhjbGI='

    def test_diversity_10(self):
        return 'hex aHR0cDovL3dnd3hreXVhLmV4YW1wbGUuY29tL3FlYmwlYThqZnVnbQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'plain aHR0cDovL3lzd2EuZXhhbXBsZS5pby93a3Jjd3c='

    def test_diversity_2(self):
        return 'plain aHR0cDovL3dncXkuZXhhbXBsZS5uZXQvb3U='

    def test_diversity_3(self):
        return 'plain aHR0cDovL3B2YncuZXhhbXBsZS5uZXQvcXZic3lyL2V2aHQ='

    def test_diversity_4(self):
        return 'plain aHR0cDovL3BhbGF4LmV4YW1wbGUubmV0L2VjL2xm'

    def test_diversity_5(self):
        return 'plain aHR0cDovL29rbHouZXhhbXBsZS5vcmcvdmRxZ2duL29lc24vbGZ2am5u'

    def test_diversity_6(self):
        return 'plain aHR0cDovL2J3cGNnaHAuZXhhbXBsZS5uZXQvbXA='

    def test_diversity_7(self):
        return 'plain aHR0cDovL2x0YnhteWNmLmV4YW1wbGUuY29tL2xldnJmaQ=='

    def test_diversity_8(self):
        return 'plain aHR0cDovL2N5a29jZy5leGFtcGxlLm9yZy95ZXJndy9jYmRzZA=='

    def test_diversity_9(self):
        return 'plain aHR0cDovL2Ntam1kLmV4YW1wbGUuaW8vanBoZHlkL3hvc3V6ZA=='

    def test_diversity_10(self):
        return 'plain aHR0cDovL2Z2ZXJkLmV4YW1wbGUuaW8vdHhscG0='
