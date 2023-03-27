from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-p/router/\n-mwebsocket\n-o"

    def test_diversity_2(self):
        return "-p/router/\n-mwebsocket\n-o\n-a"

    def test_diversity_3(self):
        return "-p/router/\n-mwebsocket\n-o\n-a\n-d{}"

    def test_diversity_4(self):
        return "-p/router/\n-mwebsocket\n-o\n-a\n-d[]"

    def test_diversity_5(self):
        return '-p/router/\n-mwebsocket\n-o\n-a\n-d[1,2,0.0,"test"]'

    def test_diversity_6(self):
        return '-p/router/\n-mwebsocket\n-o\n-a\n-d[1,2,0.0,"test"]'

    def test_diversity_7(self):
        return '-a\n-p/router/\n-mwebsocket\n-o\n-d{"d":1,"t":"test"}'

    def test_diversity_8(self):
        return "-a\n-p/router/\n-mwebsocket\n-o"

    def test_diversity_9(self):
        return '-p/router/\n-mwebsocket\n-o\n-d"test"'

    def test_diversity_10(self):
        return "-p/router/\n-mwebsocket\n-o\n-d1"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-p/router/\n-mwebsocket"

    def test_diversity_2(self):
        return "-p/items/valid\n-mget\n-o\n-a"

    def test_diversity_3(self):
        return "-p/router/\n-mwebsocket\n-a\n-d{}"

    def test_diversity_4(self):
        return "-p/router/\n-mwebsocket\n-a\n-d[]"

    def test_diversity_5(self):
        return '-p/items/\n-mpost\n-d{"name":"test-name","price":1.6,"age":5}'

    def test_diversity_6(self):
        return (
            '-p/items/\n-mpost\n-a\n-d{"aliased_name":"test-name","price":1.6,"age":5}'
        )

    def test_diversity_7(self):
        return '-a\n-p/router/\n-mwebsocket\n-d{"d":1,"t":"test"}'

    def test_diversity_8(self):
        return "-p/openapi.json"

    def test_diversity_9(self):
        return '-p/items/valid_list\n-mget\n-o\n-d"test"'

    def test_diversity_10(self):
        return "-p/model\n-mget\n-o\n-d1"
