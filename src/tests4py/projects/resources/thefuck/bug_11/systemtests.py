from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('git push --set-upstream origin master --quiet', 'fatal: The current branch has no upstream WIOrnZnxSI.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push --quiet')"

    def test_diversity_2(self):
        return "('git push --set-upstream origin master -u origin', 'fatal: The current branch has no upstream CLjyVKG.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push -u origin')"

    def test_diversity_3(self):
        return "('git push --set-upstream origin master --quiet', 'fatal: The current branch has no upstream rnzLboSwpCJiKE.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push --quiet')"

    def test_diversity_4(self):
        return "('git push --set-upstream origin master --set-upstream origin', 'fatal: The current branch has no upstream egNsoyCLkIoP.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push --set-upstream origin')"

    def test_diversity_5(self):
        return "('git push --set-upstream origin master --quiet', 'fatal: The current branch has no upstream uDlElg.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push --quiet')"

    def test_diversity_6(self):
        return "('git push --set-upstream origin master -u origin', 'fatal: The current branch has no upstream lECGllDGvHnlU.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push -u origin')"

    def test_diversity_7(self):
        return "('git push --set-upstream origin master -u origin', 'fatal: The current branch has no upstream dVgNcZU.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push -u origin')"

    def test_diversity_8(self):
        return "('git push --set-upstream origin master --set-upstream origin', 'fatal: The current branch has no upstream HdIcHHjwIE.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push --set-upstream origin')"

    def test_diversity_9(self):
        return "('git push --set-upstream origin master --quiet', 'fatal: The current branch has no upstream PnstRwxVHJRixI.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push --quiet')"

    def test_diversity_10(self):
        return "('git push --set-upstream origin master -u origin', 'fatal: The current branch has no upstream XzPGPi.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ', 'git push -u origin')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('git push --set-upstream origin master -u origin', 'git push -u origin', 'fatal: The current branch has no upstream irnhVMq.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_2(self):
        return "('git push --set-upstream origin master --quiet', 'git push --quiet', 'fatal: The current branch has no upstream QzEGvAhJ.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_3(self):
        return "('git push --set-upstream origin master --set-upstream origin', 'git push --set-upstream origin', 'fatal: The current branch has no upstream okUYRvooqBbMo.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_4(self):
        return "('git push --set-upstream origin master', 'git push', 'fatal: The current branch has no upstream aNFTcwZlTTtaGRK.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_5(self):
        return "('git push --set-upstream origin master -u origin', 'git push -u origin', 'fatal: The current branch has no upstream szmmJ.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_6(self):
        return "('git push --set-upstream origin master --set-upstream origin', 'git push --set-upstream origin', 'fatal: The current branch has no upstream ptCdt.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_7(self):
        return "('git push --set-upstream origin master --quiet', 'git push --quiet', 'fatal: The current branch has no upstream XBZIpcsuxPf.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_8(self):
        return "('git push --set-upstream origin master', 'git push', 'fatal: The current branch has no upstream IHDUjlKzdOzyQkJ.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_9(self):
        return "('git push --set-upstream origin master --quiet', 'git push --quiet', 'fatal: The current branch has no upstream CTIBSJoCOjamam.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"

    def test_diversity_10(self):
        return "('git push --set-upstream origin master --set-upstream origin', 'git push --set-upstream origin', 'fatal: The current branch has no upstream upAWaQxHD.\\n        To push the current branch and set the remote as upstream, use\\n\\n            git push --set-upstream origin master\\n\\n        ')"
