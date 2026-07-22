import base64
import json
import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import get_element_by_attribute

if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    print(repr(get_element_by_attribute(d["attr"], d["value"], d["html"])))
