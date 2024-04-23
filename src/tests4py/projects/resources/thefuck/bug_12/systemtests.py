from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'gu run CNaYQBCSymsiX.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_2(self):
        return 'gu run ynvDa.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_3(self):
        return 'gu run tBkitY.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_4(self):
        return 'gu run KHmmVxKERzQGpc.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_5(self):
        return 'gu run kaTrEIilpqTNb.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_6(self):
        return 'gu run KQhVZ.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_7(self):
        return 'gu run kjQPDGL.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_8(self):
        return 'gu run EbOAupaL.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_9(self):
        return 'gu run yupziuoo.go' '' 'gu: not found, maybe you meant "go"'

    def test_diversity_10(self):
        return 'gu run ARSGpThVBQO.go' '' 'gu: not found, maybe you meant "go"'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'got commit -m jBgySrnKjrlVUN' '' 'got: not found, maybe you meant "git"'

    def test_diversity_2(self):
        return 'got commit -m IEogeEW' '' 'got: not found, maybe you meant "git"'

    def test_diversity_3(self):
        return 'vom INxwxW.py' '' 'vom: not found, maybe you meant "vim"'

    def test_diversity_4(self):
        return 'vom MoAwT.py' '' 'vom: not found, maybe you meant "vim"'

    def test_diversity_5(self):
        return 'vom cSsmtRPwn.py' '' 'vom: not found, maybe you meant "vim"'

    def test_diversity_6(self):
        return 'vom RlhNFbBtbO.py' '' 'vom: not found, maybe you meant "vim"'

    def test_diversity_7(self):
        return 'got commit -m oVUZgKT' '' 'got: not found, maybe you meant "git"'

    def test_diversity_8(self):
        return 'vom aabaJUO.py' '' 'vom: not found, maybe you meant "vim"'

    def test_diversity_9(self):
        return 'vom CfzzGQqxelbKU.py' '' 'vom: not found, maybe you meant "vim"'

    def test_diversity_10(self):
        return 'sudo fucck OAoafNFNHLVCtGK' '' 'fuckk: not found, maybe you meant "fsck"'

