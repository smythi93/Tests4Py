from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'git submodule update WlkCUZEtaY' '' ''

    def test_diversity_2(self):
        return 'GIT SUBMODULE UPDATE uFaPMZwppSyHv' '' "error: pathspec 'uFaPMZwppSyHv' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_3(self):
        return 'GIT COMMIT DfxaSUY' '' "error: pathspec 'DfxaSUY' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_4(self):
        return 'GIT COMMIT IAjrih' '' "error: pathspec 'IAjrih' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_5(self):
        return 'git commit MvrDrCNhPBHuC' '' ''

    def test_diversity_6(self):
        return 'GIT COMMIT MDucHVJByA' '' "error: pathspec 'MDucHVJByA' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_7(self):
        return 'GIT SUBMODULE UPDATE vQTgaBNoDRdqYfH' '' "error: pathspec 'vQTgaBNoDRdqYfH' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_8(self):
        return 'GIT COMMIT ahntm' '' "error: pathspec 'ahntm' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_9(self):
        return 'GIT SUBMODULE UPDATE AEngDNAxMSk' '' "error: pathspec 'AEngDNAxMSk' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_10(self):
        return 'GIT SUBMODULE UPDATE aaSFKv' '' "error: pathspec 'aaSFKv' did not match any file(s) known to git. Did you forget to 'git add'?"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'git submodule update MmhXCRUzYjMes' '' "error: pathspec 'MmhXCRUzYjMes' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_2(self):
        return 'git submodule update GvrASrhVna' '' "error: pathspec 'GvrASrhVna' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_3(self):
        return 'git submodule update mhkPyqnYMONl' '' "error: pathspec 'mhkPyqnYMONl' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_4(self):
        return 'git commit TduHTBC' '' "error: pathspec 'TduHTBC' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_5(self):
        return 'git commit xSxlBlHhuHZ' '' "error: pathspec 'xSxlBlHhuHZ' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_6(self):
        return 'git commit bNxDAd' '' "error: pathspec 'bNxDAd' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_7(self):
        return 'git submodule update JRSQS' '' "error: pathspec 'JRSQS' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_8(self):
        return 'git submodule update wfqpuEIwxnxMp' '' "error: pathspec 'wfqpuEIwxnxMp' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_9(self):
        return 'git commit toFLkaI' '' "error: pathspec 'toFLkaI' did not match any file(s) known to git. Did you forget to 'git add'?"

    def test_diversity_10(self):
        return 'git commit FYYTFHiYpD' '' "error: pathspec 'FYYTFHiYpD' did not match any file(s) known to git. Did you forget to 'git add'?"
