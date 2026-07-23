import sys

import luigi.scheduler as scheduler


class _Cfg:
    def __init__(self, delay):
        self.worker_disconnect_delay = delay


if __name__ == "__main__":
    mode = sys.argv[1]
    worker_id = int(sys.argv[2])
    delay = int(sys.argv[3])
    if mode == "explicit":
        last_active = int(sys.argv[4])
        worker = scheduler.Worker(worker_id, last_active=last_active)
    else:
        worker = scheduler.Worker(worker_id)
    worker.prune(_Cfg(delay))
    print("HARNESS_OK")
