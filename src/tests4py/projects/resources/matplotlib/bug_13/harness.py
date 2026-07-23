import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
from matplotlib.path import Path

# Each argument is one path, given as comma-separated integer path codes
# (0=STOP, 1=MOVETO, 2=LINETO).  Every path must start with MOVETO.  The harness
# builds the Path objects, concatenates them with ``make_compound_path`` and
# prints the resulting code array.
if __name__ == "__main__":
    paths = []
    for token in sys.argv[1:]:
        codes = [int(c) for c in token.split(",")]
        verts = np.array(
            [[float(k), float(k)] for k in range(len(codes))], dtype=float
        )
        paths.append(Path(verts, codes))
    result = Path.make_compound_path(*paths)
    print([int(c) for c in result.codes])
