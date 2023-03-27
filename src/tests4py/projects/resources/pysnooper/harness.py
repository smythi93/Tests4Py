import argparse
import sys

# noinspection PyUnresolvedReferences
from pysnooper import snoop

if __name__ == "__main__":
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-o", dest="output", default=None, nargs="?", const=1)
    arguments.add_argument("-v", dest="variables", default=None)
    arguments.add_argument("-d", dest="depth", default=None, type=int)
    arguments.add_argument("-p", dest="prefix", default=None)
    arguments.add_argument("-w", dest="watch", default=None)
    arguments.add_argument("-c", dest="custom_repr", default=None)
    arguments.add_argument("-O", dest="overwrite", default=None, action="store_true")
    arguments.add_argument("-T", dest="thread_info", default=None, action="store_true")

    args = arguments.parse_args()

    parameters = dict()

    if args.output is not None:
        if args.output == 1:
            parameters["output"] = sys.stdout
        else:
            parameters["output"] = args.output
    if args.variables is not None:
        parameters["variables"] = tuple(args.variables.split(","))
    if args.depth is not None:
        parameters["depth"] = args.depth
    if args.prefix is not None:
        parameters["prefix"] = args.prefix
    if args.watch is not None:
        parameters["watch"] = tuple(args.watch.split(","))
    if args.custom_repr is not None:
        custom_reprs = tuple(
            [
                tuple([eval(pred) for pred in custom_repr.split("=")])
                for custom_repr in args.custom_repr.split(",")
            ]
        )
        if len(custom_reprs) == 1:
            custom_reprs = custom_reprs[0]
        parameters["custom_repr"] = custom_reprs
    if args.overwrite is not None:
        parameters["overwrite"] = True
    if args.thread_info is not None:
        parameters["thread_info"] = True

    @snoop(**parameters)
    def test(x, z):
        if x < 0:
            y = -x
        else:
            y = x + 1
        for i in range(len(z)):
            x += y
        return x

    test(3, "test")
