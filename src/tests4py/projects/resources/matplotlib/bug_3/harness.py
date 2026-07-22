import sys

import matplotlib

matplotlib.use("Agg")
from matplotlib.markers import MarkerStyle

if __name__ == "__main__":
    marker = sys.argv[1]
    fillstyle = sys.argv[2]
    print(bool(MarkerStyle(marker, fillstyle).is_filled()))
