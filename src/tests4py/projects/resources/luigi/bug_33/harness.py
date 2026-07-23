import sys

import luigi

if __name__ == "__main__":
    mode = sys.argv[1]
    v1 = sys.argv[2]
    v2 = sys.argv[3]

    class DummyTask(luigi.Task):
        x = luigi.Parameter()
        y = luigi.Parameter(significant=False)

    if mode == "pos":
        DummyTask(v1, v2)
    elif mode == "kw":
        DummyTask(v1, y=v2)
    else:  # allkw
        DummyTask(x=v1, y=v2)
    print("HARNESS_OK")
