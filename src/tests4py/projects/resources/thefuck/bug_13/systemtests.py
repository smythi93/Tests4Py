from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '(False, \'git branch -d gJpIHuXjyQtrEq SELECT * FROM database\', "fatal: A branch named \'gJpIHuXjyQtrEq\' already exists.")'

    def test_diversity_2(self):
        return '(False, \'git branch -d uZbrQufnDiqAvAN SELECT * FROM database\', "fatal: A branch named \'uZbrQufnDiqAvAN\' already exists.")'

    def test_diversity_3(self):
        return '([\'git branch -d YXgxOmC, git branch YXgxOmC\'], \'git branch -d YXgxOmC\', "fatal: A branch named \'YXgxOmC\' already exists.")'

    def test_diversity_4(self):
        return '([\'git branch -d bZfjLfKtblqgkp, git branch bZfjLfKtblqgkp\'], \'git branch -d bZfjLfKtblqgkp\', "fatal: A branch named \'bZfjLfKtblqgkp\' already exists.")'

    def test_diversity_5(self):
        return '(False, \'git branch -D RMSBkC SELECT * FROM database\', "fatal: A branch named \'RMSBkC\' already exists.")'

    def test_diversity_6(self):
        return '(False, \'git branch -D kzUePRtLnHA SELECT * FROM database\', "fatal: A branch named \'kzUePRtLnHA\' already exists.")'

    def test_diversity_7(self):
        return '(False, \'git branch -d NMFgWrIMCgkD SELECT * FROM database\', "fatal: A branch named \'NMFgWrIMCgkD\' already exists.")'

    def test_diversity_8(self):
        return '(False, \'git branch -D DUxwbF SELECT * FROM database\', "fatal: A branch named \'DUxwbF\' already exists.")'

    def test_diversity_9(self):
        return '(False, \'git branch -D PoSVXhtvGGjFu SELECT * FROM database\', "fatal: A branch named \'PoSVXhtvGGjFu\' already exists.")'

    def test_diversity_10(self):
        return '(False, \'git branch -d zoiMLRQupfw SELECT * FROM database\', "fatal: A branch named \'zoiMLRQupfw\' already exists.")'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '(True, \'git branch -d pzrHbtjFCRjo\', "fatal: A branch named \'pzrHbtjFCRjo already exists.")'

    def test_diversity_2(self):
        return '(\'git branch -d OtXCoWzH && git branch OtXCoWzH\', \'git branch -d OtXCoWzH\', "fatal: A branch named \'OtXCoWzH\' already exists.")'

    def test_diversity_3(self):
        return '(\'git branch -d XHllDSLGzfe && git branch XHllDSLGzfe\', \'git branch -d XHllDSLGzfe\', "fatal: A branch named \'XHllDSLGzfe\' already exists.")'

    def test_diversity_4(self):
        return '(True, \'git branch -d xqNNWBNHnntXN\', "fatal: A branch named \'xqNNWBNHnntXN already exists.")'

    def test_diversity_5(self):
        return '(\'git branch -d FcwwGEtRKGOs && git branch FcwwGEtRKGOs\', \'git branch -d FcwwGEtRKGOs\', "fatal: A branch named \'FcwwGEtRKGOs\' already exists.")'

    def test_diversity_6(self):
        return '(\'git branch -d IFiSy && git branch IFiSy\', \'git branch -d IFiSy\', "fatal: A branch named \'IFiSy\' already exists.")'

    def test_diversity_7(self):
        return '(\'git branch -d kBEISHKfWXIHN && git branch kBEISHKfWXIHN\', \'git branch -d kBEISHKfWXIHN\', "fatal: A branch named \'kBEISHKfWXIHN\' already exists.")'

    def test_diversity_8(self):
        return '(\'git branch -d OSuDTEellE && git branch OSuDTEellE\', \'git branch -d OSuDTEellE\', "fatal: A branch named \'OSuDTEellE\' already exists.")'

    def test_diversity_9(self):
        return '(\'git branch -d FooLd && git branch FooLd\', \'git branch -d FooLd\', "fatal: A branch named \'FooLd\' already exists.")'

    def test_diversity_10(self):
        return '(\'git branch -d VQQQcS && git branch VQQQcS\', \'git branch -d VQQQcS\', "fatal: A branch named \'VQQQcS\' already exists.")'
