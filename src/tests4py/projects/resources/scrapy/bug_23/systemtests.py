from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'aHR0cDovL3R2dXd5aDplZGxvZW9AdHRudHAuY29tOjM0NTE='

    def test_diversity_2(self):
        return 'aHR0cDovL3p0YXl3dWU6cWNyQHRnbnMubmV0OjE2ODM='

    def test_diversity_3(self):
        return 'aHR0cDovL3BueWJlOmRmb0BrYWJsLm5ldDozOTY0'

    def test_diversity_4(self):
        return 'aHR0cDovL2JxaXBreWY6c29jZXpmZWhAY3Nkcnh2eS5jb206NTM1Mw=='

    def test_diversity_5(self):
        return 'aHR0cDovL2tlcm46eW5rZEBsZnFmZHhpaC5pbzo5Mzg1'

    def test_diversity_6(self):
        return 'aHR0cDovL3dxaGxqOmxndG1nQGZkYS5pbzoyMzg2'

    def test_diversity_7(self):
        return 'aHR0cDovL2p4c3diOmp3a2VkQGdsYWNuLm5ldDo3NDQ4'

    def test_diversity_8(self):
        return 'aHR0cDovL3pod2M6Zm55emFucEBwdWVrYS5pbzoxNDcy'

    def test_diversity_9(self):
        return 'aHR0cDovL2RvYmN5OnBhYkBubG1sLmNvbTo2NDIy'

    def test_diversity_10(self):
        return 'aHR0cDovL3JsdHE6dXRvQGNvZi5uZXQ6NDcxNQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'aHR0cDovL3NlaWEubmV0OjE0NjQ='

    def test_diversity_2(self):
        return 'aHR0cDovL2RtdHQuaW86NDA2OA=='

    def test_diversity_3(self):
        return 'aHR0cDovL3Vqci5jb206ODkwMQ=='

    def test_diversity_4(self):
        return 'aHR0cDovL3RidGxleGUubmV0OjY0Mzg='

    def test_diversity_5(self):
        return 'aHR0cDovL3V4YnVidW5jLmNvbTozNTgy'

    def test_diversity_6(self):
        return 'aHR0cDovL2N3dy5uZXQ6NDAwMw=='

    def test_diversity_7(self):
        return 'aHR0cDovL3dnbXBnLmlvOjY5MDQ='

    def test_diversity_8(self):
        return 'aHR0cDovL2p2cmFtYi5uZXQ6NzQwNQ=='

    def test_diversity_9(self):
        return 'aHR0cDovL3Vqb3pybWVmLmlvOjQ1Mjg='

    def test_diversity_10(self):
        return 'aHR0cDovL2pycm9xdy5pbzoyODAw'
