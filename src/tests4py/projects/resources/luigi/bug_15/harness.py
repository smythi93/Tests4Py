import sys
import time

from luigi.scheduler import CentralPlannerScheduler

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    status = mode.upper()
    w, up, tid = "AS_" + tag, "UP_" + tag, "T_" + tag
    time.time = lambda: 1
    sch = CentralPlannerScheduler(retry_delay=100000000000)
    sch.add_worker(w, [("assistant", True)])
    sch.ping(worker=w)
    sch.add_task(worker=up, task_id=tid, status=status)
    time.time = lambda: 100000
    sch.ping(worker=w)
    sch.prune()
    time.time = lambda: 200000
    sch.ping(worker=w)
    sch.prune()
    exists = tid in sch.task_list(None, "")
    print("HARNESS_OK" if not exists else "STILL_EXISTS")
