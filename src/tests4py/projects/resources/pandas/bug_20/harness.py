import sys
import random
import pandas
from pandas.tseries.offsets import BMonthBegin, BMonthEnd, BQuarterBegin, BQuarterEnd, BYearBegin, BYearEnd, MonthBegin, MonthEnd, QuarterBegin, QuarterEnd, YearBegin, YearEnd

if __name__ == "__main__":
    assert len(sys.argv) == 3
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)
    n = random.choice([1, -2])
    rng_values = random.choice([0, -1])
    cls_value = random.choice(
            [MonthBegin, MonthEnd, BMonthBegin, BMonthEnd, QuarterBegin, QuarterEnd, BQuarterBegin,
             BQuarterEnd, YearBegin, YearEnd, BYearBegin, BYearEnd])

    dice = random.choice([0, 1])
    if dice == 0:
        offset = cls_value(n=n)
        rng = pandas.date_range(start=all_values[1], periods=int(all_values[0]), freq='T')
        ser = pandas.Series(rng)
        res = rng + offset
        res2 = ser + offset
        if res[0] == rng[0] + offset:
            print(all_values[0])
        else:
            print("OutOfBoundsDatetime")
    elif dice == 1:
        offset = cls_value(n=n)
        rng = pandas.date_range(start=all_values[1], periods=int(all_values[0]), freq='T')
        ser = pandas.Series(rng)
        res = rng + offset
        res2 = ser + offset
        if res2.iloc[0] == ser.iloc[0] + offset:
            print(all_values[0])
        else:
            print("OutOfBoundsDatetime")
    else:
        print("Wrong input")
