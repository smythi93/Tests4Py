import base64
import sys

import black


def _format(src: str) -> str:
    # black's ``format_str`` signature changed across the versions covered by
    # these bugs.  Try the old ``line_length`` keyword first, then fall back to
    # the newer ``mode=`` based API.
    try:
        return black.format_str(src, line_length=88)
    except TypeError:
        pass
    mode = None
    for attr in ("Mode", "FileMode"):
        if hasattr(black, attr):
            try:
                mode = getattr(black, attr)()
            except Exception:
                mode = None
            break
    if mode is None:
        return black.format_str(src)
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
