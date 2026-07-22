import contextlib
import io
import sys

from ansible.playbook.collectionsearch import CollectionSearch

if __name__ == "__main__":
    name = sys.argv[1]
    cs = CollectionSearch()
    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        result = cs._load_collections(None, [name])
    err = buf.getvalue()
    warned = ("is not templatable" in err) and (name in err)
    print("WARN" if warned else "NOWARN")
