import argparse
import sys
import re


from youtube_dl.utils import str_to_int
from youtube_dl.compat import compat_str


def str_to_int_fixed(int_str):
    """ A more relaxed version of int_or_none """
    if not isinstance(int_str, compat_str):
        return int_str
    int_str = re.sub(r'[,\.\+]', '', int_str)
    return int(int_str)


if __name__ == "__main__":
    str_or_int, query = sys.argv[1].split(" ")

    if str_or_int == '-i':
        query = eval(query)  # high security risk, but this should be fine here

    result_buggy = str_to_int(query)
    result_fixed = str_to_int_fixed(query)

    if result_buggy != result_fixed:
        raise AssertionError("Input does not match the expected outcome!")
