from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJmaWx0ZXIiOiAiIWRxd3FtIiwgImRjdCI6IHsiZHF3cW0iOiBmYWxzZX0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_2(self):
        return 'eyJmaWx0ZXIiOiAiIXpkY2xxbXEiLCAiZGN0IjogeyJ6ZGNscW1xIjogZmFsc2V9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_3(self):
        return 'eyJmaWx0ZXIiOiAiZGNxcGJvIiwgImRjdCI6IHsiZGNxcGJvIjogZmFsc2V9LCAiZXhwZWN0ZWQiOiBmYWxzZX0='

    def test_diversity_4(self):
        return 'eyJmaWx0ZXIiOiAiIW54aGphaSIsICJkY3QiOiB7Im54aGphaSI6IGZhbHNlfSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_5(self):
        return 'eyJmaWx0ZXIiOiAiIWdibnRiZXYiLCAiZGN0IjogeyJnYm50YmV2IjogZmFsc2V9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_6(self):
        return 'eyJmaWx0ZXIiOiAiIXRpaG1ociIsICJkY3QiOiB7InRpaG1ociI6IGZhbHNlfSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_7(self):
        return 'eyJmaWx0ZXIiOiAiIWV2aSIsICJkY3QiOiB7ImV2aSI6IGZhbHNlfSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_8(self):
        return 'eyJmaWx0ZXIiOiAiIWRneGNnIiwgImRjdCI6IHsiZGd4Y2ciOiBmYWxzZX0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_9(self):
        return 'eyJmaWx0ZXIiOiAiIXFvZnFhYiIsICJkY3QiOiB7InFvZnFhYiI6IGZhbHNlfSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_10(self):
        return 'eyJmaWx0ZXIiOiAieGx5cCIsICJkY3QiOiB7InhseXAiOiBmYWxzZX0sICJleHBlY3RlZCI6IGZhbHNlfQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJmaWx0ZXIiOiAiamJiIiwgImRjdCI6IHsiamJiIjogdHJ1ZX0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_2(self):
        return 'eyJmaWx0ZXIiOiAicGlyYWJ1PjM0OSIsICJkY3QiOiB7InBpcmFidSI6IDY5OH0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_3(self):
        return 'eyJmaWx0ZXIiOiAiIWlwb3Nwb2V2IiwgImRjdCI6IHsiaXBvc3BvZXYiOiB0cnVlfSwgImV4cGVjdGVkIjogZmFsc2V9'

    def test_diversity_4(self):
        return 'eyJmaWx0ZXIiOiAiamlud2p5IiwgImRjdCI6IHsiamlud2p5IjogdHJ1ZX0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_5(self):
        return 'eyJmaWx0ZXIiOiAiand4eHh1a3MiLCAiZGN0IjogeyJqd3h4eHVrcyI6IHRydWV9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_6(self):
        return 'eyJmaWx0ZXIiOiAiZHp6Znh0eCIsICJkY3QiOiB7ImR6emZ4dHgiOiB0cnVlfSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_7(self):
        return 'eyJmaWx0ZXIiOiAicmdpaXl5c3AiLCAiZGN0IjogeyJyZ2lpeXlzcCI6IHRydWV9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_8(self):
        return 'eyJmaWx0ZXIiOiAiIXV0bnRqcWV5IiwgImRjdCI6IHsidXRudGpxZXkiOiB0cnVlfSwgImV4cGVjdGVkIjogZmFsc2V9'

    def test_diversity_9(self):
        return 'eyJmaWx0ZXIiOiAidm5seW9iPjI1MSIsICJkY3QiOiB7InZubHlvYiI6IDUwM30sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_10(self):
        return 'eyJmaWx0ZXIiOiAic3puZSIsICJkY3QiOiB7InN6bmUiOiB0cnVlfSwgImV4cGVjdGVkIjogdHJ1ZX0='
