import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    trigger = sys.argv[1]
    w = float(sys.argv[2])
    h = float(sys.argv[3])
    if trigger == "polar":
        plt.figure(figsize=(w, h))
        plt.polar()
        ax = plt.gca()
    else:
        fig = plt.figure(figsize=(w, h))
        ax = fig.add_subplot(projection="polar")
        if trigger == "draw":
            fig.canvas.draw()
        elif trigger == "autoscale":
            ax.autoscale()
            fig.canvas.draw()
        elif trigger == "relim":
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
    print([round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
