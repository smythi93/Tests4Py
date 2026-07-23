import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

if __name__ == "__main__":
    fillstyle = sys.argv[1]
    n = int(sys.argv[2])
    grays = [round((i + 1) / (n + 1), 3) for i in range(n)]
    coll = plt.scatter(
        range(n),
        range(n),
        c=[str(g) for g in grays],
        marker=MarkerStyle("o", fillstyle=fillstyle),
        linewidths=[1.0] * n,
    )
    print(coll.get_facecolors().shape[0])
