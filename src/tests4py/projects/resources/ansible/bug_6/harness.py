import sys

from ansible.errors import AnsibleError
from ansible.galaxy.collection import CollectionRequirement

if __name__ == "__main__":
    # argv: mode namespace name parent have req
    mode = sys.argv[1]
    namespace = sys.argv[2]
    name = sys.argv[3]
    parent = sys.argv[4]
    have = sys.argv[5]
    req = sys.argv[6]

    obj = CollectionRequirement(
        namespace, name, None, "https://galaxy.com", [have], have, False, skip=True
    )
    try:
        obj.add_requirement(parent, req)
        print("OK %s" % obj.latest_version)
    except AnsibleError:
        print("ERROR:AnsibleError")
    except Exception as e:
        print("OTHER:%s" % type(e).__name__)
