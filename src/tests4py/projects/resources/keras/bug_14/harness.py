import sys
import numpy as np
from keras import metrics
from keras import backend as K

if __name__ == "__main__":
    assert len(sys.argv) == 3
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if all_values[1] == "1.0":
        print(all_values[0])
    else:
        print(ValueError)
