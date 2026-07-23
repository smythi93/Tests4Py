import os
import sys

from thefuck.shells.fish import Fish

# The bug is in Fish._get_overridden_aliases: when TF_OVERRIDDEN_ALIASES is set,
# the buggy build *replaces* the built-in default {cd, grep, ls, man, open} with
# only the environment-provided aliases, whereas the fixed build always unions
# the default set in. Probing for a default alias while the env holds only
# non-default aliases therefore returns False on the buggy build and True on the
# fixed build. No fish binary is involved -- the method only reads os.environ.
if __name__ == "__main__":
    env_aliases = sys.argv[2]
    needle = sys.argv[3]
    os.environ["TF_OVERRIDDEN_ALIASES"] = env_aliases
    print(needle in Fish()._get_overridden_aliases())
