from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'XAoKCgoKdG90dnZnYiA9IFs1MCwgMzAsIDgxXQo= dG90dnZnYiA9IFs1MCwgMzAsIDgxXQo='

    def test_diversity_2(self):
        return 'XAoKCgpwcmludCgidHVteWUiKQo= cHJpbnQoInR1bXllIikK'

    def test_diversity_3(self):
        return 'XAoKCgpxZXd0ZiA9IFs0MywgNTNdCg== cWV3dGYgPSBbNDMsIDUzXQo='

    def test_diversity_4(self):
        return 'XAoKCgoKCgpwcmludCgiemlva3N5IikK cHJpbnQoInppb2tzeSIpCg=='

    def test_diversity_5(self):
        return 'XAoKCnByaW50KCJod2giKQo= cHJpbnQoImh3aCIpCg=='

    def test_diversity_6(self):
        return 'XAoKCgoKcmNtY2wgPSBbOTAsIDQsIDkxLCAxN10K cmNtY2wgPSBbOTAsIDQsIDkxLCAxN10K'

    def test_diversity_7(self):
        return 'XAoKCnF2YyA9IHsiaGhnZXFnIjogNjd9Cg== cXZjID0geyJoaGdlcWciOiA2N30K'

    def test_diversity_8(self):
        return 'XAoKCgoKCgpwcmludCgiamp5dHMiKQo= cHJpbnQoImpqeXRzIikK'

    def test_diversity_9(self):
        return 'XAoKCgoKCnlhbyA9IDY2Nwo= eWFvID0gNjY3Cg=='

    def test_diversity_10(self):
        return 'XAoKCgoKCgp0bHljYmUgPSBbMjUsIDM1LCA5Nl0K dGx5Y2JlID0gWzI1LCAzNSwgOTZdCg=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'CgoKZGVmIG9jbSgpOgogICAgcmV0dXJuIDQ4Cg== ZGVmIG9jbSgpOgogICAgcmV0dXJuIDQ4Cg=='

    def test_diversity_2(self):
        return 'bGpodSA9IDU2NAo= bGpodSA9IDU2NAo='

    def test_diversity_3(self):
        return 'ZGVmIG13aWdxdCgpOgogICAgcmV0dXJuIDcyMwo= ZGVmIG13aWdxdCgpOgogICAgcmV0dXJuIDcyMwo='

    def test_diversity_4(self):
        return 'CgoKCnByaW50KCJtdnd2eXgiKQo= cHJpbnQoIm12d3Z5eCIpCg=='

    def test_diversity_5(self):
        return 'CgoKCm1ldHZ4ZXZwID0gWzgzLCA5MSwgNzddCg== bWV0dnhldnAgPSBbODMsIDkxLCA3N10K'

    def test_diversity_6(self):
        return 'CgpkZWYgbHpuZmN5aGgoKToKICAgIHJldHVybiAxNzQK ZGVmIGx6bmZjeWhoKCk6CiAgICByZXR1cm4gMTc0Cg=='

    def test_diversity_7(self):
        return 'ZGVmIHZtaSgpOgogICAgcmV0dXJuIDk2OAo= ZGVmIHZtaSgpOgogICAgcmV0dXJuIDk2OAo='

    def test_diversity_8(self):
        return 'Y25xZXlnaW0gPSA1NjQK Y25xZXlnaW0gPSA1NjQK'

    def test_diversity_9(self):
        return 'CgpkZWYgamVjeHEoKToKICAgIHJldHVybiA5NzkK ZGVmIGplY3hxKCk6CiAgICByZXR1cm4gOTc5Cg=='

    def test_diversity_10(self):
        return 'CgoKYnp4ZiA9IDc4NQo= Ynp4ZiA9IDc4NQo='
