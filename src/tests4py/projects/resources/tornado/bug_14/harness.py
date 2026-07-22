import sys

from tornado.ioloop import IOLoop

if __name__ == "__main__":
    scenario = sys.argv[1]
    IOLoop.clear_current()
    loops = []
    raised = False
    try:
        if scenario == "SINGLE_TRUE":
            loops.append(IOLoop(make_current=True))
        elif scenario == "DEFAULT_THEN_TRUE":
            loops.append(IOLoop())
            loops.append(IOLoop(make_current=True))
        elif scenario == "MC_FALSE":
            loops.append(IOLoop(make_current=False))
        elif scenario == "DEFAULT":
            loops.append(IOLoop())
        elif scenario == "DOUBLE_DEFAULT":
            loops.append(IOLoop())
            loops.append(IOLoop())
    except RuntimeError:
        raised = True
    finally:
        for _loop in loops:
            try:
                _loop.close()
            except Exception:
                pass
        IOLoop.clear_current()
    print("RAISED" if raised else "OK")
