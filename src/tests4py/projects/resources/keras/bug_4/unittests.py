import unittest
import numpy as np
from keras import constraints
from tensorflow import train
from keras.models import Sequential
from keras.layers.core import Dense
from keras import optimizers


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((8483, 3)), np.random.random((8483, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_2(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((7234, 3)), np.random.random((7234, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_3(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((1438, 3)), np.random.random((1438, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_4(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((3299, 3)), np.random.random((3299, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_5(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((2041, 3)), np.random.random((2041, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_6(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((217, 3)), np.random.random((217, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_7(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((843, 3)), np.random.random((843, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_8(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((4008, 3)), np.random.random((4008, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_9(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((8309, 3)), np.random.random((8309, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_10(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((5635, 3)), np.random.random((5635, 2)), epochs=1, batch_size=5, verbose=0)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((9524, 3)), np.random.random((9524, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_2(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((6965, 3)), np.random.random((6965, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_3(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((6259, 3)), np.random.random((6259, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_4(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((6743, 3)), np.random.random((6743, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_5(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((8372, 3)), np.random.random((8372, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_6(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((7199, 3)), np.random.random((7199, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_7(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((355, 3)), np.random.random((355, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_8(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((5699, 3)), np.random.random((5699, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_9(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((5650, 3)), np.random.random((5650, 2)), epochs=1, batch_size=5, verbose=0)

    def test_diversity_10(self):
        class MyTfOptimizer(train.Optimizer):
            wrapping_optimizer = train.AdamOptimizer()

            def compute_gradients(self, loss, param, **kwargs):
                return super(MyTfOptimizer, self).compute_gradients(loss, param, **kwargs)

            def apply_gradients(self, grads_and_vars, **kwargs):
                return self.wrapping_optimizer.apply_gradients(grads_and_vars, **kwargs)

        my_tf_optimizer = MyTfOptimizer(use_locking=False, name='MyTfOptimizer')
        optimizer = optimizers.TFOptimizer(my_tf_optimizer)
        model = Sequential()
        model.add(Dense(2, input_shape=(3,), kernel_constraint=constraints.MaxNorm(1)))
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        model.fit(np.random.random((9690, 3)), np.random.random((9690, 2)), epochs=1, batch_size=5, verbose=0)
