import sys

# noinspection PyUnresolvedReferences
from scrapy.utils.datatypes import LocalCache

if __name__ == "__main__":
    limit_arg = sys.argv[1]
    n = int(sys.argv[2])
    limit = None if limit_arg == "none" else int(limit_arg)
    cache = LocalCache(limit=limit)
    for i in range(n):
        cache[str(i)] = i
    print(repr((len(cache), list(cache.items()))))
