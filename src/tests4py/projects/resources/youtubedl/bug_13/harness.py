import argparse
import sys
import re


from youtube_dl.utils import urljoin
from youtube_dl.compat import compat_str, compat_urlparse


def urljoin_fixed(base, path):
    if isinstance(path, bytes):
        path = path.decode('utf-8')
    if not isinstance(path, compat_str) or not path:
        return None
    if re.match(r'^(?:[a-zA-Z][a-zA-Z0-9+-.]*:)?//', path):
        return path
    if isinstance(base, bytes):
        base = base.decode('utf-8')
    if not isinstance(base, compat_str) or not re.match(
            r'^(?:https?:)?//', base):
        return None
    return compat_urlparse.urljoin(base, path)


if __name__ == "__main__":
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-b", dest="base", default=None)
    arguments.add_argument("-p", dest="path", default=None)

    args = arguments.parse_args()
    # raise AssertionError(f"{args.base}, {args.path}")

    result_buggy = urljoin(args.base, args.path)
    result_fixed = urljoin_fixed(args.base, args.path)
    # raise AssertionError(f"Input does not match the expected outcome!{args.base}, {args.path}")
    if result_buggy != result_fixed:
        raise AssertionError(f"Input does not match the expected outcome!{args.base}, {args.path}")
