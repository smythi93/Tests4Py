import sys
from pandas._testing import assert_index_equal
from pandas import pandas


if __name__ == "__main__":
    assert len(sys.argv) == 10
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)
    midx1 = pandas.MultiIndex.from_product([all_values[5:7], all_values[7:9]], names=all_values[1:3])
    midx2 = pandas.MultiIndex.from_product([all_values[5:7], all_values[7:9]], names=all_values[3:5])
    join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
    assert_index_equal(midx1, join_idx)
    if lidx is None:
        print(all_values[0])
    else:
        print("Value Error: cannot join with no overlapping index names")
