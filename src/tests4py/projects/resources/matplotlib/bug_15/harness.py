import math
import sys
import warnings

import matplotlib

matplotlib.use("Agg")
import matplotlib.colors as mcolors

if __name__ == "__main__":
    mode = sys.argv[1]
    linthresh = float(sys.argv[2])
    linscale = float(sys.argv[3])
    vmin = float(sys.argv[4])
    vmax = float(sys.argv[5])
    base_token = sys.argv[6]
    value = float(sys.argv[7])
    base = math.e if base_token == "e" else float(base_token)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        if mode == "basekw":
            norm = mcolors.SymLogNorm(
                linthresh, linscale, vmin=vmin, vmax=vmax, base=base
            )
        else:
            norm = mcolors.SymLogNorm(linthresh, linscale, vmin=vmin, vmax=vmax)
        print(round(float(norm(value)), 6))
