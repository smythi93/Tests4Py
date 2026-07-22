import os
import sys

from thefuck.shells.fish import Fish

# A deterministic, host-independent set of overridden aliases injected through
# the environment variable that Fish._get_overridden_aliases reads. This avoids
# calling the host's fish shell (whose alias output format is not portable).
OVERRIDDEN = (
    "git,vim,cat,echo,sed,awk,find,make,node,curl,"
    "tar,wget,rm,cp,mv,ssh,sort,uniq,head,tail"
)

if __name__ == "__main__":
    name = sys.argv[1]
    os.environ["THEFUCK_OVERRIDDEN_ALIASES"] = OVERRIDDEN
    if name in Fish()._get_overridden_aliases():
        print(name)
    else:
        print("Error Retrieving Fish Shell Overridden")
