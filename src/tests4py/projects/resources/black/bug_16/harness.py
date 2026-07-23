import os
import re
import sys
import tempfile
from pathlib import Path

import black


def _run(kind: str, nonce: str) -> None:
    root = Path(tempfile.mkdtemp()).resolve()
    child = root / ("link_%s.py" % nonce)
    if kind == "symlink":
        outside = Path(tempfile.mkdtemp()).resolve() / "target.py"
        outside.write_text("x = 1\n")
        os.symlink(str(outside), str(child))
    else:
        child.write_text("x = 1\n")
    include = re.compile(black.DEFAULT_INCLUDES)
    exclude = re.compile(black.DEFAULT_EXCLUDES)
    report = black.Report()
    list(black.gen_python_files_in_dir(root, root, include, exclude, report))


if __name__ == "__main__":
    kind = sys.argv[1]
    nonce = sys.argv[2]
    try:
        _run(kind, nonce)
    except Exception as exception:  # noqa: BLE001
        sys.stdout.write("ERR:" + type(exception).__name__)
    else:
        sys.stdout.write("OK")
