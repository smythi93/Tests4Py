from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_2(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_3(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_4(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_5(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_6(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_7(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_8(self):
        return "-u /openapi.json -m get -pas /user {user_id} 1"

    def test_diversity_9(self):
        return "-u /openapi.json -m get -pas /user {user_id} 3"

    def test_diversity_10(self):
        return "-u /openapi.json -m get -pas /user {user_id} 2"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-u /openapi.json -m get -pas /user {user_id} 0"

    def test_diversity_2(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_3(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_4(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_5(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_6(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_7(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_8(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_9(self):
        return "-u /openapi.json -m get -gs /user Item"

    def test_diversity_10(self):
        return "-u /openapi.json -m get -gs /user Item"
