import sys

import luigi
from luigi.task_register import Register

if __name__ == "__main__":
    kind = sys.argv[1]
    name = sys.argv[2]
    if kind == "ext":
        cls = type(name, (luigi.ExternalTask,), {})
    else:
        cls = type(name, (luigi.Task,), {"run": lambda self: None})
    found = Register.get_task_cls(name)
    assert found is cls
    print("HARNESS_OK")
