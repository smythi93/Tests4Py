import unittest
import math
import warnings
import matplotlib
matplotlib.use('Agg')
import matplotlib.colors as mcolors

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.533, 0.99, vmin=-23.346, vmax=22.381, base=2)
            self.assertAlmostEqual(0.9596856052316345, float(norm(16.114)), places=4)

    def test_diversity_2(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.919, 1.451, vmin=-20.317, vmax=18.841, base=2)
            self.assertAlmostEqual(0.0628695763959525, float(norm(-11.782)), places=4)

    def test_diversity_3(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.053, 0.667, vmin=-16.378, vmax=12.318, base=math.e)
            self.assertAlmostEqual(0.1818740339158352, float(norm(-5.521)), places=4)

    def test_diversity_4(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.391, 1.456, vmin=-19.145, vmax=19.607, base=10)
            self.assertAlmostEqual(0.9306623848012232, float(norm(8.751)), places=4)

    def test_diversity_5(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(0.911, 1.611, vmin=-23.573, vmax=27.57, base=math.e)
            self.assertAlmostEqual(0.05253158308510788, float(norm(-12.709)), places=4)

    def test_diversity_6(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.104, 1.161, vmin=-17.645, vmax=17.862, base=10)
            self.assertAlmostEqual(0.8249622677772415, float(norm(2.388)), places=4)

    def test_diversity_7(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.711, 1.952, vmin=-7.325, vmax=26.313, base=10)
            self.assertAlmostEqual(0.8804251548794019, float(norm(4.831)), places=4)

    def test_diversity_8(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.781, 1.309, vmin=-14.232, vmax=20.917, base=10)
            self.assertAlmostEqual(0.01244683127247168, float(norm(-12.512)), places=4)

    def test_diversity_9(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.566, 0.638, vmin=-12.75, vmax=16.262, base=math.e)
            self.assertAlmostEqual(0.06461263944330184, float(norm(-8.955)), places=4)

    def test_diversity_10(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(0.933, 1.565, vmin=-11.379, vmax=9.464, base=2)
            self.assertAlmostEqual(0.039243204907193296, float(norm(-7.944)), places=4)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.965, 0.944, vmin=-23.302, vmax=26.166)
            self.assertAlmostEqual(0.08257554786014737, float(norm(-11.988)), places=4)

    def test_diversity_2(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.773, 1.647, vmin=-5.439, vmax=5.279)
            self.assertAlmostEqual(0.13667582160201502, float(norm(-1.972)), places=4)

    def test_diversity_3(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(0.614, 1.033, vmin=-29.078, vmax=17.737)
            self.assertAlmostEqual(0.01737999573379746, float(norm(-24.232)), places=4)

    def test_diversity_4(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.382, 1.721, vmin=-21.999, vmax=28.78)
            self.assertAlmostEqual(0.8876981009421513, float(norm(8.137)), places=4)

    def test_diversity_5(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.853, 0.863, vmin=-28.101, vmax=28.301)
            self.assertAlmostEqual(0.9492580862141553, float(norm(19.528)), places=4)

    def test_diversity_6(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.16, 1.19, vmin=-22.011, vmax=28.257)
            self.assertAlmostEqual(0.8797891461183269, float(norm(9.98)), places=4)

    def test_diversity_7(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.321, 0.746, vmin=-9.568, vmax=27.79)
            self.assertAlmostEqual(0.7952253768636797, float(norm(7.713)), places=4)

    def test_diversity_8(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.009, 1.256, vmin=-21.497, vmax=7.029)
            self.assertAlmostEqual(0.05936274996275755, float(norm(-13.694)), places=4)

    def test_diversity_9(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(1.346, 1.508, vmin=-13.636, vmax=23.84)
            self.assertAlmostEqual(0.8767311904599981, float(norm(6.983)), places=4)

    def test_diversity_10(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            norm = mcolors.SymLogNorm(2.093, 1.812, vmin=-9.696, vmax=5.792)
            self.assertAlmostEqual(0.8941522604529958, float(norm(2.41)), places=4)
