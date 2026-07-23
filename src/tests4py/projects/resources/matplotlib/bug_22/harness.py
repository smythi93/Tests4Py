import datetime
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    kind = sys.argv[1]
    edges = [
        datetime.datetime.strptime(e, "%Y-%m-%d") for e in sys.argv[2].split(",")
    ]
    data = [
        [
            datetime.datetime(2019, 1, 5),
            datetime.datetime(2019, 1, 11),
            datetime.datetime(2019, 2, 1),
            datetime.datetime(2019, 3, 1),
        ],
        [
            datetime.datetime(2019, 1, 11),
            datetime.datetime(2019, 2, 5),
            datetime.datetime(2019, 2, 18),
            datetime.datetime(2019, 3, 1),
        ],
    ]
    bins = edges if kind == "datetime" else mpl.dates.date2num(edges)
    fig, ax = plt.subplots()
    _, out_bins, _ = ax.hist(data, bins=bins, stacked=True)
    print(len(out_bins))
