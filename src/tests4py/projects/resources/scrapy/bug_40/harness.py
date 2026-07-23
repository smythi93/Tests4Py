import ast
import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.exporters import PythonItemExporter

if __name__ == "__main__":
    spec = base64.urlsafe_b64decode(sys.argv[1].encode("ascii")).decode("utf-8")
    item = ast.literal_eval(spec)
    exporter = PythonItemExporter(binary=False)
    exported = exporter.export_item(item)
    print("OK:" + base64.urlsafe_b64encode(repr(exported).encode("utf-8")).decode("ascii"))
