import unittest
from keras.wrappers.scikit_learn import KerasRegressor
from keras.utils.test_utils import get_test_data
from tests.keras.wrappers.scikit_learn_test import epochs, batch_size, hidden_dims, build_fn_reg


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=203, num_test=928, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (758,)

    def test_diversity_2(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=766, num_test=183, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (529,)

    def test_diversity_3(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=380, num_test=601, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (670,)

    def test_diversity_4(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=340, num_test=444, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (737,)

    def test_diversity_5(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=906, num_test=992, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (72,)

    def test_diversity_6(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=46, num_test=963, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (24,)

    def test_diversity_7(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=774, num_test=894, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (213,)

    def test_diversity_8(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=613, num_test=406, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (153,)

    def test_diversity_9(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=864, num_test=542, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (839,)

    def test_diversity_10(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=813, num_test=240, input_shape=(5,), classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == (66,)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=682, num_test=152, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_2(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=827, num_test=799, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_3(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=516, num_test=293, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_4(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=543, num_test=964, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_5(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=574, num_test=395, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_6(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=993, num_test=790, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_7(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=807, num_test=50, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_8(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=18, num_test=3, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_9(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=833, num_test=904, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()

    def test_diversity_10(self):
        (X_train, y_train), (X_test, y_test) = get_test_data(num_train=483, num_test=64, input_shape=(5,),
                                                             classification=True, num_classes=3)
        reg = KerasRegressor(build_fn=build_fn_reg, hidden_dims=hidden_dims, batch_size=batch_size, epochs=epochs)
        reg.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        preds = reg.predict(X_test[:1], batch_size=batch_size)
        assert preds.shape == ()
