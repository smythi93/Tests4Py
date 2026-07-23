import sys
from thefuck.types import Settings

# The bug 29 fault is in Settings.update: the buggy version lets the kwargs
# override the existing settings, while the fixed version only fills in unset
# settings (the existing self values win). We start with {key: oldval} and
# update(key=newval): the buggy result is newval, the fixed result is oldval.
if __name__ == "__main__":
    assert len(sys.argv) == 5
    expected = sys.argv[1]
    key = sys.argv[2]
    oldval = sys.argv[3]
    newval = sys.argv[4]
    settings = Settings({key: oldval})
    result = settings.update(**{key: newval})
    print(result[key])
