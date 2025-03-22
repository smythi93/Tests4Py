import unittest
from keras import callbacks


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.53, 0.03, 0.17, 0.43, 0.78]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_2(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.78, 0.45, 1.0, 0.86, 0.43]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_3(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.46, 0.41, 0.37, 0.02, 0.61]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_4(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.21, 0.74, 0.48, 1.0, 0.73]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_5(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.58, 0.06, 0.35, 0.28, 0.49]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_6(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.6, 0.22, 0.58, 0.01, 0.21]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_7(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.75, 0.61, 0.77, 0.36, 0.36]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_8(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.82, 0.97, 0.96, 0.52, 0.41]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_9(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.22, 0.59, 0.23, 0.39, 0.86]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2

    def test_diversity_10(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        early_stop.model = DummyModel()
        losses = [0.38, 0.72, 0.83, 0.36, 0.08]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() == 2


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.12, 0.45, 0.93, 0.89, 0.62]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_2(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.08, 0.64, 0.53, 0.72, 0.35]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_3(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.84, 0.51, 0.17, 0.98, 0.18]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_4(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.87, 0.96, 0.91, 0.43, 0.94]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_5(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.68, 0.79, 0.94, 0.75, 0.12]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_6(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.18, 0.26, 0.73, 0.86, 0.87]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_7(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.68, 0.67, 0.33, 0.22, 0.4]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_8(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.33, 0.43, 0.24, 0.09, 0.64]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_9(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.39, 0.09, 0.17, 0.83, 0.09]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

    def test_diversity_10(self):

        class DummyModel(object):

            def __init__(self):
                self.stop_training = False
                self.weights = -1

            def get_weights(self):
                return self.weights

            def set_weights(self, weights):
                self.weights = weights

            def set_weight_to_epoch(self, epoch):
                self.weights = epoch
        early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=2)
        early_stop.model = DummyModel()
        losses = [0.83, 0.88, 0.13, 0.18, 0.42]
        epochs_trained = 0
        early_stop.on_train_begin()
        for epoch in range(len(losses)):
            epochs_trained += 1
            early_stop.model.set_weight_to_epoch(epoch=epoch)
            early_stop.on_epoch_end(epoch, logs={'val_loss': losses[epoch]})
            if early_stop.model.stop_training:
                break
        assert early_stop.model.get_weights() <= 4

