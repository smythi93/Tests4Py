import json
import os
import sys
import tempfile

from ansible.errors import AnsibleError
from ansible.galaxy.collection import verify_collections

if __name__ == "__main__":
    # argv: mode namespace name version
    mode = sys.argv[1]
    namespace = sys.argv[2]
    name = sys.argv[3]
    version = sys.argv[4]

    root = tempfile.mkdtemp()
    cdir = os.path.join(root, namespace, name)
    os.makedirs(cdir)
    if mode == "manifest":
        with open(os.path.join(cdir, "MANIFEST.json"), "w") as fh:
            json.dump(
                {
                    "collection_info": {
                        "namespace": namespace,
                        "name": name,
                        "version": "1.0.0",
                        "dependencies": {},
                    }
                },
                fh,
            )
    try:
        verify_collections(
            [("%s.%s" % (namespace, name), version, None)], [root], [], False, False
        )
        print("NO_ERROR")
    except AnsibleError as e:
        print(e.message)
    except Exception as e:
        print("OTHER:%s:%s" % (type(e).__name__, e))
