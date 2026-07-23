import base64
import os
import subprocess
import sys
import tempfile


def _header_path(kind: str, nonce: str):
    d = tempfile.mkdtemp()
    name = "f_" + nonce + ".py"
    with open(os.path.join(d, name), "w") as f:
        f.write("x=1\n")
    if kind == "subdir":
        path = os.path.join(d, name)  # absolute path (has directory parts)
        cwd = None
    else:  # relative: run from within the directory
        path = name
        cwd = d
    proc = subprocess.run(
        [sys.executable, "-m", "black", "--diff", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
    )
    out = proc.stdout.decode("utf-8", "replace")
    first = out.splitlines()[0] if out else ""
    header = ""
    marker = "  (original)"
    if first.startswith("--- ") and marker in first:
        header = first[4 : first.index(marker)]
    return path, header


if __name__ == "__main__":
    kind = sys.argv[1]
    nonce = sys.argv[2]
    expected, header = _header_path(kind, nonce)
    sys.stdout.write(
        "EXP:%s HDR:%s"
        % (
            base64.urlsafe_b64encode(expected.encode()).decode(),
            base64.urlsafe_b64encode(header.encode()).decode(),
        )
    )
