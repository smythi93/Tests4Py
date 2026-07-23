import shutil
import sys
import tempfile

# noinspection PyUnresolvedReferences
from scrapy.dupefilters import RFPDupeFilter

# noinspection PyUnresolvedReferences
from scrapy.http import Request

if __name__ == "__main__":
    mode = sys.argv[1]
    url = sys.argv[2]
    path = tempfile.mkdtemp()
    try:
        if mode == "persist":
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request(url))
            df.close("finished")
            df2 = RFPDupeFilter(path)
            df2.open()
            result = df2.request_seen(Request(url))
            df2.close("finished")
        else:  # "same": in-instance duplicate detection (True on both builds)
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request(url))
            result = df.request_seen(Request(url))
            df.close("finished")
        print(bool(result))
    finally:
        shutil.rmtree(path)
