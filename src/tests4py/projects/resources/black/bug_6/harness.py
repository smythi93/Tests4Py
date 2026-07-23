import base64
import sys

import black


def _format(src: str) -> str:
    # Target Python 3.7, where ``async`` / ``await`` are reserved keywords and
    # therefore invalid as identifiers.  Correct (fixed) black rejects such
    # code; the buggy tokenizer accepts it.
    mode = black.FileMode(target_versions={black.TargetVersion.PY37})
    return black.format_str(src, mode=mode)


if __name__ == "__main__":
    data = sys.argv[1]
    src = base64.urlsafe_b64decode(data.encode("ascii")).decode("utf-8")
    try:
        out = _format(src)
    except Exception as exception:  # noqa: BLE001
        sys.stdout.write("ERR:" + type(exception).__name__ + ":" + str(exception))
    else:
        sys.stdout.write("OK:" + base64.urlsafe_b64encode(out.encode("utf-8")).decode("ascii"))
