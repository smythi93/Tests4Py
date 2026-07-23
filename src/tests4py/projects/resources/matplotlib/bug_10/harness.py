import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    axis = sys.argv[1]
    b1 = sys.argv[2] == "true"
    b2 = sys.argv[3] == "true"
    exp = int(sys.argv[4])
    npts = int(sys.argv[5])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    data = [(1.01 + 0.01 * i) * 10 ** exp for i in range(npts)]
    if axis == "x":
        ax.plot(data, [0] * len(data))
    else:
        ax.plot(data)
    a = ax.xaxis if axis == "x" else ax.yaxis
    a.set_tick_params(label1On=b1, label2On=b2)
    print(a.get_offset_text().get_visible())
