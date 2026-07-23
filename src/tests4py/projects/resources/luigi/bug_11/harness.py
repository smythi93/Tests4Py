import sys

from luigi.scheduler import Scheduler, DONE

WORKER = "myworker"
CONF = {
    "retry_delay": 100,
    "remove_delay": 1000,
    "worker_disconnect_delay": 10,
    "disable_persist": 10,
    "disable_window": 10,
    "retry_count": 3,
    "disable_hard_timeout": 3600,
}

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    pattern = sys.argv[3]
    sch = Scheduler(**CONF)
    fam = "A" + tag
    sch.add_task_batcher(worker=WORKER, task_family=fam, batched_args=["a"])
    ready = []
    for i, ch in enumerate(pattern, 1):
        val = str(i)
        dep = "NOTDONE_" + tag if ch == "n" else "DONE_" + tag
        sch.add_task(
            worker=WORKER,
            task_id="%s_a_%d" % (fam, i),
            family=fam,
            params={"a": val},
            batchable=True,
            deps=[dep],
        )
        if ch == "r":
            ready.append(val)
    sch.add_task(worker=WORKER, task_id="NOTDONE_" + tag, runnable=False)
    sch.add_task(worker=WORKER, task_id="DONE_" + tag, status=DONE)
    got = sch.get_work(worker=WORKER)["task_params"].get("a", [])
    print("HARNESS_OK" if got == ready else "MISMATCH got=%r exp=%r" % (got, ready))
