import sys
import warnings

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    axis = sys.argv[1]
    left = float(sys.argv[2])
    right = float(sys.argv[3])
    fig, ax = plt.subplots()
    getattr(ax, "set_" + axis + "scale")("log")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        getattr(ax, "set_" + axis + "lim")(left, right)
    print("OK")
