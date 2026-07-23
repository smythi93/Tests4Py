import io
import sys

import thefuck.shells.fish as fish_mod
from thefuck.utils import cache, memoize

# Fish.info() reports the fish version. The buggy build runs
# ``fish -c 'echo $FISH_VERSION'`` and ``.strip()``s the output; the fixed build
# runs ``fish --version`` and takes ``.split()[-1]``. We monkeypatch the Popen
# used inside fish so the two command forms return controlled output: the buggy
# (echo) form yields raw_echo, the fixed (--version) form yields
# "fish, version <ver>". With raw_echo != ver the two builds disagree, with
# raw_echo == ver they agree. cache/memoize are disabled so info() recomputes.
# argv: expected("Fish Shell <ver>"), raw_echo, ver.
if __name__ == "__main__":
    cache.disabled = True
    memoize.disabled = True
    raw_echo = sys.argv[2]
    ver = sys.argv[3]

    class FakeProc:
        def __init__(self, data):
            self.stdout = io.BytesIO(data)

        def wait(self, *a, **k):
            return 0

    def fake_popen(args, *a, **k):
        if "--version" in args:
            return FakeProc(("fish, version " + ver).encode("utf-8"))
        return FakeProc(raw_echo.encode("utf-8"))

    fish_mod.Popen = fake_popen
    print(fish_mod.Fish().info())
