from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'git branch -d muTjdAtQMCIwR SELECT * FROM database' '' "fatal: A branch named 'muTjdAtQMCIwR' already exists."

    def test_diversity_2(self):
        return 'git branch -d JIkpdi' '' "fatal: A branch named 'JIkpdi' already exists."

    def test_diversity_3(self):
        return 'git branch -d aebZiAxSX' '' "fatal: A branch named 'aebZiAxSX' already exists."

    def test_diversity_4(self):
        return 'git branch -d BlLtbeP' '' "fatal: A branch named 'BlLtbeP' already exists."

    def test_diversity_5(self):
        return 'git branch -D YHHQqQbiP SELECT * FROM database' '' "fatal: A branch named 'YHHQqQbiP' already exists."

    def test_diversity_6(self):
        return 'git branch -d LnsFRLMbtZMytXX' '' "fatal: A branch named 'LnsFRLMbtZMytXX' already exists."

    def test_diversity_7(self):
        return 'git branch -d dpJBugeHfz' '' "fatal: A branch named 'dpJBugeHfz' already exists."

    def test_diversity_8(self):
        return 'git branch -d bOXCGjusBMJMjUe SELECT * FROM database' '' "fatal: A branch named 'bOXCGjusBMJMjUe' already exists."

    def test_diversity_9(self):
        return 'git branch -d nyCmZEqimFlLBBQ' '' "fatal: A branch named 'nyCmZEqimFlLBBQ' already exists."

    def test_diversity_10(self):
        return 'git branch -d hSOwZQHjXGE' '' "fatal: A branch named 'hSOwZQHjXGE' already exists."


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'git branch -d ATSooVUN' '' "fatal: A branch named 'ATSooVUN already exists."

    def test_diversity_2(self):
        return 'git branch -D RcUHolyBDc' '' "fatal: A branch named 'RcUHolyBDc already exists."

    def test_diversity_3(self):
        return 'git branch -d CibAmH' '' "fatal: A branch named 'CibAmH' already exists."

    def test_diversity_4(self):
        return 'git branch -D NHtHg' '' "fatal: A branch named 'NHtHg already exists."

    def test_diversity_5(self):
        return 'git branch -d AUeVSHeKVtOKqGd' '' "fatal: A branch named 'AUeVSHeKVtOKqGd' already exists."

    def test_diversity_6(self):
        return 'git branch -D pHZUDkKsqIvO' '' "fatal: A branch named 'pHZUDkKsqIvO already exists."

    def test_diversity_7(self):
        return 'git branch -d QHZtvDPXt' '' "fatal: A branch named 'QHZtvDPXt' already exists."

    def test_diversity_8(self):
        return 'git branch -d GmLgqwfIEoSwGZV' '' "fatal: A branch named 'GmLgqwfIEoSwGZV' already exists."

    def test_diversity_9(self):
        return 'git branch -d NyUGujFPR' '' "fatal: A branch named 'NyUGujFPR already exists."

    def test_diversity_10(self):
        return 'git branch -D iHjAmAwxFKPFV' '' "fatal: A branch named 'iHjAmAwxFKPFV already exists."
