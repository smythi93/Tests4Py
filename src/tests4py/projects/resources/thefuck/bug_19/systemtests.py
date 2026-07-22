from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('git push --force rSbVYOF', 'git PUSH rSbVYOF', '', '')"

    def test_diversity_2(self):
        return "(True, 'git push GKlUBBh', '', '\\n        Counting objects: 3, done.\\n        Delta compression using up to 4 threads.\\n        Compressing objects: 100% (2/2), done.\\n        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.\\n        Total 3 (delta 0), reused 0 (delta 0)\\n        To /tmp/bar\\n           514eed3..f269c79  master -> master\\n        ')"

    def test_diversity_3(self):
        return "('git push --force VCLjBqYCxb', 'git PUSH VCLjBqYCxb', '', '')"

    def test_diversity_4(self):
        return "('git push --force hrtXePdBp', 'git PUSH hrtXePdBp', '', '')"

    def test_diversity_5(self):
        return "(True, 'git push ROReEHtO', '', '\\n        Counting objects: 3, done.\\n        Delta compression using up to 4 threads.\\n        Compressing objects: 100% (2/2), done.\\n        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.\\n        Total 3 (delta 0), reused 0 (delta 0)\\n        To /tmp/bar\\n           514eed3..f269c79  master -> master\\n        ')"

    def test_diversity_6(self):
        return "('git push --force TIHyrQjHUR', 'git PUSH TIHyrQjHUR', '', '')"

    def test_diversity_7(self):
        return "('git push --force pkirU', 'git PUSH pkirU', '', '')"

    def test_diversity_8(self):
        return "(True, 'git push VOHIskcrMERGh', '', '\\n        Counting objects: 3, done.\\n        Delta compression using up to 4 threads.\\n        Compressing objects: 100% (2/2), done.\\n        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.\\n        Total 3 (delta 0), reused 0 (delta 0)\\n        To /tmp/bar\\n           514eed3..f269c79  master -> master\\n        ')"

    def test_diversity_9(self):
        return "(True, 'git push MoRUtDfvGsugMvv', '', 'Everything up-to-date')"

    def test_diversity_10(self):
        return "(True, 'git push ZzjZzQNO', '', 'Everything up-to-date')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('git push --force vZbtupWjXjOrMyy', 'git push vZbtupWjXjOrMyy', '', '')"

    def test_diversity_2(self):
        return "('git push --force KfPlTW', 'git push KfPlTW', '', '')"

    def test_diversity_3(self):
        return "('git push --force tJgqGUCIACsXMIu', 'git push tJgqGUCIACsXMIu', '', '')"

    def test_diversity_4(self):
        return "('git push --force HkizZDiee', 'git push HkizZDiee', '', '')"

    def test_diversity_5(self):
        return '(True, \'git push HQdppvMCNtLu\', \'\', "\\n        To /tmp/foo\\n         ! [rejected]        master -> master (non-fast-forward)\\n         error: failed to push some refs to \'/tmp/bar\'\\n         hint: Updates were rejected because the tip of your current branch is behind\\n         hint: its remote counterpart. Integrate the remote changes (e.g.\\n         hint: \'git pull ...\') before pushing again.\\n         hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\\n        ")'

    def test_diversity_6(self):
        return '(True, \'git push OpNohnOqOIcfB\', \'\', "\\n        To /tmp/foo\\n         ! [rejected]        master -> master (non-fast-forward)\\n         error: failed to push some refs to \'/tmp/bar\'\\n         hint: Updates were rejected because the tip of your current branch is behind\\n         hint: its remote counterpart. Integrate the remote changes (e.g.\\n         hint: \'git pull ...\') before pushing again.\\n         hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\\n        ")'

    def test_diversity_7(self):
        return "('git push --force WSbLlttE', 'git push WSbLlttE', '', '')"

    def test_diversity_8(self):
        return '(True, \'git push XrHSSjFakxF\', \'\', "\\n        To /tmp/foo\\n         ! [rejected]        master -> master (non-fast-forward)\\n         error: failed to push some refs to \'/tmp/bar\'\\n         hint: Updates were rejected because the tip of your current branch is behind\\n         hint: its remote counterpart. Integrate the remote changes (e.g.\\n         hint: \'git pull ...\') before pushing again.\\n         hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\\n        ")'

    def test_diversity_9(self):
        return '(True, \'git push IPjFU\', \'\', "\\n        To /tmp/foo\\n         ! [rejected]        master -> master (non-fast-forward)\\n         error: failed to push some refs to \'/tmp/bar\'\\n         hint: Updates were rejected because the tip of your current branch is behind\\n         hint: its remote counterpart. Integrate the remote changes (e.g.\\n         hint: \'git pull ...\') before pushing again.\\n         hint: See the \'Note about fast-forwards\' in \'git push --help\' for details.\\n        ")'

    def test_diversity_10(self):
        return "('git push --force hprVzaLEMhKR', 'git push hprVzaLEMhKR', '', '')"
