from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'pip ~deBUG lYftCgUXzHhyGk' 'ERROR: unknown command "~deBUG", maybe you meant "debug"'

    def test_diversity_2(self):
        return 'pip sh0w-> sRcAay' 'ERROR: unknown command "sh0w->", maybe you meant "show"'

    def test_diversity_3(self):
        return 'pip inst@ll aBpAtfalr' 'ERROR: unknown command "inst@ll", maybe you meant "install"'

    def test_diversity_4(self):
        return 'pip c0nf1g- aQQStPvjHcl' 'ERROR: unknown command "c0nf1g-", maybe you meant "config"'

    def test_diversity_5(self):
        return 'pip *cAch3 oUcczahTRFTvN' 'ERROR: unknown command "*cAch3", maybe you meant "cache"'

    def test_diversity_6(self):
        return 'pip h4sh cUUyIw' 'ERROR: unknown command "h4sh", maybe you meant "hash"'

    def test_diversity_7(self):
        return 'pip inst@ll aBpAtfalr' 'ERROR: unknown command "inst@ll", maybe you meant "install"'

    def test_diversity_8(self):
        return 'pip che3kk= GzOOXqlDkQ' 'ERROR: unknown command "che3kk=", maybe you meant "check"'

    def test_diversity_9(self):
        return 'pip iNSPcT cZEFWZshFWW' 'ERROR: unknown command "iNSPcT", maybe you meant "inspect"'

    def test_diversity_10(self):
        return 'pip 1nsp3ct iUKKIEfqyxGEWi' 'ERROR: unknown command "1nsp3ct", maybe you meant "inspect"'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'pip serch YDyWaqGaKlDRQ' 'ERROR: unknown command "serch", maybe you meant "search"'

    def test_diversity_2(self):
        return 'pip unstal FgDHygsj' 'ERROR: unknown command "unstal", maybe you meant "uninstall"'

    def test_diversity_3(self):
        return 'pip whell MSVFpUiwVMOXn' 'ERROR: unknown command "whell", maybe you meant "wheel"'

    def test_diversity_4(self):
        return 'pip frezee LAOTFRlCtGr' 'ERROR: unknown command "frezee", maybe you meant "freeze"'

    def test_diversity_5(self):
        return 'pip dbug sCKnEZfsSi' 'ERROR: unknown command "dbug", maybe you meant "debug"'

    def test_diversity_6(self):
        return 'pip unstal mQjfjezy' 'ERROR: unknown command "unstal", maybe you meant "uninstall"'

    def test_diversity_7(self):
        return 'pip lst ImFvYBHWmDpv' 'ERROR: unknown command "lst", maybe you meant "list"'

    def test_diversity_8(self):
        return 'pip downld TzDtmgpXW' 'ERROR: unknown command "downld", maybe you meant "download"'

    def test_diversity_9(self):
        return 'pip chck kDxAspwhQXJSxWZ' 'ERROR: unknown command "chck", maybe you meant "check"'

    def test_diversity_10(self):
        return 'pip lst sjxUAkrDScqXcwD' 'ERROR: unknown command "lst", maybe you meant "list"'
