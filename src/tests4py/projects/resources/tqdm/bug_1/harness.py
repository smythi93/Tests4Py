import sys

from tqdm.contrib import tenumerate

if __name__ == "__main__":
    start = int(sys.argv[1])
    items = sys.argv[2:]
    result = [i for i, _ in tenumerate(items, start=start, disable=True)]
    print(result)
