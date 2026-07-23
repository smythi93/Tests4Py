import sys

from luigi.contrib.spark import SparkSubmitTask

if __name__ == "__main__":
    mode = sys.argv[1]
    name = sys.argv[2]
    prop = sys.argv[3]
    val = sys.argv[4]
    if mode == "dict":
        value = {prop: val}
    else:
        value = {}
    print(repr(SparkSubmitTask._dict_arg(None, name, value)))
