import sys

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]

    import luigi

    cls = type("MyTask_" + tag, (luigi.Task,), {"complete": lambda self: True})

    if mode == "none":
        sys.argv = ["harness", "--no-lock", "--local-scheduler"]
        luigi.run(main_task_cls=cls)
    else:
        luigi.run(
            cmdline_args=["--no-lock", "--local-scheduler"], main_task_cls=cls
        )
    print("HARNESS_OK")
