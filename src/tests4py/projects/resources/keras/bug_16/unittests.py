import unittest
import numpy as np
import keras
from keras.models import Sequential


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 8262)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_2(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 4854)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_3(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 303)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_4(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 4944)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_5(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 5331)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_6(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 8361)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_7(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 9360)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_8(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 3803)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_9(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 7331)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_10(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 8179)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert 'name' in config
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 5666)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_2(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 5645)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_3(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 6616)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_4(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 6741)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_5(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 4986)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_6(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 8980)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_7(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 7997)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_8(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 9686)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_9(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 9098)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4

    def test_diversity_10(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(3))
        model.add(keras.layers.Dense(3))
        model.compile('sgd', 'mse')
        assert model.built is False
        assert len(model.layers) == 2
        assert len(model.weights) == 0
        model.train_on_batch(np.random.random((2, 3522)), np.random.random((2, 3)))
        assert model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
        config = model.get_config()
        assert all(('name' in layer['config'] for layer in config if isinstance(layer, dict)))
        new_model = Sequential.from_config(config)
        assert new_model.built is True
        assert len(model.layers) == 2
        assert len(model.weights) == 4
