import argparse
import sys
import re


import json
from youtube_dl.utils import js_to_json


def js_to_json_fixed(code):
    def fix_kv(m):
        v = m.group(0)
        if v in ('true', 'false', 'null'):
            return v
        if v.startswith('"'):
            v = re.sub(r"\\'", "'", v[1:-1])
        elif v.startswith("'"):
            v = v[1:-1]
            v = re.sub(r"\\\\|\\'|\"", lambda m: {
                '\\\\': '\\\\',
                "\\'": "'",
                '"': '\\"',
            }[m.group(0)], v)
        return '"%s"' % v

    res = re.sub(r'''(?x)
        "(?:[^"\\]*(?:\\\\|\\['"nu]))*[^"\\]*"|
        '(?:[^'\\]*(?:\\\\|\\['"nu]))*[^'\\]*'|
        [a-zA-Z_][.a-zA-Z_0-9]*
        ''', fix_kv, code)
    res = re.sub(r',(\s*[\]}])', lambda m: m.group(1), res)
    return res


if __name__ == "__main__":
    query = sys.argv[1]

    result_buggy = js_to_json(query)
    result_fixed = js_to_json_fixed(query)

    if result_buggy != result_fixed:
        raise AssertionError("Input does not match the expected outcome!")
