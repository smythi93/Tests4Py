import unittest
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.colors as mcolors
def run_make_mapping_array(n, data, gamma):
    lut = mcolors.makeMappingArray(n, data, gamma)
    return [round(float(v), 6) for v in np.atleast_1d(np.asarray(lut))]



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([0.763], run_make_mapping_array(1, [(0.0, 0.64, 0.555), (0.178, 0.579, 0.171), (0.387, 0.329, 0.958), (1.0, 0.763, 0.0)], 1.0))

    def test_diversity_2(self):
        self.assertEqual([0.692], run_make_mapping_array(1, [(0.0, 0.707, 0.216), (0.225, 0.762, 0.655), (0.341, 0.636, 0.692), (1.0, 0.692, 0.366)], 1.0))

    def test_diversity_3(self):
        self.assertEqual([0.408], run_make_mapping_array(1, [(0.0, 0.548, 0.717), (0.276, 0.78, 0.881), (1.0, 0.408, 0.127)], 1.0))

    def test_diversity_4(self):
        self.assertEqual([0.788], run_make_mapping_array(1, [(0.0, 0.546, 0.211), (1.0, 0.788, 0.946)], 1.0))

    def test_diversity_5(self):
        self.assertEqual([0.483], run_make_mapping_array(1, [(0.0, 0.638, 0.466), (0.503, 0.772, 0.925), (1.0, 0.483, 0.743)], 1.0))

    def test_diversity_6(self):
        self.assertEqual([0.74], run_make_mapping_array(1, [(0.0, 0.097, 0.869), (1.0, 0.74, 0.431)], 1.0))

    def test_diversity_7(self):
        self.assertEqual([0.268], run_make_mapping_array(1, [(0.0, 0.317, 0.442), (0.386, 0.469, 0.502), (0.457, 0.15, 0.597), (1.0, 0.268, 0.105)], 1.0))

    def test_diversity_8(self):
        self.assertEqual([0.894], run_make_mapping_array(1, [(0.0, 0.235, 0.66), (0.281, 0.046, 0.622), (0.503, 0.034, 0.007), (1.0, 0.894, 0.581)], 1.0))

    def test_diversity_9(self):
        self.assertEqual([0.729], run_make_mapping_array(1, [(0.0, 0.557, 0.235), (1.0, 0.729, 0.585)], 1.0))

    def test_diversity_10(self):
        self.assertEqual([0.675], run_make_mapping_array(1, [(0.0, 0.949, 0.89), (0.449, 0.98, 0.85), (0.506, 0.986, 0.697), (1.0, 0.675, 0.912)], 1.0))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([0.414, 0.484952, 0.555904, 0.626855, 0.697807, 0.173], run_make_mapping_array(6, [(0.0, 0.195, 0.414), (0.809, 0.701, 0.959), (1.0, 0.173, 0.9)], 1.0))

    def test_diversity_2(self):
        self.assertEqual([0.007, 0.238343, 0.422331, 0.803619, 0.554413, 0.305206, 0.056], run_make_mapping_array(7, [(0.0, 0.608, 0.007), (0.201, 0.286, 0.77), (0.37, 0.326, 0.998), (1.0, 0.056, 0.113)], 1.0))

    def test_diversity_3(self):
        self.assertEqual([0.438, 0.195706, 0.66185, 0.7459, 0.82995, 0.914], run_make_mapping_array(6, [(0.0, 0.773, 0.438), (0.279, 0.1, 0.611), (1.0, 0.914, 0.488)], 1.0))

    def test_diversity_4(self):
        self.assertEqual([0.017, 0.05, 0.083, 0.116, 0.149, 0.182], run_make_mapping_array(6, [(0.0, 0.575, 0.017), (1.0, 0.182, 0.648)], 1.0))

    def test_diversity_5(self):
        self.assertEqual([0.305, 0.371794, 0.438588, 0.505382, 0.572176, 0.584268, 0.8], run_make_mapping_array(7, [(0.0, 0.083, 0.305), (0.786, 0.62, 0.523), (1.0, 0.8, 0.743)], 1.0))

    def test_diversity_6(self):
        self.assertEqual([0.668, 0.7195, 0.771], run_make_mapping_array(3, [(0.0, 0.284, 0.668), (1.0, 0.771, 0.952)], 1.0))

    def test_diversity_7(self):
        self.assertEqual([0.817, 0.770571, 0.724143, 0.677714, 0.631286, 0.584857, 0.538429, 0.492], run_make_mapping_array(8, [(0.0, 0.541, 0.817), (1.0, 0.492, 0.334)], 1.0))

    def test_diversity_8(self):
        self.assertEqual([0.625, 0.570129, 0.515259, 0.460388, 0.405517, 0.480452, 0.712726, 0.945], run_make_mapping_array(8, [(0.0, 0.633, 0.625), (0.591, 0.398, 0.28), (1.0, 0.945, 0.713)], 1.0))

    def test_diversity_9(self):
        self.assertEqual([0.322, 0.277167, 0.232333, 0.1875, 0.142667, 0.097833, 0.053], run_make_mapping_array(7, [(0.0, 0.802, 0.322), (1.0, 0.053, 0.777)], 1.0))

    def test_diversity_10(self):
        self.assertEqual([0.007, 0.568], run_make_mapping_array(2, [(0.0, 0.904, 0.007), (0.314, 0.573, 0.463), (1.0, 0.568, 0.902)], 1.0))
