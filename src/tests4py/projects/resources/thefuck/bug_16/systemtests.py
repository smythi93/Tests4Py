from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('2', '$(TF_ALIAS=RxrEmTykRpRLw PYTHONIOENCODING', 'RxrEmTykRpRLw')"

    def test_diversity_2(self):
        return '(\'2\', "alias kjoXZONJd=\'TF_CMD=$(TF_ALIAS", \'kjoXZONJd\')'

    def test_diversity_3(self):
        return "('1', '$(TF_ALIAS=PUvfjUlfpEK PYTHONIOENCODING', 'PUvfjUlfpEK')"

    def test_diversity_4(self):
        return "('2', '  eval $TF_CMD ', 'YQFlwEkiZvoVy')"

    def test_diversity_5(self):
        return '(\'1\', "alias xGAxSrZxE=\'TF_CMD=$(TF_ALIAS", \'xGAxSrZxE\')'

    def test_diversity_6(self):
        return '(\'1\', "alias iRZHfgPDptlH=\'TF_CMD=$(TF_ALIAS", \'iRZHfgPDptlH\')'

    def test_diversity_7(self):
        return '(\'1\', "alias hkbqDGmGdNPHYu=\'TF_CMD=$(TF_ALIAS", \'hkbqDGmGdNPHYu\')'

    def test_diversity_8(self):
        return '(\'2\', "alias ZhFCKzdHA=\'TF_CMD=$(TF_ALIAS", \'ZhFCKzdHA\')'

    def test_diversity_9(self):
        return '(\'1\', "alias MKTItdvllUsaCuh=\'TF_CMD=$(TF_ALIAS", \'MKTItdvllUsaCuh\')'

    def test_diversity_10(self):
        return '(\'1\', "alias DRkchepUQIkW=\'TF_CMD=$(TF_ALIAS", \'DRkchepUQIkW\')'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('1', ' history -s $TF_CMD', 'DFjWDtfG')"

    def test_diversity_2(self):
        return "('2', 'PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES', 'LzFQC')"

    def test_diversity_3(self):
        return "('1', '  eval $TF_CMD ', 'mlYjGdDrOQi')"

    def test_diversity_4(self):
        return "('1', '  eval $TF_CMD ', 'QfpONXMV')"

    def test_diversity_5(self):
        return "('2', 'TF_ALIAS=GcknwHhtpEpMOaU', 'GcknwHhtpEpMOaU')"

    def test_diversity_6(self):
        return "('1', 'TF_ALIAS=fiPUOVLPde', 'fiPUOVLPde')"

    def test_diversity_7(self):
        return "('1', 'PYTHONIOENCODING=utf-8', 'bTJqzaV')"

    def test_diversity_8(self):
        return "('1', 'TF_ALIAS=FfYgnqXoFhZbH', 'FfYgnqXoFhZbH')"

    def test_diversity_9(self):
        return "('2', 'PYTHONIOENCODING=utf-8', 'JVnRTw')"

    def test_diversity_10(self):
        return "('1', 'PYTHONIOENCODING=utf-8', 'dHEXMqAmiqVU')"
