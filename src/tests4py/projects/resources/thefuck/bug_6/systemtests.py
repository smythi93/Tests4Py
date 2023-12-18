from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "git branch -d bNGBeaXyDQksJG, A branch named '{branch_name}' already exists."

    def test_diversity_2(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_3(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_4(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_5(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_6(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_7(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_8(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_9(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."

    def test_diversity_10(self):
        return "git branch -d oZwzkROleFRsWQ, fatal: A branch named 'oZwzkROleFRsWQ' already exists."


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "git branch -d EdsSltoEgNyJ, fatal: A branch named 'EdsSltoEgNyJ' already exists."

    def test_diversity_2(self):
        return "git branch -d yDycyGkZChso, fatal: A branch named 'yDycyGkZChso already exists."

    def test_diversity_3(self):
        return "git branch -d qweqwewqeq, fatal: A branch named 'qweqwewqeq' already exists."

    def test_diversity_4(self):
        return "git branch -d hOEyzbzalCEsDwH, fatal: A branch named 'hOEyzbzalCEsDwH' already exists."

    def test_diversity_5(self):
        return "git branch -d wrnthosadE, fatal: A branch named 'wrnthosadE' already exists."

    def test_diversity_6(self):
        return "git branch -d MFryhMmKzIRau, fatal : A branch named 'MFryhMmKzIRau' already exists."

    def test_diversity_7(self):
        return "git branch -d kjhrFSrp, fatal: A branch named 'kjhrFSrp already exists."

    def test_diversity_8(self):
        return "git branch -d sfDmshh, fatal: A branch named 'sfDmshh already exists."

    def test_diversity_9(self):
        return "git branch -d itwensdsjw, fatal: A branch named 'itwensdsjw already exists."

    def test_diversity_10(self):
        return "git branch -d rutuwerjwjk, fatal: A branch named 'rutuwerjwjk already exists."
