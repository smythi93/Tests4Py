import sys

from tqdm import tqdm

if __name__ == "__main__":
    mode = sys.argv[1]
    n = int(sys.argv[2])
    if mode == "list_dis":
        t = tqdm(list(range(n)), disable=True)
    elif mode == "range_dis":
        t = tqdm(range(n), disable=True)
    else:  # total_dis
        t = tqdm(total=n, disable=True)
    print(bool(t))
