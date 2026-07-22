import os
import sys

from thefuck.shells.fish import Fish

# A deterministic, host-independent set of overridden aliases injected through
# the environment variable that Fish._get_overridden_aliases (the buggy
# function) reads. This avoids depending on the host's fish configuration.
OVERRIDDEN = (
    "cd,grep,ls,man,open,git,vim,cat,echo,sed,"
    "awk,find,make,node,curl,tar,wget,rm,cp,mv"
)

if __name__ == "__main__":
    name = sys.argv[1]
    os.environ["TF_OVERRIDDEN_ALIASES"] = OVERRIDDEN
    if name in Fish()._get_overridden_aliases():
        print(name)
    else:
        print("Error Retrieving Fish Shell Overridden")
