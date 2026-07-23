import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    axis = sys.argv[1]
    inverted = sys.argv[2] == "true"
    lo = float(sys.argv[3])
    hi = float(sys.argv[4])
    fig = plt.figure()
    ax0 = plt.subplot(211)
    share = "sharey" if axis == "y" else "sharex"
    ax1 = plt.subplot(212, **{share: ax0})
    ax0.plot([lo, hi], [lo, hi])
    getattr(ax0, axis + "axis").set_inverted(inverted)
    print(getattr(ax1, axis + "axis_inverted")())
