import sys

from tqdm import tqdm

if __name__ == "__main__":
    n = int(sys.argv[1])
    total = None if sys.argv[2] == "None" else int(sys.argv[2])
    elapsed = float(sys.argv[3])
    unit_scale = float(sys.argv[4])
    try:
        res = tqdm.format_meter(n, total, elapsed, unit_scale=unit_scale)
        print("TQDM_OK:" + (res if res else ""))
    except Exception as e:
        print("TQDM_ERROR:" + repr(e))
        sys.exit(1)
