from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_2(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_3(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_4(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_5(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_6(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_7(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_8(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_9(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"

    def test_diversity_10(self):
        return "-ps /a Item -mt application/vnd.api+json -e -m get -u /openapi.json"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-ps /a Item -mt application/json -e -m get -u /openapi.json"

    def test_diversity_2(self):
        return (
            "-ps /a ItemLower -mt application/vnd.api+json -e -m post -u /a "
            '-d {\\"m\\":{\\"name\\":\\"name\\",\\"age\\":5}}'
        )

    def test_diversity_3(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"

    def test_diversity_4(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"

    def test_diversity_5(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"

    def test_diversity_6(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"

    def test_diversity_7(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"

    def test_diversity_8(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"

    def test_diversity_9(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"

    def test_diversity_10(self):
        return "-ps /a Item -mt application/vnd.api+json -m get -u /openapi.json"
