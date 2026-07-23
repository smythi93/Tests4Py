import sys
import shelve

import thefuck.utils as u

# thefuck.utils.cache opens a shelf as a context manager. The buggy build uses
# ``with shelve.open(path) as db`` directly, so a shelf object lacking the
# context-manager protocol (as under some dbm backends / Python 2) raises
# AttributeError; the fixed build wraps it in ``contextlib.closing`` and works.
# We monkeypatch shelve.open to return a dict-based fake shelf either WITH the
# protocol ("cm", works on both builds -> passing) or WITHOUT it ("nocm", only
# the fixed build survives -> distinguishing).
if __name__ == "__main__":
    value = sys.argv[1]
    mode = sys.argv[2]

    if mode == "cm":
        class Shelf(dict):
            def close(self):
                pass

            def __enter__(self):
                return self

            def __exit__(self, *a):
                self.close()
    else:  # "nocm"
        class Shelf(dict):
            def close(self):
                pass

    shelve.open = lambda *a, **k: Shelf()

    @u.cache()
    def compute():
        return value

    print(compute())
