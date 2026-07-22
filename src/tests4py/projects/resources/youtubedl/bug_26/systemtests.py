from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcImRjeXVhc1wiOjIwMDB9IiwgImV4cGVjdGVkIjogeyJkY3l1YXMiOiAyMDAwfX0='

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcImF6YXFcIjo4MDAwMH0iLCAiZXhwZWN0ZWQiOiB7ImF6YXEiOiA4MDAwMH19'

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcImRlY2FtelwiOjIwMDAwfSIsICJleHBlY3RlZCI6IHsiZGVjYW16IjogMjAwMDB9fQ=='

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcImJybmJ2YlwiOjUwMDB9IiwgImV4cGVjdGVkIjogeyJicm5idmIiOiA1MDAwfX0='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImdyZndyXCI6OTAwfSIsICJleHBlY3RlZCI6IHsiZ3Jmd3IiOiA5MDB9fQ=='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImlzclwiOjMwMH0iLCAiZXhwZWN0ZWQiOiB7ImlzciI6IDMwMH19'

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInBlb1wiOjMwMH0iLCAiZXhwZWN0ZWQiOiB7InBlbyI6IDMwMH19'

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInV5ZGhiXCI6NTAwMDB9IiwgImV4cGVjdGVkIjogeyJ1eWRoYiI6IDUwMDAwfX0='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcImVleVwiOjMwMDB9IiwgImV4cGVjdGVkIjogeyJlZXkiOiAzMDAwfX0='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcIm90bVwiOjgwMDB9IiwgImV4cGVjdGVkIjogeyJvdG0iOiA4MDAwfX0='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcInVtdlwiOjQ4fSIsICJleHBlY3RlZCI6IHsidW12IjogNDh9fQ=='

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcImhkZWxkblwiOjQ4M30iLCAiZXhwZWN0ZWQiOiB7ImhkZWxkbiI6IDQ4M319'

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcImlzdmVcIjo5ODl9IiwgImV4cGVjdGVkIjogeyJpc3ZlIjogOTg5fX0='

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcInVsYmtiXCI6ODI4fSIsICJleHBlY3RlZCI6IHsidWxia2IiOiA4Mjh9fQ=='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImhscHdyXCI6MTJ9IiwgImV4cGVjdGVkIjogeyJobHB3ciI6IDEyfX0='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcIm52anduc1wiOjkyfSIsICJleHBlY3RlZCI6IHsibnZqd25zIjogOTJ9fQ=='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInZubVwiOjUyMTJ9IiwgImV4cGVjdGVkIjogeyJ2bm0iOiA1MjEyfX0='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInZiaWFcIjoxMTg5fSIsICJleHBlY3RlZCI6IHsidmJpYSI6IDExODl9fQ=='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcImx0ZlwiOjQ4OTV9IiwgImV4cGVjdGVkIjogeyJsdGYiOiA0ODk1fX0='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcImtyd3ZjXCI6MzQ2fSIsICJleHBlY3RlZCI6IHsia3J3dmMiOiAzNDZ9fQ=='
