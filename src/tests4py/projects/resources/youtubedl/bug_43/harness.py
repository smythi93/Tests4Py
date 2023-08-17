import argparse
import sys
from pathlib import Path
from typing import Set, List
import os
import string
import operator
import re


from youtube_dl.utils import url_basename
#from youtube_dl.compat import compat_str


def url_basename_fixed(url):
    m = re.match(r'(?:https?:|)//[^/]+/(?:[^/?#]+/)?([^/?#]+)/?(?:[?#]|$)', url)
    m = re.match(r'(?:https?:|)//[^/]+/(?:[^?#]+/)?([^/?#]+)/?(?:[?#]|$)', url)
    if not m:
        return u''
    return m.group(1)


if __name__ == "__main__":
    query = sys.argv[1]

    result_buggy = url_basename(query)
    result_fixed = url_basename_fixed(query)

    if result_buggy != result_fixed:
        raise AssertionError("Input does not match the expected outcome!")
