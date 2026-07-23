import sys

import luigi.scheduler

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    tw, ow, tp, op = f"TW_{tag}", f"OW_{tag}", f"TP_{tag}", f"OP_{tag}"
    sch = luigi.scheduler.Scheduler()
    sch.add_task(worker=tw, task_id=tp, status="PENDING")
    sch.add_task(worker=ow, task_id=op, status="PENDING")
    if mode == "trigger":
        sch.add_task(worker=tw, task_id=f"DN_{tag}", status="DONE")
    else:
        sch.add_task(worker=ow, task_id=f"EP1_{tag}", status="PENDING")
        sch.add_task(worker=ow, task_id=f"EP2_{tag}", status="PENDING")
    st = sch._state
    target = st.get_worker(tw)
    got = {t.id for t in target.get_pending_tasks(st)}
    print("HARNESS_OK" if got == {tp} else "MISMATCH:" + repr(got))
