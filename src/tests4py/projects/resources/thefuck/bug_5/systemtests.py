from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'git push --set-upstream <remote> <A>', b'fatal: The current branch [A] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [A]'

    def test_diversity_2(self):
        return 'git pull --set-upstream <remote> <B>', b'fatal: The current branch [B] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [B]'

    def test_diversity_3(self):
        return 'git push --set-upstream <remote> <C>', b'fatal: The current branch [C] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [C]'

    def test_diversity_4(self):
        return 'git push --set-upstream <remote> <U>', 1

    def test_diversity_5(self):
        return 'git push --set-upstream <remote> <K>', b'fatal: The current branch [K] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [K]'

    def test_diversity_6(self):
        return 'git push --set-upstream <remote> <L>', b'fatal: The current branch [L] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [L]'

    def test_diversity_7(self):
        return 'git pull --set-upstream <remote> <M>', b'fatal: The current branch [M] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [M]'

    def test_diversity_8(self):
        return 'git push --set-upstream <remote> <S>', 100

    def test_diversity_9(self):
        return 'git push --set-upstream <remote> <Q>', b'fatal: The current branch [Q] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [Q]'

    def test_diversity_10(self):
        return 'git push --set-upstream <remote> <T>', 1000


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'git push --set-upstream <remote> <a>', 'fatal: The current branch [a] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [a]'

    def test_diversity_2(self):
        return 'git push --set-upstream <remote> <b>', 'fatal: The current branch [b] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [b]'

    def test_diversity_3(self):
        return 'git push --set-upstream <remote> <c>', 'fatal: The current branch [c] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [c]'

    def test_diversity_4(self):
        return 'git push --set-upstream <remote> <d>', 'fatal: The current branch [d] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [d]'

    def test_diversity_5(self):
        return 'git push --set-upstream <remote> <e>', 'fatal: The current branch [e] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [e]'

    def test_diversity_6(self):
        return 'git pull --set-upstream <remote> <f>', 'fatal: The current branch [f] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [f]'

    def test_diversity_7(self):
        return 'git pull --set-upstream <remote> <g>', 'fatal: The current branch [g] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [g]'

    def test_diversity_8(self):
        return 'git pull --set-upstream <remote> <h>', 'fatal: The current branch [h] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [h]'

    def test_diversity_9(self):
        return 'git pull --set-upstream <remote> <i>', 'fatal: The current branch [i] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [i]'

    def test_diversity_10(self):
        return 'git pull --set-upstream <remote> <j>', 'fatal: The current branch [j] has no upstream branch.To push the current branch and set the remote as upstream, use git push --set-upstream origin [j]'
