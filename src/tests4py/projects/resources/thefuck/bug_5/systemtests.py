from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(False, 'git push --set-upstream <remote> <XAlFDlbfbP> SELECT * FROM users', 'fatal: The current branch [XAlFDlbfbP] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [XAlFDlbfbP]')"

    def test_diversity_2(self):
        return "(True, 'git pushpull --set-upstream <remote> <wYmgEjddM>', 'fatal: The current branch [wYmgEjddM] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [wYmgEjddM]')"

    def test_diversity_3(self):
        return "(True, 'git pushpull --set-upstream <remote> <BPAxswNSpNXaIL>', 'fatal: The current branch [BPAxswNSpNXaIL] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [BPAxswNSpNXaIL]')"

    def test_diversity_4(self):
        return "(True, 'git pushpull --set-upstream <remote> <PAZhjMSRVEt>', 'fatal: The current branch [PAZhjMSRVEt] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [PAZhjMSRVEt]')"

    def test_diversity_5(self):
        return "(True, 'git pushpull --set-upstream <remote> <aqxUFs>', 'fatal: The current branch [aqxUFs] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [aqxUFs]')"

    def test_diversity_6(self):
        return "(False, 'git push --set-upstream <remote> <XKZWvorquFw> SELECT * FROM users', 'fatal: The current branch [XKZWvorquFw] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [XKZWvorquFw]')"

    def test_diversity_7(self):
        return "(False, 'git push --set-upstream <remote> <BQEYAmNJYgjcvFv> SELECT * FROM users', 'fatal: The current branch [BQEYAmNJYgjcvFv] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [BQEYAmNJYgjcvFv]')"

    def test_diversity_8(self):
        return "(True, 'git pushpull --set-upstream <remote> <kCFFOfZSUjMf>', 'fatal: The current branch [kCFFOfZSUjMf] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [kCFFOfZSUjMf]')"

    def test_diversity_9(self):
        return "(True, 'git pushpull --set-upstream <remote> <hWnhXpMuvTg>', 'fatal: The current branch [hWnhXpMuvTg] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [hWnhXpMuvTg]')"

    def test_diversity_10(self):
        return "(False, 'git push --set-upstream <remote> <UIwsUMugi> SELECT * FROM users', 'fatal: The current branch [UIwsUMugi] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [UIwsUMugi]')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "(False, 'git pull --set-upstream <remote> <rTwNDpcEEFO>', 'fatal: The current branch [rTwNDpcEEFO] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [rTwNDpcEEFO]')"

    def test_diversity_2(self):
        return "(True, 'git push --set-upstream <remote> <RDWdru>', 'fatal: The current branch [RDWdru] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [RDWdru]')"

    def test_diversity_3(self):
        return "(True, 'git push --set-upstream <remote> <vShuqrZTTpSEpQ>', 'fatal: The current branch [vShuqrZTTpSEpQ] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [vShuqrZTTpSEpQ]')"

    def test_diversity_4(self):
        return "(True, 'git push --set-upstream <remote> <ewmqfwmunqOkbE>', 'fatal: The current branch [ewmqfwmunqOkbE] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [ewmqfwmunqOkbE]')"

    def test_diversity_5(self):
        return "(True, 'git push --set-upstream <remote> <dabNff>', 'fatal: The current branch [dabNff] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [dabNff]')"

    def test_diversity_6(self):
        return "(True, 'git push --set-upstream <remote> <ksAeYgVsYLP>', 'fatal: The current branch [ksAeYgVsYLP] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [ksAeYgVsYLP]')"

    def test_diversity_7(self):
        return "(True, 'git push --set-upstream <remote> <tYlYs>', 'fatal: The current branch [tYlYs] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [tYlYs]')"

    def test_diversity_8(self):
        return "(False, 'git pull --set-upstream <remote> <fTItRIteEMh>', 'fatal: The current branch [fTItRIteEMh] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [fTItRIteEMh]')"

    def test_diversity_9(self):
        return "(False, 'git pull --set-upstream <remote> <wBlVW>', 'fatal: The current branch [wBlVW] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [wBlVW]')"

    def test_diversity_10(self):
        return "(True, 'git push --set-upstream <remote> <RtOkQJ>', 'fatal: The current branch [RtOkQJ] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [RtOkQJ]')"
