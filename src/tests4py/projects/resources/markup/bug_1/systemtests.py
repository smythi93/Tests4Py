from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '"""aZhhGAuRzG"""'

    def test_diversity_2(self):
        return '"""WTDYcMlJGGouhwwmnwMsJF"""'

    def test_diversity_3(self):
        return '"""LPuRcKppHdFrwESGrftbpIBgvYau"""'

    def test_diversity_4(self):
        return '"""PFjpbYODHaAKtuMyDrTXHHO"""'

    def test_diversity_5(self):
        return '"""XadJLoyKcWHBHXPcSHQJyHstIeUMG"""'

    def test_diversity_6(self):
        return '"""cecpQLBVBzDVeycWLgrjTJhqa"""'

    def test_diversity_7(self):
        return '"""jQJnQXVcgjVvxBGjHYjXNReFFxm"""'

    def test_diversity_8(self):
        return '"""MtAbGRtdFGKaSZDoUsZHNMeawY"""'

    def test_diversity_9(self):
        return '"""neHVLaSzKNsPOsKpWZYGIxiSfzNSF"""'

    def test_diversity_10(self):
        return '"""jFqhKwgAmJHfAcuhhxAalvH"""'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "<search>kWOREGqWUuGrBCdJLaHk<body>gkKTWpvpuSiBK</body>qvRQILDHOlVSzaacTdt</search>"

    def test_diversity_2(self):
        return "<article>ozzHsciYyHxTJrkblU <span>QmDfwmJIsYpfa </span>DvKcsZBTYsyfabSELIjTkdnIVlgUK</article>"

    def test_diversity_3(self):
        return "<ul>cCFecupGRmCqnqupvfTgeykzRQBK'<output>zJSebCUKNLZQZdTCrUOVqXcHNInlhe'</output>bbbRPqcqbpjsHMH</ul>"

    def test_diversity_4(self):
        return "<output>IVyFsNqvZttQ <div>GGVbYJJEfogTP </div>KYFtKThfvd</output>"

    def test_diversity_5(self):
        return "<h1>KtuUbmCSJItpMTU<h1>"

    def test_diversity_6(self):
        return "<q>nfurYOhhCTPfRaRNoQFS <aside>xxnFckujbghMnk </aside>fcMOafakFoENEEFFpCOomkagmslmbN</q>"

    def test_diversity_7(self):
        return "<article>kZhAfMjuYO<progress>nEVGIFoVLGEaFKruZUjUUu</progress>pOIEVAajgdkUZxVDrboPBrmPO</article>"

    def test_diversity_8(self):
        return "<ul>nfurYOhhCTPfRaRNoQFS'<div>xxnFckujbghMnk'</div>fcMOafakFoENEEFFpCOomkagmslmbN</ul>"

    def test_diversity_9(self):
        return "<i>HuyxEjqHCgr</i>"

    def test_diversity_10(self):
        return "<search>BlGoMtRrlkklqmXGQ <datalist>zNDnzdZnHlQEgkFXgDJnqXN </datalist>AstvewUtlRPCFVAtKGqX</search>"
