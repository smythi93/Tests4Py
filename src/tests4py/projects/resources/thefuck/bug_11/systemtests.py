from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'fatal: The current branch has no upstream jQxxpdKjjQQrSv.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push -u origin'

    def test_diversity_2(self):
        return 'fatal: The current branch has no upstream OtcxtJPYAwuSZ.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push -u origin'

    def test_diversity_3(self):
        return 'fatal: The current branch has no upstream KYuJvD.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push --quiet'

    def test_diversity_4(self):
        return 'fatal: The current branch has no upstream YLzKzrfTrk.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push --quiet'

    def test_diversity_5(self):
        return 'fatal: The current branch has no upstream PBMwqNpmdMHVC.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push --set-upstream origin'

    def test_diversity_6(self):
        return 'fatal: The current branch has no upstream CeXdJqU.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push --quiet'

    def test_diversity_7(self):
        return 'fatal: The current branch has no upstream WkhSAILChI.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push'

    def test_diversity_8(self):
        return 'fatal: The current branch has no upstream MIDEtWCZFkmkqtL.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push'

    def test_diversity_9(self):
        return 'fatal: The current branch has no upstream BPNNKk.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push --quiet'

    def test_diversity_10(self):
        return 'fatal: The current branch has no upstream GhYmMytHrybc.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        ' '' 'git push -u origin'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'git push -u origin' '' 'fatal: The current branch has no upstream BTUMx.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_2(self):
        return 'git push -u origin' '' 'fatal: The current branch has no upstream ftfqV.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_3(self):
        return 'git push --set-upstream origin' '' 'fatal: The current branch has no upstream xBIEXoss.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_4(self):
        return 'git push --quiet' '' 'fatal: The current branch has no upstream xAvuXMD.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_5(self):
        return 'git push' '' 'fatal: The current branch has no upstream HGMoO.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_6(self):
        return 'git push --quiet' '' 'fatal: The current branch has no upstream owCTvO.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_7(self):
        return 'git push' '' 'fatal: The current branch has no upstream WNEhu.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_8(self):
        return 'git push -u origin' '' 'fatal: The current branch has no upstream DWDPgaIJgMxjfg.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_9(self):
        return 'git push' '' 'fatal: The current branch has no upstream zXlPaA.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '

    def test_diversity_10(self):
        return 'git push' '' 'fatal: The current branch has no upstream HWoNqaaOx.\n        To push the current branch and set the remote as upstream, use\n\n            git push --set-upstream origin master\n\n        '
