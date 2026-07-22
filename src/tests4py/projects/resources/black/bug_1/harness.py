import asyncio
import os
import sys
import tempfile
from unittest.mock import patch

from click.testing import CliRunner

import black


def _run(kind: str, nonce: str) -> bool:
    # a fresh event loop keeps repeated runs independent
    asyncio.set_event_loop(asyncio.new_event_loop())
    d = tempfile.mkdtemp()
    files = [os.path.join(d, "f_%s_%d.py" % (nonce, i)) for i in range(2)]
    for f in files:
        with open(f, "w") as fh:
            fh.write("print('hello')")
    if kind == "patched":
        # emulate an environment where multiprocessing is unavailable
        with patch("black.ProcessPoolExecutor") as mock_executor:
            mock_executor.side_effect = OSError()
            CliRunner().invoke(black.main, [d])
    else:
        CliRunner().invoke(black.main, [d])
    return all(open(f).read() == 'print("hello")\n' for f in files)


if __name__ == "__main__":
    kind = sys.argv[1]
    nonce = sys.argv[2]
    try:
        ok = _run(kind, nonce)
    except Exception as exception:  # noqa: BLE001
        sys.stdout.write("ERR:" + type(exception).__name__)
    else:
        sys.stdout.write("OK" if ok else "ERR:notformatted")
