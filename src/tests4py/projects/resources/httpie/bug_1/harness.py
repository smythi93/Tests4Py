import sys

import httpie.downloads


def make_exists(unique_on_attempt):
    def exists(filename):
        if exists.attempt == unique_on_attempt:
            return False
        exists.attempt += 1
        return True

    exists.attempt = 0
    return exists


if __name__ == "__main__":
    # argv: orig_name unique_on_attempt max_len expected
    orig_name = sys.argv[1]
    unique_on_attempt = int(sys.argv[2])
    max_len = int(sys.argv[3])
    # Force the maximum filename length the (fixed) implementation trims to.
    # On the buggy build this attribute is simply unused.
    httpie.downloads.get_filename_max_length = lambda directory: max_len
    result = httpie.downloads.get_unique_filename(
        orig_name, make_exists(unique_on_attempt)
    )
    print(result)
