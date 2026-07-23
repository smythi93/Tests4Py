import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    visible = sys.argv[1]
    x = float(sys.argv[2])
    y = float(sys.argv[3])
    fig, ax = plt.subplots()
    if visible == "false":
        ax.set_visible(False)
    print(fig.canvas.inaxes((x, y)) is None)
