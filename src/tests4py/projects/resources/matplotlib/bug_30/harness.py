import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.colors as mcolors

if __name__ == "__main__":
    n = int(sys.argv[1])
    gamma = float(sys.argv[2])
    data = []
    for tok in sys.argv[3:]:
        a, b, c = tok.split(",")
        data.append((float(a), float(b), float(c)))
    lut = mcolors.makeMappingArray(n, data, gamma)
    print([round(float(v), 6) for v in np.atleast_1d(np.asarray(lut))])
