from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '(\'git add -- HSMKaZwkGYDNPn && git submodule update HSMKaZwkGYDNPn\', \'GIT SUBMODULE UPDATE HSMKaZwkGYDNPn\', "error: pathspec \'HSMKaZwkGYDNPn\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_2(self):
        return '(\'git add -- WoMbLBIOg && git submodule update WoMbLBIOg\', \'GIT SUBMODULE UPDATE WoMbLBIOg\', "error: pathspec \'WoMbLBIOg\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_3(self):
        return "(True, 'git submodule update ofVFcPiD', '')"

    def test_diversity_4(self):
        return "(True, 'git submodule update diUqwTMMVu', '')"

    def test_diversity_5(self):
        return '(\'git add -- vBdmWfIUMoVsjl && git submodule update vBdmWfIUMoVsjl\', \'GIT SUBMODULE UPDATE vBdmWfIUMoVsjl\', "error: pathspec \'vBdmWfIUMoVsjl\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_6(self):
        return '(\'git add -- tzhEdJDAfZGMVYN && git submodule update tzhEdJDAfZGMVYN\', \'GIT SUBMODULE UPDATE tzhEdJDAfZGMVYN\', "error: pathspec \'tzhEdJDAfZGMVYN\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_7(self):
        return "(True, 'git submodule update HEXzcsy', '')"

    def test_diversity_8(self):
        return "(True, 'git commit MtaNUFAO', '')"

    def test_diversity_9(self):
        return '(\'git add -- XSjuaABxhq && git submodule update XSjuaABxhq\', \'GIT SUBMODULE UPDATE XSjuaABxhq\', "error: pathspec \'XSjuaABxhq\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_10(self):
        return "(True, 'git commit jPlZIm', '')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '(\'git add -- AbTNMRpePlsP && git submodule update AbTNMRpePlsP\', \'git submodule update AbTNMRpePlsP\', "error: pathspec \'AbTNMRpePlsP\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_2(self):
        return '(True, \'git submodule update ySdTulFQbr\', "error: pathspec \'ySdTulFQbr\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_3(self):
        return '(True, \'git submodule update wUdpuXbqyOT\', "error: pathspec \'wUdpuXbqyOT\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_4(self):
        return '(\'git add -- CerUwJlZQXZ && git commit CerUwJlZQXZ\', \'git commit CerUwJlZQXZ\', "error: pathspec \'CerUwJlZQXZ\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_5(self):
        return '(True, \'git commit QjkbwHNSoXIzkC\', "error: pathspec \'QjkbwHNSoXIzkC\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_6(self):
        return '(\'git add -- xdnnLiFQpjmX && git submodule update xdnnLiFQpjmX\', \'git submodule update xdnnLiFQpjmX\', "error: pathspec \'xdnnLiFQpjmX\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_7(self):
        return '(True, \'git submodule update MztqOvBgwTTWvf\', "error: pathspec \'MztqOvBgwTTWvf\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_8(self):
        return '(\'git add -- gOGuMWQHxaUbr && git submodule update gOGuMWQHxaUbr\', \'git submodule update gOGuMWQHxaUbr\', "error: pathspec \'gOGuMWQHxaUbr\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_9(self):
        return '(\'git add -- AjkvkSdbAZ && git commit AjkvkSdbAZ\', \'git commit AjkvkSdbAZ\', "error: pathspec \'AjkvkSdbAZ\' did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_10(self):
        return '(\'git add -- UkRXVRfFJOdPcl && git commit UkRXVRfFJOdPcl\', \'git commit UkRXVRfFJOdPcl\', "error: pathspec \'UkRXVRfFJOdPcl\' did not match any file(s) known to git. Did you forget to \'git add\'?")'
