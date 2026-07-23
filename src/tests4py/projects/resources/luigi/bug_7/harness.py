import sys

from luigi.scheduler import Scheduler

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
    x, y, a = "X_" + tag, "Y_" + tag, "A_" + tag
    newstatus = "UNKNOWN" if mode == "override" else "PENDING"
    sch = Scheduler(**CONF)
    sch.add_task(worker=x, task_id=a)
    sch.get_work(worker=x)
    sch.add_task(worker=y, task_id=a, status=newstatus)
    status = sch.task_list("", "")[a]["status"]
    print("HARNESS_OK" if status == "RUNNING" else "STATUS:" + status)
