import sys

import luigi.configuration

if __name__ == "__main__":
    mode = sys.argv[1]
    config = luigi.configuration.get_config()
    if not config.has_section("scheduler"):
        config.add_section("scheduler")
    if mode == "on":
        config.set("scheduler", "record_task_history", "True")
    else:
        config.set("scheduler", "record_task_history", "False")

    from luigi.interface import _WorkerSchedulerFactory

    ls = _WorkerSchedulerFactory().create_local_scheduler()
    print(ls._config.record_task_history)
