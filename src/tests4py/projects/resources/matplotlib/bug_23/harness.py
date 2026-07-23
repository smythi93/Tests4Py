import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    mode = sys.argv[1]
    xlo = float(sys.argv[2])
    xhi = float(sys.argv[3])
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_axes([.1, .1, .8, .8])
    ax.plot([.4, .6], [.4, .6])
    ax.set(xscale="log", xlim=(xlo, xhi), yscale="logit",
           ylim=(1 / 101, 1 / 11), aspect=1, adjustable=mode)
    ax.margins(0)
    ax.apply_aspect()
    cur = ax.get_xlim()
    print(abs(cur[0] - xlo) < 1e-06 and abs(cur[1] - xhi) < 1e-06)
