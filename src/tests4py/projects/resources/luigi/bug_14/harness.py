import sys
import time

from luigi.scheduler import CentralPlannerScheduler, FAILED

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    w, a, b = "w_" + tag, "A_" + tag, "B_" + tag
    time.time = lambda: 1
    if mode == "hardonly":
        sch = CentralPlannerScheduler(retry_delay=5, disable_hard_timeout=100)
    else:
        sch = CentralPlannerScheduler(
            retry_delay=5, disable_hard_timeout=100, disable_failures=100
        )
    sch.add_worker(w, [])
    sch.ping(worker=w)
    time.time = lambda: 2
    sch.add_task(worker=w, task_id=a)
    sch.add_task(worker=w, task_id=b, deps=[a])
    sch.get_work(worker=w)
    sch.add_task(worker=w, task_id=a, status=FAILED)
    time.time = lambda: 10
    sch.prune()
    sch.get_work(worker=w)
    print("HARNESS_OK")
