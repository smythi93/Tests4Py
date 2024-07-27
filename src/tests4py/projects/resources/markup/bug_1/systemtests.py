from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '"aZhhGAuRzG"'

    def test_diversity_2(self):
        return '<a>"WTDYcMlJGGouhwwmnwMsJF"</a>'

    def test_diversity_3(self):
        return '"LPuRcKppHdFrwESGrftbpIBgvYau"'

    def test_diversity_4(self):
        return '"<a>PFjpbYODHaAKtuMyDrTXHHO</a>"'

    def test_diversity_5(self):
        return '"XadJLoyKcWHBHXP"cSHQJyHstIeUMG'

    def test_diversity_6(self):
        return '""cecpQLBVBzDVeycWLgrjTJhqa'

    def test_diversity_7(self):
        return 'jQJnQXVcgjVvxBGjHYjXNReFFxm""'

    def test_diversity_8(self):
        return '"<a>b</a>"MtAbGRtdFGKaSZDoUsZHNMeawY""'

    def test_diversity_9(self):
        return '"neHVLaS"zKNsPOs"KpWZYGIxiSfzNSF"'

    def test_diversity_10(self):
        return '<a "abc">"jFqhKwgAmJHfAcuhhxAalvH"</a>'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "<nzyqrwruu>pLofSlUalENPkKjNNCuwygRjpolAjX</nzyqrwruu>"

    def test_diversity_2(self):
        return "<yaugptaoptra>SjDEfXXISbnuImPoQOXqRuNcsJUuv</yaugptaoptra>"

    def test_diversity_3(self):
        return "<cnyvnnvyc>HhFcSaoAjJLuVduSIEJsKLIoKGpU</cnyvnnvyc>"

    def test_diversity_4(self):
        return "<suprqo>ASwEXrsUrbdMpEmidMmJZcKXW</suprqo>"

    def test_diversity_5(self):
        return '<zmcytjrhdd "abc">IbXMFocpXLguFvGtxEqZxmH</zmcytjrhdd>'

    def test_diversity_6(self):
        return "<pnufclccpw>kojZEXvCqkEZHkfRAZxS</pnufclccpw>"

    def test_diversity_7(self):
        return "<ovaviavnqmszox>oBALzZmQwwxC</ovaviavnqmszox>"

    def test_diversity_8(self):
        return "<guersbc>tlljngrRWQEIaFtOoSEqWN</guersbc>"

    def test_diversity_9(self):
        return "<pjsacwd>PCwGKCDUlkfiFemQrKrOpIS</pjsacwd>"

    def test_diversity_10(self):
        return "<rdzjvcynbarr>tepXUOlYjcbVfJJNUGap</rdzjvcynbarr>"
