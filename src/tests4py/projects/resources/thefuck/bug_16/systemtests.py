from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(1, 'TF_CMD=$(TF_ALIAS=fuck', 'fuck')"

    def test_diversity_2(self):
        return '(1, "alias fuck=\'TF_CMD=$(TF_ALIAS=", \'fuck\')'

    def test_diversity_3(self):
        return "(1, 'TF_CMD=$(TF_ALIAS=fuck PYTHONIOENCODING', 'fuck')"

    def test_diversity_4(self):
        return "(1, '$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8', 'fuck')"

    def test_diversity_5(self):
        return '(1, "\'TF_CMD=$(TF_ALIAS=fuck", \'fuck\')'

    def test_diversity_6(self):
        return "(1, '=$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES', 'fuck')"

    def test_diversity_7(self):
        return "(2, 'TF_CMD=$(TF_ALIAS=fuck', 'fuck')"

    def test_diversity_8(self):
        return "(2, '$(alias) thefuck $(fc -ln -1 | tail', 'fuck')"

    def test_diversity_9(self):
        return '(2, "alias fuck=\'TF_CMD=$(TF_ALIAS=fuck", \'fuck\')'

    def test_diversity_10(self):
        return "(2, 'PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES=$(alias) thefuck', 'fuck')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "(1, 'PYTHONIOENCODING=utf-8', 'fuck')"

    def test_diversity_2(self):
        return "(1, 'TF_SHELL_ALIASES=$(alias)', 'fuck')"

    def test_diversity_3(self):
        return "(1, 'eval $TF_CMD', 'fuck')"

    def test_diversity_4(self):
        return "(1, 'history -s $TF_CMD', 'fuck')"

    def test_diversity_5(self):
        return "(1, '$(fc -ln -1)', 'fuck')"

    def test_diversity_6(self):
        return "(2, 'PYTHONIOENCODING=utf-8', 'fuck')"

    def test_diversity_7(self):
        return "(2, 'TF_SHELL_ALIASES=$(alias)', 'fuck')"

    def test_diversity_8(self):
        return "(2, 'eval $TF_CMD', 'fuck')"

    def test_diversity_9(self):
        return "(2, 'print -s $TF_CMD', 'fuck')"

    def test_diversity_10(self):
        return "(2, 'tail -n 1', 'fuck')"
