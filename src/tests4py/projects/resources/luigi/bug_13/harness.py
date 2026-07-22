import os
import sys
import tempfile

from luigi.file import LocalFileSystem

if __name__ == "__main__":
    mode = sys.argv[1]
    name = sys.argv[2]

    base = tempfile.mkdtemp(prefix="t4p_" + name + "_")
    src = os.path.join(base, "src.txt")
    open(src, "w").close()
    if mode == "newdir":
        dest = os.path.join(base, "newdir", "dest.txt")
    else:  # samedir
        dest = os.path.join(base, "dest.txt")

    LocalFileSystem().move(src, dest)
    print("HARNESS_OK" if os.path.exists(dest) else "MISSING")
