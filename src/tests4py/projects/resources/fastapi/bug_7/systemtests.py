from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_2(self):
        return '-ps /item ItemLower -u /item -m post -d {\\"name\\":\\"name\\",\\"age\\":100}'

    def test_diversity_3(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_4(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_5(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_6(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_7(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_8(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_9(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'

    def test_diversity_10(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":-1}'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_2(self):
        return '-ps /item ItemLower -u /item -m post -d {\\"name\\":\\"name\\",\\"age\\":5}'

    def test_diversity_3(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_4(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_5(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_6(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_7(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_8(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_9(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'

    def test_diversity_10(self):
        return '-ps /item Item -u /item -m post -d {\\"name\\":\\"name\\",\\"price\\":1.0,\\"age\\":5}'
