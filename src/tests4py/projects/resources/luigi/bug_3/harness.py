import sys

import luigi

if __name__ == "__main__":
    mode = sys.argv[1]
    nums = [int(a) for a in sys.argv[2:]]
    if mode == "flat":
        the_tuple = tuple(nums)
    else:
        the_tuple = tuple((nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2))
    tp = luigi.TupleParameter()
    result = tp.parse(tp.serialize(the_tuple))
    print(repr(result))
