import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    func = sys.argv[1]
    color = sys.argv[2]
    pos = float(sys.argv[3])
    lo = float(sys.argv[4])
    hi = float(sys.argv[5])
    fig, ax = plt.subplots()
    with mpl.rc_context({"lines.color": color}):
        lines = getattr(ax, func)(pos, lo, hi)
        print(mpl.colors.same_color(lines.get_color(), color))
