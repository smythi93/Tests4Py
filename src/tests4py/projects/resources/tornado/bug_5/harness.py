import sys

from tornado.ioloop import PeriodicCallback


def simulate(pc, durations, now=1000):
    pc._next_timeout = now
    calls = []
    for d in durations:
        pc._update_next(now)
        calls.append(pc._next_timeout)
        now = pc._next_timeout + d
    return calls


if __name__ == "__main__":
    callback_time = int(sys.argv[1])
    durations = [int(x) for x in sys.argv[2:]]
    pc = PeriodicCallback(None, callback_time)
    calls = simulate(pc, durations)
    print([int(round(x)) for x in calls])
