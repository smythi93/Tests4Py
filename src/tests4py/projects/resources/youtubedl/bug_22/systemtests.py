from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJmaWx0ZXIiOiAienFsPSd0bHJ6dWwnIiwgImRjdCI6IHsienFsIjogInRscnp1bCJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_2(self):
        return 'eyJmaWx0ZXIiOiAicnl5ciE9J3RjcHUnIiwgImRjdCI6IHsicnl5ciI6ICJta2JzZXkgdmFqd24ifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_3(self):
        return 'eyJmaWx0ZXIiOiAidnJpPSd0eGl1ZSciLCAiZGN0IjogeyJ2cmkiOiAidHhpdWUifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_4(self):
        return 'eyJmaWx0ZXIiOiAiaWF3Z2I9J2V5cndqJyIsICJkY3QiOiB7Imlhd2diIjogImV5cndqIn0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_5(self):
        return 'eyJmaWx0ZXIiOiAicmtveng9J3lxcCciLCAiZGN0IjogeyJya296eCI6ICJ5cXAifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_6(self):
        return 'eyJmaWx0ZXIiOiAibHRrbGYhPSdiZnR5d2EnIiwgImRjdCI6IHsibHRrbGYiOiAiYmZ0eXdhIn0sICJleHBlY3RlZCI6IGZhbHNlfQ=='

    def test_diversity_7(self):
        return 'eyJmaWx0ZXIiOiAidnF6cmQ9J29ieG9yJyIsICJkY3QiOiB7InZxenJkIjogIm9ieG9yIn0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_8(self):
        return 'eyJmaWx0ZXIiOiAicHNxcHYhPSdoeHFmbmgnIiwgImRjdCI6IHsicHNxcHYiOiAiaWRzbyJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_9(self):
        return 'eyJmaWx0ZXIiOiAib2hkbWNvIT0naXRjIGtlb3BwbCciLCAiZGN0IjogeyJvaGRtY28iOiAiaXRjIGtlb3BwbCJ9LCAiZXhwZWN0ZWQiOiBmYWxzZX0='

    def test_diversity_10(self):
        return 'eyJmaWx0ZXIiOiAiaGdtPSdqa256JyIsICJkY3QiOiB7ImhnbSI6ICJqa256In0sICJleHBlY3RlZCI6IHRydWV9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJmaWx0ZXIiOiAicW91cD01MDUxIiwgImRjdCI6IHsicW91cCI6ICI1MDUxIn0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_2(self):
        return 'eyJmaWx0ZXIiOiAidnF3PWlkcHEiLCAiZGN0IjogeyJ2cXciOiAiaWRwcSJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_3(self):
        return 'eyJmaWx0ZXIiOiAidWxndHdhcj03MTg4MSIsICJkY3QiOiB7InVsZ3R3YXIiOiAiNzE4ODEifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_4(self):
        return 'eyJmaWx0ZXIiOiAic25lcz1mam5uY3AiLCAiZGN0IjogeyJzbmVzIjogImZqbm5jcCJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_5(self):
        return 'eyJmaWx0ZXIiOiAiaWd0eGpjdXE9bGNtdG10IiwgImRjdCI6IHsiaWd0eGpjdXEiOiAibGNtdG10In0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_6(self):
        return 'eyJmaWx0ZXIiOiAiampubz1uc2oiLCAiZGN0IjogeyJqam5vIjogIm5zaiJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_7(self):
        return 'eyJmaWx0ZXIiOiAidXF4cT01MDI5NCIsICJkY3QiOiB7InVxeHEiOiAiNTAyOTQifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_8(self):
        return 'eyJmaWx0ZXIiOiAianRrYmJpPTE4ODY1IiwgImRjdCI6IHsianRrYmJpIjogIjE4ODY1In0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_9(self):
        return 'eyJmaWx0ZXIiOiAiZHhncnhiYng9a2tnYnR5IiwgImRjdCI6IHsiZHhncnhiYngiOiAia2tnYnR5In0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_10(self):
        return 'eyJmaWx0ZXIiOiAiaWR1a3BuPXJ1eSIsICJkY3QiOiB7ImlkdWtwbiI6ICJydXkifSwgImV4cGVjdGVkIjogdHJ1ZX0='
