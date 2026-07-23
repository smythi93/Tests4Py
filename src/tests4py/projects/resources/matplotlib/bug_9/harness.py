import hashlib
import sys
import warnings

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt


def _render(scenario, rorigin, rmax, unstale):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
    if scenario == "stale":
        ax.yaxis.set_inverted(True)
        ax.plot([0, 0], [0, rmax], c="none")
        ax.margins(0)
        ax.set_rorigin(rorigin)
    else:
        theta = np.linspace(0, 2 * np.pi, 50)
        ax.plot(theta, np.ones(50) * rmax * 0.8)
        ax.set_rlim(0, rmax)
        ax.set_rorigin(rorigin)
    if unstale:
        ax._unstale_viewLim()
    fig.canvas.draw()
    buf = np.asarray(fig.canvas.buffer_rgba()).copy()
    plt.close(fig)
    return hashlib.md5(buf.tobytes()).hexdigest()


if __name__ == "__main__":
    scenario = sys.argv[1]
    rorigin = float(sys.argv[2])
    rmax = float(sys.argv[3])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        a = _render(scenario, rorigin, rmax, False)
        b = _render(scenario, rorigin, rmax, True)
    print(a == b)
