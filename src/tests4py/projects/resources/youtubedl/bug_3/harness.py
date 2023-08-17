import argparse
import sys
from pathlib import Path
from typing import Set, List
import os
import string
import operator
import re


from youtube_dl.utils import unescapeHTML, _htmlentity_transform
from youtube_dl.compat import compat_str


def unescapeHTML_fixed(s):
    if s is None:
        return None
    assert type(s) == compat_str

    return re.sub(
        r'&([^&;]+;)', lambda m: _htmlentity_transform(m.group(1)), s)


if __name__ == "__main__":
    query = sys.argv[1]

    result_buggy = unescapeHTML(query)
    result_fixed = unescapeHTML_fixed(query)

    if result_buggy != result_fixed:
        raise AssertionError("Input does not match the expected outcome!")
