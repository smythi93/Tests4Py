import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

_AUTO_MAP = {"true": True, "false": False, "none": None}

if __name__ == "__main__":
    axis = sys.argv[1]
    auto = _AUTO_MAP[sys.argv[2]]
    lo = float(sys.argv[3])
    hi = float(sys.argv[4])
    fig, ax = plt.subplots()
    if axis == "y":
        ax.scatter(np.arange(100), np.linspace(-.1, .1, 100))
    else:
        ax.scatter(np.linspace(-.1, .1, 100), np.arange(100))
    getattr(ax, "set_" + axis + "lim")((lo, hi), auto=auto)
    fig.canvas.draw()
    print([round(float(v), 3) for v in getattr(ax, "get_" + axis + "lim")()])
