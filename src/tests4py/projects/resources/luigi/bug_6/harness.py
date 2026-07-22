import sys

import luigi

if __name__ == "__main__":
    ptype = sys.argv[1]
    shape = sys.argv[2]
    w1 = sys.argv[3]
    w2 = sys.argv[4]

    Param = luigi.ListParameter if ptype == "list" else luigi.TupleParameter
    if shape == "dicts":
        v = [{w1: w2}, {w2: w1}]
    elif shape == "nested":
        v = [[w1, w2], [w2, w1]]
    else:
        v = [w1, w2]
    if ptype == "tuple":
        v = tuple(tuple(e) if isinstance(e, list) else e for e in v)

    class DummyTask(luigi.Task):
        args = Param()

    inst = DummyTask(args=v)
    hash(inst.args)
    print("HARNESS_OK")
