import sys
import time

from luigi.scheduler import CentralPlannerScheduler, FAILED

CONF = {
    "retry_delay": 100,
    "remove_delay": 1000,
    "worker_disconnect_delay": 10,
    "disable_persist": 10,
    "disable_window": 10,
    "disable_failures": 3,
    "disable_hard_timeout": 3600,
}

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    w, tid = "W_" + tag, "A_" + tag
    time.time = lambda: 0
    sch = CentralPlannerScheduler(**CONF)
    if mode == "assistant":
        sch.add_worker(w, [("assistant", True)])
        sch.add_task(worker=w, task_id=tid, status=FAILED, assistant=True)
    else:
        sch.add_task(worker=w, task_id=tid, status=FAILED)
    time.time = lambda: 101
    sch.ping(worker=w)
    status = sch.task_list("", "")[tid]["status"]
    print("HARNESS_OK" if status == "PENDING" else "STATUS:" + status)
