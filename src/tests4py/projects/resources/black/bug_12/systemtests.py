from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'Zm9yICgodGxqdHZvdnogaW4ge30pIG9yIHt9KVsidW13bHgiXSBpbiB1cnR3anFxOgogICAgbWN5Z20gPSAxCg=='

    def test_diversity_2(self):
        return 'Zm9yICgoZXJiZmlibyBpbiB7fSkgb3Ige30pWyJucnNta25tZCJdIGluIG1ubGlyc2lpOgogICAgb2NuZiA9IDUK'

    def test_diversity_3(self):
        return 'Zm9yICgoaW55amdsaW0gaW4ge30pIG9yIHt9KVs3XSBpbiBvYXVjdnRiOgogICAgcGFzcwo='

    def test_diversity_4(self):
        return 'Zm9yICgoeHJ3ZXdneSBpbiB7fSkgb3Ige30pWyJydXhvb2tyYiJdIGluIHJyY214cWQ6CiAgICBoa3h2cnQgPSAwCg=='

    def test_diversity_5(self):
        return 'Zm9yICgoa21keG54IGluIHt9KSBvciB7fSlbInZwaCJdIGluIGd3cToKICAgIHBhc3MK'

    def test_diversity_6(self):
        return 'Zm9yICgobXRpZGwgaW4ge30pIG9yIHt9KVsiZ3d5c3oiXSBpbiByYmJhbm95OgogICAgZWZvd3dsdW8gPSAwCg=='

    def test_diversity_7(self):
        return 'Zm9yICgoa25pbG51IGluIHt9KSBvciB7fSlbM10gaW4gb29udmw6CiAgICB6ZnlvID0gMQo='

    def test_diversity_8(self):
        return 'Zm9yICgodXBlcmkgaW4ge30pIG9yIHt9KVsiZmF1Il0gaW4gcHFoY2R1bG06CiAgICBhYmNwZGIgPSAyCg=='

    def test_diversity_9(self):
        return 'Zm9yICgoanZwdWVnZSBpbiB7fSkgb3Ige30pWyJnb2UiXSBpbiBteXlsOgogICAgcGFzcwo='

    def test_diversity_10(self):
        return 'Zm9yICgoZmZrdGRsIGluIHt9KSBvciB7fSlbImdwbnJteiJdIGluIG5tZXlvOgogICAganl2Z2tucCA9IDYK'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'Zm9yIGhkZHFvIGluIHJlZToKICAgIHBhc3MK'

    def test_diversity_2(self):
        return 'cGRobWd4cCA9IHsiaGVuZmMiOiA4Nn0K'

    def test_diversity_3(self):
        return 'cnpsaSA9IGxhbWJkYSBsbWt3Y3ZtdDogNAo='

    def test_diversity_4(self):
        return 'Zm9yIGdqa3ggaW4gYmdibzoKICAgIHBhc3MK'

    def test_diversity_5(self):
        return 'Zm9yIGd2ZCBpbiBuYmt4dDoKICAgIHBhc3MK'

    def test_diversity_6(self):
        return 'Z2FxamFsID0gWzI2LCA0OCwgMF0K'

    def test_diversity_7(self):
        return 'Zm9yIGtkcmp1IGluIHJqcWQ6CiAgICBwYXNzCg=='

    def test_diversity_8(self):
        return 'd2RzaHMgPSB7InN2biI6IDgyfQo='

    def test_diversity_9(self):
        return 'bnVoam9zdSA9IGxhbWJkYSB3Y2x2c3VvOiAzCg=='

    def test_diversity_10(self):
        return 'Zm9yIGlpanRleG1nIGluIGhzdGFwZDoKICAgIHBhc3MK'
