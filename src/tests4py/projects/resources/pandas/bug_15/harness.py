import sys
from pandas._testing import assert_index_equal, round_trip_pickle
from pandas import date_range

if __name__ == "__main__":
    assert len(sys.argv) == 7
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if all_values[5] == "None":
        dti_with_freq = None
    else:
        dti_with_freq = "infer"
    dti = date_range(all_values[1], periods=int(all_values[2]), tz=all_values[3], name=all_values[4])
    dti = dti._with_freq(dti_with_freq)
    res = round_trip_pickle(dti)
    if assert_index_equal(res, dti) is None:
        print(all_values[0])
    else:
        print("AssertionError: assert d.pop(key) == getattr(dta, key)")
