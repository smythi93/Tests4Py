import sys

import luigi

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    cls_name = "Task_%s_%s" % (mode, tag)
    if mode == "insig":
        attrs = {
            "x": luigi.Parameter(),
            "y": luigi.Parameter(significant=False),
        }
        kwargs = {"x": "vx" + tag, "y": "vy" + tag}
    else:
        attrs = {
            "x": luigi.Parameter(),
            "z": luigi.Parameter(),
        }
        kwargs = {"x": "vx" + tag, "z": "vz" + tag}
    cls = type(cls_name, (luigi.Task,), attrs)
    original = cls(**kwargs)
    other = cls.from_str_params(original.to_str_params())
    assert original == other
    print("HARNESS_OK")
