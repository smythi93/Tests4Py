import io
import sys

import thefuck.shells.fish as fish_mod
from thefuck.utils import cache, memoize

# fish._get_aliases parses `fish -ic alias` output. The buggy build splits every
# line only on ' ' (``name, value = line...split(' ', 1)``) and therefore raises
# ValueError on an ``alias name=value`` line (fish's '=' form) or on empty
# output; the fixed build also tries '=' as a separator and guards empty output.
# We monkeypatch the Popen used inside fish with a fake process yielding a canned
# alias line, so no real fish shell is involved and the input is fully
# controlled. _get_aliases is @cache-decorated (disk-memoized and argument
# agnostic), so we disable the cache to recompute on every call. argv:
# expected("OK"), alias-line.
if __name__ == "__main__":
    cache.disabled = True
    memoize.disabled = True
    alias_line = sys.argv[2]

    class FakeProc:
        def __init__(self, data):
            self.stdout = io.BytesIO(data)

        def wait(self, *a, **k):
            return 0

    fish_mod.Popen = lambda *a, **k: FakeProc(alias_line.encode("utf-8"))

    try:
        fish_mod._get_aliases(set())
        print("OK")
    except Exception:
        print("ERR")
