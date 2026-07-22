from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('man -s 5 write', 'man -s 4 write', 'Output Message: cdpjV', '')"

    def test_diversity_2(self):
        return "(['read --help', 'man 5 read', 'man 4 read'], 'man read', 'Output Message: NlYcjfoQGrFFkZ', '')"

    def test_diversity_3(self):
        return "('man 4 write', 'man 5 write', 'Output Message: OYTFMFOfk', '')"

    def test_diversity_4(self):
        return "('man -s5 write', 'man -s4 write', 'Output Message: jugklUEH', '')"

    def test_diversity_5(self):
        return "('man -s 4 write', 'man -s 5 write', 'Output Message: CnRaZqtblzm', '')"

    def test_diversity_6(self):
        return "('man -s5 read', 'man -s4 read', 'Output Message: ISTIZWrHcEA', '')"

    def test_diversity_7(self):
        return "('man 5 read', 'man 4 read', 'Output Message: saLPvTDy', '')"

    def test_diversity_8(self):
        return "('man -s 4 read', 'man -s 5 read', 'Output Message: LhshoyHtmWJgB', '')"

    def test_diversity_9(self):
        return "('man -s 4 read', 'man -s 5 read', 'Output Message: VhbhhisXvAPES', '')"

    def test_diversity_10(self):
        return "('man 4 write', 'man 5 write', 'Output Message: rlkDLNqYBtai', '')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('man 2 read', 'man 3 read', 'Output Message: CrEjN', '')"

    def test_diversity_2(self):
        return "('man 2 write', 'man 3 write', 'Output Message: dQakFIngmK', '')"

    def test_diversity_3(self):
        return "('man -s 3 write', 'man -s 2 write', 'Output Message: yEDvkBFCy', '')"

    def test_diversity_4(self):
        return "('man 3 write', 'man 2 write', 'Output Message: FsPJnhriWFf', '')"

    def test_diversity_5(self):
        return "(['missing --help', 'man 3 missing', 'man 2 missing'], 'man missing', 'Output Message: WaybRDVIvS', 'No manual entry for missing\\n')"

    def test_diversity_6(self):
        return "('man -s2 write', 'man -s3 write', 'Output Message: wnLcIF', '')"

    def test_diversity_7(self):
        return "('man 2 write', 'man 3 write', 'Output Message: IuQBGiUN', '')"

    def test_diversity_8(self):
        return "('man -s 3 read', 'man -s 2 read', 'Output Message: MfEPg', '')"

    def test_diversity_9(self):
        return "('man -s 2 read', 'man -s 3 read', 'Output Message: VwWmenfhRa', '')"

    def test_diversity_10(self):
        return "('man 3 read', 'man 2 read', 'Output Message: FTtbwjdZjee', '')"
