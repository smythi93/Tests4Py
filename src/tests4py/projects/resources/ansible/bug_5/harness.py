import sys
from collections import OrderedDict

from ansible.module_utils.common.validation import check_required_arguments
from ansible.module_utils._text import to_native

if __name__ == "__main__":
    names = sys.argv[1:]
    spec = OrderedDict((n, {"required": True}) for n in names)
    try:
        check_required_arguments(spec, {})
        print("NO_ERROR")
    except TypeError as e:
        print(to_native(e))
