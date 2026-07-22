import sys

from thefuck.shells.fish import Fish

if __name__ == "__main__":
    # All arguments joined form a "needle" that is checked against the string
    # returned by Fish().info() (the function affected by the bug). The needle
    # is only ever a substring of the invariant "Fish Shell" prefix (passing)
    # or a string that never appears in the version output (failing).
    needle = " ".join(sys.argv[1:])
    info = Fish().info()
    if needle and needle in info:
        print("IN")
    else:
        print("OUT")
