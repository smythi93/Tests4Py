import unittest
import numpy as np
from keras.engine import training_utils


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([630, 796, 25, 85, 865])
        class_weights = {0: 630, 1: 796, 2: 25}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([630, 796, 25, 85, 865]))

    def test_diversity_2(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([499, 840, 992, 755, 652])
        class_weights = {0: 499, 1: 840, 2: 992}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([499, 840, 992, 755, 652]))

    def test_diversity_3(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([319, 366, 573, 477, 966])
        class_weights = {0: 319, 1: 366, 2: 573}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([319, 366, 573, 477, 966]))

    def test_diversity_4(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([418, 437, 392, 887, 607])
        class_weights = {0: 418, 1: 437, 2: 392}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([418, 437, 392, 887, 607]))

    def test_diversity_5(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([949, 497, 224, 515, 637])
        class_weights = {0: 949, 1: 497, 2: 224}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([949, 497, 224, 515, 637]))

    def test_diversity_6(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([650, 174, 231, 63, 417])
        class_weights = {0: 650, 1: 174, 2: 231}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([650, 174, 231, 63, 417]))

    def test_diversity_7(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([804, 731, 553, 783, 246])
        class_weights = {0: 804, 1: 731, 2: 553}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([804, 731, 553, 783, 246]))

    def test_diversity_8(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([500, 309, 957, 804, 261])
        class_weights = {0: 500, 1: 309, 2: 957}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([500, 309, 957, 804, 261]))

    def test_diversity_9(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([959, 610, 964, 932, 205])
        class_weights = {0: 959, 1: 610, 2: 964}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([959, 610, 964, 932, 205]))

    def test_diversity_10(self):
        y = np.array([0, 1, 0, 0, 2])
        sample_weights = np.array([886, 944, 580, 647, 164])
        class_weights = {0: 886, 1: 944, 2: 580}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([886, 944, 580, 647, 164]))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([869, 659, 742, 529, 934])
        class_weights = {0: 869, 1: 659, 2: 742, 3: 529, 4: 934}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([869, 659, 742, 529, 934]))

    def test_diversity_2(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([580, 956, 373, 78, 948])
        class_weights = {0: 580, 1: 956, 2: 373, 3: 78, 4: 948}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([580, 956, 373, 78, 948]))

    def test_diversity_3(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([54, 397, 637, 487, 509])
        class_weights = {0: 54, 1: 397, 2: 637, 3: 487, 4: 509}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([54, 397, 637, 487, 509]))

    def test_diversity_4(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([178, 104, 203, 229, 718])
        class_weights = {0: 178, 1: 104, 2: 203, 3: 229, 4: 718}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([178, 104, 203, 229, 718]))

    def test_diversity_5(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([33, 654, 728, 80, 300])
        class_weights = {0: 33, 1: 654, 2: 728, 3: 80, 4: 300}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([33, 654, 728, 80, 300]))

    def test_diversity_6(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([538, 883, 441, 883, 865])
        class_weights = {0: 538, 1: 883, 2: 441, 3: 883, 4: 865}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([538, 883, 441, 883, 865]))

    def test_diversity_7(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([388, 471, 44, 584, 940])
        class_weights = {0: 388, 1: 471, 2: 44, 3: 584, 4: 940}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([388, 471, 44, 584, 940]))

    def test_diversity_8(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([934, 413, 129, 533, 462])
        class_weights = {0: 934, 1: 413, 2: 129, 3: 533, 4: 462}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([934, 413, 129, 533, 462]))

    def test_diversity_9(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([314, 114, 613, 355, 367])
        class_weights = {0: 314, 1: 114, 2: 613, 3: 355, 4: 367}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([314, 114, 613, 355, 367]))

    def test_diversity_10(self):
        y = np.array([[0], [1], [2], [3], [4]])
        sample_weights = np.array([33, 240, 479, 478, 791])
        class_weights = {0: 33, 1: 240, 2: 479, 3: 478, 4: 791}
        weights = training_utils.standardize_weights(y, sample_weights)
        assert np.allclose(weights, sample_weights)
        weights = training_utils.standardize_weights(y, class_weight=class_weights)
        assert np.allclose(weights, np.array([33, 240, 479, 478, 791]))
