import unittest
import numpy
from keras import backend
from keras import initializers


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        initializer = initializers.truncated_normal
        init = initializer(seed=71)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) > 0.0

    def test_diversity_2(self):
        initializer = initializers.truncated_normal
        init = initializer(seed=55)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) < 0.0

    def test_diversity_3(self):
        initializer = initializers.normal
        init = initializer(seed=1829)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) > 0.0

    def test_diversity_4(self):
        initializer = initializers.orthogonal
        init = initializer(seed=752)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) > 0.0

    def test_diversity_5(self):
        initializer = initializers.uniform
        init = initializer(seed=1029)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) > 0.0

    def test_diversity_6(self):
        initializer = initializers.normal
        init = initializer(seed=1979)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) < 0.0

    def test_diversity_7(self):
        initializer = initializers.normal
        init = initializer(seed=31)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) > 0.0

    def test_diversity_8(self):
        initializer = initializers.VarianceScaling
        init = initializer(seed=625)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) < 0.0

    def test_diversity_9(self):
        initializer = initializers.uniform
        init = initializer(seed=778)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) > 0.0

    def test_diversity_10(self):
        initializer = initializers.truncated_normal
        init = initializer(seed=1730)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) < 0.0


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        initializer = initializers.normal
        init = initializer(seed=85)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_2(self):
        initializer = initializers.uniform
        init = initializer(seed=197)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_3(self):
        initializer = initializers.truncated_normal
        init = initializer(seed=1811)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_4(self):
        initializer = initializers.normal
        init = initializer(seed=34)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_5(self):
        initializer = initializers.truncated_normal
        init = initializer(seed=1508)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_6(self):
        initializer = initializers.truncated_normal
        init = initializer(seed=1498)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_7(self):
        initializer = initializers.truncated_normal
        init = initializer(seed=1112)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_8(self):
        initializer = initializers.orthogonal
        init = initializer(seed=229)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_9(self):
        initializer = initializers.orthogonal
        init = initializer(seed=732)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0

    def test_diversity_10(self):
        initializer = initializers.normal
        init = initializer(seed=1092)
        samples = [init((2, 2)) for _ in range(2)]
        samples = [backend.get_value(backend.variable(x)) for x in samples]
        assert numpy.mean(numpy.abs(samples[0] - samples[1])) == 0.0
