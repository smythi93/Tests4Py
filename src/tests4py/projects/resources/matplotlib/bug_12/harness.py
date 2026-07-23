import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    func = sys.argv[1]
    tokens = sys.argv[2].split(",")
    data = [float("nan") if t == "nan" else float(t) for t in tokens]
    fig, ax = plt.subplots()
    coll = getattr(ax, func)(data, 0, 1)
    print(len(coll.get_segments()))
