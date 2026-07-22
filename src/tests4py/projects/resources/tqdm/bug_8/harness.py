import sys

from tqdm import tqdm

if __name__ == "__main__":
    n = int(sys.argv[1])
    total = int(sys.argv[2])
    elapsed = float(sys.argv[3])
    left = sys.argv[4]
    mode = sys.argv[5]
    right = sys.argv[6]
    field = "{bar}" if mode == "bar" else "{n_fmt}"
    bar_format = left + field + right
    print(tqdm.format_meter(n, total, elapsed, bar_format=bar_format))
