from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '([\'git branch -d MHFbowC, git branch MHFbowC\'], \'git branch -d MHFbowC\', "fatal: A branch named \'MHFbowC\' already exists.")'

    def test_diversity_2(self):
        return '([\'git branch -d nHUIjNlORcWcf, git checkout -b nHUIjNlORcWcf\'], \'git branch -d nHUIjNlORcWcf\', "fatal: A branch named \'nHUIjNlORcWcf\' already exists.")'

    def test_diversity_3(self):
        return '(False, \'git branch -D zaBRfoQ SELECT * FROM database\', "fatal: A branch named \'zaBRfoQ\' already exists.")'

    def test_diversity_4(self):
        return '(False, \'git branch -D GGpzgeLneM SELECT * FROM database\', "fatal: A branch named \'GGpzgeLneM\' already exists.")'

    def test_diversity_5(self):
        return '([\'git branch -d dtpfiuDpmuSQMw, git branch dtpfiuDpmuSQMw\'], \'git branch -d dtpfiuDpmuSQMw\', "fatal: A branch named \'dtpfiuDpmuSQMw\' already exists.")'

    def test_diversity_6(self):
        return '([\'git branch -d GKaiFXiaTz, git branch GKaiFXiaTz\'], \'git branch -d GKaiFXiaTz\', "fatal: A branch named \'GKaiFXiaTz\' already exists.")'

    def test_diversity_7(self):
        return '(False, \'git branch -D xKybxZmJCiUFMdX SELECT * FROM database\', "fatal: A branch named \'xKybxZmJCiUFMdX\' already exists.")'

    def test_diversity_8(self):
        return '(False, \'git branch -d JJInRUqSRrlmAdf SELECT * FROM database\', "fatal: A branch named \'JJInRUqSRrlmAdf\' already exists.")'

    def test_diversity_9(self):
        return '([\'git branch -d GzzBvaNGU, git checkout -b GzzBvaNGU\'], \'git branch -d GzzBvaNGU\', "fatal: A branch named \'GzzBvaNGU\' already exists.")'

    def test_diversity_10(self):
        return '([\'git branch -d qzHnJbLNnTQs, git branch qzHnJbLNnTQs\'], \'git branch -d qzHnJbLNnTQs\', "fatal: A branch named \'qzHnJbLNnTQs\' already exists.")'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '(True, \'git branch -d zswXefEKEXF\', "fatal: A branch named \'zswXefEKEXF already exists.")'

    def test_diversity_2(self):
        return '(\'git branch -d fpYcGHTHewC && git checkout -b fpYcGHTHewC\', \'git branch -d fpYcGHTHewC\', "fatal: A branch named \'fpYcGHTHewC\' already exists.")'

    def test_diversity_3(self):
        return '(True, \'git branch -d TiawiXin\', "fatal: A branch named \'TiawiXin already exists.")'

    def test_diversity_4(self):
        return '(True, \'git branch -D rpxAebIXPLSsfSJ\', "fatal: A branch named \'rpxAebIXPLSsfSJ already exists.")'

    def test_diversity_5(self):
        return '(True, \'git branch -d sluGaaC\', "fatal: A branch named \'sluGaaC already exists.")'

    def test_diversity_6(self):
        return '(\'git branch -d bUigIg && git checkout -b bUigIg\', \'git branch -d bUigIg\', "fatal: A branch named \'bUigIg\' already exists.")'

    def test_diversity_7(self):
        return '(\'git branch -d pGljI && git branch pGljI\', \'git branch -d pGljI\', "fatal: A branch named \'pGljI\' already exists.")'

    def test_diversity_8(self):
        return '(\'git branch -d QcQZMIhc && git checkout -b QcQZMIhc\', \'git branch -d QcQZMIhc\', "fatal: A branch named \'QcQZMIhc\' already exists.")'

    def test_diversity_9(self):
        return '(True, \'git branch -D kCEbBasXZHZcH\', "fatal: A branch named \'kCEbBasXZHZcH already exists.")'

    def test_diversity_10(self):
        return '(True, \'git branch -D TYAQtBdjRyApI\', "fatal: A branch named \'TYAQtBdjRyApI already exists.")'
