import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
from matplotlib.collections import EventCollection

if __name__ == "__main__":
    values = [float(x) for x in sys.argv[1:]]
    arr = np.array(values, dtype=float)
    EventCollection(arr)
    print([round(float(v), 6) for v in arr])
