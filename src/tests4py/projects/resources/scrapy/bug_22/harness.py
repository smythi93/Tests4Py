import ast
import base64
import sys
from io import BytesIO

# noinspection PyUnresolvedReferences
from scrapy.exporters import XmlItemExporter

if __name__ == "__main__":
    item = ast.literal_eval(
        base64.urlsafe_b64decode(sys.argv[1].encode("ascii")).decode("utf-8")
    )
    fp = BytesIO()
    exporter = XmlItemExporter(fp)
    try:
        exporter.start_exporting()
        exporter.export_item(item)
        exporter.finish_exporting()
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + base64.urlsafe_b64encode(fp.getvalue()).decode("ascii"))
