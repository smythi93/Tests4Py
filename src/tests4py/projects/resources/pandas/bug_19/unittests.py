import unittest
import numpy
import pytest
from pandas import Series, DataFrame


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        key = [(1674, 784, 6309)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[1674, 784, 6309], [6, 8, 10]],
                       index=[[1674, 784, 6309], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_2(self):
        key = [(7898, 6681, 8921)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[7898, 6681, 8921], [6, 8, 10]],
                       index=[[7898, 6681, 8921], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_3(self):
        key = [(968, 6995, 683)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[968, 6995, 683], [6, 8, 10]],
                       index=[[968, 6995, 683], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_4(self):
        key = [(7565, 8122, 7369)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[7565, 8122, 7369], [6, 8, 10]],
                       index=[[7565, 8122, 7369], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_5(self):
        key = [(101, 5942, 9812)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[101, 5942, 9812], [6, 8, 10]],
                       index=[[101, 5942, 9812], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_6(self):
        key = [(5150, 5368, 4478)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[5150, 5368, 4478], [6, 8, 10]],
                       index=[[5150, 5368, 4478], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_7(self):
        key = [(9691, 3131, 8799)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[9691, 3131, 8799], [6, 8, 10]],
                       index=[[9691, 3131, 8799], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_8(self):
        key = [(7464, 2693, 500)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[7464, 2693, 500], [6, 8, 10]],
                       index=[[7464, 2693, 500], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_9(self):
        key = [(5795, 256, 8458)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[5795, 256, 8458], [6, 8, 10]],
                       index=[[5795, 256, 8458], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]

    def test_diversity_10(self):
        key = [(6345, 9486, 2177)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[6345, 9486, 2177], [6, 8, 10]],
                       index=[[6345, 9486, 2177], [8, 10, 12]])
        with pytest.raises(KeyError, match='not in index'):
            df.loc[key]


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        key = [(8123, 2082, 4805)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[8123, 2082, 4805], [6, 8, 10]],
                       index=[[8123, 2082, 4805], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_2(self):
        key = [(2597, 978, 9022)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[2597, 978, 9022], [6, 8, 10]],
                       index=[[2597, 978, 9022], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_3(self):
        key = [(525, 4436, 6927)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[525, 4436, 6927], [6, 8, 10]],
                       index=[[525, 4436, 6927], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_4(self):
        key = [(104, 7261, 2717)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[104, 7261, 2717], [6, 8, 10]],
                       index=[[104, 7261, 2717], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_5(self):
        key = [(756, 9875, 285)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[756, 9875, 285], [6, 8, 10]],
                       index=[[756, 9875, 285], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_6(self):
        key = [(7663, 9021, 565)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[7663, 9021, 565], [6, 8, 10]],
                       index=[[7663, 9021, 565], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_7(self):
        key = [(4336, 3782, 3836)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[4336, 3782, 3836], [6, 8, 10]],
                       index=[[4336, 3782, 3836], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_8(self):
        key = [(9331, 4707, 1654)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[9331, 4707, 1654], [6, 8, 10]],
                       index=[[9331, 4707, 1654], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_9(self):
        key = [(9807, 3790, 2411)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[9807, 3790, 2411], [6, 8, 10]],
                       index=[[9807, 3790, 2411], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]

    def test_diversity_10(self):
        key = [(671, 4958, 5379)]
        df = DataFrame(numpy.random.randn(3, 3), columns=[[671, 4958, 5379], [6, 8, 10]],
                       index=[[671, 4958, 5379], [8, 10, 12]])
        with pytest.raises(KeyError, match='None of \\[.*\\] are in the \\[index\\]'):
            df.loc[key]
