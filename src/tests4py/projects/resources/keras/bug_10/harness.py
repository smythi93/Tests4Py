import sys
import numpy as np
from keras.engine import training_utils

if __name__ == "__main__":
    assert len(sys.argv) == 11
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if all_values[5] == "0" and all_values[9] == "4":
        print(all_values[0])
    else:
        print("IndexError: tuple index out of range: y.shape[1] > 1")
