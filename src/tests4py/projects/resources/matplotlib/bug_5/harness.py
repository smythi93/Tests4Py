import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    marker = sys.argv[1]
    lw = float(sys.argv[2])
    fig, ax = plt.subplots()
    pc = ax.scatter(range(5), [0] * 5, c="C0", marker=marker, s=100, linewidths=lw)
    print(float(pc.get_linewidths()[0]))
