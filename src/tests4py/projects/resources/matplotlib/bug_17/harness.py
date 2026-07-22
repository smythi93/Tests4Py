import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.transforms as mtransforms

_DTYPES = {
    "int8": np.int8,
    "int16": np.int16,
    "int32": np.int32,
    "int64": np.int64,
    "float64": np.float64,
}

if __name__ == "__main__":
    dtype = _DTYPES[sys.argv[1]]
    vmin = dtype(int(sys.argv[2]) if "int" in sys.argv[1] else float(sys.argv[2]))
    vmax = dtype(int(sys.argv[3]) if "int" in sys.argv[1] else float(sys.argv[3]))
    out = mtransforms.nonsingular(vmin, vmax)
    print([round(float(v), 9) for v in out])
