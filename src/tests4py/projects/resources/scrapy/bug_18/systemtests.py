from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9dnV39m9l'

    def test_diversity_2(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9ZmN2aaNhbi54bWw='

    def test_diversity_3(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9cWNy_Gducy50eHQ='

    def test_diversity_4(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9bHhkemh3YfZvZS50eHQ='

    def test_diversity_5(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9Zm5kcWGjdXouaHRtbA=='

    def test_diversity_6(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9ZWhubulhLnhtbA=='

    def test_diversity_7(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9a2d3YWlr_HkuaHRtbA=='

    def test_diversity_8(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9b2RudXjpdWIueG1s'

    def test_diversity_9(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9bWdhaXhy8S50eHQ='

    def test_diversity_10(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9aHViZWN2Z7VhLmh0bWw='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9ImdxcGV0dC5odG1sIg=='

    def test_diversity_2(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9YXJl'

    def test_diversity_3(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9Z3dmLnR4dA=='

    def test_diversity_4(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9YnNjLnR4dA=='

    def test_diversity_5(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9InRzb2NlLnhtbCI='

    def test_diversity_6(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9InZ5d2ci'

    def test_diversity_7(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9ZHF0cW8='

    def test_diversity_8(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9InRld3FobGpoLmh0bWwi'

    def test_diversity_9(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9Ind3bWhmaGkuaHRtbCI='

    def test_diversity_10(self):
        return 'YXR0YWNobWVudDsgZmlsZW5hbWU9ImF6a3dnbXAuaHRtbCI='
