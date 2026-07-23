import os
import sys
import tempfile
from pathlib import Path

import black


def _run(kind: str, nonce: str) -> None:
    path = Path(tempfile.mkdtemp()) / ("f_" + nonce + ".py")
    if kind == "empty":
        path.write_bytes(b"")
    else:
        path.write_bytes(b"x = 1\n")
    black.format_file_in_place(path, 88, False, black.WriteBack.YES)


if __name__ == "__main__":
    kind = sys.argv[1]
    nonce = sys.argv[2]
    try:
        _run(kind, nonce)
    except Exception as exception:  # noqa: BLE001
        sys.stdout.write("ERR:" + type(exception).__name__)
    else:
        sys.stdout.write("OK")
