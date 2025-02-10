import unittest
import numpy as np
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.test_utils import get_test_data


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        np.random.seed(759)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_2(self):
        np.random.seed(1837)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_3(self):
        np.random.seed(6264)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_4(self):
        np.random.seed(8980)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_5(self):
        np.random.seed(5761)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_6(self):
        np.random.seed(4749)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_7(self):
        np.random.seed(373)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_8(self):
        np.random.seed(7507)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_9(self):
        np.random.seed(87)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)

    def test_diversity_10(self):
        np.random.seed(883)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=None)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        np.random.seed(7623)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_2(self):
        np.random.seed(1231)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_3(self):
        np.random.seed(332)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_4(self):
        np.random.seed(6664)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_5(self):
        np.random.seed(222)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_6(self):
        np.random.seed(412)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_7(self):
        np.random.seed(2)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_8(self):
        np.random.seed(9192)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_9(self):
        np.random.seed(534)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)

    def test_diversity_10(self):
        np.random.seed(123)
        img_gen = ImageDataGenerator(rescale=1.0)
        input_shape = (16, 16, 3)
        (x_train, y_train), (x_test, y_test) = get_test_data(num_train=500, num_test=200, input_shape=input_shape,
                                                             classification=True, num_classes=4)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        model = Sequential([layers.Conv2D(filters=8, kernel_size=3, activation='relu', input_shape=input_shape),
                            layers.MaxPooling2D(pool_size=2),
                            layers.Conv2D(filters=4, kernel_size=(3, 3), activation='relu', padding='same'),
                            layers.GlobalAveragePooling2D(),
                            layers.Dense(units=y_test.shape[-1], activation='softmax')])
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit_generator(img_gen.flow(x_train, y_train, batch_size=16), steps_per_epoch=3, epochs=3,
                                      validation_data=img_gen.flow(x_test, y_test, batch_size=16), validation_steps=3,
                                      verbose=0)
        assert history.history['val_acc'][-1] > 0.0
        model.evaluate_generator(img_gen.flow(x_train, y_train, batch_size=16), steps=1)
