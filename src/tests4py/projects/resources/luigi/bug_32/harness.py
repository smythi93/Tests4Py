import sys

import luigi


def build_value(kind, w1, w2):
    if kind == "dict":
        return {w1: w2}
    if kind == "tuple":
        return (w1, w2)
    if kind == "list":
        return [w1, w2]
    if kind == "set":
        return {w1, w2}
    return w1  # str


if __name__ == "__main__":
    kind = sys.argv[1]
    w1 = sys.argv[2]
    w2 = sys.argv[3]

    class DummyTask(luigi.Task):
        x = luigi.Parameter()

    DummyTask(x=build_value(kind, w1, w2))
    print("HARNESS_OK")
