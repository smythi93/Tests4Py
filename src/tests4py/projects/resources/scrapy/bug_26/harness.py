import sys

# noinspection PyUnresolvedReferences
from scrapy.settings import BaseSettings

if __name__ == "__main__":
    mode = sys.argv[1]
    b1 = int(sys.argv[2])
    b2 = int(sys.argv[3])
    v3 = int(sys.argv[4])
    x1 = int(sys.argv[5])
    if mode == "override":
        test_sub = BaseSettings({1: x1}, "default")
    else:
        test_sub = BaseSettings()
    s = BaseSettings({"TEST_BASE": {1: b1, 2: b2}, "TEST": test_sub})
    s["TEST"].set(3, v3, priority="project")
    try:
        cs = s._getcomposite("TEST")
        items = sorted((int(k), int(cs[k])) for k in cs)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + repr(items))
