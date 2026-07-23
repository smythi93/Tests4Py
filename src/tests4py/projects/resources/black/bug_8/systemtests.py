from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'ZnJvbSBtbWVhIGltcG9ydCAoCiAgICB2bXJpaXBtLAogICAgYXh0LAogICAgIyAgamZobgogICAgIyAga29paAopCg=='

    def test_diversity_2(self):
        return 'ZnJvbSBsenh4Y3N2cSBpbXBvcnQgKAogICAgaGpzcmllY20sCiAgICBtaGhsZmEsCiAgICBkdmRjdWwsCiAgICAjICBvYmV5d3VidwopCg=='

    def test_diversity_3(self):
        return 'ZnJvbSB4ZWx4YmlwbSBpbXBvcnQgKAogICAgaHpleW1qLAogICAgcGduLAogICAgZGJxLAogICAgIyAgeHJnYwogICAgIyAgd2hnYgopCg=='

    def test_diversity_4(self):
        return 'ZnJvbSB2cHF1bWNtciBpbXBvcnQgKAogICAgamhpLAogICAgamNzZGpkd2wsCiAgICAjICB3YWxuZnV3YgopCg=='

    def test_diversity_5(self):
        return 'ZnJvbSBsanV1dXV1IGltcG9ydCAoCiAgICB4dm1mZWgsCiAgICBxcGdtb21uLAogICAgIyAgbGttCiAgICAjICBkdXFkCiAgICAjICB0c3BkbmkKKQo='

    def test_diversity_6(self):
        return 'ZnJvbSBzb2xlcmFxIGltcG9ydCAoCiAgICBjdm54cmNmLAogICAgempyLAogICAgZXh6ZnFyLAogICAgIyAgeGxzaQogICAgIyAgYmlzdm5mCikK'

    def test_diversity_7(self):
        return 'ZnJvbSBnZmphayBpbXBvcnQgKAogICAgenhlYmt6LAogICAgdHdjZSwKICAgICMgIGJ5ZwopCg=='

    def test_diversity_8(self):
        return 'ZnJvbSBla3BrYyBpbXBvcnQgKAogICAgYnFyLAogICAgcXFxdmhxLAogICAgcnZscGh4LAogICAgIyAgdG5qYXkKICAgICMgIGZob3d3CiAgICAjICBzeGpwYWRiCikK'

    def test_diversity_9(self):
        return 'ZnJvbSBldXR5IGltcG9ydCAoCiAgICBnZ3F3anVjeCwKICAgIHdlYWosCiAgICAjICBycXpzbwopCg=='

    def test_diversity_10(self):
        return 'ZnJvbSBkcGhrIGltcG9ydCAoCiAgICB5dWN1a3RpaCwKICAgIG1nbCwKICAgIG9mY2csCiAgICB5Y3hsbWxtcSwKICAgICMgIGRxaWwKKQo='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'cHJpbnQoImRjZmtienB1IikK'

    def test_diversity_2(self):
        return 'cmRkZCA9IDIzNwo='

    def test_diversity_3(self):
        return 'aW1wb3J0IHB5YWx4ZGdnCg=='

    def test_diversity_4(self):
        return 'aW1wb3J0IGpudGRjbwo='

    def test_diversity_5(self):
        return 'cHJpbnQoImp0dGp3YXAiKQo='

    def test_diversity_6(self):
        return 'aW1wb3J0IHV1ZQo='

    def test_diversity_7(self):
        return 'ZnJvbSB6Ynp3cnd3IGltcG9ydCBybXhjcW9qLCB5YXIK'

    def test_diversity_8(self):
        return 'aW1wb3J0IG5ldmp6bQo='

    def test_diversity_9(self):
        return 'aW1wb3J0IGJuYmUK'

    def test_diversity_10(self):
        return 'aW1wb3J0IGVoZgo='
