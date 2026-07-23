import sys
import time

from luigi.scheduler import CentralPlannerScheduler, FAILED, DISABLED

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    w, tid = "w_" + tag, "T_" + tag
    time.time = lambda: 0
    sch = CentralPlannerScheduler(disable_failures=2, disable_persist=100)
    if mode == "automanual":
        sch.add_task(worker=w, task_id=tid, status=FAILED)
        sch.add_task(worker=w, task_id=tid, status=FAILED)
        sch.add_task(worker=w, task_id=tid, status=DISABLED)
    else:
        sch.add_task(worker=w, task_id=tid, status=DISABLED)
    time.time = lambda: 101
    status = sch.task_list("", "")[tid]["status"]
    print("HARNESS_OK" if status == "DISABLED" else "STATUS:" + status)
