from tests4py import sfl

if __name__ == "__main__":
    # t4p.checkout(t4p.calculator_1)
    # r = sfl.sflkit_instrument("tmp/sfl", t4p.calculator_1, events="line")
    # if r.raised:
    #    raise r.raised
    # r = sfl.sflkit_systemtest(work_dir="tmp/sfl", tests="tests4py_systemtest_diversity")
    # if r.raised:
    #    raise r.raised
    r = sfl.sflkit_analyze(
        work_dir="tmp/sfl",
        suggestions=True,
        predicates="line",
        metrics="Ochiai,Tarantula",
    )
    if r.raised:
        raise r.raised
