import sys

import luigi
import luigi.worker
import luigi.scheduler
import luigi.execution_summary


def _complete(t):
    return t.run_count > 0


def _run_retry(t):
    t.run_count += 1
    if t.run_count == 1:
        raise ValueError()


def _run_clean(t):
    t.run_count += 1


if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    run_fn = _run_retry if mode == "retry" else _run_clean
    Foo = type(
        "Foo_" + tag,
        (luigi.Task,),
        {"run_count": 0, "run": run_fn, "complete": _complete},
    )
    sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
    w = luigi.worker.Worker(scheduler=sch)
    w.add(Foo())
    w.run()
    w.add(Foo())
    w.run()
    s = luigi.execution_summary.summary(w)
    print("HARNESS_OK" if ":(" not in s else "SAD")
