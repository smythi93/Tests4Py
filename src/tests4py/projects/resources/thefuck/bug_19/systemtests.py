from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'git PUSH vOwqwMyiW' '' ''

    def test_diversity_2(self):
        return 'git push cbwPQZvhhwSFFsw' '' 'Everything up-to-date'

    def test_diversity_3(self):
        return 'git push IvpvCUiXZKQhH' '' '\n        Counting objects: 3, done.\n        Delta compression using up to 4 threads.\n        Compressing objects: 100% (2/2), done.\n        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.\n        Total 3 (delta 0), reused 0 (delta 0)\n        To /tmp/bar\n           514eed3..f269c79  master -> master\n        '

    def test_diversity_4(self):
        return 'git PUSH BFEavrpqsmcl' '' ''

    def test_diversity_5(self):
        return 'git PUSH CMOwD' '' ''

    def test_diversity_6(self):
        return 'git PUSH MnEvV' '' ''

    def test_diversity_7(self):
        return 'git PUSH ZowwjYunS' '' ''

    def test_diversity_8(self):
        return 'git PUSH oovGPY' '' ''

    def test_diversity_9(self):
        return 'git push DebXFRvrFv' '' '\n        Counting objects: 3, done.\n        Delta compression using up to 4 threads.\n        Compressing objects: 100% (2/2), done.\n        Writing objects: 100% (3/3), 282 bytes | 0 bytes/s, done.\n        Total 3 (delta 0), reused 0 (delta 0)\n        To /tmp/bar\n           514eed3..f269c79  master -> master\n        '

    def test_diversity_10(self):
        return 'git push kvxHSVMjrykci' '' 'Everything up-to-date'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'git push EezrxvNuepI' '' ''

    def test_diversity_2(self):
        return 'git push HHFwNt' '' ''

    def test_diversity_3(self):
        return 'git push UzqABdwMMJnawyX' '' "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        "

    def test_diversity_4(self):
        return 'git push GZbyCKxqnWfX' '' "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        "

    def test_diversity_5(self):
        return 'git push KqvUVnABIF' '' ''

    def test_diversity_6(self):
        return 'git push efAvWcnaRu' '' ''

    def test_diversity_7(self):
        return 'git push gRqyvdK' '' "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        "

    def test_diversity_8(self):
        return 'git push bHTWCyyw' '' ''

    def test_diversity_9(self):
        return 'git push HlXwEsNPChCkS' '' ''

    def test_diversity_10(self):
        return 'git push gnkVoPvw' '' "\n        To /tmp/foo\n         ! [rejected]        master -> master (non-fast-forward)\n         error: failed to push some refs to '/tmp/bar'\n         hint: Updates were rejected because the tip of your current branch is behind\n         hint: its remote counterpart. Integrate the remote changes (e.g.\n         hint: 'git pull ...') before pushing again.\n         hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n        "
