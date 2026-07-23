import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    n = int(sys.argv[1])
    comps = [float(x) for x in sys.argv[2].split(",")]
    fig, ax = plt.subplots()
    coll = ax.scatter(np.ones(n), range(n), c=[comps])
    print(coll.get_array() is None)
