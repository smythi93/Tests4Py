import sys

# noinspection PyUnresolvedReferences
from scrapy.http import Response

# noinspection PyUnresolvedReferences
from scrapy.utils.gz import is_gzipped

if __name__ == "__main__":
    ctype = sys.argv[1]
    response = Response("http://www.example.com", headers={"Content-Type": ctype})
    print(is_gzipped(response))
