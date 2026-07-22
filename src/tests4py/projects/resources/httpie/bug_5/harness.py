import sys

from httpie import cli


if __name__ == "__main__":
    # argv[1] is a raw key-value item string (backslash escapes preserved).
    item = sys.argv[1]
    kt = cli.KeyValueType(
        cli.SEP_HEADERS,
        cli.SEP_DATA,
        cli.SEP_DATA_RAW_JSON,
        cli.SEP_FILES,
    )
    try:
        kv = kt(item)
        print(repr((kv.key, kv.value, kv.sep)))
    except Exception:
        print("ERROR")
