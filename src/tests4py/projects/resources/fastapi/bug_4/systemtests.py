from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-p/openapi.json\n-mget\n-u"

    def test_diversity_2(self):
        return "-p/openapi.json\n-a\n-mget\n-u"

    def test_diversity_3(self):
        return "-p/openapi.json\n-a\n-mget\n-u\n-o"

    def test_diversity_4(self):
        return "-p/openapi.json\n-a\n-o\n-mget\n-u"

    def test_diversity_5(self):
        return '-p/openapi.json\n-a\n-o\n-mget\n-d[1,2,0.0,"test"]\n-u'

    def test_diversity_6(self):
        return '-p/openapi.json\n-mget\n-a\n-d[1,2,0.0,"test"]\n-u'

    def test_diversity_7(self):
        return "-a\n-p/openapi.json\n-o\n-mget\n-u"

    def test_diversity_8(self):
        return (
            '-p/openapi.json\n-mget\n-o\n-d{"name":"test-name","price":1.6,"age":5}\n-u'
        )

    def test_diversity_9(self):
        return '-p/openapi.json\n-mget\n-a\n-d"test"\n-u'

    def test_diversity_10(self):
        return "-p/openapi.json\n-mget\n-d1\n-u"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-p/router/\n-mwebsocket\n-a"

    def test_diversity_2(self):
        return "-p/user/1\n-mget\n-u"

    def test_diversity_3(self):
        return "-p/items/valid\n-mget"

    def test_diversity_4(self):
        return (
            '-p/form/python-set\n-d{"items":["first","second","third"]}\n-mpost\n-a\n-o'
        )

    def test_diversity_5(self):
        return '-p/items/\n-mpost\n-d{"name":"test-name","price":1.6,"age":5}'

    def test_diversity_6(self):
        return (
            '-p/items/\n-mpost\n-a\n-d{"aliased_name":"test-name","price":1.6,"age":5}'
        )

    def test_diversity_7(self):
        return '-p/items/valid\n-mget\n-o\n-d[1,2,0.0,"test"]'

    def test_diversity_8(self):
        return "-p/openapi.json"

    def test_diversity_9(self):
        return '-p/items/valid_list\n-mget\n-o\n-d"test"'

    def test_diversity_10(self):
        return "-p/model\n-mget\n-o\n-d1"
