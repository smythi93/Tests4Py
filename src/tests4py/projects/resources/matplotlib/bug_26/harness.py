import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Input: ``<old_min> <old_max> <new_min> <new_max>``.  The harness seeds an
# axis data interval with (old_min, old_max) (which may be *inverted*, i.e.
# old_min > old_max) and then grows it with (new_min, new_max) via
# ``set_data_interval(..., ignore=False)``, printing the resulting interval.
if __name__ == "__main__":
    old_min, old_max, new_min, new_max = (float(x) for x in sys.argv[1:5])
    fig, ax = plt.subplots()
    axis = ax.xaxis
    axis.set_data_interval(old_min, old_max, ignore=True)
    axis.set_data_interval(new_min, new_max, ignore=False)
    print([round(float(v), 9) for v in axis.get_data_interval()])
