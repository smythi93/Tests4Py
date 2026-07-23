import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    mult = float(sys.argv[1])
    kind = sys.argv[2]
    text = "" if kind == "EMPTY" else kind
    fig, ax = plt.subplots()
    t1 = ax.text(0.5, 0.5, text, ha="left", va="bottom")
    fig.canvas.draw()
    dpi = fig.dpi
    t1.get_window_extent()
    t1.get_window_extent(dpi=dpi * mult)
    print(fig.dpi == dpi)
