from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'git push --force' '' 'fatal: The current branch zrimJLik has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin zrimJLik\n\n'

    def test_diversity_2(self):
        return 'git push -u' '' 'fatal: The current branch PhFFXQPi has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin PhFFXQPi\n\n'

    def test_diversity_3(self):
        return 'git push --force' '' 'fatal: The current branch ywkehehi has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin ywkehehi\n\n'

    def test_diversity_4(self):
        return 'git push -u' '' 'fatal: The current branch uqgajskg has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin uqgajskg\n\n'

    def test_diversity_5(self):
        return 'git push --force' '' 'fatal: The current branch irkjtkhiufh has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin irkjtkhiufh\n\n'

    def test_diversity_6(self):
        return 'git push -u' '' 'fatal: The current branch IWENKhjdk has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin IWENKhjdk\n\n'

    def test_diversity_7(self):
        return 'git push --force' '' 'fatal: The current branch qwgJGKG has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin qwgJGKG\n\n'

    def test_diversity_8(self):
        return 'git push -u' '' 'fatal: The current branch turqkqjh has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin turqkqjh\n\n'

    def test_diversity_9(self):
        return 'git push --force' '' 'fatal: The current branch tyquJHGASH has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin tyquJHGASH\n\n'

    def test_diversity_10(self):
        return 'git push -u' '' 'fatal: The current branch qlkhqKLASLK has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin qlkhqKLASLK\n\n'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'git push --quiet' '' 'fatal: The current branch lLrFtBdCw has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin lLrFtBdCw\n\n'

    def test_diversity_2(self):
        return 'git push -u origin' '' 'fatal: The current branch uUgFj has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin uUgFj\n\n'

    def test_diversity_3(self):
        return 'git push --set-upstream origin' '' 'fatal: The current branch uekrhhdkNJ has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin uekrhhdkNJ\n\n'

    def test_diversity_4(self):
        return 'git push' '' 'fatal: The current branch ICvphXa has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin ICvphXa\n\n'

    def test_diversity_5(self):
        return 'git push -u origin' '' 'fatal: The current branch iwehrwiitib has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin iwehrwiitib\n\n'

    def test_diversity_6(self):
        return 'git push --quiet' '' 'fatal: The current branch yeundnja has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin yeundnja\n\n'

    def test_diversity_7(self):
        return 'git push --set-upstream origin' '' 'fatal: The current branch PBpThyQBskQk has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin PBpThyQBskQk\n\n'

    def test_diversity_8(self):
        return 'git push' '' 'fatal: The current branch UkjkYGK has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin UkjkYGK\n\n'

    def test_diversity_9(self):
        return 'git push -u origin' '' 'fatal: The current branch twohwhbewf has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin twohwhbewf\n\n'

    def test_diversity_10(self):
        return 'git push --quiet' '' 'fatal: The current branch wjgkrgfe has no upstream branch.\nTo push the current branch and set the remote as upstream, use\n\n    git push --set-upstream origin wjgkrgfe\n\n'
