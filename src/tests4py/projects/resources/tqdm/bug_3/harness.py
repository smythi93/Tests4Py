import sys

from tqdm import tqdm

if __name__ == "__main__":
    mode = sys.argv[1]
    n = int(sys.argv[2])
    if mode == "gen":
        t = tqdm((x for x in range(n)), disable=True)
    elif mode == "list":
        t = tqdm(list(range(n)), disable=True)
    else:
        t = tqdm(total=n, disable=True)
    print(bool(t))
