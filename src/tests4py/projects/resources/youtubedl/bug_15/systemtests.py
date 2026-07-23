from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcImRjeXVhc1wiOjJlNn0iLCAiZXhwZWN0ZWQiOiB7ImRjeXVhcyI6IDIwMDAwMDAuMH19'

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcImF1aVwiOjhlOH0iLCAiZXhwZWN0ZWQiOiB7ImF1aSI6IDgwMDAwMDAwMC4wfX0='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcImVjYVwiOjhlNH0iLCAiZXhwZWN0ZWQiOiB7ImVjYSI6IDgwMDAwLjB9fQ=='

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcImJybmJ2YlwiOjVFOH0iLCAiZXhwZWN0ZWQiOiB7ImJybmJ2YiI6IDUwMDAwMDAwMC4wfX0='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImd5bG5hXCI6OWUyfSIsICJleHBlY3RlZCI6IHsiZ3lsbmEiOiA5MDAuMH19'

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImRtamJwXCI6M2UyfSIsICJleHBlY3RlZCI6IHsiZG1qYnAiOiAzMDAuMH19'

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcImFqY25cIjo1ZTh9IiwgImV4cGVjdGVkIjogeyJhamNuIjogNTAwMDAwMDAwLjB9fQ=='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcImh1ZWV5ZVwiOjhFMX0iLCAiZXhwZWN0ZWQiOiB7Imh1ZWV5ZSI6IDgwLjB9fQ=='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcIm1wbWJ5XCI6M0U4fSIsICJleHBlY3RlZCI6IHsibXBtYnkiOiAzMDAwMDAwMDAuMH19'

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcImh1a3R5XCI6MkU4fSIsICJleHBlY3RlZCI6IHsiaHVrdHkiOiAyMDAwMDAwMDAuMH19'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcInFpc3ZlXCI6NDQxM30iLCAiZXhwZWN0ZWQiOiB7InFpc3ZlIjogNDQxM319'

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcInd6aXVcIjoxMTYwfSIsICJleHBlY3RlZCI6IHsid3ppdSI6IDExNjB9fQ=='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcImtiaFwiOjYyM30iLCAiZXhwZWN0ZWQiOiB7ImtiaCI6IDYyM319'

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcIm5jeXNcIjo1MTk0fSIsICJleHBlY3RlZCI6IHsibmN5cyI6IDUxOTR9fQ=='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcInliZ2JsXCI6MzMwOH0iLCAiZXhwZWN0ZWQiOiB7InliZ2JsIjogMzMwOH19'

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImtzeFwiOjgyMDF9IiwgImV4cGVjdGVkIjogeyJrc3giOiA4MjAxfX0='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInZqd25cIjo2OTAxfSIsICJleHBlY3RlZCI6IHsidmp3biI6IDY5MDF9fQ=='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInlmYmpcIjoyNTA4fSIsICJleHBlY3RlZCI6IHsieWZiaiI6IDI1MDh9fQ=='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcInh5bWRiZVwiOjIzNzV9IiwgImV4cGVjdGVkIjogeyJ4eW1kYmUiOiAyMzc1fX0='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcInNlclwiOjk5N30iLCAiZXhwZWN0ZWQiOiB7InNlciI6IDk5N319'
