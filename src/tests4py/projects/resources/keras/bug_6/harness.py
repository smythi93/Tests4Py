import sys
from keras.models import Sequential
from keras.layers import TimeDistributed, Masking, Dense
import numpy as np

if __name__ == "__main__":
    assert len(sys.argv) == 4
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        i = int(i)
        all_values.append(i)

    x = y = np.array([[[all_values[0]], [all_values[1]]]])
    model = Sequential()
    model.add(Masking(mask_value=0, input_shape=(None, 1)))
    model.add(TimeDistributed(Dense(1, kernel_initializer='one')))
    model.compile(loss='mse', optimizer='sgd')
    loss = model.train_on_batch(x, y)
    assert loss == all_values[2]
    print(all_values[0])
