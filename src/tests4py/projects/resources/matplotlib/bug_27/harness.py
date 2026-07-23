import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    orient = sys.argv[1]
    initial = sys.argv[2]
    label = sys.argv[3]
    orientation = "vertical" if orient == "v" else "horizontal"
    fig, ax = plt.subplots()
    im = ax.imshow([[1, 2], [3, 4]])
    cbar = fig.colorbar(im, orientation=orientation, label=initial)
    cbar.set_label(None if label == "NONE" else label)
    print(cbar.ax.get_xlabel() if orient == "h" else cbar.ax.get_ylabel())
