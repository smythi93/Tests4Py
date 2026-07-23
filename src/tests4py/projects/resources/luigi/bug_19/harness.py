import sys
import time

from luigi.scheduler import CentralPlannerScheduler, FAILED

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    w, tid = "w_" + tag, "T_" + tag
    df = 1 if mode == "reenable" else 1000
    time.time = lambda: 0
    sch = CentralPlannerScheduler(disable_failures=df, disable_persist=100)
    sch.add_task(worker=w, task_id=tid, status=FAILED)
    time.time = lambda: 101
    status = sch.task_list("", "")[tid]["status"]
    print("HARNESS_OK" if status == "FAILED" else "STATUS:" + status)
