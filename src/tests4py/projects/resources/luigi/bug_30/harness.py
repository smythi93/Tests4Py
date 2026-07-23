import sys

import luigi
from luigi import Event, Task, build


class DummyException(Exception):
    pass


def _run(self):
    if self.fail:
        raise DummyException()


if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    fail = mode == "fail"
    T = type("ET_" + tag, (Task,), {"fail": luigi.BoolParameter(), "run": _run})
    successes = []
    failures = []
    T.event_handler(Event.SUCCESS)(lambda task: successes.append(task))
    T.event_handler(Event.FAILURE)(lambda task, exc: failures.append(task))
    t = T(fail)
    build([t], local_scheduler=True)
    total = len(successes) + len(failures)
    print(
        "HARNESS_OK"
        if total == 1
        else "BAD S%dF%d" % (len(successes), len(failures))
    )
