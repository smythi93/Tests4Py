import os
import subprocess
import sys
import tempfile


def _reformat(kind: str, nonce: str) -> bool:
    d = tempfile.mkdtemp()
    path = os.path.join(d, "f_" + nonce + ".py")
    newline = b"\r\n" if kind == "crlf" else b"\n"
    contents = newline.join([b"def f(  ):", b"    pass"])
    with open(path, "wb") as f:
        f.write(contents)
    subprocess.run(
        [sys.executable, "-m", "black", "-q", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    with open(path, "rb") as f:
        updated = f.read()
    return b"\r\n" in updated


if __name__ == "__main__":
    kind = sys.argv[1]
    nonce = sys.argv[2]
    has_crlf = _reformat(kind, nonce)
    sys.stdout.write("KIND:%s CRLF:%d" % (kind, 1 if has_crlf else 0))
