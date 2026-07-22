import os
import subprocess
import sys
import tempfile


def _run(kind: str) -> int:
    d = tempfile.mkdtemp()
    src = os.path.join(d, "s.py")
    with open(src, "w") as f:
        f.write("x = 1\n")
    if kind == "invalid":
        # a config path that does not exist
        config = os.path.join(d, "does_not_exist.toml")
    else:
        config = os.path.join(d, "cfg.toml")
        with open(config, "w") as f:
            f.write("")
    proc = subprocess.run(
        [sys.executable, "-m", "black", "--config", config, "--check", src],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.returncode


if __name__ == "__main__":
    kind = sys.argv[1]
    sys.stdout.write("RC:%d" % _run(kind))
