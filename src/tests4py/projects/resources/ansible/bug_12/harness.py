import os
import sys
from unittest import mock

import ansible.utils.py3compat as py3compat
from ansible.plugins.loader import lookup_loader

if __name__ == "__main__":
    mode = sys.argv[1]
    var = sys.argv[2]
    value = sys.argv[3]
    env_lookup = lookup_loader.get("env")
    if mode == "patch":
        os.environ.pop(var, None)
        with mock.patch.object(py3compat.environ, "get", lambda x, y=None: value):
            retval = env_lookup.run([var], None)
    else:
        os.environ[var] = value
        retval = env_lookup.run([var], None)
    print(retval[0] if retval else "EMPTY")
