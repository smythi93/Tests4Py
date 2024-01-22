from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):

    def test_diversity_1(self):
        return "git branch -d AvOoFSURIc" "fatal: A branch named 'AvOoFSURIc' already exists."

    def test_diversity_2(self):
        return "git branch -d WwhHuXYXW" "fatal: A branch named 'WwhHuXYXW' already exists."

    def test_diversity_3(self):
        return "git branch -d xHSwKJuEU" "fatal: A branch named 'xHSwKJuEU' already exists."

    def test_diversity_4(self):
        return "git branch -D xejabUW SELECT * FROM database" "fatal: A branch named 'xejabUW' already exists."

    def test_diversity_5(self):
        return "git branch -D jXcygtPNCY SELECT * FROM database" "fatal: A branch named 'jXcygtPNCY' already exists."

    def test_diversity_6(self):
        return "git branch -D caoHYXXOvjaaM SELECT * FROM database" "fatal: A branch named 'caoHYXXOvjaaM' already exists."

    def test_diversity_7(self):
        return "git branch -d CriwRPeTur SELECT * FROM database" "fatal: A branch named 'CriwRPeTur' already exists."

    def test_diversity_8(self):
        return "git branch -d OhoOOyslxqtDkUS SELECT * FROM database" "fatal: A branch named 'OhoOOyslxqtDkUS' already exists."

    def test_diversity_9(self):
        return "git branch -d QtyjrksTWmS SELECT * FROM database" "fatal: A branch named 'QtyjrksTWmS' already exists."

    def test_diversity_10(self):
        return "git branch -d SGxPSOiyrmMj" "fatal: A branch named 'SGxPSOiyrmMj' already exists."


class TestsPassing(PassingSystemtests):

    def test_diversity_1(self):
        return "git branch -D fROSvgyLIjBaA" "fatal: A branch named 'fROSvgyLIjBaA already exists."

    def test_diversity_2(self):
        return "git branch -D pFDpLPLzyXZxUU" "fatal: A branch named 'pFDpLPLzyXZxUU already exists."

    def test_diversity_3(self):
        return "git branch -D XsVWZYqVCwTX" "fatal: A branch named 'XsVWZYqVCwTX already exists."

    def test_diversity_4(self):
        return "git branch -d ceVfFppEXkdyq" "fatal: A branch named 'ceVfFppEXkdyq' already exists."

    def test_diversity_5(self):
        return "git branch -d TlaAZnNBgQfb" "fatal: A branch named 'TlaAZnNBgQfb' already exists."

    def test_diversity_6(self):
        return "git branch -d hGWRbXfeEesdep" "fatal: A branch named 'hGWRbXfeEesdep' already exists."

    def test_diversity_7(self):
        return "git branch -d OeradBbrGY" "fatal: A branch named 'OeradBbrGY already exists."

    def test_diversity_8(self):
        return "git branch -d JeUPbfkuRKw" "fatal: A branch named 'JeUPbfkuRKw already exists."

    def test_diversity_9(self):
        return "git branch -d WnqoLp" "fatal: A branch named 'WnqoLp already exists."

    def test_diversity_10(self):
        return "git branch -d ZZjqFMHki" "fatal: A branch named 'ZZjqFMHki already exists."
