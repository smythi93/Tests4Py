import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    mode = sys.argv[1]
    group = sys.argv[2]
    marker = sys.argv[3]
    plt.rcdefaults()
    if mode == "box":
        plt.rcParams["lines.marker"] = marker
    elif group == "fliers":
        plt.rcParams["boxplot.flierprops.marker"] = marker
    else:
        plt.rcParams["boxplot.meanprops.marker"] = marker
    fig, ax = plt.subplots()
    d = np.arange(100)
    d[-1] = 150
    bxp = ax.boxplot(d, showmeans=True)
    print(bxp[group][0].get_marker())
