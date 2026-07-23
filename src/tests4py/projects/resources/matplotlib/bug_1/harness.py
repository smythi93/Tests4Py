import sys
from io import BytesIO

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == "__main__":
    mode = sys.argv[1]
    x_size = int(sys.argv[2])
    y_size = int(sys.argv[3])
    dpi = int(sys.argv[4])
    fig = plt.figure(frameon=False, dpi=dpi, figsize=(x_size / dpi, y_size / dpi))
    ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])
    fig.add_axes(ax)
    ax.set_axis_off()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    data = np.arange(x_size * y_size).reshape(y_size, x_size)
    ax.imshow(data)
    out = BytesIO()
    if mode == "tight":
        fig.savefig(out, bbox_inches="tight", pad_inches=0)
    else:
        fig.savefig(out)
    out.seek(0)
    im = np.asarray(Image.open(out))
    print(bool((im[:, :, 3] == 255).all() and not (im[:, :, :3] == 255).all()))
