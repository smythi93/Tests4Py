import sys

from ansible.utils.version import _Alpha, _Numeric

OPS = {
    "lt": lambda a, b: a < b,
    "le": lambda a, b: a <= b,
    "gt": lambda a, b: a > b,
    "ge": lambda a, b: a >= b,
    "eq": lambda a, b: a == b,
    "ne": lambda a, b: a != b,
}

if __name__ == "__main__":
    kind = sys.argv[1]
    a = sys.argv[2]
    b = sys.argv[3]
    op = sys.argv[4]
    if kind == "numeric":
        left, right = _Numeric(int(a)), _Numeric(int(b))
    else:
        left, right = _Alpha(a), _Alpha(b)
    print(OPS[op](left, right))
