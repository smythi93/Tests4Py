import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    order = sys.argv[1]
    size = float(sys.argv[2])
    family = sys.argv[3]
    fig, ax = plt.subplots()
    if order == "sf":
        t = ax.set_xlabel("value", size=size, fontproperties=family)
    else:
        t = ax.set_xlabel("value", fontproperties=family, size=size)
    print(t.get_size())
