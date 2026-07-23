import sys

from thefuck.rules.dnf_no_such_command import match, _parse_operations
from thefuck.types import Command

# The dnf_no_such_command bug lives in ``_parse_operations``: the buggy build
# compiles a *bytes* regex (``re.compile(b'^([a-z-]+) +', re.MULTILINE)``) while
# the fixed build compiles the equivalent *str* regex. ``_get_operations`` on the
# fixed build decodes the ``dnf --help`` output to ``str`` before calling
# ``_parse_operations``; on the buggy build it leaves it as ``bytes``. Feeding a
# ``str`` help text therefore succeeds on the fixed build and raises
# ``TypeError: cannot use a bytes pattern on a string-like object`` on the buggy
# build. ``match`` is invariant across builds, so it anchors the passing tests.
if __name__ == "__main__":
    mode = sys.argv[2]
    if mode == "parse":
        ops = sys.argv[3].split(",")
        help_text = "\n".join("{}    description".format(op) for op in ops)
        result = _parse_operations(help_text)  # raises TypeError on buggy build
        decoded = [
            o.decode("utf-8") if isinstance(o, (bytes, bytearray)) else o
            for o in result
        ]
        print(" ".join(decoded))
    else:  # "match" -- invariant behaviour, used for passing tests
        script = sys.argv[3]
        output = sys.argv[4]
        print(match(Command(script, output)))
