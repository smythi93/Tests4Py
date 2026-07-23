import sys

import luigi
from luigi.util import requires, inherits

if __name__ == "__main__":
    mode = sys.argv[1]
    w = sys.argv[2]

    Required = type("Req_" + w, (luigi.Task,), {})
    Parent = type("Par_" + w, (luigi.Task,), {})
    Child = type("Child_" + w, (Parent,), {})
    if mode == "requires":
        Child = requires(Required)(Child)
    elif mode == "inherits":
        Child = inherits(Required)(Child)
    # plain: no decorator applied

    print(repr(str(Child.__mro__[0]) != str(Child.__mro__[1])))
