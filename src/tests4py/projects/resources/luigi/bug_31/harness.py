import sys

from luigi.scheduler import CentralPlannerScheduler, DONE

CONF = {
    "retry_delay": 100,
    "remove_delay": 1000,
    "worker_disconnect_delay": 10,
    "disable_persist": 10,
    "disable_window": 10,
    "disable_failures": 3,
}

if __name__ == "__main__":
    mode = sys.argv[1]
    owner = sys.argv[2]
    task = sys.argv[3]
    asst = sys.argv[4]
    sch = CentralPlannerScheduler(**CONF)
    if mode == "external":
        sch.add_task(owner, task_id=task, runnable=False)
    else:
        sch.add_task(owner, task_id=task, status=DONE)
    r = sch.get_work(asst, assistant=True)
    print("HARNESS_OK" if r["task_id"] is None else "GOTTASK:" + str(r["task_id"]))
