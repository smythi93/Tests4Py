from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('TF_SHELL_ALIASES=$(alias) thefuck', 'fuck')"

    def test_diversity_2(self):
        return "('$(TF_SHELL_ALIASES=$(alias) thefuck', 'fuck')"

    def test_diversity_3(self):
        return "('TF_CMD=$(TF_SHELL_ALIASES=', 'fuck')"

    def test_diversity_4(self):
        return "('=$(TF_SHELL_ALIASES=$(alias) thefuck $', 'fuck')"

    def test_diversity_5(self):
        return "('TF_SHELL_ALIASES=$(alias) thefuck $(', 'fuck')"

    def test_diversity_6(self):
        return "('$(TF_SHELL_ALIASES=$(alias) thefuck $(fc', 'fuck')"

    def test_diversity_7(self):
        return "('TF_CMD=$(TF_SHELL_ALIASES=$(alias)', 'fuck')"

    def test_diversity_8(self):
        return "('TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln', 'fuck')"

    def test_diversity_9(self):
        return "('$(alias) thefuck $(fc -ln -1))', 'fuck')"

    def test_diversity_10(self):
        return "('TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln -1', 'fuck')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('PYTHONIOENCODING=utf-8', 'fuck')"

    def test_diversity_2(self):
        return "('eval $TF_CMD', 'fuck')"

    def test_diversity_3(self):
        return "('TF_ALIAS=fuck', 'fuck')"

    def test_diversity_4(self):
        return "('$(fc -ln -1)', 'fuck')"

    def test_diversity_5(self):
        return "('history -s $TF_CMD', 'fuck')"

    def test_diversity_6(self):
        return "('alias fuck=', 'fuck')"

    def test_diversity_7(self):
        return "('TF_CMD=$(', 'fuck')"

    def test_diversity_8(self):
        return "('thefuck $(fc -ln -1)', 'fuck')"

    def test_diversity_9(self):
        return "('&& history -s $TF_CMD', 'fuck')"

    def test_diversity_10(self):
        return "('=utf-8 TF_CMD=', 'fuck')"
