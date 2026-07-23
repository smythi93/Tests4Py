import sys
import os

# The bug 2 fault is that get_all_executables splits $PATH on a hard-coded ':'
# instead of os.pathsep. On a Unix host both are ':' by default, so we make the
# fault observable by forcing a Windows-style separator. In "semi" mode PATH is
# joined with ';' and os.pathsep is ';': the fixed code splits correctly and
# finds the executables, while the buggy code (splitting on ':') sees one bogus
# directory and finds nothing. In "plain" mode both behave identically.
if __name__ == "__main__":
    assert len(sys.argv) == 3
    name = sys.argv[1]
    mode = sys.argv[2]
    real_dirs = ["/usr/bin", "/bin", "/usr/sbin", "/sbin"]
    if mode == "semi":
        os.pathsep = ";"
        os.environ["PATH"] = ";".join(real_dirs)
    else:
        os.pathsep = ":"
        os.environ["PATH"] = ":".join(real_dirs)
    from thefuck.utils import get_all_executables

    executables = get_all_executables()
    if any(name == s for s in executables):
        print(name)
