import unittest
from keras.models import Sequential
from keras.layers import TimeDistributed, Masking, Dense
import numpy as np


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        x = y = np.array([[[752], [14]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_2(self):
        x = y = np.array([[[824], [570]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_3(self):
        x = y = np.array([[[45], [316]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_4(self):
        x = y = np.array([[[434], [98]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_5(self):
        x = y = np.array([[[405], [488]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_6(self):
        x = y = np.array([[[692], [668]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_7(self):
        x = y = np.array([[[500], [75]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_8(self):
        x = y = np.array([[[778], [928]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_9(self):
        x = y = np.array([[[585], [136]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1

    def test_diversity_10(self):
        x = y = np.array([[[683], [171]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 1


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        x = y = np.array([[[446], [710]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_2(self):
        x = y = np.array([[[81], [15]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_3(self):
        x = y = np.array([[[56], [436]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_4(self):
        x = y = np.array([[[803], [482]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_5(self):
        x = y = np.array([[[35], [843]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_6(self):
        x = y = np.array([[[889], [737]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_7(self):
        x = y = np.array([[[368], [983]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_8(self):
        x = y = np.array([[[59], [757]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_9(self):
        x = y = np.array([[[199], [572]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0

    def test_diversity_10(self):
        x = y = np.array([[[506], [580]]])
        model = Sequential()
        model.add(Masking(mask_value=0, input_shape=(None, 1)))
        model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
        model.compile(loss='mse', optimizer='sgd')
        loss = model.train_on_batch(x, y)
        assert loss == 0
